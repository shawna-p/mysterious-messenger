.. _beginners-guide:

================
Beginner's Guide
================

If you want to create your own route and some of the technicalities are going over your head, this guide will take you through setting up a new route from start to finish. More specific pages will be referenced throughout. If you already know a bit about the program, you may want to start with :ref:`Setting up a Route` instead.

.. toctree::
    :caption: Navigation

    beginners-guide


Getting Started
===============

If you've downloaded the program and assets (or created your own replacement assets), the first thing you should do is hit ``Launch`` from the Ren'Py launcher and play through the Tutorial Day to get a feel for what the program is capable of. If you tried to launch the game before obtaining or creating the assets, be sure to use **Delete Persistent** in the Ren'Py launcher under the **Actions** header.

Opening the code in a code editor
---------------------------------

Next, you need to create a new ``.rpy`` file. This is where you will write the code that will tell Mysterious Messenger how you want your route to be set up. If you have a program to edit code in, such as VS Code or Atom, you should open that program. Otherwise, you can either download an editor online or tell Ren'Py to download it for you.

.. note::
    If you don't yet have a code editor, I recommend VS Code, which you can download here: `<https://code.visualstudio.com/download>`_

    You can then install the Ren'Py language extension, which will highlight keywords in Ren'Py for you: `<https://marketplace.visualstudio.com/items?itemName=LuqueDaniel.languague-renpy>`_

    Finally, you can tell Ren'Py to use the System Editor under ``Preferences`` -> ``Text Editor`` -> ``System Editor``. Outside of Ren'Py, when you double-click a ``.rpy`` file in the ``mysterious-messenger/game`` folder, tell it to always open ``.rpy`` files with VS Code.

Otherwise, to get Ren'Py to download an editor for you, in the Ren'Py launcher under ``Preferences`` there is an option called ``Text Editor``. Click on that, and you'll see a variety of suggested editors. Of these, I recommend downloading Atom.

``Return`` to the main screen of the Ren'Py launcher. Next, in your file explorer, open the ``mysterious-messenger/game`` folder. To keep things organized, you should create a new folder here. Call it ``my_new_route``.

Now you can open your code editing program and use ``File -> Open Folder...`` to navigate to the ``mysterious-messenger/game/my_new_route`` folder. It's blank for now, but you will add ``.rpy`` files to it soon.

Creating a new .rpy file
------------------------

Inside your code editor, you can use ``File -> New File``. Name this file ``my_route.rpy``. Don't forget you need to include ``.rpy`` at the end so the editor and program understand this file contains code for Ren'Py.

Defining the route
==================

Inside your new ``.rpy`` file, copy and paste the following code::

    default my_route_good_end = ["Good End",
        RouteDay('1st'),
        RouteDay('2nd'),
        RouteDay('3rd'),
        RouteDay('4th'),
        RouteDay('5th'),
        RouteDay('6th'),
        RouteDay('7th'),
        RouteDay('8th'),
        RouteDay('9th'),
        RouteDay('10th'),
        RouteDay('Final')]

This defines a variable which is going to contain the information the program needs to understand how to display the route to the player. In particular, this defines the "Good End" of a route. In the history screen, when the player reaches the end of this route the final timeline item will show up under the title "Good End". This guide only covers how to add one ending, but if you want to learn more you can refer to :ref:`Plot Branches`.

Ensuring the route shows up in History
---------------------------------------

The last variable you defined is just for the "Good End" path of a route. You may want multiple endings or paths, perhaps with different characters or to reflect how the player's choices affected the narrative. This next variable tells the program that the various endings are part of the same "route". For now, you only have one ending, "Good End", but you can add more later.

Beneath the code from earlier, copy and paste the following code::

    default my_new_route = Route(
        default_branch=my_route_good_end,
        branch_list=None,
        route_history_title="My New"
    )

This tells the program which endings are associated with this route. ``route_history_title="My New"`` means that in the History screen, this route will be displayed as "My New Route". The default/longest path (and in this case, the only path) in this route is ``my_route_good_end``, and there are no other branches so ``branch_list=None`` lets the program know there aren't any other branches. How to add additional branches will be covered later.

