================
Chatrooms
================

.. toctree::
    :caption: Navigation

    chatrooms


Creating a Chatroom
===================

.. note::
    Example files to look at:

    * tutorial_5_coffee.rpy
    * tutorial_6_meeting.rpy

    *A brief overview of the steps required (more detail below):*

    #. Create a new ``.rpy`` file (Optional, but recommended)
    #. Create a new label for the chatroom.
    #. Set the background with ``scene morning`` where ``morning`` is replaced by whatever time of day/background you want to use.
    #. Add background music with ``play music mystic_chat`` where ``mystic_chat`` is replaced by the desired music variable.
    #. Write the chatroom dialogue.

        #. You may want to use either ``Script Generator.xlsx`` or the ``msg`` CDS.

    #. End the label with ``return``.

The first thing you should do when creating a new chatroom is create a new ``.rpy`` file and name it something descriptive so it's easy to find it again. For example, you might name it something like ``day_1_chatroom_3.rpy`` or ``day_1_3.rpy``. It's a good idea to put all the files related to a particular route inside a folder for organization.

In your newly created ``.rpy`` file, begin by making a label for the chatroom::

    label day_1_1:

Don't forget the colon after the label name. Your label name also can't have any spaces in it or begin with a number.

Next, it's time to set up the chatroom background. Note that everything under the label name **should be indented at least one level to the right**. You can look at the example files mentioned above if you're not sure what this means.

You need to give the chatroom a background to show::

    label day_1_1:
        scene morning

While chatrooms also use Ren'Py's ``scene`` statement to show backgrounds, there is a limited number of built-in backgrounds to use. New backgrounds must be defined as described in :ref:`Adding Chatroom Backgrounds`. Your background options are:

* morning
* noon
* evening
* night
* earlyMorn
* hack
* redhack
* redcrack

The background names **are** case-sensitive, so you need to get the capitalization correct. The program will automatically clear the chat history when beginning a new chatroom so new messages begin appearing at the bottom.

Now that the background is set up, you probably want some music. Music is played with the line::

    play music mystic_chat

where ``mystic_chat`` can be replaced by the name of whatever music you want. There are several files pre-defined in ``variables_music_sound.rpy``. If you want to define your own music, you need to add it to the ``music_dictionary`` as well so that it is compatible with audio captions. See :ref:`Adding New Audio` for more information.

Next, you'll write the dialogue for your chatroom. See :ref:`Writing Chatroom Dialogue`. Finally, to end the chatroom, end the label with ``return``::

    label day_1_1:
        scene earlyMorn
        play music mint_eye
        # Dialogue will go here
        return

To learn how to make this chatroom appear in your game, check out :ref:`Setting up a Route`.


Writing Chatroom Dialogue
=========================

There are two primary ways of writing dialogue for your chatroom. The first is to use the ``msg`` CDS, and the second is to use a special spreadsheet to help generate the dialogue for you.

Using the msg CDS
-----------------

The ``msg`` CDS helps add effects to your dialogue, such as special speech bubbles or alternative fonts, without sacrificing the readability of the dialogue. Dialogue written with the ``msg`` CDS looks like the following::

    msg r "Usually, the program would delay sending text messages and phone calls" sser1
    msg r "until after both this chatroom and the Story Mode were played." sser1
    msg r "But since v3.0, things are more flexible!" flower_m
    msg r "If you declare a route using the new format,"
    msg r "you can have text messages and phone calls and the like after any story item,"
    msg r "even a chatroom that has a Story Mode attached" glow

(Dialogue taken from ``tutorial_3_text_message.rpy``)

The ``msg`` CDS requires a speaker (in the example, ``r``) and some dialogue (surrounded by ``""``). There are several optional clauses that can be added after the dialogue to affect how it displays.

Fonts
^^^^^

The ``msg`` CDS has several built-in fonts that can be applied to the text. These are:

.. list-table::
    :widths: 15, 40
    :header-rows: 1

    * - **Short form**
      - **Description**
    * - sser1
      - Sans serif font 1 (Nanum Gothic)
    * - sser2
      - Sans serif font 2 (Seoul Namsan)
    * - ser1
      - Serif font 1 (Nanum Myeongjo)
    * - ser2
      - Serif font 2 (Seoul Hangang)
    * - curly
      - Cursive font (Sandoll Misaeng)
    * - blocky
      - Blocky font (BM-HANNA)

You can also use your own fonts with the ``msg`` CDS. See :ref:`Custom Fonts and Bubbles` for more on custom fonts and special bubbles.

In order to use one of the built-in fonts, just include the name of the desired font after the dialogue e.g.

::

    msg u "This is example dialogue in the cursive font." curly
    msg u "This is in the sans serif 1 font." sser1

Note that you can only have one font at a time; including more than one will simply use the last font given. The default font is ``sser1``, and dialogue will show up using ``sser1`` unless you give it a different font.

Emphasis
^^^^^^^^

You can emphasize text in several ways. To use the **bold** version of a font, use the argument ``bold`` after the dialogue e.g.

::

    msg u "This text is bolded." bold

Some fonts have **extra-bold** variants as well. These are defined in ``variables_editable.rpy`` in the variable ``bold_xbold_fonts_list``. To make a font extra bold, add the ``xbold`` clause after the dialogue e.g.

