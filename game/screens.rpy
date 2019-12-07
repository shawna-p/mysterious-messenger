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
    color "#2451c1"
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
    
transform bubble:
    #on show:
    rotate 270    
        # Shake(None, 1.0, dist=5)
        # maxsize (30, 30)

screen say(who, what):
    #style_prefix "say"
    
    # In VN mode
    if not in_phone_call and not text_person and vn_choice:
    
        if _in_replay:
            textbutton _("End Replay"):
                text_style 'vn_button'
                text_size 32
                text_hover_color "#999999"
                action EndReplay()
                align (0.98, 0.01)

        window:
            # background Fixed(Transform('vn_window_darken', 
            #                     alpha=persistent.vn_window_dark),
            #                 Transform(style.window.background, 
            #                     alpha=persistent.vn_window_alpha))
            id "window"
            xysize (750,324)
            align (0.5, 1.0)
            if who is not None:
                window:
                    style "namebox"
                    text who id "who"

            text what id "what"
        if not viewing_guest:
            # This is the overlay for VN mode 
            # that shows the Auto/Skip/Log buttons
            hbox:
                yalign 0.785
                xalign 0.90
                spacing 20
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
                    action ShowMenu('history')
            
    elif not text_person and in_phone_call:   # In a phone call        
        window:
            xfill True
            ysize 500
            yalign 0.5
            background 'call_overlay' padding(50,50)
            text what id "what" #style 'call_text'


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
    xalign 0.5
    yalign gui.textbox_yalign
    ysize gui.textbox_height

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
    
    

 
    # For text messages
    if text_msg_reply:
        if not text_person or not text_person.real_time_text:
            use text_message_screen(current_message)
        add "Phone UI/choice_dark.png"
        vbox:
            style 'choice_vbox'
            for num, i in enumerate(items):
                $ fnum = float(num*0.2)
                textbutton i.caption at the_anim(fnum):
                    style 'choice_button'
                    text_style 'choice_button_text'
                    background 'text_answer_idle'
                    hover_background 'text_answer_hover'
                    text_idle_color '#fff'
                    text_hover_color '#fff'
                    if not text_person or not text_person.real_time_text:
                        action [Show('text_message_screen',
                                        sender=current_message),
                                i.action]
                    else:
                        action [i.action]
    
    # For VN mode and phone calls
    elif in_phone_call or vn_choice:
        $ can_see_answer = 0
        add "Phone UI/choice_dark.png"
        vbox:
            style 'choice_vbox'
            spacing 20
            for num, i in enumerate(items):
                $ fnum = float(num*0.2)
                if observing:
                    $ fnum = 0
                if not observing or i.chosen:
                    $ can_see_answer += 1
                    textbutton i.caption at the_anim(fnum):
                        style 'choice_button'
                        text_style 'choice_button_text'
                        xysize (740, 180)
                        background 'call_choice' padding(45,45)
                        hover_background 'call_choice_hover'
                        text_idle_color '#f9f9f9'
                        text_hover_color '#fff'
                        text_align 0.5
                        text_text_align 0.5
                        text_xalign 0.5
                        text_yalign 0.5
                        align (0.5, 0.5)
                        action [i.action]
            # Not a perfect solution, but hopefully provides an 'out'
            # to players who somehow didn't choose a menu option and
            # are now in observing mode
            if can_see_answer == 0:
                textbutton _("(Continue)"):                    
                    style 'choice_button'
                    text_style 'choice_button_text'
                    xysize (740, 180)
                    background 'call_choice' padding(45,45)
                    hover_background 'call_choice_hover'
                    text_idle_color '#f9f9f9'
                    text_hover_color '#fff'
                    text_align 0.5
                    text_text_align 0.5
                    text_xalign 0.5
                    text_yalign 0.5
                    align (0.5, 0.5)
                    action [SetVariable('timed_choose', False), Return()]
            

    # For emails
    elif email_reply:
        use email_hub
        use open_email(current_email)
        add 'Phone UI/choice_dark.png'
        vbox:
            style 'choice_vbox'
            for num, i in enumerate(items):
                $ fnum = float(num*0.2)
                textbutton i.caption at the_anim(fnum):
                    style 'choice_button'
                    text_style 'choice_button_text'
                    background 'text_answer_idle'
                    hover_background 'text_answer_hover'
                    text_idle_color '#fff'
                    text_hover_color '#fff'
                    text_xalign 0.5
                    text_yalign 0.5
                    text_text_align 0.5
                    action [i.action]
    
    # For everything else (e.g. chatrooms)
    else:
        $ can_see_answer = 0
        add 'Phone UI/choice_dark.png'
        vbox:
            style 'choice_vbox'
            if persistent.custom_footers:
                spacing 20
            for num, i in enumerate(items):
                if not observing or i.chosen:
                    $ can_see_answer += 1
                    $ fnum = float(num*0.2)
                    if persistent.custom_footers:
                        textbutton i.caption at the_anim(fnum):
                            style 'choice_button'
                            text_style 'choice_button_text'
                            xysize (740, 180)
                            background 'call_choice' padding(45,45)
                            hover_background 'call_choice_hover'
                            text_idle_color '#f9f9f9'
                            text_hover_color '#fff'
                            text_align 0.5
                            text_text_align 0.5
                            text_xalign 0.5
                            text_yalign 0.5
                            align (0.5, 0.5)
                            if using_timed_menus:
                                action [SetVariable('reply_instant', True), 
                                        SetVariable('using_timed_menus', False),
                                        Hide('answer_countdown'),
                                        i.action]
                            else:
                                action [i.action]
                    else:
                        textbutton i.caption at the_anim:
                            style 'choice_button'
                            text_style 'choice_button_text'
                            if using_timed_menus:
                                action [SetVariable('reply_instant', True), 
                                        SetVariable('using_timed_menus', False),
                                        Hide('answer_countdown'),
                                        i.action]
                            else:
                                action [i.action]
            # Not a perfect solution, but hopefully provides an 'out'
            # to players who somehow didn't choose a menu option and
            # are now in observing mode
            if can_see_answer == 0:
                textbutton _("(Continue)"):
                    style 'choice_button'
                    text_style 'choice_button_text'
                    if persistent.custom_footers:
                        xysize (740, 180)
                        background 'call_choice' padding(45,45)
                        hover_background 'call_choice_hover'
                        text_idle_color '#f9f9f9'
                        text_hover_color '#fff'
                        text_align 0.5
                        text_text_align 0.5
                        text_xalign 0.5
                        text_yalign 0.5
                        align (0.5, 0.5)
                    action [SetVariable('timed_choose', False), Return()]
                            

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


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
# init python:
#    config.overlay_screens.append("quick_menu")