Accessing the New Route
========================

Now you need to tell the program to begin your route when the player hits the "Original Story" button from the main menu. To do this, you need to modify the ``custom_route_select_screen``, which is found in the file ``screens_custom_route_select.rpy``. Open that file in your editor.

The default code for this screen looks like::

    screen custom_route_select_screen():
        vbox:
            style_prefix 'route_select' # Remove this if you want your own styles
            button:
                ysize 210 # Set the height of the button
                # The image that goes on the left of the button
                add 'Menu Screens/Main Menu/route_select_tutorial.webp':
                    align (0.08, 0.5)
                action Start()
                # The box with text on the right side of the button
                frame:
                    text "Tutorial Day"

The simplest way to modify this is to change the ``action Start()`` property for the existing button. Normally this tells the program to begin the game at the ``start`` label. Modify ``action Start()`` to say ``action Start("my_route_introduction")``, and change the line ``text "Tutorial Day"`` to say ``text "My New Route"``. The whole screen will now look like::

    screen custom_route_select_screen():
        vbox:
            style_prefix 'route_select' # Remove this if you want your own styles
            button:
                ysize 210 # Set the height of the button
                # The image that goes on the left of the button
                add 'Menu Screens/Main Menu/route_select_tutorial.webp':
                    align (0.08, 0.5)
                action Start("my_route_introduction")
                # The box with text on the right side of the button
                frame:
                    text "My New Route"

You can also change the image 'Menu Screens/Main Menu/route_select_tutorial.webp' to something else, though it's perfectly fine to leave it as-is for now.

To see this new route select screen, on the main menu, click the **Developer** button in the bottom right corner, then check off the option titled "Use custom route select screen". Now when you start a new game and click Original Story, your custom route select screen will be displayed, though you haven't made an introduction yet so clicking on this button will cause an error.


Creating the Introduction
===========================

Now that you've got a button to start your new route, you need to write an actual introduction for it. To keep things organized, create a new ``.rpy`` file like you did last time and put it inside your ``my_new_route`` folder. Call this file ``my_route_intro.rpy``.

Now you need to create a label that the program will jump to when the player hits the button on the route select screen from earlier. The action on that button was ``action Start("my_route_introduction")``, so this label must be called ``my_route_introduction``::

    label my_route_introduction():
        $ new_route_setup(route=my_new_route, participants=None)
        $ paraphrase_choices = False

        scene night
        play music mystic_chat
        enter chatroom u
        u "This is an example chatroom! You can customize it more later."
        exit chatroom u
        return

This is where the program will jump to when the player selects this route to play. Then there are a few lines of setup, which will be explained below.

``new_route_setup`` is a special function that sets up the introduction of a route and lets the program know which route it should set up in the timeline. It has two fields:

`route`
    The Route variable defined earlier containing the main path and any branching paths for this route.

`participants`
    By default, this is ``None``, which means that no one starts in the introductory chatroom. If you would like to have characters start in the chatroom, then you can add them here as a list e.g. ``participants=[ja, ju, s, y, z]`` adds the characters ja, ju, s, y, and z to the chatroom initially before the player arrives.

Next is the line ``$ paraphrase_choices = False``. This tells the program that the main character should say the exact dialogue found on the choice buttons after the player has selected that choice. If you want to type out most choice dialogue yourself, then this should be ``$ paraphrase_choices = True`` instead. Note that you can toggle choice paraphrasing on and off on a per-menu or per-choice basis; see :ref:`Paraphrased Choices` for more information. The rest of this tutorial will assume you have ``$ paraphrase_choices = False``.

``scene night`` tells the program to set up the ``night`` background for the chatroom. For more information on backgrounds, see :ref:`Adding Chatroom Backgrounds`.

``play music mystic_chat`` tells the program to play the "mystic_chat" music in the background. This loops automatically. The usual Ren'Py method of playing music has been overwritten to support audio captions, though it supports all the usual features such as fadeout and looping as found in the Ren'Py documentation on audio. For more information, see :ref:`Adding New Audio`.

