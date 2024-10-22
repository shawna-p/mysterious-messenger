################################################################################
## Initialization
################################################################################

init offset = -1

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language
    size 33
    font gui.sans_serif_1

style input:
    adjust_spacing False
    color "#ffffff"

style hyperlink_text:
    color "#00b08d"
    hover_underline True

style gui_text:
    size 30 color "#FFF"
    font gui.sans_serif_1


style button:
    xysize (None, None)
    padding (4, 4, 4, 4)
    background None
    hover_background None
    selected_idle_background None
    selected_hover_background None
    insensitive_background None

style button_text:
    is gui_text
    yalign 0.5 xalign 0.0
    text_align 0.0
    idle_color "#ababab"
    hover_color "#3e8478"
    selected_color "#FFF"
    insensitive_color "#8888887f"
    size gui.interface_text_size
    font gui.sans_serif_1


style label_text:
    is gui_text
    properties gui.text_properties("label", accent=True)
    size 30
    color "#FFF"

style prompt_text is gui_text

style bar:
    ysize 22
    left_bar Frame("gui/bar/left.png", 4, 4, tile=False)
    right_bar Frame("gui/bar/right.png", 4, 4, tile=False)

style vbar:
    xsize 22
    top_bar Frame("gui/bar/top.png", 4, 4, tile=False)
    bottom_bar Frame("gui/bar/bottom.png", 4, 4, tile=False)

style scrollbar:
    ysize 11
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", 4, 4, tile=False)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", 4, 4, tile=False)
    unscrollable "hide"

style vscrollbar:
    unscrollable "hide"
    xsize 11
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", 4, 4, tile=False)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", 4, 4, tile=False)

style slider:
    ysize 22
    thumb "gui/slider/horizontal_[prefix_]thumb.png"
    left_gutter 10
    right_gutter 10
    left_bar Frame("gui/slider/left_horizontal_bar.png", 4, 4, tile=False)
    right_bar Frame("gui/slider/right_horizontal_bar.png", 4, 4, tile=False)

style vslider:
    xsize 22
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", 4, 4, tile=False)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    # In Story Mode
    if gamestate == VNMODE:
        style_prefix "vn_mode"
        if _in_replay and not viewing_guest:
            textbutton _("End Replay"):
                style 'vn_mode_button'
                text_style 'vn_mode_button_text'
                action EndReplay()

        # Darkens the VN window for more contrast
        window:
            add Transform('vn_window_darken', alpha=persistent.vn_window_dark)

        window:
            id "window"
            if who is not None:
                window:
                    style_prefix None
                    style "namebox"
                    text who id "who":
                        if (persistent.vn_window_alpha < 0.2
                                or persistent.dialogue_outlines):
                            outlines [ (2, "#000") ]
                            font gui.sans_serif_1xb

            text what id "what":
                style_prefix None
                if (persistent.vn_window_alpha < 0.2
                        or persistent.dialogue_outlines):
                    outlines [ (2, "#000") ]
        if not viewing_guest:
            # This is the overlay for Story Mode
            # that shows the Auto/Skip/Log buttons
            hbox:
                if persistent.vn_window_alpha < 0.1:
                    yoffset -275+20
                imagebutton:
                    idle Text("Auto", style="vn_button_hover")
                    hover Text("Auto", style="vn_button")
                    selected_idle Text("Auto", style="vn_button")
                    selected_hover Text("Auto", style="vn_button_hover")
                    action Preference("auto-forward", "toggle")

                imagebutton:
                    idle Text("Skip", style="vn_button")
                    hover Text("Skip", style="vn_button_hover")
                    selected renpy.is_skipping()
                    selected_idle Text("Stop", style="vn_button")
                    selected_hover Text("Stop", style="vn_button_hover")
                    action Skip()
                    activate_sound 'audio/sfx/UI/vn_skip.mp3'

                imagebutton:
                    idle Text("Log", style="vn_button")
                    hover Text("Log", style="vn_button_hover")
                    action Show('history')


    else:
        window id "window":
            style_prefix None
            at invisible
            if who is not None:
                window:
                    style "namebox"
                    text who id "who"
            text what id "what"


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window:
    is default
    xysize (config.screen_width, 324)
    align (0.5, 1.0)

style namebox:
    is default
    xpos 130
    xanchor 0.5
    xysize (None, None)
    ypos 6
    ## The borders of the box containing the character's name, in
    ## left, top, right, bottom order.
    padding (5, 5, 5, 5)

## The name
style say_label:
    is default
    color "#FFF"
    xalign 0.5
    yalign 0.5
    size 28
    font gui.sans_serif_1

