init offset = -1

init 5:

    ####################################
    #***********************************
    ## Tranforms
    #***********************************
    ####################################
           
    ## Used for animations that bounce
    ## (glowing and special speech bubbles)
    transform incoming_message_bounce:
        alpha 0 zoom 0.5 yoffset 30
        linear 0.1 alpha 0.8 zoom 1.1 yoffset 0
        linear 0.1 alpha 1.0 zoom 1.0
        
    ## Used for most other things (bubbles,
    ## emojis, etc)
    transform incoming_message:
        alpha 1.0 zoom 0.4 yoffset 30
        linear 0.15 zoom 1.0 yoffset 0
        
    ## Used on the 'NEW' sign for new messages
    transform new_fade:
        alpha 0.0
        linear 0.2 alpha 1.0
        0.2
        linear 0.5 alpha 0.0

    #***********************************
    # Choice button enter/exit animation
    #***********************************
    
    transform choice_anim(delay=0.0):
        alpha 0.0
        pause delay - 0.1
        yoffset 15 alpha 0.3
        ease 0.3 yoffset -10 alpha 1.0
        ease 0.1 yoffset 0
                        
        on hover:
            ease 0.5 yoffset 5
            ease 0.5 yoffset -5
            repeat
            
        on idle:
            linear 0.3 yoffset 0
                        
    #***********************************
    # Spaceship/Chips Transforms
    #*********************************** 
    
    ## For the spaceship wiggle
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
            
    ## Animation that plays when the chips are available;
    ## moves the ship over to the chips, then lands on the
    ## chips
    transform spaceship_chips(intro=0.0):
        xalign 0.0
        parallel:
            linear 1.0*intro yoffset -15
            linear 1.0*intro yoffset 15
        parallel:
            linear 0.5*intro rotate -8
            linear 0.5*intro rotate 8
            linear 0.5*intro rotate -8
            linear 0.5*intro rotate 8
        parallel:
            linear 0.8*intro xalign 0.84
            0.8*intro
            linear 0.4*intro xalign 0.96
            
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
        
    ## Animation for the chips bursting out of the bag
    transform chip_anim(delay=1):
        alpha 0
        pause 1.91*delay
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
            
    ## The wobble for the chip bag when the 'chip_tap' screen
    ## is up
    transform chip_wobble:
        linear 0.9 rotate 5
        linear 0.7 rotate -5
        repeat
        
    ## The wobble for the chip bag when the clouds are visible
    transform chip_wobble2:
        linear 0.13 rotate 2
        linear 0.13 rotate -2
        repeat
        on hide:
            alpha 1.0
            linear 1.0 alpha 0.0
            
       
    ## Transform for the smallest 'tap' sign
    transform small_tap:
        rotate -8
        zoom 0.67
        xpos 310
        ypos -40
        
    ## transform for the medium 'tap' sign
    transform med_tap:
        rotate 47
        xpos 415
        ypos 40
        
    ## transform for the largest 'tap' sign
    transform large_tap:
        rotate 28
        zoom 1.5
        xpos 360
        ypos -100
        
    ## Below are the different 'shuffle' animations for the
    ## clouds obscuring the chip bag
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
            
            
    ## A solution for the odd animation issues surrounding
    ## the chip bag; this hides the clouds after 2 seconds
    transform hide_dissolve:
        alpha 1.0
        linear 2.0 alpha 1.0
        linear 0.5 alpha 0.0
            
    #***********************************
    # CG Album Transforms
    #*********************************** 
            
    ## Used for one of the images in the CG album
    transform album_tilt:
        rotate 7
        
    transform cg_swipe_left:
        xalign 0.0 xoffset 750 zoom 0.9 alpha 0.6 yalign 0.5
        linear 0.3 xoffset 0 xalign 0.0 zoom 1.0 alpha 1.0
        on hide:
            linear 0.3 xalign 1.0 xoffset 325 alpha 0.0
            
    transform cg_swipe_left2:
        xalign 0.0 xoffset 750 zoom 0.9 alpha 0.6 yalign 0.5
        linear 0.3 xoffset 0 xalign 0.0 zoom 1.0 alpha 1.0
        on hide:
            linear 0.3 xalign 1.0 xoffset 325 alpha 0.0
            
    transform cg_swipe_right:
        xalign 0.0 xoffset -750 zoom 0.9 alpha 0.6 yalign 0.5
        linear 0.3 xalign 0.0 xoffset 0 zoom 1.0 alpha 1.0
        on hide:
            linear 0.3 xalign 0.0 xoffset -325 alpha 0.0
            
    transform cg_swipe_right2:
        xalign 0.0 xoffset -750 zoom 0.9 alpha 0.6 yalign 0.5
        linear 0.3 xalign 0.0 xoffset 0 zoom 1.0 alpha 1.0
        on hide:
            linear 0.3 xalign 0.0 xoffset -325 alpha 0.0
            
    transform cg_swipe_right_hide:
        xalign 0.0 xoffset 0 alpha 1.0 zoom 1.0 yalign 0.5
        linear 0.3 xalign 0.0 xoffset 750 alpha 0.6 zoom 0.9
        
    transform cg_swipe_left_hide:
        xalign 0.0 xoffset 0 alpha 1.0 zoom 1.0 yalign 0.5
        linear 0.3 xalign 0.5 xoffset -750 alpha 0.6 zoom 0.9

            
    #***********************************
    # Other Transforms
    #***********************************            
        
    ## Used to display the chatroom speed message
    transform speed_msg:
        alpha 1
        0.4
        linear 0.4 alpha 0
        
    ## Shows the heart icon
    transform heart:
        alpha 0.3
        xalign 0.3 yalign 0.3
        alignaround (.5, .55)
        linear 0.6 xalign .4 yalign .6 clockwise circles 0 alpha 1
        linear 0.02 alpha 0 xalign .35 yalign .55
           
           
    ## The heartbreak icon
    transform heartbreak(wait_time):
        alpha 0.0
        pause wait_time
        alpha 0.7
        align (0.5, 0.5)
        zoom 2.0
        pause 0.12
        alpha 0    
    
    ## Used for the screen shake effect
    transform shake:    
        linear 0.12 xoffset -150 yoffset -200
        linear 0.12 xoffset 80 yoffset 60
        linear 0.14 xoffset -80 yoffset -60
        linear 0.14 xoffset 80 yoffset 60
        easein_back 0.16 xoffset 0 yoffset 0

        
    ## Used for the hacker screen effect
    transform flicker:
        linear 0.18 alpha 0.0
        linear 0.18 alpha 1.0
        repeat
        
    ## For timed menus
    transform alpha_dissolve:
        alpha 0.0
        linear 0.5 alpha 1.0
        on hide:
            linear 0.5 alpha 0
        
    ## Scrolls the title of chatrooms that are too long
    transform chat_title_scroll:
        pause 3.5
        linear 5.0 xalign 1.0 xoffset -420
        xalign 0.0 xoffset 0
        repeat
        
    ## Shuffles the participants list on a chatroom so you can
    ## see all the participants
    transform participant_scroll:
        pause 3.5
        linear 2.0 xalign 1.0
        pause 3.5
        linear 2.0 xalign 0.0
        repeat
    
    ## Usually used when the transform is a variable
    transform null_anim(num=0):
        pass

    transform invisible():
        alpha 0.0
    
    transform invisible_bounce():
        alpha 0.0 zoom 1.1
        
    ## Used to keep the full background of the
    ## chat timeline icons
    transform hacked_anim(cycle_time=10):
        xoffset 0 yoffset 0
        linear 0.01 alpha 1.0 xzoom 1.000001
        pause 0.01
        linear 0.01 alpha 1.0 xzoom 0.999999
        pause cycle_time
        
    transform hacked_anim_old(delay=0, meh=0):
        xoffset 0 yoffset 0
        pause delay
        parallel:
            linear 0.05  xzoom 1.03
            ease 0.08 xzoom 0.97
            pause 0.1
            linear 0.02 xzoom 1.02
            linear 0.023  xzoom 0.98
            pause 0.1
            linear 0.02 xzoom 1.01
            linear 0.01 xzoom 0.99
        #parallel:
        #    linear 0.05 xoffset -5 
        #    ease 0.08 xoffset 5 
        #    pause 0.1
        #    linear 0.02 xoffset -3 
        #    linear 0.023 xoffset 2 
        #    pause 0.1
        #    linear 0.02 xoffset -1 
        #    linear 0.01 xoffset 0 
        #parallel:
        #    linear 0.5 xzoom 0.9999
        #    ease 0.5 xzoom 1.000001
        pause 5.0
        #pause repeat_delay
        repeat
        
    # Used for a custom screen; currently unused
    transform dropdown_menu:
        yoffset -30
        easein 0.5 yoffset 0
        on hide, replaced:
            easeout 0.5 yoffset -30 alpha 0
            
    transform dropdown_horizontal:
        xoffset -30
        easein 0.5 xoffset 0
        on hide, replaced:
            easeout 0.5 xoffset -30 alpha 0
        
    ## Used for the outgoing call arrows
    transform delayed_blink2(delay, cycle):
        alpha 0.0
        pause delay

        block:
            linear .2 alpha 1.0
            pause .2
            linear (cycle - .6) alpha 0.0
            pause .4
            repeat
            
    
            
    
    
            
    