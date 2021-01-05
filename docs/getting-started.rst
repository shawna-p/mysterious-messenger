================
Getting Started
================

.. toctree::
    :caption: Navigation

    getting-started


Welcome to Mysterious Messenger! There are a lot of features to try out and different ways to use the program. This page will walk you through the steps to set up Mysterious Messenger and begin using it, as well as explaining some of the available features and what you can create with this program.

Setting Up
============

* If you want to run this code, you will need to download the Ren'Py engine: https://www.renpy.org/
* As of 2021-01-05 (the time of this update) the version of Ren'Py used is 7.3.5.606. An update to support version 7.4.x is upcoming.
* Download or clone the `most recent release <https://github.com/shawna-p/mysterious-messenger/releases>`_ into your Ren'Py Projects Directory and unzip it into its own folder. If you don't know what it is, you can change it from the Ren'Py launcher via ``preferences -> Projects Directory``.

  * The current stable version is v2.2.
  * v3.0 is currently in prerelease, with a planned full release Jan/Feb 2021

* Refresh your Projects list and you should see ``mysterious-messenger`` listed
* Save the Script Generator spreadsheet somewhere you can find it later
* Join the `Mysterious Messenger Discord <https://discord.gg/BPbPcpk>`_ for update announcements and help with the program.
* **The images and sound files used in this project are not included in the repository. Please contact me directly if you would like to request the assets for personal use.**

Getting the Program Running
============================

If you've set up everything properly, from the Ren'Py Launcher you should be able to select the project you created from the column on the left and hit 'Launch Project'. If you don't have the images/sound files, you will likely run into several "not found" errors until you've created your own replacements; otherwise, you should be able to go ahead and type in your desired name for the protagonist and check out the "Tutorial Day", which will walk you through some of the available features in the program.


Useful Built-in Features
==========================

Besides just modifying the code, the program has some extra features built into the Settings screen specific to this program. Many are useful when creating new content.

Accessibility Options
----------------------

On the **Preferences** screen there are several toggles under the header Accessibility Options. These are explained below:

`Hacking Effect`
    Turns on/off the various flashing and glitchy "hacked" animations in the program.

`Screen Shake`
    Turns screen shake on/off.

`Chatroom Banners`
    Turns on/off animation for banners during chatrooms.

`Timed Menus`
    If turned off, Timed Menus will function like regular menus, with the chat stopping to show the player an Answer button before proceeding.

    Also see the **Timed Menu Speed** slider, explained below.

`Animated Icons`
    Turns heart icon and hourglass animations into small text notifications. Note that you can also choose not to award hourglasses in the chatroom at all by unchecking **Receive Hourglasses in Chatrooms** in the Developer settings.

`Dialogue Outlines`
    Adds outlines to fonts during Story Mode, phone calls, and chatrooms to make them more readable.

Under the header **Other Settings** are a few additional sliders and options:

`Timed Menu Speed`
    If Timed Menus are turned on, this slider will adjust the amount of time the player is given to answer a timed menu. Moving this slider to the left will make messages post slowly, giving the player time to read them and decide on an answer before the timer runs out, and moving the slider to the right will cause messages to post very quickly, resulting in a shorter timer.

    By default, this is set to the equivalent of chat SPEED 5. The value of this slider is not affected by how fast your chatroom speed is -- you could have the chatroom regularly operate at SPEED 9 but timed menus slow the chat speed down to approximately SPEED 4 until the player either chooses an answer or the timer runs out.

    This has no effect if timed menu are turned off.

`VN Window Opacity`
    Adjusts the opacity of the dialogue window during Story Mode (VN) sections of the game. If the slider is all the way to the left, the dialogue window will be completely transparent. Putting the slider all the way to the right will make the dialogue window completely opaque. This can be used in combination with **Dialogue Outlines** to make text easier to read.

`Background Contrast`
    Adjusts the opacity of the starry night background used in most menu screens. Dragging the slider all the way to the right makes the background completely black.

Finally, under the **Sound** tab in the Settings is an option for audio captions.

`Audio Captions`
    If checked, the program will display a notification describing background music and sound effects briefly when the sound is first played.


Dialogue Settings
------------------

