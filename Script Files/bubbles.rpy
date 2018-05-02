#************************************
# Special Bubbles
#************************************

    ### Note: you can find most of the gui values in the gui.rpy file
    ###  if you're looking to change them

    ####################################
    ## Speech bubbles - GLOW variant
    ####################################
    
    ## ****************************************
    ## Glow Speech Bubble Style
    style glow_bubble:
        margin (0, 5, 0, -80)
        padding (32, 25)
        pos (125, -85)
        xalign 0.0
 
        
    ####################################
    ## Speech bubbles - For TEXT
    ####################################
        
    style bubble_text:
        line_spacing gui.phone_text_line_spacing
        xalign gui.phone_text_xalign
        ypos gui.phone_text_ypos2
        
    # This bubble is shown when the text wraps
    # It forces the width to be a certain length
    style bubble_text_long:
        line_spacing gui.phone_text_line_spacing
        xalign gui.phone_text_xalign
        ypos gui.phone_text_ypos2
        xsize gui.phone_text_xsize_long
        
        
    # This is for the "special" speech bubbles
    # It's mostly just telling it to center the text
    style special_bubble:
        text_align 0.5
        line_spacing gui.phone_text_line_spacing - 10
        ycenter 0.65
        xcenter 0.5
    
    ####################################
    ## Speech bubbles - REGULAR variant
    ####################################
    
    ## ****************************************
    ## Regular Speech Bubble Style
    style reg_bubble_MC:
        background Frame("Bubble/MC-bubble.png", 18, 18, 25, 18)
        bottom_margin -55
        padding (20, 9)
        pos (598, -75)
        anchor (1.0, 0.0)
            
    style reg_bubble:        
        bottom_margin -35
        top_margin 10
        padding (20, 9)
        pos (0,25)
        xanchor 0
        xmaximum 750
        min_width 750 
        
    # one-line variant (fixes spacing)
    style reg_bubble_short:        
        bottom_margin -60
        top_margin 0
        padding (20, 9)
        pos (0, 5)
        xanchor 0

    ## ****************************************
    ## Style for the enter/exit bubble
    style msg_bubble:
        background Frame("exit-enter.png", 0, 0)
        margin(0, 5, 0, 10)
        padding (5, 10)
        xalign 0.5
        xfill True
                
    style msg_bubble_text:
        text_align 0.5
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        size gui.text_size - 10
        color "#ffffff"
        xalign 0.5
        
    ## ****************************************
    ## Style for 'padding' dialogue that pushes
    ## text to the bottom
    style filler_bubble:
        left_padding 100
        right_padding -100
        bottom_margin 10
        top_margin 10
        padding (5, 10)
                
    style filler_bubble_text:
        size 35

        
    ####################################
    ## Super Special Bubbles
    ####################################
       
    ## SPIKE
    style spike_s:
        padding gui.spike_s_padding
        bottom_margin gui.spike_s_bottom_margin
        pos gui.spike_s_pos
        xysize gui.spike_s_xysize
        layout ("subtitle" if gui.phone_text_xalign else "tex")
        
    style spike_m:
        padding gui.spike_m_padding
        bottom_margin gui.spike_m_bottom_margin
        pos gui.spike_m_pos
        xysize gui.spike_m_xysize
        layout ("subtitle" if gui.phone_text_xalign else "tex")
        
    style spike_l:
        bottom_margin gui.spike_l_bottom_margin
        padding gui.spike_l_padding
        pos gui.spike_l_pos
        xysize gui.spike_l_xysize
        layout ("subtitle" if gui.phone_text_xalign else "tex")
        
    ## CLOUD
    style cloud_s:
        padding gui.cloud_s_padding
        pos gui.cloud_s_pos
        xysize gui.cloud_s_xysize
        bottom_margin gui.cloud_s_bottom_margin
        layout ("subtitle" if gui.phone_text_xalign else "tex")
        
    style cloud_m:
        padding gui.cloud_m_padding
        pos gui.cloud_m_pos
        xysize gui.cloud_m_xysize
        bottom_margin gui.cloud_m_bottom_margin
        layout ("subtitle" if gui.phone_text_xalign else "tex")
        
    style cloud_l:
        padding gui.cloud_l_padding
        pos gui.cloud_l_pos
        xysize gui.cloud_l_xysize
        bottom_margin gui.cloud_l_bottom_margin
        layout ("subtitle" if gui.phone_text_xalign else "tex")
        
    ## SPECIAL BUBBLE 1 (ROUND)
    style round_s:
        padding gui.round_s_padding
        pos gui.round_s_pos
        xysize gui.round_s_xysize
        bottom_margin gui.round_s_bottom_margin
        layout ("subtitle" if gui.phone_text_xalign else "tex")
        
    style round_m:
        padding gui.round_m_padding
        pos gui.round_m_pos
        xysize gui.round_m_xysize
        bottom_margin gui.round_m_bottom_margin
        layout ("subtitle" if gui.phone_text_xalign else "tex")
        
    style round_l:
        padding gui.round_l_padding
        pos gui.round_l_pos
        xysize gui.round_l_xysize
        bottom_margin gui.round_l_bottom_margin
        layout ("subtitle" if gui.phone_text_xalign else "tex")
        
    ## SPECIAL BUBBLE 2 (SQUARE)
    style square_s:
        padding gui.square_s_padding
        pos gui.square_s_pos
        xysize gui.square_s_xysize
        bottom_margin gui.square_s_bottom_margin
        layout ("subtitle" if gui.phone_text_xalign else "tex")
        
    style square_m:
        padding gui.square_m_padding
        pos gui.square_m_pos
        xysize gui.square_m_xysize
        bottom_margin gui.square_m_bottom_margin
        layout ("subtitle" if gui.phone_text_xalign else "tex")
        
    style square_l:
        padding gui.square_l_padding
        pos gui.square_l_pos
        xysize gui.square_l_xysize
        bottom_margin gui.square_l_bottom_margin
        layout ("subtitle" if gui.phone_text_xalign else "tex")
        
        
    ## SIGH BUBBLE
    style sigh_s:
        padding gui.sigh_s_padding
        pos gui.sigh_s_pos
        xysize gui.sigh_s_xysize
        bottom_margin gui.sigh_s_bottom_margin
        layout ("subtitle" if gui.phone_text_xalign else "tex")
        
    style sigh_m:
        padding gui.sigh_m_padding
        pos gui.sigh_m_pos
        xysize gui.sigh_m_xysize
        bottom_margin gui.sigh_m_bottom_margin
        layout ("subtitle" if gui.phone_text_xalign else "tex")
        
    style sigh_l:
        padding gui.sigh_l_padding
        pos gui.sigh_l_pos
        xysize gui.sigh_l_xysize
        bottom_margin gui.sigh_l_bottom_margin
        layout ("subtitle" if gui.phone_text_xalign else "tex")
        
        
        
