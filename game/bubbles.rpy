#************************************
# Special Bubbles
#************************************

### Note: you can find most of the gui values in the gui.rpy file
### if you're looking to change them

####################################
## Speech bubbles - GLOW variant
####################################

## ****************************************
## Glow Speech Bubble Style
style glow_bubble:    
    xalign 0.0
    padding (25, 28, 25, 22)
    pos (138, 38)

    
####################################
## Speech bubbles - For TEXT
####################################
    
# Text style for regular bubbles
style bubble_text:
    is text
    line_spacing gui.phone_text_line_spacing
    xalign 0.0
    yalign 0.5
    font gui.sans_serif_1
    
# This text style is shown when the text wraps
# It forces the width to be a certain length
style bubble_text_long:
    is bubble_text    
    xsize gui.phone_text_xsize_long
    
    
# This is for the "special" speech bubbles
# It's mostly just telling it to center the text
style special_bubble:
    is text
    text_align 0.5
    line_spacing gui.phone_text_line_spacing - 10
    ycenter 0.5
    xcenter 0.5
    font gui.sans_serif_1
    layout 'subtitle'
    #align (.5, .5)

####################################
## Speech bubbles - REGULAR variant
####################################

## ****************************************
## Regular Speech Bubble Style
style reg_bubble_MC:    
    padding (20, 15, 20, 9)
    pos (750-138-5,38)
    xanchor 1.0
        
style reg_bubble:  
    padding (20, 15, 20, 9)
    pos (138, 38)


## TEXT MESSAGES
# MC's text message speech bubble
style reg_bubble_MC_text:
    background 'mc_text_msg_bubble'
    padding (20,12,60,12)
        
# Other characters' text message speech bubble
style reg_bubble_text:        
    background 'npc_text_msg_bubble'
    padding (60,12,20,12)
    
## ****************************************
## Style for the enter/exit bubble
style msg_bubble:
    background "#00000050" #47%
    padding (5, 10)
    xalign 0.5
    xfill True
    ysize 49
            
style msg_bubble_text:
    is text
    text_align 0.5
    font gui.sans_serif_1
    size gui.text_size - 10
    color "#ffffff"
    xalign 0.5
    
## ****************************************
## Style for 'padding' dialogue that pushes
## text to the bottom
style filler_bubble:
    padding (5, 10)
            
style filler_bubble_text:
    size 35

    
####################################
## Super Special Bubbles
####################################
   
## SPIKE
style spike_s:
    padding gui.spike_s_padding

style spike_s2:
    padding gui.spike_s2_padding
    
style spike_m:
    padding gui.spike_m_padding
    
style spike_l:
    padding gui.spike_l_padding

style ja_spike_s is spike_s2
style ju_spike_s is spike_s2
style s_spike_s is spike_s
style y_spike_s is spike_s
style z_spike_s is spike_s

# spike_m_padding = (50, 50, 50, 50)
style ja_spike_m is spike_m:
    padding (25, 35, 35, 35)
style ju_spike_m is spike_m:
    padding (25, 35, 35, 35)
style r_spike_m is spike_m
style s_spike_m is spike_m
style sa_spike_m is spike_m
style v_spike_m is spike_m
style y_spike_m is spike_m
style z_spike_m is spike_m

style ja_spike_l is spike_l
style ju_spike_l is spike_l
style r_spike_l is spike_l
style s_spike_l is spike_l
style sa_spike_l is spike_l
style v_spike_l is spike_l
style y_spike_l is spike_l
style z_spike_l is spike_l

## CLOUD

style cloud_s:
    padding gui.cloud_s_padding
    
style cloud_m:
    padding gui.cloud_m_padding
    
style cloud_l:
    padding gui.cloud_l_padding
    
style cloud_l2:
    padding gui.cloud_l2_padding

# gui.cloud_s_padding = (30, 20, 30, 20)
style ja_cloud_s is cloud_s
style ju_cloud_s is cloud_s:
    left_padding 23
    top_padding 30
    right_padding 36
