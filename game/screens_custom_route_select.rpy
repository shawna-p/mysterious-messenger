# If you want your program to default to this custom screen,
# uncomment this line
# default persistent.custom_route_select = True

screen custom_route_select_screen():
    vbox:
        style 'route_select_vbox'
        button:
            style 'route_select_button'
            action Start()
            text "Start Game" style 'menu_text_small' align (0.5, 0.5)
       