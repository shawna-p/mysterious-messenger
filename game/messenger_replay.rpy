#************************************
# Chatroom Enter/Exit
#************************************
# This does some of the code for you when you want a character
# to enter/exit a chatroom. It adds characters to the chatroom's
# participant list if they enter during a chatroom.

label enter(chara):

    $ mystring = chara.name + " has entered the chatroom."
    if (not observing and not persistent.testing_mode
            and not vn_choice
            and renpy.get_screen('phone_overlay')):
        $ enter_entry = ("enter", chara)
        $ current_chatroom.replay_log.append(enter_entry)
    
    $ addchat(special_msg, mystring, pv)
    if chara.name not in in_chat:
        $ in_chat.append(chara.name)
    
    if not observing:
        $ current_chatroom.add_participant(chara)
    
    $ renpy.restart_interaction()
    return
    
label exit(chara):
    if (not observing and not persistent.testing_mode
            and not vn_choice
            and renpy.get_screen('phone_overlay')):
        $ exit_entry = ("exit", chara)
        $ current_chatroom.replay_log.append(exit_entry)

    $ mystring = chara.name + " has left the chatroom."    
    $ addchat(special_msg, mystring, pv)
    if chara.name in in_chat:
        $ in_chat.remove(chara.name)
    $ renpy.restart_interaction()
    return

#************************************
# Play audio/music/SFX
#************************************
# This allows the program to keep track of when to play
# music during a chatroom or VN
label play_music(file):
    play music file loop
    if persistent.audio_captions:
        $ notification = ("♪ " + 
                music_dictionary[renpy.sound.get_playing('music')] + " ♪")
        show screen notify(notification)
    if (not observing and not persistent.testing_mode
            and not vn_choice):
        # Add this music to the replay_log
        $ music_entry = ("play music", file)
        $ current_chatroom.replay_log.append(music_entry)
    return

#************************************
# Screen Shake
#************************************
# This allows the program to keep track of when it should
# shake the screen during a chatroom
label shake():
    if persistent.screenshake:
        show expression current_background at shake
    if (not observing and not persistent.testing_mode
            and not vn_choice
            and renpy.get_screen('phone_overlay')):
        # Add this shake to the replay_log
        $ shake_entry = ("shake", current_background)
        $ current_chatroom.replay_log.append(shake_entry)
    return

#************************************
# Hacking effects
#************************************
# This allows the program to keep track of the different
# "hacking" effects used during a playthrough
label invert_screen(t=0, p=0):
    if persistent.hacking_effects:
        if t != 0:
            show screen invert(t)
        else:
            show screen invert()
    if (not observing and not persistent.testing_mode
            and not vn_choice
            and renpy.get_screen('phone_overlay')):
        # Add this to the replay_log
        if t == 0:
            $ tlen = False
        else:
            $ tlen = t
        $ effect_entry = ("invert", tlen)
        $ current_chatroom.replay_log.append(effect_entry)
        if p != 0:
            $ current_chatroom.replay_log.append(("pause", p))
    if p != 0 and persistent.hacking_effects:
        pause p
    return

label white_square_screen(t=0, p=0):
    if persistent.hacking_effects:
        if t != 0:
            show screen white_squares(t)
        else:
            show screen white_squares()
    if (not observing and not persistent.testing_mode
            and not vn_choice
            and renpy.get_screen('phone_overlay')):
        # Add this to the replay_log
        if t == 0:
            $ tlen = False
        else:
            $ tlen = t
        $ effect_entry = ("white squares", tlen)
        $ current_chatroom.replay_log.append(effect_entry)
        if p != 0:
            $ current_chatroom.replay_log.append(("pause", p))
    if p != 0 and persistent.hacking_effects:
        pause p
    return

label hack_rectangle_screen(t=0, p=0):
    if persistent.hacking_effects:
        if t != 0:
            show screen hack_rectangle(t)
        else:
            show screen hack_rectangle()
    if (not observing and not persistent.testing_mode
            and not vn_choice
            and renpy.get_screen('phone_overlay')):
        # Add this to the replay_log
        if t == 0:
            $ tlen = False
        else:
            $ tlen = t
        $ effect_entry = ("hack squares", tlen)
        $ current_chatroom.replay_log.append(effect_entry)
        if p != 0:
            $ current_chatroom.replay_log.append(("pause", p))
    if p != 0 and persistent.hacking_effects:
        pause p
    return 

