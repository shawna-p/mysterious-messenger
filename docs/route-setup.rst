====================
Setting up a Route
====================

.. toctree::
    :caption: Navigation

    route-setup

.. note::
    Example files to look at:

    * route_setup.rpy
    * route_example.rpy

    *A brief overview of the steps required (more detail below):*

    #. Define a list of ``RouteDay`` objects. The first item in the list should be the name of the ending e.g. ``"Good End""``.
    #. The first parameter of the RouteDay object is the name of the day e.g. "1st". The second is a list of timeline items. Possible timeline items are:

        #. ChatRoom("title", "label", "trigger_time", [participants])
        #. StoryMode("title", "label", "trigger_time", associated_character)
        #. StoryCall("title", "label", "trigger_time", caller)
        #. TheParty("label", "trigger_time")

    #. Create a ``Route`` object and fill in the information for your new route.
    #. Customize the route select screen to include a button to your new route.
    #. Create a short introduction for your new route.
    #. Select **Start Over** from the settings to test out your new route.


To set up a route and test out your own chatrooms, story mode, phone calls and more in the game, first you need to define a few special variables. The first is a list of ``RouteDay`` objects. Each ``RouteDay`` contains the information the program needs to know for one in-game day.

First, go to ``route_setup.rpy``, where you'll see an example definition called ``tutorial_good_end``.

At its most basic level, your definition will look as follows::

    default my_route_good_end = [ "Good End",
        RouteDay("1st"),
        RouteDay("2nd"),
        RouteDay("3rd"),
        # (...)
        RouteDay("Final")
    ]

The first item in the list should be a string with the name of the ending as it will appear in the History log. In this example, it is ``"Good End"``.

The remaining items in the list are ``RouteDay`` objects. They have the following fields:

`day`
    A string containing the name of the day as it should appear in the timeline.

    e.g. "1st"

    .. tip::
        A RouteDay with the day field as "Final" will have a special icon above it in the timeline screen.

`archive_list`
    Optional, although empty days have no content. A list of timeline items. See below for more.

    e.g. [ChatRoom("Example Chatroom", "example_chat", "00:01")]

`day_icon`
    Optional. A string with the name of the icon to use for this day in the timeline. Defaults to ``"day_common2"``. Existing images can be found in ``variables_editable.rpy`` under the header **DAY SELECT IMAGES**.

    e.g. "day_ju"

`branch_vn`
    Optional. If this day has a Story Mode that should be shown as soon as it's merged onto the main route after a plot branch, then it will be stored here.

    e.g. BranchStoryMode('jaehee_bre2_vn', who=ja)

`save_img`
    Optional. The file path or short form to the save image which should be used for all timeline items on this RouteDay. Existing images can be found in ``variables_editable.rpy`` under the header **SAVE & LOAD IMAGES**.

    e.g. "zen"

`auto_label`
    Optional. A string which is used as the pattern to automatically name all item labels inside this RouteDay's ``archive_list``. Each item in ``archive_list`` with None as its label will be given a label with this prefix + a number in increasing order.

    e.g. 'casual_d3_'


Adding Timeline Items
=====================

The main way you will add content to your route is by filling out a RouteDay's ``archive_list``. There are four main timeline items.

Chatrooms
---------

To add a Chatroom, you will use the ``ChatRoom`` class. It contains all the information the program needs for a single chatroom along with any accompanying phone calls or a story mode section, if applicable. You will need one ``ChatRoom`` object for each chatroom in your route.

A typical chatroom definition looks like the following::

    ChatRoom("Fight over cats", 'casual_d2_example_4', '08:05', [ja, ju])

For this example, the title of the chatroom is "Fight over cats". It can be found at the label ``casual_d2_example_4`` and will appear at 8:05 am. The characters ``ja`` and ``ju`` begin in the chatroom.

There are some additional fields as well, each of which is explained below.

`title`
    The title of the chatroom as it should appear in the timeline. A string.

    e.g. "Yoosung's omelette rice"

`chatroom_label`
    The name of the label the program will jump to in order to play this chatroom. You must define this label yourself. It should be passed to this field as a string.

    e.g. "casual_d2_example_3"

`trigger_time`
    The time this chatroom should appear at. This should be written in military time with leading zeroes, so a time like 1:00 AM becomes "01:00" and 1:38 PM becomes "13:38".

    e.g. "23:42"

