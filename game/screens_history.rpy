##############################################
## This screen allows you to view replays
## of chatrooms and phone calls you've already
## seen in-game
###############################################

image history_button = Frame('Menu Screens/History/main02_button_01.png',
                                49, 52, 270, 53)
image history_button_hover = 'btn_hover:history_button'
image history_icon_album = 'Menu Screens/History/history_icon_album.png'
image history_icon_chat = 'Menu Screens/History/history_icon_chat.png'
image history_icon_call = 'Menu Screens/History/history_icon_call.png'
image history_icon_guest = 'Menu Screens/History/history_icon_guest.png'

## This screen lets you view the album or the chat history
screen select_history():

    tag menu

    use menu_header("History", Show('main_menu', Dissolve(0.5))):

        style_prefix "select_history"
        frame:
            vbox:
                button:
                    action [Function(check_for_CGs, all_albums=all_albums),
                            Show('photo_album', Dissolve(0.5))]
                    hbox:
                        add 'history_icon_album' yalign 0.5
                        text 'ALBUM'
                button:
                    action Show('select_history_route', Dissolve(0.5))
                    hbox:
                        add 'history_icon_chat' yalign 0.5
                        text "CHAT HISTORY"

                button:
                    action Show('guestbook', Dissolve(0.5))
                    hbox:
                        add 'history_icon_guest'
                        text 'GUEST'


style select_history_hbox:
    is default
    spacing 15
    align (0.5, 0.5)

style select_history_vbox:
    spacing 30
    align (0.5, 0.5)

style select_history_button:
    is default
    align (0.5, 0.2)
    background 'history_button'
    hover_background 'history_button_hover'
    padding (40,20,40,30)
    xysize (318,114)

style select_history_text:
    is default
    color "#fff"
    size 28
    xsize 50
    font gui.sans_serif_1b
    align (0.5, 0.5)

style select_history_frame:
    is default
    xysize (740, 1100)
    align (0.5, 0.5)


default which_history_route = None

## This screen lets you select which route to view in the history
screen select_history_route():

    tag menu

    use menu_header("History", Show('main_menu', Dissolve(0.5))):
        frame:
            xysize (750, 1070)
            style_prefix 'history_route'
            has vbox
            for route in all_routes:
                textbutton _(route.route_history_title):
                    action [SetVariable('which_history_route', route.route),
                            Show('day_select', days=route.route)]

style history_route_button:
    is other_settings_end_button
    padding (30,30)
    xsize 650
    ysize 120

style history_route_button_text:
    is mode_select

style history_route_vbox:
    align (0.5, 0.5)
    spacing 30

image history_chat_active = Frame("Menu Screens/History/msgsl_bg_active.png", 10,10)
image history_chat_inactive = Frame("Menu Screens/History/msgsl_bg_inactive.png", 10,10)
image history_chat_participated = Transform("Menu Screens/History/chat_history_participated.png", zoom=0.8)
image history_chat_alone = Transform("Menu Screens/History/chat_history_alone.png", zoom=0.8)

init python:

    def display_history(item, index, archive_list):
        """Return True if the History should display this particular item."""

        global persistent

        if persistent.testing_mode:
            return True

        # If it's a TimelineItem, it's only visible if the expired or regular
        # version has been seen
        if isinstance(item, TimelineItem):
            return item.was_played(ever=True)

        # Otherwise, it's a text label
        # Check if the item immediately after it is visible
        if index < len(archive_list)-1:
            return display_history(archive_list[index+1], index+1, archive_list)

        # Otherwise all has failed so don't display it
        return False

    def calls_available_history(calls):
        """Return True if at least one phone call in calls has been seen."""

        for c in calls:
            if persistent.completed_chatrooms.get(c):
                return True
        return False

    def get_caller(c):
        """Find the caller of this phone call from its label."""

        file_id = c.split('_')[-1]
        try:
            char = getattr(store, file_id)
            return PhoneCall(char, c)
        except AttributeError:
            for p in store.all_characters:
                if file_id == p.file_id:
                    return PhoneCall(p, c)
        return PhoneCall(None, c)

# True if the player is viewing a replay of an expired chatroom
default expired_replay = False
# This is a dictionary that holds a giant list of all the
# labels the player has seen/played through
default persistent.completed_chatrooms = {}

image contact_darken = "Menu Screens/History/contact_darken.png"
image call_incoming_outline = "Menu Screens/History/call_icon_incoming_outline.png"
image call_outgoing_outline = "Menu Screens/History/call_icon_outgoing_outline.png"
image call_missed_outline = "Menu Screens/History/call_icon_missed_outline.png"

