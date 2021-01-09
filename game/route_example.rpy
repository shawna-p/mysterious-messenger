####################################################################
## CASUAL ROUTE DEFINITION
####################################################################
default example_casual_route_good_end = ["Good End",
    RouteDay('1st', [
        ChatRoom("Welcome1", 'casual_d1_example_1', '00:03', [y]),
        ChatRoom("Welcome2", 'casual_d1_example_2', '02:21', [ja]),
        ChatRoom("Zen's complaint", 'casual_d1_example_3', '04:35', [z]),
        ChatRoom("Yoosung's complaint", 'casual_d1_example_4', '07:00', [y]),
        ChatRoom("Jumin's lonely morning", 'casual_d1_example_5', '08:00', [ju, z]),
        ChatRoom("Seven loves cats", 'casual_d1_example_6', '10:04', [ju, s]),
        ChatRoom("Seven's investigation", 'casual_d1_example_7', '11:58', [s, y]),
        ChatRoom("Jaehee's expectation", 'casual_d1_example_8', '12:50', [ja]),
        ChatRoom("Jumin's curiosity", 'casual_d1_example_9', '13:48', [ju]),
        ChatRoom("Zen reminisces about the old party", 'casual_d1_example_10', '15:00', [z]),
        ChatRoom("Who hates to work?", 'casual_d1_example_11', '16:50', [s, y]),
        ChatRoom("Yoosung's hope for the new party", 'casual_d1_example_12', '18:02', [y]),
        ChatRoom("Concerns of two men", 'casual_d1_example_13', '18:58', [z, ju]),
        ChatRoom("Discussion about the party", 'casual_d1_example_14', '19:40', [ju, ja]),
        ChatRoom("Zen's expectation", 'casual_d1_example_15', '21:50', [z]),
        ChatRoom("Excited Yoosung", 'casual_d1_example_16', '22:30', [y]),
        ChatRoom("Jaehee's favor", 'casual_d1_example_17', '23:15', [ja])
        # Rather than defining the save_img for each individual item, you can
        # also set it here on the RouteDay object to apply it to all items.
        # If save_img is set for an individual item, this will not overwrite it.
        ], save_img='casual'),
    RouteDay('2nd', [
        ChatRoom("Jaehee's announcement", 'casual_d2_example_1', '00:38', [ja]),
        ChatRoom("Zen received fan letters", 'casual_d2_example_2', '03:03', [z]),
        ChatRoom("Yoosung's omelette rice", 'casual_d2_example_3', '07:00', [y]),
        ChatRoom("Fight over cats", 'casual_d2_example_4', '08:05', [ja, ju]),
        ChatRoom("Yoosung's thoughts", 'casual_d2_example_5', '11:45', [y]),
        ChatRoom("Zen hates cats", 'casual_d2_example_6', '12:43', [s, z]),
        ChatRoom("Concerns from V and Zen", 'casual_d2_example_7', '15:00', [v, z]),
        ChatRoom("Yoosung's doubt", 'casual_d2_example_8', '17:23', [s, y, ju]),
        ChatRoom("Zen with new work", 'casual_d2_example_9', '19:02', [z, y]),
        ChatRoom("Romance novel company", 'casual_d2_example_10', '20:05', [z]),
        ChatRoom("Jaehee's support", 'casual_d2_example_11', '21:35', [ja])
        ], save_img='casual'),
    RouteDay('3rd', [
        ChatRoom("Girlfriend and Zen", None, '00:00', [z, s]),
        ChatRoom("Unstoppable LOLOL", None, '03:04', [y, ja, ju]),
        ChatRoom("Jumin and Cat and Zen", None, '07:30', [ju, z, ja]),
        ChatRoom("The person that has to be found", None, '10:50', [ju, s, ja]),
        ChatRoom("Handsome Zen", None, '12:15', [z, ja, y]),
        ChatRoom("The Lady of Bracelets", None, '13:05', [ja, y]),
        ChatRoom("Jaehee's thoughts", None, '15:30', [z, ja, y]),
        ChatRoom("Zen making a fuss", None, '17:56', [y, z]),
        ChatRoom("A slave of money, Seven", None, '19:42', [s, ja]),
        ChatRoom("Jalapenos topping", None, '21:15', [ja, y, z]),
        ChatRoom("Yoosung is living alone", None, '23:00', [y, z])
        # auto_label is another convenience that will automatically create
        # numbered labels for the items on a RouteDay. You must provide the
        # prefix, and then a number starting at 1 will be assigned to each item
        # with `None` as its label. So, the chatroom "Handsome Zen" can be found
        # at the label "casual_d3_example_5". If a label is already given,
        # auto_label will not overwrite it and the numbering will continue
        # without skipping. This can be helpful if you want to insert a new
        # chatroom or story item into the day without renaming all the labels.
        ], save_img='casual', auto_label='casual_d3_example_'),
    RouteDay('4th', [
        ChatRoom("Jaehee worries about Jumin", 'casual_d4_example_1', '00:18', [ja]),
        ChatRoom("Do not drink coffee", 'casual_d4_example_2', '03:24', [s, y]),
        ChatRoom("Jaehee's position", 'casual_d4_example_3', '07:00', [ja, ju]),
        ChatRoom("Seven mocks Yoosung", 'casual_d4_example_4', '09:05', [ja, s, y]),
        ChatRoom("Blame", 'casual_d4_example_5', '10:00', [v, y]),
        ChatRoom("I quit LOLOL", 'casual_d4_example_6', '12:50', [ja, y]),
        ChatRoom("No girlfriend", 'casual_d4_example_7', '15:00', [z, y, ja]),
        ChatRoom("Found him", 'casual_d4_example_8', '17:04', [s, ja]),
        ChatRoom("Are you really...", 'casual_d4_example_9', '19:18', [y, ja, z]),
        ChatRoom("New RFA party", 'casual_d4_example_10', '21:08', [v, ja]),
        ChatRoom("The game that starts again", 'casual_d4_example_11', '22:00', [z, y, s, ju]),
        ChatRoom("Weird Dream", 'casual_d4_example_12', '23:15', [ja, y, z], plot_branch=PlotBranch(False))
        ], save_img='casual'),
    # In order for these days to show up in the timeline, they are defined
    # here with empty archive lists.
    RouteDay('5th'),
    RouteDay('6th'),
    RouteDay('7th'),
    RouteDay('8th'),
    RouteDay('9th'),
    RouteDay('10th'),
    RouteDay('Final')]

