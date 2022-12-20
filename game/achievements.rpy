## A screen which shows a popup for an achievement the first time
## it is obtained. You may modify this however you like.
## The relevant information is:
## a.name = the human-readable name of the achievement
## a.description = the description
## a.unlocked_image = the image of the achievement, now that it's unlocked
screen achievement_popup(a):

    frame:
        background 'blue_ui_bg'
        padding (10, 10)
        left_margin 15 top_margin 15
        xmaximum config.screen_width-80
        at achievement_popout()
        has hbox
        spacing 10
        add a.unlocked_image:
            fit "contain" ysize 95
        vbox:
            spacing 10
            text a.name font gui.curly_font color "#fff"
            text a.description size 25 color "#fff"

    # Hide the screen after 6 seconds
    timer 5.0 action Hide("achievement_popup")


## Replace this with whatever locked image you want to use as the default
image locked_achievement = "CGs/album_unlock.webp"

## A transform that pops the achievement out from the left side of
## the screen and bounces it slightly into place, then does the
## reverse when the achievement is hidden.
transform achievement_popout():
    # Align it off-screen
    on show:
        xpos 0.0 xanchor 1.0
        easein_back 1.0 xpos 0.0 xanchor 0.0
    on hide:
        easeout_back 1.0 xpos 0.0 xanchor 1.0

screen achievement_gallery():

    tag menu

    use menu_header("Achievements", Return()):
        null height 10

        viewport id 'achievement_vp':
            xysize (config.screen_width-20, config.screen_height-234)
            yfill True
            align (0.5, 0.0)
            draggable True
            mousewheel True
            scrollbars "vertical"
            vscrollbar_unscrollable "hide"
            side_xalign 1.0
            side_spacing 15
            has vbox
            spacing 20

            for a in Achievement.all_achievements:
                button:
                    background "#fff5"
                    padding (8, 8)
                    xsize config.screen_width-40
                    has hbox
                    spacing 25
                    add a.idle_img
                    vbox:
                        text a.name color "#fff" font gui.curly_font size 40
                        text a.description color "#fff"
                        text a.timestamp color "#fff" size 22

            textbutton "Achieve 1":
                selected test_achievement.has()
                text_selected_color "#0ff"
                action If(test_achievement.has(),
                    Function(test_achievement.clear),
                    Function(test_achievement.grant))
            textbutton "Achieve 2":
                selected hidden_achievement.has()
                text_selected_color "#0ff"
                action If(hidden_achievement.has(),
                    Function(hidden_achievement.clear),
                    Function(hidden_achievement.grant))