screen timeline_item_history(item):

    python:
        # Determine if the participants list needs to scroll or not
        part_anim = null_anim
        if isinstance(item, ChatRoom) and item.participants:
            if len(item.participants) > 4:
                part_anim = participant_scroll

        # ChatRoom story mode displays similarly to solo StoryMode in
        # some cases
        if isinstance(item, StoryMode):
            story_mode = item
        elif isinstance(item, ChatRoom) and item.story_mode:
            story_mode = item.story_mode
        else:
            story_mode = None

        # StoryCall items display the same if they are alone or not
        if isinstance(item, StoryCall):
            story_calls = [item]
        elif isinstance(item, TimelineItem) and item.story_calls_list:
            story_calls = item.story_calls_list
        else:
            story_calls = None

        replay_dictionary = {'observing': True,
                            'current_timeline_item': item,
                            'current_day': current_day,
                            'current_day_num': current_day_num,
                            'name': persistent.name}

        expired_replay_dictionary = {'expired_replay': True,
                            'observing': True,
                            'current_timeline_item': item,
                            'current_day': current_day,
                            'current_day_num': current_day_num,
                            'name': persistent.name}

        replay_dict_story = copy(replay_dictionary)
        replay_dict_story['current_timeline_item'] = story_mode

    style_prefix None
    null height 10
    if not isinstance(item, TimelineItem):
        # It's the name/title of the ending
        frame:
            style_prefix 'history_item_text'
            text item
    elif isinstance(item, ChatRoom):
        frame:
            style_prefix 'history_chatroom'
            # These are the two buttons to replay the chat
            hbox:
                button:
                    if item.played_expired():
                        background 'history_chat_active'
                        hover_foreground '#fff5'
                        action Replay('play_timeline_item',
                                        scope=expired_replay_dictionary)
                    else:
                        background Fixed('history_chat_inactive', "#000c")
                        foreground "#0003"
                        action CConfirm(("You have not yet"
                                + " viewed this chat in-game."))
                    add 'history_chat_alone' align (0.5, 0.5)
                    if not item.played_expired():
                        add 'plot_lock' align (0.5, 0.5)
                button:
                    if item.played_regular():
                        hover_foreground '#fff5'
                        background 'history_chat_active'
                        action Replay('play_timeline_item',
                                        scope=replay_dictionary)
                    else:
                        background Fixed('history_chat_inactive', "#000c")
                        foreground "#0003"
                        action CConfirm(("You have not yet"
                                + " viewed this chat in-game."))
                    add 'history_chat_participated' align (0.5, 0.5)
                    if not item.played_regular():
                        add 'plot_lock' align (0.5, 0.5)


            vbox:
                style_prefix 'chat_timeline'
                # This box displays the trigger time and title of
                # the chatroom; optionally at a scrolling transform
                # so you can read the entire title
                hbox:
                    frame:
                        xoffset 77
                        yoffset 13
                        text item.trigger_time:
                            size 27
                            xalign 0.5
                            text_align 0.5
                    viewport:
                        xysize(400,27)
                        if get_text_width(item.title,
                                'chat_timeline_text') >= 400:
                            frame:
                                xysize(400,27)
                                text item.title at chat_title_scroll
                        else:
                            text item.title
                # Shows a list of all the people who start in this chatroom
                viewport:
                    xysize(530, 85)
                    yoffset 13
                    xoffset 77
                    yalign 0.5
                    frame:
                        xysize(355, 85)
                        hbox at part_anim:
                            yalign 0.5
                            spacing 5
                            if item.original_participants:
                                for person in item.original_participants:
                                    if person.participant_pic:
                                        add person.participant_pic

    # It's a solo StoryMode with a time
    if story_mode and story_mode.trigger_time and not story_mode.party:
        button:
            style_prefix 'solo_vn'
            foreground 'solo_vn_active'
            hover_foreground Fixed('solo_vn_active', 'solo_vn_hover')
            action [Preference("auto-forward", "disable"),
                    Replay('play_timeline_item',
                        scope=replay_dictionary)]
            add story_mode.vn_img align (1.0, 1.0) xoffset 3 yoffset 5
            hbox:
                frame:
                    text story_mode.trigger_time
                viewport:
                    frame:
                        xsize 350
                        if get_text_width(story_mode.title,
                                'chat_timeline_text') >= 350:
                            text story_mode.title at chat_title_scroll
                        else:
                            text story_mode.title

    # It's a StoryMode without a time
    elif story_mode and not story_mode.party:
        frame:
            style_prefix 'reg_timeline_vn'
            has hbox
            add 'vn_marker'
            button:
                foreground 'vn_active'
                hover_foreground 'vn_active_hover'
                action [Preference("auto-forward", "disable"),
                        Replay('play_timeline_item',
                                scope=replay_dict_story)]
                add story_mode.vn_img xoffset -5

    # It's the StoryMode that leads to the party
    elif story_mode and story_mode.party:
        frame:
            style_prefix 'party_timeline_vn'
            button:
                background 'vn_party'
                hover_foreground 'vn_party'
                action [Preference("auto-forward", "disable"),
                        Replay('play_timeline_item',
                            scope=replay_dict_story)]

    if story_calls:
        # There are story calls to display
        for phonecall in story_calls:
            use history_timeline_story_calls(phonecall, item)

    # Now add an hbox of the phone calls available after this chatroom
    if (isinstance(item, TimelineItem)
            and (item.incoming_calls_list or item.outgoing_calls_list)):
        hbox:
            xalign 1.0
            xoffset -40
            add Transform('call_mainicon', size=(60,60)) align (0.5, 0.75)
            if item.incoming_calls_list:
                use history_calls_list(item, item.incoming_calls_list, 'incoming')
            if item.outgoing_calls_list:
                use history_calls_list(item, item.outgoing_calls_list, 'outgoing')

