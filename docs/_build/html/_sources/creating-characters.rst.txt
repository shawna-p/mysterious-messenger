====================
Creating Characters
====================

.. toctree::
    :caption: Navigation

    creating-Characters

While Mysterious Messenger does come with several characters already defined, you may want to define your own characters to participate in chatrooms or phone the player. There are a few definitions and several images you will need to set up in order for your character to work within the program.

On this page, the examples will show how to add a character named Emma to the program.

Checklist for a New Character
=============================

There are many definitions and images you need to set up in order for a new character to work in the program. To ensure you don't miss any steps, this page outlines what the necessary definitions and images are.

Any tasks prefaced with **(Optional)** are optional. Read the description to determine if you want this feature for your new character.

Items prefaced with **(May be required)** are dependent on whether or not you have previously implemented an **(Optional)** task. For example, if you have added a character to the ``character_list`` variable, you **must** define a phone contact image, but if the character is not in ``character_list`` then they won't need this image.

.. |check| raw:: html

    <input checked=""  type="checkbox">


.. |uncheck| raw:: html

    <input type="checkbox">


* |uncheck| Define a ChatCharacter object in ``character_definitions.rpy`` under the heading **Chatroom Characters**
    * This step is NOT required if this character will never appear in a chatroom
* |uncheck| **(Optional)** Add your character to the ``character_list`` in ``character_definitions.rpy`` if you want their profile to appear on the home screen and allow the player to call them.
* |uncheck| **(Optional)** Add your character to the ``heart_point_chars`` list in ``character_definitions.rpy`` if you want the player to see how many heart points they have earned with this character.
* |uncheck| **(May be required)** Define a ``greet`` image for your character. This is **required** if you have included the character in ``heart_point_chars`` (see above) AND/OR if you want them to have greetings on the main menu.
* |uncheck| Define a Character object in ``character_definitions.rpy`` under the heading **Story Mode**.
    * This step is NOT required if this character will never appear in a Story Mode section
