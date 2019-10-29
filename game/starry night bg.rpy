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
        "transparent.png" with Dissolve(1.0, alpha=True)
        0.9
        "Phone UI/small-star.png" with Dissolve(1.0, alpha=True)
        # This just tells the program to pick a number between 5 and 9
        # and then wait that many seconds before continuing with the animation
        renpy.random.randint(5, 9)
        repeat
        
image medium star:
    function star_func
    block:
        "Phone UI/medium-star.png" with Dissolve(1.0, alpha=True)
        renpy.random.randint(5, 11)
        "transparent.png" with Dissolve(1.0, alpha=True)
        1.3
        repeat
        

# This makes it easier to call the starry night background
screen starry_night():
    window:
        xysize (750,1334)
        background '#000'
    add "bg starry_night"
    add "small star"
    add "small star"
    add "small star"
    add "small star"
    add "small star"
    add "small star"
    add "small star"
    add "small star"
    add "small star"
    add "small star"
    add "small star"
    add "small star"
    add "medium star"
    add "medium star"
    add "medium star"
    add "medium star"
    add "medium star"
    add "medium star"
    add "medium star"
    add "medium star"
    add "medium star"
    add "medium star"
    add "medium star"

image load_circle:
    "Phone UI/Main Menu/loading_circle.png"
    block:
        rotate 0
        linear 2.0 rotate 360
        repeat
        
image load_tip = "Phone UI/Main Menu/loading_tip.png"
image load_close = "Phone UI/Main Menu/loading_close.png"
image load_tip_panel = Frame("Phone UI/Main Menu/loading_tip_panel.png", 300,100,80,80)

label splashscreen():
    if persistent.first_boot:
        call define_variables 
    show screen loading_screen
    pause 1.0
    hide screen loading_screen
    return
    
screen loading_screen():

    zorder 90
    tag menu
    
    use starry_night()
    
    window:
        maximum(600,320)
        xalign 0.5
        yalign 0.42
        add "load_tip_panel"
        
    window:
        maximum(540, 140)
        xalign 0.5
        yalign 0.445
        text "Please make sure the game is not quit or interrupted during save or load" style "loading_tip"
        
    text "Loading..." style "loading_text" 
    
    add 'load_circle' xalign 0.5 yalign 0.745
    imagebutton:
        xalign 0.966 
        yalign 0.018
        idle 'load_close'
        hover Transform("Phone UI/Main Menu/loading_close.png", zoom=1.05)
        action [ToggleVariable("greeted", False, True), Hide('splash_screen_test'), Return()]
        
        
    add 'load_tip 'xalign 0.13 yalign 0.32
    