`participants`
    Optional. A list of the characters who begin in this chatroom. If this field is ommitted, no one begins in the chatroom. This should be a list of ChatCharacter objects.

    e.g. [ja, ju]

`story_mode`
    Optional. Allows you finer control over the StoryMode object associated with this chatroom. The program will automatically try to find appropriately labelled story mode labels and create its own StoryMode object for this field.

    e.g. StoryMode("", "my_vn_label")

    .. warning::
        It is generally recommended that you let the program take care of defining StoryMode objects by using properly named labels. See [[INSERT LINK HERE]].

`plot_branch`
    Optional. Indicates that there should be a plot branch after this chatroom. See [[INSERT LINK HERE]] for more on plot branches.

    e.g. PlotBranch(True)

`save_img`
    Optional. A string with the name of the save image to use for this particular chatroom. This takes precedent over a save image set by the RouteDay. It is typically an image indicating which route the player is on. The prefix "save_" is automatically added to this field.

    e.g. "casual"

Chatrooms also have "expired" versions. This means that if the player is playing real-time mode and doesn't play this chatroom before the next timeline item appears, it will "expire". The program will look for the expired version of a chatroom under the chatroom's regular label + the suffix ``_expired``. So, if the chatroom is found at

::

    label day_4_5_coffee_chat:

Then the expired label should be located at

::

    label day_4_5_coffee_chat_expired:

Typically, an expired chatroom covers most of the same topics as the original chatroom, though the player is not present. For more on expired chatrooms and real-time mode, see [[INSERT LINK HERE]].


Attached Story Mode
^^^^^^^^^^^^^^^^^^^

Chatrooms can have an attached Story Mode, which becomes available to play after the chatroom has been played. The easiest way to do this is to create a label which follows a specific naming scheme. This will automatically define a StoryMode object for the associated chatroom.

If your chatroom's label is ``casual_day_1_4```, then if you create a label called ``casual_day_1_4_vn`` (note the ``_vn`` suffix), a general StoryMode will be created that will lead to that label.

You can also specify which character should appear on the Story Mode icon in the timeline screen by adding their file_id to the end of the label e.g. ``casual_day_1_4_vn_ja`` would create a Story Mode attached to the chatroom found at ``casual_day_1_4`` which will show Jaehee's image on the icon. Most of the existing characters have an associated Story Mode icon defined for them. You can also define one for a new character: see [[INSERT LINK HERE]] for more.

An attached Story Mode is written the same way as other story mode sections. See [[INSERT LINK HERE]] for more.

Story Mode
----------

To add a **standalone** Story Mode section, you will use the ``StoryMode`` class. It contains all the information the program needs for a single story mode along with any accompanying phone calls, if applicable. You will need one ``StoryMode`` object for each standalone story mode in your route.

A Story Mode definition looks like the following::

    StoryMode("Gone to the store", "extra_day_5_3", "20:16", y, save_img='y', plot_branch=PlotBranch(False))

For this example, the title of the Story Mode is "Gone to the store". It can be found at the label ``extra_day_5_3`` and will appear at 8:16 pm. The story mode icon in the timeline will show Yoosung's story mode image, and if the player saves the game while this is the most recent timeline item, it will show a save icon associated with "y". Additionally, there is a plot branch after this Story Mode. For more on Plot Branches, see [[INSERT LINK HERE]].

There are some additional fields as well, each of which is explained below.

`title`
    The title of the story mode as it should appear in the timeline. A string.

    e.g. "Things that matter"

`vn_label`
    The name of the label the program will jump to in order to play this story mode. You must define this label yourself. It should be passed to this field as a string.

    e.g. "casual_d2_example_3"

`trigger_time`
    The time this story mode should appear at. This should be written in military time with leading zeroes, so a time like 1:00 AM becomes "01:00" and 1:38 PM becomes "13:38".

    e.g. "03:42"

`who`
    Optional. The ChatCharacter this story mode should be associated with. Leaving this out causes the story mode to use a "general" story mode icon on the timeline screen.

    e.g. ja

`plot_branch`
    Optional. Indicates that there should be a plot branch after this story mode. See [[INSERT LINK HERE]] for more on plot branches.

    e.g. PlotBranch(False)

`party`
    True if this Story Mode is the party. In general, you should instead use ``TheParty`` to define the party for your route. See [[INSERT LINK HERE]].

    e.g. False

