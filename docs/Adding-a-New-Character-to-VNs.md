# Adding a New Character to VNs

First, go to [character_definitions.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/character_definitions.rpy "character_definitions.rpy"). Under the header **Visual Novel Mode** you will see several characters defined already.

For the purposes of this tutorial, these examples will show how to add a character named Bob to the program.

You need to give Bob a Character object so he can speak in VN mode (Story mode). A definition for Bob may look like the following:

```renpy
default b_vn = Character("Bob",
    kind=vn_character,
    image="bob",
    window_background=Transform("VN Mode/Chat Bubbles/vnmode_9.png", alpha=persistent.vn_window_alpha),
    voice_tag="b_voice")
```

These variables are explained below.

Field | Description | Example |
------|-------------|---------|
name | The name of the character as it should appear during a VN | "Bob" |
kind | Allows this Character to "inherit" from another, previously defined Character. In this case, the `vn_character` object already has many attributes related to VN mode defined, so inheriting them means you don't have to retype them. | vn_character |
image | This is the tag Ren'Py will apply to images if you want to include attribute tags during this character's dialogue (See [Changing Outfits and Expressions](Changing-Outfits-and-Expressions.md)) | "bob" |
window_background | The image used for the background of this character's dialogue. The part that you will change is the string `"VN Mode/Chat Bubbles/vnmode_9.png"`. The rest of that statement tells Ren'Py to make this background more or less transparent based on the value of `persistent.vn_window.alpha`. This allows players some degree of control over the window opacity. | Transform("VN Mode/Chat Bubbles/vnmode_9.png", alpha=persistent.vn_window_alpha) |
voice_tag | The voice tag associated with this character. Allows players to switch voice acting for this character on and off. This should be Bob's file_id + "_voice" | "b_voice" |

Optionally, you can also include the argument `who_color`. This changes the colour of the character's name displayed above their dialogue when they speak in VN mode.

Field | Description | Example |
------|-------------|---------|
who_color | Changes the colour of the character's name in the VN dialogue box. | "#fff5ca" |

## Note on Voiced Characters

If you don't want to include a `voice_tag` for Bob, you will also need to modify a line in [screens_settings.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/screens_settings.rpy "screens_settings.rpy") under the screen `preferences()`. Partway down there is a `frame` containing the toggles for all voiced characters. In particular:

```renpy
vbox:
    box_wrap True
    box_wrap_spacing 10
    spacing 20
    yalign 0.5
    for c in all_characters:
        # Unknown and Saeran are lumped into Ray's
        # voice button and MC doesn't speak
        if c not in [u, sa, m]:
            use voice_buttons(c)
    use voice_buttons("Other", 'other')
```

If you don't want Bob to have a voice button, you need to add him to the list which currently contains `[u, sa, m]` to read `[u, sa, m, b]`.

## Declaring a LayeredImage for a New Character

At the bottom of [character_definitions.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/character_definitions.rpy "character_definitions.rpy") are the layeredimage definitions for all the existing characters. These allow you to show the characters on-screen and easily change their expressions. In order to show Bob on-screen, you will also need to define a `layeredimage bob`. As this is unchanged from the usual way of defining layeredimages, you can look to [Ren'Py's layeredimage documentation](https://www.renpy.org/doc/html/layeredimage.html "Ren'Py layeredimage documentation") for more on that.

If possible, expressions should be separate from the character's body, and accessories such as glasses should be separate from facial expressions.

### "Story Mode" Images

If you would also like to define a "Story Mode" image for your new character (aka the image that shows up beneath a chatroom to let you enter story mode/VN mode), see [Setting up Sequential Chatrooms](Setting-up-Sequential-Chatrooms.md).
