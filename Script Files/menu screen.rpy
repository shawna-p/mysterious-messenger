init python:

    import time

    # Used to get the player's name from input
    class MyInputValue(InputValue):
            def __init__(self, var, default=""):
                self.var = var
                
                if not hasattr(store, var):
                    setattr(store, var, default)
                                        
            def get_text(self):
                return getattr(store, self.var)
                
            def set_text(self, s):
                global name, m
            
                s = s.strip()
                setattr(store, self.var, s)  
                persistent.name = s
                renpy.save_persistent()
                name = persistent.name  

                m.name = name 
                renpy.retain_after_load()                
                
                
            def enter(self):
                renpy.run(self.Disable())                
                raise renpy.IgnoreEvent()
               
    # This lets you change the MC's profile picture by clicking on it
    # Currently you can only use the pre-set images, not upload your own
    def MC_pic_change():   
        if persistent.MC_pic == 5:
            persistent.MC_pic = 1
        else:
            persistent.MC_pic += 1
            
        global m
        thepic = 'Profile Pics/MC/MC-[persistent.MC_pic].png'
        m.prof_pic = thepic
        renpy.retain_after_load()
        
    ## This picks a greeting depending on the time of day and plays it
    def chat_greet(hour, greet_char):  
        global greeted, greet_text_english, greet_text_korean
        greeted = True
        greet_text_english = "Welcome to my Mystic Messenger Generator!"
        
        if hour >= 6 and hour < 12:  # morning
            greet_text_english = "Good morning! " + greet_text_english
            
            num_greetings = len(morning_greeting[greet_char])
            the_greeting = renpy.random.randint(1, num_greetings) - 1
            renpy.play(morning_greeting[greet_char][the_greeting].sound_file, channel="voice_sfx")
            
        elif hour >=12 and hour < 18:    # afternoon
            greet_text_english = "Good afternoon! " + greet_text_english
            
            num_greetings = len(afternoon_greeting[greet_char])
            the_greeting = renpy.random.randint(1, num_greetings) - 1
            renpy.play(afternoon_greeting[greet_char][the_greeting].sound_file, channel="voice_sfx")
            
        elif hour >= 18 and hour < 22:  # evening
            greet_text_english = "Good evening! " + greet_text_english
            
            num_greetings = len(evening_greeting[greet_char])
            the_greeting = renpy.random.randint(1, num_greetings) - 1
            renpy.play(evening_greeting[greet_char][the_greeting].sound_file, channel="voice_sfx")
            
        elif hour >= 22 or hour < 2: # night
            greet_text_english = "It's getting late! " + greet_text_english
            
            num_greetings = len(night_greeting[greet_char])
            the_greeting = renpy.random.randint(1, num_greetings) - 1
            renpy.play(night_greeting[greet_char][the_greeting].sound_file, channel="voice_sfx")
            
        else:   # late night/early morning
            greet_text_english = "You're up late! " + greet_text_english
            
            num_greetings = len(late_night_greeting[greet_char])
            the_greeting = renpy.random.randint(1, num_greetings) - 1
            renpy.play(late_night_greeting[greet_char][the_greeting].sound_file, channel="voice_sfx")
        
        
    # This is used to make the spaceship float to a random location on the line
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
        
    # Returns a random position along the spaceship line at the bottom
    # of the screen
    def spaceship_get_xalign(new_num=False):
        global spaceship_xalign
        if new_num:
            spaceship_xalign = renpy.random.random()
            spaceship_xalign = spaceship_xalign * 0.8 + 0.04
        return spaceship_xalign
        
    # Sets the player's pronouns, if they change them
    def set_pronouns():
        global they, them, their, theirs, themself
        if persistent.pronoun == "female":
            they = "she"
            them = "her"
            their = "her"
            theirs = "hers"
            themself = "herself"
        elif persistent.pronoun == "male":
            they = "he"
            them = "him"
            their = "his"
            theirs = "his"
            themself = "himself"
        elif persistent.pronoun == "nonbinary":
            they = "they"
            them = "them"
            their = "their"
            theirs = "theirs"
            themself = "themself"
        renpy.retain_after_load()
        