`save_img`
    Optional. A string with the name of the save image to use for this particular story mode. This takes precedent over a save image set by the RouteDay. It is typically an image indicating which route the player is on. The prefix "save_" is automatically added to this field.

    e.g. "s"



Story Calls
-------------

To add a **standalone** Story Call, you will use the ``StoryCall`` class. It contains all the information the program needs for a single story call along with any accompanying regular phone calls, if applicable. You will need one ``StoryCall`` object for each standalone story call in your route.

A Story Call definition looks like the following::

    StoryCall("Did you hear?", "new_years_3", "16:10", s)


For this example, the title of the Story Call is "Did you hear?". It can be found at the label ``new_years_3`` and will appear at 4:10 pm. The person calling the player is ``s``.

There are some additional fields as well, each of which is explained below.

`title`
    The title of the story call as it should appear in the timeline. A string.

    e.g. "Good morning!"

`phone_label`
    The name of the label the program will jump to in order to play this story call. You must define this label yourself. It should be passed to this field as a string.

    e.g. "new_years_3"

`trigger_time`
    The time this story call should appear at. This should be written in military time with leading zeroes, so a time like 1:00 AM becomes "01:00" and 1:38 PM becomes "13:38".

    e.g. "11:11"

`caller`
    The ChatCharacter object of the character who will be calling the player.

    e.g. r

`plot_branch`
    Optional. Indicates that there should be a plot branch after this story call. See [[INSERT LINK HERE]] for more on plot branches.

    e.g. PlotBranch(False)

`save_img`
    Optional. A string with the name of the save image to use for this particular story call. This takes precedent over a save image set by the RouteDay. It is typically an image indicating which route the player is on. The prefix "save_" is automatically added to this field.

    e.g. "ju"

Story calls, like chatrooms, also have "expired" versions. This means that if the player is playing real-time mode and doesn't play this story call before the next timeline item appears, it will "expire". The program will look for the expired version of a story call under the story call's regular label + the suffix ``_expired``. So, if the story call is found at

::

    label my_first_story_call:

Then the expired label should be located at

::

    label my_first_story_call_expired:

Typically, an expired story call is treated as though the caller phoned the player and left a voicemail. For more on expired story calls and real-time mode, see [[INSERT LINK HERE]].

The Party
-------------

There is a special convenience function intended to help you define a standalone party for a route. It has the following fields:

`vn_label`
    The label the program should jump to to play the party.

    e.g. "emma_route_party"

`trigger_time`
    The time the party should appear at. This should be written in military time with leading zeroes, so a time like 1:00 AM becomes "01:00" and 1:38 PM becomes "13:38".

    e.g. "12:00"

`save_img`
    Optional. A string with the name of the save image to use when this is the most recent timeline item. This takes precedent over a save image set by the RouteDay. It is typically an image indicating which route the player is on. The prefix "save_" is automatically added to this field.

    e.g. "em"

An example may look like::

    TheParty("emma_route_normal_party", "12:00")



Example Route Day
-----------------

An example route day might look like the following::

    RouteDay('1st',
        [ChatRoom('Welcome!', 'day_1_emma_1', '00:01'),
        ChatRoom('Relaxing','day_1_emma_2', '06:11', [z, em]),
        ChatRoom('How are you doing?', 'day_1_emma_3', '09:53', [r]),
        ChatRoom('Something strange...', 'day_1_emma_4', '11:28', [s]),
        StoryMode('Do you...?', 'day_1_emma_5', '15:05', em),
        ChatRoom('Kimchi Sandwich', 'day_1_emma_6', '18:25', [em, ja]),
        ChatRoom('Very mysterious', 'day_1_emma_7', '20:41'),
        StoryCall('Will you visit?', 'day_1_emma_8', '22:44', em,
            plot_branch=PlotBranch(True)),
        ChatRoom("Happily Ever After", 'day_1_emma_9', '23:26')
        ], save_img="em")