style say_dialogue:
    is default
    xpos 20
    xsize 700
    ypos 75

style say_thought is say_dialogue
style namebox_label is say_label

style vn_mode_button:
    align (0.98, 0.01)

style vn_mode_window:
    xysize (config.screen_width, 324)
    align (0.5, 1.0)

style vn_mode_button_text:
    is vn_button
    size 32
    hover_color "#999999"

style vn_mode_hbox:
    xalign 1.0 xoffset -25
    yalign 1.0 yoffset -275
    spacing 20

style call_window:
    xfill True
    ysize 500
    yalign 0.5
    background 'call_overlay'
    padding (50, 50)

style vn_button:
    color '#76D0B7'
    font gui.sans_serif_2
    size 55
    outlines [(1, '#000')]
    kerning -1

style vn_button_hover:
    color "#999999"
    font gui.sans_serif_2
    size 55
    outlines [(1, '#000')]
    kerning -1

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign 0.0
            xpos 20
            xsize 700
            ypos 75

            text prompt style "input_prompt"
            input id "input"


style input_prompt:
    is default
    xalign 0.0

style input:
    xalign 0.0
    xmaximum 700


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    viewport:

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_text is gui_text

style about_label_text:
    is gui_label_text
    size 30


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
#style check_vbox is pref_vbox

style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style slot_vpgrid:
    xysize (745,1170)
    xalign 0.01
    spacing 5

style slot_hbox:
    spacing 8
    xsize 695

style slot_button:
    is gui_button
    padding (15, 10, 15, 10)
    xysize (715, 142)
    background Frame("gui/button/slot_[prefix_]background.png", 15, 10, 15, 10, tile=False)

style slot_button_text:
    is gui_button_text
    size 12
    xalign 0.0 text_align 0.0
    idle_color gui.idle_small_color


style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin 9
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 420

style radio_vbox:
    spacing 0

style radio_button:
    foreground "gui/button/check_[prefix_]foreground.png"

style check_vbox:
    spacing 0

style check_button:
    padding (50, 4, 4, 4)
    foreground "gui/button/check_[prefix_]foreground.png"

style slider_slider:
    xsize 296

style slider_button:
    is gui_button
    yalign 0.5
    left_margin 9

style slider_button_text:
    is gui_button_text
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 380


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    viewport:

        style_prefix "help"

        vbox:
            spacing 13

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 7

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 211
    right_padding 17

style help_label_text:
    size 33
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

image menu_popup_bkgrd = Frame("Menu Screens/Main Menu/menu_popup_bkgrd.webp",60,60,60,60)
image menu_popup_btn = Frame("Menu Screens/Main Menu/menu_popup_btn.webp",20,20,20,20)
image menu_popup_btn_hover = Transform('menu_popup_btn', alpha=0.5)

screen confirm(message, yes_action, no_action=False, show_link=False):

    on 'show' action SetVariable('pausing_timed_menu', True)
    on 'hide' action SetVariable('pausing_timed_menu', False)

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        vbox:
            label _(message):
                style "confirm_prompt"
                xalign 0.5
            if show_link:
                null height -53
                textbutton "check out my Ko-Fi here":
                    style 'button_text'
                    text_style 'button_text'
                    text_text_align 0.5 xalign 0.5
                    text_hover_underline True
                    text_color "#00b08d"
                    action OpenURL("https://ko-fi.com/fen")

            hbox:
                textbutton _("Confirm") action yes_action
                if no_action:
                    textbutton _("Cancel") action no_action


    ## Right-click and escape answer "no".
    if no_action:
        key "game_menu" action no_action

# Screen used specifically for the confirm prompt during a continuous menu
screen no_modal_confirm(message, yes_action, no_action=False):
    zorder 200
    style_prefix 'confirm'
    add 'gui/overlay/confirm.png'
    frame:
        vbox:
            label _(message) style 'confirm_prompt' xalign 0.5
            hbox:
                textbutton _("Confirm") action yes_action
                if no_action:
                    textbutton _("Cancel") action no_action
    ## Right-click and escape answer "no".
    if no_action:
        key "game_menu" action no_action

    # This constantly checks if there are any more choices on-screen; if not,
    # can replace this screen with the regular confirm screen.
    timer 0.1:
        action If(on_screen_choices == 0,
                [Hide('no_modal_confirm'), CConfirm(("Do you really want to "
                        + "exit this chatroom? Please note that you cannot "
                        + "participate once you leave. If you want to enter "
                        + "this chatroom again, you will need to buy it back."),
                                    [Jump('exit_item_early')])], NullAction())
        repeat True

