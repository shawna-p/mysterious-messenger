## You can add or modify this screen to add whatever options
## or features you like, including After Endings, DLC, etc.
screen game_extras():
    modal True
    add "#000a"

    frame:
        xsize 675
        ysize 200
        background Fixed('menu_settings_panel_light',
            'menu_settings_panel_bright', yfit=True)
        align (0.5, 0.5)
        bottom_padding 20
        xpadding 18

        imagebutton:
            align (1.0, 0.0)
            xoffset 18
            auto 'input_close_%s'
            keysym "rollback"
            action Hide('game_extras')

        text "Extras" style "settings_style" xpos 55 ypos 5

        vbox:
            style_prefix "other_settings"
            yalign 0.5 xalign 0.0
            null height 30
            textbutton _("Real-Time Mode"):
                style_prefix "check"
                action ToggleField(persistent, "real_time")
