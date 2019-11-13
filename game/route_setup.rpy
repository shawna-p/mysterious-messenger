##******************************
## USEFUL PYTHON FUNCTIONS
##******************************
init -6 python:

    ## This class stores past chatrooms that you've visited
    ## A more complete explanation of how to use it to set up 
    ## chatrooms can be found in the accompanying Script Generator
    ## spreadsheet
    class Chat_History(object):
        def __init__(self, title, save_img, chatroom_label, trigger_time, 
                        participants=[], vn_obj=False, plot_branch=False):
            # Title of the chatroom
            self.title = title
            # Image to use on the save screen after this chatroom
            self.save_img = save_img
            # Label to jump to for this chatroom
            self.chatroom_label = chatroom_label
            # Ensure the trigger time is set up properly
            # This doesn't work all the time, but it corrects times
            # like 3:45 to 03:45
            if ':' in trigger_time[:2]:
                self.trigger_time = '0' + trigger_time
            else:
                self.trigger_time = trigger_time
            # People already present in the chatroom before
            # it begins. Updates when new people enter
            self.participants = participants
            self.original_participants = copy(participants)
            # If this chatroom has a VN after it, it goes here
            self.vn_obj = vn_obj
            # Tracks whether this chatroom has been played
            self.played = False
            # Tracks whether the player participated in this chatroom
            self.participated = False
            # Tracks whether the program should allow the user to
            # play this chatroom or if it'll be greyed out/unavailable
            self.available = False
            # Tracks whether this chatroom has expired
            self.expired = False
            # The expired label for this chatroom
            self.expired_chat = chatroom_label + '_expired'
            # Tracks whether there's a plot branch after this chatroom
            self.plot_branch = plot_branch
            # Tracks if the user bought back this chatroom after it
            # expired
            self.buyback = False
            # Tracks if the user bought this chatroom ahead of time
            # so it can remain unlocked regardless of the current time
            self.buyahead = False
            # Used for replays; this list keeps track of the choices
            # the user made when they went through this chatroom
            self.replay_log = []
            
        ## Adds a participant to the chatroom
        def add_participant(self, chara):
            if not chara in self.participants:
                self.participants.append(chara)

        # Saves the chatlog of this chatroom for replays
        # Also adjusts the length of time to wait before
        # posting replies from MC
        def save_log(self, the_log):
            global m, pv
            self.replay_log = deepcopy(the_log)
            for c in self.replay_log:
                if c.who == m and c.pauseVal == 0:
                    c.pauseVal = pv

                
        ## Resets participants to whatever they were before the
        ## user played this chatroom (often used when a player
        ## backs out of a chatroom, for example)
        def reset_participants(self):
            self.participants = copy(self.original_participants)
            
            
    ## This class stores the information needed for the Visual 
    ## Novel portions of the game
    class VN_Mode(object):
        def __init__(self, vn_label, who=None, party=False):
            # The label to jump to for the VN
            self.vn_label = vn_label
            # Whose picture is on the VN icon
            self.who = who
            # Whether the VN has been played
            self.played = False
            # Whether the VN is available
            self.available = False
            # Whether this VN is the party/needs the party icon
            self.party = party
              
            
    ## This object stores a day's worth of chatrooms
    class Archive(object):
        def __init__(self, day, archive_list=[], route='day_common2'):
            # The day e.g. "1st"
            self.day = day
            # A list of chatrooms taking place on this day
            self.archive_list = archive_list
            # The route this day is considered a part of
            self.route = route
            
    ## This function ensures the next chatroom or VN section 
    ## becomes available.
    ## By default it unlocks chatrooms in sequence, but when 
    ## persistent.real_time is active it unlocks chatrooms 
    ## according to real-time
    def next_chatroom():
        global chat_archive, available_calls, current_chatroom, test_ran
        global today_day_num, days_to_expire, current_game_day
        global incoming_call, current_call
        triggered_next = False
        notify_player = False
        current_time = None

        # A tiny function-in-a-function to simplify real-time checks
        def compare_times(day_i, the_chatroom):
            # If the current hour is less than the next chatroom's
            # trigger time, and the current day is the same as the
            # days_to_expire, it's too early for this chatroom
            if (int(current_time.military_hour) < 
                    int(the_chatroom.trigger_time[:2]) 
                    and (day_i+1) == days_to_expire):
                return False
            
            # If the current hour is the same as the chatroom hour,
            # and today is the day to expire, we check minutes
            elif (int(current_time.military_hour) == 
                    int(the_chatroom.trigger_time[:2]) 
                    and (day_i+1) == days_to_expire):
                if (int(current_time.minute) 
                        < int(the_chatroom.trigger_time[-2:])):
                    return False

            return True

        # Figures out whether to expire chatrooms/make them
        # available/etc
        def adjust_chatrooms(day_i, the_chatroom, notify=False,
                prev_chat=False, check_time=False):
            the_chatroom.available = True
            current_chatroom = the_chatroom
            # If this chatroom has *just*  triggered, we also want to 
            # deliver incoming phone calls to the player, so we check for
            # that now. It's given a grace period of 1 min so if the trigger
            # time is 2:00 and it's 2:01 it'll still notify the player
            if check_time:
                if ((day_i+1) == days_to_expire 
                        and (int(current_time.minute)
                        == int(the_chatroom.trigger_time[-2:]) 
                        or int(current_time.minute)- 1 
                        == int(the_chatroom.trigger_time[-2:]))):
                    expire_chatroom(prev_chat, current_chatroom, True)
                else:
                    expire_chatroom(prev_chat, current_chatroom)

            if prev_chat and not check_time:
                expire_chatroom(prev_chat, current_chatroom)

            if notify:
                notify_player = True

            today_day_num = day_i



        if not persistent.real_time:
            for archive in chat_archive:
                if archive.archive_list:
                    for chatroom in archive.archive_list:
                        # Edge case; if they haven't played the currently
                        # available chatroom, don't make anything new
                        # available and stop
                        if chatroom.available and not chatroom.played:
                            triggered_next = True
                            break
                        # If the chatroom has an unavailable VN after it,
                        ## make that available and stop
                        if (chatroom.played and chatroom.vn_obj 
                                and not chatroom.vn_obj.available):
                            chatroom.vn_obj.available = True
                            triggered_next = True
                            break
                        # If they haven't played the VN yet, 
                        # don't make anything new available and stop
                        if (chatroom.played and chatroom.vn_obj 
                                and chatroom.vn_obj.available 
                                and not chatroom.vn_obj.played):
                            triggered_next = True
                            break              
                        # If the current chatroom isn't available, 
                        # make it available and stop. Also decrease 
                        # the time old phone calls are available
                        if not chatroom.available:
                            chatroom.available = True
                            current_chatroom = chatroom
                            for phonecall in available_calls:
                                phonecall.decrease_time()
                            triggered_next = True
                            break               
                if triggered_next:
                    break
        else:   # We're using real-time mode
            if days_to_expire > len(chat_archive):
                days_to_expire = len(chat_archive)
                return
            # First, check if any days have passed
            date_diff = date.today() - current_game_day
            if date_diff.days > 0:
                # At least one day has passed; increase 
                # days_to_expire accordingly
                days_to_expire += date_diff.days
            current_game_day = date.today()
            # Next, check what time it is
            current_time = upTime()
            # Now, go through the list of chatrooms and find out if
            # there's a new one to be triggered
            for day_index, archive in enumerate(chat_archive[:days_to_expire]):
                if (not archive.archive_list or len(archive.archive_list) < 1):
                    continue

                for chat_index, chatroom in enumerate(archive.archive_list):
                    # First, we check if there's a played chatroom 
                    # with a VN after it. If the chatroom has an
                    # unavailable VN after it, make that available
                    if (chatroom.played and chatroom.vn_obj 
                            and not chatroom.vn_obj.available):
                        chatroom.vn_obj.available = True
                    # If this chatroom isn't available, check if it's 
                    # time to make it available
                    if not chatroom.available:                            
                        # Check the time on the chatroom
                        # If we're loading a file, we might need 
                        # to make lots of chatrooms unavailable in 
                        # a row. So we check if this is eligible
                        # for expiry
                        if not compare_times(day_index, chatroom):
                            triggered_next = True
                            break
                        
                        if (int(current_time.military_hour) > 
                                int(chatroom.trigger_time[:2]) 
                                or (day_index+1) < days_to_expire):
                            # Current hour is later than the chatroom 
                            # trigger time. Time to trigger the chatroom
                            # First, check if it's the last chatroom of 
                            # the day
                            if (chat_index+1 == len(archive.archive_list) 
                                    and not chatroom.plot_branch 
                                    and not (day_index+1) < days_to_expire):
                                triggered_next = True
                            if chat_index == 0 and day_index == 0:
                                # If this is the first chatroom of the route, 
                                # there's nothing to expire prior to it, 
                                # so we trigger the chatroom
                                adjust_chatrooms(day_index, chatroom)
                            elif chat_index > 0:
                                # This is the second or later 
                                # chatroom of the day
                                adjust_chatrooms(day_index, chatroom, True,
                                    archive.archive_list[chat_index-1])
                            elif chat_index == 0 and day_index > 0:
                                # This is the first chatroom of the day 
                                # but there are days before this chatroom 
                                # with chatrooms that might be expired
                                adjust_chatrooms(day_index, chatroom, True,
                                    chat_archive[day_index-1].archive_list[-1])
                            continue
                        
                        # Time for the chatroom to trigger
                        # First, check if it's the last chatroom of the day
                        if (chat_index-1 == len(archive.archive_list) 
                                and not chatroom.plot_branch):
                            triggered_next = True

                        if chat_index == 0 and day_index == 0:
                            # If this is the first chatroom of the route, 
                            # there's nothing to expire, so we trigger
                            # the chatroom
                            adjust_chatrooms(day_index, chatroom)

                        elif chat_index > 0:
                            # This is the second or later chatroom of the day
                            adjust_chatrooms(day_index, chatroom, True,
                                archive.archive_list[chat_index-1], True)                                
                            # We don't set triggered_next to True so it
                            # makes more chatrooms expire if necessary

                        elif chat_index == 0 and day_index > 0:
                            # This is the first chatroom of the day but 
                            # there are days before this chatroom with 
                            # chatrooms that might be expired
                            adjust_chatrooms(day_index, chatroom, True,
                                chat_archive[day_index-1].archive_list[-1],
                                True)
                            

                        
                if triggered_next:
                    break
            if notify_player:
                # Let the player know a new chatroom is open
                the_msg = "[[new chatroom] " + current_chatroom.title
                renpy.music.play('audio/sfx/Ringtones etc/text_basic_1.wav', 'sound')
                renpy.show_screen('confirm', 
                        message=the_msg, yes_action=Hide('confirm'))
            # We also deliver any incoming calls in the event 
            # that the player *just* missed one
            if incoming_call:
                current_call = incoming_call
                incoming_call = False
                renpy.call('new_incoming_call', phonecall=current_call)
            
    ## A helper function that expires chatrooms and makes their phonecalls/
    ## text messages available
    def expire_chatroom(prev_chatroom, current_chatroom, 
                                deliver_incoming=False):
        # The previous chatroom expires if not played
        if (not prev_chatroom.played
                and not prev_chatroom.buyback 
                and not prev_chatroom.buyahead):
            prev_chatroom.expired = True
        else:
            return
            
        # We need to set a time for the missed call; should be
        # equal to the trigger time for the current chatroom
        time_for_call = upTime()
        time_for_call.twelve_hour = current_chatroom.trigger_time[:2]
        if time_for_call.twelve_hour == '00':
            time_for_call.twelve_hour = '12'
            time_for_call.am_pm = 'AM'
        elif time_for_call.twelve_hour == '12':
            time_for_call.am_pm = 'PM'
        elif int(time_for_call.twelve_hour) > 12:
            time_for_call.twelve_hour = str(abs
                                (12 - int(time_for_call.twelve_hour)))
            time_for_call.am_pm = 'PM'
        else:
            time_for_call.am_pm = 'AM'                                    
        time_for_call.minute = current_chatroom.trigger_time[-2:]
        
        # There's a rare case where we want to trigger an incoming call
        # because this chatroom has *just* expired
        if deliver_incoming:
            deliver_calls(prev_chatroom.chatroom_label, False, time_for_call)
        else:
            deliver_calls(prev_chatroom.chatroom_label, True, time_for_call) 
        
        # Checks for a post-chatroom label
        if renpy.has_label('after_' + prev_chatroom.chatroom_label): 
            renpy.call_in_new_context('after_' + prev_chatroom.chatroom_label)
        # We don't set triggered_next to True so it makes
        # more chatrooms expire if necessary
        for phonecall in available_calls:
            phonecall.decrease_time()
            
        # This delivers the text messages
        deliver_all()
                
    ## A quick function to see how many chatrooms there are left 
    ## to be played through
    ## This is used so emails will always be delivered before the party
    def num_future_chatrooms():
        global chat_archive
        total = 0
        for archive in chat_archive:
            if archive.archive_list:
                for chatroom in archive.archive_list:
                    if not chatroom.played: 
                        total += 1
        return total
                
        
    ## Delivers the next available text message and triggers an incoming
    ## phone call, if applicable
    def deliver_next():
        global text_queue, incoming_call, available_calls, current_call
        global persistent, inst_text, all_characters
        
        for msg in text_queue:
            if msg.msg_list:
                msg.deliver()
                break             
        if incoming_call:
            current_call = incoming_call
            incoming_call = False
            renpy.call('new_incoming_call', phonecall=current_call)
            
        # If instant texting is turned on, we deliver 
        # text messages differently
        # These are delivered all at the same time
        if persistent.instant_texting:
            small_char_list = [ c for c in all_characters
                                    if not c == m and c.private_text ]
            for character in small_char_list:
                if not character.private_text_read:
                    # New messages were delivered/written; popup needed
                    character.private_text_read = "Notified"
                    renpy.music.play(persistent.text_tone, 'sound')
                    renpy.show_screen('text_msg_popup_instant', 
                                                the_char=character) 
    
    ## This function takes a route (new_route) and merges it with the
    ## current route
    def merge_routes(new_route, is_vn=False):
        global chat_archive, most_recent_chat
        most_recent_chat.plot_branch = False
        for archive in chat_archive:
            for archive2 in new_route:
                if archive2.day == archive.day:
                    # If there is a conditional VN object
                    if is_vn:
                        # replace the old VN obj with the new one
                        archive.archive_list[-1].vn_obj = (archive2.
                                                    archive_list[0].vn_obj)
                        del archive2.archive_list[0]
                        is_vn = False
                    
                    archive.archive_list += archive2.archive_list
                    archive.route = archive2.route
                    
    ## This function returns the percentage of chatrooms the player
    ## has participated in, from first_day to last_day (or from first_day
    ## until the end of the route, if last_day=None)
    def participated_percentage(first_day=1, last_day=None):
        global chat_archive
        # For example, if we want to check participation from Day 2 to
        # Day 4, then first_day = 2 and last_day = 4
        # However, index-wise, those will be from index 1 to 3
        # so we subtract 1 from first_day
        first_day -= 1
            
        completed_chatrooms = 0
        num_chatrooms = 0
            
        for archive in chat_archive[first_day:last_day]:
            if archive.archive_list:
                for chatroom in archive.archive_list:
                    num_chatrooms += 1
                    if chatroom.participated:
                        completed_chatrooms += 1
        # Ensure we're not dividing by zero
        if num_chatrooms == 0:
            num_chatrooms == 1
        return (completed_chatrooms * 100 // num_chatrooms)
    
              
    ## Calculates whether or not the player can proceed
    ## through the plot branch
    def can_branch():
        global chat_archive
        for archive in chat_archive:
            if archive.archive_list:
                for chatroom in archive.archive_list:
                    if (chatroom.played 
                            and chatroom.plot_branch 
                            and (not chatroom.vn_obj 
                                or chatroom.vn_obj.played)):
                        return True
                    elif chatroom.vn_obj and not chatroom.vn_obj.played:
                        return False
                    elif not chatroom.played:
                        return False
        return False
        
    ## Calculates when the next chatroom is available
    def next_chat_time():
        global chat_archive
        for archive in chat_archive:
            if archive.archive_list:
                for chatroom in archive.archive_list:
                    if not chatroom.available:
                        return chatroom.trigger_time
        return 'Unknown Time'
        
    ## Makes the chatrooms for the next 24 hours available
    def chat_24_available():
        global chat_archive, today_day_num, days_to_expire, unlock_24_time
        current_time = upTime()
        unlock_24_time = current_time
        days_to_expire += 1
        is_branch = False
        # Check chatrooms for the current day
        for chatroom in chat_archive[today_day_num].archive_list:
            # Hour for this chatroom is greater than now; make available
            if (int(current_time.military_hour) 
                    < int(chatroom.trigger_time[:2])):
                if chatroom.plot_branch:
                    is_branch = True
                chatroom.available = True
                chatroom.buyahead = True
            # Hour is the same; check minute
            elif (int(current_time.military_hour) 
                    == int(chatroom.trigger_time[:2])):            
                if int(current_time.minute) < int(chatroom.trigger_time[-2:]):
                    if chatroom.plot_branch:
                        is_branch = True
                    # Minute is greater; make available
                    chatroom.available = True
                    chatroom.buyahead = True
        # Now check chatrooms for the next day
        if chat_archive[today_day_num+1].archive_list:
            for chatroom in chat_archive[today_day_num+1].archive_list:
                # Hour for this chatroom is smaller than now; make available
                if (int(current_time.military_hour) 
                        > int(chatroom.trigger_time[:2])):
                    if chatroom.plot_branch:
                        is_branch = True
                    chatroom.available = True
                    chatroom.buyahead = True
                # Hour is the same; check minute
                elif (int(current_time.military_hour) 
                        == int(chatroom.trigger_time[:2])):            
                    if (int(current_time.minute) 
                            > int(chatroom.trigger_time[-2:])):
                        if chatroom.plot_branch:
                            is_branch = True
                        # Minute is smaller; make available
                        chatroom.available = True
                        chatroom.buyahead = True
        # Increase the day number
        today_day_num += 1
        # If we were able to make everything available,
        # unlock_24_time can be reset
        if not is_branch:
            unlock_24_time = False 
                    
                    
        
            
# This archive will store every chatroom in the game. If done correctly,
# the program will automatically set variables and make chatrooms available
# for you
default chat_archive = [
    Archive('Tutorial', 
        [Chat_History('Example Chatroom', 'auto', 'example_chat', '00:01', []),                                     
        Chat_History('Inviting Guests', 'auto', 'example_email', '09:11', [z]),
        Chat_History('Text Message Example', 'auto', 'example_text', '09:53', [r], VN_Mode('vn_mode_tutorial', r)),
        Chat_History('Timed Menus', 'auto', 'timed_menus', '11:28', [s]),
        Chat_History('Pass Out After Drinking Caffeine Syndrome', 'auto', 'tutorial_chat', '15:05', [s]),
        Chat_History('Invite to the meeting', 'jumin', 'popcorn_chat', '18:25', [ja, ju], VN_Mode('popcorn_vn', ju)),
        Chat_History('Hacking', 'auto', 'hack_example', '20:41', []),
        Chat_History('Plot Branches', 'auto', 'plot_branch_tutorial', '22:44', [], False, True)]),                                    
    Archive('1st'),                        
    Archive('2nd'),
    Archive('3rd'),
    Archive('4th'),
    Archive('5th'),
    Archive('6th'),
    Archive('7th'),
    Archive('8th'),
    Archive('9th'),
    Archive('10th'),
    Archive('Final')]
                        
default tutorial_bad_end = [Archive('Tutorial', 
    [Chat_History('An Unfinished Task', 'auto', 'tutorial_bad_end', '23:26', [v])] )]
default tutorial_good_end = [Archive('Tutorial', 
    [Chat_History('Plot Branches', 'auto', 'plot_branch_tutorial', '22:44', [], VN_Mode('plot_branch_vn')),
    Chat_History("Onwards!", 'auto', 'tutorial_good_end', '23:26', [u], VN_Mode('good_end_party', None, True))])]
                        
default seven_route = [ Archive('5th', [], 'day_s'),
                        Archive('6th', [], 'day_s'),
                        Archive('7th', [], 'day_s'),
                        Archive('8th', [], 'day_s'),
                        Archive('9th', [], 'day_s'),
                        Archive('10th', [], 'day_s'),
                        Archive('Final', [], 'day_s')]
