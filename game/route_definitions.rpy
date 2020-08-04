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
        expired_chat : string
            Label to jump to when this chatroom has expired.
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
        story_calls_list : PhoneCall[]
            List of the labels used for story phone calls that should
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
            elif save_img[:5] == "save_":
                self.save_img = save_img[5:]
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
                self.original_participants = list(participants)
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

        def __deepcopy__(self, memo):
            """
            Return a deepcopy of a ChatHistory object. Maintained for
            compatibility with __getattr__ implementation.
            """

            result = ChatHistory(self.title, self.chatroom_label, 
                self.trigger_time, list(self.participants),
                deepcopy(self.vn_obj, memo), deepcopy(self.plot_branch, memo),
                self.save_img)
            result.played = self.played
            result.participated = self.participated
            result.available = self.available
            result.expired = self.expired
            result.buyback = self.buyback
            result.buyahead = self.buyahead
            result.outgoing_calls_list = self.outgoing_calls_list
            result.incoming_calls_list = self.incoming_calls_list
            result.story_calls_list = copy(self.story_calls_list)
            result.replay_log = []
            return result


        def __getattr__(self, name):
            """
            Ensure compatibility when accessing attributes that don't exist.
            """

            if name == 'story_calls_list':
                return []
                # chatroom_label = self.__dict__['chatroom_label']
                # return [ PhoneCall(x, chatroom_label + '_story_call_'
                #             + x.file_id, avail_timeout='test', story_call=True)
                #         for x in store.all_characters 
                #         if renpy.has_label(chatroom_label + '_story_call_'
                #             + x.file_id)]
                
            try:
                # print("ChatHistory getattr with", name)
                # if name == 'chatroom_label':
                #     raise AttributeError(name)
                # print("with", self.__dict__['chatroom_label'])
                return super(ChatHistory, self).__getattribute__(name)
            except (KeyError, AttributeError) as e:
                raise AttributeError(name)
                
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

            self.participants = list(self.original_participants)

        @property
        def party(self):
            """Retain compatibility with VNMode objects."""

            return False
            
            
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
        title : string
            The title for the VN as it should show up in the History screen.
        plot_branch : PlotBranch or False
            Keeps track of plot branch information if the story should
            branch after this chatroom.
        save_img : string
            A short version of the file path used to display the icon next
            to a save file when this is the active chatroom.
        outgoing_calls_list : string[]
            List of the labels used for phone calls that should follow this
            VN, if it is separate. Also used in the History screen.
        incoming_calls_list : string[]
            List of the labels used for incoming phone calls that should
            occur after this VN. Also used in the History screen.
        story_calls_list : PhoneCall[]
            List of the labels used for story phone calls that should
            occur after this chatroom. Also used in the History screen.
        """

        def __init__(self, vn_label, who=None, party=False, trigger_time=False,
                    title="", plot_branch=False, save_img='auto'):
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
            title : string
                The title for the VN for the History screen.
            plot_branch : PlotBranch or False
                Keeps track of plot branch information if the story should
                branch after this chatroom.
            save_img : string
                A short version of the file path used to display the icon next
                to a save file when this is the active VN.
            """

            self.vn_label = vn_label
            self.who = who
            self.played = False
            self.available = False
            self.party = party
            self.title = title
            if trigger_time:
                # Ensure the trigger time is set up properly
                # It corrects times like 3:45 to 03:45
                if ':' in trigger_time[:2]:
                    self.trigger_time = '0' + trigger_time
                else:
                    self.trigger_time = trigger_time
            else:
                self.trigger_time = trigger_time

            self.plot_branch = plot_branch
            self.save_img = save_img

            if self.trigger_time:
                self.outgoing_calls_list = [ (self.vn_label + '_outgoing_' 
                    + x.file_id) for x in store.all_characters 
                    if renpy.has_label(self.vn_label + '_outgoing_' 
                        + x.file_id)]
                self.incoming_calls_list = [ (self.vn_label + '_incoming_' 
                    + x.file_id) for x in store.all_characters 
                    if renpy.has_label(self.vn_label + '_incoming_' 
                        + x.file_id)]
                temp_story_calls = [ x for x in store.all_characters 
                    if renpy.has_label(self.chatroom_label + '_story_call_'
                        + x.file_id)]
                self.story_calls_list = []

                for char in temp_story_calls:
                    self.story_calls_list.append(PhoneCall(char,
                        self.chatroom_label + '_story_call_' + char.file_id,
                        avail_timeout='test', story_call=True))
                
            else:
                self.outgoing_calls_list = []
                self.incoming_calls_list = []
                self.story_calls_list = []
            

        @property
        def vn_img(self):
            """Return the image used for this VN."""

            if self.who:
                return 'vn_' + self.who.file_id
            else:
                return 'vn_other'
        
        @property
        def vn_obj(self):
            """
            Allow ChatHistory and VNMode objects to be used
            somewhat interchangeably.
            """
            return False

        @property
        def original_participants(self):
            """
            Allow ChatHistory and VNMode objects to be used
            somewhat interchangeably.
            """
            return []

        @property
        def chatroom_label(self):
            """
            Allow ChatHistory and VNMode objects to be used
            somewhat interchangeably.
            """
            return self.vn_label

        @property
        def expired(self):
            """
            Allow ChatHistory and VNMode objects to be used
            somewhat interchangeably.
            """
            return False

        @expired.setter
        def expired(self, other):
            """
            Allow ChatHistory and VNMode objects to be used
            somewhat interchangeably.
            """
            pass

        @property
        def buyback(self):
            """
            Allow ChatHistory and VNMode objects to be used
            somewhat interchangeably.
            """
            return False
        
        @property
        def buyahead(self):
            """
            Allow ChatHistory and VNMode objects to be used
            somewhat interchangeably.
            """
            return False

        @buyahead.setter
        def buyahead(self, other):
            """
            Allow ChatHistory and VNMode objects to be used
            somewhat interchangeably.
            """
            pass

        @property
        def participants(self):
            """
            Allow ChatHistory and VNMode objects to be used
            somewhat interchangeably.
            """
            return []

        def __deepcopy__(self, memo):
            """
            Return a deepcopy of a VNMode object. Maintained for compatibility
            with __getattr__ implementation.
            """

            result = VNMode(self.vn_label, self.who, self.party,
                self.trigger_time, self.title, deepcopy(self.plot_branch, memo),
                self.save_img)
            result.played = self.played
            result.available = self.available
            result.outgoing_calls_list = self.outgoing_calls_list
            result.incoming_calls_list = self.incoming_calls_list
            result.story_calls_list = copy(self.story_calls_list)
            return result
            

        def __getattr__(self, name):
            """
            Ensure compatibility when accessing attributes that don't exist.
            """

            if name == 'title':
                return ""
            elif name == 'plot_branch':
                return False
            elif name == 'save_img':
                return 'auto'
            elif name == 'outgoing_calls_list':
                vn_label = self.__dict__['vn_label']
                return [ (vn_label + '_outgoing_' 
                        + x.file_id) for x in store.all_characters 
                        if renpy.has_label(vn_label + '_outgoing_' 
                            + x.file_id)]
            elif name == 'incoming_calls_list':
                vn_label = self.__dict__['vn_label']
                return [ (vn_label + '_incoming_' 
                        + x.file_id) for x in store.all_characters 
                        if renpy.has_label(vn_label + '_incoming_' 
                            + x.file_id)]
            elif name == 'story_calls_list':
                return []
                # vn_label = self.__dict__['vn_label']
                # return [ PhoneCall(x, vn_label + '_story_call_'
                #             + x.file_id, avail_timeout='test', story_call=True)
                #         for x in store.all_characters 
                #         if renpy.has_label(vn_label + '_story_call_'
                #             + x.file_id)]

            try:
                # print("VNMode getattr with", name)
                # if name == 'vn_label':
                #     raise AttributeError(name)
                # print("with", self.__dict__['vn_label'])
                return super(VNMode, self).__getattribute__(name)
            except (KeyError, AttributeError) as e:                
                raise AttributeError(name)

        def __eq__(self, other):
            """Check for equality between two VNMode objects."""
            if not isinstance(other, VNMode):
                return False
            return (self.vn_label == other.vn_label
                    and self.who == other.who)
        
        def __ne__(self, other):
            """Check for inequality between two VNMode objects."""
            if not isinstance(other, VNMode):
                return True

            return (self.vn_label != other.vn_label
                    or self.who != other.who)

    def SoloVN(title, vn_label, trigger_time, who=None, plot_branch=False,
                party=False, save_img='auto'):
        """Return a VNMode object with the given parameters."""
        
        return VNMode(vn_label, who, party, trigger_time,
                title, plot_branch, save_img)

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
            """For compatibility: convert ChatHistory to ChatRoom."""
            
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
                new_vn = create_dependent_VN(self.branch_vn.vn_label,
                    self.branch_vn.who, self.branch_vn.party)
                self.branch_vn = new_vn               



        @property
        def num_items(self):
            """Return the number of timeline items on this day."""

            return len(self.archive_list)

        @property
        def played_percentage(self):
            """Return the percent of items that have been played."""

            played = 0
            total = self.num_items
            for item in self.archive_list:
                # TODO: could change this to account for played chatrooms
                # with expired story calls
                if item.played and not item.expired:
                    played += 1
            
            if total == 0:
                return 0
            
            return (played * 100) // total
            
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
                    self.ending_chatrooms.append(
                            day.archive_list[-1].get_final_item().item_label)                    
                    break

            for branch in branch_list:
                for day in reversed(branch):
                    if day.archive_list:
                        self.ending_chatrooms.append(
                            day.archive_list[-1].get_final_item().item_label)                                                
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
                        print("Got an item which is", item)
                        if isinstance(item, VNMode):
                            print("It's a VN, label", item.vn_label)

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
                    if not item.all_played():
                        triggered_next = True
                        break
                    
                    # Something associated with this item isn't available
                    # to play yet. Make it available.
                    if not item.all_available():
                        decrease_calls = item.make_next_available()
                        # If this was the "main" item in a chain of timeline
                        # items, it triggers the phone calls to expire
                        if decrease_calls:
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
                # Independent of time, ensure all items associated with
                # this item are available
                if item.played and not item.all_available():
                    item.make_next_available()

                # If this item has a plot branch, don't check anything
                # past it
                if item.plot_branch:
                    if not item.all_available():
                        item.make_next_available()
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
                    item.available = True
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
                    item.available = True
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
            renpy.show_screen('confirm',  message=item.on_available_message(), 
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
            prev_item.expire()
        else:
            # There was no need to expire anything, so return
            return

        # Otherwise, an item was expired. Deliver its associated
        # phone calls and text messages.
        # Create a timestamp for calls.
        call_timestamp = upTime(thehour=cur_item.trigger_time[:2],
                themin=cur_item.trigger_time[-2:])
        deliver_calls(prev_item.item_label, not deliver_calls, call_timestamp)
        
        # Check for a post-item label
        if renpy.has_label('after_' + prev_item.item_label):
            # This will ensure text messages etc are set up
            store.was_expired = True
            renpy.call_in_new_context('after_' + prev_item.item_label)
            store.was_expired = False
        for phonecall in store.available_calls:
            phonecall.decrease_time()

        # Deliver all outstanding text messages
        deliver_all_text()
       
      

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
                        return total
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
        # Figure out which VN to show the player
        # If this route has a branch_vn, extract it and attach it to the
        # current chatroom. It should be on the RouteDay object, which is
        # second in the list ("Bad End", RouteDay(...))
        if len(new_route) > 1 and new_route[1].branch_vn:
            # Add this VN to the day with the plot branch
            most_recent_chat.vn_obj = new_route[1].branch_vn

        plot_branch_party = False
        try:
            if new_route[1].archive_list[0].party:
                plot_branch_party = True
        except:
            print("Couldn't determine if new_route was the party")

        # Find the day the plot branch was on UNLESS this is the party
        # plot branch, in which case we're looking for the party
        a = 0
        found_branch = False
        for archive in chat_archive:
            for chat in archive.archive_list:
                if not plot_branch_party and chat.plot_branch:
                    found_branch = chat
                    break
                elif plot_branch_party and chat.party:
                    found_branch = chat
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
                for chat in day.archive_list:
                    if chat.party and not chat.played:
                        # This is the party to replace
                        print("Found the replacement party")
                        chat = new_route[1].archive_list[0]
                        current_chatroom = chat
                        print("current_chatroom is now", current_chatroom.chatroom_label)
                        return


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
            num_chatrooms = 1
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
        
    

    def next_story_time():
        """Return the time the next timeline item should be available at."""

        global chat_archive
        for archive in chat_archive:
            if archive.archive_list:
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
        for chat_index, chatroom in enumerate(chat_archive[expiry_day-2].archive_list):
            # If this chatroom is already available, don't bother with it
            if chatroom.available and (chatroom.buyahead or chatroom.played):
                continue
            # Otherwise, on this day, everything becomes available
            chatroom.available = True
            chatroom.buyahead = True
            chatroom.expired = False
            if chatroom.vn_obj:
                chatroom.vn_obj.available = True
            if chatroom.plot_branch:                
                # We haven't been able to make everything available in
                # the future, so we return without resetting unlock_24_time
                # or advancing the day
                return
            

        # Now check the next day
        for chat_index, chatroom in enumerate(chat_archive[expiry_day-1].archive_list):
            # Skip already available chatrooms
            if chatroom.available and (chatroom.buyahead or chatroom.played):
                continue
            # Compare the trigger time to the time we're unlocking up to
            if not is_time_later(unlock_time.military_hour, unlock_time.minute,
                    chatroom.trigger_time[:2], chatroom.trigger_time[-2:]):
                # Make this available
                chatroom.available = True
                chatroom.buyahead = True
                chatroom.expired = False
                if chatroom.vn_obj:
                    chatroom.vn_obj.available = True
            else:
                # We're done unlocking things
                unlock_24_time = False
                today_day_num = expiry_day-1
                return
            if chatroom.plot_branch:
                # We haven't been able to make everything available in
                # the future, so we return without resetting unlock_24_time
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
        