====================
Plot Branches
====================

.. toctree::
    :caption: Navigation

    plot-branches

.. note::
    Example files to look at:

    * route_setup.rpy
    * route_example.rpy
    * tutorial_8_plot_branches.rpy

    *A brief overview of the steps required (more detail below):*

    #. In your list of RouteDay objects, add ``plot_branch=PlotBranch(False)`` or ``plot_branch=PlotBranch(True)`` as a parameter to the timeline item you want the plot branch to appear on.
    #. Define another list of ``RouteDay`` objects for the path the player will branch onto. This should begin on the same RouteDay as the plot branch.
    #. After the timeline item with the plot branch, create another label with the item label + the suffix ``_branch`` e.g. ``label casual_day_4_10_branch``
    #. Fill out your criteria for branching. You can then either write ``$ continue_route()`` to have the player continue down the current path, or use ``$ merge_routes(my_route_normal_end)`` where ``my_route_normal_end`` is the path you defined in Step 2.
    #. ``return`` at the end of the plot branch label.

To begin, you need a list of ``RouteDay`` objects for every path you want the user to be able to branch onto. For more on defining routes, see :ref:`Setting up a Route`. If you want this branch to have a title, the first entry in the list should be a string like "Emma Good End".

This example will demonstrate a New Year's Eve route with branching paths for the different characters. The New Year's Eve Route is shown below::

    default new_years_route = Route(
        default_branch=new_years_normal_end,
        branch_list=[new_years_ju, new_years_ja,
            new_years_s, new_years_y, new_years_z],
        route_history_title="New Year's",
        history_background="Menu Screens/Main Menu/new_years_route_bg.webp"
    )

This example will focus on the definitions of three of the paths, the default branch ``new_years_normal_end``, and the branches ``new_years_ju``, and ``new_years_z``.

The default branch of the route is defined as below.

::

    default new_years_normal_end = [ "Normal End",
        RouteDay("31st",
            [ChatRoom("The end of another year...", None, '00:30', [ja, ju, s, y, z]), # 1
            ChatRoom("Resolutions", None, '06:43', [ja]), # 2
            StoryMode("At the office", None, '09:44', ju), # 3
            ChatRoom("A celebration?", None, '12:12', [y, z]), # 4
            StoryCall("Endings and beginnings", None, '15:29', s), # 5
            ChatRoom("Cats and chats", None, '18:13', [s, ju], plot_branch=PlotBranch(True)), # 6
            ChatRoom("Too busy...", None, '17:50') # 7
            ], auto_label='new_years_t'
        )
    ]

The plot branch will appear after the chatroom titled "Cats and chats". A PlotBranch object takes one field:

`branch_story_mode`
    If True, if the player proceeds through this plot branch and remains on this route, an attached Story Mode should appear after this item's chatroom.

    This is *only* applicable if the associated timeline item is a ChatRoom, as it is the only timeline item which may have an attached story mode.

    By default, this field is False.