style r_cloud_s is cloud_s
style s_cloud_s is cloud_s
style sa_cloud_s is cloud_s
style v_cloud_s is cloud_s
style y_cloud_s is cloud_s:
    padding (50, 30, 35, 20)
style z_cloud_s is cloud_s

# gui.cloud_m_padding = (45, 40, 45, 40)
style ja_cloud_m is cloud_m:
    right_padding 90
style ju_cloud_m is cloud_m:
    padding (15, 85, 40, 30)
style r_cloud_m is cloud_m
style s_cloud_m is cloud_m:
    right_padding 70
style sa_cloud_m is cloud_m
style v_cloud_m is cloud_m
style y_cloud_m is cloud_m:
    padding (85, 60, 50, 25)
style z_cloud_m is cloud_m
    
# gui.cloud_l_padding = (65, 40, 70, 80)
style ja_cloud_l is cloud_l:
    padding (65, 70, 80, 70)
style ju_cloud_l is cloud_l:
    padding (25, 125, 55, 40)
style r_cloud_l is cloud_l
style s_cloud_l is cloud_l:
    padding (55, 40, 95, 50)
style sa_cloud_l is cloud_l:
    padding (65, 50, 50, 50)
style v_cloud_l is cloud_l
style y_cloud_l is cloud_l2
style z_cloud_l is cloud_l:
    bottom_padding 65

## SPECIAL BUBBLE 1 (ROUND)
style round_s:
    padding gui.round_s_padding
    
style round_m:
    padding gui.round_m_padding
    
style round_l:
    padding gui.round_l_padding
    
# round_s_padding = (40, 30, 40, 20)
style ja_round_s is round_s:
    top_padding 40
    bottom_padding 35
style ju_round_s is round_s:
    left_padding 60
    right_padding 20
style r_round_s is round_s
style s_round_s is round_s:
    xpadding 50
style s_round2_s is round_s:
    padding (60, 40, 60, 25)
style sa_round_s is round_s
style v_round_s is round_s
style y_round_s is round_s
style z_round_s is round_s

# round_m_padding = (55, 50, 55, 50)
style ja_round_m is round_m:
    top_padding 70
    bottom_padding 35
style ju_round_m is round_m:
    padding (85, 40, 20, 20)
style r_round_m is round_m
style s_round_m is round_m:
    right_padding 90
    left_padding 75
style sa_round_m is round_m
style v_round_m is round_m:
    padding(30, 50, 40, 20)
style y_round_m is round_m
style z_round_m is round_m

# padding = (70, 50, 70, 50)
style ja_round_l is round_l:
    top_padding 80
style ju_round_l is round_l:
    left_padding 95
    right_padding 45
style r_round_l is round_l
style s_round_l is round_l
style sa_round_l is round_l
style v_round_l is round_l:
    padding (45, 65, 60, 30)
style y_round_l is round_l
style z_round_l is round_l

## SPECIAL BUBBLE 2 (SQUARE)
style square_s:
    padding gui.square_s_padding
    
style square_m:
    padding gui.square_m_padding
    
style square_l:
    padding gui.square_l_padding
    
# square_s_padding = (40, 30, 50, 25)
style ja_square_s is square_s:
    padding (55, 55, 70, 40)
style ju_square_s is square_s:
    padding (20, 60, 50, 20)
style r_square_s is square_s:
    right_padding 40
style s_square_s is square_s
style sa_square_s is square_s:
    top_padding 40
style v_square_s is square_s:
    right_padding 45
style y_square_s is square_s
style z_square_s is square_s:
    right_padding 35
    bottom_padding 45

# square_m_padding = (50, 50, 65, 35)
style ja_square_m is square_m:
    padding (80, 80, 70, 40)
style ju_square_m is square_m:
    padding (30, 65, 70, 30)
style r_square_m is square_m
style s_square_m is square_m:
    bottom_padding 45
style sa_square_m is square_m
style v_square_m is square_m:
    left_padding 60
    right_padding 55