* |uncheck| Either: **1)** in the definition for your Story Mode Character, include the ``voice_tag`` argument (``voice_tag="em_voice"`` where ``em`` is the character's file_id), OR **2)** add their ChatCharacter object to the ``novoice_chars`` list in ``character_definitions.rpy``.
* |uncheck| **(Optional)** Define a ``layeredimage`` for your character if you want to display their image during Story Mode (VN) sections.
* |uncheck| **(May be required)** Define a Story Mode timeline image for your character if you want to display a Story Mode associated with them on the timeline screen.
* |uncheck| Define a Character object in ``character_definitions.rpy`` under the heading **Phone Call Characters**.
    * This step is NOT required if this character will never appear in a phone call
* |uncheck| **(May be required)** Define a phone contact image for your new character. **Required** if you have added them to the ``character_list`` variable.
* |uncheck| **(Optional)** Define a CG album for your character. Requires a ``cg_label``, ``album_cover``, and two album variables (one persistent and one regular). Add the character's file_id to the ``all_albums`` list.
* |uncheck| **(Optional)** Add a spaceship thoughts image for your new character.
* |uncheck| **(Optional)** Add a day select image for your new character.
* |uncheck| **(Optional)** Add a Save & Load image for your new character.





Adding a New Character to Chatrooms
===================================

All characters that currently exist in the program are defined in [[INSERT LINK HERE]] ``character_definitions.rpy``. Open that file and scroll down to the header **Chatroom Characters**.

As mentioned, these examples will show how to add a character named Emma to the program. First, you need to give Emma a ChatCharacter object so she can speak in chatrooms. A definition for Emma might look like the following::

    default em = ChatCharacter(
        name="Emma",
        file_id="em",
        prof_pic="Profile Pics/Emma/emma1.webp",
        participant_pic="Profile Pics/em_chat.webp",
        heart_color="#F995F1",
        cover_pic="Cover Photos/emma_cover.png",
        status="Emma's Status",
        bubble_color="#FFDDFC",
        glow_color="#D856CD",
        homepage_pic="Profile Pics/main_profile_emma.webp",
        phone_char=em_phone,
        vn_char=em_vn
    )

Usually the actual variable name -- in this case, ``em`` -- is short. It is recommended that this be two characters long; usually the first two letters of the character's name. The program already uses ``ja``, ``ju``, ``m``, ``r``, ``ri``, ``s``, ``sa``, ``u``, ``v``, ``y``, and ``z``.

.. warning::
    New ChatCharacter variables should be at least two characters long to avoid conflicts with engine code.

Each of those fields is explained below:

`name`
    A string. This is the name of the character as it should appear above their chatroom messages and in some other locations, like in a text message conversation with them.

    e.g. ``"Emma"``

`file_id`
    A string. This is used for many things internally to associate images and other variables with the character. For example, if a character's file_id is ``"em"``, then the program will look for incoming phone calls from this character with the suffix "_em" e.g. ``my_chatroom_incoming_em``. This is usually just the string version of what you called the ChatCharacter variable.

    e.g. ``"em"``

`prof_pic`
    The profile picture for this character. Usually it is a string with the file path of the image.

    .. tip::
        Profile pictures should be 110x110 pixels large. A larger version, up to 314x314 pixels, can also be provided with the same file name + "-b" (for 'big').

        e.g. If your profile picture is ``"ja-default.webp"``, then the program will look for a larger version with the filename ``"ja-default-b.webp"``.

    e.g. "Profile Pics/Emma/emma1.webp"

`participant_pic`
    The file path to the image that should be used on the timeline screen to indicate that the character was present in a chatroom.

    e.g. "Profile Pics/em_chat.webp"

`heart_color`
    A string containing hex colour code of the heart icon that appears when awarding the player a heart point for this character. It is not case-sensitive.

    e.g. "#F995F1"

The remaining fields are optional or semi-optional depending on where this character will appear and what other variables or images are defined.

The following two fields either must be given a colour, or you will need to place a special image file inside the game's ``images/Bubble`` folder to use as the background for the character's dialogue bubbles.

`bubble_color`
    Optional; however, if this is not defined **you must provide an image** in ``game/images/Bubble/`` called ``em-Bubble.webp`` if the character's file_id is ``em``.

    Otherwise, ``bubble_color`` should be a string containing a colour code. The character's regular speech bubble will have this colour as its background.

    e.g. "#FFDDFC"

`glow_color`
    Same as bubble_color, however, if ``glow_color`` is not provided the game will look for an image in ``game/images/Bubble/em-Glow.webp`` if the character's file_id is ``em``.

    e.g. "#D856CD"

If this character will appear on the home screen with a clickable profile, you should define the following fields:

`cover_pic`
    The file path to the image used for this character's cover photo on their profile screen.

    e.g. "Cover Photos/emma_cover.webp"

`status`
    A string containing the character's current status.

    e.g. "I ate a sandwich today."

`homepage_pic`
    The file path to the image that should be displayed on the home screen. The player clicks this image to view the character's profile. This should generally be a headshot of the character with a transparent background. If not given, the character's default profile picture will be used.

    e.g. "Profile Pics/main_profile_emma.webp"

If the character will appear in phone calls and/or story mode sections, you should define the following fields:

`phone_char`
    The Character object you defined for this character for phone calls.

    e.g. ``em_phone``

`vn_char`
    The Character object you defined for this character for Story Mode.

    e.g. ``em_vn``

Finally, ``ChatCharacter`` has some additional optional fields that are either currently unused or not necessary to set manually:

`voicemail`
    A string with the name of the label to jump to for this character's voicemail.

    e.g. "voicemail_1"

`right_msgr`
    False by default, but True if this character should appear on the right side of the messenger. Typically this variable is False for everyone but the main character.

`emote_list`
    A list of the "{image=...}" lines corresponding to all emojis associated with this character. Currently unused.

`pronunciation_help`
    A screen reader-friendly spelling of the character's name for use with self-voicing.

    e.g. ``pronunciation_help`` for 707 is ``"seven-oh-seven"``


Showing Your Character on the Home Screen
-----------------------------------------

Finally, beneath all the ChatCharacter definitions in ``character_definitions.rpy``, there are two lists. The first of these is

::

    default character_list = [ju, z, s, y, ja, v, m, r, ri]


If you want Emma to show up on the home screen with a clickable profile, or to appear as a contact in the player's phone contacts, you must add her to this list e.g.

::

    default character_list = [ju, z, s, y, ja, v, m, r, ri, em]

The second list is

::

    default heart_point_chars = [ c for c in character_list if not c.right_msgr ]

This list contains all the characters in ``character_list`` unless they have the property ``right_msgr``, which generally means it includes everyone in the ``character_list`` unless they are the MC. An equivalent definition would look like::

    default heart_point_chars = [ ju, z, s, y, ja, v, r, ri ]

Characters in ``heart_point_chars`` will appear on the player's Profile screen with an indicator of how many points the player has with them. If you want to add Emma to this list, then you need to define an image called ``greet em`` since ``em`` is Emma's file_id.

You can find the existing characters' images in ``variables_editable.rpy`` under the heading **GREETING IMAGES**. Greeting images are approximately 121x107 px up to 143x127px.

A greeting image for Emma might look like::

    image greet em = "Menu Screens/Main Menu/em_greeting.webp"

Beneath this image definition, you will also see the line::

    default no_greet_chars = [r, m]

If you won't be defining greeting messages for Emma to say on the main menu, then you should add her to this list as well::

    default no_greet_chars = [r, m, em]


When all is said and done, you should now be able to write dialogue for Emma inside chatrooms the way you would with the existing ChatCharacters::

    em "How are you?"
    msg em "It's a lovely morning~" glow






Adding a New Character to Story Mode
====================================

All characters that currently exist in the program are defined in ``character_definitions.rpy``. Open that file and scroll down to the header **Story Mode**.

To have Emma speak during story mode, she needs to have a Character object defined for her. A definition for that may look like the following::

    default em_vn = Character("Emma",
        kind=vn_character,
        who_color="#FFDDFC",
        image="emma",
        window_background="VN Mode/Chat Bubbles/vnmode_other.webp",
        voice_tag="em_voice"
    )

.. tip::
    If you've made a ChatCharacter object for your new character, it's a good idea to call this variable their file_id + "_vn".

The definition fields are explained below.

`name`
    This is the name of the character as it should appear in the dialogue box and history log during story mode.

    e.g. "Emma"

`kind`
    In order to simplify Character definitions, this field allows a Character object to "inherit" from an existing Character. In this case, using ``kind=vn_character`` sets up many of the properties that are consistent across all Characters for story mode.

    e.g. vn_character

`who_color`
    Optional. The colour of the character's name during story mode. By default, it is "#FFF5CA". The existing characters use the background colour of their chatroom speech bubbles as their ``who_color``.

    e.g. "#FFDDFC"

`image`
    Optional. Ren'Py will apply this tag to images if you include attribute tags during a character's dialogue (See [[INSERT LINK HERE]]).

    e.g. "emma"

`window_background`
    Optional. This is the image that will be shown behind the character's dialogue. By default, it is "VN Mode/Chat Bubbles/vnmode_other.webp". If you provide another image, it should be the same size as the default. Typically the borders are coloured differently for the various characters.

    e.g. "VN Mode/Chat Bubbles/vnmode_em.webp",

`voice_tag`
    Optional. If this character will speak in phone calls or during story mode, then this is the tag associated with them when they speak. Including this allows players to switch voice acting for this character on and off. This should be the character's file_id + "_voice". Otherwise, by default this character's voice will fall under the "other_voice" tag in the Sound preferences.

    e.g. "em_voice"


.. warning::
    If your new character does not have their own voice tag and should not include their own voice toggle in the Settings, then you must also include them in the special ``novoice_chars`` list found in ``character_definitions.rpy`` e.g.

    ::

        default novoice_chars = [u, sa, m, em]

    This will prevent the program from generating a voice toggle button for them.


Declaring a LayeredImage for a New Character
--------------------------------------------