``enter chatroom u`` and ``exit chatroom u`` display messages like "Unknown has entered the chatroom." and "Unknown has left the chatroom." respectively. For more information on these sorts of functions, see :ref:`Advanced Chatroom Features`.

Finally, all labels including this introductory chatroom should end with ``return``. In this case, it will show the Save & Exit button to the player and return them to the game's home screen.

All of these features and more are covered in :ref:`Chatrooms Topic`, including how to write dialogue. You're welcome to expand on this chatroom later with more dialogue.


Defining Timeline Items for your Route
=======================================

Now that you've created an introduction for your route, you need to actually put some content in it. Currently the player can select your route and play the introduction (feel free to test it out!) but there won't be any chatrooms or Story Mode sections on their timeline screen. You'll also see an error message informing you that you have no content to your route. It's time to fix that now.

Return to your file ``my_route.rpy``. It should contain the code from earlier::

    default my_route_good_end = ["Good End",
        RouteDay('1st'),
        RouteDay('2nd'),
        RouteDay('3rd'),
        RouteDay('4th'),
        RouteDay('5th'),
        RouteDay('6th'),
        RouteDay('7th'),
        RouteDay('8th'),
        RouteDay('9th'),
        RouteDay('10th'),
        RouteDay('Final')]

To create your first chatroom, modify the above code so it now looks like the following::

    default my_route_good_end = ["Good End",
        RouteDay('1st',
            [ChatRoom("Welcome!", "day_1_chatroom_1", '00:01')
            ]),
        RouteDay('2nd'),
        RouteDay('3rd'),
        RouteDay('4th'),
        RouteDay('5th'),
        RouteDay('6th'),
        RouteDay('7th'),
        RouteDay('8th'),
        RouteDay('9th'),
        RouteDay('10th'),
        RouteDay('Final')]

