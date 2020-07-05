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
define curlicue_font = "fonts/NanumBarunpenR.ttf"


init 5:

    ### Note: you can find many of the gui values in the gui.rpy file
    ### if you're looking to change them
        
    ####################################
    ## Custom Text Tags
    ####################################
    
    ## Curly Font
    style curly:
        size gui.text_size + 6
        font gui.curly_font
    
    ## Serif Font 1
    style ser1:
        font gui.serif_1

    style ser1b:
        font gui.serif_1b
 
    style ser1xb:
        font gui.serif_1xb
      
    ## Serif Font 2
    style ser2:
        font gui.serif_2
        
    style ser2b:
        font gui.serif_2b
        
    style ser2xb:
        font gui.serif_2xb
        
    ## Sans Serif Font 1
    style sser1:
        # this is the regular dialogue font/the default
        font gui.sans_serif_1
        
    style sser1b:
        font gui.sans_serif_1b
        
    style sser1xb:
        font gui.sans_serif_1xb
    
    ## Sans Serif Font 2
    style sser2:
        font gui.sans_serif_2
        
    style sser2b:
        font gui.sans_serif_2b
        
    style sser2xb:
        font gui.sans_serif_2xb
      
    ## Blocky Font
    style blocky:
        font gui.blocky_font

    ####################################
    ## Chat and Text Styles
    ####################################
        
    ## ****************************************
    ## Character Names Style
    style chat_name:
        text_align 0.0  
        align (0.0, 0.0)      
        font gui.sans_serif_1
        
    style chat_name_MC:        
        text_align 1.0
        align (1.0, 0.0)
        font gui.sans_serif_1

    style chat_name_frame:
        xoffset 148
        align (0.0, 0.0)

    style chat_name_frame_MC:
        xoffset -148
        align (1.0, 0.0)

    ## ****************************************
    ## Profile Pictures Style
    style MC_profpic:
        xysize (110,110)        
        xoffset -18
        xalign 1.0
        
    style profpic:
        xoffset 18
        xysize (110,110) 
        align (0.0, 0.0)
        
    ## ****************************************
    ## Style for images posted in the chatroom
    style img_message:
        padding (5, 10)
        xoffset 138 yoffset 38
        xmaximum 750   
        align (0.0, 0.0)
        
    style mc_img_message:
        padding (5, 10)
        xoffset -138 yoffset 38
        xmaximum 750
        xalign 1.0
        yalign 0.0

    # Text style for chatroom dialogue
    style phone_dialogue:
        pos (138, 0)
        xanchor 0.0
        xsize 750
        text_align 0.0


    # Style for the list that shows who is in the chatroom
    style in_chat_list_style:
        text_align 0.5
        xalign 0.5
        yalign 0.5
        color '#fff'
        size 23       
    
    ## **********************
    ## Text Messages
    ## **********************  
    
    ## ****************************************
    ## Profile Pictures Style - Text Messages
    style MC_profpic_text:
        maximum (110,110)
        
    style profpic_text:
        maximum (110,110) 
        
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

    style text_msg_npc_fixed:
        xanchor 0.0
        yanchor 0.0
        
    style text_msg_mc_fixed:
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
   
       

    # Default frame style
    style frame is default:
        background None
        align (0.0, 0.0)
        
        
        
        
    