# This lets it randomly pick a profile picture to display        
default greet_char = "seven"
define greet_list = ['jaehee', 'jumin', 'ray', 'rika', 'seven', 
                                 'unknown', 'v', 'yoosung', 'zen']

# Greeting Text
# (Eventually these will be stored in the Day_Greet object to be
# pulled alongside the sound file)
default greet_text_korean = "제 프로그램으로 환영합니다!"
default greet_text_english = "Welcome to my Mystic Messenger Generator!"

# A variable that keeps track of whether or not the player has been "greeted"
# in order to prevent it from constantly greeting you when you switch screens
default greeted = False


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
## Also shows a greeting from a random character
##

screen main_menu:

    tag menu
    
    $ renpy.music.play(mystic_chat, loop=True)
    
    python:
        thepic = 'Profile Pics/MC/MC-[persistent.MC_pic].png'
        if m.prof_pic != thepic:
            m.prof_pic = thepic
            
        if m.name != persistent.name:
            m.name = persistent.name
            
        hour = time.strftime('%H', time.localtime())
        hour = int(hour)    # gets the hour, makes it an int
        greet_char = renpy.random.choice(greet_list)
        if not greeted:
            chat_greet(hour, greet_char)
        
    
    # This defines the 'starry night' background with a few animated stars
    # You can see them defined in 'starry night bg.rpy'
    use starry_night
        
        
    ## Greeting Bubble/Dialogue
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
        text "{size=-2}" + "[greet_text_korean]" + "{/size}" style "greet_text"
        text "[greet_text_english]" style "greet_text" yalign 0.5

    
    # The main menu buttons. Note that many currently don't take you to the screen you'd want
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
                    button:
                        focus_mask True
                        background "left_corner_menu"
                        hover_background "left_corner_menu_selected"
                        activate_sound "sfx/UI/select_4.mp3"
                        if persistent.on_route:
                            action FileLoad(mm_auto) #[QuickLoad(False)]
                        else:
                            action Show('route_select_screen') #TODO: This screen
                        
                    vbox:    
                        align(0.5, 0.5)
                        add "menu_original_story" xpos 20
                        text "Original\nStory" style "menu_text_big"  ypos 15
                
                vbox:
                    window:
                        maximum(225, 210)
                        padding (10, 10)
                        # Save and Load
                        # Top Right
                        button:
                            focus_mask True
                            background "right_corner_menu" 
                            hover_background "right_corner_menu_selected"
                            action ShowMenu("load")    
                            
                        vbox:                               
                            align(0.5, 0.5)
                            add "menu_save_load" xpos 25
                            text "Save & Load" style "menu_text_small" ypos 10
                            
                    window:
                        maximum(225, 210)
                        padding (10, 10)
                        # After Ending
                        # Mid Right
                        button:
                            focus_mask True
                            background "right_corner_menu" 
                            hover_background "right_corner_menu_selected"
                            action Return
                            
                        vbox:                               
                            xcenter 0.5
                            ycenter 0.5
                            add "menu_after_ending" xpos 40
                            text "After Ending" style "menu_text_small" ypos 20
            hbox:
                window:
                    maximum(450,210)
                    padding (10, 10)
                    # History
                    # Bottom Left
                    button:
                        focus_mask True
                        background "left_corner_menu"
                        hover_background "left_corner_menu_selected"
                        action ToggleField(persistent, 'on_route', False)
                        
                    vbox:                               
                        align(0.5, 0.5)
                        add "menu_history" xpos 15 ypos 3
                        text "History" style "menu_text_big" ypos 13
                    
                window:
                    maximum(225, 210)
                    padding (10, 10)
                    # DLC
                    # Bottom Right
                    button:
                        focus_mask True
                        background "right_corner_menu" 
                        hover_background "right_corner_menu_selected"
                        action Show('create_archive')
                        
                    vbox:                               
                        align(0.5, 0.5)
                        add "menu_dlc"
                        text "DLC" style "menu_text_small" xpos 25 ypos 15
                    
                    
    