Because this plot branch has a ``branch_story_mode``, there must be an associated Story Mode with the "Cats and chats" chatroom. The automatic labelling means that "Cats and chats" is found at ``new_years_t6``, so it should have a corresponding Story Mode at a label like ``new_years_t6_vn`` (optionally with a character's file_id as the suffix to associate this Story Mode with that character). This Story Mode will only appear if the player proceeds through the plot branch and remains on the Normal End.

Next, you must define the other paths for the route, in this case, ``new_years_ju`` and ``new_years_z``::

    default new_years_ju = [ "Jumin New Year's End",
        RouteDay("31st",
            [StoryMode("Visiting the penthouse", 'jumin_ny_end', '18:00', ju)],
            save_img='ju', day_icon='ju')
    ]

    default new_years_z = [ "Zen New Year's End",
        RouteDay("31st",
            [StoryMode("A special visit", 'zen_ny_end', "18:00", z)],
            save_img='z', day_icon='z',
            branch_vn=BranchStoryMode('zen_ny_branch_vn', z)
    ]

Note that the RouteDay is named the same as the RouteDay on the day with the plot branch -- namely, "31st". This tells the program that the timeline items on this RouteDay should be merged onto "31st Day" on the main route.

For the ``new_year_z`` definition, there is a special field called ``branch_vn`` on the RouteDay:

`branch_vn`
    If given, an attached StoryMode will be created with the provided label (and optionally the provided character image). If the player merges onto this path after a plot branch, the chatroom which had the plot branch will have this Story Mode attached to it.

    e.g. BranchStoryMode("example_jaehee_be1_vn")

A BranchStoryMode is a special convenience function to create an attached StoryMode for a plot branch. It has two fields:

`vn_label`
    The label that this StoryMode is found at.

    e.g. "example_jaehee_be2_vn"

`who`
    Optional. The character whose image should be shown on the icon for this StoryMode in the timeline.

    e.g. ja



Determining Which Path to Branch To
====================================

Now that the paths are all set up, you need to create a special label which will tell the program which path to branch onto when the player proceeds through the plot branch. This is the name of the label after which the plot branch occurs + ``_branch``. So, for the New Year's route, the automatic labelling puts the plot branch at the label ``new_years_t6``. That means you will create the label::

    label new_years_t6_branch:

Inside this label, you need to create a conditional statement to tell the program how to proceed. There are many examples in ``tutorial_8_plot_branches.rpy`` as well as ``route_example.rpy``.

The two main ways to branch are ``continue_route`` and ``merge_routes``. If the player should continue on the same path they're currently on (so, for the example, if they should continue on to the Normal End), then use ``$ continue_route()`` under your conditional statement.

On the other hand, if the player should be moved onto a separate route, then you need to use ``$ merge_routes(new_year_z)`` where ``new_year_z`` is the path the player should branch onto.

For the New Year's route, the branch label may look like the following::

    label new_years_t6_branch:
        # First, check if z or ju have more heart points
        if z.heart_points >= 10 and z.heart_points > ju.heart_points:
            $ merge_routes(new_year_z)
        elif ju.heart_points >= 10:
            $ merge_routes(new_year_ju)
        # Otherwise, the player doesn't have enough heart points with
        # either character, so they get the Normal End
        else:
            $ continue_route()

        return

This checks first if the player has at least 10 heart points with Zen, and then also if they have more points with Zen than with Jumin. If so, the player get's Zen's route.

Otherwise (``elif``), the program checks if the player has at least 10 heart points with Jumin. If so, they get Jumin's route. Because of how the previous conditional was set up, if the player has the same number of points with Zen *and* Jumin, they will get Jumin's ending.

Finally, if the player doesn't have enough points with either character, they will get the Normal End (by continuing down the current path).

.. tip::
    If the plot branch label returns without running either ``continue_route`` or ``merge_routes``, ``continue_route`` will be run automatically and the player will continue down the current route.


Branching on the Party
======================

You may also want to cause a branch to occur when the player clicks to enter the party, for example, to check how many guests are attending so that the player can branch onto either the Good End or the Normal End, as appropriate. This does not require any additional code in the route definition. So long as your timeline item is marked as the party -- either via using ``TheParty`` to define it, using something like ``StoryMode("The Party", "my_party_label", "12:00", party=True)``, or calling your attached Story Mode something like ``my_timeline_label_party`` (with the suffix ``_party``) -- then the program will automatically search for a branch label.

The branch label is searched for with the suffix ``_branch``, so, if your party is found at the label ``emma_route_good_party``, then the program will execute the label ``emma_route_good_party_branch`` before the player plays the party.

You can use this branch label as you would with any other branch label; however, if you ``merge_routes``, the path which is being merged onto the main route will need to have a party on it that will be swapped out for the current party. e.g.

::

    default emma_normal_end = [ "Normal End",
        RouteDay("Final", [TheParty('emma_route_normal_end', '12:00')])
    ]

When the player clicks on the party, the program will check if there is a branch label. If so, it will execute the code in the branch label, which may involve merging onto a new path. If the player is merged onto a new path, they will go to the party label found on the merged route.


Plot Branch Examples
======================

Checking for Participation
--------------------------

You can check the percentage of timeline items the player has actively participated in (aka that haven't expired) with a special function::

    if participated_percentage(1, 4) > 32:

This checks if the percentage of chatrooms the player has participated in across days 1-4 is over 32%. Note that ``4`` in this case does not necessarily correspond to "4th Day"; since you may name your days whatever you please. If your route is defined like::

    default my_route = [
        RouteDay("25th"),
        RouteDay("31st"),
        RouteDay("45th"),
        RouteDay("62nd")
    ]

Then ``participated_percentage(1, 4)`` would be checking for the participation on the "25th" (1) day through to the "62nd" (4) day. This number is *inclusive*; aka ``participated_percentage(1, 4)`` will total the number of timeline items found on the 25th/31st/45th/62nd days vs the number of timeline items participated in on those days and return that fraction as a whole number percentage (rounded down).

If you want to check for participation on a single day, you must pass it the same number for both the "first" and "last" days. For example, if you wanted to check for participation on just the "31st" day (from the above example), since it is the 2nd item in the list you would check::

    if participated_percentage(2, 2) > 32:

If you want to check the participation from a particular day all the way to the end of the route, you can leave the second field blank e.g.

::

    if participated_percentage(5) > 32:

.. note::
    ``participated_percentage`` only returns the proportion of participated timeline items vs *available* timeline items for a particular time range.

    So, if you have 12 timeline items on the "6th" day and the plot branch is after the second item, if you calculate participation percentage on the "6th" day, the program will ignore the 10 timeline items which aren't available. That means that if the player played the item just before the plot branch but missed the first item, they will have a 50% participation percentage that day since only 2/12 items were available and the player participated in 1/2 (50%) of those items.

Checking for Guest Attendance
------------------------------

You may also want to check how many guests are attending the party to determine which path to branch the player onto. The function ``attending_guests()`` returns the number of guests who will be attending the party at the time the function is called::

    if attending_guests() >= 10:
        $ merge_routes(my_route_good_end)
    else:
        $ merge_routes(my_route_normal_end)

This is best used for the plot branch when clicking the party (see :ref:`Branching on the Party`). You can also check if individual guests are attending the party; see :ref:`Checking in-game if a Guest Will Attend`.

Comparing Heart Points:
-----------------------

Typically, the easiest way to compare heart points between characters is to check with::

    if s.heart_points > ju.heart_points:
        $ merge_routes(seven_route)
    else:
        $ merge_routes(ju_route)

However, if you have a complex plot branch in which you want to compare several characters' heart points, you may find the following functions useful::

    $ sorted_heart_points = sorted(heart_point_chars,
        key=lambda c: c.good_heart, reverse=True)
    # sorted_heart_points now contains a list of the heart_point_chars, sorted
    # in descending order from most heart points to least

    # who is now equal to the character who has the most heart points
    $ who = sorted_heart_points[0]

    # First, check if the character with the most heart points has at least
    # 10 total heart points
    if who.heart_points < 10:
        # They don't have 10 heart points; continue down the Normal End
        $ continue_route()
    elif who == ja:
        $ merge_routes(new_year_ja)
    elif who == ju:
        $ merge_routes(new_year_ju)
    elif who == s:
        $ merge_routes(new_year_s)
    elif who == y:
        $ merge_routes(new_year_y)
    elif who == z:
        $ merge_routes(new_year_z)

    return

The sorted list saves you from writing out lengthy comparison statements such as::

    if ja.heart_points > 10 and ja.heart_points > ju.heart_points and ja.heart_points > s.heart_points and...





