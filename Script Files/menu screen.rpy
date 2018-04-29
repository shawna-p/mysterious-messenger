init python:

    import time

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
                global cantype
                cantype = False
                #renpy.run(self.Disable())                
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
        
    def chat_greet(hour, greet_char):  
        global greeted
        greeted = True
        global greet_text_english
        global greet_text_korean        
        greet_text_english = "Welcome to my Mystic Messenger Generator!"
        
        if hour >= 6 and hour < 12:  # morning
            greet_text_english = "Good morning! " + greet_text_english
            
            num_greetings = len(morning_greeting[greet_char])
            the_greeting = renpy.random.randint(1, num_greetings) - 1
            renpy.play(morning_greeting[greet_char][the_greeting], channel="voice_sfx")
            
        elif hour >=12 and hour < 18:    # afternoon
            greet_text_english = "Good afternoon! " + greet_text_english
            
            num_greetings = len(afternoon_greeting[greet_char])
            the_greeting = renpy.random.randint(1, num_greetings) - 1
            renpy.play(afternoon_greeting[greet_char][the_greeting], channel="voice_sfx")
            
        elif hour >= 18 and hour < 22:  # evening
            greet_text_english = "Good evening! " + greet_text_english
            
            num_greetings = len(evening_greeting[greet_char])
            the_greeting = renpy.random.randint(1, num_greetings) - 1
            renpy.play(evening_greeting[greet_char][the_greeting], channel="voice_sfx")
            
        elif hour >= 22 or hour < 2: # night
            greet_text_english = "It's getting late! " + greet_text_english
            
            num_greetings = len(night_greeting[greet_char])
            the_greeting = renpy.random.randint(1, num_greetings) - 1
            renpy.play(night_greeting[greet_char][the_greeting], channel="voice_sfx")
            
        else:   # late night/early morning
            greet_text_english = "You're up late! " + greet_text_english
            
            num_greetings = len(late_night_greeting[greet_char])
            the_greeting = renpy.random.randint(1, num_greetings) - 1
            renpy.play(late_night_greeting[greet_char][the_greeting], channel="voice_sfx")
        
    def spaceship_xalign_func(trans,st,at):
        if st > 1.0:
            trans.xalign = spaceship_xalign
            return None
        else:
            trans.xalign = spaceship_xalign * st
            return 0
    
        global spaceship_xalign
        trans.xalign = spaceship_xalign
        return None
        
    def spaceship_get_xalign(new_num=False):
        global spaceship_xalign
        if new_num:
            spaceship_xalign = renpy.random.random()
            spaceship_xalign = spaceship_xalign * 0.8 + 0.04
        return spaceship_xalign
        

image bg menuscreen = "Phone UI/Main Menu/menu_background.png"

# Character Greetings
image greet jaehee = "Phone UI/Main Menu/jaehee_greeting.png"
image greet jumin = "Phone UI/Main Menu/jumin_greeting.png"
image greet ray = "Phone UI/Main Menu/ray_greeting.png"
image greet rika = "Phone UI/Main Menu/rika_greeting.png"
image greet seven = "Phone UI/Main Menu/seven_greeting.png"
image greet unknown = "Phone UI/Main Menu/unknown_greeting.png"
image greet v = "Phone UI/Main Menu/v_greeting.png"
image greet yoosung = "Phone UI/Main Menu/yoosung_greeting.png"
image greet zen = "Phone UI/Main Menu/zen_greeting.png"
    
# This lets it randomly pick a profile picture to display        
default greet_char = "seven"
define character_list = ['jaehee', 'jumin', 'ray', 'rika', 'seven', 
                                 'unknown', 'v', 'yoosung', 'zen']

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
default greet_text_korean = "제 프로그램으로 환영합니다!"
default greet_text_english = "Welcome to my Mystic Messenger Generator!"

image rfa_greet:
    Text("{k=-1}>>>>>>>{/k}  Welcome to Rika's Fundraising Association", color="#ffffff", size=30, slow=True, font="00 fonts/NanumBarunpenR.ttf", slow_cps=8, bold=True)
    10.0
    "transparent.png"
    0.2
    repeat

default greeted = False


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
## Also shows a greeting from a random character
##

screen main_menu:

    tag menu
    
    $ renpy.play(mystic_chat, channel="music")
    
    python:
        thepic = 'Profile Pics/MC/MC-[persistent.MC_pic].png'
        if chatportrait["MC"] != thepic:
            mcImage = {"MC": thepic}
            chatportrait.update(mcImage)
            
        if chatnick["MC"] != persistent.name:
            mcName = {"MC": persistent.name}
            chatnick.update(mcName)
            
        hour = time.strftime('%H', time.localtime())
        hour = int(hour)    # gets the hour, makes it an int
        greet_char = renpy.random.choice(character_list)
        if not greeted:
            chat_greet(hour, greet_char)
        
    
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
            add "Phone UI/Main Menu/[greet_char]_greeting.png" xpos 65 ypos 140
        window:
            maximum(500,120)
            xpos 305
            ypos 250
            add "greeting_bubble"
    
    window:
        style "greet_box"
        # Could make this a variable so it changes the greeting message too
        # Would need a better way of keeping track of which character is displayed
        text "{size=-2}" + "[greet_text_korean]" + "{/size}" style "greet_text"
        text "[greet_text_english]" style "greet_text" yalign 0.5

    
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
                        activate_sound "sfx/UI/select_4.mp3"
                        action Show('chat_home')
                
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
                        action Start()#ShowMenu("history")
                    
                window:
                    maximum(225, 210)
                    padding (10, 10)
                    # DLC
                    # Bottom Right
                    imagebutton:
                        focus_mask True
                        idle "right_corner_menu" 
                        hover "right_corner_menu_selected"
                        action ToggleVariable('chips_available', False, True) #Jump("splashscreen")
                    
                    
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
                        
 
              
## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##


screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use starry_night
    
    use menu_header(title)
        
    
    fixed:

        ## This ensures the input will get the enter event before any of the
        ## buttons do.
        order_reverse True


        ## The grid of file slots.
        vpgrid:
            # This is a vpgrid since originally you could scroll it down to 12 slots
            # (see the commented out numbers below), but it looks cleaner if I restrict
            # it to 7 rows and a page select vs. 12 scrollable columns and a page select
            # If you wanted to *just* have a very long viewport of saves, then you could just
            # remove the code for the page select and increase the number of rows
            maximum (740,1100) #(740, 1120)
            rows 7 #gui.file_slot_rows
            draggable True
            mousewheel True
            style_prefix "slot"

            xalign 0.01
            yalign 0.68 #0.8

            spacing gui.slot_spacing

            for i in range(gui.file_slot_cols * gui.file_slot_rows):

                $ slot = i + 1

                button:
                    action FileAction(slot)

                    has hbox
                    spacing 10

                    # TODO: Implement a variable that keeps track of whose route you're on
                    # Then the appropriate picture can be appended to the save file instead
                    add FileScreenshot(slot) xalign 0.0
                    
                    window:
                        xmaximum 435
                        yalign 0.5
                        has vbox
                        text "Name of Chatroom" style "save_slot_text"
                        spacing 40
                        text "Today: 10th DAY" style "save_slot_text"
                        
                    window:
                        xmaximum 175
                        has vbox
                        
                        text FileTime(slot, format=_("{#file_time}%m/%d %H:%M"), empty=_("empty slot")):
                            style "save_timestamp"
                            
                        spacing 30

                        imagebutton:
                            hover im.FactorScale("Phone UI/Main Menu/save_trash_hover.png",1.05)
                            idle "Phone UI/Main Menu/save_trash.png"
                            xalign 1.0
                            action FileDelete(slot)

                    key "save_delete" action FileDelete(slot)

        ## Buttons to access other pages.
        hbox:
            style_prefix "page"

            xalign 0.5
            yalign 1.0

            spacing gui.page_spacing

            textbutton _("<") action FilePagePrevious()

            if config.has_autosave:
                textbutton _("{#auto_page}Auto") action FilePage("auto")

            if config.has_quicksave:
                textbutton _("{#quick_page}Quick") action FilePage("quick")

            ## range(1, 10) gives the numbers from 1 to 9.
            for page in range(1, 10):
                textbutton "[page]" action FilePage(page)

            textbutton _(">") action FilePageNext()


            
image menu_settings_panel = Frame("Phone UI/Main Menu/settings_sound_panel.png",60,200,60,120)
image menu_sound_sfx = "Phone UI/Main Menu/settings_sound_sfx.png"
image menu_default_sounds = Frame("Phone UI/Main Menu/settings_sound_default.png",10,10)
            
## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##

