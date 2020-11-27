# Pronoun Integration

**Example files to look at: [tutorial_6_meeting.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_6_meeting.rpy "tutorial_6_meeting")**

This program allows the player to change their pronouns whenever they desire during the game. This means that any reference to the player's gender or use of pronouns to refer to the player will need to be taken care of via variables. In [variables.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/variables.rpy "variables.rpy") under the **Short Forms/Startup Variables** heading you will find many default variables already defined.

## Defining additional helper variables

If you would like to define additional variables to help with typing dialogue, you must first define the variable in [variables.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/variables.rpy "variables.rpy") as mentioned above, and also under the `set_pronouns()` function in [screens_menu.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/screens_menu.rpy).

For this example, a variable called `go_goes` will be defined for the three main pronoun options.

First, in [variables.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/variables.rpy "variables.rpy") under the **Short Forms/Startup Variables** heading, add

```renpy
default go_goes = "go"
```

Then in [screens_menu.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/screens_menu.rpy) under the function `set_pronouns()` add

```renpy
global go_goes
```

at the top of the function. Then under both `if persistent.pronoun == "female"` and `elif persistent.pronoun == "male"` add the line

```renpy
go_goes = "goes"
```

and under `elif persistent.pronoun = "non binary"` add

```renpy
go_goes = "go"
```

That is all! To use the new variable in dialogue, you can type

```renpy
y "Yeah, [they] said [they] usually [go_goes] out on Fridays."
```

If the player has he/him pronouns, in-game this will display as **Yeah, he said he usually goes out on Fridays.**. If the player has they/them pronouns, this will instead display as **Yeah, they said they usually go out on Fridays.**

Variables are capitalization-sensitive, so you can also create "capitalization" versions of variables (e.g. you could have a separate `Go_Goes` variable that is either `Go` or `Goes` depending on preferred pronouns).

There is no limit to how many of these variables you can make, so feel free to create as many as you need to write your script more easily.
