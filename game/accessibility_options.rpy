## Accessibility functions #####################################################
##
## These are some additional functions and definitions intended to allow
## the player to configure the game to better suit themselves
##

# Allows the player to turn screenshake on/off
default persistent.screenshake = True
# Allows the player to turn banner animations on/off
default persistent.banners = True
# Allows players to turn the hacking effects on/off
default persistent.hacking_effects = True
# Shows a notification informing the player of audio cues
default persistent.audio_captions = False
# Allows the player to toggle timed menus on or off
default persistent.autoanswer_timed_menus = False
# Displays notifications instead of heart icons
default persistent.heart_notifications = False
# New version of the above option
default persistent.animated_icons = True
# Adds outline to VN dialogue
default persistent.dialogue_outlines = False
# Controls the contrast of the starry night background
default persistent.starry_contrast = 0.0
# Toggles animated backgrounds on and off
default persistent.animated_backgrounds = False
# Indicates past choices
default persistent.past_choices = False

## This label plays sound effects and also shows an audio
## caption if the player has that option turned on
label play_sfx(sfx):
    play sound sfx
    if persistent.audio_captions:
        $ notification = ("SFX: " + 
                sfx_dictionary[renpy.sound.get_playing('sound')])
        show screen notify(notification)
    return

## These variables are used to make the VN window more or less transparent
default persistent.vn_window_dark = 0.0
default persistent.vn_window_alpha = 1.0
default persistent.window_darken_pct = 50
image vn_window_darken = "VN Mode/Chat Bubbles/vnmode_darken.png"

init python:
    
    def adjust_vn_alpha():
        """Adjust the alpha channels of window backgrounds used in VN mode."""

        global persistent
        # When window_darken_pct <= 50, only lighten the main window
        if persistent.window_darken_pct <= 50:
            persistent.vn_window_dark = 0.0
            persistent.vn_window_alpha = float(persistent.window_darken_pct 
                                                        / 50.0)
        else:
            persistent.vn_window_alpha = 1.0
            persistent.vn_window_dark = float((persistent.window_darken_pct
                                                         - 50) / 50.0)

   



## An in-progress screen that allows the player to change
## some of the fonts in-game
screen adjust_fonts():

    modal True
    add "#000a"

    frame:
        xysize (675, 1000)
        background 'menu_settings_panel_bright'
        align (0.5, 0.5)

        imagebutton:
            align (1.0, 0.0)
            xoffset 3 yoffset -3
            idle 'input_close'
            hover 'input_close_hover'
            action Hide('adjust_fonts')
        
        text "Adjust Fonts" style "settings_style" xpos 55 ypos 5

        viewport:
            xysize(600, 940)
            xalign 0.5
            yalign 0.85
            draggable True
            mousewheel True
            scrollbars "vertical"
            side_spacing 5
            has vbox
            xsize 550
            spacing 15
            xalign 0.5
            yalign 0.5

            textbutton _("Override all fonts to OpenDyslexic"):
                style 'check_button'
                text_style 'check_button_text'
                action [ 
                    gui.SetPreference('curly_font', 
                        'fonts/OpenDyslexic2/OpenDyslexic-Italic.otf', False),
                    gui.SetPreference('serif_1', 
                        'fonts/OpenDyslexic2/OpenDyslexic-Regular.otf', False),
                    gui.SetPreference('serif_1b', 
                        'fonts/OpenDyslexic2/OpenDyslexic-Bold.otf', False),
                    gui.SetPreference('serif_1xb', 
                        'fonts/OpenDyslexic2/OpenDyslexic-BoldItalic.otf',
                        False),
                    gui.SetPreference('serif_2', 
                        'fonts/OpenDyslexic2/OpenDyslexic-Regular.otf', False),
                    gui.SetPreference('serif_2b', 
                        'fonts/OpenDyslexic2/OpenDyslexic-Bold.otf', False),
                    gui.SetPreference('serif_2xb', 
                        'fonts/OpenDyslexic2/OpenDyslexic-BoldItalic.otf',
                        False),
                    gui.SetPreference('sans_serif_1', 
                        'fonts/OpenDyslexic2/OpenDyslexic-Regular.otf', False),
                    gui.SetPreference('sans_serif_1b', 
                        'fonts/OpenDyslexic2/OpenDyslexic-Bold.otf', False),
                    gui.SetPreference('sans_serif_1xb', 
                        'fonts/OpenDyslexic2/OpenDyslexic-BoldItalic.otf',
                        False),
                    gui.SetPreference('sans_serif_2', 
                        'fonts/OpenDyslexic2/OpenDyslexic-Regular.otf', False),
                    gui.SetPreference('sans_serif_2b', 
                        'fonts/OpenDyslexic2/OpenDyslexic-Bold.otf', False),
                    gui.SetPreference('sans_serif_2xb', 
                        'fonts/OpenDyslexic2/OpenDyslexic-BoldItalic.otf',
                        False),

                    gui.SetPreference('blocky_font', 
                        'fonts/OpenDyslexic2/OpenDyslexic-Bold.otf', False),
                    gui.SetPreference('curlicue_font', 
                        'fonts/OpenDyslexic2/OpenDyslexic-Italic.otf', True)  
                ]
            
            # gui.curly_font 
            # gui.serif_1 
            # gui.serif_1b 
            # gui.serif_1xb
            # gui.serif_2 
            # gui.serif_2b 
            # gui.serif_2xb 
            # gui.sans_serif_1
            # gui.sans_serif_1b 
            # gui.sans_serif_1xb
            # gui.sans_serif_2
            # gui.sans_serif_2b 
            # gui.sans_serif_2xb
            # gui.blocky_font
            # gui.curlicue_font 
            frame:
                background 'menu_popup_bkgrd'
                textbutton _("Restore defaults"):
                    action [ 
                        gui.SetPreference('curly_font', 
                            "fonts/Sandoll Misaeng (Curly Font).ttf", False),
                        gui.SetPreference('serif_1', 
                            "fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf", False),
                        gui.SetPreference('serif_1b', 
                            "fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Bold.ttf", False),
                        gui.SetPreference('serif_1xb', 
                            "fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-ExtraBold.ttf",
                            False),
                        gui.SetPreference('serif_2', 
                            "fonts/Seoul Hangang (Serif font 2)/SeoulHangangM.ttf", False),
                        gui.SetPreference('serif_2b', 
                            "fonts/Seoul Hangang (Serif font 2)/SeoulHangangB.ttf", False),
                        gui.SetPreference('serif_2xb', 
                            "fonts/Seoul Hangang (Serif font 2)/SeoulHangangEB.ttf",
                            False),
                        gui.SetPreference('sans_serif_1', 
                            "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf", False),
                        gui.SetPreference('sans_serif_1b', 
                            "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Bold.ttf", False),
                        gui.SetPreference('sans_serif_1xb', 
                            "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-ExtraBold.ttf",
                            False),
                        gui.SetPreference('sans_serif_2', 
                            "fonts/SeoulNamsan (Sans Serif Font 2)/SeoulNamsanM.ttf", False),
                        gui.SetPreference('sans_serif_2b', 
                            "fonts/SeoulNamsan (Sans Serif Font 2)/SeoulNamsanB.ttf", False),
                        gui.SetPreference('sans_serif_2xb', 
                            "fonts/SeoulNamsan (Sans Serif Font 2)/SeoulNamsanEB.ttf",
                            False),

                        gui.SetPreference('blocky_font', 
                            "fonts/BM-HANNA (Bold Font).ttf", False),
                        gui.SetPreference('curlicue_font', 
                            "fonts/NanumBarunpenR.ttf", True)  
                    ]


