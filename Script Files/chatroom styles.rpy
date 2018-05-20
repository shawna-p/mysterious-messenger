################################################################################
## Initialization
################################################################################

init offset = -1

init 5:

    ### Note: you can find many of the gui values in the gui.rpy file
    ###  if you're looking to change them
        
    ####################################
    ## Custom Text Tags
    ####################################
    
    ## Curly Font
    style curly:
        size gui.text_size + 6
        font "00 fonts/Sandoll Misaeng (Curly Font).ttf"
    
    ## Serif Font 1
    style ser1:
        font "00 fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf"

    style ser1b:
        font "00 fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Bold.ttf"
 
    style ser1xb:
        font "00 fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-ExtraBold.ttf"
      
    ## Serif Font 2
    style ser2:
        font "00 fonts/Seoul Hangang (Serif font 2)/SeoulHangangM.ttf"
        
    style ser2b:
        font "00 fonts/Seoul Hangang (Serif font 2)/SeoulHangangB.ttf"
        
    style ser2xb:
        font "00 fonts/Seoul Hangang (Serif font 2)/SeoulHangangEB.ttf"
        
    ## Sans Serif Font 1
    style sser1:
        # this is the regular dialogue font/the default
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        
    style sser1b:
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Bold.ttf"
        
    style sser1xb:
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-ExtraBold.ttf"
    
    ## Sans Serif Font 2
    style sser2:
        font "00 fonts/SeoulNamsan (Sans Serif Font 2)/SeoulNamsanM.ttf"
        
    style sser2b:
        font "00 fonts/SeoulNamsan (Sans Serif Font 2)/SeoulNamsanB.ttf"
        
    style sser2xb:
        font "00 fonts/SeoulNamsan (Sans Serif Font 2)/SeoulNamsanEB.ttf"
      
    ## Blocky Font
    style blocky:
        font "00 fonts/BM-HANNA (Bold Font).ttf"
        
    ####################################
    #***********************************
    ## Styles
    #***********************************
    ####################################

    
    ####################################
    ## Chat Styles
    ####################################

    
    ## ****************************************
    ## Character Names Style
    style chat_name:
        pos (148, -80)
        xsize 435
        text_align 0.0
        font gui.phone_name_font
        
    style chat_name_MC:
        pos (596, -80)
        xsize 435
        text_align 1.0
        anchor (1.0, 0.0)
        font gui.phone_name_font
            
    ## ****************************************
    ## Profile Pictures Style
    style MC_profpic:
        pos (616, 30)
        maximum (110,110)
        
    style profpic:
        pos (18, 30)
        maximum (110,110) 
        
    ## ****************************************
    ## Profile Pictures Style - Texts
    style MC_profpic_text:
        pos (616, 30)
        maximum (110,110)
        
    style profpic_text:
        pos (18, 30)
        maximum (110,110) 

    ## ****************************************
    ## Style for images posted in the chatroom
    style img_message:
        padding (5, 10)
        bottom_margin -65
        pos (138, -70)
        xmaximum 750   

    # Text style for chatroom dialogue
    style phone_dialogue:
        pos (138, -75)
        xanchor 0.0
        xsize 750
        text_align 0.0
        
    ####################################
    ## Input Styles
    ####################################
    
    style input_window:
        xalign 0.5
        yalign 0.41
            
    style input_prompt:
        xalign 0.1
        yalign 0.83
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-ExtraBold.ttf"
        color "#ffffff"
        
    style input_answer:
        xalign 0.07
        yalign 0.46
        color "#ffffff"
        text_align 0.0
        
    style input_img_answer:
        xalign 0.07
        yalign 0.46
        key_events True
        xysize (365,55)
        
    style my_input:
        is default
        color "#000"
        text_align 0.5
        hover_color "#d7d7d7"
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"

      
    ####################################
    ## Save & Exit Styles
    ####################################
    
    style save_exit_text is text:
        xalign 0.5         
        text_align 0.5
        size 25
        xsize 600
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        
    style sign is text:
        xalign 0.5   
        yalign 0.607   
        text_align 0.5
        size 30
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        
    style points is text:
        yalign 0.51
        text_align 1.0
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        color "#ffffff"
        
        
    ####################################
    ## Main Menu Styles
    ####################################
    
    style menu_top_left_window:
        maximum(450,420)
        padding (10, 10)
        xfill True
        yfill True
    
    style menu_right_window:
        maximum(225, 210)
        xfill True
        yfill True
        padding (10, 10)
    
    style menu_bottom_left_window:
        maximum(450,210)
        padding (10, 10)
        xfill True
        yfill True
        
    style menu_text_big is text:
        color "#ffffff"
        size 45
        text_align 0.5
        
    style menu_text_small is text:
        color "#ffffff"
        size 30
        text_align 0.5

        
    ## **********************
    ## Main Menu -- Greeting
    ## **********************
    
    style greet_text is text:
        color "#ffffff"
        size 27
        text_align 0.0
        slow_cps 20
        font "00 fonts/NanumBarunpenR.ttf"
               
    style greet_box:
        xpos 228
        yalign 0.12
        maximum (500, 120)
        padding (10,5,33,5)
        
    ## **********************
    ## Main Menu -- Profile
    ## **********************
    
    style pronoun_window:
        background Frame("Phone UI/Main Menu/greeting_panel.png", 20, 20)
        maximum(340,400)
        xalign 0.99
        yalign 0.32
        padding (20,20)
        xfill True
        yfill True
        
    style pronoun_label:
        size 40
        color "#fff"
        text_align 0.5
        
    style point_indicator:
        size 40
        color "#fff"
        text_align 0.5
        xalign 0.5
        
    style my_name:
        color "#fff"
        text_align 0.0
        hover_color "#d7d7d7"
        font "00 fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf"
        xalign 0.06
        yalign 0.455

        
    ## **********************
    ## Main Menu -- Save/Load
    ## **********************
    
    style save_timestamp:
        size 25
        color "#fff"
        text_align 1.0
        xalign 1.0
        
    style save_slot_text:
        color "fff"
        text_align 0.0
        
    ## **********************
    ## Main Menu -- Settings
    ## **********************
    
    style voice_toggle_on:
        color "#99ffea"
        hover_color "#43ffd8"
        
    style voice_toggle_off:
        color "#a3a3a3"
        hover_color "#d0d0d0"
        
    style settings_style:
        color "#ffffff"
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        
    style settings_tabs:
        color '#fff'
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        text_align 0.5
        xalign 0.5
        yalign 0.5
        
    style sound_tags:
        color "#ffffff"
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        size 25
        text_align 0.5
        xalign 0.5
        
    style hg_heart_points:
        color "#ffffff"
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        size 39
        text_align 1.0
        
    ## **********************
    ## Main Menu -- Other
    ## **********************
    
    style mode_select:
        color "#fff"
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        text_align 0.5
        xalign 0.5
        yalign 0.5
        
    style confirm_text:
        color "#eeeeee"
        hover_color "#ffffff"
        xalign 0.5
        text_align 0.5
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        size 30
        
    ## **********************
    ## Main Menu -- Loading
    ## **********************        
    
    style loading_text:
        xalign 0.5
        yalign 0.607
        color "#fff"
        text_align 0.5
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        size 34
        
    style loading_tip:
        xalign 0.5
        text_align 0.5
        yalign 0.4
        color "#fff"
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        size 34
        
    ## **********************
    ## Chat Home - Profiles
    ## **********************  
    
    style profile_header_text:        
        xalign 0.75 #0.87
        text_align 0.5
        yalign 0.685
        color "#fff"
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        size 55
        
    style profile_status:
        xalign 0.5
        text_align 0.5
        yalign 0.905
        color "#fff"
        font "00 fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf"
        size 40
        xmaximum 600
        
        
    ## **********************
    ## Text Messages
    ## **********************  
    style text_msg_npc_fixed:
        pos (138, -55)
        xanchor 0
        yanchor 0
        xfit True
        yfit True
        
    style text_msg_mc_fixed:
        pos (598, -55)
        xanchor 1.0
        yanchor 0.0
        yfit True
        xfit True
        
    style text_num:
        kerning -3
        color '#fff'
        size 30 
        text_align 0.5
        xalign 0.5
        yalign 0.5
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Bold.ttf"
        
    ## **********************
    ## Chat Select
    ## **********************
    style day_title:
        xalign 0.5
        text_align 0.5
        color '#fff'
        size 37
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        yalign 0.5
    
    ## **********************
    ## Phone Calls
    ## **********************
    style contact_text:
        color '#fff' 
        xalign 0.5 
        text_align 0.5
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Bold.ttf"
        
    style caller_id:
        color '#fff'
        xalign 0.5
        text_align 0.5
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        size 60
        
    style call_text:
        color '#fff'
        xalign 0.5
        yalign 0.5
        text_align 0.5
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        
    ####################################
    ## Other Miscellaneous Styles
    ####################################
    
    # Style for the Close button when viewing a fullscreen CG
    style CG_close is text:
        xalign 0.06
        yalign 0.016
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        color "#ffffff"
        size 45
        
    # The number that shows up when adjusting the chatroom speed
    style speednum_style is text:
        xalign 0.97
        yalign 0.22
        color "#ffffff"
        font  "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Bold.ttf"
        size 45
        text_align 0.5
        
    style chip_prize_text:
        color "#ffffff"
        font  "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        text_align 1.0
        size 37
        xalign 0.85
        yalign 0.5
        
    style chip_prize_description:
        color '#ffffff'
        font "00 fonts/BM-HANNA (Bold Font).ttf"
        text_align 0.5
        size 45
        xalign 0.5
        yalign 0.17
        
    style header_clock:
        color '#fff'
        font  "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        text_align 1.0
        size 42
        xpos -110
        yalign 0.48
        
    
    #*************************************************************
    # Code leftover from when you could add the time to characters'
    # messages. Currently unused
    
    style phone_time is text:
        size 14
        color "#575757"
        xpos 410
        ypos 25

    style phone_time2 is text:
        size 14
        color "#575757"
        xpos 380
        ypos -100

    style phone_time3 is text:
        size 14
        color "#575757"
        xpos 160
        ypos -100

    
    ####################################
    #***********************************
    ## Tranforms
    #***********************************
    ####################################
           
    # Used for animations that bounce
    # (glowing and special speech bubbles)
    transform incoming_message_bounce:
        alpha 0 zoom 0.5
        linear 0.1 alpha 0.8 zoom 1.1
        linear 0.1 alpha 1.0 zoom 1.0
        
    # Used for most other things (bubbles,
    # emojis, etc)
    transform incoming_message:
        alpha 0 zoom 0.5
        linear 0.2 alpha 1.0 zoom 1.0
   
    # Used to make full-size CGs small enough
    # to post in a chatroom
    transform small_CG:
        alpha 0 zoom 0.175
        linear 0.2 alpha 1.0 zoom 0.35
        
    # Used on the 'NEW' sign for new messages
    transform new_fade:
        alpha 0.0
        linear 0.2 alpha 1.0
        0.5
        linear 0.5 alpha 0.0

    #***********************************
    # 'Anti' transformation for MysMe
    #***********************************
    
    transform anti_incoming_message:
        alpha 0 zoom 0.5
        linear 0.2 alpha 0.0 zoom 0

    transform anti_incoming_message_bounce:
        alpha 0 zoom 0.6
        linear 0.1 alpha 0 zoom 0.0
        linear 0.1 zoom 0.1
        
    transform anti_small_CG:
        zoom 0.165 alpha 0
        linear 0.2 zoom 0 

            
    #***********************************
    # Spaceship/Chips Transforms
    #*********************************** 
    
    # for the spaceship wiggle
    transform spaceship_flight:
        parallel:
            linear 1.0 yoffset -15
            linear 1.0 yoffset 15
        parallel:
            linear 0.5 rotate -8
            linear 0.5 rotate 8
            linear 0.5 rotate -8
            linear 0.5 rotate 8
        parallel:
            function spaceship_xalign_func
            
        block:
            parallel:
                ease 1.35 yoffset -15
                ease 1.35 yoffset 15
                repeat
            parallel:                
                linear 0.35 rotate -8
                linear 0.25 rotate 0
                linear 0.35 rotate 8
                linear 0.25 rotate 0
                repeat
            
    # Animation that plays when the chips are available;
    # moves the ship over to the chips, then lands on the
    # chips
    transform spaceship_chips:
        xalign 0.0
        parallel:
            linear 1.0 yoffset -15
            linear 1.0 yoffset 15
        parallel:
            linear 0.5 rotate -8
            linear 0.5 rotate 8
            linear 0.5 rotate -8
            linear 0.5 rotate 8
        parallel:
            linear 0.8 xalign 0.84
            0.8
            linear 0.4 xalign 0.96
            
        block:
            parallel:
                linear 1.0 yoffset -15
                linear 1.0 yoffset 15
                repeat
            parallel:
                linear 0.35 rotate -8
                linear 0.25 rotate 0
                linear 0.35 rotate 8
                linear 0.25 rotate 0
                repeat
            
    # Same animation as above, but without the intro
    # A solution to the 'reshow chat_home' problem
    transform spaceship_chips2:
        parallel:
            linear 1.0 yoffset -15
            linear 1.0 yoffset 15
            repeat
        parallel:
            linear 0.35 rotate -8
            linear 0.25 rotate 0
            linear 0.35 rotate 8
            linear 0.25 rotate 0
            repeat
        
    # Animation for the chips bursting out of the bag
    transform chip_anim:
        alpha 0
        1.91
        alpha 1
        block:
            yoffset 0
            parallel:
                linear 0.5 yoffset -43
                linear 0.66 yoffset -43
            parallel:
                alignaround(0.5,0.5)
                linear 0.5 rotate 0
                linear 0.33 rotate 25
                linear 0.33 rotate 10
            parallel:
                zoom 1.0
                linear 0.5 zoom 1.0
                linear 0.33 zoom 1.15
                linear 0.33 zoom 1.0
            repeat
            
    # Same as above, but without the ~2 second delay
    transform chip_anim2:
        yoffset 0
        parallel:
            linear 0.5 yoffset -43
            linear 0.66 yoffset -43
        parallel:
            alignaround(0.5,0.5)
            linear 0.5 rotate 0
            linear 0.33 rotate 25
            linear 0.33 rotate 10
        parallel:
            zoom 1.0
            linear 0.5 zoom 1.0
            linear 0.33 zoom 1.15
            linear 0.33 zoom 1.0
        repeat
            
    # The wobble for the chip bag when the 'chip_tap' screen
    # is up
    transform chip_wobble:
        linear 0.9 rotate 5
        linear 0.7 rotate -5
        repeat
        
    # The wobble for the chip bag when the clouds are visible
    transform chip_wobble2:
        on show:
            linear 0.13 rotate 2
            linear 0.13 rotate -2
            repeat
        on hide:
            alpha 1.0
            linear 1.0 alpha 0.0
            
       
    # Transform for the smallest 'tap' sign
    transform small_tap:
        rotate -8
        zoom 0.67
        xpos 310
        ypos -40
        
    # transform for the medium 'tap' sign
    transform med_tap:
        rotate 47
        xpos 415
        ypos 40
        
    # transform for the largest 'tap' sign
    transform large_tap:
        rotate 28
        zoom 1.5
        xpos 360
        ypos -100
        
    # Below are the different 'shuffle' animations for the
    # clouds obscuring the chip bag
    transform cloud_shuffle1:
        zoom 1.0 xanchor 1.0 yanchor 1.0
        block:
            linear 0.4 zoom 0.95
            linear 0.6 zoom 1.05
            repeat
            
    transform cloud_shuffle2:
        zoom 1.0
        block:
            linear 0.5 zoom 1.04
            linear 0.3 zoom 1.0
            linear 0.3 zoom 0.94
            repeat
        
    transform cloud_shuffle3:
        zoom 1.0 yanchor 1.0
        block:
            linear 0.4 zoom 1.05
            linear 0.45 zoom 0.95
            linear 0.3 zoom 1.02
            repeat
        
    transform cloud_shuffle4:
        zoom 1.0 xanchor 1.0 yanchor 0.0
        block:
            linear 0.5 zoom 1.05
            linear 0.5 zoom 0.95
            repeat            
            
    transform cloud_shuffle5:
        zoom 1.0
        block:
            linear 0.45 zoom 1.05
            linear 0.65 zoom 0.95
            repeat
            
            
    # A solution for the odd animation issues surrounding
    # the chip bag; this hides the clouds after 2 seconds
    transform hide_dissolve:
            alpha 1.0
            linear 2.0 alpha 1.0
            linear 0.5 alpha 0.0
            
            
    #***********************************
    # Other Transforms
    #***********************************            
        
    # Used to display the chatroom speed message
    transform speed_msg:
        alpha 1
        linear 0.4 alpha 1
        linear 0.4 alpha 0
        
    # Shows the heart icon
    transform heart:
        alpha 0.3
        xalign 0.3 yalign 0.3
        alignaround (.5, .55)
        linear 0.6 xalign .4 yalign .6 clockwise circles 0 alpha 1
        linear 0.02 alpha 0 xalign .35 yalign .55
           
    # The heartbreak icon
    transform heartbreak1:
        alpha 0.7
        xalign 0.5
        yalign 0.5
        zoom 2.0
        pause 0.12
        alpha 0
    transform heartbreak2:
        alpha 0
        linear 0.12 alpha 0
        alpha 0.7
        xalign 0.5
        yalign 0.5
        zoom 2.0
        pause 0.12
        alpha 0
    transform heartbreak3:
        alpha 0
        linear 0.24 alpha 0
        alpha 0.7
        xalign 0.5
        yalign 0.5
        zoom 2.0
        pause 0.12
        alpha 0
    transform heartbreak4:
        alpha 0
        linear 0.36 alpha 0
        alpha 0.7
        xalign 0.5
        yalign 0.5
        zoom 2.0
        pause 0.12
        alpha 0
    transform heartbreak5:
        alpha 0
        linear 0.48 alpha 0
        alpha 0.7
        xalign 0.5
        yalign 0.5
        zoom 2.0 
        pause 0.12
        alpha 0        
    
    # Used for the screen shake effect
    transform shake:    
        linear 0.12 xoffset -150 yoffset -200
        linear 0.12 xoffset 80 yoffset 60
        linear 0.14 xoffset -80 yoffset -60
        linear 0.14 xoffset 80 yoffset 60
        linear 0.16 xoffset 0 yoffset 0
        
    # Used for the hacker screen effect
    transform flicker:
        linear 0.18 alpha 0.0
        linear 0.18 alpha 1.0
        linear 0.18 alpha 0.0
        linear 0.18 alpha 1.0
        linear 0.18 alpha 0.0
        linear 0.18 alpha 1.0
        linear 0.18 alpha 0.0
        linear 0.18 alpha 1.0
        linear 0.18 alpha 0.0
        linear 0.18 alpha 1.0
        linear 0.18 alpha 0.0
        linear 0.18 alpha 1.0
        linear 0.18 alpha 0.0
        linear 0.18 alpha 1.0
        linear 0.18 alpha 0.0
        linear 0.18 alpha 1.0
        linear 0.12 alpha 0.0
        
    # For timed menus
    transform alpha_dissolve:
        alpha 0.0
        linear 0.5 alpha 1.0
        on hide:
            linear 0.5 alpha 0
            
    # Makes the profile pictures bigger for the
    # profile picture page
    transform profile_zoom:
        zoom 2.85
        xalign 0.1
        yalign 0.675
        
    transform text_zoom:
        zoom 1.15
        
    transform chat_title_scroll:
        pause 3.5
        linear 5.0 xalign 1.0 xoffset -420
        xalign 0.0 xoffset 0
        repeat
        
    transform participant_scroll:
        pause 3.5
        linear 2.0 xalign 1.0
        pause 3.5
        linear 2.0 xalign 0.0
        repeat
        
    transform null_anim:
        pass
        
    transform delayed_blink2(delay, cycle):
        alpha 0.0

        pause delay

        block:
            linear .2 alpha 1.0
            pause .2
            linear (cycle - .6) alpha 0.0
            pause .4
            #pause (cycle - .4)
            repeat
        
        
        
    