# Casual Route Bad End is defined here as a branch rather than a part of the
# main Casual Route so that it can have a title in the History screen denoting
# that it is the Casual Route Bad End.
default example_casual_route_bad_end = [
    # This is the title as it will appear in the History
    "Casual Common Bad Ending",
    # This branch only has items on the 5th day
    RouteDay('5th', [
        ChatRoom("We're machines", 'casual_d5_example_1', '01:28', [y]),
        ChatRoom("What?", 'casual_d5_example_2', '03:22', [ja]),
        ChatRoom("Yoosung's delusion", 'casual_d5_example_3', '05:35', [z, y, ja]),
        ChatRoom(" ", 'casual_d5_example_4', '07:00', [ja])
        ], save_img='casual')]

default example_casual_route = Route(
    default_branch=example_casual_route_good_end,
    branch_list=[example_casual_route_bad_end],
    route_history_title='Casual',
    # There is no "Casual Route Good End" in the History, since it just
    # changes into a new route. Thus, tell the program has_end_title is False.
    has_end_title=False
)

label example_casual_start:
    python:
        new_route_setup(route=example_casual_route)
        # r, v, and ri are not present on casual route.
        character_list = [ju, z, s, y, ja]
        heart_point_chars = [ju, z, s, y, ja]
    # Typically you would put an introductory chatroom of some kind here.
    # For convenience, this simply jumps to the home screen.
    jump skip_intro_setup

label casual_d4_example_12_branch:
    # How this might actually look for a branching path
    # if (z.heart_points >= ja.heart_points
    #         and z.heart_points >= y.heart_points
    #         and z.heart_points > 20):
    #     $ merge_routes(zen_route_good_end)
    # elif (ja.heart_points >= z.heart_points
    #         and ja.heart_points > y.heart_points
    #         and ja.heart_points > 20):
    #     $ merge_routes(jaehee_route_good_end)
    # elif (y.heart_points > z.heart_points
    #         and y.heart_points > ja.heart_points
    #         and y.heart_points > 20):
    #     $ merge_routes(yoosung_route_good_end)
    # else:
    #     $ merge_routes(casual_route_bad_end)

    # This uses a rather arbitrary but easily calculated way to determine
    # whether the player should continue on to Jaehee's route.
    if persistent.custom_footers:
        $ merge_routes(example_jaehee_route_good_end)
    else:
        # Bad End
        $ merge_routes(example_casual_route_bad_end)
    return


####################################################################
## JAEHEE ROUTE DEFINITION
####################################################################

