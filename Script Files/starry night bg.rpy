init -1 python:

    # Picks a random position for the star to appear at
    def star_func(trans,st,at):
        trans.ypos = renpy.random.random()
        trans.xpos = renpy.random.random()
        return None
        
# A starry night background with some static stars
image bg starry_night = "Phone UI/bg-starry-night.png"

# These are the stars that will be animated
image small star:
    function star_func
    block:
        "transparent.png" with Dissolve(1.0, alpha=True)
        0.9
        "Phone UI/small-star.png" with Dissolve(1.0, alpha=True)
        # This just tells the program to pick a number between 6 and 12
        # and then wait that many seconds before continuing with the animation
        renpy.random.randint(5, 9)
        repeat
        
image medium star:
    function star_func
    block:
        "Phone UI/medium-star.png" with Dissolve(1.0, alpha=True)
        renpy.random.randint(5, 10)
        "transparent.png" with Dissolve(1.0, alpha=True)
        1.3
        repeat
        

# This makes it easier to call the starry night background
screen starry_night:
    image "bg starry_night"
    image "small star"
    image "small star"
    image "small star"
    image "small star"
    image "small star"
    image "small star"
    image "small star"
    image "medium star"
    image "medium star"
    image "medium star"
    image "medium star"
    image "medium star"
    image "medium star"
    
#label splashscreen:

image load_circle:
    "Phone UI/Main Menu/loading_circle.png"
    block:
        rotate 0
        linear 2.0 rotate 360
        repeat
        
image load_tip = "Phone UI/Main Menu/loading_tip.png"
image load_close = "Phone UI/Main Menu/loading_close.png"
image load_tip_panel = Frame("Phone UI/Main Menu/loading_tip_panel.png", 300,100,80,80)

label splashscreen:
    show screen splash_screen_test
    pause 1.0
    hide screen splash_screen_test
    return
    
screen splash_screen_test:

    tag menu
    
    use starry_night
    
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
        hover im.FactorScale("Phone UI/Main Menu/loading_close.png", 1.05)
        action [ToggleVariable("greeted", False, True), Hide('splash_screen_test'), Return()]
        
        
    add 'load_tip 'xalign 0.13 yalign 0.32
    


