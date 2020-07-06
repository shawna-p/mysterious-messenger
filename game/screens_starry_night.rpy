init -1 python:

    def star_func(trans,st,at):
        """Display the star at a random position."""

        trans.ypos = renpy.random.random()
        trans.xpos = renpy.random.random()
        return None
        
## These are the stars that will be animated
image small_star_static = "Menu Screens/Main Menu/small-star.png"

image small star:
    function star_func
    block:
        "transparent_img" with Dissolve(1.0, alpha=True)
        0.9
        "small_star_static" with Dissolve(1.0, alpha=True)
        # This just tells the program to pick a number between 5 and 9
        # and then wait that many seconds before continuing with the animation
        renpy.random.randint(3, 7) + renpy.random.random()
        repeat

image medium_star_static = "Menu Screens/Main Menu/medium-star.png"
        
image medium star:
    function star_func
    block:
        "medium_star_static" with Dissolve(1.0, alpha=True)
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
    add Transform("#000", alpha=persistent.starry_contrast)
    

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

## This ensures that the player has to set up their profile
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
        text renpy.random.choice(loading_tips) style "loading_tip"
        
    text "Loading..." style "loading_text" 
    
    add 'load_circle' xalign 0.5 yalign 0.745
    imagebutton:
        xalign 0.966 
        yalign 0.018
        idle 'load_close'
        hover Transform('load_close', zoom=1.05)
        action [Return()]
        
        
    add 'load_tip 'xalign 0.13 yalign 0.32

style loading_text:
    xalign 0.5
    yalign 0.607
    color "#fff"
    text_align 0.5
    font gui.sans_serif_1
    size 34
    
style loading_tip:
    xalign 0.5
    text_align 0.5
    yalign 0.4
    color "#fff"
    font gui.sans_serif_1
    size 34

default loading_tips = [ 
    "Please make sure the game is not quit or interrupted during save or load.",
    "Tap the Links button in the hub screen to go to the Mysterious Messenger Discord.",
    "Want to contribute to the program? Submit a pull request to the Mysterious Messenger Github!",
    "There are many accessibility options in the Settings menu.",
    "Found a bug? Report it on the Mysterious Messenger GitHub.",
    "Like the program? Consider donating to my Ko-Fi in Links.",
    "Is there a feature you want to see? Let me know in the Mysterious Messenger Discord.",
    "Did you know? You can turn on Audio Captions from the Settings menu.",
    "You can toggle animated backgrounds on or off from the Settings menu."
]
