init python:
    ## This function is called right after Ren'Py loads a save game
    ## It allows the program to make changes to existing variables or
    ## define variables that have yet to exist so that save files
    ## continue to work
    def update_var_compatibility():
        """
        Update this save file for compatibility with new versions.
        """

        if not isinstance(store._version, tuple):
            # Turn the version into a tuple like (3, 0, 0)
            tuple_ver = store._version.split('.')
            if len(tuple_ver) < 3:
                tuple_ver = (int(tuple_ver[0]), int(tuple_ver[1]), 0)
            else:
                tuple_ver = (int(tuple_ver[0]), int(tuple_ver[1]), int(tuple_ver[2]))
            store._version = tuple_ver


        # Update persistent values to be compatible with v2.0
        if store._version < (2, 0, 0):
            reset_old_persistent()
            store._version = (2, 0, 0)

        # Update Routes for the history screen
        if store._version < (2, 1, 0):
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
            store._version = (2, 1, 0)

        # persistent.heart_notification changed to persistent.animated_icons
        if store._version < (2, 2, 0):
            store.persistent.animated_icons = not store.persistent.heart_notifications
            store._version = (2, 2, 0)

        if store._version < (3, 0, 0):

            for chara in store.all_characters:
                # Ensure new fields are added
                rebuild_character(chara, give_spendable=True)
                # Unlock profile pictures
                unlock_profile_pics(chara)

            # Update ChatHistory and VNMode objects
            if store.chat_archive:
                for day in store.chat_archive:
                    day.convert_archive(True)

            # Update several variables
            if store.current_chatroom:
                store.current_timeline_item = store.current_chatroom
                store.current_chatroom = None
            if store.chat_archive:
                store.story_archive = store.chat_archive
                store.chat_archive = None
            if store.most_recent_chat:
                store.most_recent_item = store.most_recent_chat
                store.most_recent_chat = None
            if store.chatroom_hp:
                store.collected_hp = store.chatroom_hp
                store.collected_hg = store.chatroom_hg
                store.chatroom_hp = None
                store.chatroom_hg = None
            if store.persistent.completed_chatrooms:
                store.persistent.completed_story = set(
                    store.persistent.completed_chatrooms.keys())
                store.persistent.completed_chatrooms = None

            store.use_2_2_guest = True
            #TODO: CONVERT EXISTING GUESTS

            if store.persistent.pronoun == 'non binary':
                store.persistent.pronoun = 'they/them'
            elif store.persistent.pronoun == 'female':
                store.persistent.pronoun = 'she/her'
            elif store.persistent.pronoun == 'male':
                store.persistent.pronoun = 'he/him'

            if store.persistent.autoanswer_timed_menus is not None:
                store.persistent.use_timed_menus = not store.persistent.autoanswer_timed_menus
                store.persistent.autoanswer_timed_menus = None


            # Update music variables to their .ogg counterparts
            update_music()
            # Try to check if this save is on Tutorial Day, in which case
            # paraphrase choices should be off.
            try:
                if store.story_archive[0].day == "Tutorial":
                    store.paraphrase_choices = False
                else:
                    store.paraphrase_choices = True
            except:
                store.paraphrase_choices = True


            store._version = (3, 0, 0)

        # Turn the version back into a string
        store._version = '.'.join(map(str, store._version))

    def update_music():
        if '.mp3' in store.music_dictionary.keys()[0]:
            store.music_dictionary = dict((key.split('.mp3')[0] + '.ogg', value)
                for (key, value) in store.music_dictionary.items())


    def unlock_profile_pics(who):
        """Ensure seen CGs and profile pictures are unlocked where possible."""

        # Add album thumbnails
        try:
            if who.file_id in store.all_albums:
                album = getattr(store.persistent, who.file_id + '_album', [])
            else:
                album = []
            for pic in album:
                if (pic.unlocked
                        and pic.get_thumb()
                            not in store.persistent.unlocked_prof_pics
                        and pic.thumbnail_tuple
                            not in store.persistent.unlock_profile_pics):
                    add_img_to_set(store.persistent.unlocked_prof_pics,
                        pic.get_thumb())
        except:
            print("ERROR: Could not add " + who.file_id + "'s album",
                "pictures to unlock list.")

        # Add currently shown profile picture
        if who.prof_pic not in store.persistent.unlocked_prof_pics:
            add_img_to_set(store.persistent.unlocked_prof_pics,
                        who.prof_pic)
        # Add default profile picture
        if who.default_prof_pic not in store.persistent.unlocked_prof_pics:
            add_img_to_set(store.persistent.unlocked_prof_pics,
                        who.default_prof_pic)



    def find_route_endings(route, chatlist, titles):
        """
        Find the last chatroom after a given string and add the appropriate
        label to the route's ending_labels list.
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
                    route.ending_labels.append(
                        chatlist[i-1].vn_obj.vn_label)
                elif (chatlist[i-1].plot_branch
                        and chatlist[i-1].plot_branch.vn_after_branch):
                    route.ending_labels.append(
                        chatlist[i-1].plot_branch.stored_vn.vn_label)
                else:
                    route.ending_labels.append(
                        chatlist[i-1].chatroom_label)
            elif (isinstance(chatlist[i-1], store.VNMode)
                    or isinstance(chatlist[i-1], VNMode)):
                route.ending_labels.append(chatlist[i-1].vn_label)
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
        # v3.0 new vars
        temp_mc_unlocked_pfps = store.persistent.__dict__['mc_unlocked_pfps']
        temp_unlocked_prof_pics = store.persistent.__dict__['unlocked_prof_pics']
        temp_bought_prof_pics = store.persistent.__dict__['bought_prof_pics']
        temp_spendable_hearts = store.persistent.__dict__['spendable_hearts']
        temp_pv = store.persistent.__dict__['pv']
        temp_completed_story = store.persistent.__dict__['completed_story']
        temp_completed_chatrooms = store.persistent.__dict__['completed_chatrooms']
        temp_timed_menu_pv = store.persistent.__dict__['timed_menu_pv']
        temp_animated_icons = store.persistent.__dict__['animated_icons']

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

        # v3.0 new vars
        store.persistent.mc_unlocked_pfps = temp_mc_unlocked_pfps
        store.persistent.unlocked_prof_pics = temp_unlocked_prof_pics
        store.persistent.bought_prof_pics = temp_bought_prof_pics
        store.persistent.spendable_hearts = temp_spendable_hearts
        store.persistent.pv = temp_pv
        store.persistent.completed_story = temp_completed_story
        store.persistent.completed_chatrooms = temp_completed_chatrooms
        store.persistent.timed_menu_pv = temp_timed_menu_pv
        store.persistent.animated_icons = temp_animated_icons

        store.persistent.phone_tone = 'audio/sfx/Ringtones etc/phone_basic_1.wav'
        store.persistent.text_tone = "audio/sfx/Ringtones etc/text_basic_1.wav"
        store.persistent.email_tone = 'audio/sfx/Ringtones etc/email_basic_1.wav'
        store.persistent.phone_tone_name = "Default"
        store.persistent.text_tone_name = "Default"
        store.persistent.email_tone_name = "Default 1"
        define_variables()
        return

    def vnmode_to_storymode(item, copy_everything=False):
        """Convert item to a StoryMode object and return it."""

        # print_file("LOOKING AT:", item.vn_label)
        if (item.plot_branch and item.plot_branch.stored_vn):
            pbranch = True
        elif isinstance(item.plot_branch, PlotBranch):
            pbranch = False
        else:
            pbranch = None

        new_obj = StoryMode(title=item.title, vn_label=item.vn_label,
            trigger_time=item.trigger_time, who=item.who,
            plot_branch=pbranch, party=item.party,
            save_img=item.save_img)

        if copy_everything:
            new_obj.played = item.played
            new_obj.available = item.available

        return new_obj


    def chathistory_to_chatroom(item, copy_everything=False):
        """Convert item to a ChatRoom object and return it."""

        # print_file("LOOKING AT:", item.title)

        if (item.plot_branch and item.plot_branch.stored_vn):
            pbranch = True
        elif isinstance(item.plot_branch, PlotBranch):
            pbranch = False
        else:
            pbranch = None

        new_obj = ChatRoom(title=item.title, chatroom_label=item.chatroom_label,
            trigger_time=item.trigger_time, participants=item.participants,
            plot_branch=pbranch, save_img=item.save_img)

        if item.vn_obj:
            try:
                new_obj.story_mode.parent = new_obj
            except:
                print_file("couldn't give new_obj.story_mode a parent")

            # Also need to update this item's after_label and phonecall_label
            # since prior to this update, individual items did not have
            # after_ content
            new_obj.story_mode.after_label = new_obj.after_label
            new_obj.after_label = None
            new_obj.story_mode.phonecall_label = new_obj.phonecall_label
            new_obj.phonecall_label = None

        # Need to update plot branch labels as well for compatibility so they
        # act as they were intended to when they were created
        if item.plot_branch and item.plot_branch.stored_vn:
            new_obj.plot_branch.stored_vn.after_label = new_obj.after_label
            new_obj.after_label = None
            new_obj.plot_branch.stored_vn.phonecall_label = new_obj.phonecall_label
            new_obj.phonecall_label = None

        if copy_everything:
            # Need to check all other fields as well
            # It's okay to copy list addresses since the program won't be
            # using the originals any more
            new_obj.original_participants = item.original_participants
            new_obj.played = item.played
            if new_obj.played:
                new_obj.delivered_post_items = True
            new_obj.participated = item.participated
            new_obj.available = item.available
            new_obj.expired = item.expired
            new_obj.buyback = item.buyback
            new_obj.buyahead = item.buyahead
            new_obj.replay_log = item.replay_log
            if item.vn_obj:
                new_obj.story_mode.played = item.vn_obj.played
                new_obj.story_mode.available = item.vn_obj.available
                if new_obj.story_mode.played:
                    new_obj.story_mode.delivered_post_items = True


        # Test to see if the two items are the same
        if item.title != new_obj.title:
            print_file("title:", item.title, new_obj.title)
        if item.chatroom_label != new_obj.item_label:
            print_file("label:", item.chatroom_label, new_obj.item_label)
        if item.expired_chat != new_obj.expired_label:
            print_file("expired:", item.expired_chat, new_obj.expired_label)
        if item.trigger_time != new_obj.get_trigger_time():
            print_file("time:", item.trigger_time, new_obj.get_trigger_time())
        if item.participants != new_obj.participants:
            print_file("participants:", item.participants, new_obj.participants)
        if (item.plot_branch != new_obj.plot_branch
                and not (item.plot_branch == False
                    and new_obj.plot_branch is None)
                and not (isinstance(item.plot_branch, PlotBranch)
                    and isinstance(new_obj.plot_branch, PlotBranch))):
            print_file("plot_branch:", item.plot_branch, new_obj.plot_branch)
        if (item.plot_branch and item.plot_branch.stored_vn):
            if (item.plot_branch.stored_vn.vn_label
                    != new_obj.plot_branch.stored_vn.item_label):
                print_file("plot_branch stored VN:", item.plot_branch.stored_vn.vn_label,
                    new_obj.plot_branch.stored_vn.item_label)
        if (item.vn_obj and new_obj.story_mode):
            if item.vn_obj.vn_label != new_obj.story_mode.item_label:
                print_file("vn/story mode:", item.vn_obj.vn_label,
                    new_obj.story_mode.item_label)
        if (item.vn_obj and not new_obj.story_mode):
            print_file("\ \ \ So we don't have an equivalent story mode for some reason")
            print_file("vn/story mode:", item.vn_obj, new_obj.story_mode)
        if item.save_img != new_obj.save_img:
            print_file("save_img:", item.save_img, new_obj.save_img)
        if item.played != new_obj.played:
            print_file("played:", item.played, new_obj.played)
        if item.participated != new_obj.participated:
            print_file("participated:", item.participated, new_obj.participated)
        if item.available != new_obj.available:
            print_file("available:", item.available, new_obj.available)
        if item.expired != new_obj.expired:
            print_file("expired:", item.expired, new_obj.expired)
        if item.buyback != new_obj.buyback:
            print_file("buyback:", item.buyback, new_obj.buyback)
        if item.buyahead != new_obj.buyahead:
            print_file("buyahead:", item.buyahead, new_obj.buyahead)
        if item.outgoing_calls_list != new_obj.outgoing_calls_list:
            print_file("outgoing_calls_list:", item.outgoing_calls_list, new_obj.outgoing_calls_list)
        if item.incoming_calls_list != new_obj.incoming_calls_list:
            print_file("incoming_calls_list:", item.incoming_calls_list, new_obj.incoming_calls_list)
        # if item.story_calls_list != new_obj.story_calls_list:
        #     print_file("story_calls_list:", item.story_calls_list, new_obj.story_calls_list)

        return new_obj

    def rebuild_character(chara, give_spendable=False):
        """
        Copy all of chara's fields into a new ChatCharacter object and
        replace chara with it.
        """

        # print_file("All of chara's fields:", chara.__dict__)
        for key, val in chara.__dict__.items():
            if "_m1_character_definitions__" in key:
                chara.__dict__["_m1_chatcharacter_definition__"
                    + key[27:]] = val

        new_c = ChatCharacter(chara.name, chara.file_id, chara.prof_pic,
            chara.participant_pic, chara.heart_color, chara.cover_pic,
            chara.status, chara.bubble_color, chara.glow_color,
            chara.emote_list, chara.voicemail.phone_label, chara.right_msgr,
            chara.homepage_pic, chara.phone_char, chara.vn_char,
            chara.p_name)

        # Only fields that aren't transferred:
        #   bonus_pfp (new this version; don't need to copy)
        #   default_prof_pic
        #   seen_updates
        #   heart_points
        #   good_heart
        #   bad_heart
        #   text_msg
        #   real_time_text
        new_c.default_prof_pic = chara.default_prof_pic
        new_c.seen_updates = chara.seen_updates
        new_c.heart_points = chara.heart_points
        new_c.good_heart = chara.good_heart
        new_c.bad_heart = chara.bad_heart
        new_c.real_time_text = chara.real_time_text

        text_obj = chara.text_msg
        new_text = TextMessage(new_c)
        new_text.msg_list = text_obj.msg_list
        new_text.msg_queue = text_obj.msg_queue
        new_text.reply_label = text_obj.reply_label
        new_text.read = text_obj.read
        new_text.cg_unlock_list = text_obj.cg_unlock_list
        new_text.notified = text_obj.notified
        # This may cause the player to miss out on a heart point but avoids
        # problems when re-defining characters
        new_text.heart = False
        new_text.heart_person = None
        new_text.bad_heart = False

        new_c.text_msg = new_text

        if give_spendable:
            # Give the player spendable hearts based on how many they've
            # earned with this character
            if chara.file_id not in store.persistent.spendable_hearts:
                store.persistent.spendable_hearts[chara.file_id] = chara.heart_points
            else:
                store.persistent.spendable_hearts[chara.file_id] += chara.heart_points

        # Replace this character object
        chara = new_c


    def define_variables():
        """Merge albums and set up the player's profile."""

        global all_albums
        set_pronouns()

        store.chatlog = []

        # This variable keeps track of whether or not the player
        # is making a choice/on a choice menu
        store.choosing = False

        if isinstance(all_albums[0], tuple) or isinstance(all_albums[0], list):
            for p_album, reg_album in all_albums:
                merge_albums(p_album, reg_album)
        else: # Should be a string
            for alb in all_albums:
                merge_albums_string(alb)

        set_name_pfp()

        #if not store.persistent.unlocked_prof_pics:
        for chara in store.all_characters:
            unlock_profile_pics(chara)

        for chara in store.all_characters:
            if chara == store.main_character:
                chara.right_msgr = True
            else:
                chara.right_msgr = False

        # store.persistent.unlocked_prof_pics = list(dict.fromkeys(store.persistent.unlocked_prof_pics))
        # to_remove = []
        # for item in store.persistent.unlocked_prof_pics:
        #     if 'Image' in item:
        #         to_remove.append(item)
        #     if 'Drop ' in item:
        #         to_remove.append(item)
        # for item in to_remove:
        #     if item in store.persistent.unlocked_prof_pics:
        #         store.persistent.unlocked_prof_pics.remove(item)
        renpy.retain_after_load()
        return


    ########################################################
    ## This directs the player back to the chat hub after
    ## loading. It also advances the game day if real-time
    ## mode is active
    ########################################################
    def advance_day():
        global persistent
        persistent.first_boot = False
        persistent.on_route = True
        if persistent.real_time:
            print_file("Load instruction is", persistent.load_instr,
                "and current_game_day is", store.current_game_day.strftime('%Y-%m-%d'))
            if persistent.load_instr == '+1 day':
                store.days_to_expire += 1
            elif persistent.load_instr == 'Same day':
                pass
            elif persistent.load_instr == 'Auto':
                store.date_diff = date.today() - current_game_day
                store.days_to_expire += date_diff.days

            if store.days_to_expire > len(store.story_archive):
                store.days_to_expire = len(store.story_archive)
            persistent.load_instr = False

        store.current_game_day = date.today()

        # Make sure that today_day_num is correct
        d = len(store.story_archive)
        for day in reversed(store.story_archive):
            d -= 1
            if day.has_playable:
                store.today_day_num = d
                break

        if d == len(store.story_archive):
            store.today_day_num = 0

        renpy.scene(layer='screens')
        no_email_notif = True
        for email in store.email_list:
            if not email.notified:
                no_email_notif = False
        no_text_notif = True
        for c in store.all_characters:
            if not c.text_msg.notified:
                no_text_notif = False
                break

        define_variables()
        renpy.retain_after_load()
        print_file("Today is now", store.current_game_day.strftime('%Y-%m-%d'))

        if store.persistent.testing_mode:
            # Don't show this message to a user who's testing.
            return
        # This determines the content of the "you have x missed calls"
        # etc message upon loading
        popup_msg = ""
        n_email = unread_emails()
        n_text = new_message_count()
        n_call = store.unseen_calls

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
            renpy.show_screen('confirm', yes_action=Hide('confirm'),
                message=popup_msg)
        return

label after_load():

    $ renpy.set_return_stack([])
    # Forcibly make sure the game isn't in an interaction so it can
    # jump to chat_home again.
    if renpy.game.context().interacting:
        $ renpy.game.context().interacting = False
        # show screen messenger_error
    call screen chat_home
    return