default example_jaehee_route_good_end = ["Jaehee Good Ending",
    RouteDay('5th', [
        ChatRoom("I cannot control myself", 'jaehee_d5_example_1', '01:22', [y]),
        ChatRoom("Lonely Zen", 'jaehee_d5_example_2', '03:13', [z]),
        ChatRoom("Tickets to the cherry farm", 'jaehee_d5_example_3', '06:49', [ju, ja]),
        ChatRoom("Jumin is the boss", 'jaehee_d5_example_4', '08:14', [z]),
        ChatRoom("A vicious enterpriser?", 'jaehee_d5_example_5', '11:20', [s, y]),
        ChatRoom("Freelancing is the best", 'jaehee_d5_example_6', '13:20', [z]),
        ChatRoom("Zen's respect towards Jaehee", 'jaehee_d5_example_7', '15:55', [ja]),
        ChatRoom("Yoosung's concern", 'jaehee_d5_example_8', '17:15', [y]),
        ChatRoom("Life that pursues happiness", 'jaehee_d5_example_9', '19:00', [s, ja]),
        ChatRoom("Jaehee and love", 'jaehee_d5_example_10', '21:04', [y, z]),
        ChatRoom("Jumin back from the business trip", 'jaehee_d5_example_11', '23:04', [ju])
        ], day_icon='ja', save_img='ja'),
        # All of the days on Jaehee's route get day_icon 'ja' and are saved
        # with save_img 'ja'
    RouteDay('6th', [
        ChatRoom("Yoosung and the tuition", 'jaehee_d6_example_1', '01:11', [y]),
        ChatRoom("Zen's injury", 'jaehee_d6_example_2', '02:48', [z]),
        ChatRoom("Jaehee worries about Zen", 'jaehee_d6_example_3', '07:40', [ja, s]),
        ChatRoom("About Zen's recovery speed", 'jaehee_d6_example_4', '10:15', [y]),
        ChatRoom("New project", 'jaehee_d6_example_5', '12:31', [ju, ja]),
        ChatRoom("Someone must be chasing us", 'jaehee_d6_example_6', '13:55', [s]),
        ChatRoom("Stalker? Or imaginary friend?", 'jaehee_d6_example_7', '16:16', [z, y]),
        ChatRoom("Jumin's security guards", 'jaehee_d6_example_8', '18:00', [ju, ja]),
        ChatRoom("Visiting Zen", 'jaehee_d6_example_9', '19:09', [ja, s], plot_branch=PlotBranch(True)),
        ChatRoom("To Zen's place", 'jaehee_d6_example_10', '21:12', [ja]),
        ChatRoom("Fresh feeling", 'jaehee_d6_example_11', '23:09', [z])
        ], day_icon='ja', save_img='ja'),
    RouteDay('7th', [
        ChatRoom("My heart is beating!", 'jaehee_d7_example_1', '00:45', [y]),
        ChatRoom("Zen's room", 'jaehee_d7_example_2', '02:01', [ja]),
        ChatRoom("Jaehee and the vacation?", 'jaehee_d7_example_3', '08:15', [z, ju]),
        ChatRoom("I need to rest!", 'jaehee_d7_example_4', '10:48', [s, y]),
        ChatRoom("Cat hotel", 'jaehee_d7_example_5', '12:30', [ju]),
        ChatRoom("NO WAY!", 'jaehee_d7_example_6', '13:46', [z]),
        ChatRoom("What's so great about coffee", 'jaehee_d7_example_7', '15:55', [ja, y]),
        ChatRoom("Hacker", 'jaehee_d7_example_8', '17:22', [s]),
        ChatRoom("New side of Jaehee", 'jaehee_d7_example_9', '19:30', [y, z]),
        ChatRoom("Adding more work", 'jaehee_d7_example_10', '21:26', [ju, ja]),
        ChatRoom("Deal", 'jaehee_d7_example_11', '23:00', [z, s])
        ], day_icon='ja', save_img='ja'),
    RouteDay('8th', [
        ChatRoom("I can do it by myself", None, '01:20', [ja, s]),
        ChatRoom("Worried Zen", None, '03:32', [z]),
        ChatRoom("Warm supports", None, '06:55', [y, ja]),
        ChatRoom("Ridiculous idea", None, '08:00', [ju]),
        ChatRoom("Relaxing café", None, '10:17', [ja]),
        ChatRoom("I am free!", None, '12:45', [s, z]),
        ChatRoom("Don't work too hard on this", None, '15:02', [ju]),
        ChatRoom("Possibilities", None, '17:16', [s, ja], plot_branch=PlotBranch(True)),
        ChatRoom("Let's support each other", None, '18:53', [z]),
        ChatRoom("Zen's gift", None, '20:34', [ja]),
        ChatRoom("Go Jaehee!", None, '22:57', [y])
        ], day_icon='ja', save_img='ja', auto_label='jaehee_d8_example_'),
    RouteDay('9th', [
        ChatRoom("Hand mill", None, '00:14', [ja, z]),
        ChatRoom("Work is done!", None, '02:48', [s]),
        ChatRoom("Assistant Kang", None, '08:43', [ju]),
        ChatRoom("Support and care", None, '11:30', [y]),
        ChatRoom("Coffee time", None, '13:39', [z]),
        ChatRoom("Premium gas", None, '16:11', [s]),
        ChatRoom("Conflict between Jumin and Jaehee", None, '17:20', [ju, ja]),
        ChatRoom("Treasure", None, '18:38', [y, s]),
        ChatRoom("Fired", None, '20:02', [z, ja]),
        ChatRoom("Old memory", None, '21:47', [y]),
        ChatRoom("I can't understand", None, '23:11', [ju])
        ], day_icon='ja', save_img='ja', auto_label='jaehee_d9_example_'),
    RouteDay('10th', [
        ChatRoom("Sorry and...thank you", None, '01:32', [ja]),
        ChatRoom("Jaehee's courage", None, '02:58', [z]),
        ChatRoom("Revenge", None, '08:10', [ju, s]),
        ChatRoom("Jumin took my babe car", None, '09:20', [s]),
        ChatRoom("Determined Yoosung", None, '12:45', [y]),
        ChatRoom("Find a path that makes you happy", None, '14:30', [z]),
        ChatRoom("Jumin's driving skill", None, '16:22', [ju], plot_branch=PlotBranch(False)),
        ChatRoom("Jaehee worries about Jumin", None, '17:30', [ja]),
        ChatRoom("Threat", None, '18:48', [s]),
        ChatRoom("Jaehee", None, '20:00', [ju, ja]),
        ChatRoom("Disappeared hacker", None, '23:18', [z, v, s])
        ], day_icon='ja', save_img='ja', auto_label='jaehee_d10_example_'),
    RouteDay('Final', [
        ChatRoom("See you at the party", 'jaehee_d11_example_1', '08:00', [y, z, s, ja]),
        # This is how the party is defined when it is separate from a
        # chatroom. Here it has a trigger time of 12:00.
        TheParty('example_jaehee_good_party', '12:00')
        ], day_icon='ja', save_img='ja')
]

