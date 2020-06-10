########################################################
## This file contains several functions related to
## the messenger system. It's organized as follows:
##   label chat_begin
##   label set_chatroom_background
##   label chat_end
##   label chat_end_route
##   label vn_during_chat
##   label chat_back
##   screen save_and_exit
##      label press_save_and_exit
##   screen signature_screen
########################################################

#####################################
# Chat Setup
#####################################

# This simplifies things when you're setting up a chatroom,
# so call it when you're about to begin
# Pass it the name of the background you want (enclosed in
# single ' or double " quotes)
# Note that it automatically clears the chatlog, so if you want
# to change the background but not clear the messages on-screen,
# you also have to pass it 'False' as its second argument

label chat_begin(background=None, clearchat=True, resetHP=True):
    if starter_story:
        $ set_name_pfp()
    stop music
    if clearchat:
        $ chatlog = []
        # $ pv = 0.8    # This resets the chatroom "speed"
                        # Ordinarily it would reset for every
                        # new chatroom, and if you want that
                        # functionality you can un-comment this
                        # line
    # Reset the heart points for this chatroom
    if resetHP:
        $ chatroom_hp = 0

    # Make sure the messenger screens are showing
    hide screen starry_night
    $ renpy.hide_screen('animated_bg')
    show screen phone_overlay
    show screen messenger_screen 
    show screen pause_button
    
    # Hide all the popup screens
    $ hide_all_popups()
    
    $ text_person = None
    window hide
    $ text_msg_reply = False
    $ in_phone_call = False
    $ vn_choice = False
    $ email_reply = False
    
    # Fills the beginning of the screen with 'empty space' 
    # so the messages begin showing up at the bottom of the 
    # screen (otherwise they start at the top)
    if clearchat:
        $ addchat(filler, "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", 0)

    call set_chatroom_background(background)

    # If you've already played this chatroom in your current runthrough,
    # viewing it again causes this variable to be True. It prevents you
    # from receiving heart points again and only lets you select choices
    # you've selected on this or previous playthroughs
    if current_chatroom.played:
        if not persistent.testing_mode:
            $ observing = True     
        else:
            $ observing = False
    else:
        $ observing = False

    # If you're viewing this from the history, observing is True
    # Pronouns, name, and profile picture must also be re-set
    # and all the characters' profile pictures should be the default
    if _in_replay:
        python:
            observing = True
            set_pronouns()
            set_name_pfp()
            if resetHP:
                for c in all_characters:
                    c.reset_pfp()
        
    
    # This resets the heart points you've collected from
    # previous chatrooms so it begins at 0 again   
    if resetHP:
        $ in_chat = []
        if not observing:
            $ current_chatroom.reset_participants()
        python:
            for person in current_chatroom.original_participants:
                if person.name not in in_chat:
                    in_chat.append(person.name)
            
        # If the player is participating, add them to the list of
        # people in the chat
        if (not current_chatroom.expired 
                or current_chatroom.buyback 
                or current_chatroom.buyahead):
            if not expired_replay:
                $ in_chat.append(m.name)
        
    return

## This label simplifies setting up backgrounds for chatrooms
## It takes the name of a background and shows the corresponding
## static or animated background
label set_chatroom_background(new_bg):
    # Sets the correct background and nickname colour
    # You need to add other backgrounds here if you define
    # new ones
    $ current_background = new_bg
    if new_bg in ['morning', 'noon', 'evening', 'hack', 'redhack',
                  'night', 'earlyMorn', 'redcrack']:
        scene
        $ renpy.show('bg ' + new_bg)
    # If the background is misspelled/etc, set a generic
    # black background
    else:
        scene bg black
        $ current_background = 'morning'

    if persistent.animated_backgrounds:
        if new_bg in ['morning', 'noon', 'evening', 'night', 'earlyMorn']:
            $ renpy.show_screen('animated_' + new_bg)
        elif new_bg == 'hack':
            show screen animated_hack_background
        elif new_bg == 'redhack':
            show screen animated_hack_background(red=True)

    if new_bg in ['morning', 'noon', 'evening']:
        $ nickColour = black
    else:
        $ nickColour = white
        

    # Add this background to the replay log
    if not observing and not persistent.testing_mode:
        $ bg_entry = ("background", current_background)
        $ current_chatroom.replay_log.append(bg_entry)


    return

