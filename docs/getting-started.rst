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
* As of 2022-08-20 (the time of this update) the version of Ren'Py used is 8.0.2. Mysterious Messenger is also intended to be compatible with 7.5+, though it's recommended you use v8.0+ to take advantage of Python 3's capabilities.
* Download or clone the `most recent release <https://github.com/shawna-p/mysterious-messenger/releases>`_ into your Ren'Py Projects Directory and unzip it into its own folder. If you don't know what it is, you can change it from the Ren'Py launcher via ``preferences -> Projects Directory``.

  * The current stable version is 3.2.0

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
    This turns on/off the messenger "hacked" effects. This particular variable only affects the save file it is activated from, so it is not available to toggle from the main menu (only the in-game developer menu). It causes the timeline items to appear "glitchy" and changes the music on the main menu screen. Some of these glitch effects will not appear for players with the **Hacking Effect** option turned off.

`Receive Hourglasses in Chatrooms`
    Unchecking this option will stop awarding the player hourglasses during chatrooms. Currently hourglasses are awarded on a pseudo-random basis when a character posts a special speech bubble from a subset of special bubbles. This option is useful if the chatroom is intended to be seen as a video and not played through, for example.

`Use custom route select screen`
    Checking this option will cause the program to use the screen titled ``custom_route_select_screen`` instead of ``route_select_screen`` when the player chooses a route at the start of the game. See :ref:`Customizing the Route Select Screen` for more.

`Prefer local documentation`
    Checking this will cause the script error popup links to open the locally-saved html documentation that comes with the repository, where possible. If a file cannot be found, it will be opened in a web browser instead. This can be useful if you are working offline.

`Use pause footer for links`
    This will use the pause footer at the bottom of the screen while waiting for the player to click a link in the chatroom. By default, the game shows a customizable message that tells the player to click the link. See :ref:`Stopping the Chat` for more information.

`Fix persistent`
    This is an option primarily intended for users updating Mysterious Messenger from older (<2.0) versions to fix issues with saved persistent values. If Ren'Py is complaining about compatibility issues with persistent variables, you can try using this option to fix it.

`Documentation`
    Clicking this will open the documentation home page for Mysterious Messenger. By default, this opens the documentation in a web browser. However, you can check off **Prefer local documentation** (above) to open the html files that come with the repository instead. Both the online and offline versions contain the same information.

`Reset Albums`
    This will cause the program to forget all persistent variables associated with albums. This includes all the persistent albums as defined in the ``all_albums`` variable, and will also clear the program's memory of images the player has been shown in-game (typically this will only affect CG images shown during Story Mode). Use this if you want to reset the persistent albums to their original, defaulted value.

    This option is only available on the main menu (not in-game).

`Chatroom Creator`
    This will open a sub-menu to create a new chat or load an existing one. You can use the chatroom creator to visually put together chatrooms and then watch them play out in-game or export them as code to put into the program.

Updates
--------

By default, Mysterious Messenger will check for updates to the program once a day. You can customize this in several ways by clicking the update icon in the bottom-right corner of the main menu.

`Check for updates (once per day)`
    Unchecking this will stop the program from automatically checking for updates. You can still manually check for them with the **Check for updates** button.

`Check for prereleases`
    Checking this will include prereleases when the program checks for updates, and will inform the player if a recent prerelease is available. Unchecking this will cause updates to only search for complete releases.

`Ignored releases`
    Whenever the program finds a release you haven't updated to yet, you'll get the option to ignore it. Ignoring a release means that you won't receive any more popups informing you of this particular update version. If you've ignored any versions, they will appear listed under the **Check for prereleases** option. You can uncheck any of these releases to stop ignoring them.

`Check for updates`
    Clicking this button will cause the program to manually check for any updates that fit the conditions you've specified above. You will receive a popup if it finds a new version you can update to.

.. note::
    Mysterious Messenger requires an internet connection to check for updates. If it cannot connect to the internet and automatic updates are turned on, it will simply silently fail to fetch them (with no adverse effects to the rest of the program).

If Mysterious Messenger finds an update for you, you will see information such as the version number, publish date, whether or not it's a prerelease, and a download link for the new code files. You can also choose to ignore this release. Your current program version will be displayed in the bottom-left corner of the popup.



Uncategorized
---------------

This section is for tips or program features that don't have a particular category, but may be useful to players.

* The space bar will activate most of the main buttons in a chatroom. It will switch between play/pause, click the Answer button when it is available, activate the Save & Close button, and click "Sign" on the signature screen.
* The left/right keyboard keys will decrease/increase the chat speed during a chatroom.
* You can swipe photos in a CG album to view the next or previous image without returning to the selection screen. It will automatically skip locked photos.
* You can see the heart points you've earned with each character on your character's profile screen
* If you are on Windows, there is a file called ``file_picker.exe`` which is included in the assets. This will allow the game to display a file picker and let the player choose an image from their computer to use as a profile picture. It does not currently work for other platforms.

Program Features
=================

Finally, below is an overview of the various features available within Mysterious Messenger:

* Fully-featured chatrooms

    * Banners, emojis, screen shake
    * "Hacked" effects (e.g. screen tear)
    * Special fonts and bubbles
    * Animated chatroom backgrounds (optional; activated in settings)
    * Heart icons
    * Optional timed menus
    * Messages with clickable links
    * Create-a-chatroom feature to visually put together chatrooms and watch them play out in-game or export them as code to use in the program

* Phone calls

    * Calls can become available after each timeline item for the player to call the characters
        * The dialogue can change depending on whether the player is calling back a missed phone call or not
    * Characters can call the player
    * Story Calls, which are a mandatory part of the story on the timeline
    * Voicemail for when a character doesn't pick up
    * Special callbacks that trigger when the player hangs up in the middle of a call

* Text messages

    * Characters can send text messages after any timeline item
    * Schedule text messages to deliver at a particular time, or a time relative to other timeline items
    * Send emojis and CGs through text
    * Have text message conversations play out in real-time like a one-on-one chatroom
    * Create text message backlog before a route begins

* Story Mode (VN)

    * Includes all the main characters' outfits and expressions
    * Jump to Story Mode in the middle of a chatroom for flexible storytelling opportunities

* Emails

    * Automatically unlock guests in the guestbook when you first invite them and when they attend the party
    * Flexible email chains of any length
    * Allows for "recovery" emails where the player made the wrong choice but can continue to email the guest to improve their chances of attending
    * Successfully invited guests are showcased before the party
    * Receive an hourglass for viewing a character in the guestbook for the first time

* Routes

    * Set up plot branches during the story or when the player enters the party
    * Mix and match chatrooms, standalone story mode, and story calls
    * Include different Good/Bad/Normal ends (or your own kind of end!)
    * Previously played story is automatically unlocked in the History screen

* Other features

    * Unlock CG images for a character's album
    * Profile picture callbacks to have the characters react to the player's profile picture choices
    * Spaceship thoughts and occasional prizes from the Honey Buddha chip bag
    * Customizable pronouns (she/her, he/him, they/them) and gender (male/female/nonbinary)
    * Select a chatroom username separate from your regular name
    * Custom ringtones
    * Character greetings on the main menu
    * Real-time and sequential mode
    * Get input from the player for more detailed information
    * Support for multiple screen sizes
    * Custom splash screen




