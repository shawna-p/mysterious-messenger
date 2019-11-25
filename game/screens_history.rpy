##############################################
## This screen allows you to view replays
## of chatrooms and phone calls you've already
## seen in-game
###############################################

image history_button = Frame('Menu Screens/History/main02_button_01.png',
                                49, 52, 270, 53)
image history_button_hover = Fixed('history_button', 
                            Transform('history_button', alpha=0.5))
image history_icon_album = 'Menu Screens/History/history_icon_album.png'
image history_icon_chat = 'Menu Screens/History/history_icon_chat.png'
image history_icon_call = 'Menu Screens/History/history_icon_call.png'
image history_icon_guest = 'Menu Screens/History/history_icon_guest.png'

## This screen lets you view the album or the chat history
screen select_history():

    tag menu

    use menu_header("History", Show('main_menu', Dissolve(0.5))):

        style_prefix "select_history" 
        window: 
            hbox:      
                spacing 30    
                button:
                    action Show('photo_album', Dissolve(0.5))
                    hbox:
                        add 'history_icon_album' yalign 0.5
                        text 'ALBUM'
                button:
                    action Show('select_history_route', Dissolve(0.5))
                    hbox:
                        add 'history_icon_chat' yalign 0.5
                        text "CHAT HISTORY" 


style select_history_hbox:
    is default
    spacing 15
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
    font sans_serif_1b
    align (0.5, 0.5)

style select_history_window:
    is default
    xysize (740, 1100)
    align (0.5, 0.5)


default which_history_route = None

screen select_history_route():

    tag menu

    use menu_header("History", Show('main_menu', Dissolve(0.5))):

        style_prefix 'history_route'
        for route in all_routes:
            textbutton _(route.route_history_title + " Route"):
                action [SetVariable('which_history_route', route.route),
                        Show('chat_select', days=route.route)]

style history_route_button:
    is other_settings_end_button
    padding (30,30)

style history_route_button_text:
    is mode_select

image history_chat_active = Frame("Menu Screens/History/msgsl_bg_active.png", 10,10)
image history_chat_inactive = Frame("Menu Screens/History/msgsl_bg_inactive.png", 10,10)
image history_chat_participated = Transform("Menu Screens/History/chat_history_participated.png", zoom=0.8)
image history_chat_alone = Transform("Menu Screens/History/chat_history_alone.png", zoom=0.8)

screen chatroom_item_history(day, day_num, chatroom, index):

    python:
        played_reg = False
        played_expired = False
        vn_played = False
        my_vn = False
        is_chatroom = (isinstance(chatroom, Chat_History)
                        or isinstance(chatroom, store.Chat_History))
        is_vn = (isinstance(chatroom, VN_Mode)
                    or isinstance(chatroom, store.VN_Mode))
                    
        # Now we set up some variables to see whether or not the player
        # has seen one version of this chatroom or not
        if is_chatroom:
            my_vn = chatroom.vn_obj
            played_reg = renpy.seen_label(chatroom.chatroom_label)
            played_expired = renpy.seen_label(chatroom.expired_chat)
            if my_vn:
                vn_played = renpy.seen_label(my_vn.vn_label)
            else:
                vn_played = True
        elif is_vn:
            my_vn = chatroom
            vn_played = renpy.seen_label(my_vn.vn_label)
        else:
            played_reg = True
            played_expired = True
            vn_played = True

        # This determines if there are enough participants
        # in this chat to make the viewport scroll automatically
        if is_chatroom and chatroom.participants:
            if len(chatroom.participants) > 4:
                part_anim = participant_scroll
            else:
                part_anim = null_anim
        else:
            part_anim = null_anim

    null height 10
    if not is_chatroom and not is_vn:
        text chatroom color "#fff" font sans_serif_1b xalign 0.5
    elif is_chatroom:
    
        
        window:
            xoffset 70
            xysize (620, 160)
            xalign 0.0
            background 'chat_active'
            # These are the two buttons to replay the chat
            hbox:
                align (0.98,0.83)
                spacing 10
                button:
                    xysize (80,80)
                    if renpy.seen_label(chatroom.expired_chat):
                        background 'history_chat_active'                        
                        action NullAction()
                    else:
                        background Fixed('history_chat_inactive', "#000c")
                        foreground "#0005"
                    add 'history_chat_alone' align (0.5, 0.5)
                    if not renpy.seen_label(chatroom.expired_chat):
                        add 'plot_lock' align (0.5, 0.5)
                button:
                    xysize(80,80)
                    if renpy.seen_label(chatroom.chatroom_label):
                        background 'history_chat_active'                        
                        action NullAction()
                    else:
                        background Fixed('history_chat_inactive', "#000c")
                        foreground "#0005"
                    add 'history_chat_participated' align (0.5, 0.5)
                    if not renpy.seen_label(chatroom.chatroom_label):
                        add 'plot_lock' align (0.5, 0.5)
                    
                
            vbox:
                yoffset 3
                spacing 18
                # This box displays the trigger time and
                # title of the chatroom; optionally at
                # a scrolling transform so you can read
                # the entire title
                hbox:
                    spacing 30
                    window:
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
                        xysize(400,27)
                        if len(chatroom.title) > 30: 
                            window:
                                xysize(400,27)
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
                    xysize(530, 85)
                    yoffset 13
                    xoffset 77            
                    yalign 0.5
                    window:
                        xysize(355, 85)
                        hbox at part_anim:
                            yalign 0.5
                            spacing 5
                            if chatroom.participants:
                                for person in chatroom.participants:
                                    if person.participant_pic:
                                        add person.participant_pic

            

    # If there's a VN object, we display it now
    if my_vn and not my_vn.party:
        window:
            xysize(700, 160)
            xalign 0.0
            xoffset 10
            
            has hbox
            add 'vn_marker'
            
            button:
                xysize(555, 126)
                foreground 'vn_selected'
                hover_foreground 'vn_selected_hover'
                activate_sound 'audio/sfx/UI/select_vn_mode.mp3'
                action NullAction()     
                
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
                background 'vn_party'              
                activate_sound 'audio/sfx/UI/select_vn_mode.mp3'
                if my_vn.available and can_play:
                    hover_foreground 'vn_party'
                    # Note: afm is ~30 at its slowest, 0 when it's off, 
                    # and 1 at its fastest
                    action [Preference("auto-forward", "disable"), 
                            SetVariable('current_chatroom', chatroom), 
                            Jump(my_vn.vn_label)]                    
                
            
        


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


