########################################################
## This file contains several functions related to
## the messenger system. It's organized as follows:
##   label chat_back
##   screen save_and_exit
##      label press_save_and_exit
##   screen signature_screen
########################################################

## This label takes care of what happens when the
## player hits the back button during a chatroom
label chat_back():
    # If you're replaying a chatroom or it's already
    # expired, you can back out without repercussions
    if observing or current_chatroom.expired:
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
        # $ renpy.save(mm_auto)
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
        # if not current_chatroom.plot_branch:
        # Checks for a post-chatroom label; triggers even if there's a VN
        # Otherwise delivers texts etc
        if renpy.has_label('after_' + current_chatroom.chatroom_label): 
            $ renpy.call('after_' + current_chatroom.chatroom_label)
        $ deliver_all()
        $ deliver_calls(current_chatroom.chatroom_label, True)
        $ renpy.retain_after_load()
        stop music
        # $ renpy.save(mm_auto)
        call screen chatroom_timeline(current_day, current_day_num)


    

        
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
        if persistent.custom_footers:
            idle "custom_save_exit"
        else:
            idle "save_exit"
        if not end_route:
            action [Jump("press_save_and_exit")]
        else:
            action Return()
        
label press_save_and_exit(phone=True):
    if observing:
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
        call screen chatroom_timeline(current_day, current_day_num)
        # call screen chat_select # call history_select_screen etc
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
            # Checks for a post-chatroom label; won't trigger if there's a VN section
            # Otherwise delivers phone calls/texts/etc
            if (renpy.has_label('after_' + current_chatroom.chatroom_label) 
                    and not current_chatroom.vn_obj): 
                $ renpy.call('after_' + current_chatroom.chatroom_label)
            # If you just finished a VN section, mark it as played and deliver emails/phone calls
            if (not phone 
                    and current_chatroom.vn_obj 
                    and not current_chatroom.vn_obj.played 
                    and current_chatroom.vn_obj.available):
                $ current_chatroom.vn_obj.played = True
                if renpy.has_label('after_' + current_chatroom.chatroom_label):
                    $ renpy.call('after_' + current_chatroom.chatroom_label)
        elif (current_chatroom.plot_branch 
                and current_chatroom.vn_obj 
                and not current_chatroom.vn_obj.played 
                and current_chatroom.vn_obj.available):
            $ current_chatroom.vn_obj.played = True
        elif (not current_chatroom.plot_branch 
                and not phone and current_chatroom.vn_obj 
                and not current_chatroom.vn_obj.played 
                and current_chatroom.vn_obj.available):
            $ current_chatroom.vn_obj.played = True
                
        if not current_chatroom.expired and not current_chatroom.buyback:
            $ deliver_calls(current_chatroom.chatroom_label)
            
        if current_chatroom.expired and not current_chatroom.buyback:
            $ current_chatroom.participated = False
        else:
            $ current_chatroom.participated = True
        $ deliver_emails()   
        $ next_chatroom()
        $ renpy.retain_after_load()
        if not chips_available:
            $ chips_available = hbc_bag.draw()
        
        stop music
        if starter_story:
            $ starter_story = False
            call screen chat_home
            return
        else:
            $ deliver_next()
            # $ renpy.save(mm_auto)
            call screen chatroom_timeline(current_day, current_day_num)
            return

    
# This shows the signature screen, which records your total heart points
# It shows hourglass points as well but currently there is no way to get
# more hourglasses
screen signature_screen(phone=True):
    zorder 5
    modal True
    if phone and not persistent.custom_footers:
        add "save_exit" ypos 1220
    elif phone and persistent.custom_footers:
        add "custom_save_exit" ypos 1220
    add "choice_darken"
    window:
        xalign 0.5
        yalign 0.5
        xsize 682
        ysize 471
        background 'signature'
        has vbox
        spacing 10
        null height 140 width 682
        text "This conversation will be archived in the RFA records.":
            style "save_exit_text" xalign 0.5     
        fixed:
            xalign 0.5
            ysize 60
            xfit True
            add "heart_hg" 
            hbox:
                spacing 170
                yalign 0.5
                xoffset 65
                window:
                    xsize 70
                    ysize 40
                    text "[chatroom_hp]" style "points" xalign 1.0
                window:
                    xsize 80
                    ysize 40
                    text "[chatroom_hg]" style "points" xalign 1.0
        
        text "I hereby agree to treat this conversation as confidential.":
            style "save_exit_text"
        
        textbutton _('sign'):
            xysize (211, 52)
            text_style 'sign'
            align (0.5, 0.842)
            focus_mask True
            background 'sign_btn' padding(20,20)
            activate_sound "audio/sfx/UI/end_chatroom.mp3"
            hover_background 'sign_btn_clicked'
            action Return()



    
    

    

    
    
    
    
    
    