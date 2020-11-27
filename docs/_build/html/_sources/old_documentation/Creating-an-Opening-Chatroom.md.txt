# Creating an Opening Chatroom

**Example files to look at: [tutorial_0_introduction.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_0_introduction.rpy "tutorial_0_introduction")**

When the player starts a new game, you may want to have an "introductory" chatroom, to introduce the characters and story before the player begins the route. Though you're free to tell the program to jump to a different label, currently the game starts at the `start` label, which is found in [tutorial_0_introduction.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_0_introduction.rpy "tutorial_0_introduction"). It works a bit differently from regular chatrooms, so it's recommended you have a good grasp of how to create regular chatrooms before you look at this code to modify it.

The line

```renpy
$ new_route_setup(route=tutorial_route)
```

tells the program to set the player on the previously-defined route `tutorial_route`. You should replace this with the name of the Route you have defined.

Next there are two definitions, first

```renpy
$ character_list = [ju, z, s, y, ja, v, m, r, ri]
```

This is the beginning character list for this particular route. Characters in this list have profiles that appear in the chat hub and in the phone contacts list. You can add or remove characters from this list later during the route.

The next definition is

```renpy
$ heart_point_chars = [ju, z, s, y, ja, v, r, ri]
```

This list contains the characters who should have "heart icons" on the Profile page indicating how many hearts the player has earned with this character. You can add or remove characters from this list later during the route.

Next, you will see the line

```renpy
call new_incoming_call(PhoneCall(u, 'n/a'))
```

In the default program, this line causes Unknown to call the player immediately after they start a new route, before they get to the chat home screen. You can also include phone calls that trigger after an opening chatroom, but this phone call is included so you can see what it might look like if you want a phone call at the beginning.

What follows is almost the exact same as any regular phone call: it begins with `call phone_begin` but ends with `call phone_end` instead of `jump phone_end`. The `call` instead of `jump` means that you can continue writing the introduction instead of ending the introduction after the phone call is completed.

Next is the line

```renpy
scene bg black
```

which is optional, but it cleans up the transition between the phone call and the chatroom.

Next, the chatroom begins as normal:

```renpy
call chat_begin('hack')
```

You can add any of the usual chatroom functions to this, including the hack effects, background music, and heart icon calls, to name a few. It's filled out the same way as a regular chatroom, including

```renpy
jump chat_end
```

to finish off the label.

If you want to have characters [send text messages](https://github.com/shawna-p/mysterious-messenger/wiki/Regular-Text-Messages) after the introductory chat, or you'd like to [make phone calls available or trigger an incoming call](https://github.com/shawna-p/mysterious-messenger/wiki/Writing-a-Phone-Call) after this chatroom, it's taken care of the same way as usual, except the label you use is called `starter_chat` __not__ `start`. So incoming calls should look like

```renpy
label starter_chat_incoming_ja:
```

and post-chatroom things (including text messages) will be taken care of in the

```renpy
label after_starter_chat:
```

label. Note that the introductory chatroom does not support a separate VN mode (Story Mode) section after the introductory chatroom. You can, however, include calls to VN sections in the starting label itself.

## Introductory Chatrooms and Multiple Routes

Note that if you have multiple routes you want to have post-chatroom features in, **you must include an additional chatroom_label argument** in your `new_route_setup` call. That may look like the following:

```renpy
label prologue():
    $ new_route_setup(route=my_new_route, chatroom_label="prologue", participants=[ja])
    $ character_list = [ju, z, s, y, ja, m]
    $ heart_point_chars = [ju, z, s, y, ja]
```

This sets up an introductory chatroom for a route in which the characters involved are ju, z, s, y, ja (and the player, m); this is set up with the line `$ character_list = [ju, z, s, y, ja, m]`. The characters who will display on the Profile screen with how many hearts the player has collected are ju, z, s, y, ja -- this is set up via `$ heart_point_chars = [ju, z, s, y, ja]`.

Furthermore, any post-introductory chatroom text messages etc can be written in the label `after_prologue` because the argument `chatroom_label="prologue"` tells the program this chatroom's label is called "prologue", so it will search for a post-chatroom label at `after_prologue`, or for phone calls that use labels such as `prologue_outgoing_ja`.

Finally, the inclusion of `participants=[ja]` as an argument tells the program that the character `ja` should start in the chatroom (i.e. you don't need to write `call enter(ja)` because `ja` is already in the chatroom when it begins). You can leave this argument out, or it can be a list of ChatCharacter objects for the characters you want to start in the chatroom.

## Ending an Introduction

You must always end the introductory chatroom with `jump chat_end` OR, if you want to customize the introduction more, ensure the end of your introduction sets the variables `starter_story = False`, `persistent.on_route = True`, and then you must call or jump to some form of the label `press_save_and_exit`. You can set `vn_choice = True` if you don't want the chatroom Save&Exit sign at the bottom of the screen.

For more information on including VN sections during the introductory chatroom, look at [Including a VN During a Chatroom](Including-a-VN-During-a-Chatroom.md).

## Skipping the Introductory Chatroom

Alternatively, if you do not want any kind of introductory chatroom/phone call/VN mode, you can simply use your introductory label to set up the correct variables and then take the player to the home screen like so:

```renpy
label prologue():
    $ new_route_setup(route=my_new_route, chatroom_label="prologue", participants=[ja])
    $ character_list = [ju, z, s, y, ja, m]
    $ heart_point_chars = [ju, z, s, y, ja]
    jump skip_intro_setup
```

When the player starts a new game, they will be taken immediately to the hub screen without seeing any kind of introductory chatroom/phone call/VN.
