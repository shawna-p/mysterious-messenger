##******************************
## USEFUL PYTHON FUNCTIONS
##******************************
init -6 python:

    ## This class stores past chatrooms that you've visited
    ## A more complete explanation of how to use it to set up 
    ## chatrooms can be found in the accompanying Script Generator
    ## spreadsheet
    class ChatHistory(renpy.store.object):
        def __init__(self, title, chatroom_label, trigger_time, 
                participants=[], vn_obj=False, plot_branch=False, 
                save_img='auto'):
            # Title of the chatroom
            self.title = title
            # Image to use on the save screen after this chatroom
            save_img = save_img.lower()
            if save_img == 'jaehee' or save_img == 'ja':
                self.save_img = 'jaehee'
            elif save_img == 'jumin' or save_img == 'ju':
                self.save_img = 'jumin'
            elif save_img == 'ray' or save_img == 'r':
                self.save_img = 'ray'
            elif save_img == 'seven' or save_img == '707' or save_img == 's':
                self.save_img = 'seven'
            elif save_img == 'v':
                self.save_img = 'v'
            elif save_img == 'yoosung' or save_img == 'y':
                self.save_img = 'yoosung'
            elif save_img == 'zen' or save_img == 'z':
                self.save_img = 'zen'
            else:
                # e.g. auto / another / april / casual
                #      deep / xmas
                self.save_img = save_img

            # Label to jump to for the chatroom
            self.chatroom_label = chatroom_label
            # Ensure the trigger time is set up properly
            # It corrects times like 3:45 to 03:45
            if ':' in trigger_time[:2]:
                self.trigger_time = '0' + trigger_time
            else:
                self.trigger_time = trigger_time
            # People already present in the chatroom before
            # it begins. Updates when new people enter
            self.participants = participants
            self.original_participants = deepcopy(participants)
            # Tracks whether there's a plot branch after this chatroom
            self.plot_branch = plot_branch

            # If this chatroom has a VN after it, it goes here
            # Look for a VN with the correct naming system
            self.vn_obj = False
            if vn_obj:
                self.vn_obj = vn_obj
                print("Got a vn obj,", vn_obj)
            else:
                # Check for a regular VN, no associated character
                if renpy.has_label(self.chatroom_label + '_vn'):
                    print ("Has label", self.chatroom_label + '_vn')
                    self.vn_obj = VNMode(self.chatroom_label + '_vn')
                # Check for a party label
                elif renpy.has_label(self.chatroom_label + '_party'):
                    print ("Has label", self.chatroom_label + '_party')
                    self.vn_obj = VNMode(self.chatroom_label + '_party',
                                        party=True)
                else:
                    # Check for a character VN
                    for c in store.all_characters:
                        # VNs are called things like my_label_vn_r
                        vnlabel = self.chatroom_label + '_vn_' + c.file_id
                        print('Checking for label', vnlabel)
                        if renpy.has_label(vnlabel):
                            # Found the appropriate VN
                            print("Found a match,", vnlabel, "exists")
                            self.vn_obj = VNMode(vnlabel, c)
            
            if self.plot_branch and self.plot_branch.vn_after_branch:
                self.plot_branch.stored_vn = self.vn_obj
                self.vn_obj = False
            
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
            # Tracks if the player bought back this chatroom after it
            # expired
            self.buyback = False
            # Tracks if the player bought this chatroom ahead of time
            # so it can remain unlocked regardless of the current time
            self.buyahead = False
            # Used for replays; this list keeps track of how the chatroom
            # played out when the player went through this chatroom
            self.replay_log = []
            # Saves incoming and outgoing calls for this chatroom
            # Most helpful for history/replay purposes
            self.outgoing_calls_list = [ (self.chatroom_label + '_outgoing_' 
                + x.file_id) for x in store.all_characters 
                if renpy.has_label(self.chatroom_label + '_outgoing_' 
                    + x.file_id)]
            self.incoming_calls_list = [ (self.chatroom_label + '_incoming_' 
                + x.file_id) for x in store.all_characters 
                if renpy.has_label(self.chatroom_label + '_incoming_' 
                    + x.file_id)]
            
        ## These two functions check for equality between two
        ## ChatHistory objects
        def __eq__(self, other):
            if not isinstance(other, ChatHistory):
                return False
            return (self.title == other.title
                    and self.chatroom_label == other.chatroom_label
                    and self.trigger_time == other.trigger_time)
        
        def __ne__(self, other):
            if not isinstance(other, ChatHistory):
                return True

            return (self.title != other.title
                    or self.chatroom_label != other.chatroom_label
                    or self.trigger_time != other.trigger_time)
                
        ## Adds a participant to the chatroom
        def add_participant(self, chara):
            if not chara in self.participants:
                print("added", chara.name, "to the participants list of", self.title)        
                self.participants.append(chara)
                
        ## Resets participants to whatever they were before the
        ## user played this chatroom (used when a player
        ## backs out of a chatroom, for example)
        def reset_participants(self):
            self.participants = deepcopy(self.original_participants)
            
            
    ## This class stores the information needed for the Visual 
    ## Novel portions of the game
    class VNMode(renpy.store.object):
        def __init__(self, vn_label, who=None, 
                    party=False, trigger_time=False):
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
            # Not currently used; useful for having VN mode
            # sections separate from a chatroom
            self.trigger_time = trigger_time

    ## This class stores information the game needs to know
    ## about how to handle a plot branch
    class PlotBranch(renpy.store.object):
        def __init__(self, vn_after_branch=False):
            # Whether this VN should appear after the plot branch
            # or before
            self.vn_after_branch = vn_after_branch
            # If the VN is supposed to appear after the plot branch,
            # store it here until it's time to branch
            self.stored_vn = None
            
    ## This object stores a day's worth of chatrooms
    class RouteDay(renpy.store.object):
        def __init__(self, day, archive_list=[], day_icon='day_common2',
                        branch_vn=False):
            # The day e.g. "1st"
            self.day = day
            # A list of chatrooms taking place on this day
            self.archive_list = archive_list
            # Whether this day has a VN that should be shown as soon
            # as it's merged with the main route
            self.branch_vn = branch_vn

            # The route this day is considered a part of
            day_icon = day_icon.lower()
            # Sets the image used on the Day timeline as well as
            # the name of the route how it should appear in the 
            # History screen
            if day_icon == 'common':
                self.day_icon = 'day_common1'
            elif day_icon == 'jaehee' or day_icon == 'ja':
                self.day_icon = 'day_ja'
            elif day_icon == 'jumin' or day_icon == 'ju':
                self.day_icon = 'day_ju'
            elif day_icon == 'ray' or day_icon == 'r':
                self.day_icon = 'day_r'
            elif (day_icon == 'seven' or day_icon == '707' 
                    or day_icon == 's'):
                self.day_icon = 'day_s'
            elif day_icon == 'v':
                self.day_icon = 'day_v'
            elif day_icon == 'yoosung' or day_icon == 'y':
                self.day_icon = 'day_y'
            elif day_icon == 'zen' or day_icon == 'z':
                self.day_icon = 'day_z'
            else:
                self.day_icon = 'day_common2'

    ## This class stores an entire route -- including good, bad,
    ## normal ends etc
    class Route(renpy.store.object):
        def __init__(self, default_branch, branch_list=[], 
                    route_history_title="Common",
                    has_good_end=True):
            

            self.route_history_title = route_history_title

            # Now combine the given branches into one large list        
            self.route = deepcopy(default_branch)
            # Add the branch title before the last item in the
            # default branch
            if has_good_end:
                for r in reversed(self.route):
                    if r.archive_list:
                        r.archive_list.insert(len(r.archive_list)-1, 
                                                        self.route[0])
                        break
            # Get rid of the route title for the default branch
            if not isinstance(self.route[0], RouteDay):
                self.route.pop(0)

            # If the default branch has any "hidden" VNs in PlotBranch
            # objects, add them to the route proper
            for day in self.route:
                for chat in day.archive_list:
                    if ((isinstance(chat, ChatHistory) or 
                            isinstance(chat, store.ChatHistory))
                            and chat.plot_branch
                            and chat.plot_branch.vn_after_branch):
                        chat.vn_obj = chat.plot_branch.stored_vn
                        chat.plot_branch = False

            if branch_list:
                # First find the day in default_branch which aligns
                # with the days to add from each branch in branch_list
                for branch in branch_list:
                    for b in branch[1:]:
                        for d in self.route:
                            # Both d and b should be a RouteDay object
                            if d.day == b.day:
                                # Append this branch to the bottom of
                                # the route, plus the title
                                d.archive_list.append(branch[0])
                                # If the day doesn't have an archive list,
                                # it should have a branch_vn
                                if b.branch_vn:
                                    d.archive_list.append(b.branch_vn)
                                if b.archive_list:
                                    d.archive_list.extend(b.archive_list)
                                # If a match was found, stop looking
                                # through the rest of the RouteDays
                                # (Since "1st" and "1st" won't match any
                                # other days)
                                break
                            
    ## This function ensures the next chatroom or VN section 
    ## becomes available. By default it unlocks chatrooms in 
    ## sequence, but when persistent.real_time is active it 
    ## unlocks chatrooms according to real-time
    def next_chatroom():
        global chat_archive, today_day_num, days_to_expire
        global current_game_day

        triggered_next = False
        # Running on sequential mode
        if not persistent.real_time:
            for archive in chat_archive:
                if archive.archive_list:
                    for chatroom in archive.archive_list:
                        # If they haven't played the currently
                        # available chatroom, don't make anything new
                        # available and stop
                        if chatroom.available and not chatroom.played:
                            triggered_next = True
                            break
                        # If the currently available chatroom is a plot branch
                        # without a VN, don't make anything new available
                        if (chatroom.available and not chatroom.vn_obj
                                and chatroom.plot_branch):
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
                        
                        # If it's a plot branch with a played VN, don't
                        # make anything new available and stop
                        if (chatroom.played and chatroom.vn_obj
                                and chatroom.plot_branch
                                and chatroom.vn_obj.played):
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
            # Done making chatrooms available
            return

        # Otherwise, the game is running in real-time
        # Check if any days have passed since this function was 
        # last called
        date_diff = date.today() - current_game_day
        if date_diff.days > 0:
            # At least one day has passed; increase days_to_expire
            days_to_expire += date_diff.days
        # Ensure the # of days to expire doesn't exceed the 
        # number of days in the route
        if days_to_expire > len(chat_archive):
            expiry_day = len(chat_archive)
        else:
            expiry_day = days_to_expire
        # Update the current game date
        current_game_day= date.today()
        # Check what time it is to expire chatrooms
        current_time = upTime()
        # Systemically look through every chatroom in the archive
        # to see if there are any to be expired
        stop_checking = False
        for day_index, routeday in enumerate(chat_archive[:expiry_day]):
            # Make sure this routeday actually has an archive list,
            # otherwise check other routedays
            if not routeday.archive_list:
                continue
            # Otherwise it's safe to assume this routeday has chatrooms
            for chat_index, chatroom in enumerate(routeday.archive_list):
                # Independent of time, check if there is a
                # played chatroom with an unavailable VN
                if (chatroom.played and chatroom.vn_obj
                        and not chatroom.vn_obj.available):
                    chatroom.vn_obj.available = True

                # Also, check if the previous chatroom was a plot branch
                # If so, stop checking chatrooms until the player has
                # proceeded through it
                if (chatroom.plot_branch and chatroom.available
                        and (not chatroom.vn_obj
                            or chatroom.vn_obj.available)):
                    stop_checking = True
                    break

                if (chat_index != 0 and len(routeday.archive_list) > 1
                        and routeday.archive_list[chat_index-1].plot_branch
                        and routeday.archive_list[chat_index-1].available
                        and (not routeday.archive_list[chat_index-1].vn_obj
                            or routeday.archive_list[chat_index
                                                -1].vn_obj.available)):
                    stop_checking = True
                    break

                # If the program has gotten this far and the current
                # chatroom is available, keep looking for unavailable 
                # chatrooms to trigger
                if chatroom.available:
                    continue
                
                if chat_index > 0:
                    prev_chatroom = routeday.archive_list[chat_index-1]
                elif chat_index == 0 and day_index == 0:
                    prev_chatroom = False
                    # First chatroom of the route; should just
                    # make this available
                    chatroom.available = True
                    today_day_num = day_index
                    continue
                elif chat_index == 0 and day_index > 0:
                    prev_chatroom = routeday[day_index-1].archive_list[-1]

                else:
                    prev_chatroom = False
                # Otherwise, this chatroom is not available. Should
                # it be made available?
                if (prev_chatroom and past_trigger_time(chatroom.trigger_time, 
                        current_time, day_index+1 == expiry_day,
                        day_index+1 < expiry_day,
                        prev_chatroom, chatroom)):
                    chatroom.available = True
                    today_day_num = day_index
                elif prev_chatroom:
                    # That means this chatroom isn't ready; break
                    stop_checking = True
                    break

            if stop_checking:
                break
        # If by the end of this there is an incoming call, deliver it
        if store.incoming_call:
            store.current_call = store.incoming_call
            store.incoming_call = False
            renpy.call('new_incoming_call', phonecall=store.current_call)
    
    ## A helper function which returns True if the given
    ## trigger time has passed/is later than the current time
    ## and expires the chatroom before this one if so
    def past_trigger_time(trig_time, cur_time, sameday, was_yesterday,
                          prev_chat, cur_chat):

        if was_yesterday:
            # It's already a day or more past this chat; expire 
            # the previous chatroom and move on
            expire_chatroom(prev_chat, cur_chat)
            return True

        trig_hour = int(trig_time[:2])
        trig_min = int(trig_time[-2:])
        cur_hour = int(cur_time.military_hour)
        cur_min = int(cur_time.minute)

        # First, check the hours
        if trig_hour < cur_hour:
            expire_chatroom(prev_chat, cur_chat)
            return True
        elif trig_hour > cur_hour:
            # Too early
            return False
        # Check minutes; if the minutes are close enough,
        # check if the program should notify the user
        if trig_min > cur_min:
            return False

        # Player has a grace period of 1 minute to be informed
        # of new chatrooms if the trigger time just passed
        if sameday and (cur_min == trig_min or trig_min+1 == cur_min):
            expire_chatroom(prev_chat, cur_chat, deliver_incoming=True)
            # Let the player know a new chatroom is open
            the_msg = "[[new chatroom] " + current_chatroom.title
            renpy.music.play('audio/sfx/Ringtones etc/text_basic_1.wav', 
                                'sound')
            renpy.show_screen('confirm',  message=the_msg, 
                              yes_action=Hide('confirm'))
            return True
        
        if trig_min < cur_min:
            expire_chatroom(prev_chat, cur_chat)
            return True
        return False
            
    ## A helper function that expires a chatroom and makes its phonecalls/
    ## text messages available
    def expire_chatroom(prev_chatroom, current_chatroom, 
                                deliver_incoming=False):
        # The previous chatroom expires if not played,
        # bought back, or bought ahead
        if (not prev_chatroom.played
                and not prev_chatroom.buyback 
                and not prev_chatroom.buyahead):
            prev_chatroom.expired = True
        else:
            return
            
        # Set a time for the missed call; should be
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
        
        # There's a rare case where the program should trigger an 
        # incoming call because this chatroom has *just* expired
        if deliver_incoming:
            deliver_calls(prev_chatroom.chatroom_label, False, time_for_call)
        else:
            deliver_calls(prev_chatroom.chatroom_label, True, time_for_call) 
        
        # Checks for a post-chatroom label
        if renpy.has_label('after_' + prev_chatroom.chatroom_label): 
            # This will ensure text messages etc are set up
            renpy.call_in_new_context('after_' + prev_chatroom.chatroom_label)

        for phonecall in available_calls:
            phonecall.decrease_time()
            
        # This delivers all outstanding text messages
        deliver_all_texts()
      

    ## A quick function to see how many chatrooms there are left 
    ## to be played through
    ## This is used so emails will always be delivered before the party
    def num_future_chatrooms(break_for_branch=False):
        global chat_archive
        total = 0
        for archive in chat_archive:
            if archive.archive_list:
                for chatroom in archive.archive_list:
                    if not chatroom.played: 
                        total += 1
                    if chatroom.plot_branch and break_for_branch:
                        break
        return total
                
        
    ## Delivers the next available text message and triggers an incoming
    ## phone call, if applicable
    def deliver_next():
        global incoming_call, available_calls, current_call
        global persistent, text_person, all_characters
        
        delivered_text = False

        if renpy.random.randint(0, 1):
            for c in all_characters:
                if (c.text_msg.msg_queue 
                        and not c.real_time_text and not delivered_text):
                    c.text_msg.deliver()
                    delivered_text = True
                # Real-time texts notify the player differently
                elif (c.real_time_text and not c.text_msg.read 
                        and not c.text_msg.notified):
                    c.text_msg.notified = True
                    renpy.music.play(persistent.text_tone, 'sound')
                    popup_screen = allocate_text_popup()
                    renpy.show_screen(popup_screen, c=c) 
                    
        else:
            for c in reversed(all_characters):
                if (c.text_msg.msg_queue 
                        and not c.real_time_text and not delivered_text):
                    c.text_msg.deliver()
                    delivered_text = True
                # Real-time texts notify the player differently
                elif (c.real_time_text and not c.text_msg.read 
                        and not c.text_msg.notified):
                    c.text_msg.notified = True
                    renpy.music.play(persistent.text_tone, 'sound')
                    popup_screen = allocate_text_popup()
                    renpy.show_screen(popup_screen, c=c) 
                    
        # Deliver the incoming call, if there is one
        if incoming_call:
            current_call = incoming_call
            incoming_call = False
            renpy.call('new_incoming_call', phonecall=current_call)
            
        
    
    ## This function takes a route (new_route) and merges it with the
    ## current route
    def merge_routes(new_route):
        global chat_archive, most_recent_chat
        # Figure out which VN to show the player
        # Check if the new route's first item is a VN -- if so, it overrides
        # the VN stored in the PlotBranch object
        if len(new_route) > 1 and new_route[1].branch_vn:
            # Add this VN to the day with the plot branch
            most_recent_chat.vn_obj = new_route[1].branch_vn

        # Find the day the plot branch was on
        a = 0
        found_branch = False
        for archive in chat_archive:
            for chat in archive.archive_list:
                if chat.plot_branch:
                    found_branch = True
                    break
            if found_branch:
                break
            a += 1

        # Now get rid of all the chats past the plot branch
        while (chat_archive[a].archive_list 
                and not chat_archive[a].archive_list[-1].plot_branch):
            chat_archive[a].archive_list.pop()

        if a < len(chat_archive):
            for archive in chat_archive[a+1:]:
                archive.archive_list = []

        # Remove the plot branch indicator
        most_recent_chat.plot_branch = False

        # Merge the days on the new route
        for archive in chat_archive:
            for archive2 in new_route[1:]:
                if archive2.day == archive.day:                    
                    archive.archive_list += archive2.archive_list
                    archive.day_icon = archive2.day_icon



    ## This function tells the program to continue on with the
    ## regular route after the plot branch
    def continue_route():
        global most_recent_chat
        if (most_recent_chat.plot_branch 
                and most_recent_chat.plot_branch.vn_after_branch):
            # This chat has a stored VN to add to the chat itself
            most_recent_chat.vn_obj = most_recent_chat.plot_branch.stored_vn

        # Remove the plot branch indicator
        most_recent_chat.plot_branch = False

    ## This function returns the percentage of chatrooms the player
    ## has participated in, from first_day to last_day (or from first_day
    ## until the end of the route, if last_day=None)
    def participated_percentage(first_day=1, last_day=None):
        global chat_archive
        # For example, if checking participation from Day 2 to
        # Day 4, then first_day = 2 and last_day = 4
        # However, index-wise, those will be from index 1 to 3
        # so subtract 1 from first_day
        first_day -= 1
        if last_day is None:
            last_day = len(chat_archive)
            
        completed_chatrooms = 0
        num_chatrooms = 0
            
        for archive in chat_archive[first_day:last_day]:
            if archive.archive_list:
                for chatroom in archive.archive_list:
                    if chatroom.available:
                        num_chatrooms += 1
                    if chatroom.available and chatroom.participated:
                        completed_chatrooms += 1
        # Be sure not to divide by zero
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
                    if chatroom.plot_branch and chatroom.available:
                        return 'Plot Branch'
                    if not chatroom.available:
                        return chatroom.trigger_time
        return 'Unknown Time'
        
    ## Makes the chatrooms for the next 24 hours available
    def chat_24_available(reset_24=True):
        global chat_archive, today_day_num, days_to_expire, unlock_24_time
        current_time = upTime()
        if reset_24:
            unlock_24_time = current_time
            days_to_expire += 1
        # Check chatrooms for the current day
        for chatroom in chat_archive[today_day_num].archive_list:
            # Hour for this chatroom is greater than now; make available
            if (int(current_time.military_hour) 
                    < int(chatroom.trigger_time[:2])):
                chatroom.available = True
                chatroom.buyahead = True
                if chatroom.plot_branch:
                    if reset_24:
                        today_day_num += 1
                    return
                    
            # Hour is the same; check minute
            elif (int(current_time.military_hour) 
                    == int(chatroom.trigger_time[:2])):            
                if int(current_time.minute) < int(chatroom.trigger_time[-2:]):
                    # Minute is greater; make available
                    chatroom.available = True
                    chatroom.buyahead = True
                    if chatroom.plot_branch:
                        if reset_24:
                            today_day_num += 1
                        return
        # Now check chatrooms for the next day
        if chat_archive[today_day_num+1].archive_list:
            for chatroom in chat_archive[today_day_num+1].archive_list:
                # Hour for this chatroom is smaller than now; make available
                if (int(current_time.military_hour) 
                        > int(chatroom.trigger_time[:2])):
                    chatroom.available = True
                    chatroom.buyahead = True
                    if chatroom.plot_branch:
                        if reset_24:
                            today_day_num += 1
                        return
                # Hour is the same; check minute
                elif (int(current_time.military_hour) 
                        == int(chatroom.trigger_time[:2])):            
                    if (int(current_time.minute) 
                            > int(chatroom.trigger_time[-2:])):
                        # Minute is smaller; make available
                        chatroom.available = True
                        chatroom.buyahead = True
                        if chatroom.plot_branch:
                            if reset_24:
                                today_day_num += 1
                            return
        # Increase the day number
        if reset_24:
            today_day_num += 1
        # If the program was able to make everything available,
        # unlock_24_time can be reset
        unlock_24_time = False 
                    
                    
    
        