::

    msg ja "This text is in the sans serif 2 font, extra bold." sser2 xbold

Finally, you can increase the size of the text inside a speech bubble with the ``big`` argument e.g.

::

    msg ju "This text is shown at a bigger size." big

You can also combine ``big`` and ``bold`` or ``xbold`` for additional emphasis.

::

    msg s "VERY IMPORTANT MESSAGE!!" sser2 big xbold

Special Bubbles
^^^^^^^^^^^^^^^

You can also use special speech bubbles as the background of dialogue. There are several bubbles built in to the program:

.. list-table::
    :widths: 15, 12, 73
    :header-rows: 1

    * - **Base bubble**
      - **Sizes**
      - **Additional Notes**
    * - cloud
      - s, m, l
      -
    * - round
      - s, m, l
      - Only available for ``ja``, ``ju``, ``s``, ``v``, and ``y``. Using a ``round`` style for ``z`` or ``r`` will result in using the ``flower`` bubble.
    * - round2
      - s, m, l
      - Only available for ``s``
    * - sigh
      - s, m, l
      - Not available for ``sa``.
    * - spike
      - s, m, l
      - small (s) size only available for ``ja``, ``ju``, ``s``, ``y``, and ``z``.
    * - square
      - s, m, l
      - Not available for ``s``.
    * - square2
      - s, m, l
      - Only available for ``r``.
    * - flower
      - s, m, l
      - Only available for ``r`` and ``z``. Previously called ``round``.
    * - glow
      - N/A
      - Available for all pre-defined characters excluding ``m`` i.e. ``u`` and ``ri`` also have this bubble.
    * - glow2
      - N/A
      - Only available for ``sa``. An extra variant on the ``glow`` bubble.

Unless otherwise mentioned, ``u``, ``ri``, and ``m`` have no special bubble variants.

For bubbles which have sizes, you must include which size bubble you would like (``s`` for small, ``m`` for medium, and ``l`` for large) after the name of the bubble e.g. ``square_m`` or ``sigh_l``.

To use a special bubble, add the name of the bubble after dialogue e.g.

::

    msg r "This is a bubble with the flower background." flower_m
    msg r "And this is a bubble with the glowing background." glow
    msg r "These can be combined with other fonts and effects, too!" glow curly big


You can also use your own bubbles with the ``msg`` CDS, or modify it so that characters can use each other's special speech bubbles. See :ref:`Custom Fonts and Bubbles` for more on custom special bubbles and fonts.

Images
^^^^^^

The ``msg`` CDS will automatically detect if dialogue includes a recognized emoji and mark the dialogue as an image accordingly. If you want a character to post an image in the chatroom (such as a CG), then you can use the ``img`` argument::

    msg s "cg s_1" img
    msg s "I just posted a CG!"

You need to follow the rules outlined in :ref:`Defining a CG` and :ref:`Showing a CG in a Chatroom or Text Message` in order for the program to find the correct image and display it during a chatroom. For CGs, the program will also automatically unlock the image in the gallery.

For emojis, it's sufficient to write::

    msg s "{image=seven_wow}"

where ``seven_wow`` is the name of the emoji image to be shown. The program will automatically recognize it as an emoji.

Modifying Message Speed
^^^^^^^^^^^^^^^^^^^^^^^

Finally, you can also adjust the speed at which a message is posted. For example, if you want a character to post a bunch of messages in quick succession, you can use the ``pv`` clause to use a multiplier on the speed at which a message is posted e.g.

::

    msg s "These" pv 0.1
    msg s "messages" pv 0.1
    msg s "are" pv 0.1
    msg s "posted" pv 0.1
    msg s "quickly!!!" pv 0.1

If you have ``paraphrase_choices`` turned off, you will generally want to add ``pv 0`` after a message posted by the main character after a menu e.g.

::

    menu:
        "Emojis and Images":
            msg m "I want to learn how to use emojis and images." pv 0
            msg u "Emojis and images, huh?" ser1

Using the Chatroom Spreadsheet
------------------------------

The second way of writing chatroom dialogue is similar to writing regular Ren'Py script, but passes special keyword arguments in brackets after the dialogue. A spreadsheet, ``Script Generator.xlsx``, is included with the program to make this style of writing easier.

The first tab in the spreadsheet is called **Chatroom Instructions** and explains how the **CHATROOM TEMPLATE** tab is used. Where possible, the spreadsheet will try to check off the appropriate boxes depending on what fonts, emphasis, or bubbles you want to use. It will also notify you if you've typed a character's name incorrectly.

The tab **tutorial_6_meeting** has examples directly from the corresponding ``.rpy`` file of how dialogue for that chatroom was written using the spreadsheet.

In general, you should create a copy of the **CHATROOM TEMPLATE** tab and fill it out with your desired dialogue. Don't forget that messages such as ``707 has entered the chatroom`` are handled differently -- see :ref:`Advanced Chatroom Features` for more.

If you've filled out the spreadsheet correctly, you should be able to copy-paste the dialogue from the "What should be filled into the program" column into your script file.

Comparison of Chatroom Dialogue
-------------------------------

