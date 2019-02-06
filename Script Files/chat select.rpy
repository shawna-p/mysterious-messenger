########################################################
## This is the screen where you choose which day to play
########################################################
screen chat_select():

    tag menu

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
                for day in chat_archive:
                    use day_select(day)
                
                
                
screen day_select(day):

    python:
        num_chatrooms = len(day.archive_list)
        completed_chatrooms = 0
        is_today = False
        played = False
        for i in day.archive_list:
            if i.played:
                completed_chatrooms += 1
                played = True
            if i.available and not i.played:
                is_today = True
            if i.played and i.plot_branch:
                is_today = True
            elif i.vn_obj and i.vn_obj.available and not i.vn_obj.played:
                is_today = True
        
        if day.archive_list:
            chat_percent = str(completed_chatrooms * 100 // num_chatrooms)
        else:
            chat_percent = '0'
            num_chatrooms = 1
            
        if is_today:
            day_bkgr = 'day_selected'
            day_bkgr_hover = 'day_selected_hover'
        elif played:
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
                action Show('chatroom_timeline', day=day)
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
        if not is_today and played:
            add 'day_hlink' xalign 0.5
        
        
########################################################
## This screen shows a timeline of the chatrooms on
## each particular day
########################################################
screen chatroom_timeline(day):

    tag menu

    use starry_night()
    
    use menu_header(day.day, Show('chat_select', Dissolve(0.5)))
    
    fixed:   
        xysize (720, 1180)
        yalign 1.0
        xalign 0.5   
        add 'day_vlink' xalign 0.15
        viewport:
            
            mousewheel True
            draggable True
            
            vbox:
                xsize 720
                spacing 20
                for index, chatroom in enumerate(day.archive_list):
                    if chatroom.available:
                        if index > 0 and chatroom.trigger_time[:2] == day.archive_list[index-1].trigger_time[:2]:
                            use chatroom_display(chatroom, True)
                        else:
                            use chatroom_display(chatroom)
                null height 40
                    
                    
screen chatroom_display(mychat, sametime=False):

    python:

        my_vn = mychat.vn_obj
        if my_vn and not my_vn.party:
            if my_vn.played:
                vn_foreground = 'vn_active'
                vn_hover = 'vn_active_hover'
            elif my_vn.available:
                vn_foreground = 'vn_selected'
                vn_hover = 'vn_selected_hover'
            else:
                vn_foreground = 'vn_inactive'
                vn_hover = 'vn_inactive'
        elif my_vn and my_vn.party:
            if my_vn.available:
                vn_background = 'vn_party'
            elif not my_vn.available:
                vn_background = 'vn_party_inactive'
                
        if mychat.played:
            chat_bkgr = 'chat_active'
            chat_hover = 'chat_active_hover'
        elif mychat.available:
            chat_bkgr = 'chat_selected'
            chat_hover = 'chat_selected_hover'
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
        
    button:
        xysize (620, 160)
        xoffset 70
        xalign 0.0
        background chat_bkgr
        hover_foreground chat_hover
        action [SetVariable('current_chatroom', mychat), Jump(mychat.chatroom_label)]
        
        has vbox
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
                xysize(400,27)
                if len(mychat.title) > 30: 
                    window:
                        xysize(400,27)
                        text mychat.title color '#fff' size 25 xalign 0.0 yalign 0.5 text_align 0.0 layout 'nobreak' at chat_title_scroll
                else:
                    text mychat.title color '#fff' size 25 xalign 0.0 yalign 0.5 text_align 0.0 layout 'nobreak'
        viewport:
            xysize(530, 85)
            yoffset 13
            xoffset 77            
            yalign 0.5
            window:
                xysize(530, 85)
                hbox at part_anim:
                    spacing 5
                    if mychat.participants:
                        for person in mychat.participants:
                            if person.participant_pic:
                                add person.participant_pic
                        
                    if mychat.participated and mychat.played:
                        add Transform(m.prof_pic, zoom=.725)
                
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
                if my_vn.available:
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
                if my_vn.available:
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
            if mychat.available and mychat.played and (not mychat.vn_obj or mychat.vn_obj.played):
                action Show("confirm", message="The game branches here. Continue?", # Missed chatrooms may appear depending on the time right now 
                        yes_action=[Hide('confirm'), SetVariable('current_chatroom', mychat),
                        Jump(mychat.chatroom_label + '_branch')], no_action=Hide('confirm'))                 
            else:
                action Show("confirm", message="Please proceed after completing the unseen old conversations.",
                        yes_action=Hide('confirm'))
                
    
# This is used to continue the game after a plot branch    
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

    $ next_chatroom()
    $ renpy.retain_after_load
    call screen chat_home
    
                
                
                
                
                