## Call this label to show the save & exit sign
label chat_end():
    if starter_story:        
        $ persistent.first_boot = False
        $ persistent.on_route = True
    call screen save_and_exit    
    return
    
## Call this label at the very end of the route
## to show a good/bad/normal ending sign and
## return the player to the main menu
label chat_end_route():
    call screen save_and_exit(True)
    $ config.skipping = False
    $ choosing = False
    hide screen phone_overlay
    hide screen save_and_exit
    hide screen play_button
    hide screen answer_button
    hide screen pause_button
    hide screen messenger_screen
    $ hide_all_popups()
    $ renpy.hide_screen('animated_bg')
    stop music
    
    if ending == 'good':
        scene bg good_end
    elif ending == 'normal':
        scene bg normal_end
    elif ending == 'bad':
        scene bg bad_end
    $ ending = False
    
    if current_chatroom.expired and not current_chatroom.buyback:
        $ persistent.completed_chatrooms[
                        current_chatroom.expired_chat] = True
    else:
        $ persistent.completed_chatrooms[
                        current_chatroom.chatroom_label] = True
    if current_chatroom.vn_obj:
        $ persistent.completed_chatrooms[
                        current_chatroom.vn_obj.vn_label] = True
    pause
    if _in_replay:
        $ renpy.end_replay()
    jump restart_game

## This label clears the necessary chatroom variables to allow
## you to show a VN section in the middle of a chatroom
## The VN section needs to be defined in its own separate label
label vn_during_chat(vn_label, clearchat_on_return=False, new_bg=False,
                     reset_participants=False, end_after_vn=False):
    
    # Add an instruction for the replay log
    if (not observing and not persistent.testing_mode):
        $ vn_jump_entry = ("vn jump", 
            [vn_label, clearchat_on_return, new_bg, reset_participants])
        $ current_chatroom.replay_log.append(vn_jump_entry)

    # Give the player a moment to read the last of the messages
    # before jumping to the VN
    $ renpy.pause(pv*2.0)
    call screen continue_button

    # Hide all the chatroom screens
    $ config.skipping = False
    $ choosing = False
    hide screen phone_overlay
    hide screen save_and_exit
    hide screen play_button
    hide screen answer_button
    hide screen pause_button
    hide screen messenger_screen
    $ hide_all_popups()
    $ renpy.hide_screen('animated_bg')

    # Setup the VN stuff
    scene bg black
    window auto
    hide screen starry_night
    hide screen chatroom_timeline

    show screen vn_overlay
    $ vn_choice = True
    $ _history_list = []
    $ _history = True
    $ _preferences.afm_enable = False

    # Don't worry about setting `observing` as it should
    # still be set from the connected chatroom
    $ renpy.call(vn_label)

    # At this point the program has returned from the VN section
    # and must set up the chatroom again, unless the chat is supposed
    # to end now
    if end_after_vn:
        return

    scene bg black
    $ text_msg_reply = False
    $ in_phone_call = False
    $ vn_choice = False
    $ email_reply = False
    hide screen vn_overlay
    $ choosing = False
    $ config.skipping = False
    $ hide_all_popups()
    
    if clearchat_on_return:
        $ chatlog = []
        $ addchat(filler, "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", 0)
    
    
    if not clearchat_on_return:
        # If the chat isn't cleared this cleans up the transition
        # between VN and chatroom
        show screen non_menu_loading_screen
        show screen phone_overlay
        show screen messenger_screen 
        show screen pause_button
        window hide
        if new_bg:
            call set_chatroom_background(new_bg)
        else:
            call set_chatroom_background(current_background)
        pause 0.5
        hide screen non_menu_loading_screen
    else:
        show screen phone_overlay
        show screen messenger_screen 
        show screen pause_button
        window hide
        if new_bg:
            call set_chatroom_background(new_bg)
        else:
            call set_chatroom_background(current_background)

    python:
        if reset_participants:
            in_chat = []
            for person in reset_participants:
                in_chat.append(person.name)
                if not observing:
                    current_chatroom.add_participant(person)

    

    # If this is part of a replayed chatroom, go back to
    # the replay log (NOT replayed from the History in the
    # main menu)
    if (observing and not vn_choice and not text_msg_reply 
            and not in_phone_call and not email_reply
            and not _in_replay):
        $ replay_from = chatroom_replay_index
        jump chatroom_replay
    return

