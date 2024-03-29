## A screen which shows a popup for an achievement the first time
## it is obtained. You may modify this however you like.
## The relevant information is:
## a.name = the human-readable name of the achievement
## a.description = the description
## a.unlocked_image = the image of the achievement, now that it's unlocked
## a.timestamp = the time the achievement was unlocked at
screen achievement_popup(a, tag, num):

    zorder 190

    ## Allows multiple achievements to be slightly offset from each other
    default achievement_yoffset = num*135

    frame:
        style_prefix 'achieve_popup'
        at achievement_popout()
        yoffset achievement_yoffset
        has hbox
        add a.unlocked_image:
            fit "contain" ysize 95 align (0.5, 0.5)
        vbox:
            text a.name font gui.curly_font
            text a.description size 25

    # Hide the screen after 5 seconds
    timer 5.0:
        action [Hide("achievement_popup"),
            Show('finish_animating_achievement', num=num, _tag=tag+"1")]

# This, coupled with the action above, ensures that the achievement
# is properly hidden before another achievement can be shown in that "slot".
# If this was done as part of the timer in the previous screen, then it would
# consider that slot empty during the 1 second the achievement is hiding itself.
# That's why this timer is 1 second long.
screen finish_animating_achievement(num):
    timer 1.0 action [SetDict(onscreen_achievements, num, None), Hide()]

style achieve_popup_frame:
    background 'blue_ui_bg'
    padding (10, 10)
    left_margin 15 top_margin 15
    xmaximum config.screen_width-80
style achieve_popup_hbox:
    spacing 10
style achieve_popup_vbox:
    spacing 10
style achieve_popup_text:
    color "#fff"


## Replace this with whatever locked image you want to use as the default
## for a locked achievement.
image locked_achievement = "CGs/album_unlock.webp"

## A transform that pops the achievement out from the left side of
## the screen and bounces it slightly into place, then does the
## reverse when the achievement is hidden.
transform achievement_popout():
    on show:
        # Align it off-screen
        xpos 0.0 xanchor 1.0
        # Ease it back on-screen
        easein_back 1.0 xpos 0.0 xanchor 0.0
    on hide, replaced:
        # Ease it off-screen again
        easeout_back 1.0 xpos 0.0 xanchor 1.0

## The screen that displays a gallery of the player's achievements.
## You may modify this however you like.
## The relevant information is:
## a.name = the human-readable name of the achievement
## a.description = the description
## a.idle_img = the image of the achievement if achieved, or the locked if not
## a.timestamp = the time the achievement was unlocked at
## a.stat_progress = the progress the player has earned towards this achievement
##                   (if it includes the progress stat)
## a.stat_max = the number at which the achievement is considered "achieved"
##              if progress reaches that number.
## You can use a.stat_max and a.stat_progress to display a bar tracking
## how far along the player has progressed, or in text to display text like 3/10
screen achievement_gallery():

    tag menu

    use menu_header("Achievements", Return()):

        viewport id 'achievement_vp':
            style_prefix 'achieve'
            draggable True
            mousewheel True
            scrollbars "vertical"
            has vbox
            null height 10

            for a in Achievement.all_achievements:
                button:
                    # Manually toggle achievements, for development
                    if config.developer:
                        action a.Toggle()
                    has hbox
                    if a.idle_img:
                        fixed:
                            align (0.5, 0.5)
                            xysize (155, 155)
                            add a.idle_img fit "scale-down" ysize 155 align (0.5, 0.5)
                    else:
                        null width -10
                    vbox:
                        text a.name font gui.curly_font size 40
                        text a.description
                        if a.has():
                            text a.timestamp size 22
                        elif a.stat_max:
                            # Has a bar
                            fixed:
                                fit_first True
                                bar value a.stat_progress range a.stat_max
                                text "[a.stat_progress]/[a.stat_max]":
                                    style_suffix "progress_text"

            null height 10

style achieve_viewport:
    xysize (config.screen_width-20, config.screen_height-154)
    yfill True
    align (1.0, 0.0)
style achieve_vscrollbar:
    unscrollable "hide"
style achieve_side:
    xalign 1.0 yalign 1.0
    spacing -5
style achieve_vbox:
    spacing 20
style achieve_button:
    background 'history_chat_active'
    padding (8, 8)
    xsize config.screen_width-40
style achieve_hbox:
    spacing 25
style achieve_text:
    color "#fff"
style achieve_progress_text:
    color "#fff" size 20
    outlines [(1, "#000")]
    align (0.5, 0.5)