## A short, not completely implemented screen where you select
## which route you'd like to start on
screen route_select_screen:

    tag menu
    
    use starry_night
    
    use menu_header("Mode Select", MainMenu)

    window:
        maximum(700, 350)
        padding (10, 10)
        xalign 0.5
        yalign 0.5
        button:
            focus_mask True
            background "right_corner_menu" 
            hover_background "right_corner_menu_selected"
            action [ToggleField(persistent, 'on_route', True), next_chatroom, Start()] 
            
        text "Start Game" style "menu_text_small" xalign 0.5 yalign 0.5
    

  
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
    
    use menu_header(title, Show('profile_pic', Dissolve(0.5)))

    fixed:

        ## This ensures the input will get the enter event before any of the
        ## buttons do.
        order_reverse True

        #side ('l r'):
        #    spacing 10
        #    xysize(740, 1100)
        #    xalign 0.01
        #    yalign 0.68
            ## The grid of file slots.
        vpgrid id 'save_load_vp':
            # This is a vpgrid since originally you could scroll it down to 12 slots
            # (see the commented out numbers below), but it looks cleaner if I restrict
            # it to 7 rows and a page select vs. 12 scrollable columns and a page select
            # If you wanted to *just* have a very long viewport of saves, then you could just
            # remove the code for the page select and increase the number of rows
            xysize (745,1170) #(740, 1120)
            rows gui.file_slot_rows
            draggable True
            mousewheel True
            style_prefix "slot"
            scrollbars "vertical"
            side_spacing 12

            xalign 0.01
            yalign 1.0 #0.8

            spacing gui.slot_spacing
            
            # This adds the 'backup' save slot to the top when loading
            if title == "Load" and FileLoadable(mm_auto):
                $ save_title = current_chatroom.route + '|' + current_chatroom.day + '|' + current_chatroom.title
                if '|' in FileSaveName(mm_auto):
                    $ rt, dn, cn = FileSaveName(mm_auto).split('|')
                else:                    
                    $ rt, dn, cn = save_title.split('|')
            
                button:
                    background 'save_auto_idle'
                    hover_background 'save_auto_hover'
                    action FileAction(mm_auto)

                    hbox:
                        spacing 8
                        xsize 695
                        
                        window:
                            align (0.5, 0.5)
                            maximum(120, 120)
                            add 'save_' + rt xalign 0.5 yalign 0.5
                        
                        window:
                            xysize (400, 120)
                            yalign 0.0
                            has vbox
                            spacing 8
                            fixed:
                                ysize 75
                                text "This is a backup file that is auto-generated" style "save_slot_text" yalign 0.0
                            text "Today: [dn] DAY" style "save_slot_text" yalign 1.0

                        window:
                            maximum (155,120)
                            has vbox                            
                            fixed:
                                xsize 155
                                yfit True
                                text FileTime(mm_auto, format=_("{#file_time}%m/%d %H:%M"), empty=_("empty slot")):
                                    style "save_timestamp"                                
                            spacing 30
                            fixed:
                                xsize 155
                                yfit True
                                imagebutton:
                                    hover im.FactorScale("Phone UI/Main Menu/save_trash_hover.png",1.05)
                                    idle "Phone UI/Main Menu/save_trash.png"
                                    xalign 1.0
                                    action FileDelete(mm_auto)

                    key "save_delete" action FileDelete(mm_auto)

            for i in range(gui.file_slot_cols * gui.file_slot_rows):

                $ slot = i + 1
                
                
                $ save_title = current_chatroom.route + '|' + current_chatroom.day + '|' + current_chatroom.title
                if '|' in FileSaveName(slot):
                    $ rt, dn, cn = FileSaveName(slot).split('|')
                else:                    
                    $ rt, dn, cn = save_title.split('|')
               

                button:
                    if title == "Save":
                        action [SetVariable('save_name', save_title), FileAction(slot)]
                    else:
                        action FileAction(slot)

                    hbox:
                        spacing 8
                        xsize 695
                        
                        window:
                            maximum(120, 120)
                            align (0.5, 0.5)
                            # Adds the correct route image to the left
                            if FileLoadable(slot):
                                add 'save_' + rt xalign 0.5 yalign 0.5
                            else:
                                add 'save_empty' xalign 0.5 yalign 0.5
                        
                        window:
                            xysize (400, 120)
                            yalign 0.0
                            has vbox
                            spacing 8
                            # Displays the most recent chatroom title + day
                            if FileLoadable(slot):
                                fixed:
                                    ysize 75
                                    text "[cn]" style "save_slot_text" yalign 0.0
                                text "Today: [dn] DAY" style "save_slot_text" yalign 1.0
                            else:
                                fixed:
                                    ysize 75
                                    text "Empty Slot" style "save_slot_text" yalign 0.0
                                text "Tap an empty slot to save" style 'save_slot_text' yalign 1.0
                            
                        window:
                            maximum (155,120)
                            has vbox
                            # Displays the time the save was created and the delete button
                            fixed:
                                xsize 155
                                yfit True
                                text FileTime(slot, format=_("{#file_time}%m/%d %H:%M"), empty=_("empty slot")):
                                    style "save_timestamp"
                                
                            spacing 30

                            fixed:
                                xsize 155
                                yfit True
                                imagebutton:
                                    hover im.FactorScale("Phone UI/Main Menu/save_trash_hover.png",1.05)
                                    idle "Phone UI/Main Menu/save_trash.png"
                                    xalign 1.0
                                    action FileDelete(slot)

                    key "save_delete" action FileDelete(slot)




            

            
## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##

screen preferences():

    tag menu

    #add "Phone UI/Main Menu/menu_settings_bg.png"
    use starry_night
    use menu_header("Settings", Show('chat_home', Dissolve(0.5)))
    use settings_tabs("Sound")
    
    window:
        xysize(700, 1070)
        xalign 0.5
        yalign 0.95
        has vbox
        spacing 30
        xalign 0.5
        
  
        window:
            maximum(675,480)
            background "menu_settings_panel" padding(10,10)
            xalign 0.5
            has vbox
            spacing 30
            xalign 0.5
            yalign 0.34
            text "Sound" style "settings_style" xpos 55 ypos -5
            
            vbox:      
                spacing 15
                xsize 625
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
            
        window:
            maximum(675,620)
            background "menu_settings_panel" padding(10,10)
            has vbox
            xalign 0.5
            yalign 0.5
            spacing 15
            text "Voice" style "settings_style" xpos 185 ypos -5
            
            ## There are no actual voiced lines in this program, so right
            ## now all you get to do is toggle the button from on to off 
            hbox:
                xalign 0.5
                yalign 0.5
                spacing -35
                null width 165            
                grid 2 5:                
                    transpose True
                    spacing 40
                    align (0.5, 0.0)
                    
                    text "Jumin Han" style "settings_style"
                    text "ZEN" style "settings_style"
                    text "707" style "settings_style"
                    text "Ray" style "settings_style"
                    text "Others" style "settings_style"
                    
                    use voice_buttons('jumin')
                    use voice_buttons('zen')
                    use voice_buttons('seven')
                    use voice_buttons('saeran')
                    use voice_buttons('other')
                    
                
                grid 2 4:
                    spacing 40
                    transpose True
                    align (0.5, 0.0)
                    text "Yoosung★" style "settings_style"
                    text "Jaehee Kang" style "settings_style"
                    text "V" style "settings_style"
                    text "Rika" style "settings_style"
                    
                    use voice_buttons('yoosung')
                    use voice_buttons('jaehee')
                    use voice_buttons('v')
                    use voice_buttons('rika')

    
screen voice_buttons(voice_char):

    $ voice_char = voice_char + '_voice'
    
    button:
        xysize (120, 30)
        idle_child Text("On", style="voice_toggle_on")
        hover_child Text("On", style="voice_toggle_on")
        selected_child Text("Off", style="voice_toggle_off")
        action ToggleVoiceMute(voice_char)
        
    
########################################################
## Just the header that often shows up over menu items;
## put in a separate screen for less repeating code
########################################################


#Analogue or Digital, hours, minutes, size, second hand, military time
default my_menu_clock = Clock(False, 0, 0, 230, False, False) 
    
