# Post-Chatroom Content

**Example files to look at: [tutorial_5_coffee.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_5_coffee.rpy "tutorial_5_coffee")**

If there is anything you would like to have occur after a chatroom, or any additional content you would like to make available to the player (e.g. text messages), you need to create an "after chatroom" label. This is `after_` + the name of your label.

For example, if your chatroom is called

```renpy
label my_chatroom:
```

then the "after label" should be called

```renpy
label after_my_chatroom:
```

This needs to be separate from the main chatroom so the program knows to deliver things like text messages in the event that a chatroom has expired. You can do many things in this label -- the most common use is for [text messages](https://github.com/shawna-p/mysterious-messenger/wiki/Regular-Text-Messages), though you can also use it to [change a character's voicemail](https://github.com/shawna-p/mysterious-messenger/wiki/Changing-a-Character%27s-Voicemail), among other things.