screen preferences():

    tag menu

    #add "Phone UI/Main Menu/menu_settings_bg.png"
    use starry_night
    use menu_header("Settings")
    use settings_tabs("Sound")
    
    window:
        maximum(700, 800)
        xalign 0.5
        yalign 0.45
        has vbox
        spacing 30
            
        window:
            maximum(675,350)
            add "menu_settings_panel"
            text "Sound" style "settings_style" xpos 55 ypos 5
            
        window:
            maximum(675,320)
            add "menu_settings_panel"
            text "Voice" style "settings_style" xpos 55 ypos 5
            
    window:
        xalign 0.5
        yalign 0.34
        maximum(580,350)
        has vbox        
        spacing 10
        hbox:
            spacing 30
            textbutton _("BGM"):
                background "menu_sound_sfx"
                text_style "sound_tags"
                xsize 163
                ysize 50
            bar value Preference("music volume") ypos 15
        hbox:
            spacing 30
            textbutton _("SFX"):
                background "menu_sound_sfx"
                text_style "sound_tags"
                xsize 163
                ysize 50
            bar value Preference("sound volume") ypos 15
            if config.sample_sound:
                        textbutton _("Test") action Play("sound", config.sample_sound)
        hbox:
            spacing 30
            textbutton _("Voice"):
                background "menu_sound_sfx"
                text_style "sound_tags"
                xsize 163
                ysize 50
            bar value Preference("voice volume") ypos 15
            if config.sample_voice:
                        textbutton _("Test") action Play("voice", config.sample_voice)
        hbox:
            spacing 30
            textbutton _("Voice SFX"):
                background "menu_sound_sfx"
                text_style "sound_tags"
                xsize 163
                ysize 50
            bar value set_voicesfx_volume() ypos 15
            
        textbutton _("Mute All"):
                    action Preference("all mute", "toggle")
                    style "mute_all_button" xalign 0.45
            

    
    ## There are no actual voiced lines in this program, so right
    ## now all you get to do is toggle the button from on to off 
    window:
        maximum(675,300)
        yalign 0.72
        xalign 1.2
        grid 2 3:
            xpos -30
            transpose True
            spacing 40
            
            text "Jumin Han" style "settings_style"
            text "ZEN" style "settings_style"
            text "707" style "settings_style"
            
            if persistent.jumin_voice:
                textbutton "On" text_style "voice_toggle_on" action SetField(persistent, "jumin_voice", False)
            else:
                textbutton "Off" text_style "voice_toggle_off" action SetField(persistent, "jumin_voice", True)

            if persistent.zen_voice:
                textbutton "On" text_style "voice_toggle_on" action SetField(persistent, "zen_voice", False)
            else:
                textbutton "Off" text_style "voice_toggle_off" action SetField(persistent, "zen_voice", True)
                
            if persistent.seven_voice:
                textbutton "On" text_style "voice_toggle_on" action SetField(persistent, "seven_voice", False)
            else:
                textbutton "Off" text_style "voice_toggle_off" action SetField(persistent, "seven_voice", True)


        
        grid 2 3:
            xpos 300
            spacing 40
            transpose True
            text "Yoosung★" style "settings_style"
            text "Jaehee Kang" style "settings_style"
            text "Others" style "settings_style"

            if persistent.yoosung_voice:
                textbutton "On" text_style "voice_toggle_on" action SetField(persistent, "yoosung_voice", False)
            else:
                textbutton "Off" text_style "voice_toggle_off" action SetField(persistent, "yoosung_voice", True)

            if persistent.jaehee_voice:
                textbutton "On" text_style "voice_toggle_on" action SetField(persistent, "jaehee_voice", False)
            else:
                textbutton "Off" text_style "voice_toggle_off" action SetField(persistent, "jaehee_voice", True)
                
            if persistent.other_voice:
                textbutton "On" text_style "voice_toggle_on" action SetField(persistent, "other_voice", False)
            else:
                textbutton "Off" text_style "voice_toggle_off" action SetField(persistent, "other_voice", True)

  
image header_plus = "Phone UI/Main Menu/header_plus.png"
image header_plus_hover = "Phone UI/Main Menu/header_plus_hover.png"
image header_tray = "Phone UI/Main Menu/header_tray.png"
image header_hg = "Phone UI/Main Menu/header_hg.png"
image header_heart = "Phone UI/Main Menu/header_heart.png"
  
########################################################
## Just the header that often shows up over menu items;
## put in a separate screen for less repeating code
########################################################


#Analogue or Digital, hours, minutes, size, second hand, military time
default my_menu_clock = Clock(False, 0, 0, 230, False, False) 
    
screen menu_header(title):

    $ my_menu_clock.runmode("real")
    hbox:
        add my_menu_clock xalign 0.0 yalign 0.0 xpos -50
        $ am_pm = time.strftime('%p', time.localtime())
        text am_pm style 'header_clock' 
    
    
    window:
        maximum(600, 80)
        yalign 0.01
        xalign 0.86
        hbox:
            yalign 0.01
            xalign 0.5
            add 'header_tray'
            imagebutton:
                idle "header_plus"
                hover "header_plus_hover"
                action Return
            add 'header_tray'
            
        add "header_hg" yalign 0.1 xalign 0.16
        add "header_heart" yalign 0.1 xalign 0.65
        
        text "[persistent.HG]" style "hg_heart_points" xalign 0.35 yalign 0.01
        text "[persistent.HP]" style "hg_heart_points" xalign 0.83 yalign 0.01
        
        
    ## Header
    if title != "Original Story":
        window:
            ymaximum 80
            yalign 0.058
            add "menu_header"
            
        text title color "#ffffff" size 40 xalign 0.5 text_align 0.5 yalign 0.072
        
        # Back button
        imagebutton:
            xalign 0.013
            yalign 0.068
            idle "menu_back"
            focus_mask None
            hover im.FactorScale("Phone UI/Main Menu/menu_back_btn.png", 1.1)
            action [ToggleVariable("greeted", False, False), Return()]
        
    # Settings gear
    if title != "Setings":
        imagebutton:
            xalign 0.98
            yalign 0.01
            idle "settings_gear"
            hover "settings_gear_rotate"
            focus_mask None
            action ShowMenu("preferences")  
      
image menu_tab_inactive = Frame("Phone UI/Main Menu/settings_tab_inactive.png",10,10)
image menu_tab_active = Frame("Phone UI/Main Menu/settings_tab_active.png",25,25)
image menu_tab_inactive_hover = Frame("Phone UI/Main Menu/settings_tab_inactive_hover.png",10,10)
  
########################################################
## The three tabs on the Settings screen
########################################################

