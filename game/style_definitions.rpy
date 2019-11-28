################################################################################
## Initialization
################################################################################

init offset = -1

define curly_font = "fonts/Sandoll Misaeng (Curly Font).ttf"
define serif_1 = "fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf"
define serif_1b = "fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Bold.ttf"
define serif_1xb = "fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-ExtraBold.ttf"
define serif_2 = "fonts/Seoul Hangang (Serif font 2)/SeoulHangangM.ttf"
define serif_2b = "fonts/Seoul Hangang (Serif font 2)/SeoulHangangB.ttf"
define serif_2xb = "fonts/Seoul Hangang (Serif font 2)/SeoulHangangEB.ttf"
define sans_serif_1 = "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
define sans_serif_1b = "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Bold.ttf"
define sans_serif_1xb = "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-ExtraBold.ttf"
define sans_serif_2 = "fonts/SeoulNamsan (Sans Serif Font 2)/SeoulNamsanM.ttf"
define sans_serif_2b = "fonts/SeoulNamsan (Sans Serif Font 2)/SeoulNamsanB.ttf"
define sans_serif_2xb = "fonts/SeoulNamsan (Sans Serif Font 2)/SeoulNamsanEB.ttf"
define blocky_font = "fonts/BM-HANNA (Bold Font).ttf"


