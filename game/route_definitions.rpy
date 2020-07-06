##******************************
## USEFUL PYTHON FUNCTIONS
##******************************
init -6 python:

    class ChatHistory(renpy.store.object):
        """
        Class that stores past chatrooms and information needed to display
        them in-game.

        Attributes:
        -----------
        title : string
            Title of the chatroom.
        chatroom_label : string
            Label to jump to to view this chatroom.
        trigger_time : string
            Time this chatroom should be available at, if playing in real-time.
            Formatted as "00:00" in 24-hour time.
        participants : ChatCharacter[]
            List of ChatCharacters who were present over the course of this
            chatroom. Initially set to the characters who begin in the chat.
        original_participants : ChatCharacter[]
            List of characters who begin in the chatroom.
        plot_branch : PlotBranch or False
            Keeps track of plot branch information if the story should
            branch after this chatroom.
        vn_obj : VNMode
            Contains the information for a VN Mode section following this
            chatroom.
        save_img : string
            A short version of the file path used to display the icon next
            to a save file when this is the active chatroom.
        played : bool
            Tracks whether this chatroom has been played.
        participated : bool
            Tracks whether the player participated in this chatroom.
        available : bool
            Tracks whether the program should allow the player to play this
            chatroom or if it should be greyed out/unavailable.
        expired : bool
            Tracks whether this chatroom has expired.
        buyback : bool
            Tracks if the player bought back this chatroom after it expired.
        buyahead : bool
            Tracks if the player bought this chatroom ahead of time so it
            can remain unlocked regardless of the current time.
        replay_log : ReplayEntry[]
            List of ReplayEntry objects that keeps track of how this chatroom
            played out to display to the user during a replay.
        outgoing_calls_list : string[]
            List of the labels used for phone calls that should follow this
            chatroom. Also used in the History screen.
        incoming_calls_list : string[]
            List of the labels used for incoming phone calls that should
            occur after this chatroom. Also used in the History screen.
        """

        def __init__(self, title, chatroom_label, trigger_time, 
                participants=None, vn_obj=False, plot_branch=False, 
                save_img='auto'):
            """
            Creates a ChatHistory object to store information about a
            particular chatroom on a route.

            Parameters:
            -----------
            title : string
                Title of the chatroom.
            chatroom_label : string
                Label to jump to to view this chatroom.
            trigger_time : string
                Time this chatroom should be available at, if playing in
                real-time. Formatted as "00:00" in 24-hour time.
            participants : ChatCharacter[]
                List of ChatCharacters who were present over the course of this
                chatroom. Initially set to the characters who begin in the chat.
            vn_obj : VNMode
                Contains the information for a VN Mode section following this
                chatroom.
            plot_branch : PlotBranch or False
                Keeps track of plot branch information if the story should
                branch after this chatroom.
            save_img : string
                A short version of the file path used to display the icon next
                to a save file when this is the active chatroom.
            """

            self.title = title
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

            self.chatroom_label = chatroom_label
            # Ensure the trigger time is set up properly
            # It corrects times like 3:45 to 03:45
            if ':' in trigger_time[:2]:
                self.trigger_time = '0' + trigger_time
            else:
                self.trigger_time = trigger_time
            self.participants = participants or []
            if len(self.participants) == 0:
                self.original_participants = []
            else:
                self.original_participants = deepcopy(participants)
            self.plot_branch = plot_branch

            # If this chatroom has a VN after it, it goes here
            # Look for a VN with the correct naming system
            self.vn_obj = False
            if vn_obj:
                self.vn_obj = vn_obj
            else:
                # Check for a regular VN, no associated character
                if renpy.has_label(self.chatroom_label + '_vn'):
                    self.vn_obj = VNMode(self.chatroom_label + '_vn')
                # Check for a party label
                elif renpy.has_label(self.chatroom_label + '_party'):
                    self.vn_obj = VNMode(self.chatroom_label + '_party',
                                        party=True)
                else:
                    # Check for a character VN
                    for c in store.all_characters:
                        # VNs are called things like my_label_vn_r
                        vnlabel = self.chatroom_label + '_vn_' + c.file_id
                        if renpy.has_label(vnlabel):
                            # Found the appropriate VN
                            self.vn_obj = VNMode(vnlabel, c)
                            # Should only ever be one VNMode object per chat
                            break
            
            if self.plot_branch and self.plot_branch.vn_after_branch:
                self.plot_branch.stored_vn = self.vn_obj
                self.vn_obj = False
            
            self.played = False
            self.participated = False
            self.available = False
            self.expired = False
            self.expired_chat = chatroom_label + '_expired'
            self.buyback = False
            self.buyahead = False
            self.replay_log = []
            self.outgoing_calls_list = [ (self.chatroom_label + '_outgoing_' 
                + x.file_id) for x in store.all_characters 
                if renpy.has_label(self.chatroom_label + '_outgoing_' 
                    + x.file_id)]
            self.incoming_calls_list = [ (self.chatroom_label + '_incoming_' 
                + x.file_id) for x in store.all_characters 
                if renpy.has_label(self.chatroom_label + '_incoming_' 
                    + x.file_id)]
            
        def __eq__(self, other):
            """Check for equality between two ChatHistory objects."""

            if not isinstance(other, ChatHistory):
                return False
            return (self.title == other.title
                    and self.chatroom_label == other.chatroom_label
                    and self.trigger_time == other.trigger_time)
        
        def __ne__(self, other):
            """Check for inequality between two ChatHistory objects."""

            if not isinstance(other, ChatHistory):
                return True

            return (self.title != other.title
                    or self.chatroom_label != other.chatroom_label
                    or self.trigger_time != other.trigger_time)
                
        def add_participant(self, chara):
            """Add a participant to the chatroom."""

            if not (chara in self.participants):
                print("added", chara.name, "to the participants list of", self.title)        
                self.participants.append(chara)
            return

        def reset_participants(self):
            """
            Reset participants to the original set of participants before
            the user played this chatroom. Used when a player backs out
            of a chatroom.
            """

            self.participants = deepcopy(self.original_participants)
            
            
    class VNMode(renpy.store.object):
        """
        Class that stores the information needed for the Visual Novel portions
        of the game.

        Attributes:
        -----------
        vn_label : string
            The label to jump to for this VN.
        who : ChatCharacter
            The character whose picture is on the VN icon in the timeline.
        played : bool
            True if this VN has been played.
        available : bool
            True if this VN should be available to play.
        party : bool
            True if this VN is the "party".
        trigger_time : string
            Formatted as "00:00" in 24-hour time. The time this VN should
            show up at, if it is not attached to a chatroom.
        """

        def __init__(self, vn_label, who=None, 
                    party=False, trigger_time=False):
            """
            Create a VNMode object to keep track of information for a Visual
            Novel section.

            Parameters:
            -----------
            vn_label : string
                The label to jump to for this VN.
            who : ChatCharacter
                The character whose picture is on the VN icon in the timeline.
            party : bool
                True if this VN is the "party".
            trigger_time : string
                Formatted as "00:00" in 24-hour time. The time this VN should
                show up at, if it is not attached to a chatroom.
            """

            self.vn_label = vn_label
            self.who = who
            self.played = False
            self.available = False
            self.party = party
            # Not currently used; useful for having VN mode
            # sections separate from a chatroom
            self.trigger_time = trigger_time

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
                        branch_vn=False):
            """
            Creates a RouteDay object to hold information on a day's worth
            of chatrooms.

            Parameters:
            -----------
            day : string
                The name/number of the day as it should show up in the timeline.
                Typically "1st" or "Final". Is followed by the word "Day" in
                the timeline.
            archive_list : ChatHistory[]
                A list of ChatHistory objects that encompasses all the chatrooms
                that should be available on this day.
            day_icon : string
                The icon for the route this day is considered a part of. Used to
                display an icon in the day timeline screen.    
            branch_vn : VNMode
                If this day has a VN that should be show as soon as soon as it's
                merged onto the main route after a plot branch, it is stored here.
            """

            self.day = day
            self.archive_list = archive_list or []
            self.branch_vn = branch_vn

            day_icon = day_icon.lower()
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
                    has_end_title=True):
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

            self.default_branch = default_branch

            if branch_list is None:
                branch_list = []

            # Names of the labels of each ending chatroom or VN
            self.ending_chatrooms = []
            for day in reversed(default_branch):
                if day.archive_list:
                    if day.archive_list[-1].vn_obj:
                        self.ending_chatrooms.append(
                            day.archive_list[-1].vn_obj.vn_label)
                    elif (day.archive_list[-1].plot_branch
                            and day.archive_list[
                                -1].plot_branch.vn_after_branch):
                        self.ending_chatrooms.append(day.archive_list[
                            -1].plot_branch.stored_vn.vn_label)
                    else:
                        self.ending_chatrooms.append(
                            day.archive_list[-1].chatroom_label)
                    break

            for branch in branch_list:
                for day in reversed(branch):
                    if day.archive_list:
                        if day.archive_list[-1].vn_obj:
                            self.ending_chatrooms.append(
                                day.archive_list[-1].vn_obj.vn_label)
                        elif (day.archive_list[-1].plot_branch
                                and day.archive_list[
                                    -1].plot_branch.vn_after_branch):
                            self.ending_chatrooms.append(
                                day.archive_list[
                                    -1].plot_branch.stored_vn.vn_label)
                        else:
                            self.ending_chatrooms.append(
                                day.archive_list[-1].chatroom_label)
                        break
                    elif day.branch_vn:
                        self.ending_chatrooms.append(day.branch_vn.vn_label)
                        break


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

            # Add this route to the list of all routes
            if self not in store.all_routes:
                store.all_routes.append(self)
                            
    def next_chatroom():
        """
        Ensure the next chatroom or VN section is available to play.
        By default the program will unlock chatrooms sequentially, but if
        persistent.real_time is True it will unlock chatrooms according to
        their trigger time and the actual time of day.
        """

        global chat_archive, today_day_num, days_to_expire
        global current_game_day

        # If the player is in Testing Mode, make all chatrooms
        # and VNs available regardless
        triggered_next = False
        if persistent.testing_mode:
            for archive in chat_archive:
                for chatroom in archive.archive_list:
                    chatroom.available = True
                    if chatroom.vn_obj:
                        chatroom.vn_obj.available = True
                    if chatroom.plot_branch:
                        triggered_next = True
                        break
                if triggered_next:
                    break
            return

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
    

    def past_trigger_time(trig_time, cur_time, sameday, was_yesterday,
                          prev_chat, cur_chat):
        """
        A helper function for next_chatroom() to determine if the given
        trigger time is after the current time and expires the
        chatroom before this one if so.

        Parameters:
        -----------
        trig_time : string
            Formatted "00:00" in 24-hour time. The time this chatroom was
            supposed to trigger at.
        cur_time : MyTime
            A MyTime object containing information on the current time.
        sameday : bool
            True if the current date is the same day as this chatroom.
        was_yesterday : bool
            True if this chatroom occurred one or more days prior to the
            current date.
        prev_chat : ChatHistory
            The chatroom before this one.
        cur_chat : ChatHistory
            The current chatroom being checked.

        Returns:
        --------
        bool
            Return True if the given trigger time has already passed and
            expire the previous chatroom. Otherwise, return False.
        """

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
            
    def expire_chatroom(prev_chatroom, current_chatroom, 
                                deliver_incoming=False):
        """
        A helper function for next_chatroom() which expires the previous
        chatroom and makes its phone calls and text messages available.

        Parameters:
        -----------
        prev_chatroom : ChatHistory
            The chatroom that should be expired.
        current_chatroom : ChatHistory
            The chatroom following the expired chatroom.
        deliver_incoming : bool
            If this chatroom has *just* expired, this should be True and
            triggers an incoming call from prev_chatroom rather than
            expiring it.
        """

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
            store.was_expired = True
            renpy.call_in_new_context('after_' + prev_chatroom.chatroom_label)
            store.was_expired = False
        for phonecall in available_calls:
            phonecall.decrease_time()
            
        # This delivers all outstanding text messages
        deliver_all_texts()
      

    def num_future_chatrooms(break_for_branch=False):
        """
        Return how many chatrooms remain in the current route. Used so emails
        are always delivered before the party.

        Parameters:
        -----------
        break_for_branch : bool
            True if the program should only list the number of chatrooms
            remaining before a plot branch.
        """
        
        total = 0
        for archive in store.chat_archive:
            if archive.archive_list:
                for chatroom in archive.archive_list:
                    if not chatroom.played: 
                        total += 1
                    if chatroom.plot_branch and break_for_branch:
                        break
        return total
                
        
    def deliver_next():
        """
        Deliver the next available text message and trigger an incoming
        phone call, if applicable.
        """

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



    def continue_route():
        """Clean up the current route to continue after a plot branch."""

        global most_recent_chat
        if (most_recent_chat.plot_branch 
                and most_recent_chat.plot_branch.vn_after_branch):
            # This chat has a stored VN to add to the chat itself
            most_recent_chat.vn_obj = most_recent_chat.plot_branch.stored_vn

        # Remove the plot branch indicator
        most_recent_chat.plot_branch = False

    def participated_percentage(first_day=1, last_day=None):
        """
        Return the percentage of chatrooms the player has participated in,
        from first_day to last_day.

        Parameters:
        -----------
        first_day : int
            The first day to check for chatroom completed percentage on. Note
            that the number given here is not the index of the first day. A
            route with "Day 1" through to "Day 4" would provide first_day=1
            to check "Day 1" onwards.
        last_day : int or None
            The last day to check for chatroom completed percentage on. As with
            first_day, it is not the index number. To check all days until the
            end of this route, last_day should be None.

        Returns:
        --------
        int
            A percentage of completed chatrooms, rounded down to the nearest
            whole number. If 3/9 chatrooms were completed across the given
            days, this function returns 33.
        """

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
    
              
    def can_branch():
        """Return True if the player can proceed through the plot branch."""

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
        
    def next_chat_time():
        """Return the time the next chatroom should be available at."""

        global chat_archive
        for archive in chat_archive:
            if archive.archive_list:
                for chatroom in archive.archive_list:
                    if chatroom.plot_branch and chatroom.available:
                        return 'Plot Branch'
                    if not chatroom.available:
                        return chatroom.trigger_time
        return 'Unknown Time'
        
    def chat_24_available(reset_24=True):
        """Make the chatrooms for the next 24 hours available."""

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
                    
# True if the chatroom before the 'after_' call was expired
default was_expired = False
        