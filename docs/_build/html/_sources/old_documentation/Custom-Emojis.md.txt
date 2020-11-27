# Custom Emojis

**Example files to look at: [emoji_definitions.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/emoji_definitions.rpy)**

If you'd like to add your own emojis to the game, you need to add a few lines to the `emoji_lookup` dictionary found in [emoji_definitions.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/emoji_definitions.rpy). Emojis are saved as separate `.png` files, and are found in the `/Gifs` folder under `/images`. At the bottom of [emoji_definitions.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/emoji_definitions.rpy), you can see how to define an emoji.

```renpy
image jaehee_angry:
    "Gifs/Jaehee/emo_jaehee_angry1.png"
    0.5
    "Gifs/Jaehee/emo_jaehee_angry2.png"
    0.5
    repeat
```

Most emojis have the name of the character (e.g. `jaehee`) + the name for the expression (e.g. `angry`). The first line should be the path to the first frame of the emoji, followed by `0.5` to tell the program to wait half a second before showing the next image. The next line is the path to the second frame of your emoji, followed by another `0.5`, and then the line `repeat` which tells the program to continue to cycle through the emoji animation while it's on the screen. You can, however, add more frames to your animation and reduce the time for the pause accordingly.

Next, go to the `emoji_lookup` dictionary at the top of the file. You need to insert your own entry in order for the emoji to play sound when it's used in a chatroom.

```renpy
'{image=jaehee_angry}': 'audio/sfx/Emotes/Jaehee/jaehee_angry.mp3'
```

The left side uses the same name as defined for the image before(`jaehee_angry`). Replace `jaehee_angry` with whatever you named your emoji earlier.

The right side after the colon is the path to the sound effect you want to play when this emoji is shown. Currenly all the sound effects are organized in the `audio/sfx/Emotes` folder under their respective characters.

Then, to show your emoji in the chatroom or in text messages, you just need to type

```renpy
ja "{image=jaehee_angry}" (img=True)
```

and it will display the emoji accompanied by the right voice clip. Note that if you use `Script Generator.xlsx` to write chatroom dialogue, it will usually check off the "image" column automatically for you if it detects `{image` in the Dialogue column. However, if the emoji is displaying oddly in-game, you may want to ensure that `(img=True)` accompanies the line in your script.

You may also notice that there are a few variables defined under `emoji_lookup` such as `jaehee_emotes`; these are used in the chatroom generator, which is not yet fully implemented. You can ignore these variables for now.