init 5:

    ### Note: you can find many of the gui values in the gui.rpy file
    ###  if you're looking to change them
        
    ####################################
    ## Custom Text Tags
    ####################################
    
    ## Curly Font
    style curly:
        size gui.text_size + 6
        font curly_font
    
    ## Serif Font 1
    style ser1:
        font serif_1

    style ser1b:
        font serif_1b
 
    style ser1xb:
        font serif_1xb
      
    ## Serif Font 2
    style ser2:
        font serif_2
        
    style ser2b:
        font serif_2b
        
    style ser2xb:
        font serif_2xb
        
    ## Sans Serif Font 1
    style sser1:
        # this is the regular dialogue font/the default
        font sans_serif_1
        
    style sser1b:
        font sans_serif_1b
        
    style sser1xb:
        font sans_serif_1xb
    
    ## Sans Serif Font 2
    style sser2:
        font sans_serif_2
        
    style sser2b:
        font sans_serif_2b
        
    style sser2xb:
        font sans_serif_2xb
      
    ## Blocky Font
    style blocky:
        font blocky_font

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
        pos (148, 0)
        xsize 435
        text_align 0.0
        font sans_serif_1
        
    style chat_name_MC:
        pos (596, 0)
        xsize 435
        text_align 1.0
        anchor (1.0, 0.0)
        font sans_serif_1
            
    ## ****************************************
    ## Profile Pictures Style
    style MC_profpic:
        pos (616, 0)
        maximum (110,110)
        align (0.0, 0.0)
        
    style profpic:
        pos (18, 0)
        maximum (110,110) 
        align (0.0, 0.0)
        
    ## ****************************************
    ## Profile Pictures Style - Texts
    style MC_profpic_text:
        maximum (110,110)
        
    style profpic_text:
        maximum (110,110) 

    ## ****************************************
    ## Style for images posted in the chatroom
    style img_message:
        padding (5, 10)
        pos (138, 38)
        xmaximum 750   
        align (0.0, 0.0)
        
    style mc_img_message:
        padding (5, 10)
        pos (600, 38)
        xmaximum 750
        xalign 1.0
        yalign 0.0
        
    ## ****************************************
    ## Style for images posted in text messages
    style img_text_message:
        padding (5, 10)
        pos (10, 0)
        xmaximum 750

    style mc_img_text_message:
        padding (5, 10)
        pos (270, 0)
        xmaximum 750
        xalign 1.0

    # Text style for chatroom dialogue
    style phone_dialogue:
        pos (138, 0)
        xanchor 0.0
        xsize 750
        text_align 0.0
        
    style in_chat_list_style:
        text_align 0.5
        xalign 0.5
        yalign 0.5
        color '#fff'
        size 23       
    
    ## **********************
    ## Text Messages
    ## **********************  
    style text_msg_npc_fixed:
        #pos (138, 0)
        xanchor 0.0
        yanchor 0.0
        
    style text_msg_mc_fixed:
        #pos (598, 0)
        xanchor 0.0
        yanchor 0.0
        
    style text_num:
        kerning -3
        color '#fff'
        size 30 
        text_align 0.5
        xalign 0.5
        yalign 0.5
        font sans_serif_1b
      
    ####################################
    ## Save & Exit Styles
    ####################################
    
    style save_exit_text is text:
        xalign 0.5         
        text_align 0.5
        size 25
        xsize 600
        font sans_serif_1
        
    style sign is text:
        xalign 0.5   
        yalign 0.607   
        text_align 0.5
        size 30
        font sans_serif_1
        
    style points is text:
        yalign 0.51
        text_align 1.0
        font sans_serif_1
        color "#ffffff"
        
        
    ####################################
    ## Main Menu Styles
    ####################################
    
    style menu_top_left_frame:
        maximum(450,420)
        padding (10, 10)
        xfill True
        yfill True
    
    style menu_right_frame:
        maximum(225, 210)
        xfill True
        yfill True
        padding (10, 10)
    
    style menu_bottom_left_frame:
        maximum(450,210)
        padding (10, 10)
        xfill True
        yfill True
        
    style menu_text_big is text:
        color "#ffffff"
        size 45
        text_align 0.5
        xalign 0.5
        
    style menu_text_small is text:
        color "#ffffff"
        size 30
        text_align 0.5
        xalign 0.5

        
    ## **********************
    ## Main Menu -- Greeting
    ## **********************
    
    style greet_text is text:
        color "#ffffff"
        size 27
        text_align 0.0
        slow_cps 20
        font "fonts/NanumBarunpenR.ttf"
        
    ## **********************
    ## Main Menu -- Profile
    ## **********************
    
        
    style point_indicator:
        size 40
        color "#fff"
        text_align 0.5
        xalign 0.5       

        
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
        font sans_serif_1
        
    style sound_tags:
        color "#ffffff"
        font sans_serif_1
        size 25
        text_align 0.5
        xalign 0.5
        yalign 0.5
        
    style hg_heart_points:
        color "#ffffff"
        font sans_serif_1
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
        font sans_serif_1
        text_align 0.5
        xalign 0.5
        yalign 0.5
        
    style confirm_text:
        color "#eeeeee"
        hover_color "#ffffff"
        xalign 0.5
        text_align 0.5
        font sans_serif_1
        size 30
        
    style vn_button:
        color '#76D0B7'
        font sans_serif_2
        size 55
        outlines [(absolute(1), '#000', absolute(0), absolute(0))]
        kerning -1
        
    style vn_button_hover:
        color "#999999"
        font sans_serif_2
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
        font sans_serif_1
        size 34
        
    style loading_tip:
        xalign 0.5
        text_align 0.5
        yalign 0.4
        color "#fff"
        font sans_serif_1
        size 34
        
    ## **********************
    ## Chat Home - Profiles
    ## **********************  
    
    style profile_header_text:        
        align (0.5, 0.5)
        text_align 0.5
        color "#fff"
        font sans_serif_1
        size 55
        
    style profile_status:
        text_align 0.5
        align (0.5, 0.5)
        color "#fff"
        font serif_1
        size 40
        xmaximum 600
        
    ## **********************
    ## Chat Home - Album
    ## ********************** 
        
    style album_text_short:
        align (0.5, 0.5)
        text_align 0.5
        color '#fff'
        font sans_serif_1
        size 30
        
    style album_text_long:
        align (0.5, 0.5)
        text_align 0.5
        color '#fff'
        font sans_serif_1
        size 25
        
        

        
    ## **********************
    ## Chat Select
    ## **********************
    style day_title:
        xalign 0.5
        text_align 0.5
        color '#fff'
        size 37
        font sans_serif_1
        yalign 0.5
    
    ## **********************
    ## Phone Calls
    ## **********************
    style contact_text:
        color '#fff' 
        xalign 0.5 
        text_align 0.5
        font sans_serif_1b
        
    style caller_id:
        color '#fff'
        xalign 0.5
        text_align 0.5
        font sans_serif_1
        size 70
        yoffset 10
        
    style call_text:
        color '#fff'
        xalign 0.5
        yalign 0.5
        text_align 0.5
        font sans_serif_1
        
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
        font serif_1
        size 25
        text_align 0.5
        align (0.5, 0.12)
        color '#ff0'
        
    style space_thought_mid:
        font serif_1
        text_align 0.5
        align (0.5, 0.5)
        color '#fff'
        
    style space_title2:
        font serif_1
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
        font sans_serif_1
        color "#ffffff"
        size 45
        
    # The number that shows up when adjusting the chatroom speed
    style speednum_style is text:
        xalign 0.97
        yalign 0.22
        color "#ffffff"
        font  sans_serif_1b
        size 45
        text_align 0.5
        
    style chip_prize_text:
        color "#ffffff"
        font  sans_serif_1
        text_align 1.0
        size 37
        xalign 0.85
        yalign 0.5
        
    style chip_prize_description_short:
        color '#ffffff'
        font blocky_font
        text_align 0.5
        size 45
        xalign 0.5
        yalign 0.5

    style chip_prize_description_long:
        color '#ffffff'
        font blocky_font
        text_align 0.5
        size 37
        xalign 0.5
        yalign 0.5
    
    style header_clock:
        color '#fff'
        font  sans_serif_1
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

    # Default frame style
    style frame is default:
        background None
        align (0.0, 0.0)
        
        
        
        
    