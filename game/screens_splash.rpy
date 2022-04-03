image touch_to_start = Fixed(
    "#0005",
    At(Text("Touch to Start", color="#fff", align=(0.5, 0.5)), fade_in_out),
    xysize=(config.screen_width, 50)
)
transform fade_in_out():
    alpha 1.0
    easein 1.2 alpha 0.0
    easeout 1.2 alpha 1.0
    repeat


screen splash_image():
    add persistent.main_menu_image:
        align (0.5, 0.5) xysize (config.screen_width, config.screen_height)
        fit "cover"
    add 'touch_to_start' yalign 1.0 yoffset -90
    button:
        xysize (config.screen_width, config.screen_height)
        activate_sound "audio/sfx/UI/digi_chime_echo.wav"
        action Return()

# Set this to the image you want to use on the splash screen.
# Note that it's persistent, so you'll need to delete your persistent
# variables or set it somewhere in script to see changes.
default persistent.main_menu_image = None

label splashscreen():
    # If there's an image to show, display the splash
    # screen and wait for a click, then go to the main menu.
    if persistent.main_menu_image:
        play music mystic_op_instrumental
        call screen splash_image()
    show screen loading_screen
    pause 1.0
    hide screen loading_screen
    return