default example_jaehee_route_bad_end_1 = ["Jaehee Bad Story Ending 1",
    RouteDay('6th', [
        ChatRoom("Very private visit", 'jaehee_d6_example_12', '21:12', [s, ja]),
        ChatRoom("Never ending work", 'jaehee_d6_example_13', '23:09', [ju, ja, y])
    ], day_icon='ja',
    # After this route branches, if it branches onto this path, the last
    # chatroom before the branch will have this Story Mode attached to it.
    branch_vn=BranchStoryMode('example_jaehee_be1_vn', who=s),
    save_img='ja')
]

default example_jaehee_route_bad_end_2 = ["Jaehee Bad Story Ending 2",
    RouteDay('8th', [
        ChatRoom("Jaehee can't work like a machine", 'jaehee_d8_example_12', '18:53', [z]),
        ChatRoom("To the hospital", 'jaehee_d8_example_13', '20:34', [s, y])
    ], day_icon='ja', branch_vn=BranchStoryMode('example_jaehee_be2_vn'),
    save_img='ja')
]

default example_jaehee_route_bad_end_3 = ["Jaehee Bad Story Ending 3",
    RouteDay('10th', [
        ChatRoom("New secretary", 'jaehee_d10_example_12', '17:30', [ja, ju])
    ], day_icon='ja', save_img='ja')
]

default example_jaehee_route_bre_1 = ["Jaehee Bad Relationship Ending 1",
    RouteDay('6th', branch_vn=BranchStoryMode('example_jaehee_bre2_vn'),
    day_icon='ja', save_img='ja')
]

default example_jaehee_route_bre_2 = ["Jaehee Bad Relationship Ending 2",
    RouteDay('10th', [
        ChatRoom("Suspicious feeling", 'jaehee_d10_example_13', '17:30', [ja, ju, y])
    ], day_icon='ja', save_img='ja')
]

