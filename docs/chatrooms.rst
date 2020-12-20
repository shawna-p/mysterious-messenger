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

First, you need to give the chatroom a background to show::

    label day_1_1:
        scene morning

While chatrooms also use Ren'Py's ``scene`` statement to show backgrounds, there is a limited number of built-in backgrounds to use. New backgrounds must be defined as described in [[INSERT LINK HERE]]. Your background options are:

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

where ``mystic_chat`` can be replaced by the name of whatever music you want. There are several files pre-defined in [[INSERT LINK HERE]] (variables_music_sound). If you want to define your own music, you need to add it to the ``music_dictionary`` as well so that it is compatible with audio captions. See [[INSERT LINK HERE]] for more information.

Next, you'll write the dialogue for your chatroom. See [[INSERT LINK HERE]]. Finally, to end the chatroom, end the label with ``return``::

    label day_1_1:
        scene earlyMorn
        play music mint_eye
        # Dialogue will go here
        return

To learn how to make this chatroom appear in your game, check out [[INSERT LINK HERE]].


Writing Chatroom Dialogue
=========================

There are two primary ways of writing dialogue for your chatroom. The first is to use a special ``msg`` CDS, and the second is to use a special spreadsheet to help generate the dialogue for you.

Using the msg CDS
-----------------

The ``msg`` CDS helps add effects to your dialogue, such as special speech bubbles or alternative fonts, without sacrificing the readability of the dialogue. Dialogue written with the ``msg`` CDS looks like the following::

    msg r "Usually, the program would delay sending text messages and phone calls" sser1
    msg r "until after both this chatroom and the Story Mode were played." sser1
    msg r "But since v3.0, things are more flexible!" flower_m
    msg r "If you declare a route using the new format,"
    msg r "you can have text messages and phone calls and the like after any story item,"
    msg r "even a chatroom that has a Story Mode attached" glow

(Dialogue can be found in [[INSERT LINK HERE]])

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

You can also use your own fonts with the ``msg`` CDS. See [[INSERT LINK HERE]] for more on customizing the ``msg`` CDS.

In order to use one of the built-in fonts, just include the name of the desired font after the dialogue e.g.

::

    msg u "This is example dialogue in the cursive font." curly
    msg u "This is in the sans serif 1 font." sser1

Note that you can only have one font at a time; including more than one will simply use the last font given. The default font is ``sser1``.

Emphasis
^^^^^^^^

You can emphasize text in several ways. To use the **bold** version of a font, use the argument ``bold`` after the dialogue e.g.

::

    msg u "This text is bolded." bold

Some fonts have **extra-bold** variants as well. These are defined in [[INSERT LINK HERE]] variables_editable.rpy in the variable ``bold_xbold_fonts_list``. To make a font extra bold, add the ``xbold`` clause after the dialogue e.g.

::

    msg ja "This text is in the sans serif 2 font, extra bold." sser2 xbold

Finally, you can also increase the size of the text inside a speech bubble with the ``big`` argument e.g.

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


You can also use your own bubbles with the ``msg`` CDS, or modify it so that characters can use each other's special speech bubbles. See [[INSERT LINK HERE]] for more on customizing the ``msg`` CDS.

Images
^^^^^^

The ``msg`` CDS will automatically detect if dialogue includes a recognized emoji and mark the dialogue as an image accordingly. If you want a character to post an image in the chatroom (such as a CG), then you can use the ``img`` argument::

    s "cg s_1" img
    s "I just posted a CG!"

You need to follow the rules outlined in [[INSERT LINK HERE]] in order for the program to find the correct image and display it during a chatroom. For CGs, the program will also automatically unlock the image in the gallery.

Modifying Message Speed
^^^^^^^^^^^^^^^^^^^^^^^

Finally, you can also adjust the speed at which a message is posted. For example, if you want a character to post a bunch of messages in quick succession, you can use the ``pv`` clause to use a multiplier on the speed at which a message is posted e.g.

::

    s "These" pv 0.1
    s "messages" pv 0.1
    s "are" pv 0.1
    s "posted" pv 0.1
    s "quickly!!!" pv 0.1

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

In general, you should create a copy of the **CHATROOM TEMPLATE** tab and fill it out with your desired dialogue. Don't forget that messages such as ``707 has entered the chatroom`` are handled differently -- see [[INSERT LINK HERE]] for more.

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

where ``s`` is the variable of the character who is entering the chatroom. See [[INSERT LINK HERE]] for a list of the characters currently programmed into the game.

.. tip::
    You can also use ``call enter(s)`` to have a character enter the chatroom.

To get the message ``Character has left the chatroom``, use the ``exit chatroom`` CDS::

    exit chatroom s

where ``s`` is the variable of the character who is exiting the chatroom.

.. tip::
    You can also use ``call exit(s)`` to have a character leave the chatroom.



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

You can also turn ``paraphrased`` on or off on a per-menu or per-choice basis. For more on paraphrasing, see [[INSERT LINK HERE]].

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

Showing a Heart Icon
--------------------

Awarding a heart point
^^^^^^^^^^^^^^^^^^^^^^

To show a heart icon to the player and award them "heart points" associated with a particular character, use

::

    award heart s

where ``s`` is the variable of the character whose heart icon you'd like to show. The player will receive one heart point with that character when this code is run. See [[INSERT LINK HERE]] for a list of the characters built-in to the program and how to add your own character.

.. note::
    Ray (``r``) and Saeran (``sa``) share heart points. So, if you award a heart point for Saeran via ``award heart sa``, Ray will also receive 1 heart point.

There is also a second optional argument to ``award heart``::

    award heart ju bad

``bad`` tells the program that this heart is a "bad" heart point, and should count towards a bad ending. In-game, a ``bad`` heart appears the same as a normal heart point. You can use this method to count the number of choices a player makes that would lead towards a bad ending, and then check whether the player made more "good" or "bad" ending choices when they reach a plot branch. See [[INSERT LINK HERE]] Plot Branches for more information on this.

Removing a heart point
^^^^^^^^^^^^^^^^^^^^^^

If the player makes a choice a character doesn't like, you can cause them to lose a point with a character by showing a "heart break" icon.

::

    break heart ju

where ``ju`` is the variable of the character whose heart break you'd like to show. This will **always** subtract points from the character's "good" heart points and never the "bad" points. Note that losing heart points in this way does not subtract from the heart point totals the player uses to unlock additional profile pictures for a character (See [[INSERT LINK HERE]]).

.. tip::
    Both ``break heart ju`` and ``heart break ju`` will show the heart break animation for the character ``ju``. You can't switch the word order for ``award heart`` though!



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

