##******************************
## USEFUL PYTHON FUNCTIONS
##******************************
init -6 python:
    
    # This class stores past chatrooms that you've visited
    # A more complete explanation of how to use it to set up chatrooms can be found
    # in the accompanying Script Generator spreadsheet
    class Chat_History(store.object):
        def __init__(self, title, save_img, chatroom_label, trigger_time, participants=[],
                        vn_obj=False, plot_branch=False):
            self.title = title
            self.save_img = save_img
            self.chatroom_label = chatroom_label
            # Ensure the trigger time is set up properly
            # This doesn't work all the time, but it corrects times
            # like 3:45 to 03:45
            if ':' in trigger_time[:2]:
                self.trigger_time = '0' + trigger_time
            else:
                self.trigger_time = trigger_time
            self.participants = participants
            self.vn_obj = vn_obj
            self.played = False
            self.participated = False
            self.available = False
            self.expired = False
            self.expired_chat = chatroom_label + '_expired'
            self.plot_branch = plot_branch
            self.buyback = False
            
        def add_participant(self, chara):
            if not chara in self.participants:
                self.participants.append(chara)
            
            
    # This class stores the information needed for the Visual Novel portions of the game
    class VN_Mode(store.object):
        def __init__(self, vn_label, who=None, party=False):
            self.vn_label = vn_label
            self.who = who
            self.played = False
            self.available = False
            self.party = party
              
            
    # This object stores all the chatrooms you've viewed in the game. 
    class Archive(store.object):
        def __init__(self, day, archive_list=[], route='day_common2'):
            self.day = day
            self.archive_list = archive_list
            self.route = route
            
    # This function ensures the next chatroom or VN section becomes available
    # Currently they are available in sequence but the program could be modified
    # to make chatrooms available at the correct real-life times
    def next_chatroom():
        global chat_archive, available_calls, current_chatroom, test_ran
        global today_day_num, days_to_expire
        triggered_next = False
        notify_player = False
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
                        # If the chatroom has an unavailable VN after it, make that available and stop
                        if chatroom.played and chatroom.vn_obj and not chatroom.vn_obj.available:
                            chatroom.vn_obj.available = True
                            triggered_next = True
                            break
                        # If they haven't played the VN yet, don't make anything new available and stop
                        if chatroom.played and chatroom.vn_obj and chatroom.vn_obj.available and not chatroom.vn_obj.played:
                            triggered_next = True
                            break              
                        # If the current chatroom isn't available, make it available and stop
                        # Also decrease the time old phone calls are available
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
            # First, check what time it is
            current_time = upTime()
            last_avail = True
            # Now, go through the list of chatrooms and find out if
            # there's a new one to be triggered
            for day_index, archive in enumerate(chat_archive[:days_to_expire]):
                if archive.archive_list:
                    for chat_index, chatroom in enumerate(archive.archive_list):
                        # First, we check if there's a chatroom with a VN after it
                        # If the chatroom has an unavailable VN after it, make that available
                        if chatroom.played and chatroom.vn_obj and not chatroom.vn_obj.available:
                            chatroom.vn_obj.available = True
                        # If this chatroom isn't available, check if it's time to make it available
                        if not chatroom.available:
                            last_avail = False
                            # Check the time on the chatroom
                            if int(current_time.military_hour) < int(chatroom.trigger_time[:2]):
                                # Too early; not time for this chatroom to trigger yet
                                triggered_next = True
                                break
                            elif int(current_time.military_hour) == int(chatroom.trigger_time[:2]):
                                # Hour is the same; check the minutes
                                if int(current_time.minute) < int(chatroom.trigger_time[-2:]):
                                    # Too early; not time for this chatroom to trigger yet
                                    triggered_next = True
                                    break
                                else:
                                    # Time for the chatroom to trigger
                                    # First, check if it's the last chatroom of the day
                                    if chat_index-1 == len(archive.archive_list):
                                        # If so, we increase the number of days to expire
                                        days_to_expire += 1
                                        triggered_next = True
                                    if chat_index == 0 and day_index == 0:
                                        # If this is the first chatroom of the route, there's
                                        # nothing to expire, so we trigger the chatroom
                                        chatroom.available = True
                                        current_chatroom = chatroom
                                        today_day_num = day_index
                                    elif chat_index > 0:
                                        # This is the second or later chatroom of the day
                                        chatroom.available = True
                                        current_chatroom = chatroom
                                        prev_chatroom = archive.archive_list[chat_index - 1]
                                        expire_chatroom(prev_chatroom, current_chatroom)                                           
                                        notify_player = True
                                        today_day_num = day_index
                                        # We don't set triggered_next to True so it makes
                                        # more chatrooms expire if necessary
                                    elif chat_index == 0 and day_index > 0:
                                        # This is the first chatroom of the day but there are
                                        # days before this chatroom with chatrooms that might
                                        # be expired
                                        chatroom.available = True
                                        current_chatroom = chatroom
                                        prev_chatroom = chat_archive[day_index - 1].archive_list[-1]
                                        expire_chatroom(prev_chatroom, current_chatroom)                                          
                                        notify_player = True
                                        today_day_num = day_index
                            elif int(current_time.military_hour) > int(chatroom.trigger_time[:2]):
                                # Current hour is later than the chatroom trigger time
                                # Time to trigger the chatroom
                                # First, check if it's the last chatroom of the day
                                if chat_index+1 == len(archive.archive_list):
                                    # If so, we increase the number of days to expire
                                    days_to_expire += 1
                                    triggered_next = True
                                if chat_index == 0 and day_index == 0:
                                    # If this is the first chatroom of the route, there's
                                    # nothing to expire prior to it, so we trigger the chatroom
                                    chatroom.available = True
                                    current_chatroom = chatroom
                                    today_day_num = day_index
                                elif chat_index > 0:
                                    # This is the second or later chatroom of the day
                                    chatroom.available = True
                                    current_chatroom = chatroom
                                    prev_chatroom = archive.archive_list[chat_index - 1]
                                    expire_chatroom(prev_chatroom, current_chatroom)                                 
                                    notify_player = True
                                    today_day_num = day_index
                                elif chat_index == 0 and day_index > 0:
                                    # This is the first chatroom of the day but there are
                                    # days before this chatroom with chatrooms that might
                                    # be expired
                                    chatroom.available = True
                                    current_chatroom = chatroom
                                    prev_chatroom = chat_archive[day_index - 1].archive_list[-1]
                                    expire_chatroom(prev_chatroom, current_chatroom)                                      
                                    notify_player = True
                                    today_day_num = day_index
                if triggered_next:
                    break
            if last_avail:
                days_to_expire += 1
            if notify_player:
                # Let the player know a new chatroom is open
                the_msg = "[[new chatroom] " + current_chatroom.title
                renpy.music.play('sfx/Ringtones etc/text_basic_1.wav', 'sound')
                renpy.show_screen('confirm', message=the_msg, yes_action=Hide('confirm'))
            
    ## A helper function that expires chatrooms and makes their phonecalls/
    ## text messages available
    def expire_chatroom(prev_chatroom, current_chatroom):
        # The previous chatroom expires if not played
        if not prev_chatroom.played and not prev_chatroom.buyback:
            prev_chatroom.expired = True
            
        # We need to set a time for the missed call; should be
        # equal to the trigger time for the current chatroom
        time_for_call = upTime()
        time_for_call.twelve_hour = current_chatroom.trigger_time[:2]
        if time_for_call.twelve_hour == '00':
            time_for_call.twelve_hour = '12'
            time_for_call.am_pm = 'AM'
        elif int(time_for_call.twelve_hour) > 12:
            time_for_call.twelve_hour = str(12 - int(time_for_call.twelve_hour))
            time_for_call.am_pm = 'PM'
        else:
            time_for_call.am_pm = 'AM'                                    
        time_for_call.minute = current_chatroom.trigger_time[-2:]
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
                
    # A quick function to see how many chatrooms there are left to be played through
    # This is used so emails will always be delivered before the party
    def num_future_chatrooms():
        global chat_archive
        total = 0
        for archive in chat_archive:
            if archive.archive_list:
                for chatroom in archive.archive_list:
                    if not chatroom.played: 
                        total += 1
        return total
                
        
    # Delivers the next available text message and triggers an incoming
    # phone call, if applicable
    def deliver_next():
        global text_queue, incoming_call, available_calls, current_call
        for msg in text_queue:
            if msg.msg_list:
                msg.deliver()
                break             
        if incoming_call:
            current_call = incoming_call
            incoming_call = False
            renpy.call('new_incoming_call', phonecall=current_call)
    
    # This function takes a route (new_route) and merges it with the
    # current route
    def merge_routes(new_route, is_vn=False):
        global chat_archive, current_chatroom
        current_chatroom.plot_branch = False
        for archive in chat_archive:
            for archive2 in new_route:
                if archive2.day == archive.day:
                    # If there is a conditional VN object
                    if is_vn:
                        # replace the old VN obj with the new one
                        archive.archive_list[-1].vn_obj = archive2.archive_list[0].vn_obj
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
                    if chatroom.played and chatroom.plot_branch and (not chatroom.vn_obj or chatroom.vn_obj.played):
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
        global chat_archive, today_day_num, days_to_expire
        current_time = upTime()
        days_to_expire += 1
        # Check chatrooms for the current day
        for chatroom in chat_archive[today_day_num].archive_list:
            # Hour for this chatroom is greater than now; make available
            if int(current_time.military_hour) < int(chatroom.trigger_time[:2]):
                chatroom.available = True
                chatroom.buyback = True
            # Hour is the same; check minute
            elif int(current_time.military_hour) == int(chatroom.trigger_time[:2]):            
                if int(current_time.minute) < int(chatroom.trigger_time[-2:]):
                    # Minute is greater; make available
                    chatroom.available = True
                    chatroom.buyback = True
        # Now check chatrooms for the next day
        if chat_archive[today_day_num+1].archive_list:
            for chatroom in chat_archive[today_day_num+1].archive_list:
                # Hour for this chatroom is smaller than now; make available
                if int(current_time.military_hour) > int(chatroom.trigger_time[:2]):
                    chatroom.available = True
                    chatroom.buyback = True
                # Hour is the same; check minute
                elif int(current_time.military_hour) == int(chatroom.trigger_time[:2]):            
                    if int(current_time.minute) > int(chatroom.trigger_time[-2:]):
                        # Minute is smaller; make available
                        chatroom.available = True
                        chatroom.buyback = True
        # Increase the day number
        today_day_num += 1
                    
                    
        
            
