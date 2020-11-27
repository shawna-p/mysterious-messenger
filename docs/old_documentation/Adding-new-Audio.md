# Adding new Audio

In order to include audio captions, defining new music and sound effects to play in the program requires a few extra steps.

## Defining new music

First, go to [variables_music_sound.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/variables_music_sound.rpy). For this example, a file called "Jingle Bells" will be added.

First, define a variable that leads to the audio file.

```renpy
define jingle_bells = "audio/music/jingle_bells.mp3"
```

Next, in the `music_dictionary`, add `jingle_bells` at the end like so:

```renpy
default music_dictionary = {
    # (Complete definition omitted)
    april_dark_secret : "Suspenseful 8-bit music",

    jingle_bells : "Jolly Christmas music"
}
```

Try to keep the description short while still conveying the general feel/mood of the song.

You can now play your music in-game via

```renpy
play music jingle_bells
```

## Defining new sound effects

First, go to [variables_music_sound.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/variables_music_sound.rpy). For this example, a file called "glass_breaking" will be added.

First, define a variable that leads to the audio file.

```renpy
define glass_breaking_sfx = "audio/sfx/glass_breaking.mp3"
```

Next, in the `sfx_dictionary`, add `glass_breaking_sfx` at the end like so:

```renpy
default sfx_dictionary = {
    # (Complete definition omitted)
    door_open_sfx : "The door opens",

    glass_breaking_sfx : "A glass shatters"
}
```

As with the background music, the audio caption should briefly describe the action or event the sound effect is meant to convey.

You can now play your sound effect in-game via

```renpy
play sound glass_breaking_sfx
```
