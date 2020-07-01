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

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    #properties gui.text_properties("hyperlink", accent=True)
    color "#00b08d"#"#2451c1"
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    #base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"
    left_gutter 10
    right_gutter 10
    left_bar Frame("gui/slider/left_horizontal_bar.png", gui.slider_borders, tile=gui.slider_tile)
    right_bar Frame("gui/slider/right_horizontal_bar.png", gui.slider_borders, tile=gui.slider_tile)

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



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

transform NullTransform:
    pass
    
screen say(who, what):
    
    # In VN mode
    if not in_phone_call and not text_person and vn_choice:
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
                            outlines [ (absolute(2), "#000", 
                                        absolute(0), absolute(0)) ]
                            font gui.sans_serif_1xb

            text what id "what":
                style_prefix None
                if (persistent.vn_window_alpha < 0.2 
                        or persistent.dialogue_outlines):
                    outlines [ (absolute(2), "#000", 
                                absolute(0), absolute(0)) ]
        if not viewing_guest:
            # This is the overlay for VN mode 
            # that shows the Auto/Skip/Log buttons
            hbox:
                if persistent.vn_window_alpha < 0.1:
                    yoffset 20
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
                    action Show('history')#ShowMenu('history')
    
    
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

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xysize (750,324)
    align (0.5, 1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

style vn_mode_button:
    align (0.98, 0.01)

style vn_mode_window:
    xysize (750,324)
    align (0.5, 1.0)

style vn_mode_button_text:
    is vn_button
    size 32
    hover_color "#999999"

style vn_mode_hbox:
    yalign 0.785
    xalign 0.90
    spacing 20

style call_window:
    xfill True
    ysize 500
    yalign 0.5
    background 'call_overlay' 
    padding(50,50)

style vn_button:
    color '#76D0B7'
    font gui.sans_serif_2
    size 55
    outlines [(absolute(1), '#000', absolute(0), absolute(0))]
    kerning -1
    
style vn_button_hover:
    color "#999999"
    font gui.sans_serif_2
    size 55
    outlines [(absolute(1), '#000', absolute(0), absolute(0))]
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
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    zorder 150
    modal True
    
    python:
        if persistent.custom_footers and not renpy.is_skipping():
            the_anim = choice_anim
        else:
            the_anim = null_anim   
 
    add "choice_darken"

    # For text messages
    if text_msg_reply:
        if not text_person or not text_person.real_time_text:
            use text_message_screen(text_person)
        vbox:
            style_prefix 'text_msg_choice'
            for num, i in enumerate(items):
                $ fnum = float(num*0.2)
                textbutton i.caption at the_anim(fnum):
                    if persistent.dialogue_outlines:
                        text_outlines [ (absolute(2), "#000", 
                                absolute(0), absolute(0)) ]
                    if (persistent.past_choices
                            and i.chosen):
                        foreground 'seen_choice_check'
                    action If((not text_person 
                                or not text_person.real_time_text),
                            [Show('text_message_screen',
                                        sender=text_person),
                                i.action], [i.action])
    
    # For VN mode and phone calls
    elif in_phone_call or vn_choice:
        $ can_see_answer = 0
        
        vbox:
            style_prefix 'phone_vn_choice'
            for num, i in enumerate(items):
                $ fnum = float(num*0.2)
                if observing:
                    $ fnum = 0
                if not observing or i.chosen:
                    $ can_see_answer += 1
                    textbutton i.caption at the_anim(fnum):
                        if persistent.dialogue_outlines:
                            text_outlines [ (absolute(2), "#000", 
                                absolute(0), absolute(0)) ]
                        if (persistent.past_choices
                                and i.chosen):
                            foreground 'seen_choice_check_circle'
                            background 'call_choice_check'
                            hover_background 'call_choice_check_hover'
                        action [i.action]
            # Not a perfect solution, but hopefully provides an 'out'
            # to players who somehow didn't choose a menu option and
            # are now in observing mode
            if can_see_answer == 0:
                textbutton _("(Continue)"):  
                    if persistent.dialogue_outlines:
                        text_outlines [ (absolute(2), "#000", 
                                absolute(0), absolute(0)) ]
                    action [SetVariable('timed_choose', False), Return()]
            
    # For emails
    elif email_reply:
        use email_hub
        use open_email(current_email)
        vbox:
            style_prefix 'email_choice'
            for num, i in enumerate(items):
                $ fnum = float(num*0.2)
                textbutton i.caption at the_anim(fnum):
                    action [i.action]
    
    # For everything else (e.g. chatrooms)
    else:
        $ can_see_answer = 0
        vbox:
            if persistent.custom_footers:
                style_prefix 'phone_vn_choice'
            else:
                style_prefix 'choice'
            for num, i in enumerate(items):
                if not observing or i.chosen:
                    $ can_see_answer += 1
                    $ fnum = float(num*0.2)
                    textbutton i.caption at the_anim(fnum):
                        if (persistent.dialogue_outlines 
                                and persistent.custom_footers):
                            text_outlines [ (2, "#000", 
                                absolute(0), absolute(0)) ]
                        elif (persistent.dialogue_outlines
                                and not persistent.custom_footers):
                            text_outlines [ (2, "#fff", 
                                absolute(0), absolute(0)) ]
                        
                        if (persistent.past_choices
                                and i.chosen):
                            if persistent.custom_footers:
                                foreground 'seen_choice_check_circle'
                                background 'call_choice_check'
                                hover_background 'call_choice_check_hover'
                            else:
                                foreground 'seen_choice_check'

                        action If(using_timed_menus, 
                            [SetVariable('reply_instant', True), 
                                SetVariable('using_timed_menus', False),
                                Hide('answer_countdown'),
                                # This ensures the messenger scrolls
                                # to the bottom
                                Hide('messenger_screen'),
                                Show('messenger_screen'),

                                i.action],
                            [i.action])
                
            # Not a perfect solution, but hopefully provides an 'out'
            # to players who somehow didn't choose a menu option and
            # are now in observing mode
            if can_see_answer == 0:
                textbutton _("(Continue)"):
                    if persistent.dialogue_outlines:
                        text_outlines [ (absolute(2), "#000", 
                                absolute(0), absolute(0)) ]
                    action [SetVariable('timed_choose', False), Return()]
                            

image seen_choice_check = Image('Menu Screens/Main Menu/main02_tick.png', 
                            align=(0.99, 0.97))
image seen_choice_check_circle = Image('Menu Screens/Main Menu/main02_tick_2.png', 
                            align=(0.985, 0.955))

## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True

style choice_vbox:
    xalign 0.5
    ypos 600
    yanchor 0.40
    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    activate_sound "audio/sfx/UI/answer_select.mp3"

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")

style text_msg_choice_vbox:
    is choice_vbox

style text_msg_choice_button:
    is choice_button
    background 'text_answer_idle'
    hover_background 'text_answer_hover'

style text_msg_choice_button_text:
    is choice_button_text
    idle_color '#fff'
    hover_color '#fff'

style phone_vn_choice_vbox:
    is choice_vbox
    spacing 20 

style phone_vn_choice_button:
    is choice_button
    xysize (740, 180)
    background 'call_choice' 
    hover_background 'call_choice_hover'
    padding(45,45)
    align (0.5, 0.5)

style phone_vn_choice_button_text:
    is choice_button_text
    align (0.5, 0.5)
    idle_color '#f9f9f9'
    hover_color '#fff'
    text_align 0.5

style email_choice_vbox:
    is choice_vbox

style email_choice_button:
    is choice_button
    background 'text_answer_idle'
    hover_background 'text_answer_hover'

style email_choice_button_text:
    is choice_button_text
    idle_color '#fff'
    hover_color '#fff'
    xalign 0.5
    yalign 0.5
    text_align 0.5



default quick_menu = False


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
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


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

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style slot_vpgrid:
    xysize (745,1170)
    xalign 0.01
    spacing gui.slot_spacing

style slot_hbox:
    spacing 8
    xsize 695

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 420#190

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 296

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 9

style slider_button_text:
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
    size gui.text_size
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

image menu_popup_bkgrd = Frame("Menu Screens/Main Menu/menu_popup_bkgrd.png",60,60,60,60)
image menu_popup_btn = Frame("Menu Screens/Main Menu/menu_popup_btn.png",20,20,20,20)
image menu_popup_btn_hover = Transform('menu_popup_btn', alpha=0.5)

screen confirm(message, yes_action, no_action=False, show_link=False):

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
                    action OpenURL("https://ko-fi.com/somniarre")

            hbox:                
                textbutton _("Confirm") action yes_action
                if no_action:
                    textbutton _("Cancel") action no_action
                

    ## Right-click and escape answer "no".
    if no_action:
        key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    padding gui.confirm_frame_borders.padding
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
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

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
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):
   
   
    window:
        style "nvl_window"
        frame:
            background "transparent.png"     # or use any semi-transparent image you like
            align (0.5, 0.2)
            
            
            viewport:
                #draggable True
                mousewheel True
                has vbox:
                    spacing 40 #gui.nvl_spacing
                
                use nvl_dialogue(dialogue)

                ## Displays the menu, if given. The menu may be displayed
                ## incorrectly if config.narrator_menu is set to True,
                ## as it is above.
                for i in items:
                    textbutton i.caption:
                        action i.action
                        style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    python:
        yadj.value = yadjValue


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

transform slow_fade(delay=0.5):
    alpha 0.0
    linear delay alpha 1.0

## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "#000c"#"gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")

    