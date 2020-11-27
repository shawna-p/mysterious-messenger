# Writing a VN Section

**Example files to look at: [tutorial_6_meeting.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_6_meeting.rpy "tutorial_6_meeting"), [tutorial_3b_VN.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_3b_VN.rpy "tutorial_3b_VN")**

_A brief overview of the steps required (more detail below):_

> 1. Create a label using the name of the chatroom + the suffix `_vn` (e.g. `label my_chatroom_vn`)
>    1. (Optional) Indicate a character the VN is associated with by including their file_id as another suffix (e.g. `label my_chatroom_vn_s`)
>    2. (Optional) Indicate that this chatroom is the party by including the suffix `_party` (e.g. `label my_chatroom_party`)
> 2. In the VN label, write `call vn_begin`
> 3. Add music with `play music your_music_var`
> 4. Set up the background with `scene bg your_bg`
>    1. (Optional) Use transitions like `with fade` e.g. `scene bg your_bg with fade`)
>    2. (Optional) Write `pause` after your `scene` statement to give the player a moment to look at the background.
> 5. Fill out the dialogue and character expressions
> 6. Finish the label with `jump vn_end`

First, much like creating a chatroom, you must create a label for the VN. For a Story Mode icon not associated with any character, you can just use the name of the chatroom + the suffix `_vn` and the program will know to set it up after that chatroom e.g.

```renpy
label my_chatroom:
```

has the VN label

```renpy
label my_chatroom_vn:
```

If you would instead like the VN to have a certain character's image associated with it, you must add another suffix: `_` + the file_id of that character e.g.

```renpy
label my_chatroom_vn_ju:
```

will show up in the program as a VN section associated with Jumin.

Alternatively, you can also use the suffix `_party` to indicate a VN contains the party. This will look like

```renpy
label my_chatroom_party:
```

Underneath your label, begin with

```renpy
call vn_begin
```

This sets some important variables before the VN. Next, set the background for your VN. It begins as black.

```renpy
scene bg rika_apartment with fade
```

where `bg rika_apartment` is a pre-defined variable you can find in [vn_mode.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/vn_mode.rpy "vn_mode.rpy") or one you defined yourself. Backgrounds should be `750x1334` pixels. `with fade` indicates the background should fade in from black.

If you want the player to have a moment to look at the background before you move on, you can write `pause` after showing the image, e.g.

```renpy
scene bg rika_apartment with fade
pause
```

## Writing a VN Menu

Writing a menu in a VN is the same as it is in phone calls; that is, you need to write `extend ''` right after `menu:` and before the choices.

```renpy
menu:
    extend ''
    "Choice 1":
        m "Choice 1"
    "Choice 2":
        m "Choice 2"
```

This tells the program to display the last line of dialogue underneath the choice menu.

## Awarding heart points in a VN

You award heart points to a player the same way as you would anywhere else:

```renpy
call heart_icon(ja)
```

where `ja` is the variable of the character you're awarding a heart point to.