A list of RouteDays like this make up a single path on a route::

    default emma_good_end = ["Good End",
        RouteDay('1st',
            [ChatRoom('Welcome!', 'day_1_emma_1', '00:01'),
            ChatRoom('Relaxing','day_1_emma_2', '06:11', [z, em]),
            ChatRoom('How are you doing?', 'day_1_emma_3', '09:53', [r]),
            ChatRoom('Something strange...', 'day_1_emma_4', '11:28', [s]),
            StoryMode('Do you...?', 'day_1_emma_5', '15:05', em),
            ChatRoom('Kimchi Sandwich', 'day_1_emma_6', '18:25', [em, ja]),
            ChatRoom('Very mysterious', 'day_1_emma_7', '20:41'),
            StoryCall('Will you visit?', 'day_1_emma_8', '22:44', em,
                plot_branch=PlotBranch(True)),
            ChatRoom("Happily Ever After", 'day_1_emma_9', '23:26')
            ], save_img="em"),
        RouteDay('2nd', [ChatRoom(...)]),
        RouteDay('3rd', [ChatRoom(...)]),
        RouteDay('4th', [ChatRoom(...)]),
        RouteDay('5th', [ChatRoom(...)]),
        RouteDay('6th', [ChatRoom(...)]),
        RouteDay('7th', [ChatRoom(...)]),
        RouteDay('8th', [ChatRoom(...)]),
        RouteDay('9th', [ChatRoom(...)]),
        RouteDay('10th', [ChatRoom(...)]),
        RouteDay('Final', [ChatRoom(...)])]

Note that ``[ChatRoom(...)]`` is shorthand for a list of many more timeline items.

..tip ::
    The above RouteDay example could also be simplified as::

        RouteDay('1st',
            [ChatRoom('Welcome!', None, '00:01'),
            ChatRoom('Relaxing', None, '06:11', [z, em]),
            ChatRoom('How are you doing?', None, '09:53', [r]),
            ChatRoom('Something strange...', None, '11:28', [s]),
            StoryMode('Do you...?', None, '15:05', em),
            ChatRoom('Kimchi Sandwich', None, '18:25', [em, ja]),
            ChatRoom('Very mysterious', None, '20:41'),
            StoryCall('Will you visit?', None, '22:44', em, plot_branch=PlotBranch(True)),
            ChatRoom("Happily Ever After", None, '23:26')
            ], save_img="em", auto_label="day_1_emma_")

    Note the use of ``None`` instead of a label name, and ``auto_label="day_1_emma_"`` on the RouteDay itself. This will automatically name all the labels inside the RouteDay to be equivalent to the previous example.


Setting up the Route
====================

Now you should have at least one definition of a route path with a list of RouteDay objects. In order for the route to show up in the History screen and be playable, you also need to define a ``Route`` object. Do this after you have defined lists of RouteDay objects for each branching path on your route.

An example Route may look like the following::

    default new_years_route = Route(
        default_branch=new_years_normal_end,
        branch_list=[new_years_ju, new_years_ja,
            new_years_s, new_years_y, new_years_z],
        route_history_title="New Year's",
        history_background="Menu Screens/Main Menu/new_years_route_bg.webp"
    )

This defines a special New Year's Eve Route with endings for five of the characters, as well as a normal ending. Each of the fields is explained below.

`default_branch`
    The "default" path for this route to take. This should generally be the longest path from start to finish, and isn't necessarily the "good" end. It will be the path the player begins on when they start a new game on this route.

    e.g. ``emma_good_end``

`branch_list`
    A list of all the other paths this route can branch onto after a plot branch. These are the variables that hold the RouteDay lists you defined earlier. Typically this includes all the bad, normal, and bad relationship ends, etc. This may also be ``None`` if the route does not branch.

    e.g. ``[emma_bad_end_1, emma_bad_end_2, emma_normal_end]``

`route_history_title`
    The name of this route as it should appear in the History screen e.g. "Emma Route" or "Common Route". The suffix " Route" is automatically appended to this title.

    e.g. "Emma"