The main thing that has changed is the code after ``RouteDay('1st',``, which now has something called a ``ChatRoom`` object. This object holds information that tells the program information like the title of the chatroom ("Welcome!"), the label where the program can find the chatroom ("day_1_chatroom_1"), and the time the chatroom should appear at ("00:01" aka 1 minute past midnight). A typical RouteDay is made up of a list of these items, along with StoryMode and StoryCall objects (for more, see :ref:`Adding Timeline Items`).

Next, you need to define your new chatroom, similar to what you did for the introduction.

Creating the First Chatroom
----------------------------

There are two main ways of writing chatroom dialogue. The most flexible way is to write the script for the chatroom yourself in an ``.rpy`` file, described below. If you're more of a visual person, though, and some of this is going over your head, you might also try the **Chatroom Creator**, which you can access from the **Developer** button on the main menu. See :ref:`Chatroom Creator` for more detailed information on using this. While you will have fewer options to customize the chatroom using the creator as opposed to creating it yourself in code (for example, the chatroom creator cannot make choice menus), you can export your created chatroom as code and modify it further in the generated ``.rpy`` file to customize it to your needs. However, below we'll explore how you can create chatrooms just from code.

Like before, you should create a new ``.rpy`` file in order to keep things organized. Call this one ``day_1_chatroom_1.rpy``. It doesn't have to be named the same as the chatroom label, but noting the day and chatroom number of this chatroom will help you keep things organized.

Now you need to define the body of the chatroom. First, make a label with the name you wrote earlier for the ``ChatRoom`` object, namely ``day_1_chatroom_1``::

    label day_1_chatroom_1():
        scene earlyMorn
        play music mystic_chat
        enter chatroom u

        u "Congratulations! You've created your first chatroom."

        menu:
            "That's amazing!":
                u "Isn't it? I'm glad you think so."
            "This is a lot of work.":
                u "I'm sure it will get easier with practice!"
                u "There are plenty of wiki pages to help you out, too."

        u "I'm leaving now. Good luck!"
        exit chatroom u
        return

This defines a very basic chatroom with the character "Unknown" (``u``). In this particular chatroom, the player is allowed to make a choice, as defined under the ``menu:`` code. For more on writing chatrooms and creating choices, see :ref:`Advanced Chatroom Features`. There are many more things you can do besides just chatrooms as well, such as having characters send text messages or call the player. For more on those, see the corresponding sections in the documentation.

Creating an Expired Chatroom
-----------------------------

There's one last thing you should do before finishing your first chatroom. If the player is playing in real-time, or chooses to back out of a chatroom before they've finished viewing it, the chatroom may "expire". Typically this means the player will then see a version of the chatroom where they don't get to participate in the conversation.

The program automatically looks for this "expired chatroom" using the name of the original chatroom + the suffix ``_expired``. So you should define your expired chatroom label beneath the regular chatroom like so::

    label day_1_chatroom_1_expired():
        scene earlyMorn
        play music mystic_chat
        enter chatroom u

        u "Oh... it appears [name] is not here."
        u "Well, I'll come back later. Bye!"

        exit chatroom u
        return

This is the chatroom the player will see if it is expired. It can be as similar or different from the original non-expired chatroom as you like. You may also note the use of ``[name]`` in the dialogue; this will be replaced with the player's name as it was entered in the profile screen. There are also variables to handle the player's pronouns, as players are free to choose one of she/her, he/him, or they/them pronouns at any time. See :ref:`Pronoun Integration` for more.

.. note::
    In this program, there are also standalone Story Mode and Story Calls. Story Mode sections do not expire, but Story Calls *will* expire like chatrooms in real-time or if the player hangs up in the middle of a conversation, and should have an ``_expired`` label as well.


Playing Your Route
===================

To play your new route, close the program if open and re-launch it after saving all your open ``.rpy`` files. Select "Settings" from the main menu and then navigate to the "Others" tab and select "Start Over". Then ensure you have the option titled "Use custom route select screen" checked off in the **Developer** settings button in the bottom right corner. Now you can press "Original Story" and click on your new route to play it!

Tips For Testing and Debugging
===============================

When writing a new route, you might run into some error screens from time to time. There are a few steps you can take to help identify the problem:

1) Take a look at the error message. It goes back in what's called "reverse stack order", so the lines at the top are typically less related to the problem than the ones lower down. In particular, you should look at the line just before it says "Full Traceback".
2) Usually you will see an error that reads something like ``NameError: name "something" is not defined``. The first part is the type of error - in this case, a ``NameError``. There are other kinds of errors, like ``ScriptError``, ``AttributeError``, and more. The next part tells you a bit about the error itself. Sometimes this will be immediately obvious - for example, ``ScriptError: could not find label 'myroute_day3_3'`` means that the program can't find the label ``myroute_day3_3``, so either you've made a typo somewhere, failed to save the file with the label on it in the right place, or haven't created the label yet. Other times the error is a bit more obtuse.

.. tip::
    One of the most common sources of errors is missing commas or incorrect parentheses. If you see an error that looks like ``TypeError: string indices must be integers``, be on the lookout for missing commas or parentheses!

3) If the error message isn't particularly clear, the first thing you should usually try is just to close the game and re-open it. If you've been making lots of script changes with the game open, particularly if the game is set to Reload or Auto-Reload, occasionally Ren'Py can't figure out how to update the script while the game is still open and it crashes. In particular, if you see an error message that looks like ``Exception: Couldn't find a place to stop rolling back. Perhaps the script changed in an incompatible way?``, this is a very common cause of that error. Closing and re-launching the game from scratch will often fix this.
4) Another common source of errors is old save games. If you aren't seeing changes you've made, try starting a new game from the settings rather than loading an old save or hitting "Original Story" (which automatically loads a save).

If you're still having trouble, feel free to send a message in the Mysterious Messenger Discord to report a bug!

Next Steps
===========

Since many things in the game build off of chatrooms, you should look at the documentation on :ref:`Chatrooms Topic`. You should also look at the code for some of the chatrooms and other features included on Tutorial Day, such as ``tutorial_5_coffee.rpy`` and ``tutorial_6_meeting.rpy``, as they have many notes included explaining the various features you will see when you play through those chatrooms.

Once you're comfortable writing and modifying chatrooms, you can look into adding :ref:`Text Messages`, then :ref:`Phone Calls`, and finally :ref:`Emails`. You should also look at :ref:`Setting up a Route` for more information on setting up a full route with plot branches and a party. Good luck!

