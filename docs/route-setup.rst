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
    Optional. A string with the name of the save image to use for this particular chatroom. This takes precedent over a save image set by the RouteDay. It is typically an image indicating which route the player is on. The prefix 'save_' is automatically added to this field.

    e.g. "casual"

Attached Story Mode
^^^^^^^^^^^^^^^^^^^

Chatrooms can have an attached Story Mode. The easiest way to do this is to simply