# If the party should act as a plot branch (as in, clicking the party can
# lead to more than one ending), then you need to define a route for it like
# any other plot branch. In this case, the only item is a lone party at 12:00.
default example_jaehee_route_normal_end = ["Jaehee Normal Ending",
    RouteDay('Final',
        [TheParty('example_jaehee_normal_party', '12:00')], day_icon='ja',
        save_img='ja')
]

default example_jaehee_route = Route(
    default_branch=example_jaehee_route_good_end,
    branch_list=[example_jaehee_route_normal_end,
        example_jaehee_route_bad_end_1,
        example_jaehee_route_bad_end_2,
        example_jaehee_route_bad_end_3,
        example_jaehee_route_bre_1,
        example_jaehee_route_bre_2
    ],
    route_history_title="Jaehee",
    # You can define a background for this route. It should be
    # 650x120 px and will have its corners automatically cropped to
    # fit the frame.
    history_background="Menu Screens/Main Menu/jaehee-route-bg.webp"
)

####################################################################
## Jaehee route branches
####################################################################

# First Jaehee Route Branch
label jaehee_d6_example_9_branch:
    # How this would typically look:
    # if participated_percentage(5, 6) < 20:
    #     $ merge_routes(example_jaehee_route_bre_1)
    # elif ja.good_heart >= ja.bad_heart:
    #     $ continue_route()
    # else:
    #     $ merge_routes(example_jaehee_route_bad_end_1)

    # However, this is simplified for testing purposes
    if persistent.custom_footers and persistent.animated_backgrounds:
        $ continue_route()
    elif persistent.custom_footers:
        $ merge_routes(example_jaehee_route_bad_end_1)
    else:
        $ merge_routes(example_jaehee_route_bre_1)
    return

# Second Jaehee Route Branch
label jaehee_d8_example_8_branch:
    if persistent.custom_footers:
        $ continue_route()
    else:
        $ merge_routes(example_jaehee_route_bad_end_2)
    return

# Third Jaehee Route Branch
label jaehee_d10_example_7_branch:
    if persistent.custom_footers and persistent.animated_backgrounds:
        $ continue_route()
    elif persistent.custom_footers:
        $ merge_routes(example_jaehee_route_bad_end_3)
    else:
        $ merge_routes(example_jaehee_route_bre_2)
    return

# Jaehee Party Branch
label example_jaehee_good_party_branch:
    # How this might typically look
    # if attending_guests() >= 10:
    #     $ continue_route()
    # else:
    #     $ merge_routes(example_jaehee_route_normal_end)
    if persistent.custom_footers:
        $ continue_route()
    else:
        $ merge_routes(example_jaehee_route_normal_end)
    return

label example_jaehee_good_party:
    scene bg rfa_party_3
    show jaehee party happy
    ja "Some example dialogue."
    $ ending = 'good'
    return

####################################################################
## CASUAL ROUTE STUB STORY ITEMS
####################################################################
# These are simply stub implementations of the chatrooms and Story Mode
# items on Casual Route and Jaehee's route. Some are there so that the
# correct Story Mode shows up in the History, but most are simply for
# testing. For the various endings, the line `$ ending =` is included to
# tell the game the route is over.
label casual_d1_example_1:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_2:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_3:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_4:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_5:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_6:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_7:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_8:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_9:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_10:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_11:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_12:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_13:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_14:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_15:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_16:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_17:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return

label casual_d1_example_1_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_2_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_3_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_4_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_5_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_6_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_7_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_8_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_9_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_10_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_11_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_12_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_13_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_14_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_15_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_16_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label casual_d1_example_17_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return

label casual_d2_example_1:
    scene noon
    play music narcissistic_jazz
    z "Some example dialogue."
    return
label casual_d2_example_2:
    scene noon
    play music narcissistic_jazz
    z "Some example dialogue."
    return
label casual_d2_example_3:
    scene noon
    play music narcissistic_jazz
    z "Some example dialogue."
    return
label casual_d2_example_4:
    scene noon
    play music narcissistic_jazz
    z "Some example dialogue."
    return
label casual_d2_example_5:
    scene noon
    play music narcissistic_jazz
    z "Some example dialogue."
    return
label casual_d2_example_6:
    scene noon
    play music narcissistic_jazz
    z "Some example dialogue."
    return
label casual_d2_example_7:
    scene noon
    play music narcissistic_jazz
    z "Some example dialogue."
    return
label casual_d2_example_8:
    scene noon
    play music narcissistic_jazz
    z "Some example dialogue."
    return
