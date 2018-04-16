#************************************
# Special Bubbles
#************************************

    ### Note: you can find most of the gui values in the gui.rpy file
    ###  if you're looking to change them

    ####################################
    ## Speech bubbles - GLOW variant
    ####################################
    
    style reg_glow:
        margin gui.phone_glow_margin
        padding gui.phone_glow_padding
        xpos gui.phone_glow_xpos
        xalign gui.phone_glow_xalign 
        ypos gui.phone_glow_ypos 
        xmaximum gui.phone_glow_xmaximum
        min_width gui.phone_glow_min_width
        text_align gui.phone_glow_text_align
        layout ("subtitle" if gui.phone_text_xalign else "tex")
        
        
    ####################################
    ## Speech bubbles - For TEXT
    ####################################
        
    style bubble_text:
        line_spacing gui.phone_text_line_spacing
        xalign gui.phone_text_xalign
        ypos gui.phone_text_ypos2
        
    # Leftover from experiments to get the "NEW"
    # text to show up beside speech bubbles;
    # does nothing currently
    style NEW_text:
        xcenter 0.5
        ycenter 0.5
        
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
    
    style reg_bubble:
        bottom_margin gui.phone_text_bottom_margin
        padding gui.phone_text_padding
        pos gui.phone_text_pos
        xanchor gui.phone_text_xalign
        xmaximum gui.phone_text_width
        min_width gui.phone_text_width
        text_align gui.phone_text_xalign
        layout ("subtitle" if gui.phone_text_xalign else "tex")

    style MC_bubble:
        background Frame("Bubble/MC-bubble.png", 25, 18,18,18)
        bottom_margin gui.phone_textMC_bottom_margin
        padding gui.phone_textMC_padding
        pos gui.phone_textMC_pos
        xanchor gui.phone_textMC_xalign
        xmaximum gui.phone_textMC_width
        min_width gui.phone_textMC_width
        text_align gui.phone_textMC_xalign
        layout ("subtitle" if gui.phone_text_xalign else "tex")

    # This is for the chatroom exit/enter message
    style msg_bubble is text:
        background Frame("exit-enter.png", 0, 0)
        bottom_margin 10
        top_margin 5
        padding (5, 10)
        xalign 0.5
        xfill True
        text_align 0.5
        font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
        size gui.text_size - 10
        color "#ffffff"
        
    # This is specifically used to pad out the beginning of chatrooms
    # so that the text begins showing up at the bottom of the screen
    style filler_bubble:
        left_padding 100
        right_padding -100
        bottom_margin 10
        top_margin 10
        padding (5, 10)
        
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
        
        
        
