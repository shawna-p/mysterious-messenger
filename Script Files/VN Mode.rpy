#************************************
#************************************
#********Visual Novel Mode***********
#************************************
#************************************

#####################################
## Backgrounds
#####################################

image bg mint_eye_room = "VN Mode/Backgrounds/mint_eye_room.png"
image bg rika_apartment = "VN Mode/Backgrounds/rika_apartment.png"
image bg cr_meeting_room = "VN Mode/Backgrounds/cr_meeting_room.png"
image bg good_end = "VN Mode/Backgrounds/good_end.jpg"
image bg normal_end = "VN Mode/Backgrounds/normal_end.jpg"
image bg bad_end = "VN Mode/Backgrounds/bad_end.jpg"
image bg black = '#000000'

#####################################
## Extra Sound Effects
#####################################

define car_moving_sfx = "sfx/car moving.mp3"
define door_knock_sfx = "sfx/door knock.mp3"
define door_open_sfx = "sfx/door open.mp3"


#####################################
## Transforms/VN Positions
#####################################

# In order from leftmost to rightmost pose
transform vn_farleft:
    xalign 0.0
    yalign 1.0
    xoffset -300
    yoffset 0
    zoom 1.0

transform vn_left:
    xalign 0.0
    yalign 1.0
    xoffset -100
    zoom 1.0
    
transform vn_midleft:
    xalign 0.0
    yalign 1.0
    xoffset -50
    zoom 1.0
    
transform vn_center:
    xalign 0.5
    yalign 0.5
    zoom 1.15
    yoffset 280
    xoffset 0
    xanchor 0.5
    yanchor 0.5
    
transform vn_midright:
    xalign 1.0
    yalign 1.0
    xoffset 50
    zoom 1.0
    
transform vn_right:
    xalign 1.0
    yalign 1.0
    xoffset 100
    zoom 1.0
    
transform vn_farright:
    xalign 1.0
    yalign 1.0
    yoffset 0
    xoffset 300    
    zoom 1.0
    
    
#####################################
## VN Setup
#####################################

label vn_begin:
    window auto
    $ chatroom_hp = 0
    scene bg black
    stop music
    hide screen starry_night
    hide screen phone_overlay
    hide screen messenger_screen 
    hide screen pause_button
    hide screen chatroom_timeline
    show screen vn_overlay
    $ vn_choice = True
    $ _history_list = [] # This clears the History screen
    $ _history = True
    
    if current_chatroom.vn_obj.played:
        if not testing_mode:
            $ observing = True
        else:
            pass
    else:
        $ observing = False
        
    return
        
label vn_end:
    hide screen vn_overlay
    $ vn_choice = False
    $ renpy.retain_after_load()
    call press_save_and_exit(False) 
        
#####################################
## This screen shows the "Skip", 
## "Log", and new "Auto" buttons
#####################################

screen vn_overlay:

    $ my_menu_clock.runmode("real")
    hbox:
        add my_menu_clock xalign 0.0 yalign 0.0 xpos -50
        $ am_pm = time.strftime('%p', time.localtime())
        text am_pm style 'header_clock' 

        
#####################################
## This is the custom history screen
## for VN Mode
#####################################

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    add "Phone UI/choice_dark.png"
    add "Phone UI/choice_dark.png"
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        focus_mask True
        idle "close_button"
        action Return
        
    text "Close" style "CG_close"
    
    
    viewport:
        yinitial 1.0
        scrollbars "vertical"
        mousewheel True
        draggable True
        side_yfill True

        ysize 1235
        yalign 1.0

        vbox:
            style_prefix "history"
            spacing 20

            for h in _history_list:

                fixed:
                    yfit True

                    if h.who:

                        label h.who + ':':
                            style "history_name"

                            ## Take the color of the who text from the Character, if
                            ## set.
                            if "color" in h.who_args:
                                text_color h.who_args["color"]

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what

            if not _history_list:
                label _("The dialogue history is empty.")