## A very simple screen used for transitions
screen non_menu_loading_screen():
    zorder 100
    add Solid("#000")
    use loading_screen

## This label takes care of what happens when the
## player hits the back button during a chatroom
label chat_back():
    # If you're replaying a chatroom or it's already
    # expired, you can back out without repercussions
    if observing or current_chatroom.expired or _in_replay:
        $ config.skipping = False
        $ choosing = False
        hide screen phone_overlay
        hide screen messenger_screen
        hide screen save_and_exit
        hide screen play_button
        hide screen answer_button
        hide screen pause_button
        $ renpy.hide_screen('animated_bg')
        stop music
        if _in_replay:
            $ renpy.end_replay()
    else:
        # If you back out of a chatroom, it expires
        $ current_chatroom.expired = True
        # And if you bought it back, it still expires
        $ current_chatroom.buyback = False
        $ current_chatroom.buyahead = False
        $ current_chatroom.participated = False
        # The replay log should reset since the player hasn't
        # seen the entire chatroom
        $ current_chatroom.replay_log = []
        # Reset participants
        $ current_chatroom.reset_participants()
        $ chatroom_hp = 0
        $ chatroom_hg = 0
        $ config.skipping = False       
        $ choosing = False
        $ most_recent_chat = current_chatroom
        hide screen phone_overlay
        hide screen messenger_screen
        hide screen save_and_exit
        $ renpy.hide_screen('animated_bg')
        hide screen play_button
        hide screen answer_button
        hide screen pause_button
        hide screen vn_overlay
        # Deliver text and calls        
        # Checks for a post-chatroom label; triggers even if there's a VN
        # and delivers text messages, phone calls etc
        if renpy.has_label('after_' + current_chatroom.chatroom_label): 
            $ was_expired = current_chatroom.expired
            $ renpy.call('after_' + current_chatroom.chatroom_label)
            $ was_expired = False
        $ deliver_all_texts()
        $ deliver_calls(current_chatroom.chatroom_label, True)
        $ renpy.retain_after_load()
        stop music
    $ renpy.set_return_stack([])
    call screen chatroom_timeline(current_day, current_day_num)
    return

    

        
#####################################
# Save & Exit
#####################################
   
# This is the screen that shows Save & Exit at the bottom
screen save_and_exit(end_route=False):
    zorder 4
    tag chat_footer
    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 0
        ypos 1220
        focus_mask True
        idle "save_exit"
        if not end_route:
            action [Jump("press_save_and_exit")]
        else:
            action Return()
        
