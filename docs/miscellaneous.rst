====================
Miscellaneous
====================

.. toctree::
    :caption: Navigation

    miscellaneous


Pronoun Integration
===================

Mysterious Messenger allows the player to change their pronouns and gender whenever they desire during the game. This means that any reference to the player's gender or use of pronouns to refer to the player must be taken care of via variables.

At the top of ``variables_editable.rpy`` you will see a function called ``set_pronouns`` and several existing variables defined under the header **PRONOUN VARIABLES**. These can be used in script::

    s "Aw, it doesn't look like [name] is logged in. I wonder what [they_re] doing?"

For a player with she/her pronouns, the final part of this dialogue will appear as "I wonder what she's doing?" whereas a player with they/them pronouns will see "I wonder what they're doing?"

It's important to remember that many verbs conjugate differently for "he/she" than for "they", which is why you should use the pronoun variables. Ren'Py's interpolation is very flexible; for example, you can negate the ``do_does`` variable like::

    ju "I think [name] said [they] [do_does]n't know if [they]'ll be free this weekend."

For a player with they/them pronouns, this displays as "I think [name] said they don't know if they'll be free this weekend", meanwhile, a player with he/him pronouns will see "I think [name] said he doesn't know if he'll be free this weekend." (Note: ``[name]`` is replaced with the player's name)

.. note::
    In Mysterious Messenger, players can pick their gender separately from their pronouns. This means, for example, that a player can identify as nonbinary and use she/her pronouns. You are welcome to extend this functionality as well to have the player further clarify how they want to be referred to.

    Note that because a player's pronouns will not necessarily directly correlate to their gender, it may be good to ask the player if they would like to be referred to as a woman, man, person, or something else, if that comes up in your writing. You can use input prompts to get more specific information from the player as well (see :ref:`Getting Input from the Player`).



Defining Additional Pronoun Variables
-------------------------------------

If you would like to define additional variables to help with scripting dialogue, you must define the variable in ``variables_editable.rpy`` under the **PRONOUN VARIABLES** header and also in the ``set_pronouns`` function.

For this example, a variable called ``go_goes`` will be defined for the three main pronoun options.

First, in ``variables_editable.rpy`` under the **PRONOUN VARIABLES** header, add

::

    default go_goes = "go"

Then in the ``set_pronouns()`` function under all the ``global`` declarations, add

::

    global go_goes

at the top of the function.

Next, under both ``if persistent.pronoun == "she/her"`` and ``elif persistent.pronoun == "he/him"`` add the line

::

    go_goes = "goes"

and under ``elif persistent.pronoun == "they/them"`` add

::

    go_goes = "go"

And you're done! To use your new variable in dialogue, you can type

::

    y "Yeah, [they] said [they] usually [go_goes] out on Fridays."

If the player has they/them pronouns, in-game this displays as "Yeah, they said they usually go out on Fridays", but a player with she/her pronouns will see "Yeah, she said she usually goes out on Fridays.".

Variables are capitalization-sensitive; if you need a capitalized version of a variable you can either create another variable (see ``They`` vs ``they`` for an example of this), or you can write the variable with ``[is_are!cl]`` to get the first letter capitalized (so, "Is" or "Are") or ``[is_are!u]`` to get the whole word in capitals (so "IS" or "ARE"). See https://www.renpy.org/doc/html/text.html#interpolating-data for more information on interpolation flags.

There is no limit to how many pronoun variables you can make, so feel free to create as many as you need to write your script more easily while supporting the different pronoun options.



Adding Additional Genders
--------------------------

Mysterious Messenger comes with three possible genders that the player can choose from on the profile page: nonbinary, female, and male. You are welcome to add more options to this list via the ``gender_options`` variable found in ``variables_editable.rpy``. The default list looks like so::

    define gender_options = ["nonbinary", "female", "male"]

The first item in the list is what will appear on the profile page when the player first starts the game. If you would like to add more options, simply add them to this list e.g.

::

    define gender_options = ["nonbinary", "female", "male", "agender", "genderfluid"]

If you ever want to change dialogue based on the player's gender, you can write statements like::

    if persistent.gender == "female":
        s "I'm sure Jaehee appreciates not being the only lady lol"
    elif persistent.gender == "male":
        s "It's nice to have a guy around here who understands my jokes lolol"
    # Can add more elif clauses in here as needed
    else:
        s "It's been so much fun having you here since Day 1, [name] ^^"


Using Gendered Terms
---------------------

Since the program allows players to choose their gender and pronouns, you may need to consider these factors when writing dialogue. The program has a built-in GenderedTerm class to help with this.

The class can be found in ``variables_editable.rpy`` and currently functions as follows:

* If the player has she/her pronouns *and* identifies as female, the "feminine" term will be used
* If the player has he/him pronouns *and* identifies as male, the "masculine" term will be used
* Otherwise, the neutral term is used

To use it, you can declare variables like so::

    default cutie = GenderedTerm("cute girl", "cute boy", "cutie")

in which the first argument ("cute girl") is the term that should be used for female players, the second argument ("cute boy") for male players, and the final argument for a neutral term. A similar use-case might be::

    default datefriend = GenderedTerm("girlfriend", "boyfriend", "datefriend")
    label day8_5():
        s "So... can I call u my [datefriend] lol"

The variable will update automatically based on the player's pronouns and gender without you needing to do anything else, so long as you set it up initially with ``default``.


Custom Emojis
=============

If you'd like to add your own emojis to the program, you need to define it as an image and add a few lines to the ``emoji_lookup`` dictionary found in ``emoji_definitions.rpy``. Emojis are saved as a series of frames, found in the ``images/Gifs/`` folder.

The bottom of ``emoji_definitions.rpy`` contains several image definitions which look like::

    image jaehee_angry:
        "Gifs/Jaehee/emo_jaehee_angry1.webp"
        0.5
        "Gifs/Jaehee/emo_jaehee_angry2.webp"
        0.5
        repeat

The name of this image is ``jaehee_angry``. It is made up of two separate images with a half-second pause between them. The first image is "Gifs/Jaehee/emo_jaehee_angry1.webp" and the second is "Gifs/Jaehee/emo_jaehee_angry2.webp". ``0.5`` tells the program to wait 0.5 seconds before showing the image on the next line. ``repeat`` lets the program know that it should loop indefinitely over these two images.

You're not limited to just two frames; for a smoother animation, something like::

    image my_new_emoji:
        "Gifs/Example/frame1.webp"
        0.25
        "Gifs/Example/frame2.webp"
        0.25
        "Gifs/Example/frame3.webp"
        0.3
        "Gifs/Example/frame4.webp"
        0.25
        repeat

will also work. This will cycle through frames 1-4 on repeat. Note that the time between each frame can be adjusted according to the animation's needs.

In order for the emoji to have an accompanying sound, you need to add it to the ``emoji_lookup`` dictionary near the top of the file. Assuming your image is named ``my_new_emoji`` as shown in the example definition above, you need to create an entry for your image like so::

    "{image=my_new_emoji}": "audio/sfx/Emotes/Example/some_audio_file.mp3"

``my_new_emoji`` is the name of your defined image, and ``audio/sfx/Emotes/Example/some_audio_file.mp3`` is the path to the audio file that should play when this emoji is shown.

If you're adding this to the end of the dictionary, ensure there is a comma after each entry before the last e.g.

::

        '{image=zen_shock}': 'audio/sfx/Emotes/Zen/zen_shock.mp3',
        '{image=zen_well}': 'audio/sfx/Emotes/Zen/zen_well.mp3',
        '{image=zen_wink}': 'audio/sfx/Emotes/Zen/zen_wink.mp3', # <- Comma

        "{image=my_new_emoji}": "audio/sfx/Emotes/Example/some_audio_file.mp3"
    }