screen settings_tabs(active_tab):

    # "Backgrounds" of the different panels
    window:
        xalign 0.5
        yalign 0.14
        maximum(700,70)
        has hbox
        spacing 10
        # Account / Sound / Others tab
        window:
            maximum(231,57)
            imagebutton:
                if active_tab == "Profile":
                    idle "menu_tab_active"
                else:
                    idle "menu_tab_inactive"
                    hover "menu_tab_inactive_hover"
                    action Show("profile_pic", Dissolve(0.5))
            text "Profile" style "settings_style" xalign 0.5 yalign 0.5
        window:
            maximum(231,57)
            imagebutton:
                if active_tab == "Sound":
                    idle "menu_tab_active"
                else:
                    idle "menu_tab_inactive"
                    hover "menu_tab_inactive_hover"
                    action Show("preferences", Dissolve(0.5))
            text "Sound" style "settings_style" xalign 0.5 yalign 0.5
                
        window:
            maximum(231,57)
            imagebutton:
                if active_tab == "Others":
                    idle "menu_tab_active"
                else:
                    idle "menu_tab_inactive"
                    hover "menu_tab_inactive_hover"
                    action Show("other_settings",Dissolve(0.5))
            text "Others" style "settings_style" xalign 0.5 yalign 0.5
                
                
image menu_header = Frame("Phone UI/Main Menu/menu_header.png", 0, 50) 
image menu_back = "Phone UI/Main Menu/menu_back_btn.png"
image save_btn = "Phone UI/Main Menu/menu_save_btn.png"
image load_btn = "Phone UI/Main Menu/menu_load_btn.png"
image name_line = "Phone UI/Main Menu/menu_underline.png"
image menu_edit = "Phone UI/Main Menu/menu_pencil_long.png"



image MC_profpic = ConditionSwitch(
    "persistent.MC_pic == 1", im.FactorScale("Profile Pics/MC/MC-1.png",3.3),
    "persistent.MC_pic == 2", im.FactorScale("Profile Pics/MC/MC-2.png",3.3),
    "persistent.MC_pic == 3", im.FactorScale("Profile Pics/MC/MC-3.png",3.3),
    "persistent.MC_pic == 4", im.FactorScale("Profile Pics/MC/MC-4.png",3.3),
    "persistent.MC_pic == 5", im.FactorScale("Profile Pics/MC/MC-5.png",3.3),
    "True", "Profile Pics/MC/MC-1.png")
     
     
image radio_on = "Phone UI/Main Menu/menu_radio_on.png"
image radio_off = "Phone UI/Main Menu/menu_radio_off.png"

image settings_gear = "Phone UI/Main Menu/menu_settings_gear.png"
# Just for fun, this is the animation when you hover over the settings
# button. It makes the gear look like it's turning
image settings_gear_rotate:
    "Phone UI/Main Menu/menu_settings_gear.png"
    xpos 10
    ypos -10
    block:
        rotate 0
        linear 1.0 rotate 45
        repeat

        
default cantype = False

image menu_check_edit = "Phone UI/Main Menu/menu_check_long.png"

########################################################
## The "Profile" tab of Settings. Allows you to change
## your profile pic, name, and preferred pronouns
########################################################

screen profile_pic:
    
    tag menu
        
    # This defines the 'starry night' background with a few animated stars
    # You can see them defined in 'starry night bg.rpy'
    use starry_night

    use settings_tabs("Profile")  
    
    window:
        yalign 0.7
        xalign 0.05
        maximum(325, 900)
        ## Edit MC's Name
        add "name_line" xalign 0.079 yalign 0.475
        
        $ input = Input(value=MyInputValue("persistent.name", persistent.name), style="my_input", length=20)
            
        button:        
            style "input_img_answer"
            action ToggleVariable('cantype', False, True)        
            if cantype:
                add input
            else:
                text persistent.name style "my_input"
        
        imagebutton:
            if not cantype:
                idle "menu_edit"
            else:
                idle "menu_check_edit"
            focus_mask None
            xalign 0.06 #0.475
            yalign 0.453 #0.457
            if not cantype:
                hover im.FactorScale("Phone UI/Main Menu/menu_pencil_long.png",1.03)
            else:
                hover im.FactorScale("Phone UI/Main Menu/menu_check_long.png",1.03)
            action ToggleVariable('cantype', False, True)  

        ## MC's profile picture
        imagebutton:
            idle "MC_profpic"
            xalign 0.055
            #yalign 0.212
            action [MC_pic_change, renpy.restart_interaction]
            focus_mask True
      
    ## Not in MysMe; pick your pronouns
    window:
        style "pronoun_window"
        
        has vbox
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
                       
        
        
    use menu_header("Settings")
    
            
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
        
        
    ## Possibly temporary, but shows how many heart points you've earned
    ## with each character
    
    grid 4 4:
        xalign 0.5
        yalign 0.95
        add 'greet jaehee'
        add 'greet jumin'
        add 'greet ray'
        add 'greet rika'
        
        text str(heart_points['ja']) + " {image=header_heart}" style "point_indicator"
        text str(heart_points['ju']) + " {image=header_heart}" style "point_indicator"
        text str(heart_points['sa']) + " {image=header_heart}" style "point_indicator"
        text str(heart_points['r']) + " {image=header_heart}" style "point_indicator"
        
        add 'greet seven'
        add 'greet v'
        add 'greet yoosung'
        add 'greet zen'
        
        text str(heart_points['s']) + " {image=header_heart}" style "point_indicator"
        text str(heart_points['v']) + " {image=header_heart}" style "point_indicator"
        text str(heart_points['y']) + " {image=header_heart}" style "point_indicator"
        text str(heart_points['z']) + " {image=header_heart}" style "point_indicator" 
    

                
