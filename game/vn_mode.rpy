#************************************
# Visual Novel Mode
#************************************

#####################################
## VN Setup
#####################################

label vn_begin(nvl=False):
    return

## Call to end a VN section
label vn_end():
    return

label vn_end_route():
    jump end_route

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
