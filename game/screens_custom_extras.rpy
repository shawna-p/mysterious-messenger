## You can add or modify this screen to add whatever options
## or features you like, including After Endings, DLC, etc.
screen game_extras():
    modal True
    add "#000a"

    frame:
        xysize (675, 780)
        background Fixed('menu_settings_panel_light',
            'menu_settings_panel_bright')
        align (0.5, 0.5)
        bottom_padding 20

        imagebutton:
            align (1.0, 0.0)
            xoffset 3 yoffset -3
            auto 'input_close_%s'
            action Hide('developer_settings')

        text "Extras" style "settings_style" xpos 55 ypos 5

        vbox:
            style_prefix "other_settings"
            yalign 0.5
            null height 30

            frame:
                xsize 680
                background "menu_settings_panel"
                has vbox
                spacing 6
                first_spacing 15
                text "Variables for testing":
                    style "settings_style" xpos 45 ypos -3
                style_prefix "check"
                textbutton _("Real-Time Mode"):
                    action ToggleField(persistent, "real_time")
