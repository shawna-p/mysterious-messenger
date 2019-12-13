#************************************
# Heart Icons
#************************************ 
    
init python:
    ## This function allows the program to show up to three
    ## heart icons on the screen at once
    def allocate_heart_screen():
        possible_screens = ["heart_icon_screen", "hicon2", "hicon3"]
        available_screens = [ x for x in possible_screens 
                                if not renpy.get_screen(x) ]
        if len(available_screens) < len(possible_screens):
            renpy.pause(0.1)
        if available_screens:
            return available_screens[0]
        else:
            renpy.hide_screen(possible_screens[0])
            return possible_screens[0]
    
    ## This allocates a notification screen that can
    ## be used to display popup messages
    ## Here it is used to display heart icon messages
    def allocate_notification_screen(can_pause=False):
        possible_screens = ["stackable_notifications", 
                            "stackable_notifications_2",
                            "stackable_notifications_3",
                            "stackable_notifications_4",
                            "stackable_notifications_5"]
        available_screens = [ x for x in possible_screens 
                                if not renpy.get_screen(x) ]
        if can_pause and len(available_screens) < len(possible_screens):
            renpy.pause(0.1)
        if available_screens:
            return available_screens[0]
        else:
            renpy.hide_screen(possible_screens[0])
            return possible_screens[0]
    
    ## This function is just a slightly quicker way to hide all the
    ## allocated notification screens
    def hide_stackable_notifications():
        renpy.hide_screen('stackable_notifications')
        renpy.hide_screen('stackable_notifications_2')
        renpy.hide_screen('stackable_notifications_3')
        renpy.hide_screen('stackable_notifications_4')
        renpy.hide_screen('stackable_notifications_5')
        return

# Call this to display the heart icon for a given character
label heart_icon(character, bad=False):
    
    if text_person is None:
        python:            
            if not observing:
                character.increase_heart(bad)
                # Ensure both Ray and Saeran share the same number
                # of heart points
                if character == r:
                    sa.increase_heart(bad)
                elif character == sa:
                    r.increase_heart(bad)
                chatroom_hp += 1
                persistent.HP += 1
            if (not observing and not persistent.heart_notifications):
                renpy.show_screen(allocate_heart_screen(), character=character)
            elif (not observing and persistent.heart_notifications):
                msg = character.name + " +1"
                renpy.show_screen(allocate_notification_screen(True), msg)
    # This is shown during a real-time text conversation
    elif text_person.real_time_text:
        $ character.increase_heart(bad)
        if character == r:
            $ sa.increase_heart(bad)
        elif character == sa:
            $ r.increase_heart(bad)
        $ persistent.HP += 1
        if persistent.heart_notifications:
            $ msg = character.name + " +1"
            $ renpy.show_screen(allocate_notification_screen(True), msg)
        else:
            show screen heart_icon_screen(character)
    # This is not a real-time text, so store the heart to 
    # display after this message is delivered
    else:
        $ add_heart(text_person, character, bad)
    return
    
# Displays the heart on-screen
screen heart_icon_screen(character, hide_screen='heart_icon_screen'):
    zorder 20   

    fixed at heart:
        yfit True
        xfit True
        add heart_icon(character)
        
    timer 0.62 action [Hide('heart_icon_screen')]

# Additional screens for allocation
screen hicon2(character):
    zorder 20   
    use heart_icon_screen(character, 'hicon2')

screen hicon3(character):
    zorder 20   
    use heart_icon_screen(character, 'hicon3')

## This screen is used to display text notifications
## about whom the player received a heart point with
screen stackable_notifications(message, hide_screen='stackable_notifications'):
    zorder 100
    button at stack_notify_appear:
        style 'notify_frame'
        xalign 1.0 yalign 0.92
        text "[message!tq]" style 'notify_text'
        action Hide(hide_screen)
    timer 5.25 action Hide(hide_screen)

screen stackable_notifications_2(message):
    zorder 101
    use stackable_notifications(message, 'stackable_notifications_2')

screen stackable_notifications_3(message):
    zorder 102
    use stackable_notifications(message, 'stackable_notifications_3')

screen stackable_notifications_4(message):
    zorder 103
    use stackable_notifications(message, 'stackable_notifications_4')

screen stackable_notifications_5(message):
    zorder 104
    use stackable_notifications(message, 'stackable_notifications_5')

transform stack_notify_appear:
    yoffset 0
    on show:
        alpha 0 yoffset 30
        linear .25 alpha 1.0 yoffset 0
        linear 5 yoffset -250
    on hide:
        linear .5 alpha 0.0 yoffset -310
        
# Like the heart icon, call this to display the heart break   
label heart_break(character):
    python:        
        if not observing:
            character.decrease_heart()
            if character == sa:
                r.decrease_heart()
            elif character == r:
                sa.decrease_heart()
            chatroom_hp -= 1
            persistent.HP -= 1     
    if (not observing and not persistent.heart_notifications):
        show screen heart_break_screen(character)
    elif (not observing and persistent.heart_notifications):
        $ msg = character.name + " -1"
        $ renpy.show_screen(allocate_notification_screen(True), msg)
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
        return VBox(speedtxt, numtxt), 0.05

# The number that shows up when adjusting the chatroom speed
style speednum_style is text:
    xalign 0.97
    yalign 0.22
    color "#ffffff"
    font gui.sans_serif_1b
    size 45
    text_align 0.5

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
# Displays the scrolled hacking effect

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
    if persistent.hacking_effects:
        show screen hack_screen('hack scroll')
        pause 3.0
        hide screen hack_screen
    return
    
label redhack():
    if (not observing and not persistent.testing_mode
            and not vn_choice):
        $ hack_entry = ("hack", "red")
        $ current_chatroom.replay_log.append(hack_entry)
    if persistent.hacking_effects:
        show screen hack_screen('redhack scroll')
        pause 3.0
        hide screen hack_screen
    return
    
#************************************
# Banners
#************************************

# These are the special "banners" that crawl across the screen
# Call them using "call banner('well')" etc

label banner(banner):
    if (not observing and not persistent.testing_mode
            and not vn_choice):
        $ banner_entry = ("banner", banner)
        $ current_chatroom.replay_log.append(banner_entry)
    if persistent.banners:
        show screen banner_screen(banner)
    return
    
screen banner_screen(banner):
    zorder 10
    fixed at truecenter:
        add 'banner ' + banner
        
    timer 0.72 action Hide('banner_screen')
    