Both methods of writing dialogue can be mixed and matched freely in-game. For example, if you don't want to add any additional fonts, emphasis, or special bubbles, it can be easier to type out dialogue using just the character variable and their dialogue. Here is a comparison of what dialogue looks like for each method when various fonts, emphasis, and special bubbles are added::

    # msg CDS
    msg u "Extra bold sans serif 2 font" sser2 xbold
    # Spreadsheet dialogue
    u "{=sser2xb}Extra bold sans serif 2 font{/=sser2xb}"

    # msg CDS
    msg u "Glowing bubble with blocky font" blocky glow
    # Spreadsheet dialogue
    u "{=blocky}Glowing bubble with blocky font{/=blocky}" (bounce=True)

    # msg CDS
    msg z "Bold large curly font with flower bubble" curly bold big flower_m
    # Spreadsheet dialogue
    z "{=curly}{size=+10}{b}Bold large curly font with flower bubble{/b}{/size}{/=curly}" (bounce=True, specBubble="flower_m")

    # msg CDS
    msg s "{image=seven_wow}"
    # Spreadsheet dialogue
    s "{image=seven_wow}" (img=True)

    # msg CDS
    msg m "Dialogue with a speed modifier." pv 0
    # Spreadsheet dialogue
    m "Dialogue with a speed modifier." (pauseVal=0)

    # msg CDS
    msg s "cg s_1" img
    # Spreadsheet dialogue
    s "cg s_1" (img=True)

.. attention::
    If you have script from v2.x or earlier, you don't need to modify it to work with the ``msg`` CDS. You can mix and match script writing styles within the same chatroom.


Advanced Chatroom Features
==========================

Now that you've made a label for your chatroom and filled it with some dialogue, you may want to add additional polish to your chatroom, like allowing the player to make a choice or adding the special ``707 has entered the chatroom``-style messages.

Entering and Exiting the Chatroom
---------------------------------

To get the message ``Character has entered the chatroom``, use the ``enter chatroom`` CDS::

    enter chatroom s

where ``s`` is the variable of the character who is entering the chatroom. See :ref:`Creating Characters` for a list of the characters currently programmed into the game.

.. tip::
    You can also use ``call enter(s)`` to have a character enter the chatroom.

To get the message ``Character has left the chatroom``, use the ``exit chatroom`` CDS::

    exit chatroom s

where ``s`` is the variable of the character who is exiting the chatroom.

.. tip::
    You can also use ``call exit(s)`` to have a character leave the chatroom.


Clearing the Chat History
-------------------------

If you would like to clear the chat history so that all previous messages are erased, you can use the ``clear chat`` CDS::

    y "Anyway, I should go now."
    exit chatroom y
    clear chat
    scene hack
    show hack effect
    enter chatroom u
    u "Hi, [name]."

.. note::
    The chat history is automatically cleared before beginning a new chatroom.

Clearing Chatroom Participants
-------------------------------

If you would like to clear all current chatroom participants from the chatroom header, you can use the extra argument ``participants`` for the ``clear chat`` CDS::

    label my_chatroom:
        scene morning
        play music narcissistic_jazz
        enter chatroom z
        z "Has the chatroom been acting up for you too, [name]?"
        msg z "I've been having trouble with it all morning." sigh_s
        clear chat participants
        scene hack
        show hack effect
        enter chatroom u
        u "Ah, excellent."
        u "I've gained access to the messenger."

This will both clear the chat history and remove any existing participants from the list at the top of the messenger screen.

This isn't typically used outside of using story mode sections in the middle of chatrooms (see :ref:`Including a Story Mode During a Chatroom`) or linking together "separate" chatrooms as part of a scene for something like an After End.


Providing Choices
-----------------

During a chatroom, you may want to allow the player to make a choice. This can be accomplished with Ren'Py's built-in menu system::

    msg s "What kind of food do you eat?"
    menu:
        "I like soup.":
            msg s "You like soup?"
        "I eat a lot of junk food.":
            msg s "lolol same."
    msg s "But you should have a balanced diet, unlike me~" glow

Note that for this menu, it is assumed that ``paraphrase_choices`` is turned on for this route. This means that the main character will automatically say the exact dialogue on the chosen choice. If ``paraphrase_choices`` is turned off, the menu might look something like this::

    msg s "What kind of food do you eat?"
    menu:
        "I like soup.":
            msg m "I like soup." pv 0
            msg s "You like soup?"
        "I eat a lot of junk food.":
            msg m "I eat a lot of junk food." pv 0
            msg s "lolol same."
    msg s "But you should have a balanced diet, unlike me~" glow

You can also turn ``paraphrased`` on or off on a per-menu or per-choice basis. For more on paraphrasing, see :ref:`Paraphrased Choices`.

You can add as many choices as you want to the menu, though only 5 options will fit on the screen at once. All code indented after a choice will only be run if the player picks that choice. So, only a player who chose ``"I like soup"`` will see the line ``"You like soup?"``. Anything indented at the same level as the menu will be run regardless of the choice made, so the player will see the line ``"But you should have a balanced diet, unlike me~"`` regardless of whether they said they like soup or eat junk food.

.. warning::
    You can use the ``TAB`` key to indent your code an additional level to the right, but make sure your code editor is using spaces to indent code. Otherwise, you will get errors complaining about "tab" characters in your code.