There are several options which affect dialogue display on the **Preferences** tab:

`Text Speed`
    Affects how fast the text displays during Story Mode and phone calls. By default, the slider is all the way to the right, which means dialogue shows up instantly. Moving the slider farther to the right decreases the number of characters per second (CPS) that are shown, so dialogue will show up character-by-character instead of all at once.

`Auto-Forward Time`
    This program includes an "Auto" feature for Story Mode as well as phone calls. Setting this slider farther to the right results in a shorter delay between showing new lines of dialogue, and setting it farther to the left gives you more time to read dialogue before the program moves on to the next line.

`Skip Unseen Text`
    By default, this option is checked. If unchecked, the program will stop skipping/stop Max Speed when it comes across text you've never seen before. The program remembers which text you have seen across playthroughs.

`Skip After Choices`
    By default, this option is checked. If unchecked, the program will stop Max Speed/skipping after you make a choice, and you will need to press the Skip/Max Speed button again to resume skipping after a choice.

`Skip Transitions`
    If checked, this causes the program to not show transitions when skipping.

`Indicate Past Choices`
    If checked, the program will display a small checkmark in the corner of choices you've picked during past playthroughs.

Other Settings
---------------

`Modified UI`
    If checked, the program will change some of the UI elements in the game to be more consistent with the turquoise and black colour scheme found elsewhere in the game. It also includes some subtle animation for the choice screens. Does not affect gameplay in any way.

`Animated Backgrounds`
    If checked, the chatroom background will be animated. This often includes features such as gently drifting clouds or twinkling stars. The animations take 2-3 minutes to play out fully and then loop for the rest of the chatroom.


Developer Settings
-------------------

Finally, there are several settings which are helpful when testing a route. They can be found both on the main menu and on the in-game home screen under the button labelled **Developer**.

`Testing Mode`
    When Testing Mode is turned on, you will have access to several useful features and conveniences:

    * Shows a button to instantly end a chatroom and mark it as played
    * Allows you to right-click any timeline item to instantly mark it as played
    * Removes several confirm-style messages (such as showing you how many missed calls and unread messages you have when loading a game, or asking for confirmation when proceeding through a plot branch)
    * Unlocks all available profile pictures for both the player and the characters
    * Delivers any outstanding email replies after proceeding through a single timeline item
    * Allows you to replay timeline items (such as chatrooms) multiple times and choose different options (otherwise, re-entering a played chatroom would just show a replay of the original conversation)

        * Any content in the ``after_`` label of a timeline item is also delivered each time you play the chatroom (rather than only the first time)

`Unlock all story`
    When checked, this option will make all timeline items available to play instantly, rather than having to play each item sequentially from beginning to end. This may result in failed plot branch checks, as available timeline items are not marked as played unless you've actually gone through them, but you are allowed to proceed through a plot branch at any time.

    To get around this, you can include a check for `if persistent.unlock_all_story` in your plot branch label to branch the story differently when this option is checked.

`Real-Time Mode`
    By default, this is unchecked. Timeline items will appear sequentially one after the other after the previous item is played. However, if Real-Time Mode is checked off, then chatrooms and other content will appear at the scheduled time in real-time.

`Hacked Effect`
    This turns on/off the messenger "hacked" effects. This particular variable only affects the save file it is activated from. It causes the timeline items to appear "glitchy" and changes the music on the main menu screen. Some of these glitch effects will not appear for players with the **Hacking Effect** option turned off.

`Receive Hourglasses in Chatrooms`
    Unchecking this option will stop awarding the player hourglasses during chatrooms. Currently hourglasses are awarded on a pseudo-random basis when a character posts a special speech bubble from a subset of special bubbles. This option is useful if the chatroom is intended to be seen as a video and not played through, for example.

`Use custom route select screen`
    Checking this option will cause the program to use the screen titled ``custom_route_select_screen`` instead of ``route_select_screen`` when the player chooses a route at the start of the game. See [[INSERT LINK HERE]] for more.

`Fix persistent`
    This is an option primarily intended for users updating Mysterious Messenger from older (<2.0) versions to fix issues with saved persistent values. If Ren'Py is complaining about compatibility issues with persistent variables, you can try using this option to fix it.