image menu_select_btn = "Phone UI/Main Menu/menu_select_button.png"
image menu_account_btn = "Phone UI/Main Menu/menu_account_button.png"
image menu_select_btn_hover = "Phone UI/Main Menu/menu_select_button_hover.png"

########################################################
## The "Others" tab of the settings screen
## Includes VN options and Ringtone selection
########################################################
              
screen other_settings():

    tag menu

    #add "Phone UI/Main Menu/menu_settings_bg.png"
    use starry_night
    use menu_header("Settings")
    use settings_tabs("Others")
        
    window:
        maximum(700, 800)
        xalign 0.5
        yalign 0.5
        has vbox
        spacing 30
            
        window:
            maximum(675,350)
            add "menu_settings_panel"
            text "Ringtone" style "settings_style" xpos 55 ypos 5
            
        window:
            maximum(675,320)
            add "menu_settings_panel"
            text "VN Settings" style "settings_style" xpos 55 ypos 5

            vbox:
                xalign 0.2
                yalign 0.5
                style_prefix "check"
                label _("Skip")
                textbutton _("Unseen Text") action Preference("skip", "toggle")
                textbutton _("After Choices") action Preference("after choices", "toggle")
                textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

            ## Additional vboxes of type "radio_pref" or "check_pref" can be
            ## added here, to add additional creator-defined preferences.
            
        window:
            maximum (517, 116)
            xalign 0.5
            has hbox
            spacing 40
            imagebutton:
                idle "menu_select_btn"
                hover "menu_select_btn_hover"
                action [ToggleVariable("greeted", False, False), ShowMenu("main_menu")]
            imagebutton:
                idle "menu_select_btn"
                hover "menu_select_btn_hover"
                action Show("confirm", message="Are you sure you want to start over? You'll be unable to return to this point except through a save file.", yes_action=[Hide('confirm'), Jump("restart_game")], no_action=Hide('confirm'))

    hbox:
        spacing 90
        xalign 0.45
        yalign 0.812
        window:
            maximum(190,100)
            text "Go to Mode Select" style "mode_select"
            
        window:
            maximum(190,100)
            text "Start Over" style "mode_select"
            
            
# *********************************
# Restart Game -- resets variables
# *********************************       
label restart_game:
    python:
        # removes heart points from all the characters
        for key in heart_points:
            newVal = {key: 0}
            heart_points.update(newVal)
        
    # presumably some more resets here
    call screen main_menu

########################################################
## The 'homepage' from which you interact with the game
## after the main menu
########################################################

image gray_chatbtn = "Phone UI/Main Menu/Original Story/main01_chatbtn.png"
image gray_chatbtn_hover = "Phone UI/Main Menu/Original Story/main01_chatbtn_hover.png"
image rfa_chatcircle:
    "Phone UI/Main Menu/Original Story/main01_chatcircle.png"
    block:
        rotate 0
        alignaround(.5, .5)
        linear 13.0 rotate 360
        repeat
        
image blue_chatcircle:
    "Phone UI/Main Menu/Original Story/main01_chatcircle_big.png"
    block:
        rotate 60
        alignaround(.5, .5)
        linear 4 rotate 420
        repeat
image chat_text = "Phone UI/Main Menu/Original Story/main01_chattext.png"
image chat_icon = "Phone UI/Main Menu/Original Story/main01_chaticon.png"

image gray_mainbtn = "Phone UI/Main Menu/Original Story/main01_mainbtn.png"
image blue_mainbtn = "Phone UI/Main Menu/Original Story/main01_mainbtn_lit.png"
image gray_mainbtn_hover = "Phone UI/Main Menu/Original Story/main01_mainbtn_hover.png"
image blue_mainbtn_hover = "Phone UI/Main Menu/Original Story/main01_mainbtn_lit_hover.png"
image gray_maincircle:
    "Phone UI/Main Menu/Original Story/main01_maincircle.png"
    block:
        rotate -120
        alignaround(.5, .5)
        linear 4 rotate -480
        repeat
image blue_maincircle:
    "Phone UI/Main Menu/Original Story/main01_maincircle_lit.png"
    block:
        rotate 180
        alignaround(.5, .5)
        linear 4 rotate 540
        repeat
image call_mainicon = "Phone UI/Main Menu/Original Story/main01_mainicon_call.png"
image email_mainicon = "Phone UI/Main Menu/Original Story/main01_mainicon_email.png"
image msg_mainicon = "Phone UI/Main Menu/Original Story/main01_mainicon_message.png"
image call_maintext = "Phone UI/Main Menu/Original Story/main01_maintext_call.png"
image email_maintext = "Phone UI/Main Menu/Original Story/main01_maintext_email.png"
image msg_maintext = "Phone UI/Main Menu/Original Story/main01_maintext_message.png"

