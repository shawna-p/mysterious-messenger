
image bg menuscreen = "Phone UI/Main Menu/menu_background.png"

# Character Greetings
image greet jaehee:
    "Phone UI/Main Menu/jaehee_greeting.png"
    xpos 65
    ypos 140
image greet jumin:
    "Phone UI/Main Menu/jumin_greeting.png"
    xpos 65
    ypos 140
image greet ray:
    "Phone UI/Main Menu/ray_greeting.png"
    xpos 65
    ypos 140
image greet rika:
    "Phone UI/Main Menu/rika_greeting.png"
    xpos 65
    ypos 140
image greet seven:
    "Phone UI/Main Menu/seven_greeting.png"
    xpos 65
    ypos 140
image greet unknown:
    "Phone UI/Main Menu/unknown_greeting.png"
    xpos 65
    ypos 140
image greet v:
    "Phone UI/Main Menu/v_greeting.png"
    xpos 65
    ypos 140
image greet yoosung:
    "Phone UI/Main Menu/yoosung_greeting.png"
    xpos 65
    ypos 140
image greet zen:
    "Phone UI/Main Menu/zen_greeting.png"
    xpos 65
    ypos 140
    
# This lets it randomly pick a profile picture to display
image greet random:
    choice:
        "greet jaehee"
    choice:
        "greet jumin"
    choice:
        "greet ray"
    choice:
        "greet rika"
    choice:
        "greet seven"
    choice:
        "greet unknown"
    choice:
        "greet v"
    choice:
        "greet yoosung"
    choice:
        "greet zen"

image greeting_bubble = Frame("Phone UI/Main Menu/greeting_bubble.png", 40, 10, 10, 10)
image greeting_panel = Frame("Phone UI/Main Menu/greeting_panel.png", 20, 20)

# Background Menu Squares
image right_corner_menu = Frame("Phone UI/Main Menu/right_corner_menu.png", 45, 45)
image left_corner_menu = Frame("Phone UI/Main Menu/left_corner_menu.png", 45, 45)
image right_corner_menu_selected = Frame("Phone UI/Main Menu/right_corner_menu_selected.png", 45, 45)
image left_corner_menu_selected = Frame("Phone UI/Main Menu/left_corner_menu_selected.png", 45, 45)

# Menu Icons
image menu_after_ending = "Phone UI/Main Menu/after_ending.png"
image menu_dlc = "Phone UI/Main Menu/dlc.png"
image menu_history = "Phone UI/Main Menu/history.png"
image menu_save_load = "Phone UI/Main Menu/save_load.png"
image menu_original_story = "Phone UI/Main Menu/original_story.png"

# Greeting Text
# (thus far very sparse)
image greet_text = Text("A short greeting", slow=True, color="#ffffff", size=30)

default greet_char = None

screen main_menu:

    tag menu
    
    # This defines the 'starry night' background with a few animated stars
    # You can see them defined in 'starry night bg.rpy'
    use starry_night

    
    window:
        maximum(670,140)
        xpos 380
        ypos 260
        add "greeting_panel"
    hbox:
        window:
            maximum(143,127)
            add "greet random"
        window:
            maximum(500,120)
            xpos 305
            ypos 250
            add "greeting_bubble"
    
    window:
        style "greet_box"
        text "Welcome to my Mystic Messenger Generator!" style "greet_text"

    
    # Note that most of these don't actually take you to the kind of screen you want >.<
    window:
        maximum(695, 650)
        xalign 0.6
        yalign 0.62
        vbox:
            hbox:
                window:
                    maximum(450,420)
                    padding (10, 10)
                    # Original Story
                    # Top left
                    imagebutton:
                        focus_mask True
                        idle "left_corner_menu"
                        hover "left_corner_menu_selected"
                        action Start()
                
                vbox:
                    window:
                        maximum(225, 210)
                        padding (10, 10)
                        # Save and Load
                        # Top Right
                        imagebutton:
                            focus_mask True
                            idle "right_corner_menu" 
                            hover "right_corner_menu_selected"
                            action ShowMenu("load")    
                            
                    window:
                        maximum(225, 210)
                        padding (10, 10)
                        # After Ending
                        # Mid Right
                        imagebutton:
                            focus_mask True
                            idle "right_corner_menu" 
                            hover "right_corner_menu_selected"
                            action ShowMenu("load") 
            hbox:
                window:
                    maximum(450,210)
                    padding (10, 10)
                    # History
                    # Bottom Left
                    imagebutton:
                        focus_mask True
                        idle "left_corner_menu"
                        hover "left_corner_menu_selected"
                        action ShowMenu("history")
                    
                window:
                    maximum(225, 210)
                    padding (10, 10)
                    # DLC
                    # Bottom Right
                    imagebutton:
                        focus_mask True
                        idle "right_corner_menu" 
                        hover "right_corner_menu_selected"
                        action ShowMenu("preferences")
                    
                    
    window:
        maximum(695, 650)
        xalign 0.6
        yalign 0.61
        vbox:
            hbox:
                window:
                    maximum(450,420)
                    padding (10, 10)
                    xfill True
                    yfill True
                    # Original Story
                    # Top left
                    vbox:    
                        align(0.5, 0.5)
                        add "menu_original_story" xpos 20
                        text "Original\nStory" style "menu_text_big"  ypos 15
                
                vbox:
                    window:
                        maximum(225, 210)
                        xfill True
                        yfill True
                        padding (10, 10)
                        # Save and load
                        # Top Right
                        vbox:                               
                            align(0.5, 0.5)
                            add "menu_save_load" xpos 25
                            text "Save & Load" style "menu_text_small" ypos 10
                    window:
                        maximum(225, 210)
                        xfill True
                        yfill True
                        padding (10, 10)
                        # After Ending
                        # Mid Right
                        vbox:                               
                            xcenter 0.5
                            ycenter 0.5
                            add "menu_after_ending" xpos 40
                            text "After Ending" style "menu_text_small" ypos 20
            hbox:
                window:
                    maximum(450,210)
                    padding (10, 10)
                    xfill True
                    yfill True
                    # History
                    # Bottom Left
                    vbox:                               
                        align(0.5, 0.5)
                        add "menu_history" xpos 15
                        text "History" style "menu_text_big" ypos 10
                    
                window:
                    maximum(225, 210)
                    padding (10, 10)
                    xfill True
                    yfill True
                    # DLC
                    # Bottom Right
                    vbox:                               
                        align(0.5, 0.5)
                        add "menu_dlc"
                        text "DLC" style "menu_text_small" xpos 25 ypos 15
                    
    
        
        
        
        
        
        
        
        
        
        
