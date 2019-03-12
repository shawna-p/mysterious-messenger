########################################################
## This is the screen where you choose which day to play
########################################################
screen chat_select():

    tag menu
    modal True
    
    use starry_night()
    
    use menu_header("Day List", Show('chat_home', Dissolve(0.5)))
    
    python:
        if renpy.music.get_playing(channel='music') != mystic_chat:
            renpy.music.play(mystic_chat, loop=True)
    
    fixed:
        viewport:
            xysize (720, 1100)
            yalign 0.85
            xalign 0.5
            mousewheel "horizontal"
            draggable True
            
            hbox:
                spacing 3
                for day_num, day in enumerate(chat_archive):
                    use day_select(day, day_num)
                
                
                
screen day_select(day, day_num):

    python:
        num_chatrooms = len(day.archive_list)
        completed_chatrooms = 0
        played_chatrooms = 0
        is_today = False
        playable = False
        most_recent_day = False
        for index, i in enumerate(day.archive_list):
            if i.played and not i.expired:
                completed_chatrooms += 1
            if i.played:
                played_chatrooms += 1
            if i.available:
                playable = True
        if day_num == today_day_num:
            most_recent_day = True
        # Do they still have chats to play on this day?
        # If so, it's "today"
        if played_chatrooms == len(day.archive_list):
            # All the chatrooms in this day are played;
            # it's not the current day unless there's
            # a plot branch or an unplayed VN
            if day.archive_list:
                if day.archive_list[-1].plot_branch:
                    is_today = True
                elif day.archive_list[-1].vn_obj and not day.archive_list[-1].vn_obj.played:
                    is_today = True
        elif played_chatrooms == 0:
            # None of the chatrooms in this day have been
            # played; it's only today if all the chatrooms
            # from the previous day are played
            # If this is the first day, it's today
            if day_num == 0:
                is_today = True
            # Last chat in the previous day is played; it's today
            elif chat_archive[day_num-1].archive_list and chat_archive[day_num-1].archive_list[-1].played and (not chat_archive[day_num-1].archive_list[-1].vn_obj or chat_archive[day_num-1].archive_list[-1].vn_obj.played):
                is_today = True
            else:
                is_today = False
        elif played_chatrooms < len(day.archive_list):
            is_today = True
        
        if day.archive_list:
            chat_percent = str(completed_chatrooms * 100 // num_chatrooms)
        else:
            chat_percent = '0'
            num_chatrooms = 1
            
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
                add 'day_today' xalign 0.5 yalign 1.0
            elif is_today and day.day == 'Final':
                add 'day_today' xalign 0.5 yalign 1.0 yoffset 50
                add 'final_day' xalign 0.5 yalign 1.0
            if day.day == 'Final':
                add 'final_day' xalign 0.5 yalign 1.0
                
        textbutton _(day.day + " Day"):
            text_style 'day_title'
            xysize (265,152)
            background day_bkgr padding(-80, 0)
            hover_background day_bkgr_hover
            if day.archive_list and day.archive_list[0].available:
                action [SetVariable('current_day', day), SetVariable('current_day_num', day_num),
                        Show('chatroom_timeline', day=day, day_num=day_num)]
                activate_sound 'sfx/UI/select_day.mp3'
            xalign 0.5
        
        viewport:
            xysize (265,35)                      
            has hbox
            align (0.5, 0.5)
            spacing 5
            fixed:
                xysize (180,35)
                xalign 0.0
                fixed:
                    xysize (180, 30)
                    align (0.5, 0.5)
                    add 'day_percent_border'
                bar:
                    value completed_chatrooms
                    range num_chatrooms
                    xysize (170, 20)
                    align (0.5, 0.5)
            fixed:
                xysize (80, 30)
                align (0.5, 0.5)
                add 'day_percent_border'
                text '[chat_percent]%' color '#fff' size 20 xalign 0.5 yalign 0.5
                
        fixed:
            xfit True
            yfit True
            add day.route


            
    
    fixed:
        xysize (104,32)
        yalign 0.4
        if not most_recent_day and day.archive_list and day.archive_list[-1].available:
            add 'day_hlink' xalign 0.5
            
        
        
########################################################
## This screen shows a timeline of the chatrooms on
## each particular day
########################################################
screen chatroom_timeline(day, day_num):

    tag menu
    modal True
    
    use starry_night()
    
    use menu_header(day.day, Show('chat_select', Dissolve(0.5)))
    
    #$ yadj.value = yadjValue
    $ chat_time = next_chat_time()
   
        
    fixed:   
        xysize (720, 1180)
        yalign 1.0
        xalign 0.5   
        add 'day_vlink' xalign 0.15
        viewport yadjustment yadj:
            
            mousewheel True
            draggable True
            
            vbox:
                xsize 720
                spacing 20                
                for index, chatroom in enumerate(day.archive_list):
                    $ same_time = False
                    $ was_played = False
                    if chatroom.available:
                        if index > 0:
                            if chatroom.trigger_time[:2] == day.archive_list[index-1].trigger_time[:2]:
                                $ same_time = True
                            if day.archive_list[index-1].played:
                                if day.archive_list[index-1].vn_obj:
                                    $ was_played = day.archive_list[index-1].vn_obj.played
                                else:
                                    $ was_played = True
                        elif index == 0:
                            if day_num == 0:
                                $ was_played = True
                            else:
                                if chat_archive[day_num-1].archive_list[-1].vn_obj:
                                    $ was_played = chat_archive[day_num-1].archive_list[-1].vn_obj.played
                                else:
                                    $ was_played = chat_archive[day_num-1].archive_list[-1].played
                        
                        use chatroom_display(chatroom, same_time, was_played)
                if persistent.real_time and day_num == today_day_num and not (day.archive_list[-1].plot_branch and day.archive_list[-1].available) and not unlock_24_time and not chat_time == 'Unknown Time':
                    hbox:
                        xysize (620, 110)
                        xoffset 70
                        xalign 0.0
                        button:
                            xysize (620, 110)
                            xalign 0.0
                            background 'chat_continue'
                            hover_foreground 'chat_continue'
                            action Show("confirm", message="Would you like to purchase the next day? You can participate in all the chat conversations for the next 24 hours.", 
                                    yes_action=[Function(chat_24_available), renpy.retain_after_load, renpy.restart_interaction, Hide('confirm')], 
                                    no_action=Hide('confirm'))    
                            if hacked_effect:
                                add Transform('Phone UI/Day Select/chatlist_hacking_long.png', yzoom=0.75) xoffset -210 yoffset -120            
                            vbox:
                                spacing 18
                                hbox:
                                    spacing 30
                                    window:
                                        xysize (75,27)
                                        xoffset 77
                                        yoffset 13
                                        add Transform("Phone UI/Main Menu/header_hg.png", zoom=0.8) xalign 0.5 yalign 0.5
                                    viewport:
                                        yoffset 13
                                        xoffset 77                
                                        xysize(400,27)
                                        text "Continue..." color '#fff' size 25 xalign 0.0 yalign 0.5 text_align 0.0 layout 'nobreak'
                                window:
                                    xysize(430, 35)
                                    yoffset 13
                                    xoffset 50        
                                    yalign 0.5
                                    text "Next chatroom opens at " + chat_time color '#fff' size 25 yalign 0.5 text_align 0.0
                            
                null height 40                    
    
    if hacked_effect:        
        timer 10:
            action [Show('tear', number=10, offtimeMult=0.4, ontimeMult=0.2, offsetMin=-10, offsetMax=30, w_timer=0.3),
                    Show('white_squares', w_timer=1.0)] repeat True
                    
        timer 3.0 action [Show('tear', number=10, offtimeMult=0.4, ontimeMult=0.2, offsetMin=-10, offsetMax=30, w_timer=0.3),
                            Show('white_squares', w_timer=1.0)] repeat False
                    
screen chatroom_display(mychat, sametime=False, wasplayed=False):

    python:
        anim = null_anim
        if hacked_effect:
            anim = hacked_anim
        my_vn = mychat.vn_obj
        can_play = False
        chat_title_width = 400
        chat_box_width = 620
        partic_viewport_width = 530
        if mychat.expired:
            chat_title_width = 300
            chat_box_width = 520
            partic_viewport_width = 430
            
        if my_vn and not my_vn.party:
            if my_vn.played:
                vn_foreground = 'vn_active'
                vn_hover = 'vn_active_hover'   
                can_play = True
            elif my_vn.available and wasplayed and mychat.played:
                vn_foreground = 'vn_selected'
                vn_hover = 'vn_selected_hover'
                can_play = True
            elif mychat.expired:
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
                
        if mychat.played:
            chat_bkgr = 'chat_active'
            chat_hover = 'chat_active_hover'  
            can_play = True            
        elif mychat.available and wasplayed:
            chat_bkgr = 'chat_selected'
            chat_hover = 'chat_selected_hover'
            can_play = True
        elif mychat.expired:
            chat_bkgr = 'chat_inactive'
            chat_hover = 'chat_inactive'
        else:
            chat_bkgr = 'chat_inactive'
            chat_hover = 'chat_inactive'
        
        
        if mychat.participants:
            if len(mychat.participants) > 5 and mychat.participated:
                part_anim = participant_scroll
            elif len(mychat.participants) > 6 and not mychat.participated:
                part_anim = participant_scroll
            else:
                part_anim = null_anim
        else:
            part_anim = null_anim
            
        
    
    null height 10
                      
    if not sametime:
        textbutton _(mychat.trigger_time[:2] + ':00'):
            xysize (181,62)
            text_color '#fff'
            text_size 40
            text_xalign 0.5
            xalign 0.05
            text_align 0.5
            yalign 0.5
            background 'vn_time_bg' padding (20,20)
        
    hbox:
        xysize (620, 160)
        xoffset 70
        xalign 0.0
        button at anim(10):
            xysize (chat_box_width, 160)
            xalign 0.0
            background chat_bkgr
            hover_foreground chat_hover
            if can_play and wasplayed:
                if mychat.expired:
                    action [SetVariable('current_chatroom', mychat), Jump(mychat.expired_chat)]
                else:
                    action [SetVariable('current_chatroom', mychat), Jump(mychat.chatroom_label)]
                    
            if hacked_effect and mychat.expired:
                add 'day_reg_hacked' xoffset -185 yoffset -178
            elif hacked_effect:
                add 'day_reg_hacked_long' xoffset -210 yoffset -170
                
            vbox:
                spacing 18
                hbox:
                    spacing 30
                    window:
                        xysize (75,27)
                        xoffset 77
                        yoffset 13
                        text mychat.trigger_time color '#fff' size 27 xalign 0.5 yalign 0.5 text_align 0.5
                    viewport:
                        yoffset 13
                        xoffset 77                
                        xysize(chat_title_width,27)
                        if len(mychat.title) > 30: 
                            window:
                                xysize(chat_title_width,27)
                                text mychat.title color '#fff' size 25 xalign 0.0 yalign 0.5 text_align 0.0 layout 'nobreak' at chat_title_scroll
                        else:
                            text mychat.title color '#fff' size 25 xalign 0.0 yalign 0.5 text_align 0.0 layout 'nobreak'
                viewport:
                    xysize(partic_viewport_width, 85)
                    yoffset 13
                    xoffset 77            
                    yalign 0.5
                    window:
                        xysize(partic_viewport_width, 85)
                        hbox at part_anim:
                            spacing 5
                            if mychat.participants:
                                for person in mychat.participants:
                                    if person.participant_pic:
                                        add person.participant_pic
                                
                            if mychat.participated and mychat.played:
                                add Transform(m.prof_pic, size=(80,80))

            
        if mychat.expired and not mychat.buyback:
            imagebutton:
                yalign 0.9
                xalign 0.5
                idle 'expired_chat'
                hover_foreground 'expired_chat'
                if mychat.available:
                    action Show('confirm', message="Would you like to participate in the chat conversation that has passed?",
                            yes_action=[SetField(mychat, 'expired', False),
                            SetField(mychat, 'buyback', True),
                            SetField(mychat, 'played', False),
                            Function(mychat.reset_participants),
                            renpy.retain_after_load,
                            renpy.restart_interaction, Hide('confirm')], no_action=Hide('confirm'))
                
    if my_vn and not my_vn.party:
        window:
            xysize(700, 160)
            xalign 0.0
            xoffset 10
            
            has hbox
            add 'vn_marker'
            
            button:
                xysize(555, 126)
                foreground vn_foreground
                hover_foreground vn_hover
                activate_sound 'sfx/UI/select_vn_mode.mp3'
                if my_vn.available and can_play and mychat.played:
                    # Note: afm is ~30 at its slowest, 0 when it's off, and 1 at its fastest
                    action [Preference("auto-forward", "disable"), SetVariable('current_chatroom', mychat), Jump(my_vn.vn_label)]                    
                if my_vn.who:
                    add 'vn_' + my_vn.who.file_id xoffset -5
                else:
                    add 'vn_other' xoffset -5
    
    # It's the VN that leads to the party
    if my_vn and my_vn.party:
        window:
            xysize(600, 300)
            xalign 1.0
           
            button:
                xysize(463, 185)
                xalign 0.5
                yalign 0.5
                background vn_background                
                activate_sound 'sfx/UI/select_vn_mode.mp3'
                if my_vn.available and can_play:
                    hover_foreground vn_background
                    # Note: afm is ~30 at its slowest, 0 when it's off, and 1 at its fastest
                    action [Preference("auto-forward", "disable"), SetVariable('current_chatroom', mychat), Jump(my_vn.vn_label)]                    
            
        
    # There's a plot branch
    if mychat.plot_branch:
        button:
            xysize(330, 85)
            background 'input_popup_bkgr'
            hover_background 'input_popup_bkgr_hover'
            xalign 0.5
            hbox:
                spacing 15
                align (0.5, 0.5)
                add 'plot_lock'
                text 'Tap to unlock' color '#fff' xalign 0.5 yalign 0.5
            #if mychat.available and mychat.played and (not mychat.vn_obj or mychat.vn_obj.played):
            if can_branch():
                if persistent.real_time:
                    action Show("confirm", message="The game branches here. Missed chatrooms may appear depending on the time right now. Continue?", 
                            yes_action=[Hide('confirm'), SetVariable('current_chatroom', mychat),
                            Jump(mychat.chatroom_label + '_branch')], no_action=Hide('confirm'))           
                else:
                    action Show("confirm", message="The game branches here. Continue?", 
                        yes_action=[Hide('confirm'), SetVariable('current_chatroom', mychat),
                        Jump(mychat.chatroom_label + '_branch')], no_action=Hide('confirm'))                 
            else:
                action Show("confirm", message="Please proceed after completing the unseen old conversations.",
                        yes_action=Hide('confirm'))
                
    
## This is used to continue the game after a plot branch    
label plot_branch_end:
    # CASE 1
    # Plot branch is just a chatroom, has an after label
    if not current_chatroom.vn_obj:
        if renpy.has_label('after_' + current_chatroom.chatroom_label):
            $ renpy.call('after_' + current_chatroom.chatroom_label)
        # Deliver calls/texts/etc
        $ deliver_calls(current_chatroom.chatroom_label)
        $ deliver_emails()   
    # CASE 2
    # Plot branch is after a chatroom, after branching there's a VN
    elif current_chatroom.vn_obj and not current_chatroom.vn_obj.played:
        # Don't deliver anything yet
        pass
    # CASE 3
    # Plot branch is after a chatroom with a VN
    elif current_chatroom.vn_obj and current_chatroom.vn_obj.played:
        if renpy.has_label('after_' + current_chatroom.chatroom_label):
            $ renpy.call('after_' + current_chatroom.chatroom_label)
        # Deliver calls/texts/etc
        $ deliver_calls(current_chatroom.chatroom_label)
        $ deliver_emails()

    # Now we need to check if the player unlocked the next 24 hours
    # of chatrooms, and make those available
    if unlock_24_time:
        python:
            is_branch = False
            # Check chatrooms for the previous day
            for chatroom in chat_archive[today_day_num-1].archive_list:
                # Hour for this chatroom is greater than now; make available
                if int(unlock_24_time.military_hour) < int(chatroom.trigger_time[:2]) and not is_branch:
                    if chatroom.plot_branch:
                        is_branch = True
                    chatroom.available = True
                    chatroom.buyahead = True
                # Hour is the same; check minute
                elif int(unlock_24_time.military_hour) == int(chatroom.trigger_time[:2]):            
                    if int(unlock_24_time.minute) < int(chatroom.trigger_time[-2:]) and not is_branch:
                        if chatroom.plot_branch:
                            is_branch = True
                        # Minute is greater; make available
                        chatroom.available = True
                        chatroom.buyahead = True
            # Now check chatrooms for today
            if chat_archive[today_day_num].archive_list:
                for chatroom in chat_archive[today_day_num].archive_list:
                    # Hour for this chatroom is smaller than now; make available
                    if int(unlock_24_time.military_hour) > int(chatroom.trigger_time[:2]) and not is_branch:
                        if chatroom.plot_branch:
                            is_branch = True
                        chatroom.available = True
                        chatroom.buyahead = True
                    # Hour is the same; check minute
                    elif int(unlock_24_time.military_hour) == int(chatroom.trigger_time[:2]):            
                        if int(unlock_24_time.minute) > int(chatroom.trigger_time[-2:]) and not is_branch:
                            if chatroom.plot_branch:
                                is_branch = True
                            # Minute is smaller; make available
                            chatroom.available = True
                            chatroom.buyahead = True
            # 24-hour buy-ahead is done; reset the variable
            # *unless* there was a plot branch, in which case
            # we're not done unlocking
            if not is_branch:
                unlock_24_time = False            
    $ next_chatroom()
    $ renpy.retain_after_load
    show screen chat_home
    hide screen chat_home
    call screen chat_select
                
                
                
                
                
