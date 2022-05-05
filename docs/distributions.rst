==============
Distributions
==============

If you would like to package up the engine to distribute to personal acquaintances, there are some options for developers that you may want to turn off or modify.

In ``variables_editable.rpy``, there is a section near the top with the header ``## FOR RELEASE``. Here, several values are set before the game starts.

`persistent.testing_mode`
    Typically, for a release, this should be False. This variable toggles on some options which are useful for testing, such as allowing you to skip to the end of a chatroom, and also makes it so that chatrooms can be endlessly replayed and never expire.

`persistent.unlock_all_story`
    Similarly, this should usually be False for a release. It removes restrictions on play order of chats and unlocks all story items from the beginning of the game.

`persistent.receive_hg`
    If True, then players can randomly receive hourglasses in chatrooms. If False, then they will not receive hourglasses. In most cases this will be True.

`persistent.available_call_indicator`
    This adds an online indicator next to characters when they are available for a phone call. Setting this to True or False is up to developer preference.

`persistent.link_wait_pause`
    When the chat stops (usually to wait for the player to press a link message), by default the footer directs the player to click the link to proceed (This message can be customized). If ``persistent.link_wait_pause`` is True, then it will instead show the pause button footer at the bottom of the screen. In most cases you should leave this as False to improve usability.

`persistent.custom_route_select`
    If False, the game will use the default route select screen, which has options to play Tutorial Day or a basic Casual Story route. In most cases, you will have a custom route select screen that leads to your own route, and so this variable should be True.

`persistent.real_time`
    If True, the game will wait in real-time to unlock story items like chats and phone calls. If False, completing a story item will unlock the next one in sequence. You may also want to provide a toggle for the player to turn this on and off as they like. **If you provide a toggle, you MUST remove this line**, otherwise you will reset the player's preference on every launch of the program.


Additional Considerations
==========================

When distributing a version of Mysterious Messenger, you may want to ensure that save files for your copy don't conflict with the main engine. To do this, you must change the save directory.

In ``options.rpy`` you will find the line::

    define config.save_directory = "MysteriousMessenger-1520899129"

You should change this to have a new name for your own version, e.g.

::

    define config.save_directory = "MyMysteriousMessenger-1591663287"

You may also wish to repurpose the "Developer" buttons on both the main menu and the home screen.

Splash Screen
--------------

If you would like to change the splash screen that displays before the player begins the game, you can go to ``screens_splash.rpy`` and change ``persistent.main_menu_image`` to the image you would like to use for the splash screen image. Note that you will need to clear your persistent data to see