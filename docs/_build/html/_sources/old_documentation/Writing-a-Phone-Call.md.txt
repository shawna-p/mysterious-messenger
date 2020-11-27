# Writing a Phone Call

**Example files to look at: [tutorial_5_coffee.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_5_coffee.rpy "tutorial_5_coffee")**

_A brief overview of the steps required (more detail below):_

> 1. Create a label + the correct suffix for the phone call
>    1. `my_chatroom_outgoing_ja` to make an outgoing call to the character `ja` available
>    2. `my_chatroom_incoming_ja` to trigger an incoming call from the character `ja` after the chatroom has been played
> 2. At the beginning of your new label, write `call phone_begin`
> 3. Write the phone call dialogue
> 4. End the phone call with `jump phone_end`

All phone call labels follow the same naming convention. If your chatroom is named

```renpy
label my_chatroom:
```

then an incoming call should be named

```renpy
label my_chatroom_incoming_ja:
```

and an outgoing call will be called

```renpy
label my_chatroom_outgoing_ja:
```

where `ja` is the variable of the character whom the player is calling or who is calling the player (see [character_definitions.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/character_definitions.rpy "character_definitions.rpy")) for a list of the existing characters).

If the program finds the correct label, after the player has exited the chatroom, the appropriate phone calls will be made available. The player can then go to the phone menu and call the characters. You can make up to one phone call available for every character, regardless of whether or not that character also has an incoming call. In case the player misses the incoming call from that character, **both** the incoming and outgoing calls to that character will be made available, and the player can call the character twice to receive both conversations.

Underneath your phone call label, begin the conversation by typing

```renpy
call phone_begin
```

Then you will write dialogue the same way as you write it for the characters anywhere else in the program. Note that phone calls do not take the arguments you can pass during chatroom dialogue, such as `(pauseVal=0)` or `(img=True)`.

All phone dialogue looks the same regardless of the speaking character (with the exception of the MC, whose dialogue is darker and disappears more quickly). However, using the different characters for the dialogue allows the player to switch off voice acting for particular characters. Currently there is very little voice acting in the program; however, both calls after the chatroom in [tutorial_5_coffee.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_5_coffee.rpy "tutorial_5_coffee") have voice acting included via Ren'Py's automatic voice tagging system.

You may also find Ren'Py's "monologue mode" helpful, since unlike in VN mode, you won't be switching between expressions or different speakers very often. See `tutorial_chat_outgoing_y` in [tutorial_5_coffee.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_5_coffee.rpy "tutorial_5_coffee") for an example of this.

## Writing Menus in Phone Calls

Writing a menu to provide a choice to the player works nearly the same way as a chatroom, with the exception of the line `extend ''` right after the `menu:` statement:

```renpy
menu:
    extend ''
    "Choice 1":
        m "Choice 1"
    "Choice 2":
        m "Choice 2"
```

This shows the dialogue said just before the menu behind the choice screen

## Ending a Phone Call

At the end of your phone call label, type

```renpy
jump phone_end
```

to finish up the phone call.
