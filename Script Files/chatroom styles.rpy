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
        font "fonts/Sandoll Misaeng (Curly Font).ttf"
    
    ## Serif Font 1
    style ser1:
        font "fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf"

    style ser1b:
        font "fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Bold.ttf"
 
    style ser1xb:
        font "fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-ExtraBold.ttf"
      
    ## Serif Font 2
    style ser2:
        font "fonts/Seoul Hangang (Serif font 2)/SeoulHangangM.ttf"
        
    style ser2b:
        font "fonts/Seoul Hangang (Serif font 2)/SeoulHangangB.ttf"
        
    style ser2xb:
        font "fonts/Seoul Hangang (Serif font 2)/SeoulHangangEB.ttf"
        
    ## Sans Serif Font 1
    style sser1:
        # this is the regular dialogue font/the default
        font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        
    style sser1b:
        font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Bold.ttf"
        
    style sser1xb:
        font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-ExtraBold.ttf"
    
    ## Sans Serif Font 2
    style sser2:
        font "fonts/SeoulNamsan (Sans Serif Font 2)/SeoulNamsanM.ttf"
        
    style sser2b:
        font "fonts/SeoulNamsan (Sans Serif Font 2)/SeoulNamsanB.ttf"
        
    style sser2xb:
        font "fonts/SeoulNamsan (Sans Serif Font 2)/SeoulNamsanEB.ttf"
      
    ## Blocky Font
    style blocky:
        font "fonts/BM-HANNA (Bold Font).ttf"

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
        
    style mc_img_message:
        padding (5, 10)
        bottom_margin -65
        pos (600, -70)
        xmaximum 750
        xalign 1.0
        
    ## ****************************************
    ## Style for images posted in text messages
    style img_text_message:
        padding (5, 10)
        bottom_margin -65
        pos (10, 5)
        xmaximum 750

    style mc_img_text_message:
        padding (5, 10)
        bottom_margin -65
        pos (270, -15)
        xmaximum 750
        xalign 1.0

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
        font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-ExtraBold.ttf"
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
        font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"

      
    ####################################
    ## Save & Exit Styles
    ####################################
    
    style save_exit_text is text:
        xalign 0.5         
        text_align 0.5
        size 25
        xsize 600
        font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        
    style sign is text:
        xalign 0.5   
        yalign 0.607   
        text_align 0.5
        size 30
        font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        
    style points is text:
        yalign 0.51
        text_align 1.0
        font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
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
        font "fonts/NanumBarunpenR.ttf"
               
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
        font "fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf"
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
        
    style vscroll_bar:
        base_bar Frame('gui/scrollbar/vertical_hover_bar.png',0,0)
        xsize 110
        thumb 'gui/scrollbar/vertical_hover_thumb.png'
        #yoffset 15
        
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
        font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        
    style settings_tabs:
        color '#fff'
        font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        text_align 0.5
        xalign 0.5
        yalign 0.5
        
    style sound_tags:
        color "#ffffff"
        font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        size 25
        text_align 0.5
        xalign 0.5
        yalign 0.5
        
    style hg_heart_points:
        color "#ffffff"
        font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        size 39
        text_align 1.0
        
    style ringtone_change:
        color '#fff'
        size 28
        xalign 0.5
        text_align 0.5
        yalign 0.5
        
    style ringtone_description:
        color '#fff'
        size 20
        xalign 0.5
        text_align 0.5
        yalign 0.5
        
    ## **********************
    ## Main Menu -- Other
    ## **********************
    
    style mode_select:
        color "#fff"
        font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        text_align 0.5
        xalign 0.5
        yalign 0.5
        
    style confirm_text:
        color "#eeeeee"
        hover_color "#ffffff"
        xalign 0.5
        text_align 0.5
        font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        size 30
        
    style vn_button:
        color '#76D0B7'
        font "fonts/SeoulNamsan (Sans Serif Font 2)/SeoulNamsanM.ttf"
        size 55
        outlines [(absolute(1), '#000', absolute(0), absolute(0))]
        kerning -1
        
    style vn_button_hover:
        color "#999999"
        font "fonts/SeoulNamsan (Sans Serif Font 2)/SeoulNamsanM.ttf"
        size 55
        outlines [(absolute(1), '#000', absolute(0), absolute(0))]
        kerning -1
        
    ## **********************
    ## Main Menu -- Loading
    ## **********************        
    
    style loading_text:
        xalign 0.5
        yalign 0.607
        color "#fff"
        text_align 0.5
        font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        size 34
        
    style loading_tip:
        xalign 0.5
        text_align 0.5
        yalign 0.4
        color "#fff"
        font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        size 34
        
    ## **********************
    ## Chat Home - Profiles
    ## **********************  
    
    style profile_header_text:        
        align (0.5, 0.5)
        text_align 0.5
        color "#fff"
        font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        size 55
        
    style profile_status:
        text_align 0.5
        align (0.5, 0.5)
        color "#fff"
        font "fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf"
        size 40
        xmaximum 600
        
    ## **********************
    ## Chat Home - Album
    ## ********************** 
        
    style album_text_short:
        align (0.5, 0.5)
        text_align 0.5
        color '#fff'
        font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        size 30
        
    style album_text_long:
        align (0.5, 0.5)
        text_align 0.5
        color '#fff'
        font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        size 25
        
        
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
        font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Bold.ttf"
        
    ## **********************
    ## Chat Select
    ## **********************
    style day_title:
        xalign 0.5
        text_align 0.5
        color '#fff'
        size 37
        font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        yalign 0.5
    
    ## **********************
    ## Phone Calls
    ## **********************
    style contact_text:
        color '#fff' 
        xalign 0.5 
        text_align 0.5
        font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Bold.ttf"
        
    style caller_id:
        color '#fff'
        xalign 0.5
        text_align 0.5
        font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        size 60
        
    style call_text:
        color '#fff'
        xalign 0.5
        yalign 0.5
        text_align 0.5
        font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        
    ## **********************
    ## Emails
    ## **********************
    style email_address:
        font "fonts/NanumBarunpenR.ttf"
        color '#fff'
        size 27
        
    ## **********************
    ## Spaceship Thoughts
    ## **********************
    style space_title1:
        font "fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf"
        size 25
        text_align 0.5
        align (0.5, 0.12)
        color '#ff0'
        
    style space_thought_mid:
        font "fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf"
        text_align 0.5
        align (0.5, 0.5)
        color '#fff'
        
    style space_title2:
        font "fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf"
        size 22
        text_align 0.5
        align (0.5, 0.95)
        outlines [(absolute(1), '#743801', absolute(0), absolute(0))]
        color '#fff'
        

        
    ####################################
    ## Other Miscellaneous Styles
    ####################################
    
    # Style for the Close button when viewing a fullscreen CG
    style CG_close is text:
        xalign 0.06
        yalign 0.016
        font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        color "#ffffff"
        size 45
        
    # The number that shows up when adjusting the chatroom speed
    style speednum_style is text:
        xalign 0.97
        yalign 0.22
        color "#ffffff"
        font  "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Bold.ttf"
        size 45
        text_align 0.5
        
    style chip_prize_text:
        color "#ffffff"
        font  "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        text_align 1.0
        size 37
        xalign 0.85
        yalign 0.5
        
    style chip_prize_description_short:
        color '#ffffff'
        font "fonts/BM-HANNA (Bold Font).ttf"
        text_align 0.5
        size 45
        xalign 0.5
        yalign 0.5

    style chip_prize_description_long:
        color '#ffffff'
        font "fonts/BM-HANNA (Bold Font).ttf"
        text_align 0.5
        size 37
        xalign 0.5
        yalign 0.5
    
    style header_clock:
        color '#fff'
        font  "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
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

    
    
        
        
        
    