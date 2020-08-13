# ######################################################
# This file contains several definitions related to 
# creating routes and plot branches.
# It's organized as follows:
#   python definitions:
#       def TheParty(vn_label, trigger_time, save_img)
#       class PlotBranch
#       class RouteDay
#       class Route
#       def check_and_unlock_story()
#       def past_trigger_time(trig_time, cur_time, was_yesterday,
#             prev_item, cur_item)
#       def expire_item(prev_item, cur_item, deliver_incoming)
#       def num_future_timeline_items(break_for_branch, recursive)
#       def deliver_next()
#       def merge_routes(new_route)
#       def continue_route()
#       def participated_percentage(first_day, last_day)
#       def can_branch()
#       def next_story_time()
#       def make_24h_available()
#       def is_time_later(current_hour, current_min, given_hour, given_min)
#   variable definitions:
#       was_expired
# ######################################################

init -6 python:       

    def TheParty(vn_label, trigger_time=False, save_img='auto'):
        """Return a StoryMode object defined to be the party."""

        return StoryMode(title="The Party", vn_label=vn_label,
            trigger_time=trigger_time, party=True, save_img=save_img)            

    class PlotBranch(renpy.store.object):
        """
        Class that stores information so the program can handle a plot branch.

        Attributes:
        -----------
        vn_after_branch : bool
            True if the VN associated with the chatroom that has this plot
            branch should appear after the plot branch has been proceeded
            through.
        stored_vn : VNMode
            The VN that should appear after the plot branch, if applicable.
        """

        def __init__(self, vn_after_branch=False):
            """
            Create a PlotBranch object to store plot branch information.

            Parameters:
            -----------
            vn_after_branch : bool
                True if the VN associated with the chatroom that has this plot
                branch should appear after the plot branch has been proceeded
                through.
            """

            self.vn_after_branch = vn_after_branch
            self.stored_vn = None
            
    class RouteDay(renpy.store.object):
        """
        Class that stores a day's worth of chatrooms in order to display
        in a timeline for the player.

        Attributes:
        -----------
        day : string
            The name/number of the day as it should show up in the timeline.
            Typically "1st" or "Final". Is followed by the word "Day" in
            the timeline.
        archive_list : ChatHistory[]
            A list of ChatHistory objects that encompasses all the chatrooms
            that should be available on this day.
        branch_vn : VNMode
            If this day has a VN that should be show as soon as soon as it's
            merged onto the main route after a plot branch, it is stored here.
        day_icon : string
            The icon for the route this day is considered a part of. Used to
            display an icon in the day timeline screen.        
        """

        def __init__(self, day, archive_list=None, day_icon='day_common2',
                        branch_vn=None):
            """
            Creates a RouteDay object to hold information on a day's worth
            of chatrooms.

            Parameters:
            -----------
            day : string
                The name/number of the day as it should show up in the timeline.
                Typically "1st" or "Final". Is followed by the word "Day" in
                the timeline.
            archive_list : TimelineItem[]
                A list of TimelineItem objects that encompasses all the
                story items that should be available on this day.
            day_icon : string
                The icon for the route this day is considered a part of. Used
                to display an icon in the day timeline screen.    
            branch_vn : StoryMode
                If this day has a StoryMode that should be shown as soon as
                soon as it's merged onto the main route after a plot branch,
                it is stored here.
            """

            self.day = day
            self.archive_list = archive_list or []
            self.branch_vn = branch_vn

            day_icon = day_icon.lower()
            if day_icon == 'common':
                self.day_icon = 'day_common1'
            elif day_icon  in ['jaehee', 'ja']:
                self.day_icon = 'day_ja'
            elif day_icon in ['jumin', 'ju']:
                self.day_icon = 'day_ju'
            elif day_icon in ['ray', 'r']:
                self.day_icon = 'day_r'
            elif day_icon in ['seven', '707', 's']:
                self.day_icon = 'day_s'
            elif day_icon == 'v':
                self.day_icon = 'day_v'
            elif day_icon in ['yoosung', 'y']:
                self.day_icon = 'day_y'
            elif day_icon in ['zen', 'z']:
                self.day_icon = 'day_z'
            elif day_icon[:4] != "day_":
                self.day_icon = "day_" + day_icon
            else:
                self.day_icon = day_icon

            self.convert_archive(False)            

        def convert_archive(self, copy_everything=True):
            """
            For compatibility: convert ChatHistory to ChatRoom and VNMode
            to StoryMode. If copy_everything is True, it will also copy
            internal fields such as `played` and `available`.
            """
            
            new_archive_list = []

            if (len(self.archive_list) > 0 
                    and isinstance(self.archive_list[0], ChatHistory)):
                for item in self.archive_list:
                    if isinstance(item, ChatHistory):
                        new_archive_list.append(chathistory_to_chatroom(item,
                                                            copy_everything))
                    elif isinstance(item, VNMode):
                        new_archive_list.append(vnmode_to_storymode(item,
                                                            copy_everything))
                    else:
                        new_archive_list.append(item)
                
                self.archive_list = new_archive_list

            # Also ensure the branch_vn is a StoryMode object
            if self.branch_vn and isinstance(self.branch_vn, VNMode):
                new_vn = create_dependent_VN(None, self.branch_vn.vn_label,
                    self.branch_vn.who, self.branch_vn.party)
                self.branch_vn = new_vn               
        
        def participated_percentage(self, only_if_available=False):
            """Return the percent of items that have been participated in."""

            played = 0
            total = 0
            for item in self.archive_list:
                if (isinstance(item, TimelineItem)
                        and ((only_if_available and item.available)
                            or not only_if_available)):
                    add_played, add_total = item.participated_percentage(True)
                    played += add_played
                    total += add_total
            
            if total == 0:
                return 0
            
            return int((played * 100) // total)
            
        @property
        def has_playable(self):
            """Return True if this day has at least one playable item."""
            
            for item in self.archive_list:                
                if isinstance(item, TimelineItem) and item.available:
                    return True
            
            return False

        @property
        def is_today(self):
            """Return True if there are still items to play on this day."""

            for item in self.archive_list:
                if item.available and not item.all_played():
                    return True
                if item.all_played() and item.plot_branch:
                    return True

            return False

        @property
        def all_played(self):
            """Return True if everything on this day has been played."""

            for item in self.archive_list:
                if not item.all_played():
                    return False

            return True

        @property
        def get_branch_item(self):
            """
            Return the item in branch_vn, converting it to StoryMode if
            necessary.
            """

            if not self.branch_vn:
                return False
            # Check if the item needs to be converted
            if isinstance(self.branch_vn, VNMode):
                self.branch_vn = vnmode_to_storymode(self.branch_vn)
            return self.branch_vn
            
       

    class Route(renpy.store.object):
        """
        A class that stores an entire route, including good, bad, normal
        endings etc.

        Attributes:
        -----------
        ending_chatrooms : string[]
            List of the label names for the chatroom or VN that finishes
            each route.
        route_history_title : string
            Name of the route as it should show up in the History screen.
        route : RouteDay[]
            A giant list of RouteDay objects occasionally interspersed with
            strings like "Good End"
        default_branch : RouteDay[]
            A list of RouteDay objects. The first item in the list should
            be a string like "Good End". The 'default' path for the player
            to take; it should be the longest continuous route and is
            typically the route the player will start on until/unless
            they branch onto a different route later.
        """

        def __init__(self, default_branch, branch_list=None, 
                    route_history_title="Common",
                    has_end_title="unset"):
            """
            Creates a Route object to store an entire route.

            Parameters:
            -----------
            default_branch : RouteDay[]
                A list of RouteDay objects. The first item in the list should
                be a string like "Good End". The 'default' path for the player
                to take; it should be the longest continuous route and is
                typically the route the player will start on until/unless
                they branch onto a different route later.
            branch_list : (RouteDay[])[]
                A list of lists of RouteDay objects defined like default_branch
                where the first list item is a string like "Bad End 1". These
                are collections of RouteDay objects the player will proceed
                through if they branch onto this route.
            route_history_title : string
                The title of this route as it should show up in the History 
                screen. " Route" is appended to the end of the given string,
                but to exclude it the argument " -route" can be added e.g.
                route_history_title = "Special Event -route" will show up in
                the History screen as "Special Event".
            has_end_title : bool
                True if this route should have a title over the final chatroom
                such as "Good End". This will be the title provided as the
                first list item in default_branch. Typically this is True
                unless the route has no branching paths.           
            """

            if has_end_title == "unset":
                # This variable will be True if there are branches,
                # and False otherwise.
                if branch_list is not None:
                    has_end_title = True
                else:
                    has_end_title = False

            self.default_branch = default_branch

            if branch_list is None:
                branch_list = []

            # Names of the labels of each ending chatroom or VN
            self.ending_chatrooms = []
            for day in reversed(default_branch):
                if day.archive_list:
                    try:
                        self.ending_chatrooms.append(
                            day.archive_list[-1].get_final_item().item_label)
                    except:
                        print_file(day.archive_list[-1].title, "has no final item?")                                      
                    break

            for branch in branch_list:
                for day in reversed(branch):
                    if day.archive_list:
                        try:
                            self.ending_chatrooms.append(
                                day.archive_list[-1].get_final_item().item_label)
                        except:
                            print_file(day.archive_list[-1].title, "has no final item?")
                        break
                    elif day.branch_vn:
                        self.ending_chatrooms.append(day.branch_vn.item_label)
                        break

            # Add "Route" to the title of the route, unless it ends with
            # " -route" in which case remove that before using it as a title
            if route_history_title[-7:] == " -route":
                self.route_history_title = route_history_title[:-7]
            else:
                self.route_history_title = route_history_title + " Route"
                       
                        
            # Now combine the given branches into one large list        
            self.route = deepcopy(default_branch)
            # Add the branch title before the last item in the
            # default branch
            if has_end_title:
                for r in reversed(self.route):
                    if r.archive_list:
                        r.archive_list.insert(len(r.archive_list)-1, 
                                                        self.route[0])
                        break
            # Get rid of the route title for the default branch
            if not isinstance(self.route[0], RouteDay):
                self.route.pop(0)

            # If the default branch has any "hidden" StoryModes in PlotBranch
            # objects, add them to the route proper
            for day in self.route:
                for item in day.archive_list:
                    if (isinstance(item, TimelineItem)
                            and item.plot_branch 
                            and item.plot_branch.vn_after_branch):
                        item.story_mode = item.plot_branch.stored_vn
                        item.plot_branch = False
                    elif not isinstance(item, TimelineItem):
                        print_file("Got an item which is", item)
                        if isinstance(item, VNMode):
                            print_file("It's a VN, label", item.vn_label)

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

            to_remove = []
            # Finally, get rid of any RouteDays that don't have content
            for item in self.route:
                if (item.archive_list == None
                            or len(item.archive_list) == 0):
                    to_remove.append(item)
                    
            for item in to_remove:
                self.route.remove(item)

            # Add this route to the list of all routes
            if self not in store.all_routes:
                store.all_routes.append(self)
                            
    def check_and_unlock_story():
        """
        Ensure the next timeline item is available to play. By default the 
        program will unlock items sequentially, but if persistent.real_time is 
        True it will unlock items according to their trigger time and the 
        actual time of day.
        """

        global chat_archive, today_day_num, days_to_expire
        global current_game_day

        # If the player is in Testing Mode, make all items available
        triggered_next = False
        if persistent.testing_mode:
            for archive in chat_archive:
                for item in archive.archive_list:
                    item.unlock_all()
                    if item.plot_branch:
                        triggered_next = True
                        break
                if triggered_next:
                    break
            return

        triggered_next = False
        # Next, check if the player is in sequential mode
        if not store.persistent.real_time:
            for archive in chat_archive:
                for item in archive.archive_list:
                    # If the player hasn't played everything associated with
                    # this item, don't make anything new available and stop
                    if item.all_available() and not item.all_played():
                        triggered_next = True
                        break
                    
                    # Something associated with this item isn't available
                    # to play yet. Make it available.
                    if not item.all_available():
                        # Phone calls count down when new items are available
                        item.unlock_all()                                                
                        for phonecall in store.available_calls:
                            phonecall.decrease_time()                            
                        triggered_next = True
                        break
                    
                    # Don't make anything available after a plot branch
                    if item.plot_branch:
                        triggered_next = True
                        break
                if triggered_next:
                    break
            # Done making items available
            return
        
        # If the program isn't in sequential mode, they're in real-time mode.
        # Check if any days have passed since this function was last called.
        date_diff = date.today() - current_game_day
        if date_diff.days > 0:
            # At least one day has passed; increase days_to_expire
            # Its maximum size is the length of the chat_archive.
            days_to_expire = min(date_diff.days + days_to_expire,
                                len(chat_archive))

        # Update the current game date
        current_game_day = date.today()
        # Check what time it is to expire timeline items
        current_time = upTime()

        # Search through every item in the archive to see if there
        # are any to be expired based on the current time of day.
        stop_checking = False
        for day_index, routeday in enumerate(chat_archive[:days_to_expire]):
            for item_index, item in enumerate(routeday.archive_list):
                # If this item has a plot branch, don't check anything
                # past it
                if item.plot_branch:
                    if not item.all_available():
                        item.unlock_all()
                    stop_checking = True
                    break

                if item.available:
                    # The main item is already available; check if anything
                    # later on should be available or should expire.
                    continue

                # Get the timeline item immediately before this one
                if item_index == 0 and day_index == 0:
                    prev_item = False
                    # This is the first item of the route; it should
                    # be available.
                    item.unlock_all()
                    today_day_num = day_index
                    continue                
                elif item_index > 0:
                    prev_item = routeday.archive_list[item_index-1]
                # This is the first item of the day; previous item was the last
                # item on the day before this one
                elif item_index == 0 and day_index > 0:
                    prev_item = chat_archive[day_index-1].archive_list[-1]
                else:
                    prev_item = False
                
                # If the program has gotten this far, this item is not yet
                # available. Should it be made available?
                if (prev_item and past_trigger_time(item.trigger_time,
                        current_time, day_index+1 < days_to_expire, 
                        prev_item, item)):
                    item.unlock_all()
                    today_day_num = day_index
                elif prev_item:
                    # This means this item isn't ready; everything has
                    # been checked.
                    stop_checking = True
                    break
            
            if stop_checking:
                break

        # If by the end of this there is an incoming call, deliver it
        if store.incoming_call:
            store.current_call = store.incoming_call
            store.incoming_call = False
            renpy.call('new_incoming_call', phonecall=store.current_call)
        return
                

    def past_trigger_time(trig_time, cur_time, was_yesterday,
            prev_item, cur_item):
        """
        A helper function for next_timeline_item() which determines if the
        given trigger time is after the current time, and expires the
        previous item if so.

        Parameters:
        -----------
        trig_time : string
            Formatted "00:00" in 24-hour time. The time this item is
            supposed to trigger at.
        cur_time : MyTime
            A MyTime object containing information on the current time.        
        was_yesterday : bool
            True if this item occurred one or more days prior to the
            current date.
        prev_item : TimelineItem
            The item in the timeline before the current one.
        cur_item : TimelineItem
            The current timeline item being checked.

        Returns:
        --------
        bool
            Expire the previous item if the trigger time has already passed
            and return True. Otherwise, return False.
        """

        if was_yesterday:
            # A day or more has passed since this item was supposed to be
            # available. Expire the previous item and move on.
            expire_item(prev_item, cur_item)
            return True
        
        # Otherwise, compare times
        trig_hour = int(trig_time[:2])
        trig_min = int(trig_time[-2:])
        cur_hour = int(cur_time.military_hour)
        cur_min = int(cur_time.minute)

        # If the trigger time is strictly later than the current time,
        # then it isn't time to make it available or expire anything.
        if is_time_later(cur_hour, cur_min, trig_hour, trig_min):
            return False

        if trig_hour < cur_hour:
            expire_item(prev_item, cur_item)
            return True
        
        # Otherwise, special case where the player has a grace period of 1
        # minute to be notified of an item being available if the trigger
        # time just passed
        if (cur_min == trig_min) or (trig_min+1 == cur_min):
            expire_item(prev_item, cur_item, deliver_incoming=True)

            # Let the player know a new item is available
            renpy.music.play('audio/sfx/Ringtones etc/text_basic_1.wav', 
                                'sound')
            renpy.show_screen('confirm',  message=cur_item.on_available_message(), 
                              yes_action=Hide('confirm'))

            return True

        else:
            expire_item(prev_item, cur_item)
            return True

        return False

    def expire_item(prev_item, cur_item, deliver_incoming=False):
        """
        A helper function for next_timeline_item() which expires the
        previous item and makes its phone calls and text messages available.

        Parameters:
        -----------
        prev_item : TimelineItem
            The item that should be expired.
        cur_item : TimelineItem
            The item following the expired item.
        deliver_incoming : bool
            If this item has *just* expired, this should be True and it
            will trigger an incoming call (if available) from prev_item
            rather than expiring it
        """

        # prev_item will expire unless it was played, bought back,
        # or bought ahead
        if prev_item.can_expire():
            prev_item.expire_all()
        else:
            # There was no need to expire anything, so return
            return

        # Otherwise, an item was expired. Deliver its associated
        # phone calls and text messages.
        # Create a timestamp for calls.
        call_timestamp = upTime(thetime=cur_item.trigger_time)
        deliver_calls(prev_item.item_label, not deliver_calls, call_timestamp)
        
        # Check for a post-item label
        # This will ensure text messages etc are set up
        prev_item.call_after_label(True)        
        for phonecall in store.available_calls:
            phonecall.decrease_time()

        # Deliver all outstanding text messages
        deliver_all_texts()
       
      

    def num_future_timeline_items(break_for_branch=False, check_all=True):
        """
        Return how many timeline items remain in the current route.
        Used so emails are always delivered before the party.

        Parameters:
        -----------
        break_for_branch : bool
            True if the program should only list the number of chatrooms
            remaining before a plot branch.
        check_all : bool
            If False, the program counts a TimelineItem as a "unit". If True,
            each individual TimelineItem contained within the parent item is
            also counted.
        """
        
        total = 0
        for archive in store.chat_archive:
            if archive.archive_list:
                for item in archive.archive_list:
                    if check_all:
                        # Count individual items
                        total += item.total_timeline_items(True)
                    elif not item.played:
                        total += 1
                    if item.plot_branch and break_for_branch:
                        return total
        print_file("DEBUG: There are", total, "items remaining")
        return total
                
        
    def deliver_next():
        """
        Deliver the next available text message and trigger an incoming
        phone call, if applicable.
        """

        global incoming_call, available_calls, current_call
        global persistent, all_characters
        
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
                    break                    
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
                    break
                    
        # Deliver the incoming call, if there is one
        if incoming_call:
            current_call = incoming_call
            incoming_call = False
            renpy.call('new_incoming_call', phonecall=current_call)
            
        
    
    def merge_routes(new_route):
        """Merge new_route with the current route."""
        
        global chat_archive, most_recent_chat, current_chatroom

        # May need to update the merged route to TimelineItems    
        for day in new_route:
            if isinstance(day, RouteDay):
                day.convert_archive(False)

        # If the first item of the merged route has a branch_vn, it gets added
        # to the main TimelineItem that contained the branch
        if len(new_route) > 1 and new_route[1].branch_vn:
            most_recent_chat.story_mode = new_route[1].get_branch_item

        plot_branch_party = False
        try:
            # Test if this RouteDay only includes the party            
            if new_route[1].archive_list[0].party:
                plot_branch_party = True
        except:
            print_file("Couldn't determine if new_route was the party")

        # Find the day the plot branch was on UNLESS this is the party
        # plot branch, in which case we're looking for the party
        a = 0
        found_branch = None
        for archive in chat_archive:
            for item in archive.archive_list:
                if not plot_branch_party and item.plot_branch:
                    found_branch = item
                    break
                elif plot_branch_party and item.party:
                    found_branch = item
                    break
            if found_branch:
                break
            a += 1

        # Now get rid of all the chats past the plot branch
        while (chat_archive[a].archive_list 
                and not chat_archive[a].archive_list[-1] == found_branch):
            # Remove the last item from the archive_list if it isn't the
            # plot branch we're dealing with
            chat_archive[a].archive_list.pop()

        if a < len(chat_archive):
            for archive in chat_archive[a+1:]:
                archive.archive_list = []

        # Remove the plot branch indicator
        most_recent_chat.plot_branch = False

        # If this is the party, might need to update the current_chatroom
        # to be the merged party
        if plot_branch_party:
            # Search through chat_archive to find the party we're replacing
            for day in chat_archive:
                for item in day.archive_list:
                    if (isinstance(item, StoryMode)
                            and item.party and not item.played):
                        # This is the party to replace
                        print_file("Found the replacement party")
                        item = new_route[1].archive_list[0]
                        current_chatroom = item
                        print_file("current_chatroom is now", current_chatroom.item_label)
                        return


        # Merge the days on the new route
        for archive in chat_archive:
            for archive2 in new_route[1:]:
                if archive2.day == archive.day:                    
                    archive.archive_list += archive2.archive_list
                    archive.day_icon = archive2.day_icon
                    continue


    def continue_route():
        """Clean up the current route to continue after a plot branch."""

        global most_recent_chat
        
        if (most_recent_chat.plot_branch 
                and most_recent_chat.plot_branch.vn_after_branch):
            # This chat has a stored VN to add to the chat itself
            most_recent_chat.story_mode = most_recent_chat.plot_branch.stored_vn

        # Remove the plot branch indicator
        most_recent_chat.plot_branch = False

    def participated_percentage(first_day=1, last_day=None):
        """
        Return the percentage of story items the player has participated in,
        from first_day to last_day.

        Parameters:
        -----------
        first_day : int
            The first day to check for item completed percentage on. Note
            that the number given here is not the index of the first day. A
            route with "Day 1" through to "Day 4" would provide first_day=1
            to check "Day 1" onwards.
        last_day : int or None
            The last day to check for item completed percentage on. As with
            first_day, it is not the index number. To check all days until the
            end of this route, last_day should be None.

        Returns:
        --------
        int
            A percentage of completed items, rounded down to the nearest
            whole number. If 3/9 items were completed across the given
            days, this function returns 33.
        """

        # For example, if checking participation from Day 2 to
        # Day 4, then first_day = 2 and last_day = 4
        # However, index-wise, those will be from index 1 to 3
        # so subtract 1 from first_day
        first_day -= 1
        if last_day is None:
            last_day = len(store.chat_archive)
            
        total_days = last_day - first_day
        total_percent = 0
                    
        for day in store.chat_archive[first_day:last_day]:
            total_percent += day.participated_percentage(True)
        
        return (total_percent // total_days)
    
              
    def can_branch():
        """Return True if the player can proceed through the plot branch."""

        for archive in store.chat_archive:
            if archive.archive_list:
                for item in archive.archive_list:
                    if not item.all_played():
                        return False
                    if (item.plot_branch and item.all_played()):
                        return True                
        return False
        
    

    def next_story_time():
        """Return the time the next timeline item should be available at."""

        global chat_archive
        for archive in chat_archive:
            for item in archive.archive_list:
                if item.plot_branch and item.available:
                    return 'Plot Branch'
                if not item.available:
                    return item.trigger_time
        return 'Unknown Time'
        
    def make_24h_available():
        """Make the chatrooms for the next 24 hours available."""

        global chat_archive, today_day_num, days_to_expire, unlock_24_time
        
        # Record the time that this function was called at. If this isn't
        # False, then we're trying to continue unlocking chatrooms (usually
        # after a plot branch)
        if not unlock_24_time:
            unlock_time = upTime()
            # First, advance the day
            days_to_expire += 1
            if days_to_expire > len(chat_archive):
                days_to_expire = len(chat_archive)
            expiry_day = days_to_expire
            unlock_24_time = [expiry_day, upTime()]
        else:
            # Trying to continue unlocking; 
            expiry_day = unlock_24_time[0]
            unlock_time = unlock_24_time[1]
        
        # This functions much like the check_and_unlock_story() function, only
        # here instead of expiring chatrooms we make them available
        for i, item in enumerate(chat_archive[expiry_day-2].archive_list):
            # If this item is already available, don't bother with it
            if item.available and (item.buyahead or item.played):
                continue
            # Otherwise, on this day, everything becomes available
            if not item.buy_ahead():
                # We haven't been able to make everything available in
                # the future, so we return without resetting unlock_24_time
                # or advancing the day
                return

        # Now check the next day
        for i, item in enumerate(chat_archive[expiry_day-1].archive_list):
            # Skip already available items
            if item.available and (item.buyahead or item.played):
                continue
            # Compare the trigger time to the time we're unlocking up to
            if not is_time_later(unlock_time.military_hour, unlock_time.minute,
                    item.trigger_time[:2], item.trigger_time[-2:]):
                # Make this available
                if not item.buy_ahead():
                    # We haven't been able to make everything available in
                    # the future, so we return without resetting unlock_24_time
                    today_day_num = expiry_day-1
                    return
            else:
                # We're done unlocking things
                unlock_24_time = False
                today_day_num = expiry_day-1
                return

        # Otherwise, we may have been able to reach the end of the route
        if expiry_day == len(chat_archive):
            today_day_num = expiry_day - 1
            return


    def is_time_later(current_hour, current_min, given_hour, given_min):
        """Return True if the given hour/min is later than the current one."""

        current_hour = int(current_hour)
        current_min = int(current_min)
        given_hour = int(given_hour)
        given_min = int(given_min)

        if given_hour > current_hour:
            return True
        elif given_hour < current_hour:
            return False

        # Check minutes if we've gotten this far; hour is the same
        if given_min > current_min:
            return True
        else:
            return False


                    
# True if the chatroom before the 'after_' call was expired
default was_expired = False
        