label casual_d2_example_9:
    scene noon
    play music narcissistic_jazz
    z "Some example dialogue."
    return
label casual_d2_example_10:
    scene noon
    play music narcissistic_jazz
    z "Some example dialogue."
    return
label casual_d2_example_11:
    scene noon
    play music narcissistic_jazz
    z "Some example dialogue."
    return


label casual_d2_example_1_expired:
    scene noon
    play music narcissistic_jazz
    z "Some example dialogue."
    return
label casual_d2_example_2_expired:
    scene noon
    play music narcissistic_jazz
    z "Some example dialogue."
    return
label casual_d2_example_3_expired:
    scene noon
    play music narcissistic_jazz
    z "Some example dialogue."
    return
label casual_d2_example_4_expired:
    scene noon
    play music narcissistic_jazz
    z "Some example dialogue."
    return
label casual_d2_example_5_expired:
    scene noon
    play music narcissistic_jazz
    z "Some example dialogue."
    return
label casual_d2_example_6_expired:
    scene noon
    play music narcissistic_jazz
    z "Some example dialogue."
    return
label casual_d2_example_7_expired:
    scene noon
    play music narcissistic_jazz
    z "Some example dialogue."
    return
label casual_d2_example_8_expired:
    scene noon
    play music narcissistic_jazz
    z "Some example dialogue."
    return
label casual_d2_example_9_expired:
    scene noon
    play music narcissistic_jazz
    z "Some example dialogue."
    return
label casual_d2_example_10_expired:
    scene noon
    play music narcissistic_jazz
    z "Some example dialogue."
    return
label casual_d2_example_11_expired:
    scene noon
    play music narcissistic_jazz
    z "Some example dialogue."
    return


label casual_d3_example_1:
    scene evening
    play music silly_smile_again
    y "Some example dialogue."
    return
label casual_d3_example_2:
    scene evening
    play music silly_smile_again
    y "Some example dialogue."
    return
label casual_d3_example_3:
    scene evening
    play music silly_smile_again
    y "Some example dialogue."
    return
label casual_d3_example_4:
    scene evening
    play music silly_smile_again
    y "Some example dialogue."
    return
label casual_d3_example_5:
    scene evening
    play music silly_smile_again
    y "Some example dialogue."
    return
label casual_d3_example_6:
    scene evening
    play music silly_smile_again
    y "Some example dialogue."
    return
label casual_d3_example_7:
    scene evening
    play music silly_smile_again
    y "Some example dialogue."
    return
label casual_d3_example_8:
    scene evening
    play music silly_smile_again
    y "Some example dialogue."
    return
label casual_d3_example_9:
    scene evening
    play music silly_smile_again
    y "Some example dialogue."
    return
label casual_d3_example_10:
    scene evening
    play music silly_smile_again
    y "Some example dialogue."
    return
label casual_d3_example_11:
    scene evening
    play music silly_smile_again
    y "Some example dialogue."
    return


label casual_d3_example_1_expired:
    scene evening
    play music silly_smile_again
    y "Some example dialogue."
    return
label casual_d3_example_2_expired:
    scene evening
    play music silly_smile_again
    y "Some example dialogue."
    return
label casual_d3_example_3_expired:
    scene evening
    play music silly_smile_again
    y "Some example dialogue."
    return
label casual_d3_example_4_expired:
    scene evening
    play music silly_smile_again
    y "Some example dialogue."
    return
label casual_d3_example_5_expired:
    scene evening
    play music silly_smile_again
    y "Some example dialogue."
    return
label casual_d3_example_6_expired:
    scene evening
    play music silly_smile_again
    y "Some example dialogue."
    return
label casual_d3_example_7_expired:
    scene evening
    play music silly_smile_again
    y "Some example dialogue."
    return
label casual_d3_example_8_expired:
    scene evening
    play music silly_smile_again
    y "Some example dialogue."
    return
label casual_d3_example_9_expired:
    scene evening
    play music silly_smile_again
    y "Some example dialogue."
    return
label casual_d3_example_10_expired:
    scene evening
    play music silly_smile_again
    y "Some example dialogue."
    return
label casual_d3_example_11_expired:
    scene evening
    play music silly_smile_again
    y "Some example dialogue."
    return

label casual_d4_example_1:
    scene night
    play music urban_night_cityscape
    ju "Some example dialogue."
    return
label casual_d4_example_2:
    scene night
    play music urban_night_cityscape
    ju "Some example dialogue."
    return
label casual_d4_example_3:
    scene night
    play music urban_night_cityscape
    ju "Some example dialogue."
    return
