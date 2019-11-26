#************************************
# Heart Icons
#************************************ 
    
init python:
    ## This function is modified from Elaine/Empish's Automagical Notices code
    ## https://github.com/Emperrific/Renpy-Tutorials-Automagical-Notices
    def allocate_heart_screen():
        global available_heart_screens
        if len(available_heart_screens) < 3:
            renpy.pause(0.1)
        if available_heart_screens:
            return available_heart_screens.pop(0)
        else:
            return 'heart_icon_screen'
    
    def add_heart_screen(screen_name):
        global available_heart_screens
        available_heart_screens.append(screen_name)

default available_heart_screens = ["heart_icon_screen", "hicon2", "hicon3"]
# You call this to display the heart icon for a given character
label heart_icon(character, bad=False):
    if character == r:
        $ character = sa
    if text_person is None:
        python:            
            if not observing and not no_heart:
                character.increase_heart(bad)
                chatroom_hp += 1
                persistent.HP += 1
        if not observing and not no_heart:
            $ renpy.show_screen(allocate_heart_screen(), character=character)
            #show screen heart_icon_screen(character)
    # This is shown during a real-time text conversation
    elif text_person.real_time_text:
        $ character.increase_heart(bad)
        $ persistent.HP += 1
        show screen heart_icon_screen(character)
    # This is not a real-time text so we store the heart to 
    # display after this message is delivered
    else:
        $ add_heart(text_person, character, bad)
    return
    
# Displays the heart on-screen
screen heart_icon_screen(character):
    zorder 20   

    fixed at heart:
        yfit True
        xfit True
        add heart_icon(character)
        
    timer 0.62 action [Function(add_heart_screen, 'heart_icon_screen'),
                        Hide('heart_icon_screen')]

# Additional screens for allocation
screen hicon2(character):
    zorder 20   

    fixed at heart:
        yfit True
        xfit True
        add heart_icon(character)
        
    timer 0.62 action [Function(add_heart_screen, 'hicon2'),
                        Hide('hicon2')]

screen hicon3(character):
    zorder 20   

    fixed at heart:
        yfit True
        xfit True
        add heart_icon(character)
        
    timer 0.62 action [Function(add_heart_screen, 'hicon3'),
                        Hide('hicon3')]
        
# Like the heart icon, call this to display the heart break   
label heart_break(character):
    python:
        if character == r:
            character = sa
        if not observing and not no_heart:
            character.decrease_heart()
            chatroom_hp -= 1
            persistent.HP -= 1     
    if not observing and not no_heart:
        show screen heart_break_screen(character)
    return

# Displays the heartbreak on-screen
screen heart_break_screen(character):
    zorder 20
   
    fixed at heartbreak(0.0):
        yfit True
        xfit True
        add heart_break_img("Heart Point/heartbreak_0.png",
                             character)
    fixed at heartbreak(0.12):
        yfit True
        xfit True
        add heart_break_img("Heart Point/heartbreak_1.png",
                             character)
    fixed at heartbreak(0.24):
        yfit True
        xfit True
        add heart_break_img("Heart Point/heartbreak_2.png",
                             character)
    fixed at heartbreak(0.36):
        yfit True
        xfit True
        add heart_break_img("Heart Point/heartbreak_3.png",
                             character)
    fixed at heartbreak(0.48):
        yfit True
        xfit True
        add heart_break_img("Heart Point/heartbreak_4.png",
                             character)
        
    timer 0.6 action [Hide('heart_break_screen')]


#####################################
# Chat Speed Modifiers
#####################################

## This speeds up/slows down the speed of the chat

init python:
    def speed_num_fn(st, at):
        speednum = "!!"
        pv = store.pv
        if pv <= 0.45:
            speednum = "9"
        elif pv <= 0.54:
            speednum = "8"
        elif pv <= 0.63:
            speednum = "7"
        elif pv <= 0.72:
            speednum = "6"
        elif pv <= 0.81:
            speednum = "5"
        elif pv <= 0.90:
            speednum = "4"
        elif pv <= 0.99:
            speednum = "3"
        elif pv <= 1.08:
            speednum = "2"
        elif pv <= 1.17:
            speednum = "1" 
        else:
            speednum = "!!"

        speedtxt = Text("SPEED", style='speednum_style', size=30)
        numtxt = Text(speednum, style='speednum_style', align=(.5,.5))
        return VBox(speedtxt, numtxt), 0.02

image speed_num_img = DynamicDisplayable(speed_num_fn)

screen speed_num():
    
    add 'speed_num_img' align(0.98, 0.2)

    timer 0.4 action Hide('speed_num', Dissolve(0.4))

#####################################
# Hack scrolls, banners, enter/exit
#####################################
        
#************************************
# Hack Scrolls
#************************************
# You can call this when you want to display the green
# scrolled hacking effect

screen hack_screen(hack):
    zorder 10
    modal True
    add 'black'
    imagebutton at flicker:
        xysize (750,1334)
        idle hack
        if observing and not _in_replay:
            action Hide('hack_screen')
        
    timer 3.0 action Hide('hack_screen')
        
    
label hack():
    if (not observing and not persistent.testing_mode
            and not vn_choice):
        $ hack_entry = ("hack", "regular")
        $ current_chatroom.replay_log.append(hack_entry)
    show screen hack_screen('hack scroll')
    pause 3.0
    hide screen hack_screen
    return
    
label redhack():
    if (not observing and not persistent.testing_mode
            and not vn_choice):
        $ hack_entry = ("hack", "red")
        $ current_chatroom.replay_log.append(hack_entry)
    show screen hack_screen('redhack scroll')
    pause 3.0
    hide screen hack_screen
    return
    
#************************************
# Banners
#************************************

# These are the special "banners" that crawl across the screen
# Just call them using "call banner('well')" etc

label banner(banner):
    if (not observing and not persistent.testing_mode
            and not vn_choice):
        $ banner_entry = ("banner", banner)
        $ current_chatroom.replay_log.append(banner_entry)
    show screen banner_screen(banner)
    return
    
screen banner_screen(banner):
    zorder 10
    window at truecenter:
        add 'banner ' + banner
        
    timer 0.72 action Hide('banner_screen')