Now when you want to show your new emoji in a chatroom or text message, you just need to type

::

    ja "{image=my_new_emoji}" (img=True)

and if you've added it to the emoji_lookup dictionary, the following will also work::

    msg ja "{image=my_new_emoji}"


.. note::
    You may also notice that there are a few variables defined under `emoji_lookup` such as `jaehee_emotes`; these are used in the chatroom generator. In a character's ChatCharacter declaration, you can include the `emote_list` parameter and set it to a list with the names of all their emojis. This is only relevant if you would like a character's emojis to appear in the chatroom creator; they will work in-game without requiring this list.



Spaceship Thoughts and Chip Prizes
==================================

Spaceship Thoughts
------------------

When the floating spaceship on the home screen isn't giving out chips, you can click it to view a random thought from one of the characters. You can find the initial list of thoughts in ``variables_editable.rpy`` under the header **SPACESHIP/CHIP BAG VARIABLES** in the variable ``space_thoughts``.

The variable ``space_thoughts`` can be modified here to change the spaceship thoughts the player sees upon starting the game. They can also be modified in any ``after_`` label during the game. You can have as many or as few ``SpaceThought`` objects in the list as you like -- even multiple thoughts for the same character. A ``SpaceThought`` only has two fields:

`char`
    The ChatCharacter object of the character whose thought this is. Used to find the background image for this thought.

    e.g. ja

`thought`
    A string with the thought this character is thinking.

    e.g. "I wonder if the cafe downstairs is open..."

To change spaceship thoughts during the game, in the ``after_`` label of a timeline item, use::

    $ space_thoughts.new_choices([
        SpaceThought(ja, "I wonder if the cafe downstairs is open..."),
        SpaceThought(ju, "The stripe on this sleeve is 3mm wider than the other stripes."),
        SpaceThought(s, "I think my body is made of PhD Pepper and Honey Buddha Chips."),
        SpaceThought(y, "Oh no, I'm going to be late for class again!"),
        SpaceThought(z, "Is there a typo in the script here?")
    ])

You can see an example of this in ``tutorial_6_meeting.rpy``. Using ``space_thoughts.new_choices`` will overwrite any of the previous thoughts in the list. If you would like to simply add a thought instead, you can use::

    $ space_thoughts.add_choices(
        SpaceThought(z, "Wish I could take a nap right now...")
    )

Or you can add multiple thoughts by using a list::

    $ space_thoughts.add_choices([
        SpaceThought(z, "Wish I could take a nap right now..."),
        SpaceThought(s, "Oh, a shooting star! How lucky~")
    ])

You can see an example of this in ``tutorial_0_introduction.rpy`` as part of a profile picture callback (see :ref:`Profile Picture Callbacks`).


Chip Prizes
-----------

Occasionally when finishing a timeline item, the chip bag on the home screen will give the player heart points and/or hourglasses. These heart points don't count toward any particular character. You can add to the list of possible prizes any time you like. The initial list of prizes is in ``variables_editable.rpy`` under the header **SPACESHIP/CHIP BAG VARIABLES** in the variable ``chip_prize_list``.

You can modify this variable so that the initial chip prizes are different upon starting the game, or modify the list in the ``after_`` label of any timeline item. You can have as many or as few prizes as you like.

Prizes are listed in something called a tuple with three items. The first is the text that should be shown when the player gets this prize e.g. "A clump of cat hair". The second and third items are numbers. The first number is the approximate amount of heart points the player should receive when they get this prize, and the second number is the number of hourglasses they should receive.

An example prize might look like::

    ("A clump of cat hair", 50, 1)

In this case, the prize message is "A clump of cat hair", and the player will receive approximately 50 heart points and exactly 1 hourglass.

The number of heart points is slightly randomized; the number will be within 10% of the value given, so the actual number of heart points the player will receive will be 45-55 in the above example. Hourglasses are not randomized in this way and the player will always receive the exact number of hourglasses specified.

You can add or replace prizes in the same way as Spaceship Thoughts. To replace all the current prizes with a new list of prizes, use the method ``new_choices`` e.g.

::

    $ chip_prize_list.new_choices([
        ("Trash. How unfortunate.", 25, 0),
        ("Leftover snacks Yoosung was eating.", 80, 0),
        ("A month's worth of rent!", 120, 2)
    ])

To add to the existing choices, use ``add_choices``::

    $ chip_prize_list.add_choices([
        ("Bubbly bubbles", 30, 0),
        ("Yoosung's bus is waiting for you!", 130, 1),
        ("A single potato chip", 75, 0)
    ])


Getting Input from the Player
===============================

In addition to choice menus, you can also prompt the player to enter text to get information such as nicknames, age, and other personalized information about the player, and then use this to shape the story later on. These input prompts work in many areas of the game, including chatrooms, story mode, text messages, and phone calls.

To show an input prompt to the player, you'll call the special label ``get_input``::

    get_input(the_var, prompt="", default="", length=20, allow=None,
        exclude=None, show_answer=None)

The parameters are explained below:

`the_var`
    A string corresponding to the name of a variable where the input will be saved to as a string. For example, if you want to save the player's name to a variable called ``nickname`` you might have a line like the following::

        $ nickname = ""
        call get_input('nickname', "Enter a nickname")

`prompt`
    Optional. If included, this text will appear above the input box to remind the player what information they're supposed to be entering. See the example above.

`default`
    Optional. A string that will automatically be filled into the input box as the "default" value, which the player can then delete and change if they wish. By default, this is the empty string "" (so, no text will be filled in automatically).

`length`
    By default, 20. An integer equal to the number of characters you will allow in the input box. Depending on where you are using the result, excessively long input values may not display correctly everywhere in the game.

`allow`
    A string containing all the letters, numbers, symbols etc that are permitted to be entered as input. By default, all characters accepted by the font are allowed (except for ``{}`` which can cause program issues). For example, you can use this to ensure you receive a number as input::

        msg u "How old are you?"
        $ player_age = "23"
        call get_input('player_age', "Enter your age", "23", allow="0123456789")
        if player_age == "":
            msg u "So you won't tell me, huh?"
            $ player_age = 0
        else:
            $ player_age = int(player_age)
            msg u "You're [player_age]?"

    The line ``$ player_age = int(player_age)`` ensures that the input, which is always a string, is then converted to an integer value which you can do math on if you so please.

    There is a pre-defined variable, ``allowed_alphabet``, which you can give to ``allow`` to only accept letters from the alphabet as well as spaces, dashes (-), and apostrophes e.g.

    ::

        msg z "Do you have any nicknames you want us to use?"
        $ nickname = ''
        menu (paraphrased=True):
            "I do have a nickname (enter nickname)":
                msg m "I do have a nickname." pv 0
                call get_input('nickname', "Enter a nickname", allow=allowed_alphabet)
                # This loops so long as the player leaves the input blank
                while not nickname:
                    z "Oh, so you don't have a nickname then?"
                    menu:
                        "No, I don't have a nickname.":
                            jump no_nickname
                        "Yes, I do. I want to input it again.":
                            pass
                    call get_input('nickname', "Enter a nickname", allow=allowed_alphabet)
                msg m "Call me [nickname]" pv 0
                z "[nickname], huh?"
                z "Sounds cute!"
            "I don't have a nickname." (paraphrased=False):
                z "That's fine!"


