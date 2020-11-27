# Setting up Sequential Chatrooms

_A brief overview of the steps required (more detail below):_

> 1. Define a list of `RouteDay` objects. The first item in the list should be the name of the ending e.g. `"Good End"`
> 2. The first field of a `RouteDay` object is the name of the day (e.g. "1st"), and then the second is a list of `ChatHistory` objects. Fill these out with the information for each chatroom
> 3. Create a `Route` object and fill out its `default_branch` and optionally `branch_list` and `route_history_title` fields.
> 4. Either customize the route select screen, or in [tutorial_0_introduction.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_0_introduction.rpy "tutorial_0_introduction"), change the line `$ new_route_setup(route=tutorial_route)` so that `tutorial_route` is replaced by the variable for the Route object you defined
> 5. Select **Start Over** from the Settings screen to test out your new route

To set up a route, you need to first define a list of `RouteDay` objects. Each `RouteDay` object contains the information the program needs for one in-game Day. Go to [route_setup.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/route_setup.rpy) to see an example definition called `tutorial_good_end`.

At its most basic level, your definition will look as follows:

```renpy
default my_route_good_end = [ "Good End",
    RouteDay("1st"),
    RouteDay("2nd"),
    RouteDay("3rd"),
    # (...)
    RouteDay("Final")]
```

The *first* item in the list should be a string containing the name of the ending as it will appear in the History log. In this example, it is `"Good End"`.

The rest of the items in the list are `RouteDay` objects. They have the following fields:

> RouteDay | `day, archive_list=[], day_icon='day_common2', branch_vn=False` |

Field | Description | Example |
------|-------------|---------|
day | A string containing the name of the day as it should show up in the chatroom timeline (e.g. "1st" appears in-game as "1st Day"). Note that a special icon appears over a day titled "Final". | "1st" |
archive_list | A list of `ChatHistory` objects; see below | `[ChatHistory("Example Chatroom", "example_chat", "00:01")]` |
day_icon | The icon to use for this day in the timeline. Defaults to `'day_common2'`. Previously defined images can be found in [variables.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/variables.rpy "variables.rpy") under the heading **Chat Select Screen** -- `"day_common1"` up to `"day_z"` can be used. | "day_s" |
branch_vn | By default, this is False. Otherwise, it should contain a `VNMode` object. If this route is merged onto the main route during a plot branch, the `VNMode` object stored in `branch_vn` will appear after the chatroom immediately before the plot branch. | `VNMode('plot_branch_bre')` |

## ChatHistory Objects

A `ChatHistory` object contains all the information needed for a single chatroom (plus its accompanying VN mode, phone calls, etc). You will need one `ChatHistory` object for every chatroom in your game.

> ChatHistory | `title, chatroom_label, trigger_time, participants=[], vn_obj=False, plot_branch=False, save_img='auto'` |

The initialization fields are explained below.

Field | Description | Example |
------|-------------|---------|
title | The name of the chatroom as it should show up in the timeline. A string. | "My chatroom title" |
chatroom_label | The name of the label to jump to for this chatroom. This is used for many things, such as phone call labels an VN labels. A string. | "day_1_chatroom_1" |
trigger_time | The time this chatroom should trigger at. A string. This should be written in military time with leading zeroes, e.g. 1:00AM is written "01:00" and 1:38PM is written "13:38" | "05:28" |
participants | Optional. A list of the ChatCharacter objects of the people who should be already present in the chatroom before the player enters. If left blank, no one starts in the chatroom. | [ja, ju] |
vn_obj | Optional. Allows you to better customize the `VNMode` object associated with this chatroom. If not provided, the program will attempt to find appropriately labelled VN labels and create its own `VNMode` object. | `VNMode("my_vn_label", y)` |
plot_branch | A `PlotBranch` object. Indicates if this chatroom should have a VN after it. A `PlotBranch` object only takes one argument -- a boolean telling it whether or not there is a VN that should only be shown after the plot branch has been proceeded through. By default, this is False. | PlotBranch(True) |
save_img | The image that will appear in the save screen on the left when the player saves their game. This is usually an image indicating which route the player is on, if any. Previously defined images can be found in [variables.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/variables.rpy "variables.rpy") under the heading **Save & Load Images**. Note that you do *not* need the prefix "save_", as this is automatically added. It is sufficient to use the character's file_id to get their save image e.g. "seven", "707", and "s" will all get you the same save image, `save_seven`. | "casual" |

