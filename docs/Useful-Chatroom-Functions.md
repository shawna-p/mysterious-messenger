# Useful Chatroom Functions

**You can see many of these functions in use in [tutorial_1_chatroom.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_1_chatroom.rpy "tutorial_1_chatroom")**

## How to let the player make a choice

```renpy
call answer
menu:
    "Choice 1":
        m "Choice 1" (pauseVal=0)
        # More dialogue here
    "Choice 2":
        m "Choice 2" (pauseVal=0)
        # More dialogue here
# Regular dialogue continues here
```

The main thing to remember is to write `call answer` before `menu:`, which will bring up the "answer" button at the bottom of the screen and pause the chat.

You can add as many choices as you want to the menu, although only 5 options will fit on the screen at once. Any dialogue that is indented after a choice will only be shown to the player if they pick that choice. Dialogue intended at the same level as `menu:` will be shown to players regardless of what option they picked in the menu. You can use the `TAB` key to indent text an additional level to the right, though make sure your editor is using spaces to indent code (since Python and Ren'Py will have errors if you use actual `TAB` characters).

After a choice, the MC usually has dialogue. You can see that under `"Choice 1":`, the dialogue is repeated, but this time it's preceded by `m`. `m` is the variable used to make the MC speak in chatrooms. Unless the menu option is paraphrased, you need to copy the line of dialogue from the choice below for `m` to say.

Secondly, there's also an argument after the MC's dialogue: `(pauseVal=0)`. The included spreadsheet will usually include this argument for you when the MC speaks (see [[Using the Chatroom Spreadsheet]]). It tells the program not to wait before posting this message. Otherwise, after choosing an answer, the program would pause for a moment to simulate "typing time" for the MC to send their message. Since this can be rather disorienting after a choice, adding `(pauseVal=0)` after the dialogue removes this wait time.

However, the MC doesn't need to send a message after a choice, or you can have other characters send things. For example, one of your choices could be `"(Remain silent)"`, in which case the MC probably won't send a message after the choice. (You can see an example of this in [tutorial_8_plot_branches.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_8_plot_branches.rpy)).

## How to show a heart icon

heart_icon |
-----------|
`character, bad=False` |

To show heart icons to the player and award them heart points, use

```renpy
call heart_icon(s)
```

where `s` is the variable of the character whose heart point you'd like to show. The options built into the program are:

* ja (Jaehee)
* ju (Jumin)
* r (Ray/Saeran)
* ri (Rika)
* s (Seven)
* sa (Saeran/Ray)
* u (Unknown, a white heart)
* v (V)
* y (Yoosung)
* z (Zen)

If you'd like to add your own character to give a heart point to, see [[Adding a New Character to Chatrooms]]. Both Ray and Saeran's heart points count towards the same character.

There is also an optional second argument in the `heart_icon` call:

```renpy
call heart_icon(s, bad=True)
```

The `bad=True` argument tells the program that this heart is a "bad" heart icon -- in other words, it indicates that this answer, while awarding the player a heart point, also counts towards a bad ending. In this way, you can conceal which answers lead to the "Good" end since you can award the player a heart point for both the good and bad ending answers (See [tutorial_6_meeting.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_6_meeting.rpy "tutorial_5_coffee") for an example of this). When you get to a plot branch, you can have the program calculate whether the player has more "good" or "bad" heart points with a character. See [[Plot Branches]] for more information on this.

Similarly, to show a "heartbreak" icon with a character, write

```renpy
call heart_break(s)
```

where `s` is the variable of the character whose heart break you'd like to show. This will *always* subtract from the character's "good" heart points and never the "bad" points.

## How to show a banner

```renpy
call banner('name of banner')
```

where `'name of banner'` is replaced with the actual name e.g. `call banner('heart')`. The available banners are:

* lightning
* heart
* annoy
* well

The names are case-sensitive when you call them.

## How to make a character enter/exit the chatroom

To get the message `Character has entered the chatroom` type:

```renpy
call enter(y)
```

where `y` is the variable of the character who is entering (see [How to show a heart icon](#how-to-show-a-heart-icon) for a list).

To get the message `Character has left the chatroom` type:

```renpy
call exit(y)
```

where `y` is the variable of the character who is exiting.

## How to update a character's profile picture

To update a character's profile picture, use

```renpy
$ ja.prof_pic = 'Profile Pics/Jaehee/your-pic.jpg'
```

where `ja` is the character whose profile picture you'd like to change, and `'Profile Pics/Jaehee/your-pic.jpg'` is the path to the profile picture you'd like to update to. Profile pictures should be 110x110 pixels. You can also provide a larger image, up to 314x314 pixels, for use on the character's profile page and on the phone call screens. This image should be in the same folder as the original, and should end with `-b` (b for "big") just before the file extention.

So, if you have a regular image that's 110x110 in `Profile Pics/Jaehee/your-pic.jpg`, the program will look for the big version of the profile picture at `Profile Pics/Jaehee/your-pic-b.jpg`.

You should usually change a character's profile picture at the beginning of a chatroom, just after the `chat_begin` call.

### Changing the MC's profile picture

Updating the MC's profile picture is done differently. Currently the program has 5 default images that the player can cycle through by clicking on the profile picture in the Profile tab on the Settings screen. If you have a custom picture you'd like to use, you can drop it in the `game/Drop Your Profile Picture Here` folder. The dimensions should be at least 110x110 pixels, though images that are up to 363x363 pixels will display better on the profile screen. The program does not search for multiple image sizes and will instead scale up and down as appropriate (which can lead to fuzzy images or odd anti-aliasing with particularly small or large pictures). The program takes `png`, `jpg`, non-animated `gif` and `webp` image formats. You can add as many or as few pictures as you like and are free to remove the existing images in that folder.

## How to update a character's cover photo

To update a character's cover photo, use

```renpy
$ ja.cover_pic = 'Cover Photos/Jaehee/your-pic.jpg'
```

where `ja` is the character whose cover photo you'd like to change, and `'Cover Photos/Jaehee/your-pic.jpg'` is the path to the cover photo you'd like to update to. Cover photos should be 750x672 pixels.

You should usually change a character's cover photo at the beginning of a chatroom, just after the `chat_begin` call, as you do when changing a character's profile photo. Don't forget to do this both for the regular chatroom and the expired chatroom, if applicable.

## How to update a character's status

To update a character's status, use

```renpy
$ ja.status = "This is my new status update."
```

where `ja` is the character whose status you'd like to change, and `"This is my new status update."` is whatever you'd like to update their status to.

You should usually change a character's status at the beginning of a chatroom, just after the `chat_begin` call, as you do when changing a character's profile photo or cover photo.
