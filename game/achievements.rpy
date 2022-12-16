## A screen which shows a popup for an achievement the first time
## it is obtained. You may modify this however you like.
## The relevant information is:
## a.name = the human-readable name of the achievement
## a.description = the description
## a.unlocked_image = the image of the achievement, now that it's unlocked
screen achievement_popup(a):

    frame:
        at achievement_popout()
        has hbox
        add a.unlocked_image
        vbox:
            text a.name
            text a.description



transform achievement_popout():
    # Align it off-screen
    on show:
        xpos 0.0 xanchor 1.0
        easein_back 1.0 xpos 0.0 xanchor 0.0
    on hide:
        easeout_back 1.0 xpos 0.0 xanchor 1.0

