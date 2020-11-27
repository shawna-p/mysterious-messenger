# Changing a Character's Voicemail

**Example files to look at: [tutorial_5_coffee.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_5_coffee.rpy "tutorial_5_coffee")**

Voicemail is part of a character's definition. If the program determines theree are no phone calls available for a character when the player phones them, it will automatically play the character's voicemail instead.

To update a character's voicemail, type

```renpy
$ ja.voicemail = 'voicemail_1'
```

where `ja` is the variable of the character whose voicemail you're changing, and `voicemail_1` is the name of the label where the voicemail call is.

Existing voicemails are defined in [phonecall_system.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/phonecall_system.rpy "phonecall_system.rpy"). They are written the same way as a regular phone call, though there are no restrictions on what the label can be called (but it's recommended you pick a descriptive name for it; probably including the word 'voicemail').

If you want to write a "generic" voicemail message, there is a character named `vmail_phone` that you can use to write the dialogue. Otherwise, you can use the characters' regular variables to write dialogue (e.g. `ja "Some dialogue"`).
