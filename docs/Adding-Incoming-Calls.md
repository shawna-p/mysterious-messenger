# Adding Incoming Calls

**Example files to look at: [tutorial_5_coffee.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_5_coffee.rpy "tutorial_5_coffee")**

To trigger an incoming call, there is a specific naming convention for the label. If your chatroom is called

```renpy
label my_chatroom:
```

then to trigger an incoming call, you must create a label called

```renpy
label my_chatroom_incoming_ja:
```

where `ja` is the variable of the character who will call the player (See [character_definitions.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/character_definitions.rpy "character_definitions.rpy")) for a list of the existing characters).

Note that you can only have one incoming call after a chatroom, so if you define two labels like `label my_chatroom_incoming_ja` and `label my_chatroom_incoming_ju`, then only one of them will show up as an incoming call.

You can then use that label to write the phone call as outlined in [[Writing a Phone Call]]. After the player goes through that chatroom (or its corresponding VN section), they will receive a phone call from that character.
