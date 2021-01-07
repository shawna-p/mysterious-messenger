================
Story Mode (VN)
================

.. toctree::
    :caption: Navigation

    story-mode

In this program, you can create Story Mode sections which can either be attached to a chatroom or can appear as its own timeline item. You declare "solo" Story Mode items in the route definition (see :ref:`Story Mode`).

Writing a Story Mode
====================

.. note::
    Example files to look at:

    * tutorial_6_meeting.rpy
    * tutorial_3b_VN.rpy

    *A brief overview of the steps required (more detail below):*

    #. If writing an attached Story Mode, create a label using the label of the attached chtroom + the suffix ``_vn`` (e.g. ``label my_chatroom_vn``)

        #. (Optional) Indicate the character a Story Mode section is associated with by including their file_id as an additional suffix (e.g. ``label my_chatroom_vn_s``)
        #. (Optional) Indicate that this Story Mode is the party by including the suffix ``_party`` (e.g. ``label my_chatroom_party``)

    #. Show your desired background with ``scene bg my_background``.

        #. (Optional) Use transitions like ``with fade`` e.g. ``scene bg your_bg with fade``
        #. (Optional) Write ``pause`` after your ``scene`` statement to give the player a moment to look at the background.

    #. Add music with ``play music your_music_var``.
    #. Fill out the dialogue and character expressions.
    #. End the label with ``return``.


If this Story Mode is associated with a chatroom, the program uses a specific naming convention to know to set it up. For a Story Mode icon not associated with any character, you can just use the name of the chatroom + the suffix ``_vn`` e.g.

::

    label my_chatroom:

will look for a generic Story Mode located at

::

    label my_chatroom_vn:

If you would instead like to have a certain character's image associated with the Story Mode, you must add another suffix: ``_`` + the file_id for that character e.g.

::

    label my_chatroom_vn_y:

will show up in the program as a Story Mode associated with Yoosung.

Alternatively, you can also use the suffix ``_party`` to indicate a Story Mode contains the party e.g.

::

    label my_chatroom_party:

Next, you can set up the Story Mode and begin writing dialogue. It's a good idea to start by setting a background using Ren'Py's ``scene`` statement::

    scene bg rika_apartment with fade

``bg rika_apartment`` is a background that is already defined in ``vn_variables.rpy``. You can add your own backgrounds here as well to display in-game. Backgrounds should be ``750x1334`` pixels.

``with fade`` indicates that the background should fade in from black. There are many more transitions you can use that are covered in Ren'Py's documentation `Transitions <https://www.renpy.org/doc/html/transitions.html>`_.

If you want the player to have a moment to look at the background before you move on, you can write ``pause`` after showing the image e.g.

::

    scene bg rika_apartment with fade
    pause

Adding Music and SFX
====================

Playing background music inside a Story Mode is the same as playing music elsewhere in the program; simply use ``play music my_music_var`` where ``my_music_var`` is a track included in the ``music_dictionary`` in ``variables_music_sound.rpy``.

To add sound effects, use

::

    play sound door_knock_sfx

where ``door_knock_sfx`` can be replaced by the name of whatever sound effect you want. There are several files already pre-defined in ``variables_music_sound.rpy``.

Note that Ren'Py's built-in music and sound functions have been modified to work with audio captions for this program. The program will notify you if an audio caption has not been defined for an audio file.

If you would like to play a sound that does not have an audio caption, you can give ``play music`` or ``play sound`` the ``nocaption`` argument e.g.

::

    play music ringtone nocaption

For accessibility purposes, most audio should have a caption, so this option should be used sparingly. Previously defined audio captions can be found in ``variables_music_sound.rpy``. To learn about adding your own audio, see :ref:`Adding New Audio`.


Providing Choices
=================

Writing a menu in a Story Mode is identical to how it is written in phone calls; that is, you need to include ``extend ''`` after ``menu:`` and before the choices::

    menu (paraphrased=True):
        extend ''
        "(Investigate the window)":
            u "Don't move."
        "(Stay where you are)":
            u "Why hello there."

