# Adding a New Character to Phone Calls

First, go to [character_definitions.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/character_definitions.rpy "character_definitions.rpy"). Under the heading **Phone Call Characters** you will see several characters already defined.

For the purposes of this tutorial, these examples will show how to add a character named Bob to the program.

You need to give Bob a Character object so he can speak in phone calls. A definition for Bob may look like the following:

```renpy
define b_phone = Character("Bob",
    kind=phone_character,
    voice_tag="b_voice")
```

These variables are explained below.

Field | Description | Example |
------|-------------|---------|
name | The name of the character | "Bob" |
kind | Allows this Character to "inherit" from another, previously defined Character. In this case, the `phone_character` object already has many attributes related to phone calls defined, so inheriting them means you don't have to retype them. | phone_character |
voice_tag | The voice tag associated with this character. Allows players to switch voice acting for this character on and off. This should be Bob's file_id + "_voice" | "b_voice" |

See [Note on Voiced Characters](https://github.com/shawna-p/mysterious-messenger/wiki/Adding-a-New-Character-to-VNs#note-on-voiced-characters) for more information on adding a voice tag to a character.

So long as you have passed your definition of `default b = ChatCharacter(...)` the variable `phone_char=b_phone`, you can now write dialogue for phone calls like so

```renpy
b "How are you, [name]?"
```