You'll also notice in the "paraphrased" version of the menu, the main character (``m``) has the clauses ``pv 0`` after their dialogue. This tells the program to not wait at all before posting the MC's message. Usually the program will pause before posting a message to simulate "typing time", but you want the player's choice to appear right away after a choice, so you should include ``pv 0`` if you're using the ``msg`` CDS, or ``(pauseVal=0)`` if you're using the spreadsheet style.


Showing a Chatroom Banner
-------------------------

There are four special banners included in the program. The available banners are:

* lightning
* heart
* annoy
* well

You can show a banner with the code::

    show banner lightning

Note that while the order of ``banner`` and ``lightning`` don't matter, the name is case-sensitive. So, you could also use ``show lightning banner`` but ``show Lightning banner`` would not work.

.. note::
    These images are not displayed for players who have toggled the **Chatroom Banners** setting off.

Showing a Heart Icon
--------------------

Awarding a heart point
^^^^^^^^^^^^^^^^^^^^^^

To show a heart icon to the player and award them "heart points" associated with a particular character, use

::

    award heart s

where ``s`` is the variable of the character whose heart icon you'd like to show. The player will receive one heart point with that character when this code is run. See :ref:`Creating Characters` for a list of the characters built-in to the program and how to add your own character.

.. note::
    Ray (``r``) and Saeran (``sa``) share heart points. So, if you award a heart point for Saeran via ``award heart sa``, Ray will also receive 1 heart point.

There is also a second optional argument to ``award heart``::

    award heart ju bad

``bad`` tells the program that this heart is a "bad" heart point, and should count towards a bad ending. In-game, a ``bad`` heart appears the same as a normal heart point. You can use this method to count the number of choices a player makes that would lead towards a bad ending, and then check whether the player made more "good" or "bad" ending choices when they reach a plot branch. See :ref:`Plot Branches` for more information on this.

Removing a heart point
^^^^^^^^^^^^^^^^^^^^^^

If the player makes a choice a character doesn't like, you can cause them to lose a point with a character by showing a "heart break" icon.

::

    break heart ju

where ``ju`` is the variable of the character whose heart break you'd like to show. This will **always** subtract points from the character's "good" heart points and never the "bad" points. Note that losing heart points in this way does not subtract from the heart point totals the player uses to unlock additional profile pictures for a character (See :ref:`Bonus Profile Pictures`).

.. tip::
    Both ``break heart ju`` and ``heart break ju`` will show the heart break animation for the character ``ju``. You can't switch the word order for ``award heart`` though!

Showing the Hacked Scroll Effect
---------------------------------

To show the scrolling "hack" effect during a chatroom, use the line

::

    show hack effect

or alternatively,

::

    show redhack effect

for the red version of the scrolling hack image.

.. note::
    These effects are not displayed for players who have toggled the **Hacking Effects** setting off.

Shaking the Screen
-------------------

To shake the screen, use the line

::

    show shake

Screen shake is compatible both with regular backgrounds and with the animated backgrounds.

.. note::
    This effect is not displayed for players who have toggled the **Screen Shake** setting off.

Custom Fonts and Bubbles
=========================

Mysterious Messenger supports user-defined fonts and special bubbles through customizable variables and functions. These work with the ``msg`` CDS as well as the text tag approach used for the spreadsheet dialogue.

Custom Fonts
-------------

To add your own font to the game, first you need to add it to the ``all_fonts_list`` found in ``variables_editable.rpy``::

    define all_fonts_list = ['sser1', 'sser2', 'ser1', 'ser2', 'curly', 'blocky']

In general you should **not** replace this list; just add your new font to the end. For this example, a font called "cursive" will be added.

::

    define all_fonts_list = ['sser1', 'sser2', 'ser1', 'ser2',
        'curly', 'blocky', 'cursive']

Now you need to add it to the ``font_dict``::

    define font_dict = { 'curly' : gui.curly_font, 'ser1' : gui.serif_1,
            'ser1b' : gui.serif_1b, 'ser1xb' : gui.serif_1xb,
            'ser2' : gui.serif_2, 'ser2b' : gui.serif_2b,
            'ser2xb' : gui.serif_2xb, 'sser1' : gui.sans_serif_1,
            'sser1b' : gui.sans_serif_1b, 'sser1xb' : gui.sans_serif_1xb,
            'sser2' : gui.sans_serif_2, 'sser2b' : gui.sans_serif_2b,
            'sser2xb' : gui.sans_serif_2xb, 'blocky' : gui.blocky_font,
            'cursive' : "fonts/cursivefont.ttf"
        }

"fonts/cursivefont.ttf" should be the path to the ``.ttf`` or ``.otf`` file of your desired font.

If your font has bold and/or extra bold variants, you will also add it to the ``bold_xbold_fonts_list`` variable::

    define bold_xbold_fonts_list = ['sser1', 'sser2', 'ser1', 'ser2', 'cursive']

And you will need to specify how the bold and extra bold variants should be mapped. The bold version of a font is always the name of the font in the ``all_fonts_list`` + ``b``, and the extra bold is the name + ``xb``.

