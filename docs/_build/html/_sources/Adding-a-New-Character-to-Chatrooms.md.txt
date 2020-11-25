# Adding a New Character to Chatrooms

First, go to [character_definitions.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/character_definitions.rpy "character_definitions.rpy"). Under the heading **Chatroom Characters** near the middle of the file, you will see several characters already defined.

For the purposes of this tutorial, these examples will show how to add a character named Bob to the program.

You need to give Bob a ChatCharacter object so he can speak in chatrooms. A definition for Bob may look like the following:

```renpy
default b = ChatCharacter(
    name="Bob",
    file_id="b",
    prof_pic="Profile Pics/Bob/bob1.png",
    participant_pic="Profile Pics/b_chat.png",
    heart_color="#f995f1",
    cover_pic="Cover Photos/bob_cover.png",
    status="Bob's Status",
    bubble_color="#ffddfc",
    glow_color="#d856cd",
    homepage_pic="Profile Pics/main_profile_bob.png",
    phone_char=b_phone,
    vn_char=b_vn)
```

Though this looks long, this will ensure all the variables for Bob are set up properly at the start of the game.

Field | Description | Example |
------|-------------|---------|
name | The name of the character as it appears in the chatroom | "Bob" |
file_id | This is used for many things. For example, the program will look for Bob's speech bubbles under "game/images/Bubble/b-Bubble.png" and for phone calls from Bob with the suffix "_incoming_b". This is usually just a string of the name of the variable. | "b"
prof_pic | Profile picture for the character. 110x110px | "Profile Pics/Bob/bob1.png"
participant_pic | The image that shows on the timeline screen to show Bob was present in a chatroom. | "Profile Pics/b_chat.png"
heart_color | The colour of the heart icon that appears when awarding the player a heart point with Bob. | "#f995f1"
cover_pic | Bob's cover photo on his profile screen | "Cover Photos/bob_cover.png"
status | Bob's status update | "I ate a sandwich today."
bubble_color | Optional; if this is not defined you must have an image in `game/images/Bubble/` called `b-Bubble.png`. If this argument is given a colour, it will instead dynamically colour a speech bubble to be that colour. | "#ffddfc"
glow_color | Same as above. If not given, there should be an image in `game/images/Bubble` called `b-Glow.png`. | "#d856cd"
homepage_pic | The picture to display on the home screen which the player clicks on to view Bob's profile. This should generally be a headshot of Bob with a transparent background. | "Profile Pics/main_profile_bob.png"
phone_char | The Character object you defined for Bob for phone calls. See [[Adding a New Character to Phone Calls]] | b_phone
vn_char | The Character object you defined for Bob for VN sections. See [[Adding a New Character to VNs]] | b_vn

Those are the main variables you should set when defining a new character. There are a few additional parameters you can declare if you want:

Field | Description | Example |
------|-------------|---------|
voicemail | The label to jump to for this character's voicemail | "voicemail_1"
right_msgr | Indicates this character should appear on the right side of the messenger (usually False for everyone but the MC) | False
emote_list | A list of all the character's emojis. Currently unused. | False

Finally, below all the ChatCharacter definitions, there are two lists. The first is:

```renpy
default character_list = [ju, z, s, y, ja, v, m, r, ri]
```

If you want Bob to show up on the home screen with a clickable profile, or to show up as a contact in the Contact book, you must add him to this list, e.g.

```renpy
default character_list = [ju, z, s, y, ja, v, m, r, ri, b]
```

The second list is

```renpy
default heart_point_chars = [ c for c in character_list if not c.right_msgr ]
```

This list contains all the characters in `character_list` unless they have the property `right_msgr`, which generally means it's True for everyone except the MC. Characters in this list will appear on the Profile screen with an indicator of how many points the player has with them.

If you want an icon to appear letting the player know how many heart points they have with Bob, you need to define an image called `greet b` since `b` is Bob's file_id. These images are stored in `game/images/Menu Screens/Main Menu` and defined in [variables.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/variables.rpy "variables.rpy") under the heading **Image Definitions - Menu**.

If you don't want Bob to appear in the Profile screen, replace this variable with a list of the characters whose heart points you want to display e.g.

```renpy
default heart_point_chars = [ju, z, s, y, ja]
```

When all is said and done, you should be able to write dialogue for Bob like any other character in a chatroom, e.g.

```renpy
b "How's it going?"
```
