           
# This archive will store every chatroom in the game. If done correctly,
# the program will automatically set variables and make chatrooms available
# for you
default chat_archive = []



default tutorial_good_end = ["Good End",
    RouteDay('Tutorial', 
        [ChatHistory('Example Chatroom', 'example_chat', '00:01'),                                     
        ChatHistory('Inviting Guests','example_email', '09:11', [z]),
        ChatHistory('Text Message Example', 'example_text', '09:53', [r], VNMode('vn_mode_tutorial', r)),
        ChatHistory('Timed Menus', 'timed_menus', '11:28', [s]),
        ChatHistory('Pass Out After Drinking Caffeine Syndrome', 'tutorial_chat', '15:05', [s]),
        ChatHistory('Invite to the meeting', 'popcorn_chat', '18:25', [ja, ju], VNMode('popcorn_vn', ju), save_img='ju'),
        ChatHistory('Hacking', 'hack_example', '20:41'),
        ChatHistory('Plot Branches', 'plot_branch_tutorial', '22:44', [], VNMode('plot_branch_vn'), plot_branch=PlotBranch(True)),
        ChatHistory("Onwards!", 'tutorial_good_end', '23:26', [u], VNMode('good_end_party', party=True))
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
        [ChatHistory('An Unfinished Task', 'tutorial_bad_end', '23:26', [v])] )]
default tutorial_bre = ["Bad Relationship End",
    RouteDay('Tutorial', 
            branch_vn= VNMode('plot_branch_bre'))]

default tutorial_route = Route(
                        default_branch=tutorial_good_end,
                        branch_list=[tutorial_bad_end,
                                     tutorial_bre],
                        route_history_title='Tutorial')

# This is an example of how a route for another character, such as 707,
# might look like
default seven_route = [ RouteDay('5th', [], 's'),
                        RouteDay('6th', [], 's'),
                        RouteDay('7th', [], 's'),
                        RouteDay('8th', [], 's'),
                        RouteDay('9th', [], 's'),
                        RouteDay('10th', [], 's'),
                        RouteDay('Final', [], 's')]

# This variable keeps track of all the routes you've defined in order
# to display it in the History screen from the main menu
# It should ALWAYS be at the end of the file
# It's a list of tuples; the first item in the tuple is the name
# of the route how you want it to show up in history (e.g. 'Tutorial'
# will show up in the history screen as "Tutorial Route") and the second
# also a tuple, where the first item is the variable for the route you
# defined earlier, and the second item is a string that's how you want
# that route to show up in the history list
default all_routes = [ tutorial_route ]

# default seven_bad_end_1 = []
# default seven_bad_end_2 = []
# default seven_bad_end_3 = []
# default seven_bre_1 = []
# default seven_bre_2 = []
# default seven_good_end = []
# default seven_normal_end = []
# default zen_route = []
# default zen_bad_end_1 = []
# default zen_bad_end_2 = []
# default zen_bad_end_3 = []
# default zen_bre_1 = []
# default zen_bre_2 = []
# default zen_good_end = []
# default zen_normal_end = []


# Here's an example all_routes definition as it might look if
# you had a common route and a route for 707 and Zen
# default all_routes = [ ('Common', [(common_route, 'default'),
#                                     (common_bad_end, 'Common Route Bad End') ]),
#                         ('707', [(seven_route, 'default'),
#                                  (seven_route_2, 'default'),
#                                  (seven_route_3, 'default'),
#                                  (seven_bad_end_1, '707 Bad Story End 1'),
#                                  (seven_bad_end_2, '707 Bad Story End 2'),
#                                  (seven_bad_end_3, '707 Bad Story End 3'),
#                                  (seven_bre_1, '707 Bad Relationship End 1'),
#                                  (seven_bre_2, '707 Bad Relationship End 2'),
#                                  (seven_good_end, '707 Good End'),
#                                  (seven_normal_end, '707 Normal End')]),
#                         ('Zen', [(zen_route, 'default'),
#                                  (zen_route_2, 'default'),
#                                  (zen_route_3, 'default'),
#                                  (zen_bad_end_1, 'Zen Bad Story End 1'),
#                                  (zen_bad_end_2, 'Zen Bad Story End 2'),
#                                  (zen_bad_end_3, 'Zen Bad Story End 3'),
#                                  (zen_bre_1, 'Zen Bad Relationship End 1'),
#                                  (zen_bre_2, 'Zen Bad Relationship End 2'),
#                                  (zen_good_end, 'Zen Good End'),
#                                  (zen_normal_end, 'Zen Normal End')])
#                                     ]
