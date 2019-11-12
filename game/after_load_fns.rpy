init python:
    ## This function is called right after Ren'Py loads a save game
    ## It allows us to make changes to existing variables or define
    ## variables that have yet to exist so that save files
    ## continue to work
    def update_var_compatibility():
        # if _version == "2.02":
        #     try:
        #         for i in all_characters:
        #             test = i.text_msg_char
        #     except AttributeError:
        #         for i in all_characters:
        #             setattr(i, 'text_msg_char', "Success")
        #     # This was the version just before the new one,
        #     # so the rest of the changes will be already
        #     # implemented
        #     return
        return


########################################################
## This directs the player back to the chat hub after
## loading. It also advances the game day if real-time
## mode is active
########################################################     
label after_load():    
    python:
        if persistent.real_time:
            if persistent.load_instr == '+1 day':
                days_to_expire += 1
                current_game_day = date.today()
            elif persistent.load_instr == 'Same day':
                current_game_day = date.today()
            elif persistent.load_instr == 'Auto':
                date_diff = date.today() - current_game_day
                days_to_expire += date_diff.days
                current_game_day = date.today()
            persistent.load_instr = False
    
        no_email_notif = True
        for email in email_list:
            if not email.notified:
                no_email_notif = False
        if no_email_notif:
            renpy.hide_screen('email_popup')
        no_text_notif = True
        for msg in text_messages:
            if not msg.notified:
                no_text_notif = False
        if no_text_notif:
            renpy.hide_screen('text_msg_popup')
            
        if m.prof_pic != persistent.MC_pic and isImg(persistent.MC_pic):
            m.prof_pic = persistent.MC_pic
        if m.name != persistent.name:
            m.name = persistent.name
            name = persistent.name
        set_pronouns()
            
        renpy.hide_screen('settings_screen')
        renpy.hide_screen('save_load')
        renpy.hide_screen('menu')
        renpy.hide_screen('chat_footer')
        renpy.hide_screen('phone_overlay')
    
        # This determines the content of the "you have x missed calls"
        # etc message upon loading
        popup_msg = ""
        n_email = unread_emails()
        n_text = new_message_count()
        n_call = unseen_calls
        
        if n_email + n_text + n_call > 0:
            # We should show the player a message
            popup_msg += "You have "
        
            if n_email > 0:
                popup_msg += str(n_email) + " unread email"
                if n_email > 1:
                    popup_msg += "s"
                    
            if n_text > 0 and n_email > 0 and n_call > 0:
                popup_msg += ", "
            elif n_text > 0 and n_email > 0 and n_call <= 0:
                popup_msg += " and "
                
            if n_text > 0:
                popup_msg += str(n_text) + " unread text message"
                if n_text > 1:
                    popup_msg += "s"
            
            if n_call > 0 and n_text > 0 and n_email > 0:
                popup_msg += ", and "
            elif (n_call > 0 and n_text > 0) or (n_call > 0 and n_email > 0):
                popup_msg += " and "
                
            if n_call > 0:
                popup_msg += str(n_call) + " missed call"
                if n_call > 1:
                    popup_msg += "s"
            
            popup_msg += "."            
    if popup_msg != "":
        show screen confirm(yes_action=Hide('confirm'), message=popup_msg)
    # $ print("Is chat_home showing?", renpy.get_screen('chat_home'))
    # if not renpy.get_screen('chat_home'):#persistent.manual_load:
    #     call screen chat_home     
    # $ print("Reached the end of after_load")
    return        