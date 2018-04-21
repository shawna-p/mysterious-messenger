init python:

    class MyInputValue(InputValue):
            def __init__(self, var, default=""):
                self.var = var
                
                if not hasattr(store, var):
                    setattr(store, var, default)
                    mcName = {"MC": "Wrong"}
                    chatnick.update(mcName)
                    
            def get_text(self):
                return getattr(store, self.var)
                
            def set_text(self, s):
                s = s.strip()
                setattr(store, self.var, s)  
                persistent.name = s
                mcName = {"MC": "Wrong"}
                chatnick.update(mcName)
                renpy.save_persistent()
                
            def enter(self):
                renpy.run(self.Disable())                
                #raise renpy.IgnoreEvent()
               
    # This lets you change the MC's profile picture by clicking on it
    # Currently you can only use the pre-set images, not upload your own
    def MC_pic_change():   
        if persistent.MC_pic == 5:
            persistent.MC_pic = 1
        else:
            persistent.MC_pic += 1
            
        thepic = 'Profile Pics/MC/MC-[persistent.MC_pic].png'
        mcImage = {"MC": thepic}
        chatportrait.update(mcImage)
        
default persistent.pronoun = "nonbinary"
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
image greet_text2 = ParameterizedText(style="rfa_text")

image rfa_greet:
    Text("{k=-1}>>>>>>>{/k}  Welcome to Rika's Fundraising Association", color="#ffffff", size=30, slow=True, font="00 fonts/NanumBarunpenR.ttf", slow_cps=8, bold=True)
    10.0
    "transparent.png"
    0.2
    repeat

default greet_char = None

screen main_menu:

    tag menu
    
    python:
        thepic = 'Profile Pics/MC/MC-[persistent.MC_pic].png'
        if chatportrait["MC"] != thepic:
            mcImage = {"MC": thepic}
            chatportrait.update(mcImage)
            
        if chatnick["MC"] != persistent.name:
            mcName = {"MC": persistent.name}
            chatnick.update(mcName)
    
    # This defines the 'starry night' background with a few animated stars
    # You can see them defined in 'starry night bg.rpy'
    use starry_night
    
    add "rfa_greet" yalign 0.01 xalign 0.25
    
    
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
        # Could make this a variable so it changes the greeting message too
        # Would need a better way of keeping track of which character is displayed
        text "{size=-2}프로그램에 오신 것을 환영합니다!{/size}" style "greet_text"
        text "Welcome to my Mystic Messenger Generator!" style "greet_text" yalign 0.5

    
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
                            action ShowMenu("preferences") 
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
                        action ShowMenu("profile_pic")
                    
                    
    window:
        maximum(695, 650)
        xalign 0.6
        yalign 0.61
        vbox:
            hbox:
                window:
                    style "menu_top_left_window"
                    # Original Story
                    # Top left
                    vbox:    
                        align(0.5, 0.5)
                        add "menu_original_story" xpos 20
                        text "Original\nStory" style "menu_text_big"  ypos 15
                
                vbox:
                    window:
                        style "menu_right_window"
                        # Save and load
                        # Top Right
                        vbox:                               
                            align(0.5, 0.5)
                            add "menu_save_load" xpos 25
                            text "Save & Load" style "menu_text_small" ypos 10
                    window:
                        style "menu_right_window"
                        # After Ending
                        # Mid Right
                        vbox:                               
                            xcenter 0.5
                            ycenter 0.5
                            add "menu_after_ending" xpos 40
                            text "After Ending" style "menu_text_small" ypos 20
            hbox:
                window:
                    style "menu_bottom_left_window"
                    # History
                    # Bottom Left
                    vbox:                               
                        align(0.5, 0.5)
                        add "menu_history" xpos 15 ypos 3
                        text "History" style "menu_text_big" ypos 13
                    
                window:
                    style "menu_right_window"
                    # DLC
                    # Bottom Right
                    vbox:                               
                        align(0.5, 0.5)
                        add "menu_dlc"
                        text "DLC" style "menu_text_small" xpos 25 ypos 15
                        
 


image menu_header = Frame("Phone UI/Main Menu/menu_header.png", 0, 50) 
image menu_back = "Phone UI/Main Menu/menu_back_btn.png"
image save_btn = "Phone UI/Main Menu/menu_save_btn.png"
image load_btn = "Phone UI/Main Menu/menu_load_btn.png"
image name_line = "Phone UI/Main Menu/menu_underline.png"
image menu_edit = "Phone UI/Main Menu/menu_pencil_long.png"