::

    define font_dict = { 'curly' : gui.curly_font, 'ser1' : gui.serif_1,
            'ser1b' : gui.serif_1b, 'ser1xb' : gui.serif_1xb,
            'ser2' : gui.serif_2, 'ser2b' : gui.serif_2b,
            'ser2xb' : gui.serif_2xb, 'sser1' : gui.sans_serif_1,
            'sser1b' : gui.sans_serif_1b, 'sser1xb' : gui.sans_serif_1xb,
            'sser2' : gui.sans_serif_2, 'sser2b' : gui.sans_serif_2b,
            'sser2xb' : gui.sans_serif_2xb, 'blocky' : gui.blocky_font,
            'cursive' : "fonts/cursivefont.ttf",
            'cursiveb' : "fonts/cursivefont-bold.ttf",
            'cursivexb' : "fonts/cursivefont-xbold.ttf"
        }

In this example, the bold is called "cursiveb" and the extra bold "cursivexb". Note that you will need an entry for **both** bold and extra bold, even if you only have one font. In that case, you can set the file path for both entries to the same font.

Finally, to use the font as a text tag, you need to define a style for it. Existing styles can be found in ``style_definitions.rpy``::

    style cursive:
        font "fonts/cursivefont.ttf"

    style cursiveb:
        font "fonts/cursivefont-bold.ttf"

    style cursivexb:
        font "fonts/cursivefont-xbold.ttf"


Now you can use the font while writing chatroom or text message dialogue. If you use the ``msg`` CDS, you need to preface the name of the font with the tag ``font`` e.g.

::

    msg s "This is a new font!" font cursive
    msg s "You can add other effects, too!" big font cursive xbold

And text tags work the way they would with the predefined fonts::

    s "{=cursive}This is a bit more verbose.{/=cursive}"
    s "{=cursivexb}Which method you use depends on your preference.{/=cursivexb}"


Custom Bubbles
----------------

You can also add your own custom bubbles to work with the ``msg`` CDS and spreadsheet dialogue method, or expand the functionality of existing bubbles to work for other characters.

To add a new bubble, first you must add it to the ``all_bubbles_list`` in ``variables_editable.rpy``. For this example, three bubbles called "spooky_s", "spooky_m", and "spooky_l" will be added (for small, medium, and large variants).

::

    define all_bubbles_list = ['cloud_l', 'cloud_m', 'cloud_s', 'round_l',
        'round_m', 'round_s', 'sigh_l', 'sigh_m', 'sigh_s', 'spike_l', 'spike_m',
        'spike_s', 'square_l', 'square_m', 'square_s', 'square2_l', 'square2_m',
        'square2_s', 'round2_l', 'round2_m', 'round2_s', 'flower_l', 'flower_m',
        'flower_s', 'glow2', 'spooky_s', 'spooky_m', 'spooky_l']

Next, you need to define a base style for the bubble. Typically the most important property is the padding. First, define a general style::

    style spooky_s:
        padding (25, 25, 25, 25)

    style spooky_m:
        padding (25, 25, 25, 25)

    style spooky_l:
        padding (25, 25, 25, 25)

This defines a style for the spooky bubbles with 25 pixels of padding on the left, top, right, and bottom of the bubble. These numbers should, of course, be adjusted to suit the actual bubble image you're using.

Next, if any characters have a variant of this bubble that requires different styling, you can define a style for them. For example, if the padding for ``s``'s spooky_m bubble is different, you can create an ``s_spooky_m`` style::

    style s_spooky_m:
        is spooky_m # This inherits the spooky_m padding
        top_padding 35

``is spooky_m`` tells the style to inherit from the original ``spooky_m`` style; this is optional, but can be helpful. In this case, it means that the ``s_spooky_m`` bubble has a left/right/bottom padding of 25, as in the ``spooky_m`` style, but the ``top_padding`` is now 35.

Finally, you need to define an offset for each of your new bubbles. This is how far the bubble should be relative to the top left corner of the character's profile picture (for bubbles posted on the left side of the messenger). All the existing bubble offsets can be found in ``gui.rpy``. For the ``spooky_`` bubbles, three variables are needed::

    define gui.spooky_s_offset = (140, 38)
    define gui.spooky_m_offset = (130, 38)
    define gui.spooky_l_offset = (140, 32)

Note that these are the name of the bubble + the suffix ``_offset``. You can also define specific offsets for characters using their file_id. e.g. if ``em``'s spooky_m bubble needs to be a bit further to the right than the rest of the characters', you can define the value ``define gui.em_spooky_m_offset = (150, 32)``.

And that's all! To show this special bubble in-game, you must ensure you have the appropriate images defined inside the "Bubbles/Special/" folder.

* The image extension must be one of ``.webp``, ``.png``, or ``.jpg``
* If every character uses the same bubble, it is sufficient to have a "Bubbles/Special/spooky_s.webp" image. Otherwise, you will need an image with the file_id of each character who has a variant e.g. "Bubbles/Special/ja_spooky_s.webp", "Bubbles/Special/ju_spooky_s.webp", etc.

Then you can write dialogue which will show the bubble in-game e.g.

::

    ju "This will use the spooky_m bubble." (bounce=True, specBubble="spooky_m")
    msg ja "This message will also use the spooky_m bubble" bubble spooky_m

Unlike the predefined bubbles, custom bubbles must be prefixed with ``bubble`` as in ``bubble spooky_m`` when used in the ``msg`` CDS.