label tear_screen(number=40, offtimeMult=0.4, ontimeMult=0.2, 
                        offsetMin=-10, offsetMax=30, w_timer=0.2,
                        p=0):
    if persistent.hacking_effects:
        show screen tear(number=number, offtimeMult=offtimeMult, 
                        ontimeMult=ontimeMult, offsetMin=offsetMin, 
                        offsetMax=offsetMax, w_timer=w_timer)

    if (not observing and not persistent.testing_mode
            and not vn_choice
            and renpy.get_screen('phone_overlay')):
        # Add this to the replay_log
        $ effect_entry = ("tear", [number, offtimeMult, ontimeMult, offsetMin, 
                                    offsetMax, w_timer])
        $ current_chatroom.replay_log.append(effect_entry)
        if p != 0:
            $ current_chatroom.replay_log.append(("pause", p))
    if p != 0 and persistent.hacking_effects:
        pause p
    return 

label remove_entries(num=1):
    $ num *= -1
    if (not observing and not persistent.testing_mode
            and not vn_choice
            and renpy.get_screen('phone_overlay')):
        # Add this to the replay_log
        $ remove_entry = ("remove", num)
        $ current_chatroom.replay_log.append(remove_entry)
    $ del chatlog[num:]
    return

#************************************
# Chatroom Replay (in-game)
#************************************
default chatroom_replay_index = 0
default replay_from = 0

## This label is called when you replay a chatroom
label rewatch_chatroom():
    stop music
    $ chatlog = []

    # Show the messenger screens
    hide screen starry_night
    show screen phone_overlay
    show screen messenger_screen 
    show screen pause_button
    
    # Hide all the popup screens
    $ hide_all_popups()
    
    $ text_person = None
    window hide
    $ text_msg_reply = False
    $ in_phone_call = False
    $ vn_choice = False
    $ email_reply = False
    
    $ chatroom_replay_index = 0
    $ replay_from = 0
    # Fill the beginning of the screen with 'empty space' 
    # so the messages begin showing up at the bottom of the 
    # screen (otherwise they start at the top)
    $ addchat(filler, "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", 0)
        
    python:
        in_chat = []
        for person in current_chatroom.original_participants:
            if person.name not in in_chat:
                in_chat.append(person.name)
            
        # If the player participated, add them to the list of
        # people in the chat
        if (not current_chatroom.expired 
                or current_chatroom.buyback 
                or current_chatroom.buyahead):
            in_chat.append(m.name)

    # Set a generic background just in case
    scene bg black

    jump chatroom_replay

