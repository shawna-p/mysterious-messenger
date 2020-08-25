#************************************
# Visual Novel Mode
#************************************

#####################################
## VN Setup
#####################################

label vn_begin(nvl=False):
    return
    if starter_story:
        $ set_name_pfp()
    window auto
    $ collected_hp = {'good': [], 'bad': [], 'break': []}
    scene bg black
    stop music
    hide screen starry_night
    hide screen phone_overlay
    hide screen messenger_screen
    hide screen pause_button
    hide screen timeline

    # Hide all the popup screens
    $ hide_all_popups()

    if not nvl:
        show screen vn_overlay
    else:
        nvl clear
    $ vn_choice = True
    $ _history_list = [] # This clears the History screen
    $ _history = True

    if (not _in_replay and
            ((isinstance(current_timeline_item, ChatRoom)
                and current_timeline_item.story_mode.played)
            or (isinstance(current_timeline_item, StoryMode)
                and current_timeline_item.played))):
        if not persistent.testing_mode:
            $ observing = True
        else:
            pass
    else:
        $ observing = False
    if _in_replay:
        $ observing = True
        $ set_name_pfp()
        $ set_pronouns()

    return

## Call to end a VN section
label vn_end():
    return
    if _in_replay:
        $ renpy.end_replay()
    hide screen vn_overlay
    $ renpy.retain_after_load()
    jump press_save_and_exit

label vn_end_route():
    $ config.skipping = False
    $ choosing = False
    stop music

    if ending == 'good':
        scene bg good_end
    elif ending == 'normal':
        scene bg normal_end
    elif ending == 'bad':
        scene bg bad_end
    $ ending = False
    if current_timeline_item.expired and not current_timeline_item.buyback:
        $ persistent.completed_story.add(
                        current_timeline_item.expired_chat)
    else:
        $ persistent.completed_story.add(
                        current_timeline_item.chatroom_label)
    if current_timeline_item.vn_obj:
        $ persistent.completed_story.add(
                        current_timeline_item.vn_obj.vn_label)

    pause
    if _in_replay:
        $ renpy.end_replay()
    jump restart_game

#####################################
## This screen shows the clock
#####################################

screen vn_overlay():

    hbox:
        add my_menu_clock xalign 0.0 yalign 0.0 xpos 5


################################################
## This is the custom history screen
## for VN Mode
## https://www.renpy.org/doc/html/history.html
################################################

screen history():

    tag menu

    # Avoid predicting this screen, as it can be very large.
    predict False

    # Allow the user to darken the VN window for better contrast
    add Transform('#000', alpha=max(((persistent.vn_window_dark
                        + persistent.vn_window_alpha) / 2.0), 0.7))

    # Close button
    button:
        xalign 1.0
        yalign 0.0
        focus_mask True
        add "close_button"
        action Hide('history')#Return()
        text "Close" style "CG_close":
            if persistent.dialogue_outlines:
                outlines [ (2, "#000",
                            absolute(0), absolute(0)) ]
                font gui.sans_serif_1xb


    viewport:
        yinitial 1.0
        scrollbars "vertical"
        mousewheel True
        draggable True
        side_yfill True

        ysize 1235
        yalign 1.0

        vbox:
            style_prefix "history"
            spacing 20
            null height 5
            for h in _history_list:

                fixed:
                    yfit True

                    if h.who:

                        label h.who + ':':
                            style "history_name"
                            if persistent.dialogue_outlines:
                                text_outlines [ (absolute(2), "#000",
                                            absolute(0), absolute(0)) ]
                                text_font gui.sans_serif_1xb

                            # Take the color of the who text from the
                            # Character, if set.
                            if "color" in h.who_args:
                                text_color h.who_args["color"]

                    $ what = renpy.filter_text_tags(h.what,
                                    allow=gui.history_allow_tags)
                    text what:
                        if persistent.dialogue_outlines:
                            outlines [ (absolute(2), "#000",
                                        absolute(0), absolute(0)) ]

            if not _history_list:
                label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.
define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5