.. tip::
    You can also add the name of your bubble to the ``hourglass_bubbles`` variable in ``variables_editable.rpy``. This means that when a character uses that bubble in-game, it has a chance of awarding the player an hourglass.

    Typically only the large (``l``) version of a bubble is added to this list e.g. ``"spooky_l"``


Extending Custom Bubbles
--------------------------

Besides adding your own bubbles, you can also extend the functionality of existing bubbles (or your own custom bubbles) via some special provided functions in ``variables_editable.rpy``. There are three such functions. All are passed a ``msg`` variable, which is a ChatEntry object with the following fields:

`who`
    The ChatCharacter object of the sender of the message.

    e.g. ``s``

`what`
    The contents (dialogue) of the message.

    e.g. "Have you heard from V lately?"

`thetime`
    A MyTime object with information on the time the message was sent at (in real-time)

`img`
    True if this message contains either an emoji or a CG; False otherwise.

`bounce`
    True if this message should "bounce" in as its animation. This is True if the message uses the "glowing" style of bubble, and also True if a special speech bubble is used (such as "cloud_m"). It is generally False for images and the default speech bubble.

`specBubble`
    The special bubble. Typically this is equal to somethingn like "sigh_s" or "spike_l". However, you can pass in particular strings and use this function to take care of what background image it should evaluate to.


Custom Bubble Background Function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Inside ``variables_editable.rpy`` is a function called ``custom_bubble_bg`` under the **CUSTOM MESSENGER ITEMS** header. Each chatroom message is passed to this function, which allows you a chance to check for certain conditions and return particular bubble backgrounds. For example, although currently characters can only use the special bubbles associated with their file_id, you could add a statement which will allow them to use each other's special speech bubbles::

    def custom_bubble_bg(msg):

        if msg.specBubble and len(msg.specBubble.split('_')) > 2:
            # msg.specBubble checks if the message is using a special bubble
            # specBubble.split('_') splits the special bubble into separate
            # words based on the '_' character. So, "square_m" becomes
            # ["square", "m"]. the len() function checks the length of the
            # resulting list, so ["square", "m"] has a length of 2. If the list
            # is more than 2 long, it means it was something like "r_round_s"
            # so it was split into ["r", "round", "s"], aka a length of 3
            # In this case, the program shouldn't automatically add the
            # character's file_id to the bubble.

            return "Bubble/Special/" + msg.specBubble + ".webp"

        return False

The above code will then allow you to write dialogue such as

::

    s "Look, I'm using Jumin's bubble!" (bounce=True, specBubble="ju_cloud_l")
    msg s "This message uses it too!" bubble ju_cloud_m

in order to have the characters use each other's special speech bubbles.

.. warning::
    Aside from allowing characters to use each other's special speech bubbles, you need to make sure any new bubbles you allow characters to use (such as a third glowing bubble variant) are added to the ``all_bubbles_list`` and have styles defined for them as described above.

Note that you can also return general displayables, such as a Frame(), inside the ``custom_bubble_bg`` function. For example, you could give Emma (from the new character examples) a second "glowing" bubble variant::

    def custom_bubble_bg(msg):

        if msg.who.file_id == "em" and msg.specBubble == "glow2":
            return Frame("Bubble/Special/em_glow2.webp", 25, 25)

        return False

This returns the "Bubble/Special/em_glow2.webp" image, formatted as a frame with borders 25 pixels wide. The inside of the bubble will expand to be large enough to accommodate the text (this is how the regular speech bubbles and glowing bubble variants are defined and used).

You could then write dialogue to use this bubble like::

    em "This goes in my glowing bubble." (bounce=True, specBubble="glow2")
    msg em "As does this message." bubble glow2


Custom Bubble Style Function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Although the program will try to pick out specific styles based on the name of the special speech bubble used, there may be some cases in which you want to apply a particular style to a bubble. The ``custom_bubble_style`` function in ``variables_editable.rpy`` will let you return a particular style.

For example, if you want the characters to be able to use each other's special bubbles as shown in the example for the last section, you will also need them to use the other characters' bubble styles::

    def custom_bubble_style(msg):

        if msg.specBubble and len(specBubble.split('_')) > 2:
            # See the example in the last section to understand what this
            # conditional statement is checking for
            return msg.specBubble

        return False

This will ensure that a character using another character's special bubble background will still get the original character's bubble styling as well.

This function should return a string that corresponds to the name of a style. For example, if you want a bubble to use the style ``style my_special_bubble``, then you need to return the string ``"my_special_bubble"``.



