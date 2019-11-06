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
    def heart_icon_fn(st,at, colour=False):
        if not colour:
            colour = white
        return im.MatrixColor("Heart Point/Unknown Heart Point.png", 
                                im.matrix.colorize("#000000", colour)), 0.1

    ## This lets the screen call this image to display to the user
    def heart_icon(character):
        if character.heart_color:
            return DynamicDisplayable(heart_icon_fn,
                            colour=character.heart_color)
        else:
            return "Heart Point/Unknown Heart Point.png"
        
    # Similarly, this recolours the heartbreak animation
    def heart_break_fn(st,at, picture, colour=False):    
        if not colour:
            colour = white
        return im.MatrixColor(picture, 
                    im.matrix.colorize("#000000", colour)), 0.1

    def heart_break_img(picture, character):
        if character.heart_color:
            return DynamicDisplayable(heart_break_fn,
                            picture=picture,
                            colour=character.heart_color)
        else:
            return "Heart Point/HeartBreak/stat_animation_6.png"
        
    ## These next two functions recolour "generic" speech bubbles
    ## so you can have custom glow/regular bubbles
    def glow_bubble_fn(st,at, glow_color='#000'):
        colour = glow_color
        return im.MatrixColor('Bubble/Special/sa_glow2.png', 
                            im.matrix.colorize(colour, '#fff')), 0.1
                            
    
    def reg_bubble_fn(st,at, bubble_color='#000'):
        colour = bubble_color
        return im.MatrixColor('Bubble/white-Bubble.png', 
                            im.matrix.colorize('#000', colour)), 0.1

            
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
    
    $ addchat(special_msg, mystring, pv)
    if chara.name not in in_chat:
        $ in_chat.append(chara.name)
    
    if not observing:
        $ current_chatroom.add_participant(chara)
    
    $ renpy.restart_interaction
    return
    
label exit(chara):
    
    $ mystring = chara.name + " has left the chatroom."    
    $ addchat(special_msg, mystring, pv)
    if chara.name in in_chat:
        $ in_chat.remove(chara.name)
    $ renpy.restart_interaction
    return

#************************************
# Play Music/SFX
#************************************
# This allows the program to keep track of when to play
# music during a chatroom or VN
label play_music(file):
    play music file loop
    if not observing:
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
    if not observing:
        # We should add this shake to the replay_log
        $ shake_entry = ("shake", current_background)
        $ current_chatroom.replay_log.append(shake_entry)
    return


