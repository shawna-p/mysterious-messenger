# Unlockable Routes

If you want to keep certain features "locked" until the player has fulfilled a condition of your choosing (e.g. preventing the player from going through Character B's route until after they have gone through Character A's route), you need to set up your own persistent variables to keep track of whether the player has fulfilled your desired condition or not. You can define these variables anywhere you like, though [variables.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/variables.rpy) is a good place if you're unsure.

For this example, the program will check whether or not the player has successfully gotten the Good End in Tutorial day. First, define the variable:

```renpy
default persistent.tutorial_good_end_complete = False
```

`tutorial_good_end_complete` is the name of your created field in the `persistent` object; variables preceeded by `persistent` will be saved across playthroughs. The variable is first initialized to `False` and will be set to `True` after the player has successfully gone through the Good End.

A player who has gone through the Tutorial Good End will have finished the party VN called `tutorial_good_end_party` found in [tutorial_8_plot_branches.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_8_plot_branches.rpy "tutorial_8_plot_branches"). The last lines of that label are currently as follows:

```renpy
$ ending = 'good'
jump vn_end_route
```

This ends the route and takes the player back to the menu, so just before this you can set your variable to `True`.

```renpy
$ persistent.tutorial_good_end_complete = True
$ ending = 'good'
jump vn_end_route
```

Note that you're not limited to putting your variable check right at the end of a route -- you could also put the `$ persistent.your_variable_here = True` check after a menu option, or after a particular phone call, for example.

Note that if you don't need the program to remember a variable across playthroughs (for example, if you want the program to remember that the player told Bob "I own a cat" so that you can later have him mention the cat when you're on his route), you **do not** need `persistent.` in front of your variable definition and can simply write `default owns_cat = False` and then set `$ owns_cat = True` after the line where the player declares they own a cat. This variable will be reset to its default of `False` whenever the player begins a new game.

## Customizing a screen based on variables

If you only want to allow the player to access a route after a certain condition is fulfilled, you will need to add some extra code to the route select screen in [screens_menu.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/screens_menu.rpy). This example will assume you've defined that screen as seen in [[Customizing the Route Select Screen]].

In this example, Deep Route will be shown as "locked" until after the player has completed the Good End of Tutorial Day. Everything in `route_select_screen` will remain as shown in [[Customizing the Route Select Screen]] except for the Deep Route button:

```renpy
vbox:
    style 'route_select_vbox'
    button:
        style 'route_select_button'
        action Start('casual_route_start')
        text "Casual Route" style 'menu_text_small' align (0.5, 0.5)
    button:
        style 'route_select_button'
        if persistent.tutorial_good_end_complete:
            add 'plot_lock' align (0.7, 0.5)
            action Show("confirm", message="This route is locked until you've completed the Tutorial Good End.", yes_action=Hide('confirm'))
            hover_foreground None
        else:
            action Start('deep_route_start')
        text "Deep Route" style 'menu_text_small' align (0.5, 0.5)
```

This will show a "lock" icon next to the button for Deep Route if `persistent.tutorial_good_end_complete` is `False`. If the player clicks on Deep Route without having seen the Tutorial Good End, they will get a confirmation screen telling them that Deep Route is locked until they have completed the Tutorial Good End.

After the player has completed the Tutorial Good End, the lock symbol will disappear and clicking on Deep Route will take the player to the beginning of that route as usual.

Alternatively you could also put the `if persistent.tutorial_good_end_complete` before the button for Deep Route, which would cause it to not be shown at all to a player who hasn't unlocked it yet.

```renpy
vbox:
    style 'route_select_vbox'
    button:
        style 'route_select_button'
        action Start('casual_route_start')
        text "Casual Route" style 'menu_text_small' align (0.5, 0.5)
    if persistent.tutorial_good_end_complete:
        button:
            style 'route_select_button'
            action Start('deep_route_start')
            text "Deep Route" style 'menu_text_small' align (0.5, 0.5)
```

Keep in mind, however, that it's usually a better idea to show the player this content exists so they have a reason to come back and play more of the game.
