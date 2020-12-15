====================
Miscellaneous
====================

.. toctree::
    :caption: Navigation

    miscellaneous


Pronoun Integration
===================

Mysterious Messenger allows the player to change their pronouns whenever they desire during the game. This means that any reference to the player's gender or use of pronouns to refer to the player must be taken care of via variables.

At the top of ``variables_editable.rpy`` you will see a function called ``set_pronouns`` and several existing variables defined under the header **PRONOUN VARIABLES**. These can be used in script::

    s "Aw, it doesn't look like [name] is logged in. I wonder what [they_re] doing?"

For a player with she/her pronouns, the final part of this dialogue will appear as "I wonder what she's doing?" whereas a player with they/them pronouns will see "I wonder what they're doing?"

It's important to remember that many verbs conjugate differently for "he/she" than for "they", which is why you should use the pronoun variables. Ren'Py's interpolation is very flexible; for example, you can negate the ``do_does`` variable like::

    ju "I think [name] said [they] [do_does]n't know if [they]'ll be free this weekend."

For a player with they/them pronouns, this displays as "I think [name] said they don't know if they'll be free this weekend", meanwhile, a player with he/him pronouns will see "I think [name] said he doesn't know if he'll be free this weekend." (Note: ``[name]`` is replaced with the player's name)

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
    You may also notice that there are a few variables defined under `emoji_lookup` such as `jaehee_emotes`; these are used in the chatroom generator, which is not yet fully implemented. You can ignore these variables for now.



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

You can see an example of this in ``tutorial_0_introduction.rpy`` as part of a profile picture callback (see [[INSERT LINK HERE]]).


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





Adding New Ringtones, Text Tones, & Email Tones
=================================================

In ``variables_editable.rpy`` under the header **RINGTONES** are three variables, one for email tones, text tones, and ringtones. The method of adding a new tone is the same for each, so only adding a new text tone is described below.

First, add a new entry to the corresponding dictionary. In this case, ``text_tone_dict``. Dictionary entries are a key-value pair, separated by a colon. In this case, the "key" is the name of the tone you want to show to the player, and the "value" is the path to the file with the correct sound effect. Note that no two entries can have the same key, so you should preface entries with a category title if you're adding multiple tones for the same character e.g.

::

    default text_tone_dict = {
        'ZEN': 'audio/sfx/Ringtones etc/text_basic_z.wav',
        'Bonus ZEN': 'audio/sfx/Ringtones etc/text_bonus_z.wav'
        'Christmas ZEN': 'audio/sfx/Ringtones etc/text_xmas_z.wav'
    }

Entries in the dictionary can be in any order; this dictionary is only used to find the correct sound file, and not to display possible tones to the player. That's taken care of next.

To display your new tone to the settings screen, you must add it to the appropriate "tone" list, found below the tone dictionaries. For this case, you need to add an entry to ``persistent.text_tone_list``.

.. tip::
    You don't have to add all your ringtones/email/text tones right at the start of the game. For example, just before ending a route, you could add a set of "bonus" ringtones to ``persistent.ringtone_list`` e.g.

    ::

        $ persistent.ringtone_list.append([
            "New Year's", ["Jumin Han NY", "Jaehee Kang NY", "707 NY",
                "Yoosung NY", "ZEN NY"]
        ])

Each tone list is made up of two separate parts - the category title and a list of the available tones in that category. The names of the tones