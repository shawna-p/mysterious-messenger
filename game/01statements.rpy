python early hide:


    def parse_invite_guest(l):
        guest = l.simple_expression()
        if not guest:
            renpy.error("invite requires a guest to invite")

        return dict(guest=guest)
    
    def execute_invite_guest(p):

        if p["guest"] is not None:
            guest = eval(p["guest"])
        else:
            renpy.error("invite requires a guest to invite.")

        if not isinstance(guest, Guest):
            print("Invited guest is not recognized as a Guest object.")
            renpy.show_screen('script_error',
                message="Invited guest %s is not recognized as a Guest object." % p["guest"],
                link="Inviting-a-Guest", link_text="Inviting a Guest") 
            return
        elif guest is None:
            print("Invited guest cannot be None.")
            renpy.show_screen('script_error', message="Invited guest cannot be None.",
                link="Inviting-a-Guest", link_text="Inviting a Guest") 
            return


        # So you can't re-invite a guest while replaying a chatroom
        if not store.observing or store.persistent.testing_mode:
            try:
                guest.sent_time = upTime()
                # Add them to the front of the email inbox
                store.email_list.insert(0, Email(guest, guest.start_msg, guest.label1))
                # The player has encountered the guest so the guestbook can be
                # updated
                if not store.persistent.guestbook[guest.name]:
                    store.persistent.guestbook[guest.name] = "seen"
            except:
                print("WARNING: Guest %s could not be invited." % p["guest"])
                renpy.show_screen('script_error',
                    message="Guest %s could not be invited." % p["guest"],
                    link="Inviting-a-Guest", link_text="Inviting a Guest")

        return

    def predict_invite_guest(p):
        return [ ]

    def lint_invite_guest(p):

        guest = p["guest"]
        eval_guest = None

        try:
            eval_guest = eval(p["guest"])
        except:
            renpy.error("invite requires a guest to invite.")

        if eval_guest is None:
            renpy.error("Invited guest cannot be None.")        

        if not isinstance(eval_guest, Guest):
            renpy.error("Invited guest %s is not recognized as a Guest object." % p["guest"])

        return
    
    def warp_invite_guest(p):        
        return True

    renpy.register_statement('invite',
        parse=parse_invite_guest,
        execute=execute_invite_guest,
        predict=predict_invite_guest,
        lint=lint_invite_guest,
        warp=warp_invite_guest)



    # These statements replace Ren'Py's default `play music` and `play sound`
    # implementations so they are compatible with audio captions.
    def warp_audio(p):
        """
        Determines if we should play this statement while warping.
        """

        if p.get("channel", None) is not None:
            channel = eval(p["channel"])
        else:
            channel = "music"

        return renpy.music.is_music(channel)

    def parse_play_music(l):

        file = l.simple_expression()
        if not file:
            renpy.error("play requires a file")

        fadeout = "None"
        fadein = "0"
        channel = None
        loop = None
        if_changed = False
        captions = True

        while True:

            if l.eol():
                break

            if l.keyword('fadeout'):
                fadeout = l.simple_expression()
                if fadeout is None:
                    renpy.error('expected simple expression')

                continue

            if l.keyword('fadein'):
                fadein = l.simple_expression()
                if fadein is None:
                    renpy.error('expected simple expression')

                continue

            if l.keyword('channel'):
                channel = l.simple_expression()
                if channel is None:
                    renpy.error('expected simple expression')

                continue

            if l.keyword('loop'):
                loop = True
                continue

            if l.keyword('noloop'):
                loop = False
                continue

            if l.keyword('if_changed'):
                if_changed = True
                continue
            
            if l.keyword('nocaption'):
                captions = False
                continue

            renpy.error('could not parse statement.')

        return dict(file=file,
                    fadeout=fadeout,
                    fadein=fadein,
                    channel=channel,
                    loop=loop,
                    if_changed=if_changed,
                    captions=captions)


    def execute_play_c_music(p):

        if p["channel"] is not None:
            channel = eval(p["channel"])
        else:
            channel = "music"

        captions = p["captions"]

        if captions:
            try:
                notification =  ("♪ " + 
                        store.music_dictionary[getattr(store, p["file"])]
                        + " ♪")
                if store.persistent.audio_captions:
                    renpy.show_screen('notify', notification)
            except (KeyError, AttributeError) as e:
                renpy.show_screen('script_error',
                    message="No Audio Caption defined for %s" % p["file"],
                    link="Adding-Music-and-SFX", link_text="Adding Music and SFX") 
                print("WARNING: No Audio Caption defined for " + p["file"])
            
            if (not store.observing and not store.persistent.testing_mode
                    and not store.vn_choice):
                # Add this music to the replay_log
                try:
                    music_entry = ("play music", getattr(store, p["file"]))
                except AttributeError:
                    music_entry = ("play music", p["file"])
                store.current_chatroom.replay_log.append(music_entry)
        
        renpy.music.play(_audio_eval(p["file"]),
                         fadeout=eval(p["fadeout"]),
                         fadein=eval(p["fadein"]),
                         channel=channel,
                         loop=p.get("loop", None),
                         if_changed=p.get("if_changed", False))
    
    def predict_play_music(p):
        return [ ]

    def lint_play_music(p, channel="music"):

        file = _try_eval(p["file"], 'filename')

        if p["channel"] is not None:
            channel = _try_eval(p["channel"], 'channel')

        if not isinstance(file, list):
            file = [ file ]

        for fn in file:
            if isinstance(fn, basestring):
                try:
                    if not renpy.music.playable(fn, channel):
                        renpy.error("%r is not loadable" % fn)
                except:
                    pass

    renpy.register_statement('play music',
        parse=parse_play_music,
        execute=execute_play_c_music,
        predict=predict_play_music,
        lint=lint_play_music,
        warp=warp_audio)

    def warp_sound(p):
        """
        Determines if we should play this statement while warping.
        """

        if p.get("channel", None) is not None:
            channel = eval(p["channel"])
        else:
            channel = "sound"

        return renpy.music.is_music(channel)

    def lint_play_sound(p, lint_play_music=lint_play_music):
        return lint_play_music(p, channel="sound")

    def execute_play_c_sound(p):

        if p["channel"] is not None:
            channel = eval(p["channel"])
        else:
            channel = "sound"

        fadeout = eval(p["fadeout"]) or 0
        captions = p["captions"]

        loop = p.get("loop", False)

        if loop is None:
            loop = config.default_sound_loop

        if captions:
            try:
                notification = ("SFX: " + 
                        store.sfx_dictionary[getattr(store, p["file"])])
                if store.persistent.audio_captions:
                    renpy.show_screen('notify', notification)
            except (KeyError, AttributeError) as e:
                renpy.show_screen('script_error',
                    message="No Audio Caption defined for %s" % p["file"],
                    link="Adding-Music-and-SFX", link_text="Adding Music and SFX")                
                print("WARNING: No Audio Caption defined for " + p["file"])


        renpy.sound.play(_audio_eval(p["file"]),
                         fadeout=fadeout,
                         fadein=eval(p["fadein"]),
                         loop=loop,
                         channel=channel)

    
    renpy.register_statement('play sound',
                              parse=parse_play_music,
                              execute=execute_play_c_sound,
                              lint=lint_play_sound,
                              warp=warp_sound)

