python early hide:

    def parse_chat_stmt(l):

        who = l.simple_expression()
        what = l.simple_expression()

        if not who or not what:
            renpy.error("chat requires a speaker and some dialogue")

        ffont = 'sser1'
        pv = "None"
        bold = False
        xbold = False
        big = False
        img = False
        bounce = False
        spec_bubble = None

        bubble_list = ['cloud_l', 'cloud_m', 'cloud_s', 'round_l', 'round_m',
                    'round_s', 'sigh_l', 'sigh_m', 'sigh_s', 'spike_l', 'spike_m',
                    'spike_s', 'square_l', 'square_m', 'square_s', 'square2_l',
                    'square2_m', 'square2_s', 'round2_l', 'round2_m', 'round2_s',
                    'flower_l', 'flower_m', 'flower_s', 'glow2']
        
        font_list = ['sser1', 'sser2', 'ser1', 'ser2', 'curly','blocky']
        
        while True:

            if l.eol():
                break

            if l.keyword('font'):
                ffont = l.simple_expression()
                if ffont is None:
                    renpy.error('expected font for chat argument')  
                if ffont not in font_list:
                    renpy.error("given font %s is not recognized in chat CDS" % ffont)
                continue
            if l.keyword('pv'):
                pv = l.simple_expression()
                if pv is None:
                    renpy.error('expected simple expression for pv value')
                continue

            if l.keyword('bold'):
                bold = True
                xbold = False
                continue
            if l.keyword('xbold'):
                xbold = True
                bold = False
                continue
            if l.keyword('img'):
                img = True
                bounce = False
                continue
            if l.keyword('bounce'):
                bounce = True
                continue
            if l.keyword('big'):
                big = True
                continue

            item = l.simple_expression()
            if item in bubble_list:
                spec_bubble = item
                bounce = True
                continue

            if item in font_list:
                ffont = item
                continue

            renpy.error("couldn't recognize chat argument")

        return dict(who=who,
                    what=what,
                    pv=pv,
                    ffont=ffont,
                    bold=bold,
                    xbold=xbold,
                    big=big,
                    img=img,
                    bounce=bounce,
                    spec_bubble=spec_bubble)


    def execute_chat_stmt(p):
        try:
            who = eval(p["who"])       
            what = eval(p["what"])        
            pv = eval(p["pv"])
            ffont = p["ffont"]            
            bold = p["bold"]
            xbold = p["xbold"]        
            big = p["big"]
            img = p["img"]        
            bounce = p["bounce"]        
            spec_bubble = p["spec_bubble"]
        except:
            renpy.error("Could not parse arguments of chat CDS")
            return

        # Double-check 'who' is a ChatCharacter
        if not isinstance(who, ChatCharacter):
            print("WARNING: The ChatCharacter %s for dialogue", what, "could not",
                "be evaluated." % p['who'])
            renpy.show_screen('script_error',
                    message=("The ChatCharacter %s for dialogue " + what 
                        + " could not be evaluated." % p['who']),
                    link="Adding-a-New-Character-to-Chatrooms",
                    link_text="Adding a New Character to Chatrooms")
            return

        # Construct the actual "what" statement
        dialogue = what
        # First, the size
        if big:
            dialogue = "{size=+10}" + dialogue + "{/size}"
        
        # Next, construct the font
        d_font = ffont
        extra_item = False
        if bold and ffont in ['sser1', 'sser2', 'ser1', 'ser2']:
            d_font = d_font + 'b'
        elif xbold and ffont in ['sser1', 'sser2', 'ser1', 'ser2']:
            d_font = d_font + 'xb'
        elif (bold or xbold) and ffont in ['curly', 'blocky']:
            extra_item = 'b'        

        # Add the font around the dialogue, unless it's the default
        if d_font != 'sser1':
            dialogue = "{=" + d_font + "}" + dialogue + "{/=" + d_font + "}"
        if extra_item:
            dialogue = ("{" + extra_item + "}" + dialogue + "{/" 
                + extra_item + "}")
        
        # There is a special bubble; check if need to correct it
        if (spec_bubble and spec_bubble[:7] == "round"
                and (who.file_id == 'r' or who.file_id == 'z')):
            # Correct this to the new 'flower' variant if applicable
            spec_bubble = "flower_" + spec_bubble[-1:]

        if what in store.emoji_lookup:
            # Automatically set img to True
            img = True
        
        # Add an entry to the replay_log if the player is not observing
        # this chat
        if not store.observing:
            new_pv = pv
            # For replays, MC shouldn't reply instantly
            if who.right_msgr and new_pv == 0:
                new_pv = None
                store.current_chatroom.replay_log.append(ReplayEntry(
                        who, dialogue, new_pv, img, bounce, spec_bubble))
            
        # Now add this dialogue to the chatlog
        addchat(who, dialogue, pauseVal=pv, img=img, bounce=bounce,
            specBubble=spec_bubble)
        
        return

    def lint_chat_stmt(p):
        return
    
    def predict_chat_stmt(p):
        return [ ]
    
    def warp_chat_stmt(p):
        return True
    

    renpy.register_statement('chat',
        parse=parse_chat_stmt,
        execute=execute_chat_stmt,
        predict=predict_chat_stmt,
        lint=lint_chat_stmt,
        warp=warp_chat_stmt)

    ## Creator-defined statements for awarding and rescinding heart points
    def parse_award_heart(l):

        who = l.simple_expression()
        if not who:
            renpy.error("award heart requires a person to award the heart to.")

        bad = False

        while True:
            if l.eol():
                break
            if l.keyword('bad'):
                bad = True
                continue
            
            renpy.error("Could not parse statement.")

        return dict(who=who, bad=bad)

    def execute_award_heart(p):

        if p["who"] is not None:
            who = eval(p["who"])
        else:
            renpy.error("award heart requires a ChatCharacter the heart belongs to")
        
        if who is None or not isinstance(who, ChatCharacter):
            print("WARNING: variable %s provided to award heart is not recognized as a ChatCharacter." % p["who"])
            renpy.show_screen('script_error',
                message="Variable %s provided to award heart is not recognized as a ChatCharacter.",
                link="Useful-Chatroom-Functions#how-to-show-a-heart-icon",
                link_text="How to show a heart icon")
            return
        

        bad = p["bad"]

        # This is during a chatroom or a real-time text conversation
        if store.text_person is None or store.text_person.real_time_text:
            try:
                if not store.observing:
                    who.increase_heart(bad)
                    if store.text_person is None:
                        store.chatroom_hp += 1
                    store.persistent.HP += 1

                    # Saeran and Ray share the same heart points
                    if who == store.r:
                        store.sa.increase_heart(bad)
                    elif who == store.sa:
                        store.r.increase_heart(bad)

                    if store.persistent.animated_icons:
                        renpy.show_screen(allocate_heart_screen(), character=who)
                    else:
                        msg = who.name + " +1"
                        renpy.show_screen(allocate_notification_screen(True), msg)                    
            except:
                print("WARNING: Heart could not be awarded for %s." % p["who"])
                renpy.show_screen('script_error',
                    message="Heart could not be awarded for " + p["who"],
                    link="Useful-Chatroom-Functions#how-to-show-a-heart-icon",
                    link_text="How to show a heart icon")
                return
        # This is during a regular text message
        else:
            add_heart(store.text_person, who, bad)
        return
        
            
    def predict_award_heart(p):
        return [ ]
    
    def warp_award_heart(p):
        return True

    def lint_award_heart(p):

        who = p["who"]
        eval_who = None
        try:
            eval_who = eval(p["who"])
        except:
            renpy.error("heart functions require a ChatCharacter the heart belongs to")

        if eval_who is None:
            renpy.error("The person the heart belongs to cannot be None.")
        
        if not isinstance(eval_who, ChatCharacter):
            renpy.error("%s is not recognized as a ChatCharacter object for the heart icon." % p["who"])
        
        return

    renpy.register_statement('award heart',
        parse=parse_award_heart,
        execute=execute_award_heart,
        predict=predict_award_heart,
        lint=lint_award_heart,
        warp=warp_award_heart)

    def parse_break_heart(l):
        who = l.simple_expression()
        return dict(who=who)        

    def execute_break_heart(p):
        if p["who"] is not None:
            who = eval(p["who"])
        else:
            renpy.error("break heart requires a ChatCharacter the heart belongs to")
        
        if who is None or not isinstance(who, ChatCharacter):
            print("WARNING: variable %s provided to break heart is not recognized as a ChatCharacter." % p["who"])
            renpy.show_screen('script_error',
                message="Variable %s provided to break heart is not recognized as a ChatCharacter.",
                link="Useful-Chatroom-Functions#how-to-show-a-heart-icon",
                link_text="How to show a heart icon")
            return
        
        if not store.observing:
            who.decrease_heart()
            if who == store.sa:
                r.decrease_heart()
            elif who == store.r:
                sa.decrease_heart()

            if store.text_person is None:
                store.chatroom_hp -= 1
            store.persistent.HP -= 1

            if store.persistent.animated_icons:
                renpy.show_screen('heart_break_screen', character=who)
            else:
                msg = who.name + " -1"
                renpy.show_screen(allocate_notification_screen(True), msg)
        return

    renpy.register_statement('break heart',
        parse=parse_break_heart,
        execute=execute_break_heart,
        predict=predict_award_heart,
        lint=lint_award_heart,
        warp=warp_award_heart)

    # This duplicates the above statement, just switches the words to account
    # for possible error checking.
    renpy.register_statement('heart break',
        parse=parse_break_heart,
        execute=execute_break_heart,
        predict=predict_award_heart,
        lint=lint_award_heart,
        warp=warp_award_heart)

    # Definitions that allow you to write `invite guest` in Ren'Py script
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
            print("WARNING: Invited guest is not recognized as a Guest object.")
            renpy.show_screen('script_error',
                message="Invited guest %s is not recognized as a Guest object." % p["guest"],
                link="Inviting-a-Guest", link_text="Inviting a Guest") 
            return
        elif guest is None:
            print("WARNING: Invited guest cannot be None.")
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

