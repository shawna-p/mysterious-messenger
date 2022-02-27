# This is the definition for Tutorial Day. It sets up all the chatrooms,
# Story Mode sections, and Story Calls, as well as the plot branches and party.
# If done correctly, the program will take care of unlocking and displaying
# each item to the user and will unlock them in the History.
default tutorial_good_end = ["Good End",
    RouteDay('Tutorial',
        [ChatRoom('Example Chatroom', 'example_chat', '00:01'),
        ChatRoom('Inviting Guests','example_email', '06:11', [z]),
        ChatRoom('Text Message Example', 'example_text', '06:53', [r]),
        StoryCall("Example Story Call", 'example_solo_story_call', '09:30', ja),
        ChatRoom('Timed Menus', 'timed_menus', '11:28', [s]),
        ChatRoom('Other Storytelling Features', 'other_storytelling', '13:44', [y]),
        ChatRoom('Pass Out After Drinking Caffeine Syndrome', 'tutorial_chat', '15:05', [s]),
        ChatRoom('Invite to the meeting', 'popcorn_chat', '18:25', [ja, ju], save_img='ju'),
        StoryMode("Story Mode without Chatrooms", "example_solo_vn", "19:55", z),
        ChatRoom('Hacking', 'hack_example', '20:41', box_bg='secure'),
        ChatRoom('Plot Branches', 'plot_branch_tutorial', '21:44', [], plot_branch=PlotBranch(True)),
        ChatRoom("Onwards!", 'tutorial_end_example', '22:26', [u], box_bg='colorhack'),
        TheParty('tutorial_good_end_party', '23:54')
        ]),
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

default tutorial_bad_end = ["Bad Story End",
    RouteDay('Tutorial',
        [ChatRoom('An Unfinished Task', 'tutorial_bad_end', '23:26', [v])] )]
default tutorial_bre = ["Bad Relationship End",
    RouteDay('Tutorial',
            branch_vn=BranchStoryMode('plot_branch_bre'))]
default tutorial_normal_end = ["Normal End",
    RouteDay('Tutorial',
        [TheParty('plot_branch_normal_end', '23:54')])]

default tutorial_route = Route(
    default_branch=tutorial_good_end,
    branch_list=[tutorial_normal_end,
                    tutorial_bad_end,
                    tutorial_bre],
    route_history_title='Tutorial',
    history_background="Menu Screens/Main Menu/tutorial_day_route_bg.webp")

## If you want further examples on how to define a route, check out
## route_example.rpy to see how the Common Route and Jaehee Route are defined.