Custom Bubble Offset Function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This function allows you to fine-tune the offset of a message, relative to the top-left corner of the message box (typically the top-left corner of the character's profile picture). For example, if you wanted special speech bubbles to appear appropriately for the character on the right side of the messenger (typically the MC), you would need to adjust these values appropriately. This function is expected to return either False or a tuple of (x, y) integers for the position of this bubble.

::

    def custom_bubble_offset(msg):

        if msg.who.right_msgr and msg.specBubble:
            # This character is on the right side of the screen
            # using a special bubble
            # You will likely need more specific styling for particular bubbles,
            # but this will return a generic position for each bubble.
            return (0, 30)

        return False


Adding Chatroom Backgrounds
============================

Chatroom backgrounds must be defined in a particular way in order to be compatible with the ``scene`` and ``show`` statements to display them.

Existing background options are:

* morning
* noon
* evening
* night
* earlyMorn
* hack
* redhack
* redcrack

The background names **are** case-sensitive, so you need to get the capitalization correct.

For this example, a new background that will be displayed using ``scene rainy_day`` will be added.

To add a new background, inside ``variables_editable.rpy`` under the header **CUSTOM MESSENGER ITEMS** are several variables. First, you need to define the image that will be used as the background. This should be ``bg`` + the name of the image as you want to write when displaying it in a chatroom::

    image bg rainy_day = "center_bg:Phone UI/bg-rainy_day.webp"

The ``center_bg:`` before the file path to the image file itself is optional, but will center the image on the screen if it is not exactly 750x1334 pixels. If your image is exactly 750x1334 pixels, then just ``image bg rainy_day = "Phone UI/bg-rainy_day.webp"`` would be sufficient.

You can put this image definition wherever you like, though it may make sense to keep it under the **CUSTOM MESSENGER ITEMS** header alongside the background variable definitions.

Next, add the background name to the ``all_static_backgrounds`` list::

    define all_static_backgrounds = ['morning', 'noon', 'evening', 'hack',
                'redhack', 'night', 'earlyMorn', 'redcrack', 'rainy_day']

Note that you do **not** add the "bg" part to the name of your background.

Next, if the characters' names should appear in black during a chatroom (as is typical of the lighter backgrounds, such as "morning" and "noon"), you also need to add it to the ``black_text_bgs`` list::

    define black_text_bgs = ['morning', 'noon', 'evening', 'rainy_day']

Otherwise, if the background is not in this list, the characters' names will be displayed in white.



Adding an Animated Background
-------------------------------

If you would also like to add an animated version of your new background, you need to define a specific screen for it. First, however, you will add the background to the ``all_animated_backgrounds`` list in ``variables_editable.rpy``::

    define all_animated_backgrounds = ['morning', 'noon', 'evening', 'night',
                'earlyMorn', 'rainy_day']

Next, you need to define the screen which will have the animated background. The existing backgrounds are defined in ``screens_backgrounds.rpy``.

Because the new background is called "rainy_day", you need to create a new screen called ``animated_rainy_day``::

    screen animated_rainy_day():
        zorder 0
        tag animated_bg

        # add images here

You **must** include the lines ``zorder 0`` (to ensure the animated backgrounds appears behind other screen elements) and ``tag animated_bg`` (to ensure only one animated background is shown at once, and so that the background is properly cleared at the end of a chatroom).

You can then add animated elements to the screen. For a rainy day background, for example, you might take advantage of the existing ``slow_pan`` transform for clouds, and perhaps add raindrops which fall from the top of the screen to the bottom. As the exact requirements for a given animated background will vary substantially depending on what sort of background you want to add, this part is largely up to your own skill with screen language. You can see how the existing animated backgrounds are put together in the ``screens_backgrounds.rpy`` file.

.. warning::
    If you would like to include an animated background, it must have a corresponding "static" version that can be displayed to users who don't have animated backgrounds turned on.





Timed Menus
============

.. note::

    Example files to look at:

    * tutorial_5_coffee.rpy
    * tutorial_6_meeting.rpy


Mysterious Messenger includes a new kind of menu which will display answers at the bottom of the screen for a brief period of time while the characters continue to post messages to the chat. The player can choose an answer at any time before the timer runs out, or refrain from choosing anything and stay silent. The time the player has to choose a reply depends on the length of the dialogue before the menu. Currently, this type of menu is **only** available for chatrooms.

An example timed menu may look like the following::

    u "Hello, [name]!"
    timed menu:
        u "I'm working on a UI for the choices you see at the bottom of the screen."
        u "It's typed almost identically to regular menus this time,"
        u "but with some convenience features I think you'll like."
        u "You should try clicking the options before the timer runs out."
        "This is really neat!":
            msg u "I'm glad you think so!" curly
            award heart u
        "Does it remember choices?":
            msg u "Yes it does!" bounce big curly
            award heart u
            msg u "And you can use regular Ren'Py code in the choices"
            msg u "to do things like award heart points and the like." curly
    msg u "You can choose an answer any time while the choices are on-screen,"
    msg u "Or just let the timer run out to stay silent, too."

Timed menus are written almost identically to regular Ren'Py menus, but you can add as many lines of dialogue before the first choice as you like. The choices included in the menu will be on-screen while the dialogue after the ``timed menu:`` statement is shown.

The dialogue for the menu can be written using the ``msg`` CDS or the spreadsheet format. You can also include other regular scripting lines, such as characters entering/exiting chatrooms, inviting guests, or awarding heart points. You can include conditional statements inside the menu dialogue or on choices themselves e.g.

::

    ju "[name], do you own a cat?"
    menu:
        "No.":
            $ owns_cat = False
        "I do.":
            $ owns_cat = True
    ju "I see. Cats are wonderful creatures, aren't they?"
    timed menu:
        ju "Elizabeth the 3rd has been a constant source of joy in my life"
        if owns_cat:
            ju "as I'm sure your cat is in yours."
        ju "It's a shame some may never know the joy of owning a cat."
        "Some people are allergic though, like Zen.":
            ju "That is true."
            ju "I believe that can be overcome with appropriate medication."
        "I don't know what I'd do without my cat" if owns_cat:
            ju "May the two of you never have to be parted, then."
        "I think dogs are better, though.":
            ju "Hmm. I don't agree but I will respect your opinion."

For this menu, the line "as I'm sure your cat is in yours" only appears to a player who previously answered that they own a cat. Similarly, a player who didn't say they own a cat will not see the choice "I don't know what I'd do without my cat".

.. tip::
    Since the choices for a timed menu are smaller, it's often a good idea to either paraphrase the choices and/or keep the amount of text for each choice caption short. A maximum of three choices can appear on the screen at once for a timed menu.

.. warning::
    While you can use Python statements inside timed menus, such as ``$ owns_cat = True``, you **should not change the value of variables that are used in the menu**, such as in conditionals. This will cause undefined behaviour. So, the following is **incorrect**::

        $ owns_cat = False
        timed menu:
            ju "I believe you mentioned you own a cat, [name]?"
            $ owns_cat = True
            ju "They are wonderful companions."
            "Yeah I do own a cat" if owns_cat:
                ju "I see."
            "I don't have a cat" if not owns_cat:
                ju "Oh, I was mistaken."

    Because ``owns_cat`` was set to True inside the menu itself, its initial value before the menu (False) is used and it will be impossible for the player to ever see the "Yeah I do own a cat" choice, even if they see all the timed menu dialogue.

    You can, however, set variables inside the menu provided they are not used in that same menu. So, the following is acceptable::

        # These variables are set up outside the menu in the case that the player
        # doesn't see the full menu
        $ owns_cat = False
        $ answered_jumin = False
        timed menu:
            ju "Do you own a cat, [name]?"
            ju "Elizabeth the 3rd has been a constant source of joy in my life"
            ju "It's a shame some may never know the joy of owning a cat."
            $ answered_jumin = False
            "I have a cat.":
                $ owns_cat = True
                $ answered_jumin = True
                ju "You're someone of excellent taste, I see."
            "I don't have a cat.":
                $ owns_cat = False
                $ answered_jumin = True
                ju "Ah, that is most unfortunate then."
        if not answered_jumin:
            # The player didn't reply to the timed menu
            ju "I apologize if that was an overly personal question."

Timed Menu Settings
--------------------

There are two options in the settings that affect timed menus. Both are found under the Preferences tab. The first is **Timed Menu Speed**, a slider at the top of the screen. Clicking the title will cause the timed menu speed to be set to your current chatroom speed. Moving the slider further to the left will slow timed menus down (giving the player more time to reply), and moving the slider further to the right will speed timed menus up.

This creates a sort of "bullet time" for timed menus, where the regular chat speed may be very fast, but the timed menus will slow down to give the player time to read the messages and possible responses before deciding what to do.

The second option is under **Accessibility Options** and allows the player to toggle timed menus off altogether. If timed menus are turned off, the menu will act like a regular menu. All of the dialogue before the choices will be shown, and then the player will be presented with the "answer" button at the bottom of the screen. They will be able to choose between any of the given answers, or use a special choice that will be shown as "(Say nothing)" and will function as though the timer on the menu ran out without the player responding.

Keep these options in mind when using timed menus in your script, as not all players will want to keep them turned on.

Timed Menu Functionality
-------------------------

There are a few special things to note about timed menus:

* The time the player has to answer the timed menu depends on what the **Timed Menu Speed** slider in the settings is set to. By default this is set to the equivalent of SPEED 5 in the chatrooms.
* The timed menu's timer will expire after all the dialogue inside the menu before the choices has been posted. How long it takes to post all the messages depends on the **Timed Menu Speed** as mentioned above. So, regardless of the player's chat speed or timed menu speed, they will always have enough time to view all the dialogue inside a menu before choosing an answer.
* If a player is on Max Speed, the timed menu will be skipped entirely. The dialogue will be posted, but there will be no choices at the bottom of the screen and the program will act as though the player did not reply.

    * However, if the player has timed menus turned off, the answer button will still appear at the bottom of the screen and allow the player to choose an answer (or choose to remain silent)

* If a player chooses an answer before all the menu dialogue has been posted, they will not be able to see the rest of the menu dialogue.
* If a player replays a chatroom with timed menus from the History screen, it will always act as though the Timed Menus option is turned **off**; that is, the chat will always stop at the end of the timed menu dialogue and show the answer button to allow the player to pick a response they have previously seen in-game.

    * If the player has never chosen any of the menu choices in a past playthrough, the answer button and choices will not appear at all (since the only option would be to remain silent). The menu dialogue will be posted and the chat will simply move on.

* If all the choices in the menu have a conditional dictating when they should be shown (e.g. ``"I want to visit Seven" if s.heart_points > 10:``) and none of those conditions evaluate to True (that is, none of the choices should be shown to the player because they don't meet the conditions), then the menu dialogue will be shown only if ``show_empty_menus`` is True. This variable can be found in ``variables_editable.rpy`` and is True by default. If set to False, if a menu has no valid choices then the menu dialogue will be skipped altogether and the chat will continue after the menu.
