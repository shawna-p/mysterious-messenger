#************************************
# Heart Icons
#************************************ 
    
# You call this to display the heart icon for a given character
label heart_icon(character, bad=False):
    python:
        if character == r:
            character = sa
        if not observing and not no_heart:
            character.increase_heart(bad)
            chatroom_hp += 1
            persistent.HP += 1
    if not observing and not no_heart:
        show screen heart_icon_screen(character)
    return
    
# Displays the heart on-screen
screen heart_icon_screen(character):
    zorder 20   

    fixed at heart:
        yfit True
        xfit True
        add heart_icon(character)
        
    timer 0.62 action [Hide('heart_icon_screen')]
        
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
        add heart_break_img("Heart Point/HeartBreak/stat_animation_6.png",
                             character)
    fixed at heartbreak(0.12):
        yfit True
        xfit True
        add heart_break_img("Heart Point/HeartBreak/stat_animation_7.png",
                             character)
    fixed at heartbreak(0.24):
        yfit True
        xfit True
        add heart_break_img("Heart Point/HeartBreak/stat_animation_8.png",
                             character)
    fixed at heartbreak(0.36):
        yfit True
        xfit True
        add heart_break_img("Heart Point/HeartBreak/stat_animation_9.png",
                             character)
    fixed at heartbreak(0.48):
        yfit True
        xfit True
        add heart_break_img("Heart Point/HeartBreak/stat_animation_10.png",
                             character)
        
    timer 0.6 action [Hide('heart_break_screen')]


#####################################
# Chat Speed Modifiers
#####################################

## This speeds up/slows down the speed of the chat

screen speed_num():
    python:
        global pv  
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
            
    text "{size=30}SPEED{/size}\n [speednum]" style 'speednum_style'
    
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
        action Hide('hack_screen')
        
    timer 3.0 action Hide('hack_screen')
        
    
label hack():
    if not observing and not persistent.testing_mode:
        $ hack_entry = ("hack", "regular")
        $ current_chatroom.replay_log.append(hack_entry)
    show screen hack_screen('hack scroll')
    pause 3.0
    hide screen hack_screen
    return
    
label redhack():
    if not observing and not persistent.testing_mode:
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
    if not observing and not persistent.testing_mode:
        $ banner_entry = ("banner", banner)
        $ current_chatroom.replay_log.append(banner_entry)
    show screen banner_screen(banner)
    return
    
screen banner_screen(banner):
    zorder 10
    window at truecenter:
        add 'banner ' + banner
        
    timer 0.72 action Hide('banner_screen')