label press_save_and_exit():
    if vn_choice:
        $ vn_choice = False
        $ phone = False
    else:
        $ phone = True
    
    if (most_recent_chat is None 
            and chat_archive 
            and chat_archive[0].archive_list):
        $ most_recent_chat = chat_archive[0].archive_list[0]
    elif most_recent_chat is None:
        $ most_recent_chat = ChatHistory('Example Chatroom', 
                                        'example_chat', '00:01')
        
    if observing or _in_replay:
        $ config.skipping = False
        $ choosing = False
        $ observing = False
        hide screen phone_overlay
        hide screen save_and_exit
        hide screen play_button
        hide screen answer_button
        hide screen pause_button
        hide screen messenger_screen
        $ hide_all_popups()
        stop music
        if _in_replay:
            $ renpy.end_replay()
        $ renpy.hide_screen('animated_bg')
        call screen chatroom_timeline(current_day, current_day_num)
    else:
        call screen signature_screen(phone)        
        $ persistent.HG += chatroom_hg
        $ chatroom_hp = 0
        $ chatroom_hg = 0
        $ config.skipping = False        
        $ choosing = False
        hide screen phone_overlay
        hide screen messenger_screen
        hide screen save_and_exit
        hide screen vn_overlay
        hide screen pause_button
        $ renpy.hide_screen('animated_bg')
        show screen loading_screen
        if not current_chatroom.played:
            $ current_chatroom.played = True
            if not starter_story and not current_chatroom.buyback:
                $ most_recent_chat = current_chatroom
        
        if not current_chatroom.expired and not current_chatroom.buyback:
            # Checks for a post-chatroom label; won't trigger 
            # if there's a VN section
            # Otherwise delivers phone calls/texts/etc
            if (renpy.has_label('after_' + current_chatroom.chatroom_label) 
                    and not current_chatroom.vn_obj): 
                $ was_expired = current_chatroom.expired
                $ renpy.call('after_' + current_chatroom.chatroom_label)
                $ was_expired = False
            # Add this label to the list of completed labels
            $ persistent.completed_chatrooms[
                                current_chatroom.chatroom_label] = True
            # If you just finished a VN section, mark it as played
            # and deliver emails/phone calls
            if (not phone 
                    and current_chatroom.vn_obj 
                    and not current_chatroom.vn_obj.played 
                    and current_chatroom.vn_obj.available):
                $ current_chatroom.vn_obj.played = True
                # Add this label to the list of completed labels
                $ persistent.completed_chatrooms[
                            current_chatroom.vn_obj.vn_label] = True
                if renpy.has_label('after_' + current_chatroom.chatroom_label):
                    $ was_expired = current_chatroom.expired
                    $ renpy.call('after_' + current_chatroom.chatroom_label)
                    $ was_expired = False
        elif (current_chatroom.plot_branch 
                and current_chatroom.vn_obj 
                and not current_chatroom.vn_obj.played 
                and current_chatroom.vn_obj.available):
            $ current_chatroom.vn_obj.played = True
            # Add this label to the list of completed labels
            $ persistent.completed_chatrooms[
                            current_chatroom.vn_obj.vn_label] = True
        elif (not current_chatroom.plot_branch 
                and not phone and current_chatroom.vn_obj 
                and not current_chatroom.vn_obj.played 
                and current_chatroom.vn_obj.available):
            $ current_chatroom.vn_obj.played = True
            # Add this label to the list of completed labels
            $ persistent.completed_chatrooms[
                            current_chatroom.vn_obj.vn_label] = True
        if not current_chatroom.expired and not current_chatroom.buyback:
            $ deliver_calls(current_chatroom.chatroom_label)
            
        if current_chatroom.expired and not current_chatroom.buyback:
            $ current_chatroom.participated = False
            # Add this label to the list of completed labels
            $ persistent.completed_chatrooms[
                            current_chatroom.expired_chat] = True
        else:
            $ current_chatroom.participated = True
            $ persistent.completed_chatrooms[
                            current_chatroom.chatroom_label] = True
        
        # Deliver emails and trigger the next chatroom (if applicable)
        $ deliver_emails()   
        $ next_chatroom()
        $ hide_all_popups()
        # Make sure any images shown are unlocked
        $ check_for_CGs(all_albums)
        $ renpy.retain_after_load()
        # Check to see if the honey buddha chips should be available
        if not chips_available:
            $ chips_available = hbc_bag.draw()
        
        stop music
        # This helps clean up the transition between sections
        # in case it takes the program a few moments to calculate
        # messages, emails, etc
        pause 0.2
        hide screen loading_screen
        if starter_story:
            $ starter_story = False
            call screen chat_home
            return
        else:
            $ deliver_next()
            call screen chatroom_timeline(current_day, current_day_num)
            return
    return

    
# This shows the signature screen, which records your total heart points
# It shows hourglass points as well but currently there is no way to get
# more hourglasses
screen signature_screen(phone=True):
    zorder 5
    modal True
    style_prefix "sig_screen"
    if phone:
        add "save_exit" ypos 1220
    add "choice_darken"
    frame:        
        has vbox
        spacing 10
        null height 80
        text "This conversation will be archived in the RFA records.":
            if persistent.custom_footers:
                color "#fff"
        hbox:
            style_prefix "sig_points"            
            frame:
                background 'heart_sign'
                text str(chatroom_hp)
            frame:
                background 'hg_sign'
                text str(chatroom_hg)
        
        text "I hereby agree to treat this conversation as confidential.":
            if persistent.custom_footers:
                color "#fff"
        
        textbutton _('sign'): 
            if persistent.custom_footers:
                text_color "#fff"
            action Return()