label chatroom_replay():
    # Now start the loop to iterate through the replay_log
    python:
        for i, entry in enumerate(current_chatroom.replay_log[replay_from:]):
            chatroom_replay_index += 1
            if isinstance(entry, ReplayEntry):
                # pop it through the addchat function
                addchat(entry.who, entry.what, entry.pauseVal,
                    entry.img, entry.bounce, entry.specBubble)
            elif isinstance(entry, tuple):
                # It's some kind of command; determine what to do
                # based on what the command and given info is
                first = entry[0]
                second = entry[1]
                if first == "banner":
                    if persistent.banners:
                        renpy.show_screen('banner_screen', banner=second)
                elif first == "vn jump":
                    # The chatroom jumps to a VN section
                    # renpy.pause(pv*2.0)
                    renpy.call('vn_during_chat', second[0], second[1], 
                                        second[2], second[3])
                
                elif first == "hack":
                    if persistent.hacking_effects:
                        if second == "regular":
                            renpy.show_screen('hack_screen', 
                                                hack='hack scroll')
                            # The program checks to make sure the hack 
                            # screen is still showing so that it should 
                            # continue to pause
                            if (not renpy.is_skipping()
                                    and renpy.get_screen("hack_screen")):
                                renpy.pause(0.5, hard=False)
                            if (not renpy.is_skipping()
                                    and renpy.get_screen("hack_screen")):
                                renpy.pause(0.5, hard=False)
                            if (not renpy.is_skipping()
                                    and renpy.get_screen("hack_screen")):
                                renpy.pause(0.5, hard=False)
                            if (not renpy.is_skipping()
                                    and renpy.get_screen("hack_screen")):
                                renpy.pause(0.5, hard=False)
                            if (not renpy.is_skipping()
                                    and renpy.get_screen("hack_screen")):
                                renpy.pause(0.5, hard=False)
                            if (not renpy.is_skipping()
                                    and renpy.get_screen("hack_screen")):
                                renpy.pause(0.5, hard=False)
                            renpy.hide_screen('hack_screen')
                        elif second == "red":
                            renpy.show_screen('hack_screen', 
                                                hack='redhack scroll')
                            if (not renpy.is_skipping()
                                    and renpy.get_screen("hack_screen")):
                                renpy.pause(0.5, hard=False)
                            if (not renpy.is_skipping()
                                    and renpy.get_screen("hack_screen")):
                                renpy.pause(0.5, hard=False)
                            if (not renpy.is_skipping()
                                    and renpy.get_screen("hack_screen")):
                                renpy.pause(0.5, hard=False)
                            if (not renpy.is_skipping()
                                    and renpy.get_screen("hack_screen")):
                                renpy.pause(0.5, hard=False)
                            if (not renpy.is_skipping()
                                    and renpy.get_screen("hack_screen")):
                                renpy.pause(0.5, hard=False)
                            if (not renpy.is_skipping()
                                    and renpy.get_screen("hack_screen")):
                                renpy.pause(0.5, hard=False)
                            renpy.hide_screen('hack_screen')
                elif first == "play music":
                    renpy.music.play(second, channel='music', loop=True)
                    if persistent.audio_captions:
                        notification = ("♪ " + 
                            music_dictionary[renpy.sound.get_playing('music')] 
                            + " ♪")
                        renpy.show_screen('notify', notification)
                elif first == "shake":
                    current_background = second
                    if persistent.screenshake:
                        renpy.show(second, at_list=[shake])
                elif first == "enter":
                    mystring = second.name + " has entered the chatroom."
                    addchat(special_msg, mystring, pv)
                    if second.name not in in_chat:
                        in_chat.append(second.name)
                    renpy.restart_interaction()
                elif first == "exit":
                    mystring = second.name + " has left the chatroom."
                    addchat(special_msg, mystring, pv)
                    if second.name in in_chat:
                        in_chat.remove(second.name)
                    renpy.restart_interaction()
                elif first == "background":
                    renpy.scene()
                    current_background = second
                    renpy.show('bg ' + second)
                    if (persistent.animated_backgrounds
                            and second in ['morning', 'noon', 'evening',
                                           'night', 'earlyMorn']):
                        renpy.show_screen('animated_' + second)
                    elif (persistent.animated_backgrounds
                            and second == 'redhack'):
                        renpy.show_screen('animated_hack_background', red=True)
                    elif (persistent.animated_backgrounds
                            and second == 'hack'):
                        renpy.show_screen('animated_hack_background')
                    
                    if second in ['morning', 'noon', 'evening']:
                        nickColour = black
                    else:
                        nickColour = white
                elif first == "invert":
                    if persistent.hacking_effects:
                        renpy.show_screen('invert', w_timer=second)
                elif first == "pause":
                    if not renpy.is_skipping():
                        renpy.pause(second, hard=False)
                    else:
                        pass
                elif first == "white squares":
                    if persistent.hacking_effects:
                        renpy.show_screen('white_squares', w_timer=second)
                elif first == "hack squares":
                    if persistent.hacking_effects:
                        renpy.show_screen('hack_rectangle', w_timer=second)
                elif first == "tear":
                    if persistent.hacking_effects:
                        renpy.show_screen('tear', number=second[0],
                            offtimeMult=second[1], ontimeMult=second[2],
                            offsetMin=second[3], offsetMax=second[4],
                            w_timer=second[5])
                elif first == "remove":
                    del chatlog[second:]               
                    
                
            else:
                print("something's wacky", entry)

    $ chatroom_replay_index = 0
    $ replay_from = 0
    jump chat_end
