init -1 python:

    # Picks a random position for the star to appear at
    def star_func(trans,st,at):
        trans.ypos = renpy.random.random()
        trans.xpos = renpy.random.random()
        return None
        
# These are the stars that will be animated
image small star:
    function star_func
    block:
        "transparent_img" with Dissolve(1.0, alpha=True)
        0.9
        "small_star" with Dissolve(1.0, alpha=True)
        # This just tells the program to pick a number between 5 and 9
        # and then wait that many seconds before continuing with the animation
        renpy.random.randint(3, 7) + renpy.random.random()
        repeat
        
image medium star:
    function star_func
    block:
        "medium_star" with Dissolve(1.0, alpha=True)
        renpy.random.randint(4, 11) + renpy.random.random()
        "transparent_img" with Dissolve(1.0, alpha=True)
        1.3
        repeat
        

# This makes it easier to call the starry night background
screen starry_night():
    frame:
        xysize (750,1334)
        background '#000'
    add "bg starry_night"
    for i in range(20):
        add "small star"
    for j in range(11):
        add "medium star"
        
    

image load_circle:
    'loading_circle_stationary'
    block:
        rotate 0
        linear 2.0 rotate 360
        repeat
        
image load_tip = "Menu Screens/Main Menu/loading_tip.png"
image load_close = "Menu Screens/Main Menu/loading_close.png"
image load_tip_panel = Frame("Menu Screens/Main Menu/loading_tip_panel.png", 300,100,80,80)

label splashscreen():    
    show screen loading_screen
    pause 1.0
    hide screen loading_screen
    return

## This ensures that the user has to set up their profile
## the very first time they open the game
label before_main_menu():
    if persistent.first_boot:
        call screen profile_pic
        $ define_variables()
    return
    
screen loading_screen():

    zorder 90
    tag menu
    
    use starry_night()
    
    frame:
        maximum(600,320)
        xalign 0.5
        yalign 0.42
        add "load_tip_panel"
        
    frame:
        maximum(540, 140)
        xalign 0.5
        yalign 0.445
        text ("Please make sure the game is not quit or" 
               + " interrupted during save or load") style "loading_tip"
        
    text "Loading..." style "loading_text" 
    
    add 'load_circle' xalign 0.5 yalign 0.745
    imagebutton:
        xalign 0.966 
        yalign 0.018
        idle 'load_close'
        hover Transform('load_close', zoom=1.05)
        action [Hide('splash_screen_test'), Return()]
        
        
    add 'load_tip 'xalign 0.13 yalign 0.32
    


