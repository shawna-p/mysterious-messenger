########################################################
## This is the screen where you choose which day to play
########################################################
screen chat_select(days=chat_archive):

    tag menu
    modal True

    # If the player isn't on the main menu (aka viewing this screen
    # from the history), the game should save
    if not main_menu:
        on 'show' action [FileSave(mm_auto, confirm=False)]
        on 'replace' action [FileSave(mm_auto, confirm=False)]
        $ return_action = Show('chat_home', Dissolve(0.5))
    else:
        $ return_action = Show('select_history_route', Dissolve(0.5))

    use menu_header("Day List", return_action):  
        viewport:
            xysize (720, 1100)
            yalign 0.85
            xalign 0.5
            mousewheel "horizontal"
            scrollbars "horizontal"
            draggable True
            
            hbox:
                spacing 3
                # This iterates through each day in the given list
                # (usually chat_archive)
                for day_num, day in enumerate(days):
                    use day_select(day, day_num)
                    if (main_menu and day_num < len(days) -1):
                        null width -6
                        fixed:
                            xysize (104,32)
                            yalign 0.4
                            add 'day_hlink' xalign 0.5

style hscrollbar:
    unscrollable "hide"
                    
                
## This screen shows each day as well as a percentage
## bar showing what percent of chatrooms on that day
## have been viewed
screen day_select(day, day_num):

    python:
        num_chatrooms = len(day.archive_list)
        completed_chatrooms = 0
        played_chatrooms = 0
        is_today = False
        playable = False
        most_recent_day = False

        if not main_menu:
            # Calculate the completion percentage
            for index, i in enumerate(day.archive_list):
                if i.played and not i.expired:
                    completed_chatrooms += 1
                if i.played:
                    played_chatrooms += 1
                # This also lets the program know if the player
                # should be able to click on this day
                if i.available:
                    playable = True
            if day_num == today_day_num:
                most_recent_day = True

            # Do they still have chats to play on this day?
            # If so, it's "today"
            if played_chatrooms == len(day.archive_list):
                # All the chatrooms on this day are played;
                # it's not the current day unless there's
                # a plot branch or an unplayed VN
                if day.archive_list:
                    if day.archive_list[-1].plot_branch:
                        is_today = True
                    elif (day.archive_list[-1].vn_obj 
                            and not day.archive_list[-1].vn_obj.played):
                        is_today = True

            elif played_chatrooms == 0:
                # None of the chatrooms in this day have been
                # played; it's only today if all the chatrooms
                # from the previous day are played
                # If this is the first day, it's today
                if day_num == 0:
                    is_today = True
                # Last chat in the previous day is played; it's today
                elif (chat_archive[day_num-1].archive_list 
                        and chat_archive[day_num-1].archive_list[-1].played 
                        and (not chat_archive[day_num
                                            -1].archive_list[-1].vn_obj 
                        or (chat_archive[day_num-1].
                            archive_list[-1].vn_obj.played))):
                    is_today = True
                else:
                    is_today = False
            
            # Otherwise, this day is today if there are unplayed
            # chatrooms left on it
            elif played_chatrooms < len(day.archive_list):
                is_today = True
            
            # Calculate the completion percentage, rounded to an int
            if day.archive_list:
                chat_percent = str(completed_chatrooms * 100 // num_chatrooms)
            else:
                chat_percent = '0'
                num_chatrooms = 1

        else:
            is_today = False
            # If the player has at least seen the first chat of this day,
            # it is selectable ("playable")
            if (main_menu and len(day.archive_list) > 1
                    and not isinstance(day.archive_list[0], ChatHistory)
                    and not isinstance(day.archive_list[0], 
                        store.ChatHistory)):
                if (persistent.completed_chatrooms.get(
                        day.archive_list[1].chatroom_label)
                        or persistent.completed_chatrooms.get(
                            day.archive_list[1].expired_chat)):
                    playable = True                
            elif (main_menu and day.archive_list 
                    and (persistent.completed_chatrooms.get(
                                day.archive_list[0].chatroom_label)
                    or persistent.completed_chatrooms.get(
                                day.archive_list[0].expired_chat))):
                playable = True
            elif (not main_menu and day.archive_list 
                    and day.archive_list[0].played):
                playable = True
            else:
                playable = False

        # Background is determined by whether this day is today
        # and whether or not it is playable
        if is_today:
            day_bkgr = 'day_selected'
            day_bkgr_hover = 'day_selected_hover'
        elif playable:
            day_bkgr = 'day_active'
            day_bkgr_hover = 'day_active_hover'
        else:
            day_bkgr = 'day_inactive'
            day_bkgr_hover = 'day_inactive'

    vbox:
        spacing 10
        vbox:
            xysize (265,235)
            if is_today and day.day != 'Final':
                # This is the bouncy "TODAY" sign
                add 'day_today' xalign 0.5 yalign 1.0
            elif is_today and day.day == 'Final':
                # This ensures the Final/Today signs don't
                # conflict with each other
                add 'day_today' xalign 0.5 yalign 1.0 yoffset 50
                add 'final_day' xalign 0.5 yalign 1.0
            elif day.day == 'Final':
                # Adds the 'Final' sign to the final day
                add 'final_day' xalign 0.5 yalign 1.0
                
        textbutton _(day.day + " Day"):
            text_style 'day_title'
            xysize (265,152)
            background day_bkgr padding(-80, 0)
            hover_background day_bkgr_hover
            if ((main_menu and playable)
                    or (day.archive_list 
                        and (isinstance(day.archive_list[0], ChatHistory)
                            or isinstance(day.archive_list[0], 
                                store.ChatHistory))
                        and day.archive_list[0].available)):                
                action [SetVariable('current_day', day), 
                        SetVariable('current_day_num', day_num),
                        Show('chatroom_timeline', day=day, day_num=day_num)]
                activate_sound 'audio/sfx/UI/select_day.mp3'
            else:
                action Show("confirm", message=("There are no chatrooms "
                    + "available on this day yet. Keep playing the game"
                    + " to see more!"),
                yes_action=Hide('confirm'))
            xalign 0.5
        
        # This displays the chatroom completion percentage
        if not main_menu:
            frame:
                xysize (265,35)                      
                has hbox
                align (0.5, 0.5)
                spacing 5
                frame:
                    xysize (180,35)
                    xalign 0.0
                    background 'day_percent_border'
                    ypadding 2                    
                    bar:
                        value completed_chatrooms
                        range num_chatrooms
                        xysize (170, 20)
                        align (0.5, 0.5)
                frame:
                    xysize (80, 30)
                    align (0.5, 0.5)
                    background 'day_percent_border'
                    text '[chat_percent]%':
                        color '#fff' 
                        size 20 
                        xalign 0.5 yalign 0.5
                
        fixed:
            xfit True
            yfit True
            add day.day_icon


            
    if (not most_recent_day 
            and day.archive_list 
            and day.archive_list[-1].available):
        fixed:
            xysize (104,32)
            yalign 0.4
            
            add 'day_hlink' xalign 0.5
    elif not main_menu:
        null width 104
        
            
style day_title:
    xalign 0.5
    text_align 0.5
    color '#fff'
    size 37
    font gui.sans_serif_1
    yalign 0.5        
        
########################################################
## This screen shows a timeline of the chatrooms on
## each particular day
########################################################
screen chatroom_timeline(day, day_num):

    tag menu
    modal True
    
    if not main_menu:
        on 'show' action [FileSave(mm_auto, confirm=False)]
        on 'replace' action [FileSave(mm_auto, confirm=False)]

        $ chat_time = next_chat_time()
        $ return_action = Show('chat_select', Dissolve(0.5))
    else:
        $ chat_time = None
        $ return_action = Show('chat_select', Dissolve(0.5),
                            days=which_history_route)
    
    use menu_header(day.day, return_action):
        null height -19
        fixed:   
            xysize (720, 1190)
            yalign 0.0
            xalign 0.5   
            add 'day_vlink' size (15,1180) xalign 0.15
            viewport:
                ysize 1190
                yadjustment yadj            
                mousewheel True
                draggable True    
                side_spacing 5
                scrollbars "vertical"        
                vbox:
                    xsize 700
                    spacing 20      
                            
                    for index, chatroom in enumerate(day.archive_list):
                        # Displays rows of all the available chats
                        if not main_menu and chatroom.available:
                            use chatroom_item(day, day_num, chatroom, index)
                        # Use a different screen for the History
                        elif (main_menu and display_history(chatroom, index,
                                                            day.archive_list)):
                            use chatroom_item_history(chatroom)

                    if (not main_menu and persistent.real_time 
                            and day_num == today_day_num 
                            and not unlock_24_time 
                            and not chat_time == 'Unknown Time'
                            and not chat_time == 'Plot Branch'):
                        hbox:
                            xysize (620, 110)
                            xoffset 70
                            xalign 0.0
                            # Shows the 'Continue'/Buyahead button
                            use timeline_continue_button(chat_time)                        
                                
                    null height 40                    
    
    if hacked_effect and persistent.hacking_effects:        
        timer 10:
            action [Show('tear', number=10, offtimeMult=0.4, 
                    ontimeMult=0.2, offsetMin=-10, offsetMax=30, w_timer=0.3),
                    Show('white_squares', w_timer=1.0)] repeat True
                    
        timer 3.0 action [Show('tear', number=10, offtimeMult=0.4, 
                          ontimeMult=0.2, offsetMin=-10, offsetMax=30, 
                          w_timer=0.3),
                            Show('white_squares', w_timer=1.0)] repeat False



## Small screen largely intended to reduce the indentation
## in the main screen; determines whether or not this chat
## was played, what day it was, etc
screen chatroom_item(day, day_num, chatroom, index):
    python:
        sametime = False
        wasplayed = False
        vn_background = ''
        if index > 0:
            # If this is the second or later chatroom, check if the
            # chatroom just before this one occured in the same hour
            if (chatroom.trigger_time[:2] 
                == day.archive_list[index-1].trigger_time[:2]):
                sametime = True
            # Also check if the chatroom or VN before this chatroom
            # was played
            if day.archive_list[index-1].played:
                if day.archive_list[index-1].vn_obj:
                    wasplayed = day.archive_list[index-1].vn_obj.played
                else:
                    wasplayed = True
        elif index == 0:
            # This chatroom can be played if it's the very first
            # chatroom of the route
            if day_num == 0:
                wasplayed = True
            # Otherwise, check if the last chatroom of the previous
            # day was played so the player can play this one
            else:
                if chat_archive[day_num-1].archive_list[-1].vn_obj:
                    wasplayed = (chat_archive[day_num-1].
                                    archive_list[-1].vn_obj.played)
                else:
                    wasplayed = (chat_archive[day_num-1].
                                    archive_list[-1].played)

        anim = null_anim
        if hacked_effect and persistent.hacking_effects:
            anim = hacked_anim
        my_vn = chatroom.vn_obj
        can_play = False
        # Several items vary in width if the chatroom is expired
        # or if hack effects are active
        chat_title_width = 400
        chat_box_width = 620
        partic_viewport_width = 530
        if chatroom.expired:
            chat_title_width = 300
            chat_box_width = 520
            partic_viewport_width = 430
            
        # These statements determine how the VN mode
        # should look -- active/inactive etc
        if my_vn and not my_vn.party:
            if my_vn.played:
                vn_foreground = 'vn_active'
                vn_hover = 'vn_active_hover'   
                can_play = True
            elif my_vn.available and wasplayed and chatroom.played:
                vn_foreground = 'vn_selected'
                vn_hover = 'vn_selected_hover'
                can_play = True
            elif chatroom.expired:
                vn_foreground = 'vn_inactive'
                vn_hover = 'vn_inactive'
            else:
                vn_foreground = 'vn_inactive'
                vn_hover = 'vn_inactive'
        elif my_vn and my_vn.party:
            if my_vn.available:
                vn_background = 'vn_party'
                can_play = True
            elif not my_vn.available:
                vn_background = 'vn_party_inactive'
                
        # These statements determine how a chatroom button
        # should look -- active/inactive/etc
        if chatroom.played:
            chat_bkgr = 'chat_active'
            chat_hover = 'chat_active_hover'  
            can_play = True            
        elif chatroom.available and wasplayed:
            chat_bkgr = 'chat_selected'
            chat_hover = 'chat_selected_hover'
            can_play = True
        elif chatroom.expired:
            chat_bkgr = 'chat_inactive'
            chat_hover = 'chat_inactive'
        else:
            chat_bkgr = 'chat_inactive'
            chat_hover = 'chat_inactive'
        
        # This determines if there are enough participants
        # in this chat to make the viewport scroll automatically
        if chatroom.participants:
            if (len(chatroom.participants) > 5 and chatroom.participated):
                part_anim = participant_scroll
            elif ((len(chatroom.participants) > 6
                     and not chatroom.participated)
                     or (chatroom.expired and len(chatroom.participants) > 4)):
                part_anim = participant_scroll
            else:
                part_anim = null_anim
        else:
            part_anim = null_anim

        if persistent.testing_mode and chat_bkgr == 'chat_inactive':
            chat_bkgr = 'chat_active'
            chat_hover = 'chat_active_hover'
            can_play = True
            wasplayed = True
        if persistent.testing_mode:
            most_recent_chat = chatroom
            can_play = True
            wasplayed = True
        if (persistent.testing_mode and my_vn 
                and (vn_foreground == 'vn_inactive' 
                    or vn_background == 'vn_party_inactive')):
            if vn_foreground == 'vn_inactive':
                vn_foreground = 'vn_active'
                vn_hover = 'vn_active_hover'
            elif vn_background == 'vn_party_inactive':
                vn_background = 'vn_party'
            can_play = True
            wasplayed = True

    null height 10
                      
    if not sametime:
        # sametime means these chatrooms occur during the
        # same hour. If it's false, show the hour above this chat
        textbutton _(chatroom.trigger_time[:2] + ':00'):
            style 'timeline_button'
            text_style 'timeline_button_text'
        
    hbox:
        style 'timeline_hbox'
        button at anim(10):
            xysize (chat_box_width, 160)
            xalign 0.0
            background chat_bkgr
            hover_foreground chat_hover
            if can_play and wasplayed:
                # Determines where to take the player depending
                # on whether this chatroom is expired or not
                if chatroom.expired and not chatroom.played:
                    action [SetVariable('current_chatroom', chatroom), 
                            Jump(chatroom.expired_chat)]
                else:
                    if (chatroom.played 
                            and not persistent.testing_mode
                            and chatroom.replay_log != []):
                        action [SetVariable('current_chatroom', chatroom),
                            SetVariable('observing', True),
                            Jump('rewatch_chatroom')]
                    else:
                        action [SetVariable('current_chatroom', chatroom), 
                                Jump(chatroom.chatroom_label)]
                    
            if (hacked_effect and chatroom.expired 
                    and persistent.hacking_effects):
                add 'day_reg_hacked' xoffset -185 yoffset -178
            elif hacked_effect and persistent.hacking_effects:
                add 'day_reg_hacked_long' xoffset -210 yoffset -170
                
            vbox:
                spacing 18
                # This box displays the trigger time and title of the
                # chatroom; optionally at a scrolling transform so you 
                # can read the entire title
                hbox:
                    spacing 30
                    frame:
                        xysize (75,27)
                        xoffset 77
                        yoffset 13
                        text chatroom.trigger_time:
                            color '#fff' 
                            size 27 
                            xalign 0.5 yalign 0.5 
                            text_align 0.5
                    viewport:
                        yoffset 13
                        xoffset 77                
                        xysize(chat_title_width,27)
                        if len(chatroom.title) > 30: 
                            frame:
                                xysize(chat_title_width,27)
                                text chatroom.title at chat_title_scroll:
                                    color '#fff' 
                                    size 25 
                                    xalign 0.0 yalign 0.5 
                                    text_align 0.0 
                                    layout 'nobreak' 
                        else:
                            text chatroom.title:
                                color '#fff' 
                                size 25 
                                xalign 0.0 yalign 0.5 
                                text_align 0.0 
                                layout 'nobreak'
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
                            if chatroom.participants:
                                for person in chatroom.participants:
                                    if person.participant_pic:
                                        add person.participant_pic
                                
                            if chatroom.participated and chatroom.played:
                                add m.get_pfp(80)

        # If this chat is expired and hasn't been bought back,
        # show a button allowing the player to buy this chat again            
        if chatroom.expired and not chatroom.buyback:
            imagebutton:
                yalign 0.9
                xalign 0.5
                idle 'expired_chat'
                hover_background 'btn_hover:expired_chat'
                if chatroom.available or persistent.testing_mode:
                    action Show('confirm', message=("Would you like to"
                                + " participate in the chat conversation"
                                + " that has passed?"),
                            yes_action=[SetField(chatroom, 'expired', False),
                            SetField(chatroom, 'buyback', True),
                            SetField(chatroom, 'played', False),
                            SetField(chatroom, 'replay_log', []),
                            Function(chatroom.reset_participants),
                            renpy.retain_after_load,
                            renpy.restart_interaction, Hide('confirm')], 
                            no_action=Hide('confirm'))

    # If there's a VN object, display it now
    if my_vn and not my_vn.party:
        frame:
            xysize(700, 160)
            xalign 0.0
            xoffset 10
            
            has hbox
            add 'vn_marker'
            
            button:
                xysize(555, 126)
                foreground vn_foreground
                hover_foreground vn_hover
                activate_sound 'audio/sfx/UI/select_vn_mode.mp3'
                if (my_vn.available 
                        and can_play 
                        and chatroom.played):
                    # Note: afm is ~30 at its slowest, 0 when it's off, 
                    # and 1 at its fastest
                    # This Preference means the player always has to
                    # manually enable auto-forward in a new story mode
                    action [Preference("auto-forward", "disable"), 
                            SetVariable('current_chatroom', chatroom), 
                            Jump(my_vn.vn_label)]      
                
                if my_vn.who:
                    add 'vn_' + my_vn.who.file_id xoffset -5
                else:
                    add 'vn_other' xoffset -5
    
    # It's the VN that leads to the party
    if my_vn and my_vn.party:
        frame:
            xysize(600, 300)
            xalign 1.0
           
            button:
                xysize(463, 185)
                xalign 0.5
                yalign 0.5
                background vn_background                
                activate_sound 'audio/sfx/UI/select_vn_mode.mp3'
                if my_vn.available and can_play:
                    hover_foreground vn_background
                    # Note: afm is ~30 at its slowest, 0 when it's off, 
                    # and 1 at its fastest
                    action Show('confirm', message=("If you start the party"
                        + " before answering a guest's emails, that guest will"
                        + " not attend the party. Continue?"),
                        yes_action=[Preference("auto-forward", "disable"), 
                            SetVariable('current_chatroom', chatroom),
                            Hide('confirm'), 
                            Jump('guest_party_showcase')],
                            #Jump(my_vn.vn_label)],
                        no_action=Hide('confirm'))
            
        
    # There's a plot branch
    if chatroom.plot_branch:
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
            # Check if the player has seen all chatrooms before
            # they try to branch
            if can_branch() or persistent.testing_mode:
                # The message varies slightly depending on whether
                # the player is playing in real-time or not
                if persistent.real_time:
                    action Show("confirm", message=("The game branches here."
                                + " Missed chatrooms may appear depending on"
                                + " the time right now. Continue?"), 
                            yes_action=[Hide('confirm'), 
                            SetVariable('most_recent_chat', chatroom),
                            SetVariable('current_chatroom', chatroom),
                            Jump(chatroom.chatroom_label + '_branch')], 
                            no_action=Hide('confirm'))           
                else:
                    action Show("confirm", message=("The game branches here."
                            + " Continue?"), 
                        yes_action=[Hide('confirm'), 
                        SetVariable('current_chatroom', chatroom),
                        SetVariable('most_recent_chat', chatroom),
                        Jump(chatroom.chatroom_label + '_branch')], 
                        no_action=Hide('confirm'))                 
            else:
                action Show("confirm", message=("Please proceed after"
                            + " completing the unseen old conversations."),
                        yes_action=Hide('confirm'))

## A small screen intended to reduce the indentation of 
## the chatroom_timeline screen. Shows a button that
## lets the player purchase the next 24 hours/continue
screen timeline_continue_button(chat_time):
    button:
        xysize (620, 110)
        xalign 0.0
        background 'chat_continue'
        hover_background 'btn_hover:chat_continue'
        action Show("confirm", message=("Would you like to purchase the next"
                                + " day? You can participate in all the chat"
                                + " conversations for the next 24 hours."), 
                yes_action=[Function(chat_24_available), 
                    renpy.retain_after_load, 
                    renpy.restart_interaction, 
                    Hide('confirm')], 
                no_action=Hide('confirm'))    
        if hacked_effect and persistent.hacking_effects:
            add Transform('day_reg_hacked_long', 
                            yzoom=0.75):
                xoffset -210 yoffset -120            
        vbox:
            spacing 18
            hbox:
                spacing 30
                frame:
                    xysize (75,27)
                    xoffset 77
                    yoffset 13
                    add Transform("header_hg", zoom=0.8) xalign 0.5 yalign 0.5
                viewport:
                    yoffset 13
                    xoffset 77                
                    xysize(400,27)
                    text "Continue...":
                        color '#fff' 
                        size 25 
                        xalign 0.0 yalign 0.5 
                        text_align 0.0 
                        layout 'nobreak'
            frame:
                xysize(430, 35)
                yoffset 13
                xoffset 75       
                yalign 0.5
                text "Next chatroom opens at " + chat_time:
                    color '#fff' 
                    size 25 
                    yalign 0.5 
                    text_align 0.0
    
## This is used to continue the game after a plot branch    
label plot_branch_end():
    python:
        # CASE 1
        # Plot branch is just a chatroom, has an after label
        if not current_chatroom.vn_obj:
            if renpy.has_label('after_' + current_chatroom.chatroom_label):
                was_expired = current_chatroom.expired
                renpy.call('after_' + current_chatroom.chatroom_label)
                was_expired = False
            # Deliver calls/texts/etc
            deliver_calls(current_chatroom.chatroom_label)
            deliver_emails()   
        # CASE 2
        # Plot branch is after a chatroom, after branching there's a VN
        elif current_chatroom.vn_obj and not current_chatroom.vn_obj.played:
            # Don't deliver anything yet
            pass
        # CASE 3
        # Plot branch is after a chatroom with a VN
        elif current_chatroom.vn_obj and current_chatroom.vn_obj.played:
            if renpy.has_label('after_' + current_chatroom.chatroom_label):
                was_expired = current_chatroom.expired
                renpy.call('after_' + current_chatroom.chatroom_label)
                was_expired = False
            # Deliver calls/texts/etc
            deliver_calls(current_chatroom.chatroom_label)
            deliver_emails()

        # Now check if the player unlocked the next 24 hours
        # of chatrooms, and make those available
        if unlock_24_time:
            chat_24_available(reset_24=False)           
        next_chatroom()
        renpy.retain_after_load
        
    call screen chat_select
    return
                

default guest_countup = 0
## This label displays all the guests attending the party
label guest_party_showcase():
    call vn_begin
    hide screen vn_overlay
    show screen guest_count
    python:
        # Make a list of all the guests attending the party
        attending_guests = [ x.guest for x in email_list if x.guest.attending ]
        num_guests = len(attending_guests)
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
            show expression attending_guests[j].large_img as theguest at guest_enter
        else:
            show expression attending_guests[j].large_img as theguest2 at guest_enter
        
        $ guest_name = attending_guests[j].dialogue_name
        $ guest_dialogue = attending_guests[j].dialogue_what

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
        for g in attending_guests:
            persistent.guestbook[g.name] = "attended"

    hide screen guest_count
    $ viewing_guest = False

    # Now jump to the actual party
    $ renpy.jump(current_chatroom.vn_obj.vn_label)


image rfa_logo = "Phone UI/main03_rfa_logo.png"
image guest_count_bkgr = "Email/guest_count_bkgr.png"

# It seems 15+ guests is A grade and 6- guests is D grade
# This program has its own arbitrary grade calculations instead
image party_grade = ConditionSwitch(
    "guest_countup >= 20", "Email/a_grade.png",
    "guest_countup >= 10", "Email/b_grade.png",
    "guest_countup >= 5", "Email/c_grade.png",
    "guest_countup >= 2", "Email/d_grade.png",
    True, "Email/e_grade.png",
)

## Screen that shows the player the total number of guests
## attending the party
screen guest_count():
    zorder 5

    style_prefix 'guest_display'
    frame:
        has vbox
        hbox:
            xsize 750
            add 'text_msg_line' size (250, 30) yalign 0.5
            add 'rfa_logo'
            add 'text_msg_line' size (250, 30) yalign 0.5
        frame:
            style_prefix 'guest_header'            
            text "GUEST COUNT" 
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
    xysize (750, 280)
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
        spacing 10
        null height 80
        text "Party Guest Result":
            if persistent.custom_footers:
                color "#fff"
            font gui.blocky_font size 30
        hbox:
            style_prefix "guest_num"            
            frame:
                text "{:02d}".format(guest_countup)
            frame:
                add 'party_grade'
        
        text "All the guests have arrived.":
            if persistent.custom_footers:
                color "#fff"
            size 30
        
        textbutton _('sign'): 
            if persistent.custom_footers:
                text_color "#fff"
            action Return()

style guest_num_hbox:
    align (.5, .5)
    spacing 30
    ysize 118

style guest_num_text:
    is guest_count_text
    size 110
    color "#5ef4d3"
    
transform guest_enter:
    on show:
        xalign 1.0 yalign 0.6 xoffset 350
        linear 0.7 xalign 0.5 yalign 0.6 xoffset 0
    on hide:
        linear 0.7 xalign 0.0 yalign 0.6 xoffset -350

    
        
                
