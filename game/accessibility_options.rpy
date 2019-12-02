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
image vn_window_darken = "VN Mode/Chat Bubbles/window_darken.png"

init python:
    ## This adjusts the alpha channels of the window
    ## backgrounds used in VN mode
    def adjust_vn_alpha():
        global persistent
        # When window_darken_pct <= 50, we only lighten the main window
        if persistent.window_darken_pct <= 50:
            persistent.vn_window_dark = 0.0
            persistent.vn_window_alpha = float(persistent.window_darken_pct 
                                                        / 50.0)
        else:
            persistent.vn_window_alpha = 1.0
            persistent.vn_window_dark = float((persistent.window_darken_pct
                                                         - 50) / 50.0)

    ## This allocates a notification screen that can
    ## be used to display popup messages
    def allocate_notification_screen(can_pause=False):
        possible_screens = ["stackable_notifications", 
                            "stackable_notifications_2",
                            "stackable_notifications_3",
                            "stackable_notifications_4",
                            "stackable_notifications_5"]
        available_screens = [ x for x in possible_screens 
                                if not renpy.get_screen(x) ]
        if can_pause and len(available_screens) < 5:
            renpy.pause(0.1)
        if available_screens:
            return available_screens[0]
        else:
            renpy.hide_screen(possible_screens[0])
            return possible_screens[0]
    
    ## This function is just a slightly quicker way to hide all the
    ## allocated notification screens
    def hide_stackable_notifications():
        renpy.hide_screen('stackable_notifications')
        renpy.hide_screen('stackable_notifications_2')
        renpy.hide_screen('stackable_notifications_3')
        renpy.hide_screen('stackable_notifications_4')
        renpy.hide_screen('stackable_notifications_5')
        return

## This screen is used to display text notifications
## about whom the player received a heart point with
screen stackable_notifications(message, hide_screen='stackable_notifications'):
    zorder 100
    button at stack_notify_appear:
        style 'notify_frame'
        xalign 1.0 yalign 0.92
        text "[message!tq]" style 'notify_text'
        action Hide(hide_screen)
    timer 5.25 action Hide(hide_screen)

screen stackable_notifications_2(message):
    zorder 101
    use stackable_notifications(message, 'stackable_notifications_2')

screen stackable_notifications_3(message):
    zorder 102
    use stackable_notifications(message, 'stackable_notifications_3')

screen stackable_notifications_4(message):
    zorder 103
    use stackable_notifications(message, 'stackable_notifications_4')

screen stackable_notifications_5(message):
    zorder 104
    use stackable_notifications(message, 'stackable_notifications_5')

transform stack_notify_appear:
    yoffset 0
    on show:
        alpha 0 yoffset 30
        linear .25 alpha 1.0 yoffset 0
        linear 5 yoffset -250
    on hide:
        linear .5 alpha 0.0 yoffset -310

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