default quick_menu = False

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc"):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

            ## The quit button is banned on iOS and unnecessary on Android.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu_old():

    ## This ensures that any other menu screen is replaced.
    #tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 237
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -16
    xmaximum 675
    yalign 1.0
    yoffset -16

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 26
    top_padding 102

    background "gui/overlay/game_menu.png"
    
style game_menu_navigation_frame:
    xsize 237
    yfill True

style game_menu_content_frame:
    left_margin 34
    right_margin 17
    top_margin 9

style game_menu_viewport:
    xsize 777

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 9

style game_menu_label:
    xpos 43
    ysize 102

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -25


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
    use game_menu(_("About"), scroll="viewport"):

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


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save_old():

    tag menu

    use file_slots(_("Save"))


screen load_old():

    tag menu

    use file_slots(_("Load"))


screen file_slots_old(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    #use game_menu(title):

    fixed:

        ## This ensures the input will get the enter event before any of the
        ## buttons do.
        order_reverse True

        ## The page name, which can be edited by clicking on a button.
        button:
            style "page_label"

            key_events True
            xalign 0.5
            action page_name_value.Toggle()

            input:
                style "page_label_text"
                value page_name_value

        ## The grid of file slots.
        grid gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"

            xalign 0.5
            yalign 0.5

            spacing gui.slot_spacing

            for i in range(gui.file_slot_cols * gui.file_slot_rows):

                $ slot = i + 1

                button:
                    action FileAction(slot)

                    has vbox

                    add FileScreenshot(slot) xalign 0.5

                    text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                        style "slot_time_text"

                    text FileSaveName(slot):
                        style "slot_name_text"

                    key "save_delete" action FileDelete(slot)

        ## Buttons to access other pages.
        hbox:
            style_prefix "page"

            xalign 0.5
            yalign 1.0

            spacing gui.page_spacing

            textbutton _("<") action FilePagePrevious()

            if config.has_autosave:
                textbutton _("{#auto_page}A") action FilePage("auto")

            if config.has_quicksave:
                textbutton _("{#quick_page}Q") action FilePage("quick")

            ## range(1, 10) gives the numbers from 1 to 9.
            for page in range(1, 10):
                textbutton "[page]" action FilePage(page)

            textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 43
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

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


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences_old():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                text "VN Mode" style "menu_text_big"
                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                text "{vspace=20}Sounds" style "menu_text_big"
                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)
                                
                                
                    label _("Voice SFX Volume")
                    
                    hbox:
                        bar value set_voicesfx_volume()

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


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

    use game_menu(_("Help"), scroll="viewport"):

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

