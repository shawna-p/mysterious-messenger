# Adding New Ringtones

First, go to [screens_settings.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/screens_settings.rpy "screens_settings.rpy"). There are three dictionaries defined near the beginning of the file, along with three lists, one of each for email, text, and ringtones. As the method is the same for all three, only adding a text tone is described below.

First, add a new entry to `text_tone_dict`. Dictionary entries are a key-value pair, separated by a colon. In this case, the "key" is the name of the tone you want to show the player, and the "value" is the path to the file with the correct sound effect. Note that no two entries can have the same key, so you should preface entries with a category title if you're adding multiple text tones for the same character e.g.

```renpy
default text_tone_dict = {
    'ZEN': 'audio/sfx/Ringtones etc/text_basic_z.wav',
    'Bonus ZEN': 'audio/sfx/Ringtones etc/text_bonus_z.wav'
}
```

Next, you need to add your tone to the `text_tone_list`. You can either add on to an existing list entry to add more text tones in the same category, or you can create a new category like so:

```renpy
default text_tone_list = [ 
    ["Basic", ['Default', '707', 'ZEN']],
    ["Bonus", ['Bonus 707', 'Bonus ZEN']]
]
```

This will create a new category called "Bonus" which is shown when the player selects a new text tone. Note that entries need to match up with the key you entered in the `text_tone_dict` dictionary. And that's all! Your ringtones should show up and be selectable in the Settings menu.