If the `ChatHistory` object is not given a `VNMode` object, it will try to find a label with the correct naming scheme instead. However, in the event you want more control over the `vn_obj` field, you can define it yourself.

> VNMode | `vn_label, who=None, party=False, trigger_time=False` |

These fields are explained below.

Field | Description | Example |
------|-------------|---------|
vn_label | The name of the label to jump to for this VN. A string. | "my_vn_label" |
who | The ChatCharacter object of the character who this VN is associated with. Changes the image in the timeline. | `r` |
party | True if this VN is the party, False otherwise. | `True` |
trigger_time | Currently unused. May be used in the future to have VNs independent of chatrooms. | False |

The other thing you may use is a `PlotBranch` object to indicate the existence of a plot branch.

> PlotBranch | `vn_after_branch=False` |

This field is explained below.

Field | Description | Example |
------|-------------|---------|
vn_after_branch | True if the chatroom this is attached to has a VN that should only be seen after the player has proceeded through the plot branch; False otherwise. | True |

A typical `ChatHistory` object, then, might look like the following:

```renpy
ChatHistory("Welcome to the RFA!", "day_1_chatroom_1", "00:05", [s])
```

This defines a `ChatHistory` object whose title is `"Welcome to the RFA!"`. The label you need to put the chatroom in is called `day_1_chatroom_1` (so, somewhere in your program you should have

```renpy
label day_1_chatroom_1:
    call chat_begin('earlyMorn')
```

etc). The chatroom triggers at 00:05, or 12:05 AM. The character `s` starts in the chatroom.

A chatroom with a plot branch following it may look like the following:

```renpy
ChatHistory("Suspicious Happenings...", "day_7_chatroom_8", "19:32", [ja, z], save_img='z', plot_branch=PlotBranch(True))
```

This defines a `ChatHistory` object whose title is `"Suspicious Happenings..."`, found at the label `day_7_chatroom_8`. It triggers at 19:32, or 7:32 PM. The characters `ja` and `z` begin in this chatroom. The save image for this chatroom is `'z'`. There is a plot branch after this chatroom, and a VN associated with this chatroom. This VN should only be shown to the player if they successfully pass the plot branch and continue on the main path (Hence `plot_branch=PlotBranch(True)` rather than just `plot_branch=PlotBranch()`).

All in all, a full route definition may look like the following:

```renpy
default bob_good_end = ["Good End",
    RouteDay('1st',
        [ChatHistory('Welcome!', 'day_1_chatroom_1', '00:01'),
        ChatHistory('Relaxing','day_1_chatroom_2', '09:11', [z, b]),
        ChatHistory('How are you doing?', 'day_1_chatroom_3', '09:53', [r]),
        ChatHistory('Something strange...', 'day_1_chatroom_4', '11:28', [s]),
        ChatHistory('Do you...?', 'day_1_chatroom_5', '15:05', [b]),
        ChatHistory('Kimchi Sandwich', 'day_1_chatroom_6', '18:25', [b, ja]),
        ChatHistory('Very mysterious', 'day_1_chatroom_7', '20:41'),
        ChatHistory('Will you visit?', 'day_1_chatroom_8', '22:44', [b], plot_branch=PlotBranch(True)),
        ChatHistory("Happily Ever After", 'day_1_chatroom_9', '23:26')
        ]),
    RouteDay('2nd', [ChatHistory(...)]),
    RouteDay('3rd', [ChatHistory(...)]),
    RouteDay('4th', [ChatHistory(...)]),
    RouteDay('5th', [ChatHistory(...)]),
    RouteDay('6th', [ChatHistory(...)]),
    RouteDay('7th', [ChatHistory(...)]),
    RouteDay('8th', [ChatHistory(...)]),
    RouteDay('9th', [ChatHistory(...)]),
    RouteDay('10th', [ChatHistory(...)]),
    RouteDay('Final', [ChatHistory(...)])]
```

