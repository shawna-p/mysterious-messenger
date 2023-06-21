# If you want your program to default to this custom screen,
# uncomment this line
# default persistent.custom_route_select = True

screen custom_route_select_screen():
    vbox:
        style_prefix 'route_select' # Remove this if you want your own styles
        button:
            ysize 210 # Set the height of the button
            # The image that goes on the left of the button
            add 'Menu Screens/Main Menu/route_select_tutorial.webp':
                align (0.08, 0.5)
            action Start("my_route_introduction")
            # The box with text on the right side of the button
            frame:
                text "My New Route"
        button:
            ysize 210 # Set the height of the button
            # The image that goes on the left of the button
            add 'Menu Screens/Main Menu/route_select_tutorial.webp':
                align (0.08, 0.5)
            action Start("prologue")
            # The box with text on the right side of the button
            frame:
                text "Prologue"

        button:
            action Start("casual_start")
            add 'Menu Screens/Main Menu/route_select_casual.webp':
                align (0.08, 0.5)
            frame:
                text "Casual Story"




