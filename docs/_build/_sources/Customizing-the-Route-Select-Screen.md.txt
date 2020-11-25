# Customizing the Route Select Screen

**Example files to look at: [screens_menu.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/screens_menu.rpy)**

When you begin a new game, after pressing "Original Story" you'll be taken to the "Mode Select" screen, where there is a large button that says "Start Game". This screen is defined in [screens_menu.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/screens_menu.rpy) and is called `screen route_select_screen()`.

To use your own route select screen, in the **Developer** settings, check off **Use custom route select screen**. This will cause the program to use the screen defined in [screens_custom_route_select.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/screens_custom_route_select.rpy) instead of `screen route_select_screen`. If you want other players to see this screen from the start, you should also uncomment the line `default persistent.custom_route_select = True` in [screens_custom_route_select.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/screens_custom_route_select.rpy).

Your custom route select screen should look like the following:

```renpy
default persistent.custom_route_select = True

screen custom_route_select_screen():
    vbox:
        style 'route_select_vbox'
        button:
            style 'route_select_button'
            action Start()
            text "Start Game" style 'menu_text_small' align (0.5, 0.5)
```

Currently this screen is identical to the regular route select screen. The only element this screen requires is a button that will take the player to the beginning of the game or route. If you are using a common route, it is sufficient to have a button with the action

```renpy
action Start('common_route_start')
```

This will take the player to the `common_route_start` label; this should be a label containing your introductory chatroom. You can see [[Creating an Opening Chatroom]] for more on creating an introductory chatrooom to the route.

## Providing Multiple Route Options

Otherwise, you must create a button for each route you will allow the player to choose. For example, a screen which allows the player to choose between a "Casual" and a "Deep" route might look like the following:

```renpy
screen custom_route_select_screen():
    vbox:
        style 'route_select_vbox'
        button:
            style 'route_select_button'
            action Start('casual_route_start')
            text "Casual Route" style 'menu_text_small' align (0.5, 0.5)
        button:
            style 'route_select_button'
            action Start('deep_route_start')
            text "Deep Route" style 'menu_text_small' align (0.5, 0.5)
```

You can, of course, change the button backgrounds, text, spacing, and other styles. This will create a very simple route select screen with two buttons tacked on top of each other -- one for Casual Route, and one for Deep Route. For more information on customizing screens, you can read the [Ren'Py documentation on Screen Language](https://www.renpy.org/doc/html/screens.html?).

Since you have two separate routes, casual and deep, you will need to have two separate lists of `RouteDay` objects and a `Route` object defined for them. For more on that, see [[Setting up Sequential Chatrooms]]. In this example, the Route object for "casual route" is defined in the variable `casual_route` and deep route in `deep_route`. Then you would have two labels that look like the following:

```renpy
label casual_route_start:
    $ new_route_setup(route=casual_route)
    # (Intro continues from here)
```

and

```renpy
label deep_route_start:
    $ new_route_setup(route=deep_route)
```

If you also want to include an "after_" label for things such as text messages and character status updates, you can add the field `chatroom_label` like so:

```renpy
$ new_route_setup(route=deep_route, chatroom_label="deep_starter_chat")
```

which tells the program that the `after_` label will be located at `after_deep_starter_chat`.

## Skipping the Introductory Chatroom

If you do not want an introductory chatroom, and would instead like the player to begin in the chat hub where they can begin playing after selecting a chatroom from the day list, you still need to include some code after the label you told the program to start the game at. For example, if you want the casual story route to jump right to the chat hub after selecting "Casual Route" from the route select screen, your label should look like the following:

```renpy
label casual_route_start:
    $ new_route_setup(route=casual_route)
    $ new_route_setup(route=my_new_route, chatroom_label="prologue", participants=[ja])
    $ character_list = [ju, z, s, y, ja, m]
    $ heart_point_chars = [ju, z, s, y, ja]
    jump skip_intro_setup
```