label casual_d4_example_4:
    scene night
    play music urban_night_cityscape
    ju "Some example dialogue."
    return
label casual_d4_example_5:
    scene night
    play music urban_night_cityscape
    ju "Some example dialogue."
    return
label casual_d4_example_6:
    scene night
    play music urban_night_cityscape
    ju "Some example dialogue."
    return
label casual_d4_example_7:
    scene night
    play music urban_night_cityscape
    ju "Some example dialogue."
    return
label casual_d4_example_8:
    scene night
    play music urban_night_cityscape
    ju "Some example dialogue."
    return
label casual_d4_example_9:
    scene night
    play music urban_night_cityscape
    ju "Some example dialogue."
    return
label casual_d4_example_10:
    scene night
    play music urban_night_cityscape
    ju "Some example dialogue."
    return
label casual_d4_example_11:
    scene night
    play music urban_night_cityscape
    ju "Some example dialogue."
    return
label casual_d4_example_12:
    scene night
    play music urban_night_cityscape
    ju "Some example dialogue."
    return


label casual_d4_example_1_expired:
    scene night
    play music urban_night_cityscape
    ju "Some example dialogue."
    return
label casual_d4_example_2_expired:
    scene night
    play music urban_night_cityscape
    ju "Some example dialogue."
    return
label casual_d4_example_3_expired:
    scene night
    play music urban_night_cityscape
    ju "Some example dialogue."
    return
label casual_d4_example_4_expired:
    scene night
    play music urban_night_cityscape
    ju "Some example dialogue."
    return
label casual_d4_example_5_expired:
    scene night
    play music urban_night_cityscape
    ju "Some example dialogue."
    return
label casual_d4_example_6_expired:
    scene night
    play music urban_night_cityscape
    ju "Some example dialogue."
    return
label casual_d4_example_7_expired:
    scene night
    play music urban_night_cityscape
    ju "Some example dialogue."
    return
label casual_d4_example_8_expired:
    scene night
    play music urban_night_cityscape
    ju "Some example dialogue."
    return
label casual_d4_example_9_expired:
    scene night
    play music urban_night_cityscape
    ju "Some example dialogue."
    return
label casual_d4_example_10_expired:
    scene night
    play music urban_night_cityscape
    ju "Some example dialogue."
    return
label casual_d4_example_11_expired:
    scene night
    play music urban_night_cityscape
    ju "Some example dialogue."
    return
label casual_d4_example_12_expired:
    scene night
    play music urban_night_cityscape
    ju "Some example dialogue."
    return


label casual_d5_example_1:
    scene earlyMorn
    play music geniusly_hacked_bebop
    s "Some example dialogue."
    return
label casual_d5_example_2:
    scene earlyMorn
    play music geniusly_hacked_bebop
    s "Some example dialogue."
    return
label casual_d5_example_3:
    scene earlyMorn
    play music geniusly_hacked_bebop
    s "Some example dialogue."
    return
label casual_d5_example_4:
    scene earlyMorn
    play music geniusly_hacked_bebop
    s "Some example dialogue."
    $ ending = 'bad'
    return


label casual_d5_example_1_expired:
    scene earlyMorn
    play music geniusly_hacked_bebop
    s "Some example dialogue."
    return
label casual_d5_example_2_expired:
    scene earlyMorn
    play music geniusly_hacked_bebop
    s "Some example dialogue."
    return
label casual_d5_example_3_expired:
    scene earlyMorn
    play music geniusly_hacked_bebop
    s "Some example dialogue."
    return
label casual_d5_example_4_expired:
    scene earlyMorn
    play music geniusly_hacked_bebop
    s "Some example dialogue."
    $ ending = 'bad'
    return

####################################################################
## JAEHEE ROUTE STUB STORY ITEMS
####################################################################