image profile_pic_select_square = "Phone UI/Main Menu/Original Story/profile_pic_select_square.png"

image white_hex = "Phone UI/Main Menu/Original Story/main01_subbtn.png"
image blue_hex = "Phone UI/Main Menu/Original Story/main01_subbtn_lit.png"
image red_hex = "Phone UI/Main Menu/Original Story/main01_subbtn_shop.png"
image white_hex_hover = "Phone UI/Main Menu/Original Story/main01_subbtn_hover.png"
image blue_hex_hover = "Phone UI/Main Menu/Original Story/main01_subbtn_lit_hover.png"
image red_hex_hover = "Phone UI/Main Menu/Original Story/main01_subbtn_shop_hover.png"

image album_icon = "Phone UI/Main Menu/Original Story/main01_subicon_album.png"
image guest_icon = "Phone UI/Main Menu/Original Story/main01_subicon_guest.png"
image link_icon = "Phone UI/Main Menu/Original Story/main01_subicon_link.png"
image notice_icon = "Phone UI/Main Menu/Original Story/main01_subicon_notice.png"
image shop_icon = "Phone UI/Main Menu/Original Story/main01_subicon_shop.png"
image album_text = "Phone UI/Main Menu/Original Story/main01_subtext_album.png"
image guest_text = "Phone UI/Main Menu/Original Story/main01_subtext_guest.png"
image link_text = "Phone UI/Main Menu/Original Story/main01_subtext_link.png"
image notice_text = "Phone UI/Main Menu/Original Story/main01_subtext_notice.png"
image shop_text = "Phone UI/Main Menu/Original Story/main01_subtext_shop.png"

### Spaceship

image space_chip_active:
    "Phone UI/Main Menu/Original Story/Spaceship/spaceship_chip_inactive.png"
    2.7
    block:
        "Phone UI/Main Menu/Original Story/Spaceship/spaceship_chip_active.png"
        1.16
        "Phone UI/Main Menu/Original Story/Spaceship/spaceship_chip_glow.png"
        1.16
        repeat
    
image space_chip_explode = "Phone UI/Main Menu/Original Story/Spaceship/spaceship_chip_explode.png"
image space_chip_inactive = "Phone UI/Main Menu/Original Story/Spaceship/spaceship_chip_inactive.png"
image space_dot_line = "Phone UI/Main Menu/Original Story/Spaceship/dot_line.png"
image space_gray_dot = "Phone UI/Main Menu/Original Story/Spaceship/spaceship_dot_white.png"
image space_yellow_dot = "Phone UI/Main Menu/Original Story/Spaceship/spaceship_dot_yellow.png"
image space_transparent_btn = "Phone UI/Main Menu/Original Story/Spaceship/space-transparent-button.png"

image spaceship = "Phone UI/Main Menu/Original Story/Spaceship/spaceship_craft.png"
    

image space_flame:
    "Phone UI/Main Menu/Original Story/Spaceship/spaceship_flame_big.png"
    0.6
    "Phone UI/Main Menu/Original Story/Spaceship/spaceship_flame_small.png"
    0.6
    repeat
    
default chips_available = False
default spaceship_xalign = 0.04
default reset_spaceship_pos = False

