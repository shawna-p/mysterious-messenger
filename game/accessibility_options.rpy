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


## This label plays sound effects and also shows an audio
## caption if the player has that option turned on
label play_sfx(sfx):
    play sound sfx
    if persistent.audio_captions:
        $ notification = ("SFX: " + 
                sfx_dictionary[renpy.sound.get_playing('sound')])
        show screen notify(notification)
    return

default persistent.vn_window_dark = 0.0
default persistent.vn_window_alpha = 1.0
default persistent.window_darken_pct = 50
image vn_window_darken = "VN Mode/Chat Bubbles/window_darken.png"

init python:
    ## This function adjusts the alpha channels of the window
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