label jaehee_d5_example_1:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d5_example_2:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d5_example_3:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d5_example_4:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d5_example_5:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d5_example_6:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d5_example_7:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d5_example_8:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d5_example_9:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d5_example_10:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d5_example_11:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d5_example_1_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d5_example_2_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d5_example_3_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d5_example_4_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d5_example_5_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d5_example_6_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d5_example_7_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d5_example_8_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d5_example_9_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d5_example_10_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d5_example_11_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d6_example_1:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d6_example_2:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d6_example_3:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d6_example_4:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d6_example_5:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d6_example_6:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d6_example_7:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d6_example_8:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d6_example_9:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d6_example_10:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d6_example_11:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d6_example_12:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d6_example_13:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d6_example_1_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d6_example_2_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d6_example_3_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d6_example_4_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d6_example_5_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d6_example_6_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d6_example_7_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d6_example_8_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d6_example_9_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d6_example_10_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d6_example_11_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d6_example_12_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d6_example_13_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d7_example_1:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d7_example_2:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d7_example_3:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d7_example_4:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d7_example_5:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d7_example_6:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d7_example_7:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d7_example_8:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d7_example_9:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d7_example_10:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d7_example_11:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d7_example_1_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d7_example_2_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d7_example_3_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d7_example_4_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d7_example_5_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d7_example_6_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d7_example_7_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d7_example_8_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d7_example_9_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d7_example_10_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return
label jaehee_d7_example_11_expired:
    scene morning
    play music lonesome_practicalism
    ja "Some example dialogue."
    return

label jaehee_d8_example_1:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d8_example_2:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d8_example_3:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d8_example_4:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d8_example_5:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d8_example_6:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d8_example_7:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d8_example_8:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d8_example_9:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d8_example_10:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d8_example_11:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d8_example_12:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d8_example_13:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d8_example_1_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d8_example_2_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d8_example_3_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d8_example_4_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d8_example_5_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d8_example_6_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d8_example_7_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d8_example_8_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d8_example_9_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d8_example_10_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d8_example_11_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d8_example_12_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d8_example_13_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d9_example_1:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d9_example_2:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d9_example_3:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d9_example_4:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d9_example_5:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d9_example_6:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d9_example_7:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d9_example_8:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d9_example_9:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d9_example_10:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d9_example_11:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d9_example_1_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d9_example_2_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d9_example_3_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d9_example_4_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d9_example_5_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d9_example_6_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d9_example_7_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d9_example_8_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d9_example_9_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d9_example_10_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d9_example_11_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d10_example_1:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d10_example_2:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d10_example_3:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d10_example_4:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d10_example_5:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d10_example_6:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d10_example_7:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d10_example_8:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d10_example_9:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d10_example_10:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d10_example_11:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d10_example_12:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d10_example_13:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d10_example_1_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d10_example_2_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d10_example_3_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d10_example_4_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d10_example_5_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d10_example_6_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d10_example_7_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d10_example_8_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d10_example_9_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d10_example_10_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d10_example_11_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d10_example_12_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d10_example_13_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d11_example_1:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return
label jaehee_d11_example_1_expired:
    scene evening
    play music lonesome_practicalism_v2
    ja "Some dialogue."
    ju "Some more dialogue."
    return


label jaehee_d5_example_4_vn_ja:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    return
label jaehee_d6_example_5_vn_s:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    return
label jaehee_d6_example_7_vn_ju:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    return
label jaehee_d6_example_9_vn_ja:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    return
label jaehee_d6_example_10_vn_z:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    return
label jaehee_d6_example_12_vn_z:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    return
label jaehee_d6_example_13_vn_z:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    $ ending = 'bad'
    return
label jaehee_d7_example_2_vn:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    return
label jaehee_d7_example_3_vn_ja:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    return
label jaehee_d7_example_6_vn_s:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    return
label jaehee_d7_example_7_vn_z:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    return
label jaehee_d7_example_10_vn_ja:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    return
label jaehee_d7_example_11_vn:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    return
label jaehee_d8_example_2_vn_s:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    return
label jaehee_d8_example_4_vn:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    return
label jaehee_d8_example_7_vn_ju:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    return
label jaehee_d8_example_8_vn_ja:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    return
label jaehee_d8_example_12_vn_ju:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    return
label jaehee_d8_example_13_vn_ja:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    $ ending = 'bad'
    return
label example_jaehee_be1_vn:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    return
label example_jaehee_be2_vn:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    return
label example_jaehee_bre2_vn:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    $ ending = 'bad'
    return
label example_jaehee_normal_party:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy party
    ja "Some dialogue."
    $ ending = 'normal'
    return
label jaehee_d9_example_5_vn_z:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    return
label jaehee_d9_example_6_vn_ju:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    return
label jaehee_d10_example_3_vn_ju:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    return
label jaehee_d10_example_10_vn_ju:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    return
label jaehee_d10_example_11_vn_v:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    return
label jaehee_d10_example_12_vn_ju:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    $ ending = 'bad'
    return
label jaehee_d10_example_13_vn:
    play music mystic_chat
    scene bg cr_meeting_room
    show jaehee happy
    ja "Some dialogue."
    $ ending = 'bad'
    return