screen chat_home:

    tag menu     
    
    $ mc_pic = 'Profile Pics/MC/MC-' + str(persistent.MC_pic) + '.png'
    
   
   
    #add "Phone UI/Main Menu/Original Story/main-bkgd.png"
    use starry_night
    
    use menu_header("Original Story")
  
    
    # Text Messages
    window:
        maximum(168,168)
        xalign 0.62
        yalign 0.195
        # if new_texts:
        imagebutton:
            idle "gray_mainbtn"
            hover "gray_mainbtn_hover"
            action Return()
        add "gray_maincircle" xalign 0.5 yalign 0.5
        add "msg_mainicon" xalign 0.5 yalign 0.5
        add "msg_maintext" xalign 0.5 yalign 0.85
        
    # Calls
    window:
        maximum(168,168) 
        xalign 0.91
        yalign 0.35
        # if new_call:
        imagebutton:
            idle "blue_mainbtn"
            hover "blue_mainbtn_hover"
            action Return()
        add "blue_maincircle" xalign 0.5 yalign 0.5
        add "call_mainicon" xalign 0.5 yalign 0.5
        add "call_maintext" xalign 0.5 yalign 0.85
     
    # Emails
    window:
        maximum(168,168)
        xalign 0.342
        yalign 0.33
        # if new_email:
        imagebutton:
            idle "gray_mainbtn"
            hover "gray_mainbtn_hover"
            action ToggleVariable('chips_available', False, True)
        add "gray_maincircle" xalign 0.5 yalign 0.5
        add "email_mainicon" xalign 0.5 yalign 0.5
        add "email_maintext" xalign 0.5 yalign 0.85
        
    window:
        maximum(305,305)
        xalign 0.65
        yalign 0.722
        imagebutton:
            idle "gray_chatbtn"
            hover "gray_chatbtn_hover"
            action Return()
        add "rfa_chatcircle" yalign 0.5 xalign 0.5
        add "blue_chatcircle" xalign 0.5 yalign 0.5
        add "chat_icon" xalign 0.5 yalign 0.5
        add "chat_text" xalign 0.5 yalign 0.8
       
    # Note that the number of pictures changes depending on
    # whether you're in Another Story or Casual/Deep Story,
    # but here I've chosen to include all the characters
    # Also usually the characters have "generic" profile
    # pictures, but I've chosen to simply include their actual
    # profile picture at the time
    window:
        maximum(741, 206)
        xalign 0.5
        yalign 0.08
        vbox:
            spacing 8
            hbox:
                spacing 8
                xalign 0.0
                yalign 0.0
                imagebutton:
                    hover "profile_pic_select_square"                    
                    idle im.FactorScale(chatportrait['Ju'], 0.9)
                    background im.FactorScale(chatportrait['Ju'], 0.9)
                    action Return()
                imagebutton:
                    idle im.FactorScale(chatportrait['Zen'], 0.9)
                    hover "profile_pic_select_square"
                    background im.FactorScale(chatportrait['Zen'], 0.9)
                    action Return()
                imagebutton:
                    idle im.FactorScale(chatportrait['Sev'], 0.9)
                    hover "profile_pic_select_square"
                    background im.FactorScale(chatportrait['Sev'], 0.9)
                    action Return()
                imagebutton:
                    idle im.FactorScale(chatportrait['Yoo'], 0.9)
                    hover "profile_pic_select_square"
                    background im.FactorScale(chatportrait['Yoo'], 0.9)
                    action Return()
                imagebutton:
                    idle im.FactorScale(chatportrait['Ja'], 0.9)
                    hover "profile_pic_select_square"
                    background im.FactorScale(chatportrait['Ja'], 0.9)
                    action Return()
                imagebutton:
                    idle im.FactorScale(chatportrait['V'], 0.9)
                    hover "profile_pic_select_square"
                    background im.FactorScale(chatportrait['V'], 0.9)
                    action Return()
                imagebutton:
                    idle im.FactorScale(mc_pic, 0.9)
                    hover "profile_pic_select_square"
                    background im.FactorScale(mc_pic, 0.9)
                    action ShowMenu('profile_pic')
            hbox:
                spacing 8
                imagebutton:
                    idle im.FactorScale(chatportrait['Ray'], 0.9)
                    hover "profile_pic_select_square"
                    background im.FactorScale(chatportrait['Ray'], 0.9)
                    action Return()
                imagebutton:
                    idle im.FactorScale(chatportrait['Rika'], 0.9)
                    hover "profile_pic_select_square"
                    background im.FactorScale(chatportrait['Rika'], 0.9)
                    action Return()

    window:
        maximum(140, 1000)
        xalign 0.03
        yalign 0.62
        has vbox
        spacing 20
        # Album
        window:
            maximum(130,149)
            imagebutton:
                idle "white_hex"
                hover "white_hex_hover"
                action Return()
            add "album_icon" xalign 0.5 yalign 0.4
            add "album_text" xalign 0.5 yalign 0.8
            
        # Guest
        window:
            maximum(130,149)
            imagebutton:
                idle "white_hex"
                hover "white_hex_hover"
                action Return()
            add "guest_icon" xalign 0.5 yalign 0.4
            add "guest_text" xalign 0.5 yalign 0.8
            
        # Shop
        window:
            maximum(130,149)
            imagebutton:
                idle "red_hex"
                hover "red_hex_hover"
                action Show("chip_tap")
            add "shop_icon" xalign 0.55 yalign 0.4
            add "shop_text" xalign 0.5 yalign 0.8
            
        # Notice
        window:
            maximum(130,149)
            imagebutton:
                idle "white_hex"
                hover "white_hex_hover"
                action Return()
            add "notice_icon" xalign 0.5 yalign 0.4
            add "notice_text" xalign 0.5 yalign 0.8
            
        # Link
        window:
            maximum(130,149)
            imagebutton:
                idle "white_hex"
                hover "white_hex_hover"
                action Return()
            add "link_icon" xalign 0.5 yalign 0.4
            add "link_text" xalign 0.5 yalign 0.8
            
            
    ## Spaceship    
    add "dot_line" xalign 0.5 yalign .97
        
    #text str(reset_spaceship_pos) + ' - ' + str(spaceship_xalign) color '#fff'
    $ spaceship_xalign = spaceship_get_xalign(True)
    
    if chips_available:       
        window at chip_anim:
            maximum(90,70)
            xalign 0.93
            yalign 0.942
            add "space_chip_explode"
            
        add "space_chip_active" xalign 0.92 yalign 0.98
        
        window at spaceship_chips:
            maximum (100,110)
            xalign 0.96
            yalign 1.0
            add "space_flame" xalign 0.5 yalign 1.0
            add "spaceship" xalign 0.5 yalign 0.0
            imagebutton:
                idle "space_transparent_btn"
                focus_mask None
                activate_sound 'sfx/UI/select_6.mp3'
                action Show('chip_tap')
      
    else:            
        add "space_chip_inactive" xalign 0.92 yalign 0.98
        
        window at spaceship_flight:
            maximum (100,110)
            xalign 0.04#spaceship_xalign
            yalign 1.0
            add "space_flame" xalign 0.5 yalign 1.0
            add "spaceship" xalign 0.5 yalign 0.0
     
