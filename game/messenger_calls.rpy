########################################################
## This file contains several functions related to
## the messenger system. It's organized as follows:
##   label chat_begin
##   label chat_end
##   label chat_end_route
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
        
    # Sets the correct background and nickname colour
    # You need to add other backgrounds here if you define
    # new ones
    $ current_background = background
    if background == "morning":
        scene bg morning
        $ nickColour = black
    elif background == "noon":
        scene bg noon
        $ nickColour = black
    elif background == "evening":
        scene bg evening
        $ nickColour = black
    elif background == "night":
        scene bg night
        $ nickColour = white
    elif background == "earlyMorn":
        scene bg earlyMorn
        $ nickColour = white
    elif background == "hack":
        scene bg hack
        $ nickColour = white
    elif background == "redhack":
        scene bg redhack
        $ nickColour = white
    elif background == "redcrack":
        scene bg redcrack
        $ nickColour = white
    else:
        scene bg black
        $ nickColour = white
        $ current_background = "morning"

        
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
        
    # Add this background to the replay log
    if not observing and not persistent.testing_mode:
        $ bg_entry = ("background", "bg " + current_background)
        $ current_chatroom.replay_log.append(bg_entry)

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
    $ greeted = False
    $ choosing = False
    hide screen phone_overlay
    hide screen messenger_screen
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


## This label takes care of what happens when the
## player hits the back button during a chatroom
label chat_back():
    # If you're replaying a chatroom or it's already
    # expired, you can back out without repercussions
    if observing or current_chatroom.expired or _in_replay:
        $ config.skipping = False
        $ greeted = False
        $ choosing = False
        hide screen phone_overlay
        hide screen messenger_screen
        hide screen save_and_exit
        hide screen play_button
        hide screen answer_button
        hide screen pause_button
        stop music
        if _in_replay:
            $ renpy.end_replay()
        call screen chatroom_timeline(current_day, current_day_num)
    else:
        # If you back out of a chatroom, it expires
        $ current_chatroom.expired = True
        # And if you bought it back, it still expires
        $ current_chatroom.buyback = False
        $ current_chatroom.buyahead = False
        $ current_chatroom.participated = False
        # Reset participants
        $ current_chatroom.reset_participants()
        $ chatroom_hp = 0
        $ chatroom_hg = 0
        $ config.skipping = False   
        $ greeted = False         
        $ choosing = False
        $ most_recent_chat = current_chatroom
        hide screen phone_overlay
        hide screen messenger_screen
        hide screen save_and_exit
        hide screen play_button
        hide screen answer_button
        hide screen pause_button
        hide screen vn_overlay
        # Deliver text and calls        
        # Checks for a post-chatroom label; triggers even if there's a VN
        # and delivers text messages, phone calls etc
        if renpy.has_label('after_' + current_chatroom.chatroom_label): 
            $ renpy.call('after_' + current_chatroom.chatroom_label)
        $ deliver_all()
        $ deliver_calls(current_chatroom.chatroom_label, True)
        $ renpy.retain_after_load()
        stop music
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
        
label press_save_and_exit(phone=True):
    if observing or _in_replay:
        $ config.skipping = False
        $ greeted = False
        $ choosing = False
        $ observing = False
        hide screen phone_overlay
        hide screen save_and_exit
        hide screen play_button
        hide screen answer_button
        hide screen pause_button
        hide screen messenger_screen
        stop music
        if _in_replay:
            $ renpy.end_replay()
        call screen chatroom_timeline(current_day, current_day_num)
    else:
        call screen signature_screen(phone)        
        $ persistent.HG += chatroom_hg
        $ chatroom_hp = 0
        $ chatroom_hg = 0
        $ config.skipping = False   
        $ greeted = False         
        $ choosing = False
        $ no_heart = False
        hide screen phone_overlay
        hide screen messenger_screen
        hide screen save_and_exit
        hide screen vn_overlay
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
                $ renpy.call('after_' + current_chatroom.chatroom_label)
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
                    $ renpy.call('after_' + current_chatroom.chatroom_label)
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
        $ renpy.retain_after_load()
        # Check to see if the honey buddha chips should be available
        if not chips_available:
            $ chips_available = hbc_bag.draw()
        
        stop music
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
        text "This conversation will be archived in the RFA records."
        hbox:
            style_prefix "sig_points"            
            frame:
                background 'heart_sign'
                text str(chatroom_hp)
            frame:
                background 'hg_sign'
                text str(chatroom_hg)
        
        text "I hereby agree to treat this conversation as confidential."
        
        textbutton _('sign'): 
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
    

    

    
    
    
    
    
    