# This archive will store every chatroom in the game. If done correctly,
# the program will automatically set variables and make chatrooms available
# for you
default chat_archive = [Archive('Tutorial', [Chat_History('Example Chatroom', 'auto', 'example_chat', '00:01'),                                     
                                    Chat_History('Inviting Guests', 'auto', 'example_email', '02:11', [z]),
                                    Chat_History('Text Message Example', 'auto', 'example_text', '02:53', [r], VN_Mode('vn_mode_tutorial', r)),
                                    Chat_History('Pass Out After Drinking Caffeine Syndrome', 'auto', 'tutorial_chat', '04:05', [s]),
                                    Chat_History('Invite to the meeting', 'jumin', 'popcorn_chat', '07:07', [ja, ju], VN_Mode('popcorn_vn', ju)),
                                    Chat_History('Plot Branches', 'auto', 'plot_branch_tutorial', '18:44', [], False, True)]),                                    
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
                        
default tutorial_bad_end = [Archive('Tutorial', [Chat_History('An Unfinished Task', 'auto', 'tutorial_bad_end', '13:26', [v])] )]
default tutorial_good_end = [Archive('Tutorial', [ Chat_History('Plot Branches', 'auto', 'plot_branch_tutorial', '10:44', [], VN_Mode('plot_branch_vn')),
                                                   Chat_History('Onwards!', 'auto', 'tutorial_good_end', '13:26', [u], VN_Mode('good_end_party', None, True))] )]
                        
default seven_route = [ Archive('5th', [], 'day_s'),
                        Archive('6th', [], 'day_s'),
                        Archive('7th', [], 'day_s'),
                        Archive('8th', [], 'day_s'),
                        Archive('9th', [], 'day_s'),
                        Archive('10th', [], 'day_s'),
                        Archive('Final', [], 'day_s')]