image space_chip = "Phone UI/Main Menu/Original Story/Spaceship/chip.png"
image space_tap_large:
    "Phone UI/Main Menu/Original Story/Spaceship/tap_0.png"
    0.55
    "Phone UI/Main Menu/Original Story/Spaceship/tap_1.png"
    0.6
    repeat
image space_tap_med:
    "Phone UI/Main Menu/Original Story/Spaceship/tap_1.png"
    0.62
    "Phone UI/Main Menu/Original Story/Spaceship/tap_0.png"
    0.45
    repeat
image space_tap_small:
    "Phone UI/Main Menu/Original Story/Spaceship/tap_0.png"
    0.48
    "Phone UI/Main Menu/Original Story/Spaceship/tap_1.png"
    0.56
    repeat
    
image space_tap_to_close = "Phone UI/Main Menu/Original Story/Spaceship/close.png"

image cloud_1 = "Phone UI/Main Menu/Original Story/Spaceship/cloud_1.png"
image cloud_2 = "Phone UI/Main Menu/Original Story/Spaceship/cloud_2.png"
image cloud_3 = "Phone UI/Main Menu/Original Story/Spaceship/cloud_3.png"
image cloud_4 = "Phone UI/Main Menu/Original Story/Spaceship/cloud_4.png"
image cloud_5 = "Phone UI/Main Menu/Original Story/Spaceship/cloud_5.png"

screen chip_tap:

    modal True

    zorder 100
    
    add "Phone UI/choice_dark.png"
    window at chip_wobble:
        maximum(481,598)
        xalign 0.5
        yalign 0.6
        imagebutton:
            idle "space_chip"
            activate_sound 'sfx/UI/select_6.mp3'
            action Jump('chip_prize')
        add 'space_tap_large' at large_tap
        add 'space_tap_med' at med_tap
        add 'space_tap_small' at small_tap
        
    
 
label chip_prize:
    #$ reset_spaceship_pos = True
    #$ spaceship_xalign = 0.04
    hide screen chip_tap
    show screen chip_cloud
    #show screen chat_home
    pause 2.5
    hide screen chip_cloud 
    $ chips_available = False
    call screen chip_end
 
screen chip_cloud:
    modal True

    zorder 100
    
    
    
    add "Phone UI/choice_dark.png"
    window at chip_wobble2:
        maximum(481,598)
        xalign 0.5
        yalign 0.6
        add "space_chip"
        
    #add "Phone UI/Main Menu/Original Story/Spaceship/cloud_bkgd.png"
    
    window at hide_dissolve:
        maximum(750,640)
        xalign 0.5
        yalign 0.6
        add 'cloud_1' xpos 735 ypos 500 at cloud_shuffle1
        add 'cloud_2' xpos -20 ypos 310 at cloud_shuffle2
        add 'cloud_3' xpos 10 ypos 300 at cloud_shuffle3
        add 'cloud_4' xpos 300 at cloud_shuffle4
        add 'cloud_5' xpos 350 ypos 20 at cloud_shuffle5
        
image spotlight:
    "Phone UI/Main Menu/Original Story/Spaceship/spotlight.png"
    alpha 0.6
    block:
        rotate 0
        linear 15.0 rotate 360
        repeat
        
image space_prize_box = "Phone UI/Main Menu/Original Story/Spaceship/space_prize_box.png"
image space_black_box = Frame("Phone UI/Main Menu/Original Story/Spaceship/main03_black_box.png",30,30,30,30)
image space_continue = "Phone UI/Main Menu/Original Story/Spaceship/Continue.png"
image space_continue_hover = "Phone UI/Main Menu/Original Story/Spaceship/Continue_hover.png"
default prize_hg = 10

screen chip_end:
    modal True

    zorder 100
    
    $ prize_heart = renpy.random.randint(1, 130)
    $ new_hp_total = persistent.HP + prize_heart
    
    add "Phone UI/choice_dark.png"   

    add 'spotlight' xalign 0.5 yalign 0.0
    
    window:
        maximum(481,598)
        xalign 0.5
        yalign 0.6
        add "space_chip"
        
    window:
        maximum(647,270)
        xalign 0.5 yalign 0.55
        background 'space_prize_box'
            
        hbox:
            spacing 70
            xalign 0.5
            yalign 0.55
            window:
                maximum(200,60)
                background 'space_black_box'
                text str(prize_heart) style 'chip_prize_text'
                add 'header_heart' xalign 0.15 yalign 0.5
                
                
            window:
                maximum(200,60)
                background 'space_black_box'
                text '0' style 'chip_prize_text'
                add 'header_hg' xalign 0.15 yalign 0.5
                
                
        text 'A clump of cat hair.' style 'chip_prize_description'
        imagebutton:
            idle 'space_continue'
            hover 'space_continue_hover'
            xalign 0.5
            yalign 0.85
            action [SetField(persistent, 'HP', new_hp_total), Hide('chip_end'), Show('chat_home', Dissolve(0.5))]
        

        
    
    
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
        
        
        
        
        
        
        
        
