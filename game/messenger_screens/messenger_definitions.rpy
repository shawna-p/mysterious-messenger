init python:

    # A function to make the Max Speed button work
    def toggle_skipping():
        config.skipping = not config.skipping     

    # So you can increase/decrease the speed of the chat
    def slow_pv():
        global pv
        if pv <= 1.1:
            pv += 0.09  
        return
        
    def fast_pv():
        global pv
        if pv >= 0.53:
            pv -= 0.09
        return

    # This is a helper function for the heart icon that dynamically 
    # recolours a generic white heart depending on the character
    # See character definitions.rpy to define your own character 
    # & heart point
    def heart_icon(character):
        if character.heart_color:
            return im.MatrixColor("Heart Point/Unknown Heart Point.png", 
                    im.matrix.colorize("#000000", character.heart_color))
        else:
            return "Heart Point/Unknown Heart Point.png"
        
    # Similarly, this recolours the heartbreak animation
    def heart_break_img(picture, character):
        if character.heart_color:
            return im.MatrixColor(picture, 
                    im.matrix.colorize("#000000", character.heart_color))
        else:
            return "Heart Point/heartbreak_0.png"
        
    ## These next two functions recolour "generic" speech bubbles
    ## so you can have custom glow/regular bubbles
    def glow_bubble_fn(glow_color='#000'):
        return im.MatrixColor('Bubble/Special/sa_glow2.png', 
                            im.matrix.colorize(glow_color, '#fff'))
    
    def reg_bubble_fn(bubble_color='#000'):
        return im.MatrixColor('Bubble/white-Bubble.png', 
                            im.matrix.colorize('#000', bubble_color))

    

            
## Note: There is also a custom version of the chat footers
## (pause/play/save & exit/answer) that you can use by setting
## this variable to True. Otherwise, it will use the original assets
## If you change the variable here, you'll need to start the game over
## Otherwise it can also be changed from the Settings menu
default persistent.custom_footers = False

#************************************
# Chatroom Enter/Exit
#************************************
# This does some of the code for you when you want a character
# to enter/exit a chatroom. It adds characters to the chatroom's
# participant list if they enter during a chatroom.

label enter(chara):

    $ mystring = chara.name + " has entered the chatroom."
    if (not observing and not persistent.testing_mode
            and not vn_choice):
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
            and not vn_choice):
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
    if (not observing and not persistent.testing_mode
            and not vn_choice):
        # We should add this music to the replay_log
        $ music_entry = ("play music", file)
        $ current_chatroom.replay_log.append(music_entry)
    return

#************************************
# Screen Shake
#************************************
# This allows the program to keep track of when it should
# shake the screen during a chatroom
label shake():
    show expression current_background at shake
    if (not observing and not persistent.testing_mode
            and not vn_choice):
        # We should add this shake to the replay_log
        $ shake_entry = ("shake", current_background)
        $ current_chatroom.replay_log.append(shake_entry)
    return

#************************************
# Chatroom Replay (in-game)
#************************************
## This label is called when you want to replay a chatroom
label rewatch_chatroom():
    stop music
    $ chatlog = []

    # Make sure we're showing the messenger screens
    hide screen starry_night
    show screen phone_overlay
    show screen messenger_screen 
    show screen pause_button
    
    # Hide all the popup screens
    hide screen text_msg_popup
    hide screen text_msg_popup_instant
    hide screen email_popup
    
    $ inst_text = False
    window hide
    $ reply_screen = False
    $ in_phone_call = False
    $ vn_choice = False
    $ email_reply = False
    
    # Fills the beginning of the screen with 'empty space' 
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

    # Now we start the loop to iterate through the replay_log
    python:
        for entry in current_chatroom.replay_log:
            if isinstance(entry, ReplayEntry):
                # We want to pop it through the addchat function
                addchat(entry.who, entry.what, entry.pauseVal,
                    entry.img, entry.bounce, entry.specBubble)
            elif isinstance(entry, tuple):
                # It's some kind of command; we determine what to do
                # based on what the command and given info is
                first = entry[0]
                second = entry[1]
                if first == "banner":
                    renpy.show_screen('banner_screen', banner=second)
                elif first == "hack":
                    if second == "regular":
                        renpy.show_screen('hack_screen', hack='hack scroll')
                        # This looks a bit silly but for whatever reason it
                        # doesn't allow the player to skip it otherwise
                        # The hack screen was turned into a button, and if
                        # the player presses it it hides itself. Then the 
                        # program checks to make sure the hack screen is still
                        # showing so that it should continue to pause
                        if (not config.skipping 
                                and renpy.get_screen("hack_screen")):
                            renpy.pause(0.5, hard=False)
                        if (not config.skipping 
                                and renpy.get_screen("hack_screen")):
                            renpy.pause(0.5, hard=False)
                        if (not config.skipping 
                                and renpy.get_screen("hack_screen")):
                            renpy.pause(0.5, hard=False)
                        if (not config.skipping 
                                and renpy.get_screen("hack_screen")):
                            renpy.pause(0.5, hard=False)
                        if (not config.skipping 
                                and renpy.get_screen("hack_screen")):
                            renpy.pause(0.5, hard=False)
                        if (not config.skipping 
                                and renpy.get_screen("hack_screen")):
                            renpy.pause(0.5, hard=False)
                        renpy.hide_screen('hack_screen')
                    elif second == "red":
                        renpy.show_screen('hack_screen', hack='redhack scroll')
                        if (not config.skipping 
                                and renpy.get_screen("hack_screen")):
                            renpy.pause(0.5, hard=False)
                        if (not config.skipping 
                                and renpy.get_screen("hack_screen")):
                            renpy.pause(0.5, hard=False)
                        if (not config.skipping 
                                and renpy.get_screen("hack_screen")):
                            renpy.pause(0.5, hard=False)
                        if (not config.skipping 
                                and renpy.get_screen("hack_screen")):
                            renpy.pause(0.5, hard=False)
                        if (not config.skipping 
                                and renpy.get_screen("hack_screen")):
                            renpy.pause(0.5, hard=False)
                        if (not config.skipping 
                                and renpy.get_screen("hack_screen")):
                            renpy.pause(0.5, hard=False)
                        renpy.hide_screen('hack_screen')
                elif first == "play music":
                    renpy.music.play(second, channel='music', loop=True)
                elif first == "shake":
                    current_background = second
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
                    renpy.show(second)
                    if (first == "morning"
                            or first == "noon"
                            or first == "evening"):
                        nickColour = black
                    else:
                        nickColour = white
            else:
                print("something's wacky", entry)

    call chat_end

      


    
    
        