screen menu_header(title, return_action=NullAction, envelope=False):

    $ my_menu_clock.runmode("real")
    hbox:
        add my_menu_clock xalign 0.0 yalign 0.0 xpos -50
        $ am_pm = time.strftime('%p', time.localtime())
        text am_pm style 'header_clock' 
    
    
    if not persistent.first_boot:
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
                    if not renpy.get_screen("choice"):
                        action NullAction
                add 'header_tray'
                
            add "header_hg" yalign 0.1 xalign 0.16
            add "header_heart" yalign 0.1 xalign 0.65
            
            text "[persistent.HG]" style "hg_heart_points" xalign 0.35 yalign 0.01
            text "[persistent.HP]" style "hg_heart_points" xalign 0.83 yalign 0.01
        
        
    ## Header
    if title != "Original Story" and title != "In Call":
        window:
            ymaximum 80
            yalign 0.058
            add "menu_header"
            
        if not envelope:
            text title color "#ffffff" size 40 xalign 0.5 text_align 0.5 yalign 0.072
        else:
            hbox:
                xalign 0.5 
                yalign 0.072
                spacing 15
                add 'header_envelope' xalign 0.5 yalign 0.5
                text title color "#ffffff" size 40 text_align 0.5
        
        # Back button
        imagebutton:
            xalign 0.013
            yalign 0.068
            idle "menu_back"
            focus_mask None
            hover im.FactorScale("Phone UI/Main Menu/menu_back_btn.png", 1.1)
            if not renpy.get_screen("choice"):                
                if envelope:
                    action Show('text_message_hub', Dissolve(0.5))
                elif persistent.first_boot or not persistent.on_route:
                    action [SetField(persistent, 'first_boot', False), MainMenu(False)]
                else:
                    action return_action
                
        
    if not persistent.first_boot:
        # Settings gear
        if title != "Setings":
            imagebutton:
                xalign 0.98
                yalign 0.01
                idle "settings_gear"
                hover "settings_gear_rotate"
                focus_mask None
                if not renpy.get_screen("choice"):
                    action Show("preferences", Dissolve(0.5))  
      

  
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
        textbutton _('Profile'):
            text_style "settings_tabs" 
            xsize 231
            ysize 57
            if active_tab == "Profile":
                background "menu_tab_active"
            else:
                background "menu_tab_inactive"
                hover_background "menu_tab_inactive_hover"
                action Show("profile_pic", Dissolve(0.5))
                
        textbutton _('Sound'):
            text_style "settings_tabs" 
            xsize 231
            ysize 57
            if active_tab == "Sound":
                background "menu_tab_active"
            else:
                background "menu_tab_inactive"
                hover_background "menu_tab_inactive_hover"
                action Show("preferences", Dissolve(0.5))
            
        textbutton _('Others'):
            text_style "settings_tabs"  
            xsize 231
            ysize 57
            if active_tab == "Others":
                background "menu_tab_active"
            else:
                background "menu_tab_inactive"
                hover_background "menu_tab_inactive_hover"
                action Show("other_settings", Dissolve(0.5))              
                

        
########################################################
## The "Profile" tab of Settings. Allows you to change
## your profile pic, name, and preferred pronouns
########################################################

