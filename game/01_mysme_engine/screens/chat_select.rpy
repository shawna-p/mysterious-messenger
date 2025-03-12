########################################################
## This is the screen where you choose which day to play
########################################################
screen day_select(days=story_archive):

    tag menu
    modal True

    # If the player isn't on the main menu (aka viewing this screen
    # from the history), the game should save
    if not main_menu:
        on 'show' action [AutoSave()]
        on 'replace' action [AutoSave()]
    default return_action = Show('select_history_route', Dissolve(0.5)) if main_menu else Show('chat_home', Dissolve(0.5))

    use menu_header("Day List", return_action):
        viewport:
            xysize (config.screen_width-30, config.screen_height-234)
            yalign 0.85
            xalign 0.5
            xadjustment day_select_xadj
            mousewheel "horizontal"
            scrollbars "horizontal"
            draggable True

            hbox:
                spacing 3
                # This iterates through each day in the given list
                # (usually story_archive)
                for day_num, day in enumerate(days):
                    if len(days) < 2:
                        # Center a single day in the middle of the screen
                        null width (config.screen_width//2)-(263//2)-3
                    use day_display(day, day_num)
                    if (main_menu and day_num < len(days) -1):
                        null width -6
                        fixed:
                            xysize (104,32)
                            yalign 0.4
                            add 'day_hlink' xalign 0.5



init python:
    def determine_playable(day):
        """
        A convenience function to reduce screen code. Determines whether
        a given day is playable or not (i.e. has playable TimelineItems).
        """
        if main_menu:
            # This day is selectable if the player has seen at least the
            # first item of the day
            if (day.archive_list
                    and isinstance(day.archive_list[0], TimelineItem)):
                playable = day.archive_list[0].was_played()
            elif (day.archive_list
                    and isinstance(day.archive_list[1], TimelineItem)):
                playable = day.archive_list[1].was_played()
            else:
                playable = False
        else:
            playable = day.has_playable
        return playable

    def determine_today(day, day_num, playable):
        """
        A convenience function to reduce screen code. Determines whether
        a given day is "today" or not.
        """
        if main_menu:
            return False
        if day_num == 0 and not day.archive_list[0].was_played(ever=False):
            return True
        elif day.is_today:
            # Make sure the last item on the previous day was also played.
            if (day_num > 0 and story_archive[day_num-1
                    ].archive_list[-1].was_played(ever=False)):
                return True
            elif day_num == 0:
                return True
            else:
                return False
        elif persistent.real_time and not day.is_today:
            # This might still be today if running in real-time
            if (len(story_archive) > day_num+1
                    and story_archive[day_num+1].archive_list
                    and not story_archive[
                        day_num+1].archive_list[0].available
                    and playable):
                return True


## This screen shows each day as well as a percentage bar showing what
## percent of items on that day have been viewed
screen day_display(day, day_num):

    default most_recent_day = (day_num == today_day_num)
    default playable = determine_playable(day)
    default is_today = determine_today(day, day_num, playable)
    # Background is determined by whether this day is today
    # and whether or not it is playable
    default day_bkgr = 'day_selected' if is_today else 'day_active' if playable else 'day_inactive'
    default day_bkgr_hover = 'day_selected_hover' if is_today else 'day_active_hover' if playable else 'day_inactive'
    default partic_percent = day.participated_percentage()

    if not main_menu:
        on 'show' action [AutoSave()]
        on 'replace' action [AutoSave()]

    vbox:
        spacing 10
        fixed:
            xysize (265,235)
            if is_today:
                # The bouncy 'TODAY' sign
                add 'day_today' align (0.5, 0.0):
                    if day.day == 'Final':
                        yoffset 100
                    else:
                        yoffset 215
            if day.day == 'Final':
                add 'final_day' align (0.5, 0.0) yoffset 145

        textbutton _(day.day_title):
            text_style 'day_title'
            xysize (265,152)
            background day_bkgr padding(-80, 0)
            hover_background day_bkgr_hover
            if playable:
                action [SetVariable('current_day', day),
                        SetVariable('current_day_num', day_num),
                        Show('timeline', day=day, day_num=day_num)]
                activate_sound 'audio/sfx/UI/select_day.mp3'
            else:
                action CConfirm(_("There is no story available on this day yet. Keep playing the game to see more!"))
            xalign 0.5

        # This displays the story completion percentage
        if not main_menu:
            frame:
                style_prefix 'day_percentage'
                xysize (265,35)
                background None
                has hbox
                frame:
                    xysize (180,30)
                    xalign 0.0
                    bar:
                        style 'day_percentage_bar'
                        value partic_percent
                        range 100
                frame:
                    xysize (80, 30)
                    align (0.5, 0.5)
                    background 'day_percent_border'
                    text '[partic_percent]\%'
        fixed:
            xfit True yfit True
            add day.day_icon

    if not main_menu:
        fixed:
            xysize (104,32)
            yalign 0.4
            if (not most_recent_day
                    and day.archive_list
                    and day.archive_list[-1].available
                    and day_num < today_day_num):
                add 'day_hlink' xalign 0.5


style day_percentage_frame:
    background 'day_percent_border'

style day_percentage_hbox:
    align (0.5, 0.5)
    spacing 5

style day_percentage_bar:
    xysize (170, 20)
    align (0.5, 0.5)

style day_percentage_text:
    color '#fff'
    size 20
    xalign 0.5 yalign 0.5

style day_title:
    xalign 0.5
    text_align 0.5
    color '#fff'
    size 37
    font gui.sans_serif_1
    yalign 0.5

default day_select_xadj = ui.adjustment()
default timeline_yadj = ui.adjustment()
########################################################
## This screen shows a timeline of the timeline items
## on each particular day.
########################################################
screen timeline(day, day_num):

    tag menu
    modal True

    if not main_menu:
        on 'show' action [AutoSave()]
        on 'replace' action [AutoSave()]


    default story_time = None if main_menu else next_story_time()
    default return_action = Show('day_select', Dissolve(0.5),
        days=which_history_route) if main_menu else Show('day_select', Dissolve(0.5))

    use menu_header(day.day_title, return_action):
        fixed:
            style_prefix 'timeline2'
            add 'day_vlink' xsize 15 xalign 0.15 yalign 1.0
            viewport:
                yadjustment timeline_yadj
                mousewheel True
                draggable True
                side_spacing 5
                scrollbars "vertical"
                has vbox
                for i, item in enumerate(day.archive_list):
                    # Displays rows of all the available chats
                    if not main_menu and item.available:
                        use timeline_item_display(day, day_num, item, i)
                    # Use a different screen for the History
                    elif (main_menu and display_history(item, i,
                                                        day.archive_list)):
                        use timeline_item_history(item)

                if (not main_menu and persistent.real_time
                        and day_num == today_day_num
                        and not unlock_24_time
                        and not story_time == _('Unknown Time')
                        and not story_time == _('Plot Branch')):
                    hbox:
                        # Show the 'Continue'/Buyahead button
                        use timeline_continue_button(story_time)
                null height 40

    # Show the 'hacked' timeline effects, if the player has them turned
    # on and if applicable.
    if hacked_effect and persistent.hacking_effects:
        timer 10:
            action [Show('tear2', None, 10, -10, 30, 0.4, 0.2, w_timer=0.3),
                    Show('white_squares', w_timer=1.0)] repeat True

        timer 3.0 action [Show('tear2', None, 10, -10, 30, 0.4, 0.2, w_timer=0.3),
                        Show('white_squares', w_timer=1.0)] repeat False

style timeline2_fixed:
    xysize (720, config.screen_height-172+20)
    yalign 0.0
    xalign 0.5
    #yoffset -18

style timeline2_viewport:
    ysize config.screen_height-172+20
    yalign 0.0

style timeline2_vbox:
    xsize 700
    spacing 20

style timeline2_hbox:
    xysize (620, 110)
    xoffset 70
    xalign 0.0


## Displays a single timeline item and all its related timeline items
## (e.g. StoryMode, StoryCalls, etc).
screen timeline_item_display(day, day_num, item, index):

    python:
        # Whether this item occurs in the same hour as the one before it
        sametime = False
        if index > 0:
            # This is the second or later item on the day
            prev_item = day.archive_list[index-1]
            sametime = (item.trigger_time[:2] == prev_item.trigger_time[:2])
            was_played = prev_item.all_played
        elif index == 0 and day_num > 0:
            # This is the first item on a new day, but not the first day
            prev_item = story_archive[day_num-1].archive_list[-1]
            was_played = prev_item.all_played
        else:
            prev_item = None
            was_played = True

        # Some items vary in size depending on if hacked effects are
        # active and whether or not the item has expired
        if hacked_effect and persistent.hacking_effects:
            anim = hacked_anim
        else:
            anim = null_anim

        if item.currently_expired:
            chat_title_width = 300
            chat_box_width = 520
            partic_viewport_width = 430
        else:
            chat_title_width = 400
            chat_box_width = 620
            partic_viewport_width = 530

        # Determine if there are enough participants to make the
        # participant viewport scroll automatically
        part_anim = null_anim
        if isinstance(item, ChatRoom) and item.participants:
            num_participants = len(item.participants)
            if item.participated:
                num_participants += 1
            if num_participants > 6:
                part_anim = participant_scroll

        # ChatRoom story mode displays similarly to solo StoryMode in
        # some cases
        if isinstance(item, StoryMode):
            story_mode = item
            can_play_story_mode = was_played
        elif isinstance(item, ChatRoom) and item.story_mode:
            story_mode = item.story_mode
            can_play_story_mode = (was_played and item.played)
        else:
            can_play_story_mode = True
            story_mode = None

        # StoryCall items display the same if they are alone or not
        if isinstance(item, StoryCall):
            story_calls = [item]
            can_play_calls = was_played
        elif isinstance(item, TimelineItem) and item.story_calls_list:
            story_calls = item.story_calls_list
            can_play_calls = (was_played and item.played
                and can_play_story_mode
                and (not story_mode or story_mode.played))
        else:
            can_play_calls = True
            story_calls = None

        if persistent.unlock_all_story:
            was_played = True
            can_play_calls = True
            can_play_story_mode = True


    style_prefix None

    null height 10

    # Display an extra marker with the hour. If this item is during the
    # same hour as the previous one, this is omitted.
    if not sametime:
        textbutton _(item.trigger_time[:2] + ':00'):
            style 'timeline_button'
            text_style 'timeline_button_text'

    # A ChatRoom
    if isinstance(item, ChatRoom):
        hbox:
            style 'timeline_hbox'
            fixed:
                xysize (chat_box_width, 160)
                frame:
                    background item.timeline_box_bg
                    xysize (chat_box_width, 160)
                button at anim(10):
                    xysize (chat_box_width, 160)
                    xalign 0.0
                    background item.timeline_img(was_played)
                    hover_foreground 'chat_timeline_hover'
                    if item.available and was_played:
                        action [SetVariable('current_timeline_item', item),
                                Jump('play_timeline_item')]
                        if persistent.testing_mode:
                            alternate [SetVariable('current_timeline_item', item),
                                SetVariable('skip_story_item', True),
                                Jump('play_timeline_item')]
                    if (hacked_effect and item.currently_expired
                            and persistent.hacking_effects):
                        add 'day_reg_hacked' xoffset -185 yoffset -178
                    elif hacked_effect and persistent.hacking_effects:
                        add 'day_reg_hacked_long' xoffset -210 yoffset -170

                    vbox:
                        style_prefix 'chat_timeline'
                        # This box displays the trigger time and title of the
                        # chatroom; optionally at a scrolling transform so you
                        # can read the entire title
                        hbox:
                            frame:
                                xoffset 77
                                yoffset 13
                                text item.trigger_time:
                                    size 27
                                    xalign 0.5
                                    text_align 0.5
                            viewport:
                                xysize(chat_title_width,27)
                                if get_text_width(item.title,
                                        'chat_timeline_text') >= chat_title_width:
                                    frame:
                                        xysize(chat_title_width,27)
                                        text item.title at chat_title_scroll
                                else:
                                    text item.title
                        # Shows a list of all the people who were in/
                        # are in this chatroom
                        viewport:
                            xysize(partic_viewport_width, 85)
                            yoffset 13
                            xoffset 77
                            yalign 0.5
                            frame:
                                xysize(partic_viewport_width, 85)
                                hbox at part_anim:
                                    spacing 5
                                    if item.participants:
                                        for person in item.participants:
                                            if person.participant_pic:
                                                add person.participant_pic

                                    if item.participated and item.played:
                                        add m.get_pfp(80)

            # If this chat is expired and hasn't been bought back,
            # show a button allowing the player to buy this chat again
            if item.currently_expired:
                imagebutton:
                    yalign 0.9
                    xalign 0.5
                    idle 'expired_chat'
                    hover_background 'btn_hover:expired_chat'
                    if item.available or persistent.unlock_all_story:
                        action If(persistent.testing_mode,
                            # Just unlock it without a confirmation message
                            [Function(item.buy_back),
                            Function(renpy.retain_after_load),
                            Function(renpy.restart_interaction),
                            AutoSave()],

                            CConfirm(_("Would you like to participate in the chat conversation that has passed?"),
                                [Function(item.buy_back),
                                Function(renpy.retain_after_load),
                                Function(renpy.restart_interaction),
                                AutoSave()]))

    # A lone StoryMode item
    if isinstance(item, StoryMode) and not item.party:
        button:
            style_prefix 'solo_vn'
            foreground 'solo_' + item.timeline_img(can_play_story_mode)
            hover_foreground Fixed('solo_'
                + item.timeline_img(can_play_story_mode), 'solo_vn_hover')
            if item.available and can_play_story_mode:
                # Note: afm is ~30 at its slowest, 0 when it's off,
                # and 1 at its fastest
                # This Preference means the player always has to
                # manually enable auto-forward in a new story mode
                action [SetVariable('current_timeline_item', item),
                        Jump('play_timeline_item')]
                if persistent.testing_mode:
                    alternate [SetVariable('current_timeline_item', item),
                        SetVariable('skip_story_item', True),
                        Jump('play_timeline_item')]
            add item.vn_img align (1.0, 1.0) xoffset 3 yoffset 1
            hbox:
                frame:
                    text item.trigger_time
                viewport:
                    frame:
                        xsize 350
                        if get_text_width(item.title,
                                'chat_timeline_text') >= 350:
                            text item.title at chat_title_scroll
                        else:
                            text item.title

    # A StoryMode connected to a chatroom
    if (isinstance(item, ChatRoom) and item.story_mode
            and not item.story_mode.party):
        frame:
            style_prefix 'reg_timeline_vn'
            has hbox
            add 'vn_marker'
            button:
                foreground item.story_mode.timeline_img(can_play_story_mode)
                hover_foreground (item.story_mode.timeline_img(
                        can_play_story_mode) + '_hover')
                if item.story_mode.available and can_play_story_mode:
                    action [SetVariable('current_timeline_item',
                                item.story_mode),
                            Jump('play_timeline_item')]
                    if persistent.testing_mode:
                        alternate [SetVariable('current_timeline_item',
                                item.story_mode),
                            SetVariable('skip_story_item', True),
                            Jump('play_timeline_item')]
                add item.story_mode.vn_img xoffset -5


    # It's the VN that leads to the party
    if story_mode and story_mode.party:
        frame:
            style_prefix 'party_timeline_vn'
            button:
                background story_mode.timeline_img(can_play_story_mode)
                if story_mode.available and can_play_story_mode:
                    hover_foreground story_mode.timeline_img(can_play_story_mode)
                    action CConfirm(_("If you start the party before answering a guest's emails, that guest will not attend the party. Continue?"),
                            [SetVariable('current_timeline_item',
                                    story_mode),
                                Jump('play_timeline_item')])
                    if persistent.testing_mode:
                        alternate [SetVariable('current_timeline_item', story_mode),
                            SetVariable('skip_story_item', True),
                            Jump('play_timeline_item')]

    # If there are mandatory story calls, display them
    if story_calls:
        for i, phonecall in enumerate(story_calls):
            if i > 0 and not persistent.unlock_all_story:
                $ can_play_calls = (can_play_calls and story_calls[i-1].played)
            use timeline_story_calls(phonecall, item, can_play_calls)


    # There's a plot branch
    if item.plot_branch:
        button:
            xysize(330, 85)
            background 'input_popup_bkgr'
            hover_background 'input_popup_bkgr_hover'
            xalign 0.5
            xoffset 40
            hbox:
                spacing 15
                align (0.5, 0.5)
                add 'plot_lock'
                text 'Tap to unlock' color '#fff' xalign 0.5 yalign 0.5
            # Check if the player has seen all items before
            # they try to branch
            if can_branch():
                # The message varies slightly depending on whether
                # the player is playing in real-time or not
                if persistent.real_time:
                    action If(persistent.testing_mode,
                        # Just unlock the branch
                        [SetVariable('current_timeline_item', item),
                        Jump('execute_plot_branch')],

                        CConfirm(_("The game branches here. Missed story may appear depending on the time right now. Continue?"),
                            [SetVariable('current_timeline_item', item),
                                Jump('execute_plot_branch')]))
                else:
                    action If(persistent.testing_mode,
                        # Just unlock the branch
                        [SetVariable('current_timeline_item', item),
                        Jump('execute_plot_branch')],

                        CConfirm(_("The game branches here. Continue?"),
                        [SetVariable('current_timeline_item', item),
                            Jump('execute_plot_branch')]))
            else:
                action CConfirm(_("Please proceed after completing the unseen old conversations."))

## Screen to display story calls
screen timeline_story_calls(phonecall, item, was_played):
    python:
        if phonecall.currently_expired:
            call_title_width = 300
            call_box_width = 520
        else:
            call_title_width = 400
            call_box_width = 620

    hbox:
        style 'timeline_hbox'
        ysize 111
        button:
            xysize (call_box_width, 111)
            background phonecall.timeline_img(was_played)
            hover_foreground 'story_call_hover'
            if phonecall.available and was_played:
                action [SetVariable('current_timeline_item', phonecall),
                            Jump('play_timeline_item')]
                if persistent.testing_mode:
                    alternate [SetVariable('current_timeline_item', phonecall),
                        SetVariable('skip_story_item', True),
                        Jump('play_timeline_item')]
            hbox:
                yoffset 12 xoffset 78
                spacing 25
                # First add the profile picture of the caller
                fixed:
                    fit_first True
                    add phonecall.caller.participant_pic:
                        xalign 0.0
                    add Transform('call_mainicon', xysize=(28,28)) align (0.01, 0.99)
                vbox:
                    spacing 25
                    hbox:
                        spacing 30
                        # The time of the call
                        $ the_time = phonecall.trigger_time or item.trigger_time
                        text the_time style 'chat_timeline_text'
                        # The name of the caller
                        text phonecall.caller.name style 'chat_timeline_text'
                    # The title of the call, or just "Story Call"
                    fixed:
                        $ the_title = phonecall.title or _("Story Call")
                        text the_title style 'chat_timeline_text'

        if phonecall.currently_expired:
            imagebutton:
                yalign 0.85
                xalign 0.5
                idle 'expired_chat'
                hover_background 'btn_hover:expired_chat'
                if phonecall.available or persistent.unlock_all_story:
                    action If(persistent.testing_mode,
                        [Function(phonecall.buy_back),
                            Function(renpy.retain_after_load),
                            Function(renpy.restart_interaction),
                            AutoSave()],

                        CConfirm(_("Would you like to call {} back to participate in this phone call?".format(phonecall.caller.name)),
                            [Function(phonecall.buy_back),
                            Function(renpy.retain_after_load),
                            Function(renpy.restart_interaction),
                            AutoSave()]))

style chat_timeline_vbox:
    spacing 18

style chat_timeline_hbox:
    is hbox
    spacing 30

style chat_timeline_frame:
    xysize (75,30)
    padding (0,0,0,0)

style chat_timeline_text:
    color '#fff'
    size 25
    yoffset -4
    xalign 0.0 yalign 0.0
    text_align 0.0
    layout 'nobreak'

style chat_timeline_viewport:
    yoffset 13
    xoffset 77

style reg_timeline_vn_frame:
    xysize(700, 160)
    xalign 0.0
    xoffset 10

style reg_timeline_vn_hbox:
    is hbox

style reg_timeline_vn_button:
    xysize(555, 126)
    activate_sound 'audio/sfx/UI/select_vn_mode.mp3'

style party_timeline_vn_frame:
    xysize(600, 300)
    xalign 1.0

style party_timeline_vn_button:
    xysize(463, 185)
    xalign 0.5
    yalign 0.5
    activate_sound 'audio/sfx/UI/select_vn_mode.mp3'


## A small screen intended to reduce the indentation of the timeline screen.
## Shows a button that lets the player purchase the next 24 hours in advance.
screen timeline_continue_button(story_time):
    style_prefix 'timeline_continue'
    button:
        action If(played_all_available(),
            CConfirm(_("Would you like to purchase the next day? You can participate in all  conversations for the next 24 hours."),
                [Function(make_24h_available),
                    Function(check_and_unlock_story),
                    Function(renpy.retain_after_load),
                    Function(renpy.restart_interaction),
                    AutoSave()]),
            CConfirm(_("You have not played all the available story yet.")))
        if hacked_effect and persistent.hacking_effects:
            add Transform('day_reg_hacked_long',
                            yzoom=0.75):
                xoffset -210 yoffset -120
        vbox:
            hbox:
                frame:
                    xysize (75,27)
                    xoffset 77
                    yalign 0.0
                    add Transform("header_hg", zoom=0.8) xalign 0.5 yalign 0.5
                viewport:
                    text _("Continue...")
            frame:
                text _("Next story available at {}".format(story_time))

style timeline_continue_button:
    xysize (620, 110)
    xalign 0.0
    background 'chat_continue'
    hover_background 'btn_hover:chat_continue'

style timeline_continue_vbox:
    spacing 18

style timeline_continue_hbox:
    spacing 30

style timeline_continue_frame:
    xysize(430, 35)
    yoffset 13
    xoffset 75
    yalign 0.5

style timeline_continue_viewport:
    yoffset 13
    xoffset 77
    xysize(400,27)

style timeline_continue_text:
    color '#fff'
    size 25
    xalign 0.0 yalign 0.5
    text_align 0.0
    layout 'nobreak'

default guest_countup = 0
## This label displays all the guests attending the party
label guest_party_showcase():
    hide screen vn_overlay
    show screen guest_count
    python:
        # Make a list of all the guests attending the party
        attending_guests_list = [ x.guest for x in email_list if x.guest.attending ]
        num_guests = len(attending_guests_list)
        guest_countup = 0
        j = 0
        viewing_guest = True


    scene bg guest_walkway
    while (j < num_guests):
        $ guest_countup += 1
        # Show the guest arriving on the scene; there are two different
        # aliases used so the program doesn't replace one guest with the
        # other before hiding them
        if j % 2 == 0:
            show expression attending_guests_list[j].large_img as theguest at guest_enter
        else:
            show expression attending_guests_list[j].large_img as theguest2 at guest_enter

        $ guest_name = attending_guests_list[j].dialogue_name
        $ guest_dialogue = attending_guests_list[j].dialogue_what

        # The guest says their designated dialogue here
        "[guest_name]" "[guest_dialogue]"

        # And then is hidden
        if j % 2 == 0:
            hide theguest
        else:
            hide theguest2
        pause 0.7
        $ j += 1

    # This lets the player see how many guests they gathered
    call screen guests_arrived

    # These guests can now be seen in the guestbook
    python:
        for g in attending_guests_list:
            persistent.guestbook[g.name] = "attended"

    # Achievement for having one or more guests attend
    if num_guests > 0:
        if not first_guest_achievement.has():
            $ first_guest_achievement.grant()
            $ progress_stat_achievement.add_progress(1)

    hide screen guest_count
    $ viewing_guest = False

    if testing_emails:
        return

    # Now jump to the actual party
    if (isinstance(current_timeline_item, StoryMode) and current_timeline_item.party):
        $ print_file("1. Jumping to", current_timeline_item.item_label)
        jump expression current_timeline_item.item_label
    else:
        $ print_file("2. Jumping to", current_timeline_item.story_mode.item_label)
        jump expression current_timeline_item.story_mode.item_label
    return

image rfa_logo = "Phone UI/main03_rfa_logo.webp"
image guest_count_bkgr = "Email/guest_count_bkgr.webp"

## Screen that shows the player the total number of guests
## attending the party
screen guest_count():
    zorder 5

    style_prefix 'guest_display'
    frame:
        has vbox
        hbox:
            xsize config.screen_width
            add 'text_msg_line' xysize (250, 30) yalign 0.5
            add 'rfa_logo'
            add 'text_msg_line' xysize (250, 30) yalign 0.5
        frame:
            style_prefix 'guest_header'
            text _("GUEST COUNT")
        hbox:
            style_prefix 'guest_count'
            text "( " font gui.serif_2xb
            hbox:
                fixed:
                    text str(guest_countup // 10) style 'guest_digi_text'
                    text '8' style 'guest_digi_text' color "#5ef4d31f"
                fixed:
                    text str(guest_countup % 10) style 'guest_digi_text'
                    text '8' style 'guest_digi_text' color "#5ef4d31f"
            text " )" font gui.serif_2xb

style guest_display_frame:
    xysize (config.screen_width, 280)
    align (0.5, 0.01)

style guest_display_vbox:
    spacing 15

style guest_header_frame:
    xysize (328, 40)
    xalign 0.5
    background 'guest_count_bkgr'

style guest_header_text:
    color "#fff"
    align (0.5, 0.5)
    font gui.sans_serif_1b

style guest_count_hbox:
    xalign 0.5
    xysize (100, 97)
    spacing 0

style guest_count_text:
    color "#fff"
    font "fonts/DigitalRegular.ttf"
    size 95

style guest_count_fixed:
    xysize (50, 97)

style guest_digi_text:
    is guest_count_text
    color "#5ef4d3"
    align (1.0, .5)

## Shows the number of guests who arrived at the party
## and a grade based on that number
screen guests_arrived():
    style_prefix "sig_screen"
    add "choice_darken"
    frame:
        has vbox
        first_spacing 10
        spacing 5
        null height 65
        text _("Party Guest Result"):
            if persistent.custom_footers:
                color "#fff"
            font gui.blocky_font size 30
        hbox:
            style_prefix "guest_num"
            frame:
                yalign 0.85
                text "{:02d}".format(guest_countup)
            frame:
                add 'party_grade'

        text _("All the guests have arrived."):
            if persistent.custom_footers:
                color "#fff"
            size 30

        textbutton _('sign'):
            if persistent.custom_footers:
                text_color "#fff"
            action Return()

style guest_num_hbox:
    align (.5, .5)
    spacing 10
    ysize 118

style guest_num_text:
    is guest_count_text
    size 110
    color "#5ef4d3"

transform guest_enter:
    on show:
        xpos 1.0 xanchor 0.0 yalign 0.5 yoffset 40
        linear 0.7 xalign 0.5 yalign 0.5 xoffset 0 yoffset 40
    on hide:
        linear 0.7 yalign 0.5 xpos 0.0 xanchor 1.0  yoffset 40