`exclude`
    Like allow, a string which contains all the letters, numbers, symbols etc which are *not* permitted to be entered as input.

`accept_blank`
    If True, the default, the prompt will accept the empty string ("") as input. If False, the player must enter at least one valid character for the Confirm button to be active.

`show_answer`
    By default, this is True during chatrooms and text messages and ignored during other times (such as phone calls and Story Mode). It will show the answer button at the bottom of the screen which, when clicked, will display the input prompt. If you set this to False, the input prompt will show up right away, without requiring the player to click to answer at the bottom of the screen.



Hacked Effects
===============

In your route, you may want to cause the program to appear as though it has been hacked. There are a few features to help you achieve this look. First, there is a variable called ``hacked_effect`` that, if set to ``True``, will cause the chatroom timeline to have additional "broken" backgrounds, and will also show a glitchy screen tear effect every 10 seconds or so. You can set this variable to ``True`` at any point during your route; simply including the line

::

    $ hacked_effect = True

in an ``after_`` label, for example, will activate it. Similarly, ``$ hacked_effect = False`` will get rid of these effects.

While you are testing a route, there is also an option to toggle the ``hacked_effect`` on/off in the **Developer** settings from the home screen.

.. warning::
    Many players may find the hacked effects distracting or irritating, so they should be used sparingly. There are also options in the Settings screen to turn off these effects, so know that not every player will be able to see or appreciate them.

The tear screen
---------------

There is a special screen called the ``tear`` screen which will cause the screen to be split into several smaller pieces that are offset a little from their original position. It's used to create the hacked effect in the chatroom timeline screen, but can also be shown in the middle of any ordinary chatroom/phone call/Story Mode/etc. You can call it like so::

    call show_tear_screen(num_pieces=25, xoffset_min=-10, xoffset_max=30,
                    idle_len_multiplier=0.4, move_len_multiplier=0.2,
                    w_timer=0.2, p=0.5)

The arguments are as follows:

`num_pieces`
    An integer. The number of horizontal slices the screen will be split up into. More pieces increase the distortion, but are also more resource-taxing. Typically it is good to keep this number under 50 or so for a full-screen image (like a screenshot, the default), and even less for images which are smaller. More pieces may take longer to render.

`xoffset_min`
    An integer. The minimum number of pixels the piece can be moved from its original starting position. Negative numbers move the piece to the left of its starting position.

`xoffset_max`
    An integer. The maximum number of pixels the piece can be moved from its original starting position. Positive numbers move the piece to the right of its starting position. This, along with ``xoffset_min``, are used to generate a random number for the xoffset of the torn piece.

`idle_len_multiplier`
    A float. A multiplier for how long the piece stays in an "idle" state (that is, it appears normally as opposed to being offset). Larger values mean the piece spends more time in its original position.

`move_len_multiplier`
    A float. A multiplier for how long the piece stays in its offset position. Larger values mean the piece spends more time away from its original position.

`w_timer`
    A float. How long the program should display the torn image for, in seconds, before it is automatically hidden. If this is not provided, the screen must be hidden manually.

`p`
    A float. The number of seconds the program should pause for after showing the torn screen. This is provided as an argument to the call so that it can be reproduced in replays. You should not write a pause after showing the torn screen.

The tear screen also takes an image argument and width and height arguments to size it.

`img`
    A displayable, usually the file path to an image or the name of a defined image. This is the image that will be torn into horizontal slices for the tearing effect, rather than a screenshot of the current screen.

`width`
    An integer. The width, in pixels, of the provided image above.

`height`
    An integer. The height, in pixels, of the provided image above.

If the ``img``, ``width``, and ``height`` arguments are given to ``show_tear_screen``, then instead of tearing the current screenshot into vertical slices, the provided image will be torn. It is displayed in the center of the screen. Otherwise, the rest of the arguments (``num_pieces``, etc) all apply identically to the provided image when tearing it.

You can also briefly show an image on-screen before showing the tear screen in order to have that image "torn" along with the rest of the screen. For this, you can use the special screen `display_img`::

    show screen display_img([ ['vn_party', 200, 400] ])
    pause 0.0001
    call show_tear_screen(40, 0.4, -100, 100, 0.2, 0.3, 0.3)
    hide screen display_img

The ``display_img`` screen will show an image in the specified position. It takes a lists of lists as its sole parameter. Each item in the list should be a list of three items: the image to display (which can be the name of a previously declared image, as above, a string with a path to the file name, or a Transform with the image, among other things), then the xpos, and then the ypos. So, in this case, the program displays the image ``'vn_party'`` at an xpos of 200 and a ypos of 400.

The short pause after showing the ``display_img`` screen gives the program enough time to register the images before it takes a screenshot for the tear screen. Call the tear screen as normal. Be sure to hide the `display_img` screen at the end.

