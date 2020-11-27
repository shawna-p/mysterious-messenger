# Adding Music and SFX

**Example files to look at: [tutorial_6_meeting.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_6_meeting.rpy "tutorial_6_meeting"), [tutorial_3b_VN.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_3b_VN.rpy "tutorial_3b_VN")**

Much like chatrooms, music can be played via

```renpy
play music mystic_chat
```

where `mystic_chat` can be replaced by the name of whatever music you want. There are several files already pre-defined in [variables_music_sound.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/variables_music_sound.rpy) under the heading **BACKGROUND MUSIC DEFINITIONS**.

To add sound effects, use

```renpy
play sound door_knock_sfx
```

where `door_knock_sfx` can be replaced by the name of whatever sound effect you want. There are several files already pre-defined in [variables_music_sound.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/variables_music_sound.rpy) under the heading **SFX DEFINITIONS**.

Note that Ren'Py's built-in music and sound functions have been modified to work with audio captions for this program. The program will notify you if an audio caption has not been defined for an audio file.

If you would like to play a sound that does not have an audio caption, you can give it the `nocaption` argument e.g.

```renpy
play music ringtone nocaption
```

For accessibility purposes, most audio should have a caption, so this argument should be used sparingly.

Previously defined audio captions can be found in [variables_music_sound.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/variables_music_sound.rpy). To learn about adding your own audio, see [Adding new Audio](Adding-new-Audio.md).