screen profile_pic:
    
    tag menu
        
    # This defines the 'starry night' background with a few animated stars
    # You can see them defined in 'starry night bg.rpy'
    use starry_night

    if not persistent.first_boot:
        use settings_tabs("Profile")  
    
    window:
        yalign 0.7
        xalign 0.05
        maximum(325, 900)
        ## Edit MC's Name
        add "name_line" xalign 0.079 yalign 0.475
        
        text persistent.name style "my_name"
        
        imagebutton:
            idle "menu_edit"
            focus_mask None
            xalign 0.06 #0.475
            yalign 0.453 #0.457
            hover im.FactorScale("Phone UI/Main Menu/menu_pencil_long.png",1.03)
            action Show('input_popup', prompt='Please input a name.') 

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
        button:     
            action [SetField(persistent, "pronoun", "female"), set_pronouns, renpy.restart_interaction]
            has hbox
            spacing 10
            if persistent.pronoun == "female":
                add "radio_on"
                text 'she/her' color '#fff' hover_color '#ddd'
            else:
                add "radio_off"            
                text 'she/her' hover_color '#fff' color '#ddd'
            
        button:
            action [SetField(persistent, "pronoun", "male"), set_pronouns, renpy.restart_interaction]
            has hbox
            spacing 10
            if persistent.pronoun == "male":
                add "radio_on"
                text 'he/him' color '#fff' hover_color '#ddd'
            else:
                add "radio_off"
                text 'he/him' hover_color '#fff' color '#ddd'
            
            
        button:
            action [SetField(persistent, "pronoun", "nonbinary"), set_pronouns, renpy.restart_interaction]
            has hbox
            spacing 10
            if persistent.pronoun == "nonbinary":
                add "radio_on"
                text 'they/them' color '#fff' hover_color '#ddd'
            else:
                add "radio_off"
                text 'they/them' hover_color '#fff' color '#ddd'
             
        
        
    if not persistent.first_boot:
        use menu_header("Settings", Show('chat_home', Dissolve(0.5)))
    else:
        use menu_header("Customize your Profile")
        
    if not persistent.first_boot:            
        ## Save / Load
        imagebutton:
            yalign 0.978
            xalign 0.66
            idle "save_btn"
            hover im.FactorScale("Phone UI/Main Menu/menu_save_btn.png",1.1)
            action Show("save", Dissolve(0.5))
            
        imagebutton:
            yalign 0.978
            xalign 0.974
            idle "load_btn"
            hover im.FactorScale("Phone UI/Main Menu/menu_load_btn.png",1.1)
            action Show("load", Dissolve(0.5))
        
        
        ## Possibly temporary, but shows how many heart points you've earned
        ## with each character
        
        grid 4 4:
            xalign 0.5
            yalign 0.95
            add 'greet jaehee'
            add 'greet jumin'
            add 'greet ray'
            add 'greet rika'
            
            text str(ja.heart_points) + " {image=header_heart}" style "point_indicator"
            text str(ju.heart_points) + " {image=header_heart}" style "point_indicator"
            text str(sa.heart_points) + " {image=header_heart}" style "point_indicator"
            text str(ri.heart_points) + " {image=header_heart}" style "point_indicator"
            
            add 'greet seven'
            add 'greet v'
            add 'greet yoosung'
            add 'greet zen'
            
            text str(s.heart_points) + " {image=header_heart}" style "point_indicator"
            text str(v.heart_points) + " {image=header_heart}" style "point_indicator"
            text str(y.heart_points) + " {image=header_heart}" style "point_indicator"
            text str(z.heart_points) + " {image=header_heart}" style "point_indicator" 
    

                
screen input_popup(prompt=''):

    zorder 100
    modal True
    
    $ old_name = persistent.name
    $ input = Input(value=MyInputValue("persistent.name", persistent.name), style="my_input", length=20)
    
    window:
        maximum(550,313)
        background 'input_popup_bkgr'
        xalign 0.5
        yalign 0.4
        imagebutton:
            align (1.0, 0.0)
            idle 'input_close'
            hover 'input_close_hover'
            action [Hide('input_popup'), SetField(m, 'name', old_name), SetVariable('name', old_name), SetField(persistent, 'name', old_name), renpy.retain_after_load, Show('profile_pic')]
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5
            text prompt color '#fff' xalign 0.5 text_align 0.5
            fixed:
                xsize 500 
                ysize 75
                xalign 0.5
                add 'input_square'
                add input  xalign 0.5 yalign 0.5
            textbutton _('Confirm'):
                text_style 'mode_select'
                xalign 0.5
                xsize 240
                ysize 80
                background 'menu_select_btn' padding(20,20)
                hover_background 'menu_select_btn_hover'
                action [Hide('input_popup'), Show('profile_pic')]


########################################################
## The "Others" tab of the settings screen
## Includes VN options and Ringtone selection
########################################################
              
