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

To begin, you need a list of ``RouteDay`` objects for every path you want the user to be able to branch onto. For more on defining routes, see [[INSERT LINK HERE]]. If you want this branch to have a title, the first entry in the list should be a string like "Emma Good End".

This example will demonstrate a New Year's Eve route with branching paths for the different characters. The New Year's Eve Route is shown below::

    default new_years_route = Route(
        default_branch=new_years_normal_end,
        branch_list=[new_years_ju, new_years_ja,
            new_years_s, new_years_y, new_years_z],
        route_history_title="New Year's",
        history_background="Menu Screens/Main Menu/new_years_route_bg.webp"
    )

This example will focus on the definitions of two of the paths, the default branch ``new_years_normal_end`` and ``new_years_ju``.

The default branch of the route is defined as below.

::

    default new_years_normal_end = [ "Normal End",
        RouteDay("31st",
            [ChatRoom("The end of another year...", None, '00:30', [ja, ju, s, y, z]),
            ChatRoom("Resolutions", None, '06:43', [ja]),
            StoryMode("At the office", None, '09:44', ju),
            ChatRoom("A celebration?", None, '12:12', [y, z]),
            StoryCall("Endings and beginnings", None, '15:29', s),
            ChatRoom("Cats and chats", None, '18:13', [s, ju], plot_branch=PlotBranch(True)),
            ChatRoom("Too busy...", None, '17:50')
            ], auto_label='new_years_t'
        )
    ]

The plot branch will appear after the chatroom titled "Cats and chats". A PlotBranch object takes one field:

`branch_story_mode`
    If True, if the player proceeds through this plot branch and remains on this route, a Story Mode should appear after this item's chatroom.

    This is *only* applicable if the associated timeline item is a ChatRoom, as it is the only timeline item which may have an attached story mode.