screen confirm(message, yes_action, no_action=False):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        background "menu_popup_bkgrd"
        xmaximum 700
        vbox:
            xalign .5
            yalign .5
            spacing 26
            xmaximum 650

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100
                
                textbutton _("Confirm"):
                    text_style "confirm_text"
                    xsize 200
                    background "menu_popup_btn" padding(20,20)
                    hover_foreground "menu_popup_btn_hover"
                    action yes_action
                if no_action:
                    textbutton _("Cancel"): 
                        text_style "confirm_text"
                        xsize 200
                        background "menu_popup_btn" padding(20,20)
                        hover_foreground "menu_popup_btn_hover"
                        action no_action
                

    ## Right-click and escape answer "no".
    if no_action:
        key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    font gui.sans_serif_1
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


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
    
    python:
        yadj.value = yadjValue

    window:
        style "nvl_window"
        frame:
            background "transparent.png"     # or use any semi-transparent image you like
            align (0.5, 0.2)
            
            side "c r":
                area (0, 99, 750, 1069)

                viewport yadjustment yadj:
                    #draggable True
                    mousewheel True
                    has vbox:
                        spacing gui.nvl_spacing

                    ## Displays dialogue in either a vpgrid or the vbox.
                    if gui.nvl_height:

                        vpgrid:
                            cols 1
                            yinitial 1.0

                            use nvl_dialogue(dialogue)

                    else:

                        use nvl_dialogue(dialogue)

                    ## Displays the menu, if given. The menu may be displayed incorrectly if
                    ## config.narrator_menu is set to True, as it is above.
                    for i in items:

                        textbutton i.caption:
                            action i.action
                            style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    python:
        yadj.value = yadjValue

    vbox at incoming_message:
        for d in dialogue:

            window:
                id d.window_id

                fixed:
                    yfit gui.nvl_height is None

                    if d.who is not None:

                        text d.who:
                            id d.who_id

                    text d.what:
                        id d.what_id
                    #if d.who is None:
                    #    pass
                    #else:
                    #    text thetime style "phone_time"


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

    background "gui/nvl.png"
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



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 380

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Menu") action ShowMenu()


#style window:
#    variant "small"
#    #background "gui/phone/textbox.png"

#style radio_button:
#    variant "small"
#    foreground "gui/phone/button/check_[prefix_]foreground.png"

#style check_button:
#    variant "small"
#    foreground "gui/phone/button/check_[prefix_]foreground.png"

#style nvl_window:
#    variant "small"
#    #background "gui/phone/nvl.png"

#style main_menu_frame:
#    variant "small"
#    background "gui/phone/overlay/main_menu.png"

#style game_menu_outer_frame:
#    variant "small"
#    background "gui/phone/overlay/game_menu.png"

#style game_menu_navigation_frame:
#    variant "small"
#    xsize 287

#style game_menu_content_frame:
#    variant "small"
#    top_margin 0

#style pref_vbox:
#    variant "small"
#    xsize 338

#style bar:
#    variant "small"
#    ysize gui.bar_size
#    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
#    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

#style vbar:
#    variant "small"
#    xsize gui.bar_size
#    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
#    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

#style scrollbar:
#    variant "small"
#    ysize gui.scrollbar_size
#    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
#    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

#style vscrollbar:
#    variant "small"
#    xsize gui.scrollbar_size
#    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
#    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

#style slider:
#    variant "small"
#    ysize gui.slider_size
#    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
#    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

#style vslider:
#    variant "small"
#    xsize gui.slider_size
#    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
#    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

#style slider_pref_vbox:
#    variant "small"
#    xsize None

#style slider_pref_slider:
#    variant "small"
#    xsize 507

    
    
    
    
    