style y_square_m is square_m
style z_square_m is square_m:
    top_padding 40
    bottom_padding 60

# square_l_padding = (80, 60, 90, 50)
style ja_square_l is square_l:
    top_padding 75
    right_padding 70
    bottom_padding 30
style ju_square_l is square_l:
    padding (30, 90, 95, 20)
style r_square_l is square_l:
    bottom_padding 60
style s_square_l is square_l
style sa_square_l is square_l:
    top_padding 85
style v_square_l is square_l:
    left_padding 95
style y_square_l is square_l:
    left_padding 60
style z_square_l is square_l:
    padding (95, 100, 105, 95)

## SPECIAL BUBBLE 3 (FLOWER)
style flower_s:
    padding gui.flower_s_padding

style flower_m:
    padding gui.flower_m_padding

style flower_l:
    padding gui.flower_l_padding

# flower_s_padding = (35, 50, 40, 20)
style z_flower_s is flower_s:
    padding (55, 65, 55, 20)
style r_flower_s is flower_s
# flower_m_padding = (40, 80, 55, 35)
style z_flower_m is flower_m:
    padding (60, 55, 35, 30)
style r_flower_m is flower_m
# flower_l_padding = (55, 90, 65, 50)
style z_flower_l is flower_l:
    left_padding 80
    top_padding 70
    bottom_padding 35
style r_flower_l is flower_l

## SIGH BUBBLE
style sigh_s:
    padding gui.sigh_s_padding
    
style sigh_m:
    padding gui.sigh_m_padding
    
style sigh_l:
    padding gui.sigh_l_padding

    
style ja_sigh_s is sigh_s
style ju_sigh_s is sigh_s
style r_sigh_s is sigh_s
style s_sigh_s is sigh_s
style sa_sigh_s is sigh_s
style v_sigh_s is sigh_s
style y_sigh_s is sigh_s
style z_sigh_s is sigh_s

style ja_sigh_m is sigh_m
style ju_sigh_m is sigh_m
style r_sigh_m is sigh_m
style s_sigh_m is sigh_m
style sa_sigh_m is sigh_m
style v_sigh_m is sigh_m
style y_sigh_m is sigh_m
style z_sigh_m is sigh_m

style ja_sigh_l is sigh_l
style ju_sigh_l is sigh_l
style r_sigh_l is sigh_l
style s_sigh_l is sigh_l
style sa_sigh_l is sigh_l
style v_sigh_l is sigh_l
style y_sigh_l is sigh_l
style z_sigh_l is sigh_l
        
default bubble_list = [ ['Bubble/', '-Bubble.png'], ['Bubble/', '-Glow.png'],
                        ['Bubble/Special/', '_cloud_l.png'], 
                        ['Bubble/Special/', '_cloud_m.png'], 
                        ['Bubble/Special/', '_cloud_s.png'],
                        ['Bubble/Special/', '_round_l.png'], 
                        ['Bubble/Special/', '_round_m.png'], 
                        ['Bubble/Special/', '_round_s.png'],
                        ['Bubble/Special/', '_sigh_l.png'], 
                        ['Bubble/Special/', '_sigh_m.png'], 
                        ['Bubble/Special/', '_sigh_s.png'],
                        ['Bubble/Special/', '_square_l.png'], 
                        ['Bubble/Special/', '_square_m.png'], 
                        ['Bubble/Special/', '_square_s.png'],
                        ['Bubble/Special/', '_spike_l.png'], 
                        ['Bubble/Special/', '_spike_m.png'], 
                        ['Bubble/Special/', '_spike_s.png'],
                        ['Bubble/Special/', '_square2_l.png'], 
                        ['Bubble/Special/', '_square2_m.png'], 
                        ['Bubble/Special/', '_square2_s.png'],
                        ['Bubble/Special/', '_round2_l.png'], 
                        ['Bubble/Special/', '_round2_m.png'], 
                        ['Bubble/Special/', '_round2_s.png'] ]