style sig_screen_frame:
    xalign 0.5
    yalign 0.5
    xsize 682
    ysize 471
    background 'signature'

style sig_screen_vbox:
    align (0.5, 0.5)

style sig_points_fixed:
    xalign 0.5
    ysize 60
    xsize 682

style sig_points_hbox:
    spacing 105
    yalign 0.5
    xalign 0.5

style sig_points_frame:
    ysize 60
    xsize 154
    padding (62, 12, 20, 12)

style sig_points_text:        
    is text
    yalign 1.0
    xalign 1.0
    text_align 1.0
    font sans_serif_1
    color "#ffffff"

style sig_screen_text:
    is text
    xalign 0.5         
    text_align 0.5
    size 25
    xsize 600
    font gui.sans_serif_1

style sig_screen_button:
    xysize (211, 52)
    align (0.5, 0.842)
    focus_mask True
    background 'sign_btn' padding(20,20)
    activate_sound "audio/sfx/UI/end_chatroom.mp3"
    hover_background 'sign_btn_clicked'

style sig_screen_button_text:
    is text
    xalign 0.5   
    yalign 0.607   
    text_align 0.5
    size 30
    font gui.sans_serif_1
    
## Jumping to this label during an introductory/prologue label
## allows the program to properly set up variables before taking
## the player to the chat home screen
label skip_intro_setup():
    $ persistent.first_boot = False
    $ persistent.on_route = True
    
    if vn_choice:
        $ vn_choice = False
        $ phone = False
    $ most_recent_chat = chat_archive[0].archive_list[0]
    $ chatroom_hp = 0
    $ chatroom_hg = 0
    $ config.skipping = False        
    $ choosing = False
    hide screen phone_overlay
    hide screen messenger_screen
    hide screen save_and_exit
    hide screen vn_overlay
    hide screen pause_button
    $ renpy.hide_screen('animated_bg')
    show screen loading_screen
        
    if not current_chatroom.expired and not current_chatroom.buyback:
        # Checks for a post-chatroom label; won't trigger 
        # if there's a VN section
        # Otherwise delivers phone calls/texts/etc
        if (renpy.has_label('after_' + current_chatroom.chatroom_label) 
                and not current_chatroom.vn_obj): 
            $ was_expired = current_chatroom.expired
            $ renpy.call('after_' + current_chatroom.chatroom_label)
            $ was_expired = False
        # Add this label to the list of completed labels
        $ persistent.completed_chatrooms[
                            current_chatroom.chatroom_label] = True
        
    
    if not current_chatroom.expired and not current_chatroom.buyback:
        $ deliver_calls(current_chatroom.chatroom_label)
        
    if current_chatroom.expired and not current_chatroom.buyback:
        $ current_chatroom.participated = False
        # Add this label to the list of completed labels
        $ persistent.completed_chatrooms[
                        current_chatroom.expired_chat] = True
    else:
        $ current_chatroom.participated = True
        $ persistent.completed_chatrooms[
                        current_chatroom.chatroom_label] = True
    
    # Deliver emails and trigger the next chatroom (if applicable)
    $ deliver_emails()   
    $ next_chatroom()
    $ hide_all_popups()
    # Make sure any images shown are unlocked
    $ check_for_CGs(all_albums)
    $ renpy.retain_after_load()
    # Check to see if the honey buddha chips should be available
    if not chips_available:
        $ chips_available = hbc_bag.draw()
    
    stop music
    # This helps clean up the transition between sections
    # in case it takes the program a few moments to calculate
    # messages, emails, etc
    pause 0.2
    hide screen loading_screen
    if starter_story:
        $ starter_story = False
        call screen chat_home
        return
    else:
        $ deliver_next()
        call screen chatroom_timeline(current_day, current_day_num)
        return
    return
    
    
    
    
    
    