`has_end_title`
    True if this route should have a title labelling the ending type over the last timeline item in the History. If the variable you used for ``default_branch`` begins with a title like "Good End" (e.g. ``emma_good_end = ["Good End", RouteDay("1st", [...])]``, then if ``has_end_title`` is True, "Good End" will appear just before the last item on ``emma_good_end``.

    If you don't set this to True/False yourself, the program will automatically set it to True if there is a ``branch_list`` and False otherwise. An example of a time when this variable should be False even with branching paths is seen in ``route_example.rpy`` for Casual Route -- there is no "Casual Route Good End", since successfully completing Casual Route means the player has branched onto a character route. However, there *is* a Casual Route Bad End inside the Route's branch_list.

    e.g. True

`history_background`
    Optional. The path to the image that should be used for this route's background in the History screen. This should be 650x120 px for best results. The corners are automatically cropped to fit the button frame.

    e.g. "Menu Screens/Main Menu/jaehee-route-bg.webp"

Both ``route_setup.rpy`` and ``route_example.rpy`` have definitions of Routes and their associated branching paths so you can get an idea of how routes are defined.


Customizing the Route Select Screen
====================================

Now that you have your route defined, you can customize the route select screen to include a button to your new route. You will need to create a label for your introduction as well. This can be called whatever you like e.g.

::

    label new_years_introduction:

.. warning::
    Even if you don't want an introduction and just want to take the player directly to the home screen, you **must still** create an introduction label. This label includes important instructions to set up the route properly.

See [[INSERT LINK HERE]] for more information on how to write your introduction and set up the route. The important part here is the name of the label, which will be used for the button on the route select screen.

Mysterious Messenger has a special screen called ``custom_route_select_screen``, found inside the file ``screens_custom_route_select.rpy``. Inside the **Developer** settings found on the main menu on on the home screen after loading a game, there is an option called **Use custom route select screen**. Checking this option will cause the game to use the ``custom_route_select_screen`` instead of the default version (which contains buttons for Tutorial Day and Casual Story).

Your custom route select screen should look like the following::

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

You're free to replace the image "Menu Screens/Main Menu/route_select_tutorial.webp" with your own image or leave it out altogether. The important thing is the action on the button, currently ``Start()``. You need to give this the name of the label where it can find your route introduction::

    screen custom_route_select_screen():
        vbox:
            style_prefix 'route_select' # Remove this if you want your own styles
            button:
                ysize 200 # Set the height of the button
                action Start('new_years_introduction')
                # The box with text on the right side of the button
                frame:
                    text "New Year's Story"

Note that the action is now ``Start('new_years_introduction')``, which will start the game at the label ``new_years_introduction``.

Providing Multiple Routes
-------------------------

If you want to provide multiple routes the player can begin on, you will need a button for each route on the route select screen. By default, the buttons on the route select screen are organized inside something called a ``vbox``, which will stack its contents on top of each other vertically. This makes it easy to create multiple buttons.

For example, a version of the route select screen which allows the player to choose between a "Casual" or "Deep" story might look like the following::

    screen custom_route_select_screen():
        vbox:
            style_prefix 'route_select'
            button:
                ysize 210
                add 'Menu Screens/Main Menu/route_select_casual.webp':
                    align (0.08, 0.5)
                action Start('casual_story_start')
                frame:
                    text "Casual Story"
            button:
                ysize 210
                add 'Menu Screens/Main Menu/route_select_deep.webp':
                    align (0.08, 0.5)
                action Start('deep_story_start')
                frame:
                    text "Deep Story"

.. note::
    The image 'Menu Screens/Main Menu/route_select_deep.webp' does not currently exist in the game; you would need to create it yourself.

You're free to change the button backgrounds, text, spacing, and other styles. The above example provides two buttons. The first takes the player to a label called ``casual_story_start``, and the second to a label called ``deep_story_start``.

Unlockable Routes
-----------------

If you want to keep certain routes "locked" until the player has fulfilled a condition of your choosing (e.g. preventing the player from going through Character B's route until after they have completed Character A's route), you need to set up persistent variables to keep track of whether the player has fulfilled your desired condition or not. You can define these variables anywhere you like, though it's a good idea to keep them in a separate ``.rpy`` file for organization. Since this variable affects the route select screen, you could put it in ``screens_custom_route_select.rpy``.

For this example, the program will check whether or not the player has successfully gotten the Good End in Tutorial Day. First, define a variable::

    default persistent.tutorial_good_end_complete = False

``tutorial_good_end_complete`` is the name of your created field in the ``persistent`` object. ``persistent`` is a special class in Ren'Py that is saved across playthroughs. The above statement first initializes this variable to ``False``, and you will set it to ``True`` after the player has successfully gone through the Good End.

The final label that a player will see if they achieved the good end on Tutorial Day is called ``label tutorial_good_end_party`` and can be found in ``tutorial_8_plot_branches.rpy``. The last lines of that label are currently as follows::

    $ ending = 'good'
    return

This ends the route and takes the player back to the menu, so just before the ``return`` statement you can set your new persistent variable to ``True``::

    $ persistent.tutorial_good_end_complete = True
    $ ending = 'good'
    return

.. note::
    You're not limited to putting your variable check right at the end of a route -- you can also put a variable like ``$ persistent.confessed_to_emma = True``, which might happen in the middle of a route and unlock a special Valentine's Day event or something else. Remember that ``persistent`` variables *persist* across multiple playthroughs, so they're best used for events you only want to unlock once.

.. note::
    If you *don't* need the program to remember a variable across different playthroughs (for example, if you want the game to remember you told Emma "I own a cat" so you can later have her mention the cat in a different conversation), you **do  not** need ``persistent`` in front of your variable definition and can simply use a variable like::

        default owns_cat = False
        label emma_route_3_8:
            scene morning
            play music mystic_chat
            em "Hi, [name]!"
            em "I had a question -- do you own a cat?"
            menu:
                "Yes, I have a cat.":
                    $ owns_cat = True
                    em "Cool!"
                "No, I don't.":
                    $ owns_cat = False
                    em "Aw, okay."

    The variable ``owns_cat`` will be set to False whenever the player begins a new game.

Now you can customize the route select screen based on the value of your persistent variable::

    vbox:
        style_prefix 'route_select'
        button:
            ysize 210
            add 'Menu Screens/Main Menu/route_select_tutorial.webp':
                align (0.08, 0.5)
            action Start()
            frame:
                text "Tutorial Day"
        # Casual/Jaehee's route is only available to a player who
        # has completed the Good End on Tutorial Day
        button:
            add 'Menu Screens/Main Menu/route_select_casual.webp':
                align (0.08, 0.5)
            frame:
                if persistent.tutorial_good_end_complete:
                    text "Casual Story"
                else:
                    hbox:
                        align (0.4, 0.5)
                        add 'plot_lock' align (0.5, 0.5)
                        text "Casual Story"
            if persistent.tutorial_good_end_complete:
                action Start('example_casual_start')
            else:
                action CConfirm("This route is locked until you've played through Tutorial Day at least once.")
                hover_foreground None

There are a lot of parts here, so each will be explained separately.

::

    vbox:
        style_prefix 'route_select'
        button:
            ysize 210
            add 'Menu Screens/Main Menu/route_select_tutorial.webp':
                align (0.08, 0.5)
            action Start()
            frame:
                text "Tutorial Day"

This part contains a button for Tutorial Day. There are no conditions on it, so it is always available to the player.

::

    # Casual/Jaehee's route is only available to a player who
    # has completed the Good End on Tutorial Day
    button:
        add 'Menu Screens/Main Menu/route_select_casual.webp':
            align (0.08, 0.5)
        frame:
            if persistent.tutorial_good_end_complete:
                text "Casual Story"
            else:
                hbox:
                    align (0.4, 0.5)
                    add 'plot_lock' align (0.5, 0.5)
                    text "Casual Story"

This makes a button for Casual Story. However, there is a conditional -- ``if persistent.tutorial_good_end_complete``, the variable defined earlier. If this variable is True -- aka the player has seen the Good End on Tutorial Day -- then the button just contains the text "Casual Story". However, if it is false, there is an ``hbox``, which organizes its items side-by-side. This hbox shows a "locked" image next to the text "Casual Story" to indicate that Casual Story is currently locked.

::
    if persistent.tutorial_good_end_complete:
        action Start('example_casual_start')
    else:
        action CConfirm("This route is locked until you've played the Good End on Tutorial Day")
        hover_foreground None

Finally, if the player hasn't gone through the Good End on Tutorial Day, they shouldn't be able to play Casual Story yet, so there is another conditional statement with the action inside it. If the player has seen the Good End, the game will start at the label ``example_casual_start``.

However, if the player *hasn't* seen the Good End, the button will not light up (``hover_foreground None``), and the special action ``CConfirm`` is used. ``CConfirm`` shows a confirmation prompt to the user with the given message. In this case, it tells the player that they cannot access this route until they've played the Good End on Tutorial Day.

You could leave the ``else`` out altogether, which would cause the button to be inactive if the player hasn't played the Good End, but including it helps the player understand why they can't play this route yet and what they have to do to unlock it.