screen other_settings():

    tag menu

    #add "Phone UI/Main Menu/menu_settings_bg.png"
    use starry_night
    use menu_header("Settings", Show('chat_home', Dissolve(0.5)))
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
            
            hbox:
                align (0.2, 0.5)
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")
            
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
            maximum (520, 130)
            xalign 0.5
            has hbox
            spacing 40
            textbutton _('Go to Mode Select'):
                text_style 'mode_select'
                xsize 240
                ysize 120
                background 'menu_select_btn' padding(20,20)
                hover_background 'menu_select_btn_hover'
                action [ToggleVariable("greeted", False, False), renpy.full_restart]
                
            textbutton _('Start Over'):
                text_style 'mode_select'
                xsize 240
                ysize 120
                background 'menu_select_btn' padding(20,20)
                hover_background 'menu_select_btn_hover'
                action Show("confirm", message="Are you sure you want to start over? You'll be unable to return to this point except through a save file.", yes_action=[Hide('confirm'), Jump("restart_game")], no_action=Hide('confirm'))
            
            
# *********************************
# Restart Game -- resets variables
# *********************************       
label restart_game:
    python:
        # removes heart points from all the characters
        for person in character_list:
            person.reset_heart()
        
        # presumably some more resets here
        persistent.on_route = False
        renpy.full_restart()
        

########################################################
## The 'homepage' from which you interact with the game
## after the main menu
########################################################
    
default chips_available = False
default spaceship_xalign = 0.04
default reset_spaceship_pos = False