## Screen which displays script error messages to the user
screen script_error(message, link=False, link_text=False):
    modal True
    zorder 190
    python:
        message = "{=sser1xb}{color=#f00}Script Error:\n{/color}{/=sser1xb}" + message
        if link:
            message += "\n\nLink to documentation:"
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    frame:
        vbox:
            label _(message):
                style "confirm_prompt"
                xalign 0.5
            if link:
                null height -53
                textbutton link_text:
                    style 'button_text'
                    text_layout "subtitle"
                    text_style 'button_text'
                    text_text_align 0.5 xalign 0.5
                    text_hover_underline True
                    text_color "#00b08d"
                    action OpenMysMeDocumentation(link=link)

            hbox:
                textbutton _("Confirm") action Hide('script_error')

image error_present = "Menu Screens/Main Menu/menu_gift.webp"
screen messenger_error():
    modal True
    zorder 190
    add "gui/overlay/confirm.png"
    vbox:
        order_reverse True
        spacing -70
        align (0.55, 0.5)
        add 'error_present' align (0.0, 0.0) xoffset -70
        frame:
            style_prefix "confirm"
            xsize 600
            vbox:
                label _("Messenger Error! An hourglass is force added..."):
                    style "confirm_prompt"
                    text_size 35
                    xalign 0.5
                frame:
                    style_prefix "sig_points"
                    xalign 0.5
                    background 'hg_sign'
                    text "1"
                hbox:
                    textbutton _("Confirm"):
                        action [SetField(persistent, 'HG', persistent.HG+1),
                                Hide('messenger_error')]
                        keysym "rollback"

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    padding (34, 34)
    xalign .5
    yalign .5
    background "menu_popup_bkgrd"
    xmaximum 700

style confirm_vbox:
    xalign .5
    yalign .5
    spacing 26
    xmaximum 650

style confirm_hbox:
    xalign 0.5
    spacing 100

style confirm_prompt_text:
    font gui.sans_serif_1
    text_align 0.5
    layout "subtitle"

style confirm_button:
    #properties gui.button_properties("confirm_button")
    xsize 200
    background "menu_popup_btn"
    padding(20,20)
    hover_foreground "menu_popup_btn_hover"

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
    color "#eeeeee"
    hover_color "#ffffff"
    xalign 0.5
    text_align 0.5
    font gui.sans_serif_1
    size 30


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos 9
    background Frame("gui/skip.png", 14, 5, 43, 5, False)
    padding (14, 5, 43, 5)

style skip_text:
    size 25

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"
    if message != False:
        frame at notify_appear:
            text "[message!tq]"

        timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos 38

    background Frame("gui/notify.png", 14, 5, 34, 5, tile=False)
    padding (14, 5, 34, 5)

style notify_text:
    size 25


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        viewport:
            align (0.5, 0.2)
            yinitial 1.0
            mousewheel True
            has vbox
            spacing 40

            use nvl_dialogue(dialogue)

            ## Displays the menu, if given. The menu may be displayed
            ## incorrectly if config.narrator_menu is set to True,
            ## as it is above.
            if items:
                for i in items:
                    textbutton i.caption:
                        action i.action
                        style "nvl_button"


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit True

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id

## The maximum number of NVL-mode entries Ren'Py will display. When more entries
## than this are to be show, the oldest entry will be removed.
define config.nvl_list_length = 20


## NVL-Mode ####################################################################
##
## The NVL-mode screen displays the dialogue spoken by NVL-mode characters.

style nvl_window:
    is default
    xfill True
    yfill True

    background "#000c"
    ## The borders of the background of the NVL-mode background window.
    padding (0, 20, 0, 20)

style nvl_entry:
    is default
    xfill True
    ysize None

## The position, width, and alignment of the label giving the name of the
## speaking character.
style nvl_label:
    is say_label
    xpos 70
    xanchor 0.5
    ypos 0
    yanchor 0.0
    xsize 127
    min_width 127
    text_align 0.5


## The position, width, and alignment of the dialogue text.
style nvl_dialogue:
    is say_dialogue
    xpos 130
    xanchor 0.0
    ypos 7
    xsize 500
    min_width 500
    text_align 0.0
    layout "tex"

## The position, width, and alignment of nvl_thought text (the text said by the
## nvl_narrator character.)

style nvl_thought:
    xpos 550
    xanchor 0.5
    ypos 7
    xsize 750
    min_width 750
    text_align 0.5
    layout "subtitle"


## The position of nvl menu_buttons.
style nvl_button:
    is button
    xpos 380 ypos 200
    xalign 0.0

style nvl_button_text:
    is button_text
    properties gui.button_text_properties("nvl_button")