screen history_timeline_story_calls(phonecall, item):

    frame:
        xoffset 70
        background 'story_call_history'
        xysize (625, 111)
        xalign 0.0
        hbox:
            yoffset 12 xoffset 78
            spacing 25
            # First add the profile picture of the caller
            fixed:
                fit_first True
                add phonecall.caller.participant_pic:
                    xalign 0.0
                add Transform('call_mainicon', size=(28,28)) align (0.01, 0.99)
            vbox:
                spacing 21
                hbox:
                    spacing 30
                    # The time of the call
                    $ the_time = phonecall.trigger_time or item.trigger_time
                    text the_time style 'chat_timeline_text'
                    # The title of the chatroom
                    text phonecall.caller.name style 'chat_timeline_text'
                # Thing that says the caller's name
                fixed:
                    $ the_title = phonecall.title or "Story Call"
                    text the_title style 'chat_timeline_text'

        # The replay icons
        hbox:
            align (0.99,0.6)
            spacing 10
            button:
                xysize (80,80)
                if phonecall.played_expired():
                    background 'history_chat_active'
                    hover_foreground '#fff5'
                    action Replay('play_timeline_item',
                                    scope={'expired_replay': True,
                            'observing': True,
                            'current_timeline_item': phonecall,
                            'current_day': current_day,
                            'current_day_num': current_day_num,
                            'name': persistent.name,
                            'current_call': phonecall},
                            locked=False)
                else:
                    background Fixed('history_chat_inactive', "#000c")
                    foreground "#0003"
                    action CConfirm(("You have not yet"
                        + " viewed this call in-game."))
                add 'call_missed_outline' align (0.5, 0.5)
                if not phonecall.played_expired():
                    add 'plot_lock' align (0.5, 0.5)
            button:
                xysize(80,80)
                if phonecall.played_regular():
                    hover_foreground '#fff5'
                    background 'history_chat_active'
                    action Replay('play_timeline_item',
                        scope={'observing': True,
                        'current_timeline_item': phonecall,
                        'current_day': current_day,
                        'current_day_num': current_day_num,
                        'name': persistent.name,
                        'current_call': phonecall},
                        locked=False)
                else:
                    background Fixed('history_chat_inactive', "#000c")
                    foreground "#0003"
                    action CConfirm(("You have not yet"
                        + " viewed this call in-game."))
                add 'call_incoming_outline' align (0.5, 0.5)
                if not phonecall.played_regular():
                    add 'plot_lock' align (0.5, 0.5)

## Shows regular phone calls that were available after this TimelineItem
screen history_calls_list(item, call_list, call_icon):
    for c in call_list:
        if persistent.completed_chatrooms.get(c):
            button:
                background Transform(c.split('_')[-1] + '_contact',
                                                size=(85,85))
                hover_background Fixed(Transform(c.split('_')[-1] + '_contact',
                                size=(85,85)), Transform(c.split('_')[-1]
                                + '_contact', size=(85,85)))
                add Transform('contact_darken', size=(85,85), alpha=0.3):
                    align (0.5,0.5)
                add Transform('call_' + call_icon + '_outline', size=(32, 32)):
                    align (1.0, 1.0)
                xysize (85,85)
                action Replay('play_phone_call', scope={'observing': True,
                    'current_timeline_item': item,
                    'current_day': current_day,
                    'current_day_num': current_day_num,
                    'name': persistent.name,
                    'current_call': get_caller(c)})


style history_item_text_frame:
    xsize 570
    yminimum 55
    xalign 1.0

style history_item_text_text:
    text_align 0.5
    color "#fff"
    font gui.sans_serif_1b
    xalign 0.5

style history_chatroom_frame:
    xoffset 70
    xysize (620, 160)
    xalign 0.0
    background 'chat_active'

style history_chatroom_hbox:
    align (0.98,0.83)
    spacing 10

style history_chatroom_button:
    xysize (80,80)



style timeline_button:
    xysize (181,62)
    text_align 0.5
    xalign 0.05
    yalign 0.5
    background 'vn_time_bg' padding (20,20)

style timeline_button_text:
    color '#fff'
    size 40
    xalign 0.5

style timeline_hbox:
    xysize (620, 160)
    xoffset 70
    xalign 0.0

style solo_vn_button:
    xoffset 77
    xysize (604, 173)
    xalign 0.0

style solo_vn_hbox:
    spacing 30
    xoffset 77
    yoffset 10

style solo_vn_frame:
    xysize (75, 30)

style solo_vn_text:
    is chat_timeline_text

style solo_vn_viewport:
    xysize (350, 30)