This tells the program to display the last line of dialogue underneath the choice menu while it is on-screen.

Awarding Heart Points
=====================

Heart points are awarded the same way as they are elsewhere in the game::

    award heart ja

where ``ja`` is the variable of the character you're awarding a heart point for. See :ref:`Showing a Heart Icon` for more information.


Positioning Characters
======================

There are several pre-defined positions you can move the characters to. These are:

* vn_farleft
* vn_left
* vn_midleft
* vn_center
* vn_midright
* vn_right
* vn_farright
* default

Not every position will work for every character due to spacing and differences in sprite design. You can define more positions in ``vn_variables.rpy``.

``vn_center`` is a unique position because it moves the character closer to the screen in addition to centering them. It's often used to imply the character is talking directly to the player. However, if you want to move a character who is currently shown in the ``vn_center`` position to another position, you must ``hide`` them first. See ``tutorial_6_meeting.rpy`` for an example of this.

To show a character at a given position, write

::

    show jumin front at vn_right

where ``jumin front`` is the name + attributes of the character you want to show (e.g. expressions, outfits etc) and ``vn_right`` is the position to show them in. You can also add a transition like so::

    show jumin side happy at vn_left with ease

where ``ease`` is a transition. (See `Transitions <https://www.renpy.org/doc/html/transitions.html>`_ in the Ren'Py documentation for more).


Changing Outfits and Expressions
================================

To show a character, look at [[INSERT LINK HERE] and find the character you want to show under the **Character VN Expressions Cheat Sheet** header.

To show a character, use their name tag (usually their first name) + any additional expression, position, outfit, or accessory tags as applicable. In practice, this means if you want to show ``jaehee`` with the expression ``happy`` and wearing her ``glasses``, write

::

    show jaehee glasses happy

Since Jaehee does not have any additional positions (such as a "side" or "front" position), you don't need to include that when you show her on-screen. However, a character like V *does* have multiple positions, and so a similar statement for him would look like

::

    show v side angry glasses


where ``v`` is the character, ``side`` is the position, ``angry`` is his expression, and ``glasses`` indicates he should be shown wearing glasses.

To change the character's outfit, when you show them you should include the attribute name of the outfit you'd like them to wear e.g.

::

    show yoosung suit surprised


In this case, ``yoosung`` is the character, ``suit`` is his outfit, and ``surprised`` is his expression.

Note that attributes can be listed in any order after the character, so ``show yoosung surprised suit`` is equally correct.

Characters with accessories (glasses, hoods, masks) can include those keywords as well e.g.

::

    show v front mint_eye worried hood_up at vn_right with easeinright


which will show ``V`` in his ``front`` position wearing his ``mint_eye`` cloak with the ``hood_up`` at the position ``vn_right`` after being "eased in" (``easeinright``) from the right side of the screen.

Luckily, after you've shown a character on-screen the first time, Ren'Py will remember which attributes you showed them with so that you don't have to write out the whole attribute list every time after that. For example::

    show v front mint_eye worried hood_up at vn_right with easeinright
    v "Some sample dialogue."
    show v thinking
    v "More dialogue."


The second ``show`` statement remembers the attributes ``v`` was shown with previously, namely ``front mint_eye hood_up`` since the ``thinking`` expression replaces the ``worried`` expression. So he will still be shown in his front position with the mint_eye cloak and his hood_up, just with the ``thinking`` expression.

Attribute Shorthand
-------------------

There is also another way of simplifying showing characters even further -- since characters are defined with an "image" tag in mind, after showing them on screen the first time you can change tags directly during dialogue like so::

    show seven front happy party
    s "Some dialogue while happy."
    s worried "Some dialogue with the party outfit in the front pose, but worried."
    s normal "Now in the normal outfit, and still worried and in the front position."

Note that you can only change expressions this way after the character has already been shown on-screen.

For more on Image Attributes, see the [Ren'Py documentation pages on Dialogue and Narration](https://www.renpy.org/doc/html/dialogue.html?highlight=attribute#say-with-image-attributes "Ren'Py Dialogue and Narration documentation").

Hiding Characters
-----------------

When you're done showing a character on-screen, you only have to use their name to hide them::

    show seven front happy party
    s "Some dialogue while happy."
    hide seven



Including a Story Mode During a Chatroom
========================================

.. note::
    Example files to look at:

    * tutorial_9_storytelling.rpy

    *A brief overview of the steps required (more detail below):*

    #. Create a chatroom as you usually would (see :ref:`Creating a Chatroom`.
    #. When you want the story mode to interrupt the chatroom, use ``call vn_during_chat("name_of_story_mode_label")`` where ``name_of_story_mode_label`` is the name of the label where the program can find the associated story mode.

        #. If you want to change the list of chatroom participants between chatroom sections, pass the argument ``reset_participants=[y, s, m]`` where ``[y, s, m]]`` is a list of the character variables who you want to show participating in the chatroom section following the story mode.

    #. If you don't want to return to the chatroom section after jumping to the story mode section, use the argument ``end_after_vn=True`` e.g. ``call vn_during_chat("vn_label", end_after_vn=True)``.
    #. Create the label for the story mode and write the dialogue as normal (see :ref:`Writing a Story Mode`).
    #. If the timeline item does not end on the story mode, continue writing chatroom dialogue after the call to ``vn_during_chat``.

        #. (Optional) use ``clear chat`` to erase the chat history.
        #. (Optional) change the chat background with a ``scene`` statement.
        #. (Optional) clear all participants from the chatroom with ``clear chat participants``.

    #. End the chatroom and any story mode labels with ``return``.

.. tip::
    This section covers how to include a story mode section **in the middle of a chatroom**, such that the player will be viewing the chatroom and it will transition into a story mode section and back to the chatroom in the same "scene".

    This is different from how Story Mode sections usually play out in-game; that is, first the player plays a chatroom, is returned to the timeline screen, and then must select the corresponding Story Mode section to proceed. If you are interested in the latter, see :ref:`Attached Story Mode`.

First, you'll begin by setting up a chatroom the way you usually would (see :ref:`Creating a Chatroom`). Next, wherever you would like to have the story mode appear and interrupt the chatroom, write ``call vn_during_chat("my_vn_label")`` where ``my_vn_label`` is the name of the label you will be using for your story mode section.

.. warning::
    Be sure your mid-chatroom story mode label **doesn't** follow one of the naming conventions for declaring an attached Story Mode -- so, if your chatroom is at ``label my_chatroom``, then don't call the mid-chatroom story mode ``label my_chatroom_vn`` or the program will generate an attached Story Mode leading to that label!

Create this label and write the story mode. It is written the same way as a regular story mode -- see :ref:`Writing a Story Mode`. Example::

    label my_chatroom:
        scene morning
        play music silly_smile_again
        enter chatroom y
        y "Good morning!"
        call vn_during_chat("my_chatroom_vn_chat")
        y "And we're back! Hope you enjoyed that."
        exit chatroom y
        return

    label my_chatroom_vn_chat:
        scene bg rika_apartment
        play music lonesome_practicalism
        show jaehee glasses happy
        ja "Oh dear. It seems the new intern has spilled coffee on this file."
        return

Once the story mode is finished, the program will return to where it left off in the chatroom. All the previous messages will remain on-screen in the chatlog, and the background will be what it was before the story mode.

Clearing the Chat History
-------------------------

If you would like to clear the chat history after returning from the Story Mode section (that is, previous messages in the chatroom will be erased), you can use the ``clear chat`` CDS::

    y "Anyway, I should go now."
    exit chatroom y
    call vn_during_chat('my_chatroom_vn_chat')
    clear chat
    enter chatroom y
    y "Hi, [name]."

Modifying Chatroom Participants
-------------------------------

If you want to modify the list of participants between scenes, you can either clear the participants altogether or pass ``vn_during_chat`` a special ``reset_participants`` argument. First, to remove all participants from the chatroom, use ``clear chat participants``::

    label my_chatroom:
        scene morning
        play music narcisisstic_jazz
        enter chatroom z
        z "Darn... I was hoping to catch Jaehee in the chatroom at this hour."
        z "I wonder what she's up to..."
        call vn_during_chat("my_chatroom_vn_chat")
        clear chat participants
        enter chatroom ja
        ja "And the day begins to go downhill..."
        ja "I suppose everyone is busy doing something else at this hour."
        ja "I will log off as well, then."
        exit chatroom ja
        return

    label my_chatroom_vn_chat:
        scene bg cr_meeting_room
        show jaehee glasses at vn_midleft
        show jumin front at vn_midright
        ju "Assistant Kang. I need you to reschedule a meeting."
        ja "Oh... I see. Which meeting do you need to reschedule?"
        ju "The one for the Cultured Citizens group this afternoon."
        ju "I received word that Elizabeth the 3rd is acting particularly lethargic today so I will need to return to check on her."
        ja "...Understood."
        return

In this example, when the player returns from the Story Mode section, the chat history will be cleared and the characters who were present in the chatroom prior to the story mode (aka Zen) will no longer be shown as in the chatroom. The main character will be automatically added back to the list of people present if this chatroom is not expired; otherwise, no one will be in this chatroom when the story mode returns to the chatroom.

You can also tell the program exactly who you would like to appear in the chatroom when the story mode is finished via ``reset_participants``::

    label day_3_8:
        scene night
        play music mint_eye
        r "I know I've been really busy lately,"
        msg r "But I wanted to let you know that I'll be over with food shortly!" curly glow
        msg r "I made it myself ^^" glow
        r "See you soon!"
        call vn_during_chat("day_3_8_story_vn", reset_participants=[s, z])
        clear chat
        scene earlyMorn
        play music narcisisstic_jazz
        z "You know, we haven't heard from [name] for a few hours..."
        z "I hope [they_re] doing all right."
        s "lolol ur impatient aren't u."
        s "I'm sure [they] just logged off for the night."
        z "You're probably right. I should go to sleep, too."
        s "Toodles~!"
        exit chatroom z
        exit chatroom s
        return

    label day_3_8_story_vn:
        scene bg mint_eye_room
        play sound door_knock_sfx
        "(A knock at the door)"
        menu:
            extend ''
            "(Answer the door)" (paraphrased=True):
                pass
            "Who is it?":
                r "It's me, Ray! I've come to bring you dinner."
        play sound door_open_sfx
        "(Door opened)"
        show saeran ray happy
        r "Hi, [name]. I really missed you today."
        r "I brought some food. I hope it's to your liking."
        return

In the above example, after the game returns from the story mode, the chat log is cleared and Zen and 707 are added to the list at the top of the chatroom to show that they are present. The main character is *not* added; in order to include them, the argument would need to be ``reset_participants=[s, z, m]`` instead (so, it needs to include ``m``).

The background for the chatroom is also modified upon returning with another ``scene`` statement, and new music is played. Unless otherwise specified, any music that is already playing during the previous chatroom or story mode will be carried over into the next section until the timeline item ends. If you want to stop the music altogether, you can use the line ``stop music``.

Ending a Timeline Item after a Story Mode Section
-------------------------------------------------

If you don't want the player to return to the chatroom and instead want the timeline item to end on the story mode section, you can pass the argument ``end_after_vn=True`` to ``vn_during_chat`` e.g.

::

    u "Anyway, this is the end of the scene."
    exit chatroom u
    call vn_during_chat("my_final_vn_label", end_after_vn=True)
    return












