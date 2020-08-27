
default textbackup = ChatEntry(filler,"","")

## Used for instant text messaging footers
transform text_footer_disappear:
    yoffset 0 alpha 1.0
    on hide:
        linear 1.0 yoffset 0
        easein 0.2 yoffset -15
        easeout 0.5 yoffset 150 alpha 0.6
        linear 0.1 alpha 0.0

########################################################
## Includes the 'answer' button at the bottom
########################################################
screen text_answer():
    tag chat_footer

    button at text_footer_disappear:
        xsize 468
        ysize 95
        xalign 0.5
        yalign 0.98
        background 'text_answer_active'
        hover_background 'text_answer_animation'
        if not renpy.get_screen("choice"):
            action [Show('text_pause_button'), Return()]
            activate_sound "audio/sfx/UI/answer_screen.mp3"
        add 'text_answer_text' xalign 0.5 yalign 0.5

screen inactive_text_answer():
    tag chat_footer
    button at text_footer_disappear:
        yalign 0.98
        xsize 468
        ysize 95
        xalign 0.5
        background 'text_answer_inactive'
        add 'text_answer_text' xalign 0.5 yalign 0.5

#####################################
# Pause/Play footers
#####################################

## This is the screen that shows the pause button
## (but the chat is still playing)
screen text_pause_button():
    zorder 4
    tag chat_footer

    imagebutton at text_footer_disappear:
        yalign 0.98
        xalign 0.5
        focus_mask True
        idle "text_pause_button"
        if not choosing:
            action [Jump("play"), Return()]


## This screen is visible when the chat is paused;
## shows the play button
screen text_play_button():
    zorder 4
    tag chat_footer

    imagebutton at text_footer_disappear:
        yalign 0.98
        xalign 0.5
        focus_mask True
        idle "text_play_button"
        action [Show('text_pause_button'), Return()]