.. note::
    Prior to v3.3.0, a different label and screen were used to tear the screen into pieces. This label, ``tear_screen``, still exists in the program and can be used with its original arguments (aka you don't have to update it to work on 3.3.0). However, for new torn screen sections, you should use the new label call and arguments as described above.

    The argument names have also been changed for the new label, but remain unchanged for the old method. ``number`` is now ``num_pieces``, ``offsetMin``/``offsetMax`` is now ``xoffset_min``/``xoffset_max``, ``offtimeMult``/``ontimeMult`` is now ``idle_len_multiplier``/``move_len_multiplier``. ``w_timer`` and ``p`` remain unchanged.

The hack_rectangle screen
-------------------------

The ``hack_rectangle`` screen will also help create a "hacked" effect. It will show several random rectangles on the screen, and works well when paired with the tear screen. For example::

    call hack_rectangle_screen(t=0.2, p=0.01)
    call tear_screen(number=10, offtimeMult=0.4, ontimeMult=0.2,
        offsetMin=-10, offsetMax=30, w_timer=0.18, p=0.18)

This will show the ``hack_rectangle`` screen for 0.2 seconds (``t=0.2``), and after pausing for 0.01 seconds (``p=0.01``) to give the program time to register the images on-screen, it shows the `tear` screen for 0.18 seconds.

Static white squares
--------------------

The program also has a screen called ``white_squares`` which randomly shows a sequence of white "static" squares on top of the screen. It is used for the chatroom select screen when ``hacked_effect`` is True. To call it, use

::

    call white_square_screen(t=0.16, p=0.17)

where ``t=0.16`` is how long to show the screen for (0.16 seconds) and ``p=0.17`` tells the program how long to pause for before continuing (0.17 seconds).

Inverting the screen colours
----------------------------

Finally, there is also a screen called ``invert`` which will take a screenshot of the currently displayed screen and invert the colours::

    call invert_screen(t=0.19, p=0.2)

where ``t=0.19`` is how long to show the screen for (0.19 seconds) and ``p=0.2`` is how long the program should pause for before continuing (0.2 seconds). This works well with screens that were previously mentioned. For example::

    call hack_rectangle_screen(t=0.2, p=0.01)
    call invert_screen(t=0.19, p=0.01)
    call tear_screen(number=10, offtimeMult=0.4, ontimeMult=0.2,
                offsetMin=-10, offsetMax=30, w_timer=0.18, p=0.01)
    call white_square_screen(t=0.16, p=0.17)

Removing Messages from the Chatlog
===================================

Besides just adding "hacked" effects, above, you may also want to remove entries from the chatlog for dramatic effect. This should typically be used sparingly, as it may be jarring for the reader.

Here is an example from ``tutorial_7_hacking.rpy``::

    menu:
        "I don't want to freak them out exactly...":
            sa "You don't, hmm?"
            sa "Just you wait a moment"
            m "Show me what to do."
            # This deletes the last three items in the chatlog, discounting
            # the most recent message.
            # You might have to experiment with how many messages to
            # delete/where to put the delete line since the program sometimes
            # has "hidden" chatlog entries that aren't shown to the user
            # In general you can put it one message after the last message
            # you want to delete
            call remove_entries(num=4)

In this case, the automatic message posted by the player ("I don't want to freak them out exactly..."), as well as Saeran's next two lines ("You don't, hmm?" / "Just you wait a moment") get removed from the chatlog via the line ``call remove_entries(num=4)``. As can be seen in this case, this number isn't always precisely the number of message you want to remove, as there are some internal calculations that take place when removing messages. Typically you would put ``call remove_entries`` *after* the first message which you want to remain on-screen due to the order in which messages are posted.

You may need to experiment with the placement of this line + the number of messages to delete until you get the desired result.

Adding New Audio
=================

In order to support audio captions, defining new music and sound effects to play in the program requires a few extra steps.

Defining New Music
------------------

All music currently in the game is defined in ``variables_music_sound.rpy``. Open that file and you will see several statements for the existing background music.

For this example, a song called "Jingle Bells" will be added.

First, define a variable that leads to the audio file::

    define jingle_bells = "audio/music/jingle_bells.ogg"

Next, in the ``music_dictionary`` variable, add ``jingle_bells`` to the end like so::

    define music_dictionary = {
        # (Complete definition omitted)
        april_mystic_chat : "Upbeat 8-bit music",
        april_mysterious_clues : "Sinister 8-bit music",
        april_dark_secret : "Suspenseful 8-bit music",

        jingle_bells : "Jolly Christmas music"
    }

This should be a pair of the name of your music variable (``jingle_bells``) and the description as will be displayed in an audio caption. Try to keep the description short while still conveying the general mood/feel of the song.

You can now play your music in-game via::

    play music jingle_bells



Defining New Sound Effects
--------------------------

All sound effects currently in the game is defined in ``variables_music_sound.rpy``. Open that file and you will see several statements for the existing background music.

For this example, a sound effect called "glass_breaking" will be added.

First, define a variable that leads to the audio file::

    define glass_breaking_sfx = "audio/sfx/glass_breaking.ogg"

Next, in the ``sfx_dictionary`` variable, add ``glass_breaking_sfx`` to the end like so::

    define sfx_dictionary = {
        car_moving_sfx : "Sound of a car moving",
        door_knock_sfx : "A knock at the door",
        door_open_sfx : "The door opens",
        glass_breaking_sfx : "A glass shatters"
    }

This should be a pair of the name of your sound effect (``glass_breaking_sfx``) and the description as will be displayed in an audio caption. The description should briefly describe the action or event the sound effect is meant to convey.

You can now play your sound effect in-game via::

    play sound glass_breaking_sfx


Adding New Ringtones, Text Tones, & Email Tones
---------------------------------------------------

In ``variables_music_sound.rpy`` under the header **RINGTONES** are three variables, one for email tones, text tones, and ringtones. The method of adding a new tone is the same for each, so only adding a new text tone is described below.

First, you need to add a new category to the corresponding tone variable. In this case, ``text_tones``. Categories are handled with a special class called ``ToneCategory``, which takes the following arguments:

`category`
    The name of the category as it should appear in the tone list.

    e.g. "Bonus"

`folder`
    The folder and/or prefix that should be prepended to the start of each tone name in this category.

    e.g. "audio/ringtones/" or "audio/ringtones/bonus_"

`ext`
    The extension of each file in this category.

    e.g. "ogg" or "wav"

`condition`
    Optional. If used, this should be given at the end of the definition. A string which evaluates to a condition that determines if this category of tones should be shown to the player. Can be used to unlock bonus ringtones etc after the player has reached the ending of a route, for example.

    e.g. condition="persistent.ray_good_end"

A typical ToneCategory definition looks like the following::

    ToneCategory("Bonus", "audio/sfx/Ringtones etc/text_tone_bonus_", "wav",
        "Bonus Unknown", "unknown",
        "Bonus V", "v",
        "Bonus Rika", "ri",
        condition="name == 'Rainbow'")

First, the category's title is given as "Bonus". The second argument, "audio/sfx/Ringtones etc/text_tone_bonus_" is combined with the next argument, "wav", to create a file name for each of the tones in this category.

After "wav", each of the following arguments comes in a pair -- first, the title of the tone, and second, the name of the tone as combined with the folder and ext arguments to construct a file path to the audio file. So for the above example, the first tone is called "Bonus Unknown", and its sound file is found at "audio/sfx/Ringtones etc/text_tone_bonus_unknown.wav". The last file in this category is called "Bonus Rika" and its associated sound file is "audio/sfx/Ringtones etc/text_tone_bonus_ri.wav".

Finally, there is the special argument ``condition``. By default, a ToneCategory is automatically shown to the player. However, you can also add a condition after all the tone definitions. This condition will determine whether the tone is shown to a player.

For the above example, the condition is ``condition="name == 'Rainbow'"``. Note that the condition *must* be a string. When evaluating whether this category should be available, the program will take apart the string and evaluate it. In this case, it will evaluate ``name == 'Rainbow'``. Therefore, if the player currently has their name set to "Rainbow" when they check the text tones list, they will see the "Bonus" tone category.

You can permanently unlock tones for the player using persistent variables in a similar method to the one described in :ref:`Unlockable Routes`. For example, if you want to unlock the bonus text tones after the player has seen the good end of Tutorial Day, you could create a variable called ``persistent.tutorial_good_end_complete`` which you set to True at the end of the Good End on Tutorial Day. Your condition for the ToneCategory would then be::

    ToneCategory("Bonus", "audio/sfx/Ringtones etc/text_tone_bonus_", "wav",
        "Bonus Unknown", "unknown",
        "Bonus V", "v",
        "Bonus Rika", "ri",
        condition="persistent.tutorial_good_end_complete")

Overall, the ``text_tones`` variable might look like the following if you were to add a Bonus category::

    define text_tones = [
        ToneCategory("Basic", "audio/sfx/Ringtones etc/text_basic_", "wav",
            "Default", "1",
            'Jumin Han', "ju",
            'Jaehee Kang', "ja",
            '707', "s",
            'Yoosung★', "y",
            'ZEN', "z"),
        ToneCategory("Bonus", "audio/sfx/Ringtones etc/text_tone_bonus_", "wav",
            "Bonus Unknown", "unknown",
            "Bonus V", "v",
            "Bonus Rika", "ri",
            condition="persistent.tutorial_good_end_complete")
    ]

You can add as many tones and categories as you like. The ``condition`` field is always optional; if omitted, that category will always be available.


Bonus Profile Pictures
=======================

Profile Pictures for the Characters
------------------------------------

In this program, the player can change the other characters' profile pictures on that character's profile screen by clicking their current profile picture. In-game, this is treated as a "bonus" profile picture and does not affect dialogue. The bonus profile picture is applied "on top of" the existing profile picture that is set by the game during the story. To return to the intended profile picture, there is a button captioned "Revert to default" which will restore the intended story profile picture.

By default, all the images in a character's corresponding "Profile Pics/" folder are available to choose as a profile picture, as are all the image in their corresponding CG album. This is set up on a per-character basis in ``variables_editable.rpy`` under the header **BONUS PROFILE PICTURES**.

If you want a new character to have bonus profile pictures, you must set up a variable for them in ``variables_editable.rpy``. For this example, the character Emma from :ref:`Adding a New Character to Chatrooms` will be given bonus profile pictures.

Because Emma's file_id is ``em``, the variable will be called ``em_unlockable_pfps``::

    define em_unlockable_pfps = combine_lists(
        register_pfp(folder="Profile Pics/Emma/", filter_out='-b.'),
        register_pfp(folder="CGs/em_album/", filter_keep='-thumb.')
    )

The functions used are explained below.

First, ``combine_lists`` is a special function which will combine all the given arguments into one large list, removing duplicates. It can take individual items or lists of items as arguments. For the most part, you should just make sure that you pass all your bonus profile pictures into this function as shown in the existing variable definitions.

The second and most important function is ``register_pfp``. This has many parameters which you may take advantage of that are explained below:

`files`
    Should be a string or a list of strings corresponding to file paths that lead to images you want to use for profile pictures. Can be used in combination with the ``folder`` parameter to prepend folder names to file names.

    e.g. ["em-1.webp", "em-2.webp"]

`condition`
    By default, this is 'seen', which means that the images passed to the function will become visible on the profile picture screen once the player has seen the image in-game (either as a CG or as another character's profile picture).

    Otherwise, the program expects a string that evaluates to a Python condition that determines when these images should be unlocked. For example, if you want the pictures to be unlocked after setting a particular variable, you could write ``condition="persistent.saw_casual_bad_end"``, for example. It is best to use persistent variables for conditions so they persist throughout different playthroughs.

    e.g. "persistent.seen_endings > 3"

`folder`
    A string with the folder path where the program should look for files. This is automatically prepended to each file name while searching.

    e.g. "Profile Pics/Emma/"

`ext`
    The extension for this file. Automatically appended to each file name when searching.

    e.g. "webp"

`filter_out`
    Requires the ``folder`` parameter. If included, searches through files in the given folder that do **not** contain the string in filter_out.

    e.g. "-b" (this will *exclude* images in the folder that contain the string "-b")

`filter_keep`
    Requires the ``folder`` parameter. If included, searches through images in the provided folder that **do** contain the string in filter_keep.

    e.g. "-thumb" (this will **only** include files if they include the string "-thumb")

These fields can be combined in many ways to intelligently create a filter which will add all your desired images to the character's profile picture list. For example, the current characters have two ``register_pfp`` statements::

    define ja_unlockable_pfps = combine_lists(
        register_pfp(folder="Profile Pics/Jaehee/", filter_out='-b.'),
        register_pfp(folder="CGs/ja_album/", filter_keep='-thumb.')
    )

The first statement looks in the provided folder ("Profile Pics/Jaehee/") and adds all images in that folder so long as they do not contain the string "-b.". This is because the "big" version of each profile picture is saved as something like "jae-1-b.webp", and since the large versions of the images are all duplicates of their smaller counterparts, they don't need to be included in the unlockable profile pictures.

The second statement looks in the folder "CGs/ja_album/" and only adds images if they have the string "-thumb." in them. Since this is a folder that holds the CGs for Jaehee, the full-size CGs shouldn't be added. The square thumbnails for the CGs are always called something like "cg-1-thumb.webp", so the program should only keep images that have the "-thumb." string in their file path.

Other valid uses of the ``register_pfp`` statement might look like::

    register_pfp(files=["em-1", "em-2", "em-3"], folder="Profile Pics/Emma/",
        ext="webp")

This will include the images "Profile Pics/Emma/em-1.webp" up to "Profile Pics/Emma/em-3.webp".

::

    register_pfp(files="Profile Pics/Bonus/em-bonus.webp",
        condition="persistent.saw_emma_end")

This will include the image "Profile Pics/Bonus/em-bonus.webp", which will be unlocked when the variable ``persistent.saw_emma_end`` is True (you are in charge of setting this variable yourself).

Finally, there is also a variable in ``variables_editable.rpy`` under the **BONUS PROFILE PICTURES** header called ``pfp_cost``; this is the number of heart points the player must earn with a character in order to unlock a profile picture with the "seen" condition. All other conditions unlock automatically once their condition is fulfilled.

Profile Pictures for the Player
--------------------------------

Whenever the player sees a new CG in-game or a character changes their profile picture, that image is automatically unlocked for the player to use as their own profile picture. Each profile picture requires the player spend 1 hourglass to unlock it.

.. note::
    For testing, if **Testing Mode** is turned on in the Developer Settings, than all profile pictures (for the MC and the NPCs) don't cost heart points or hourglasses.

Unlike bonus profile pictures for the other characters, the player's own profile picture can be commented on in-game and is treated as their current profile picture (see :ref:`Profile Picture Callbacks`). Bonus profile pictures remain unlocked across all playthroughs.

The initial set of images available to the player are all the images in the ``Drop Your Profile Picture Here`` folder. If you would like to add new options for a player who is beginning a certain route, then you can use the special ``add_mc_pfp`` function::

    $ add_mc_pfp("Profile Pics/MC/mc_bonus_1.webp")

This will add the image "Profile Pics/MC/mc_bonus_1.webp" to the set of profile pictures available to the player, so that the player can unlock it on the profile pictures screen with an hourglass. This function also takes a list of images as its first parameter e.g.

::

    $ add_mc_pfp([
        "Profile Pics/MC/mc_bonus_1.webp",
        "Profile Pics/MC/mc_bonus_2.webp",
        "Profile Pics/MC/mc_bonus_3.webp"
    ])

If you would like the images to be added already unlocked, there is a parameter ``unlocked`` you can set to True::

    $ add_mc_pfp([
        "Profile Pics/MC/mc_bonus_1.webp",
        "Profile Pics/MC/mc_bonus_2.webp",
        "Profile Pics/MC/mc_bonus_3.webp"
    ], unlocked=True)

You can use this in combination with the ``register_pfp`` function as well to filter out file names from folders; however, the ``condition`` field will be ignored.

::

    $ add_mc_pfp(register_pfp(folder="Profile Pics/MC Bonus/",
        filter_out='-b.'), unlocked=True)

This will add all the images in the "Profile Pics/MC Bonus/" folder without the string "-b." in the file name to the list of available profile pictures, and the images will come already unlocked.



Profile Picture Callbacks
==========================

.. note::
    Example files to look at:

    * tutorial_0_introduction.rpy
    * variables_editable.rpy


    *A brief overview of the steps required (more detail below):*

    #. Create a Python function in an ``init -1 python:`` block which takes four parameters -- the time difference, previous profile picture, current profile picture, and character associated with the current profile picture.
    #. Set the variable ``mc_pfp_callback`` to the name of your function.
    #. Write some conditionals inside your callback function to determine which label the program should jump to if the player sets their profile picture to a given image.
    #. Create a label for the callback. You can have characters call the player, send text messages, update their status, etc.


If the player changes their profile picture, a special "callback" function is called that allows the characters to comment on their profile picture. This callback function can be different for different routes, and may also be changed in the middle of a route, if desired.

To create a callback function, you must first put it inside an ``init -1 python:`` block. There are two examples of callback functions in the game -- the first is in ``variables_editable.rpy`` called ``bonus_pfp_dialogue``, and the second is the callback that is active during Tutorial Day, called ``tutorial_pfp_dialogue``.

A callback function is given four parameters -- the time difference since the callback was last called, the player's previous profile picture, their current profile picture, and the ChatCharacter the profile picture is associated with (e.g. if it belongs in a particular character's CG album or they used it as a profile picture). A typical profile picture callback function may look like the following::

    init -1 python:
        def casual_route_pfp(time_diff, prev_pic, current_pic, who):

While you can call these parameters anything you like, they will be explained with the names given above.

`time_diff`
    A MyTimeDelta object. This is the difference between the time the player last changed their profile picture and the current time. This can be helpful to prevent the player from constantly changing their profile picture just to see dialogue -- at the beginning of your profile picture callback, for example, you can include a conditional statement that will automatically return if less than 30 minutes have passed since the player last changed their profile picture.

    A ``MyTimeDelta`` object has several useful fields you can access to compare the time the player last changed their profile picture at. Each field is rounded **down** to the nearest whole number; so, if 2 minutes and 45 seconds (2.75 minutes) have passed since the player last changed their profile picture, ``time_diff.minutes`` will be equal to 2 and ``time_diff.seconds`` will be equal to 165.

    The available fields are ``days``, ``hours``, ``minutes``, and ``seconds``.

`prev_pic`
    The file path of the image that was used as the profile picture before the new one. This will never be the same as ``current_pic``; if they are the same, then the profile picture callback will not be called.

`current_pic`
    The file path to the image the player just set as their profile picture. This, like ``prev_pic``, may also be a string with a colour e.g. "#000".

`who`
    The ChatCharacter object of the character this image is associated with. This is determined by checking if the image is in a particular character's ``unlockable_pfps`` variable (see :ref:`Profile Pictures for the Characters`). If the image is not in any character's unlockable profile pictures set, then it will be equal to None.

    This can be useful if you want a character to react generally to any image associated with themselves.


You can use all or none of the passed parameters in your callback function. The callback function must either return ``None`` (either directly, via ``return None`` or ``return``, or implicitly by reaching the end of the function) or return a string or list of strings that correspond to a label the program can call for this profile picture callback.

If the profile picture callback returns a string corresponding to the name of a label, the program will check if it has already jumped to this particular label. If so, then the player has already seen this callback and the program will do nothing. Otherwise, the program will execute the contents of the label before returning to the regular game context. This means that the contents of the label should **not** be real-time -- e.g. you can't include a phone call directly in the callback label, but you **can** add a new phone call to the list of available calls, which will then jump to a label with the contents of that phone call.

You can also return a list of label names, in which case the program will check the list until it either finds a label which hasn't yet been executed or reaches the end of the list.

.. note::
    If **Testing Mode** is turned on from the developer settings, profile picture callbacks can execute more than once. Otherwise, they will only activate once on any given playthrough.


Profile picture callbacks should typically be treated the same way as an ``after_`` label is, and can include the same sorts of functions. Some examples of things that you can do in a profile picture callback label are:

* Have a character send the player a text message

    * You can include a label that will be jumped to to allow the player to reply and/or continue the conversation

* Change a character's status, profile picture, or cover photo
* Add a new spaceship thought
* Have a character call the player, or make a new phone call available for them
* Unlock bonus ringtones or profile pictures

Convenience functions and CDSs are provided to do the most common actions, but the true limit is your own programming ability. You could even use profile picture callbacks to branch the story, add new chatrooms to a route, or show a popup, for example.


Common Profile Picture Callback Examples
-----------------------------------------

The following examples will include conditional statements that will go inside a profile picture callback function -- while this function can be called anything, for the purposes of these examples assume the callback is set up like so::

    default mc_pfp_callback = example_pfp_callback

    init -1 python:
        def example_pfp_callback(time_diff, prev_pic, current_pic, who):

You can assume that unless otherwise specified, the example code should be inside the profile picture callback function.

Checking the Last Time the Picture was Changed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    if time_diff.minutes < 30:
        # It has been less than 30 minutes since the player changed their
        # profile picture, so don't execute a callback.
        return

::

    init -1 python:
        def example_pfp_callback(time_diff, prev_pic, current_pic, who):
            if time_diff.seconds < 60:
                # It has been less than a minute since the player changed their pfp
                return 'quickly_changing_pfp'

    # Outside of the main function
    label quickly_changing_pfp:
        compose text s:
            s "Wow I thought you just changed your profile picture lol"
        return

::

    init -1 python:
        def example_pfp_callback(time_diff, prev_pic, current_pic, who):
            if time_diff.days > 3:
                # It has been more than 3 days since the player changed their pfp
                return 'long_time_no_change'

    label long_time_no_change:
        $ space_thoughts.add_choices(
            SpaceThought(y, "[name] finally changed [their] profile picture! I was starting to feel self-conscious changing mine so much...")
        )
        return

Checking if an Image is Associated with a Character
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    if who == r:
        # Profile picture is associated with `r` (Ray)
        return ['ray_pfp_change_1', 'ray_pfp_change_2']

This means that the first time the player changes their profile picture to an image associated with Ray (``r``), the label ``label ray_pfp_change_1`` will execute. The second time the player does so, ``label ray_pfp_change_2`` will execute.


Checking For a Particular Image
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    if "CGs/ja_bonus_cg" in current_pic:
        return "ja_bonus_cg_dialogue"

You should use the ``if x in y`` terminology to check for particular images, and it is generally a good idea to leave out the file extension (e.g. .png or .webp) to ensure the correct image is matched. The above condition would be True if ``current_pic`` was "images/CGs/ja_bonus_cg.png" or "CGs/ja_bonus_cg.webp", for example.

The same should be done when comparing a string to the ``prev_pic`` variable e.g.

::

    if "Profile Pics/Ray/ray_03" in prev_pic and not who == r:
        return 'changed_ray_pfp'

This would cause ``label changed_ray_pfp`` to be executed the first time the player changes their profile picture from an image like "Profile Pics/Ray/ray_03.png" to a different image that isn't associated with Ray.


Paraphrased Choices
====================

Inside ``variables_editable.rpy`` is a variable called ``paraphrase_choices`` under the header **MISCELLANEOUS VARIABLES**. If this variable is set to True, choices are treated as "paraphrased" -- that is, it is your responsibility to write out exactly what you want the MC to say after a choice. This was the default behaviour prior to v3.0.

However, if ``paraphrase_choices`` is set to False, then the main character will automatically say the dialogue provided in a choice caption. This means that the following code is equivalent::

    $ paraphrase_choices = True
    menu:
        "I don't want to go.":
            m "I don't want to go." (pauseVal=0)
            ju "I understand."
        "I'll come with you.":
            msg m "I'll come with you." pv 0
            ju "That's good to hear."

    # Is equivalent to
    $ paraphrase_choices = False
    menu:
        "I don't want to go.":
            ju "I understand."
        "I'll come with you.":
            ju "That's good to hear."

In both cases, the main character (``m``) will say "I don't want to go." after the player chooses that option (same with "I'll come with you."). This feature works for all choices -- i.e. text messages, chatrooms, phone calls, and story mode.

You should set the value of ``paraphrase_choices`` at the beginning of a route, generally just after the ``new_route_setup`` function e.g.

::

    label new_year_prologue():

        $ new_route_setup(route=new_years_route, chatroom_label='new_year_prologue',
        participants=[ja])
        $ paraphrase_choices = False
        jump skip_intro_setup

After setting it, it is expected to remain that way the rest of the route. However, you can toggle it on/off on a per-menu or per-choice basis.

For example, if you have ``paraphrase_choices = False`` but want to have a menu include paraphrased choices, you can provide the menu argument ``paraphrased=True`` so that all the choices in that menu will be considered paraphrased::

    menu (paraphrased=True):
        "(Don't say anything)":
            ri "...I see."
        "(Try to reason with her)":
            m "Rika, really, you don't have to do this."

.. tip::
    Setting ``paraphrased`` for a menu will work with timed menus (see :ref:`Paraphrased Choices`) as well as regular menus.

You can also set the ``paraphrased`` argument for individual choices as well::

    menu (paraphrased=True):
        "(Don't say anything)":
            ri "...I see."
        "(Try to reason with her)":
            m "Rika, really, you don't have to do this."
        "You're better than this." (paraphrased=False):
            ri "Oh? What makes you think that?"

In this case, though the menu is treated as paraphrased (that is, the main character won't directly say the dialogue in the choices), the final choice *is not* paraphrased, so the main character will say "You're better than this" before Rika says "Oh? What makes you think that?".

Paraphrasing can be particularly useful for timed menus, which have limited space for choice text::

    timed menu:
        s "Ugh, so tired..."
        s "[name], help lol"
        s "I need something to do."
        s "Maybe Yoosung will come by."
        "(Sympathize)" (paraphrased=True):
            msg m "Right? It's been such a slow day." pv 0
            msg m "Sometimes u just wanna be lazy."
        "Get a hobby lol":
            s "Omg 0_0"
            s "ya maybe ur right lololol"

In this case, ``paraphrase_choices`` is set to False for the whole route, but in this menu the choice "(Sympathize)" is paraphrased.

Changing the Main Character
----------------------------

As non-paraphrased dialogue is automatically said by the main character, you may also want to change who the main character is. By default, it is ``m``, which uses the name and profile picture set by the player, but you can change it on a per-route basis or change the default definition in ``character_definitions.rpy``.

::

    default main_character = m

If you set this variable equal to a different character (e.g. ``em`` from the character examples), then ``em`` will say non-paraphrased choice dialogue instead of ``m``. ``em`` will also appear on the right side of the screen when saying dialogue in chatrooms or text messages.


Spending Hourglasses
==========================

If there's a part of your game where the player must use hourglasses to proceed, there is a special screen action to help with handling that transaction. It is called ``SpendHourglass``.

To use ``SpendHourglass``, pass in a message, the number of required hourglasses, and an action to execute if the player spends the required hourglasses.

For example, an action to unlock Deep Route might look like so::

    textbutton _("Deep Route"):
        action SpendHourglass("Would you like to unlock the deep story mode?",
                300, SetField(persistent, 'deep_story_unlocked', True))

In this example, we presume you are checking for whether deep story is unlocked via the variable ``persistent.deep_story_unlocked``, which begins as False. Thus, the message the player sees is "Would  you like to unlock the deep story mode?" and they are prompted to spend 300 hourglasses. If they spend the 300 hourglasses, then the action ``SetField(persistent, 'deep_story_unlocked', True)`` is run, which sets the variable ``persistent.deep_story_unlocked`` to True. Note that you can pass in a list of actions here too instead of just one action, if needed.

The SpendHourglass action takes care of the case where the player attempts to spend more hourglasses than they currently hold (e.g. they have 100 hourglasses but require 300 to unlock deep story mode). In this case, the provided action is not run and the player is simply shown a message saying they don't have enough hourglasses.

Achievements
===================

Mysterious Messenger provides an in-game achievement system which also integrates with existing Ren'Py systems, including Steam achievements. Several default achievements are included with the program which trigger when you complete various actions around the messenger and throughout Tutorial Day.

You will find most of the relevant code in ``achievements.rpy``. Here there is an ``achievement_popup`` screen, which is what will display a preview of the unlocked achievement in-game when the player earns it. It is passed one parameter, which I called ``a`` in the example screen, which corresponds to the Achievement object representing the achievement the player just earned.

There is also another screen, ``achievement_gallery``, which is what displays the achievements to the player. You are welcome to customize these in whatever way you like.

Setting Up Achievements
-----------------------

To set up an achievement, you will use the Achievement class. This takes several parameters:

`name`
    A string representing the name of this achievement, as it should appear in the popup and in the achievement screen.

`id`
    A string which does not include spaces, single or double quotes, or dashes (aka just use alphanumeric + underscores). This will be used as the ID for this achievement for backends such as Steam's backend.

`description`
    Optional. A string with the description for this achievement.

`unlocked_image`
    Optional. A displayable which is shown as an icon when this achievement is unlocked.

`locked_image`
    Optional. A displayable which is shown as an icon when this achievement is locked. By default this is set to the image ``locked_achievement``, which you can change.

`stat_max`
    Optional. If provided, it's an integer corresponding to the maximum progress of an achievement, if the achievement can be partially completed. For example, if your game has 24 chapters and you want this achievement to have a progress bar displaying the % of chapters the player has completed, you would set ``stat_max=24``. The achievement is unlocked when it reaches this value.

`stat_modulo`
    Optional. Only relevant if using the ``stat_max`` attribute. The formula ``(stat_progress % stat_modulo)`` is applied whenever achievement progress is updated. If the result of this calculation is 0, then the progress is shown to the user. By default this is 0, so all updates to ``stat_progress`` are shown.

    This is useful if, for example, for the earlier 24-chapter game progress stat, you only wanted to show updates every time the player got through a quarter of the chapters (0% full -> 25% full -> 50% full -> 75% full -> 100% full). In that case, the ``stat_modulo`` would be 6 (24/4).

`hidden`
    If True, then this achievement's title and description will be replaced with "???" until the player has unlocked it.

Thus, a few example achievements::

    ## An achievement which will unlock when the player starts a new game
    start_game = Achievement("Start of your journey", "start_game",
        "Start a new game", "achievements/new_game.webp")
    ## An achievement for getting to any bad end in the game
    bad_end = Achievement("Happily Never After", "bad_end",
        "Reach a bad end", "achievements/bad_end.webp")

Granting Achievements
---------------------

Now that you've set up the achievement, you will need to specify when it should be granted to the player. To do this, there are two different methods you can use.

The first method is to use ``my_achievement.grant()``, where ``my_achievement`` is the name of the Achievement object you declared earlier (in :ref:`Setting Up Achievements`). Note that you *do not need* to check if the achievement has already been granted before running this function; if the achievement has already been granted, this line will do nothing. It won't grant the achievement again, and the player won't see another popup for the achievement. This method is most useful for achievements earned during the script (where you can write ``$ my_achievement.grant()`` inside the label), or inside Python functions.

The second method is to use the convenience screen action ``my_achievement.Grant()``, which works the same way, but is intended to be used as a screen action. Thus, you can write buttons such as::

    textbutton _("Start") action [start_game.Grant(), Start()]

This will grant the ``start_game`` achievement to the player when they press the Start button to start a new game. As with before, ``Grant()`` will only grant the player the achievement once; if the player has already earned this achievement, they will not get it again and they won't see a popup about getting the achievement.

Checking if an Achievement was Granted
--------------------------------------

To check if the player has a particular achievement, use the ``has`` method, e.g.

::

    if good_ending_achievement.has():
        jump epilogue

This will return True if the achievement has been granted to the player, and False if it has not.

Tracking Achievement Progress
-----------------------------

For some achievements, you may want to track the player's progress towards completing them. There are two main ways of updating the player's progress, depending on whether you are doing so as a screen action or as part of the script.

Setting Progress
^^^^^^^^^^^^^^^^

The easiest way to update the progress value of an achievement is to use the ``progress`` method, or the ``Progress`` screen action method. This will allow you to *set* the current progress value of the achievement.

Note that, because this *sets* the progress value, it is best suited for achievements which are tracking things such as the number of chapters the player has played through in a linear game. For example, regardless of the previous value of the progress variable, it makes sense to write ``$ chapter_achievement.progress(12)`` when the player reaches Chapter 12 in your linear story. It is **not** suitable for achievements that are attempting to track cumulative progress across multiple different playthroughs or branching choice paths.

The ``Progress`` screen action method acts similarly, but is used as a screen action e.g.

::

    action chapter_achievement.Progress(12)

Remember that this will update the progress to the provided value regardless of when the player presses this button, so without further checks it's possible you could "reset" a player's achievement progress by using this method.

Updating Progress
^^^^^^^^^^^^^^^^^

If you would like to update the current progress value, you can use the ``add_progress`` method in script or Python, and the ``AddProgress`` screen action in screens. It takes one number, the amount of progress to add to the current progress stat.

::

    if not bad_end_achievement.has():
        $ bad_end_achievement.grant()
        $ ending_achievements.add_progress(1)

In this example, the achievement is for getting all of the game endings, which the player can achieve in any order. If the player reaches the bad end, it should only progress their progress towards achieving the ``ending_achievements`` achievement if they haven't seen the bad end before (otherwise we'd end up counting it twice, and it's possible they would be granted the achievement without actually seeing all the endings).

.. warning::

    It's incredibly important that you have a persistent check in place, either through persistent variables or through checking if another achievement has been granted, to ensure you are not "double-updating" an achievement's progress. The ``add_progress`` methods have *no way of knowing* if this progress has been added to the achievement in the past, so it is up to you the creator to ensure it is protected from adding progress more than once.

The second way uses a screen action. Like with the ``add_progress`` method, it is *very* important that you put checks in place to ensure you are not updating progress towards the achievement multiple times.

::

    textbutton _("Start"):
        action [
            If(not start_game.has(),
            [start_game.Grant(),
            all_achievements.AddProgress(1)]),
            Start()
        ]

This is an updated version of the Start button from before. Here, the game first checks if the player has achieved the ``start_game`` achievement before via ``start_game.has()``. If they have not, then it grants them that achievement and increases progress towards the ``all_achievements`` achievement by 1 (with the ``all_achievements`` achievement tracking how many achievements the player has gotten, total). After that, it runs the ``Start()`` action like normal.

Checking Progress
^^^^^^^^^^^^^^^^^

You can retrieve the current achievement progress via the ``get_progress`` method, e.g.

::

    if all_achievements.get_progress() >= 10:
        $ ten_achievements.grant() # Achievement for getting 10+ achievements

Resetting Achievement Progress
-------------------------------

You can reset an individual achievement's progress via the ``clear`` method, e.g.

::

    $ my_achievement.clear()

This is largely for testing purposes; to clear all achievement progress, you can use **Delete Persistent** from the Ren'Py launcher (as achievements are saved via persistent data).

Reserved Names
===============

Mysterious Messenger uses several variables, transforms, class names, and other features in order to work. As a result, you can run into errors if you accidentally use the same name as something already in the engine. If you're getting mysterious errors, you might try checking if you've accidentally replaced one of these reserved names.

Transform Names
---------------
* album_tilt
* alpha_dissolve
* cg_swipe_left
* cg_swipe_left2
* cg_swipe_left_hide
* cg_swipe_right
* cg_swipe_right2
* cg_swipe_right_hide
* chat_title_scroll
* chip_anim
* chip_wobble
* chip_wobble2
* choice_anim
* choice_disappear_hourglass
* cloud_shuffle1
* cloud_shuffle2
* cloud_shuffle3
* cloud_shuffle4
* cloud_shuffle5
* continue_appear_disappear
* continue_appear_disappear_first
* delayed_blink
* delayed_blink2
* dropdown_horizontal
* dropdown_menu
* fadein_out
* fade_in_out
* flash_yellow
* flicker
* guest_enter
* hacked_anim
* heart
* heartbreak
* hide_dissolve
* hourglass_anim
* hourglass_anim_2
* incoming_message
* incoming_message_bounce
* invisible
* invisible_bounce
* large_tap
* lightning_cloud_flash
* lock_spin
* med_tap
* moon_pan
* move_clouds
* new_fade
* notify_appear
* NullTransform
* null_anim
* participant_scroll
* reverse_topbottom_pan
* scale_vn_bg
* shake
* shooting_star
* shrink_away
* slide_in_out
* slide_up_down
* slide_up_down
* slow_fade
* slow_pan
* small_tap
* spaceship_chips
* spaceship_flight
* speed_msg
* stack_notify_appear
* star_fade_in
* star_place_randomly
* star_rotate
* star_twinkle_in
* star_twinkle_out
* star_twinkle_randomly
* text_footer_disappear
* toggle_btn_transform
* topbottom_pan
* topbottom_pan2
* tutorial_anim
* vn_center
* vn_farleft
* vn_farright
* vn_left
* vn_midleft
* vn_midright
* vn_right
* wait_fade
* yzoom_in


Variable Names
---------------

.. note::

    This list is not exhaustive! If you are running into an error you think may be caused by conflicting variable names, try searching for ``define var_name``, ``image var_name``, ``transform var_name``, ``default var_name``, or ``var_name =`` to see if you come across any unexpected matches.

* all_characters
* all_guests
* answer
* available_calls
* bubble_list
* call_countdown
* call_history
* character_list
* chat_pause
* current_call
* email_list
* example_guest
* filler
* fullsizeCG
* heart_point_chars
* incoming_call
* in_phone_call
* ja
* ju
* m
* main_character
* new_cg
* novoice_chars
* r
* rainbow2
* ri
* s
* sa
* special_msg
* u
* unseen_calls
* v
* va
* y
* z