Note that `[ChatHistory(...)]` is shorthand for a list of many more ChatHistory objects.

## Displaying a Route in the History Screen

In order for the route to show up in the History screen, you also need to define a `Route` object. Do this after you have set up the variables for all the different endings/branches of the route itself.

> Route | `default_branch, branch_list=[], route_history_title="Common", has_end_title=True` |

These fields are explained below.

Field | Description | Example |
------|-------------|---------|
default_branch | The "default" path for this route to take. This should be the longest path from start to finish, and may not necessarily be the "good" end. | `bob_good_end` |
branch_list | A list of all the other paths this route can take. Typically includes all the bad, normal, bad relationship ends, etc. May also be empty, if this route does not branch. | [ bob_bad_end_1, bob_bad_end_2, bob_normal_end ] |
route_history_title | How this route should show up in the History screen e.g. "Bob Route" or "Common Route". "Route" is automatically appended to this title. | "Bob" |
has_end_title | True if this route has a "title" at the beginning of its definition e.g. `default bob_good_end = ["Good End", RouteDay('1st', (...)` has the end title "Good End". If this route has no branching paths, there is no need to label the name of the ending, so this field can be False. | True |

Therefore a Route definition for a special New Year's Eve route with endings for each of the characters as well as a normal ending might look like so:

```renpy
default new_years_route = Route(
    default_branch=new_years_normal_end,
    branch_list=[new_years_ju, new_years_ja,
        new_years_s, new_years_y, new_years_z],
    route_history_title="New Year's"
)
```

You can see some additonal definitions at the bottom of [route_setup.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/route_setup.rpy).

## Accessing your Route In-Game

To play your route, you can either customize the route select screen (see [Customizing the Route Select Screen](Customizing-the-Route-Select-Screen.md)) or change the line `$ new_route_setup(route=tutorial_route)` in [tutorial_0_introduction.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_0_introduction.rpy "tutorial_0_introduction") so that `tutorial_good_end` is replaced by the "default route" of the Route object you defined.

For example, for the "New Year's Route" defined above, you will have a line in your introductory label that has

```renpy
$ new_route_setup(route=new_years_route)
```

### Managing Multiple Routes

If you would like to keep the Tutorial Route (or any other routes with different variables) accessible while you test your new route, you will first need to customize the route select screen (see [Customizing the Route Select Screen](Customizing-the-Route-Select-Screen.md)) to have multiple buttons, one to lead to each route.

For example's sake, the route select screen has buttons to lead to two routes, one called deep_story and one called another_story.

In the introductory label for each story, you may need to re-define the `character_list` and `heart_point_chars` variables so they display the correct characters. An example follows:

```renpy
label deep_route_start:
    $ new_route_setup(route=deep_story_end)
    $ current_chatroom = ChatHistory('Starter Chat', 'deep_story_start', '00:00')
    $ character_list = [ju, z, s, y, ja, m]
    $ heart_point_chars = [ju, z, s, y, ja]
    # Write your introductory chatroom here

# The following label is optional for text messages, voicemail, etc
label after_deep_story_start:
    # Optional things here
    return

label another_story_start:
    $ new_route_setup(route=another_story_end)
    $ current_chatroom = ChatHistory('Starter Chat', 'another_story_start', '00:00')
    $ character_list = [ju, z, s, y, ja, v, r, m]
    $ heart_point_chars = [ju, z, s, y, ja, v, r]
    # Write your introductory chatroom here

# The following label is optional for text messages, voicemail, etc
label after_another_story_start:
    # Optional things here
    return
```

The main difference is that `another_story` includes the characters `r` and `v`, while `deep_route` does not. When the player begins playing the route, explicitly setting `character_list` and `heart_point_chars` ensures the correct profiles are shown on the chat home screen and that the player can see how many heart points they have with the relevant characters.

Similarly, explicitly writing `$ current_chatroom = ChatHistory('Starter Chat', 'deep_story_start', '00:00')` allows you to use the label `after_deep_story_start` to put any text messages, voicemail changes, spaceship thoughts, etc.

## Playing Your Route

To play your new route, re-launch the program and select **Start Over** from the Settings screen, then **Original Story** to test out your new route.
