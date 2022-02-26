transform start_text_effect:
    align (0.5, 0.90) alpha 0.0 #align defines the x and y position of the text respectively
    linear 0.5 alpha 0.2
    linear 0.5 alpha 0.5
    linear 0.5 alpha 0.7
    linear 0.5 alpha 1.0  #frame of text with no transparency
    linear 0.5 alpha 0.7
    linear 0.5 alpha 0.5
    linear 0.5 alpha 0.2
    linear 0.5 alpha 0.0  #alpha 0.0 so in these frames text is invisible
    repeat

transform start_bar_effect:
    align (0.5, 0.90) alpha 0.5
    ysize 50

screen start_screen():

    button:
        xysize (config.screen_width, config.screen_height)
        padding (0, 0)
        background "gui/main_title.png" #here you can replace the opening illustration
        bar yalign 0.0
        text "{b}Thi is only a prototype, the final game might be different!{/b}" size 20 xalign 0.5 yalign 0.0
        text "{color=#ffffffff}Mystic Messenger: New Story{/color}" size 32 xalign 0.06 yalign 0.05
        text "{color=#ffffffff}{b}DEMO EDITION VER. 0.1{/b}{/color}" size 20 xalign 0.06 yalign 0.08
        bar at start_bar_effect
        add "#0008" align (0.5, 0.90) ysize 50
        text "{color=#ffffffff}Game Start{/color}" size 40 at start_text_effect
        action Return()

##the start screen plays when it's summoned by label splash screen
##in screens_starry_night.rpy line 114 - anarki
