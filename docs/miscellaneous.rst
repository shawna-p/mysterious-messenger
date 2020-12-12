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

Variables are capitalization-sensitive; if you need a capitalized version of a variable you can either create another variable (see ``They`` vs ``they`` for an example of this), or you can write the variable with ``[is_are!c]`` to get the first letter capitalized (so, "Is" or "Are") or ``[is_are!u]`` to get the whole word in capitals (so "IS" or "ARE"). See https://www.renpy.org/doc/html/text.html#interpolating-data for more information on interpolation flags.

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




