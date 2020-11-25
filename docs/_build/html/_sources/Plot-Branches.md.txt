# Plot Branches

**Example Files to look at: [tutorial_8_plot_branches.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_8_plot_branches.rpy "tutorial_8_plot_branches"), [route_setup.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/route_setup.rpy)**

A brief overview of the steps required (more detail below): |
------------------------------------------------------------|

> 1. Use the **List of Chatrooms** tab in **Script Generator.xlsx** or refer to [[Setting up Sequential Chatrooms]] to set up your route. In the `ChatHistory` object that contains the chatroom after which you want the plot to branch, either fill in `true` or `false` to the plot branch column in the spreadsheet or ensure you have `plot_branch=PlotBranch()` in your definition.
> 2. Define another list of `RouteDay` objects for the path the player will branch onto.
> 3. After the chatroom with the plot branch, create another label with the chatroom label name + `_branch` e.g. `label my_chatroom_branch`.
> 4. Put whatever criteria you are testing for in this label. You can then either write `$ continue_route()` to have the player continue down the main path of the route, or use `$ merge_routes(my_route_bad_end)` where `my_route_bad_end` is the path you defined in step 2.
> 5. At the end of the label, write `jump plot_branch_end`.

To begin, you need to define a list of `RouteDay` objects for every path you want the user to be able to branch onto. For more on defining route branches, see [[Setting up Sequential Chatrooms]]. If you want the branch to have a title, the first item in the list should be a string like "Bob Good Ending".

To show the plot branch icon in-game, the `ChatHistory` object containing the chatroom before the plot branch must have `plot_branch=PlotBranch()` **or** `plot_branch=PlotBranch(True)`.

If `PlotBranch` receives `True` as an argument, this indicates that the VN that should occur after the chatroom defined in this `ChatHistory` object should *only* appear after the player has proceeded through the plot branch. Otherwise, you do not have to include any arguments for the `PlotBranch()` object.

You will include the `plot_branch` argument after every `ChatHistory` object that has a chatroom you would like to branch after.

## Plot Branches and Visual Novel Sections

If you only want a plot branch to occur *after* the player proceeds through the plot branch, one of two things must be done depending on the situation.

### The VN occurs on the main path

If the plot branch occurs on the "main path" (aka the longest path in the game; likely the one you told the game to use in [[Creating an Opening Chatroom]]), then you simply need to ensure that the corresponding `ChatHistory` object has the argument `plot_branch=PlotBranch(True)`. This will only unlock its corresponding VN after the player has proceeded through the plot branch.

### The VN occurs on a branching path

If the branch you are trying to merge onto the main path has a VN that should appear after the player has proceeded through the plot branch, then the *very first* `RouteDay` object of that route's definition must have the argument `branch_vn=VNMode('branch_label', ja)` where `'branch_label'` is the name of the label for that VN section, and `ja` is an optional argument that tells the program it should use the character `ja`'s image on the VN icon. If not included, the program will simply show a default icon.

In practice, this looks like the following:

```renpy
default bob_bad_end_1 = ["Bad Story End 1",
    RouteDay('7th', [ChatHistory(...),
                     ChatHistory(...),
                     (...)],
             branch_vn=VNMode('bob_bad_story_end_1', b))]
```

In [route_setup.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/route_setup.rpy) you can see an example of this in the definition for `tutorial_bre`.

## Determining Which Route to Branch To

You need a way of telling the program which branching path to put the player on once they decide to go through the plot branch. You will tell the program what to do in the a label with the suffix `'_branch'`. So, if your chatroom is called

```renpy
label my_chatroom:
```

then you will create a branch label

```renpy
label my_chatroom_branch:
```

In [tutorial_8_plot_branches.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_8_plot_branches.rpy "tutorial_8_plot_branches") there are many examples of functions under the label `plot_branch_tutorial_branch` that you might want to use to determine which route the player branches onto.

To change which route the player is on, you will either use the function call

```renpy
$ continue_route()
```

which simply allows the player to continue along the "main" path, or you will use the function call

```renpy
$ merge_routes(bob_route)
```

where `bob_route` is the name of the variable where you defined the route you want the player to branch onto.

Finally, end the '_branch' label with

```renpy
jump plot_branch_end
```
