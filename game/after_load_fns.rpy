init python:
    ## This function is called right after Ren'Py loads a save game
    ## It allows the program to make changes to existing variables or
    ## define variables that have yet to exist so that save files
    ## continue to work
    def update_var_compatibility():
        """
        Update this save file for compatibility with new versions.
        """

        while store._version != "2.2":
            if store._version == "2.1.1":
                float_ver = 2.1001
            else:
                float_ver = float(store._version)
                        
            # Update persistent values to be compatible with v2.0           
            if float_ver < 2.00:
                reset_old_persistent()
                store._version = '2.00'

            # Update Routes for the history screen
            if float_ver <= 2.00:
                try:
                    for r in all_routes:
                        test = r.ending_chatrooms
                except AttributeError:
                    for r in all_routes:
                        setattr(r, 'ending_chatrooms', [])
                        # Not 100% accurate, but for most cases
                        # should be all right; check number of strings
                        # in the route
                        ending_titles = []
                        for day in reversed(r.route):
                            if day.archive_list:
                                ending_titles.extend(find_route_endings(r, 
                                    day.archive_list, ending_titles))
                        if ending_titles == []:
                            # There were no titles; final chatroom is
                            # just the last one
                            for day in reversed(r.route):
                                if day.archive_list:
                                    if day.archive_list[-1].vn_obj:
                                        r.ending_chatrooms.append(
                                            day.archive_list[
                                                -1].vn_obj.vn_label)
                                    else:
                                        r.ending_chatrooms.append(
                                            day.archive_list[
                                                -1].chatroom_label)
                store._version = '2.1'

            # persistent.heart_notification changed to persistent.animated_icons
            if float_ver < 2.2:
                store.persistent.animated_icons = not store.persistent.heart_notifications
                store._version = "2.2"
            
            store._version = "2.2"
                                        

    def find_route_endings(route, chatlist, titles):
        """
        Find the last chatroom after a given string and add the appropriate
        label to the route's ending_chatrooms list.
        """

        # First, count the number of strings (endings) in this list
        extra_ending_titles = []
        ending_indices = []
        for i, chat in enumerate(chatlist):
            if (not isinstance(chat, store.ChatHistory)
                and not isinstance(chat, ChatHistory)
                and not isinstance(chat, VNMode)
                and not isinstance(chat, store.VNMode)):
                if chat not in titles:
                    extra_ending_titles.append(chat)
                    ending_indices.append(i)
                
        if len(ending_indices) == 0:
            return extra_ending_titles
        # Endings will now be the chatroom just before the ending index
        # EXCEPT for the first index which is changed to a zero so that
        # it fetches the last item of the list
        ending_indices[0] = 0
        for i in ending_indices:
            if (isinstance(chatlist[i-1], store.ChatHistory)
                    or isinstance(chatlist[i-1], ChatHistory)):
                if chatlist[i-1].vn_obj:
                    route.ending_chatrooms.append(
                        chatlist[i-1].vn_obj.vn_label)
                elif (chatlist[i-1].plot_branch
                        and chatlist[i-1].plot_branch.vn_after_branch):
                    route.ending_chatrooms.append(
                        chatlist[i-1].plot_branch.stored_vn.vn_label)
                else:
                    route.ending_chatrooms.append(
                        chatlist[i-1].chatroom_label)
            elif (isinstance(chatlist[i-1], store.VNMode)
                    or isinstance(chatlist[i-1], VNMode)):
                route.ending_chatrooms.append(chatlist[i-1].vn_label)
        return extra_ending_titles


    def reset_old_persistent():
        """Reset problematic persistent values to their original values."""

        # First, save HP and HG
        temp_HP = store.persistent.__dict__['HP']
        temp_HG = store.persistent.__dict__['HG']
        # Save accessibility preferences
        temp_screenshake = store.persistent.__dict__['screenshake']
        temp_banners = store.persistent.__dict__['banners']
        temp_hacking_effects = store.persistent.__dict__['hacking_effects']
        temp_audio_captions = store.persistent.__dict__['audio_captions']
        temp_autoanswer_timed_menus = store.persistent.__dict__['autoanswer_timed_menus']
        temp_heart_notifications = store.persistent.__dict__['heart_notifications']
        temp_animated_icons = store.persistent.__dict__['animated_icons']
        temp_dialogue_outlines = store.persistent.__dict__['dialogue_outlines']
        temp_starry_contrast = store.persistent.__dict__['starry_contrast']
        temp_window_darken_pct = store.persistent.__dict__['window_darken_pct']
        temp_vn_window_dark = store.persistent.__dict__['vn_window_dark']
        temp_vn_window_alpha = store.persistent.__dict__['vn_window_alpha']
        temp_custom_footers = store.persistent.__dict__['custom_footers']
        # MC name, pronouns, and pfp
        temp_MC_pic = store.persistent.__dict__['MC_pic']
        temp_name = store.persistent.__dict__['name']
        temp_pronoun = store.persistent.__dict__['pronoun']
        # Played chatrooms
        temp_completed_chatrooms = store.persistent.__dict__['completed_chatrooms']
        temp_guestbook = store.persistent.__dict__['guestbook']
        # Developer settings/preferences
        temp_real_time = store.persistent.__dict__['real_time']
        temp_testing_mode = store.persistent.__dict__['testing_mode']
        # Note: don't save unlocked Album objects
        # or saved email/text/ringtones
        temp_first_boot = store.persistent.__dict__['first_boot']
        temp_animated_backgrounds = store.persistent.__dict__['animated_backgrounds']
        # temp_on_route = store.persistent.__dict__['on_route']
        temp_hidden_route = store.persistent.__dict__['hidden_route']

        # Reset persistent
        store.persistent._clear()

        # Restore saved values
        store.persistent.HP = temp_HP
        store.persistent.HG = temp_HG
        store.persistent.screenshake = temp_screenshake
        store.persistent.banners = temp_banners
        store.persistent.hacking_effects = temp_hacking_effects
        store.persistent.audio_captions = temp_audio_captions
        store.persistent.autoanswer_timed_menus = temp_autoanswer_timed_menus
        store.persistent.heart_notifications = temp_heart_notifications
        store.persistent.animated_icons = temp_animated_icons
        store.persistent.dialogue_outlines = temp_dialogue_outlines
        store.persistent.starry_contrast = temp_starry_contrast
        store.persistent.window_darken_pct = temp_window_darken_pct
        store.persistent.vn_window_dark = temp_vn_window_dark
        store.persistent.vn_window_alpha = temp_vn_window_alpha
        store.persistent.custom_footers = temp_custom_footers
        store.persistent.MC_pic = temp_MC_pic
        store.persistent.name = temp_name
        store.persistent.pronoun = temp_pronoun
        store.persistent.completed_chatrooms = temp_completed_chatrooms
        store.persistent.guestbook = temp_guestbook
        store.persistent.real_time = temp_real_time
        store.persistent.testing_mode = temp_testing_mode
        store.persistent.first_boot = temp_first_boot
        store.persistent.on_route = False
        store.persistent.hidden_route = temp_hidden_route   
        store.persistent.animated_backgrounds = temp_animated_backgrounds                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

        store.persistent.ja_album = []
        store.persistent.ju_album = []
        store.persistent.r_album = []
        store.persistent.s_album = []
        store.persistent.u_album = []
        store.persistent.v_album = []
        store.persistent.y_album = []
        store.persistent.z_album = []
        store.persistent.common_album = []

        store.persistent.phone_tone = 'audio/sfx/Ringtones etc/phone_basic_1.wav'
        store.persistent.text_tone = "audio/sfx/Ringtones etc/text_basic_1.wav"
        store.persistent.email_tone = 'audio/sfx/Ringtones etc/email_basic_1.wav'
        store.persistent.phone_tone_name = "Default"
        store.persistent.text_tone_name = "Default"
        store.persistent.email_tone_name = "Default 1"
        define_variables()
        return
        

    
    def define_variables():
        """Merge albums and set up the player's profile."""
        
        global all_albums        
        set_pronouns()
        
        store.chatlog = []

        # This variable keeps track of whether or not the player
        # is making a choice/on a choice menu
        store.choosing = False
        print("all_albums", all_albums)
        for p_album, reg_album in all_albums:
            merge_albums(p_album, reg_album)
        
        set_name_pfp()
            
        renpy.retain_after_load()
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
        else:
            # The program keeps track of the current day even if
            # not in real-time mode in case the player switches
            # to real-time mode
            current_game_day = date.today()
    
        no_email_notif = True
        for email in email_list:
            if not email.notified:
                no_email_notif = False
        if no_email_notif:
            renpy.hide_screen('email_popup')
        no_text_notif = True
        for c in all_characters:
            if not c.text_msg.notified:
                no_text_notif = False
                break
        if no_text_notif:
            renpy.hide_screen('text_msg_popup')
            renpy.hide_screen('text_pop_2')
            renpy.hide_screen('text_pop_3')
            
        define_variables()
        hide_heart_icons()
        renpy.hide_screen("viewCG_fullsize")
        renpy.hide_screen("viewCG_fullsize_album")
        hide_stackable_notifications()
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
            # Show the player a notification of unread messages
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
    return     