default persistent.MC_pic = 1
default persistent.name = "Song"

image MC_profpic = ConditionSwitch(
    "persistent.MC_pic == 1", im.FactorScale("Profile Pics/MC/MC-1.png",3.3),
    "persistent.MC_pic == 2", im.FactorScale("Profile Pics/MC/MC-2.png",3.3),
    "persistent.MC_pic == 3", im.FactorScale("Profile Pics/MC/MC-3.png",3.3),
    "persistent.MC_pic == 4", im.FactorScale("Profile Pics/MC/MC-4.png",3.3),
    "persistent.MC_pic == 5", im.FactorScale("Profile Pics/MC/MC-5.png",3.3),
    "True", "Profile Pics/MC/MC-1.png")
     
     
image radio_on = "Phone UI/Main Menu/menu_radio_on.png"
image radio_off = "Phone UI/Main Menu/menu_radio_off.png"

screen profile_pic:
    
    tag menu
        
    # This defines the 'starry night' background with a few animated stars
    # You can see them defined in 'starry night bg.rpy'
    use starry_night
    
    ## Edit MC's Name
    add "name_line" xalign 0.079 yalign 0.475
    
    $ input = Input(value=MyInputValue("persistent.name", persistent.name), style="my_input", length=20)
        
    button:        
        style "input_img_answer"
        action input.enable        
        add input
        
    imagebutton:
        idle "menu_edit"
        focus_mask None
        xalign 0.06 #0.475
        yalign 0.457 #0.453
        hover im.FactorScale("Phone UI/Main Menu/menu_pencil_long.png",1.03)
        action input.enable   

    ## MC's profile picture
    imagebutton:
        idle "MC_profpic"
        xalign 0.055
        yalign 0.212
        action [MC_pic_change, renpy.restart_interaction]
        focus_mask True
      
    ## Not in MysMe; pick your pronouns
    window:
        style "pronoun_window"
        
        vbox:
            spacing 15
            xalign 0.5
            yalign 0.5
            text "Preferred Pronouns" style "pronoun_label"
            hbox:
                spacing 10
                if persistent.pronoun == "female":
                    add "radio_on"
                else:
                    add "radio_off"
                textbutton _("she/her") action [SetField(persistent, "pronoun", "female"), renpy.restart_interaction]
            hbox:
                spacing 10
                if persistent.pronoun == "male":
                    add "radio_on"
                else:
                    add "radio_off"
                textbutton _("he/him") action [SetField(persistent, "pronoun", "male"), renpy.restart_interaction]
                
            hbox:
                spacing 10
                if persistent.pronoun == "nonbinary":
                    add "radio_on"
                else:
                    add "radio_off"
                textbutton _("they/them") action [SetField(persistent, "pronoun", "nonbinary"), renpy.restart_interaction]
                
            
            
        
        
        
    ## Header
    window:
        ymaximum 80
        yalign 0.058
        add "menu_header"
        
    text "Profile" color "#ffffff" size 40 xalign 0.5 text_align 0.5 yalign 0.072
        
    imagebutton:
        xalign 0.013
        yalign 0.068
        idle "menu_back"
        focus_mask None
        hover im.FactorScale("Phone UI/Main Menu/menu_back_btn.png", 1.1)
        action ShowMenu("main_menu")
        
    ## Save / Load
    imagebutton:
        yalign 0.978
        xalign 0.66
        idle "save_btn"
        hover im.FactorScale("Phone UI/Main Menu/menu_save_btn.png",1.1)
        if main_menu:
            action ShowMenu("load")
        else:
            action ShowMenu("save")
        
    imagebutton:
        yalign 0.978
        xalign 0.974
        idle "load_btn"
        hover im.FactorScale("Phone UI/Main Menu/menu_load_btn.png",1.1)
        action ShowMenu("load")
                


# ****************************
# *******Fetch Name***********
# ****************************
label fetch_name:
    
    #$ name = renpy.call_screen("input", prompt="Please enter a username", defAnswer = "Sujin")
    $ name = name.strip()
    
    $ mcImage = {"MC": 'Profile Pics/MC/MC-2.jpg'}
    $ mcName = {"MC": "[name]"}

    $ chatportrait.update(mcImage)
    $ chatnick.update(mcName)

    $ stutter = name[:1]
    $ nameLength = len(name)
    $ nameEnd = name[nameLength - 1]
    $ nameCaps = name.upper()
    $ nameLow = name.lower()
    $ nameTypo = name[:nameLength - 1]
        
        
        
        
        
        
        
        