screen chat_home(reshow=False):

    tag menu     
    
    $ renpy.music.play(mystic_chat, loop=True)
    $ mc_pic = 'Profile Pics/MC/MC-' + str(persistent.MC_pic) + '.png'   
   
    use starry_night
    
    use menu_header("Original Story")

    on 'show':
        action [FileSave(mm_auto, confirm=False), deliver_next] 
        #[QuickSave(False), deliver_next]
 
    on 'replace':
        action [FileSave(mm_auto, confirm=False), deliver_next] 
        #action [QuickSave(False), deliver_next]

    if num_undelivered():
        timer 3.5 action If(randint(0,1), deliver_next, NullAction) repeat True
  
    
    # Text Messages
    button:
        maximum(168,168)
        xalign 0.62
        yalign 0.195
        if new_message_count() > 0:
            background 'blue_mainbtn'
            hover_background 'blue_mainbtn_hover'
        else:
            background "gray_mainbtn"
            hover_background "gray_mainbtn_hover"
        action Show('text_message_hub', Dissolve(0.5))
        if new_message_count() > 0:
            add 'blue_maincircle' xalign 0.5 yalign 0.5
            window:
                maximum(45,45)
                xalign 1.0
                yalign 0.0
                background 'new_text_count' 
                text str(new_message_count()) style 'text_num'
        else:
            add "gray_maincircle" xalign 0.5 yalign 0.5
        add "msg_mainicon" xalign 0.5 yalign 0.5
        add "msg_maintext" xalign 0.5 yalign 0.85
        
    # Calls
    button:
        maximum(168,168) 
        xalign 0.91
        yalign 0.35
        if unseen_calls > 0:
            background "blue_mainbtn"
            hover_background "blue_mainbtn_hover"
        else:
            background "gray_mainbtn"
            hover_background "gray_mainbtn_hover"
        action Show('phone_calls')        
        if unseen_calls > 0:
            add "blue_maincircle" xalign 0.5 yalign 0.5  
            window:
                maximum(45,45)
                xalign 1.0
                yalign 0.0
                background 'new_text_count' 
                text "[unseen_calls]" style 'text_num'
        else:
            add "gray_maincircle" xalign 0.5 yalign 0.5
        
        add "call_mainicon" xalign 0.5 yalign 0.5
        add "call_maintext" xalign 0.5 yalign 0.85
     
    # Emails
    button:
        maximum(168,168)
        xalign 0.342
        yalign 0.33
        if unread_emails() > 0:
            background "blue_mainbtn"
            hover_background "blue_mainbtn_hover"
        else:
            background "gray_mainbtn"
            hover_background "gray_mainbtn_hover"
        action Show('email_hub', Dissolve(0.5))
        if unread_emails() > 0:
            add "blue_maincircle" xalign 0.5 yalign 0.5
            window:
                maximum(45, 45)
                xalign 1.0
                yalign 0.0
                background 'new_text_count'
                text str(unread_emails()) style 'text_num'
        else:
            add "gray_maincircle" xalign 0.5 yalign 0.5
        add "email_mainicon" xalign 0.5 yalign 0.5
        add "email_maintext" xalign 0.5 yalign 0.85
        
    # Main Chatroom
    button:
        maximum(305,305)
        xalign 0.65
        yalign 0.722
        background "gray_chatbtn"
        hover_background "gray_chatbtn_hover"
        action [deliver_all, Show('chat_select')]
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
                for person in character_list[:6]:
                    imagebutton:
                        hover "profile_pic_select_square"
                        idle im.FactorScale(person.prof_pic, 0.9)
                        background im.FactorScale(person.prof_pic, 0.9)
                        action Show('chara_profile', who=person)
                        
                imagebutton:
                    hover "profile_pic_select_square"
                    idle im.FactorScale(mc_pic, 0.9)
                    background im.FactorScale(mc_pic, 0.9)
                    action Show('profile_pic')
            hbox:
                spacing 8
                for person in character_list[7:]:
                    imagebutton:
                            hover "profile_pic_select_square"
                            idle im.FactorScale(person.prof_pic, 0.9)
                            background im.FactorScale(person.prof_pic, 0.9)
                            action Show('chara_profile', who=person)

    window:
        maximum(140, 1000)
        xalign 0.03
        yalign 0.62
        has vbox
        spacing 20
        # Album
        button:
            maximum(130,149)
            background "white_hex"
            hover_background "white_hex_hover"
            action Jump('tutorial_chat_incoming_z')
            add "album_icon" xalign 0.5 yalign 0.35
            add "album_text" xalign 0.5 yalign 0.8
            
        # Guest
        button:
            maximum(130,149)
            background "white_hex"
            hover_background "white_hex_hover"
            action Jump('email_test')
            add "guest_icon" xalign 0.5 yalign 0.3
            add "guest_text" xalign 0.5 yalign 0.8
            
        # Shop
        button:
            maximum(130,149)
            background "red_hex"
            hover_background "red_hex_hover"
            action Jump('chapter_select1')
            add "shop_icon" xalign 0.55 yalign 0.35
            add "shop_text" xalign 0.5 yalign 0.8
            
        # Notice
        button:
            maximum(130,149)
            background "white_hex"
            hover_background "white_hex_hover"
            action Function(deliver_emails())
            add "notice_icon" xalign 0.5 yalign 0.3
            add "notice_text" xalign 0.5 yalign 0.8
            
        # Link            
        button:
            maximum(130,149)
            background "white_hex"
            hover_background "white_hex_hover"
            action NullAction
            
            add "link_icon" xalign 0.5 yalign 0.3
            add "link_text" xalign 0.5 yalign 0.8
            
            
    ## Spaceship    
    add "dot_line" xalign 0.5 yalign .97
        
    #text str(reset_spaceship_pos) + ' - ' + str(spaceship_xalign) color '#fff'
    $ spaceship_xalign = spaceship_get_xalign(True)
        
    if chips_available:       
    
        if not reshow:
            window at chip_anim:
                maximum(90,70)
                xalign 0.93
                yalign 0.942
                add "space_chip_explode"
                
            add "space_chip_active" xalign 0.92 yalign 0.98
            
            window at spaceship_chips(1.0):
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
        
        if reshow:
            window at chip_anim(0):
                maximum(90,70)
                xalign 0.93
                yalign 0.942
                add "space_chip_explode"
                
            add "space_chip_active2" xalign 0.92 yalign 0.98
            
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
     
     
########################################################
## The Profile Screen for each of the characters
########################################################
        
screen chara_profile(who):

    tag menu

    use starry_night
    use menu_header("Profile", Show('chat_home', Dissolve(0.5)))   
    
    add who.cover_pic yalign 0.231
    
    fixed:
        xfit True yfit True
        xalign 0.1 yalign 0.675
        add Transform(who.prof_pic, zoom=2.85)
        add 'profile_outline'    
    window:
        maximum (350,75)
        xalign 0.96
        yalign 0.685
        text who.name style "profile_header_text"
    window:  
        maximum (700, 260)
        yalign 0.97
        text who.status style "profile_status"
    

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
    show screen chat_home(True)
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
        
   
        
        
        
        
        
        
