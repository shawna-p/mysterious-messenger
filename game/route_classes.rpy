init -6 python:

    class TimelineItem(renpy.store.object):
        """
        Parent class which holds information needed to display items on
        the timeline e.g. chatrooms, story mode, phone calls.

        Attributes:
        -----------
        title : string
            Title of this item.
        item_label : string
            Label to jump to to view this item.
        expired_label : string
            Label to jump to when this item has expired.
        trigger_time : string
            Time this item should be available at, if playing in real-time
            mode. Formatted as "00:00" in 24-hour time.
        plot_branch : PlotBranch
            Keeps track of plot branch information if the story should
            branch after this item.
        save_img : string
            A short version of the file path used to display the icon next
            to a save file when this is the active timeline item.
        played : bool
            True if this item has been played.
        available : bool
            True if this item should be available in the timeline.
        expired : bool
            True if this item has expired in the timeline.
        buyback : bool
            True if the player bought this item back after it expired.
        buyahead : bool
            True if the player bought this item ahead of time so it can
            remain unlocked regardless of the current time.
        outgoing_calls_list : string[]
            List of the labels used for phone calls that should follow this
            timeline item. Also used in the History screen.
        incoming_calls_list : string[]
            List of the labels used for incoming phone calls that should
            occur afterr this item. Also used in the History screen.
        story_calls_list : PhoneCall[]
            List of the labels used for mandatory story phone calls that should
            occur after this item. Also used in the History screen.
        """

        def __init__(self, title, item_label, trigger_time, plot_branch="None",
            save_img='auto'):
            """
            Create a generic TimelineItem object.

            Parameters:
            -----------
            title : string
                Title of this item.
            item_label : string
                Label to jump to to view this item.
            trigger_time : string
                Time this item should be available at, if playing in real-time
                mode. Formatted as "00:00" in 24-hour time.
            plot_branch : PlotBranch
                Keeps track of plot branch information if the story should
                branch after this item.
            save_img : string
                A short version of the file path used to display the icon next
                to a save file when this is the active timeline item.
            """

            self.title = title
            self.item_label = item_label

            if plot_branch == "None":
                # There is no plot branch
                self.plot_branch = None
            elif isinstance(plot_branch, PlotBranch):
                self.plot_branch = plot_branch
            elif plot_branch:
                # plot branch should have vn_after_branch=True
                self.plot_branch = PlotBranch(True)
            else:
                self.plot_branch = PlotBranch(False)

            # Ensure the trigger time is set up properly
            # It corrects times like 3:45 to 03:45
            if trigger_time and ':' in trigger_time[:2]:
                self.trigger_time = '0' + trigger_time
            else:
                self.trigger_time = trigger_time
            
            save_img = save_img.lower()
            if save_img in ['jaehee', 'ja']:
                self.save_img = 'jaehee'
            elif save_img in ['jumin', 'ju']:
                self.save_img = 'jumin'
            elif save_img in ['ray', 'r']:
                self.save_img = 'ray'
            elif save_img in ['seven', '707', 's']:
                self.save_img = 'seven'
            elif save_img == 'v':
                self.save_img = 'v'
            elif save_img in ['yoosung', 'y']:
                self.save_img = 'yoosung'
            elif save_img in ['zen', 'z']:
                self.save_img = 'zen'
            elif save_img[:5] == "save_":
                self.save_img = save_img[5:]
            else:
                # e.g. auto / another / april / casual / deep / xmas
                self.save_img = save_img

            self.expired_label = item_label + "_expired"
            self.played = False
            self.available = False
            self.expired = False
            self.buyback = False
            self.buyahead = False

            self.outgoing_calls_list = [ (self.item_label + '_outgoing_' 
                + x.file_id) for x in store.all_characters 
                if renpy.has_label(self.item_label + '_outgoing_' 
                    + x.file_id)]
            self.incoming_calls_list = [ (self.item_label + '_incoming_' 
                + x.file_id) for x in store.all_characters 
                if renpy.has_label(self.item_label + '_incoming_' 
                    + x.file_id)]

            self.story_calls_list = [
                    create_dependent_storycall(x, 
                    self.item_label + '_story_call_' + x.file_id)
                for x in store.all_characters 
                    if renpy.has_label(self.item_label + '_story_call_'
                        + x.file_id)]
        
        def unlock_all(self):
            """Make all items associated with this TimelineItem available."""

            self.available = True
            if len(self.story_calls_list) > 0:
                for phonecall in self.story_calls_list:
                    phonecall.available = True

        def all_available(self):
            """
            Return True if everything associated with this item is available.
            """

            if not self.available:
                return False
            if len(self.story_calls_list) > 0:
                for phonecall in self.story_calls_list:
                    if not phonecall.available:
                        return False
            return True

        def all_played(self):
            """
            Return True if everything associated with this item has been
            played.
            """

            if not self.played:
                return False
            if len(self.story_calls_list) > 0:
                for phonecall in self.story_calls_list:
                    if not phonecall.played:
                        return False
            return True

        def make_next_available(self):
            """
            Make the next unavailable item associated with this item
            available to play.
            """

            if not self.available:
                self.available = True
                return True
            # Subsequent items are only available if previous ones were played
            if not self.played:
                return
            
            if len(self.story_calls_list) > 0:
                for phonecall in self.story_calls_list:
                    # Subsequent items are only available if previous
                    # ones were played
                    if phonecall.available and not phonecall.played:
                        return
                    if not phonecall.available:
                        phonecall.available = True
                        return

        def mark_next_played(self):
            """
            Mark the next unplayed item as played.
            """

            if not self.played:
                self.played = True
                # Add this label to the list of completed labels for the History
                if self.expired and not self.buyback:
                    store.persistent.completed_chatrooms[
                        self.expired_label] = True
                else:
                    store.persistent.completed_chatrooms[
                        self.item_label] = True
                return True
            
            # Otherwise, check story calls
            if len(self.story_calls_list) > 0:
                for phonecall in self.story_calls_list:
                    if not phonecall.played:
                        phonecall.played = True
                        if phonecall.expired and not phonecall.buyback:
                            store.persistent.completed_chatrooms[
                                phonecall.expired_label] = True
                        else:
                            store.persistent.completed_chatrooms[
                                phonecall.item_label] = True
                        return True

            return False

        def on_available_message(self):
            """
            Return a message to display to the player when this item
            is available.
            """
            return "[[new story available]"

        def can_expire(self):
            """Return True if there are items that can be expired."""

            if not self.played and not self.buyahead and not self.buyback:
                return True
            
            if len(self.story_calls_list) > 0:
                for phonecall in self.story_calls_list:
                    if (not phonecall.played and not phonecall.buyahead
                            and not phonecall.buyback):
                        return True
            return False

        def expire(self):
            """Expire all items related to this timeline item."""

            if not self.played and not self.buyahead and not self.buyback:
                self.expired = True
            
            # Also expire any story calls associated with this item
            if len(self.story_calls_list) > 0:
                for phonecall in self.story_calls_list:
                    if (not phonecall.played and not phonecall.buyahead
                            and not phonecall.buyback):
                        phonecall.expired = True

        def was_played(self, ever=True):
            """
            Return whether this item has been played by the player, whether
            in expired format or regular. If ever=True, check if this has
            been seen across any playthrough. Else, check if it has been
            played on this particular playthrough.
            """

            if not ever:
                return self.played
            
            if (self.played_regular() or self.played_expired()):
                return True
            return False

        def get_final_item(self):
            """Return the final item to be played in this timeine item."""

            if len(self.story_calls_list) > 0:
                return self.story_calls_list[-1]
            
            if self.plot_branch and self.plot_branch.vn_after_branch:
                return self.plot_branch.stored_vn

            return self

        def get_timeline_img(self, was_played=True):
            """
            Return the hover image that should be used for this item.
            was_played is True if any prior items were played first.
            """
            print("Got default timeline image")
            return "#59efc7"

        def played_regular(self):
            """Return True if the regular label of this item has been played."""

            return store.persistent.completed_chatrooms.get(self.item_label)

        def played_expired(self):
            """Return True if the expired label of this item has been played."""

            return store.persistent.completed_chatrooms.get(self.expired_label)

        def buy_ahead(self):
            """
            Make all items related to this item available and set buyahead.
            Return True if successful, and False if encountered a plot branch.
            """

            self.available = True
            self.buyahead = True
            self.expired = False

            if len(self.story_calls_list) > 0:
                for phonecall in self.story_calls_list:
                    phonecall.buy_ahead()
            
            if self.plot_branch:
                return False
            return True

        def call_after_label(self, new_context=False):
            """Call this item's after_ label, if it exists."""

            if not renpy.has_label('after_' + self.item_label):
                return
            
            store.was_expired = self.expired
            if new_context:
                renpy.call_in_new_context('after_' + self.item_label)
            else:
                renpy.call('after_' + self.item_label)
            store.was_expired = False
            return
        
        def total_timeline_items(self, only_if_unplayed=False):
            """Return the number of timeline items contained within this one."""

            if not only_if_unplayed:
                return 1 + len(self.story_calls_list)
            
            # Otherwise, count only unplayed items
            total = 0
            if not self.played:
                total += 1
            if len(self.story_calls_list) > 0:
                for phonecall in self.story_calls_list:
                    if not phonecall.played:
                        total += 1
            return total

        def participated_percentage(self, check_all=False):
            """
            Return the number of timeline items that have been participated in.

            Parameters:
            -----------
            check_all : bool
                If True, return a tuple with the number of participated items
                vs the total number of items contained within this one.
                StoryMode cannot expire and so is not included in the total.
            """

            if not check_all:
                # Only return whether or not this item was played
                if self.played and not self.expired:
                    return 1.0
                else:
                    return 0.0
            
            # Otherwise, return a tuple
            total = 1.0 + len(self.story_calls_list)
            num_played = 0.0
            if len(self.story_calls_list) > 0:
                for phonecall in self.story_calls_list:
                    if phonecall.played and not phonecall.expired:
                        num_played += 1.0

            if self.played and not self.expired:
                num_played += 1.0
            return (num_played, total)


        def __eq__(self, other):
            """Check for equality between two TimelineItem objects."""

            if not isinstance(other, TimelineItem):
                return False
            return (self.title == other.title
                    and self.item_label == other.item_label
                    and self.trigger_time == other.trigger_time)

        def __ne__(self, other):
            """Check for inequality between two TimelineItem objects."""

            if not isinstance(other, TimelineItem):
                return True
            return (self.title != other.title
                    or self.item_label != other.item_label
                    or self.triggger_time != other.trigger_time)

        
    class ChatRoom(TimelineItem):
        """
        Class that stores information needed to display chatrooms in-game.

        Attributes:
        -----------
        participants : ChatCharacter[]
            List of ChatCharacters who were present over the course of this
            chatroom. Initially set to the characters who begin in the chat.
        original_participants : ChatCharacter[]
            List of ChatCharacters who begin in the chatroom.
        story_mode : StoryMode
            Contains the information for a Story Mode section following
            this chatroom.
        participated : bool
            True if the player participated in this chatroom.
        replay_log : ReplayEntry
            List of ReplayEntry objects that keeps track of how this chatroom
            played out to display to the player during a replay.        
        """

        def __init__(self, title, chatroom_label, trigger_time,
                participants=None, story_mode=None, plot_branch="None",
                save_img='auto'):
            """
            Create a ChatRoom object to store information about a particular
            chatroom on a route.

            Parameters:
            -----------
            title : string
                Title of the chatroom.
            chatroom_label : string
                Label to jump to to view this chatroom.
            trigger_time : string
                Time this chatroom should be available at, if playing in
                real-time. Formated as "00:00" in 24-hour time.
            participants : ChatCharacter[]
                List of ChatCharacters who were present over the course of
                this chatroom. Initially set to the characters who begin in
                the chat.
            story_mode : StoryMode
                Contains the information for a StoryMode section that follows
                this chatroom.
            plot_branch : bool
                True if this chatroom should have a plot branch following it
                and the StoryMode associated with the chatroom should appear
                after the plot branch has been proceeded through; False if 
                there is a plot branch but no corresponding StoryMode.
            save_img : string
                A short version of the file path used to display the icon next
                to a save file when this is the active timeline item.
            """

            super(ChatRoom, self).__init__(title, chatroom_label, trigger_time,
                plot_branch, save_img)
                        
            self.participants = participants or []
            if len(self.participants) == 0:
                self.original_participants = []
            else:
                self.original_participants = list(participants)

            self.story_mode = None
            if story_mode:
                self.story_mode = story_mode
            else:
                # Check for labels to auto-define StoryMode objects
                # First check for the default VN with no associated character
                if renpy.has_label(self.item_label + '_vn'):
                    self.story_mode = create_dependent_VN(
                        self.item_label + '_vn')
                # Check for a party label
                elif renpy.has_label(self.item_label + '_party'):
                    self.story_mode = create_dependent_VN(
                        self.item_label + '_party',
                        party=True)
                # Check for VNs associated with a character
                else:                    
                    for c in store.all_characters:
                        # VNs are called things like my_label_vn_r
                        vnlabel = self.item_label + '_vn_' + c.file_id
                        if renpy.has_label(vnlabel):
                            self.story_mode = create_dependent_VN(vnlabel, c)
                            # Should only be one StoryMode object per chat
                            break
                
            if self.plot_branch and self.plot_branch.vn_after_branch:
                self.plot_branch.stored_vn = self.story_mode
                self.story_mode = None

            self.participated = False
            self.replay_log = []

        def unlock_all(self):
            """Ensure all items associated with this chatroom are available."""

            super(ChatRoom, self).unlock_all()
            if self.story_mode:
                self.story_mode.available = True

        def all_available(self):
            """
            Return True if everything associated with this item is available.
            """

            if self.story_mode and not self.story_mode.available:
                return False
            return super(ChatRoom, self).all_available()
            
        def all_played(self):
            """
            Return True if everything associated with this item has been
            played.
            """

            if self.story_mode and not self.story_mode.played:
                return False
            return super(ChatRoom, self).all_played()

        
        def make_next_available(self):
            """
            Make the next unavailable item associated with this item
            available to play.
            """

            if not self.available:
                self.available = True
                return True
            # Subsequent items are only available if previous ones were played
            if not self.played:
                return
            
            if self.story_mode and not self.story_mode.available:
                self.story_mode.available = True
                return

            # Don't make anything past the Story Mode available if it hasn't
            # been played
            if self.story_mode and not self.story_mode.played:
                return
            super(ChatRoom, self).make_next_available()

        def mark_next_played(self):
            """
            Mark the next unplayed item as played.
            """

            if not self.played:
                self.played = True
                # Add this label to the list of completed labels for the History
                if self.expired and not self.buyback:
                    store.persistent.completed_chatrooms[
                        self.expired_label] = True
                    self.participated = False
                else:
                    store.persistent.completed_chatrooms[
                        self.item_label] = True
                    self.participated = True
                return True

            if self.story_mode and not self.story_mode.played:
                self.story_mode.played = True
                # StoryMode doesn't expire
                store.persistent.completed_chatrooms[
                    self.story_mode.item_label] = True

                return True

            return super(ChatRoom, self).mark_next_played()
            

        def on_available_message(self):
            """
            Return a message to display to the player when this item
            is available.
            """

            return "[[new chatroom] " + self.title

        def get_final_item(self):
            """Return the final item to be played in this timeine item."""

            if len(self.story_calls_list) > 0:
                return self.story_calls_list[-1]
                
            if self.story_mode:
                return self.story_mode
            
            if self.plot_branch and self.plot_branch.vn_after_branch:
                return self.plot_branch.stored_vn

            return self

        def get_timeline_img(self, was_played=True):
            """
            Return the hover image that should be used for this item.
            was_played is True if any prior items were played first.
            """

            if store.persistent.testing_mode:
                return 'chat_active'
            
            if self.played:
                return 'chat_active'
            elif self.available and was_played:
                return 'chat_selected'
            else:
                return 'chat_inactive'

        def add_participant(self, chara):
            """Add a participant to the chatroom."""

            if not (chara in self.participants):
                self.participants.append(chara)
            return
        
        def reset_participants(self):
            """
            Reset participants to the original set of participants before
            the user played this chatroom. Used when a player backs out
            of a chatroom.
            """

            self.participants = list(self.original_participants)

        def buy_ahead(self):
            """
            Make all items related to this item available and set buyahead.
            Return True if successful, and False if encountered a plot branch.
            """

            if self.story_mode:
                self.story_mode.available = True
            
            return super(ChatRoom, self).buy_ahead()
            
        def total_timeline_items(self, only_if_unplayed=False):
            """Return the number of timeline items contained within this one."""

            if (self.story_mode 
                    and ((only_if_unplayed and not self.story_mode.played)
                        or (not only_if_unplayed))):
                return 1 + super(ChatRoom,
                    self).total_timeline_items(only_if_unplayed)
            else:
                return super(ChatRoom,
                    self).total_timeline_items(only_if_unplayed)

    class StoryMode(TimelineItem):
        """
        Class that stores information needed to display StoryMode objects
        in-game.

        Attributes:
        -----------
        who : string
            The character's file_id whose picture is on the StoryMode icon
            in the timeline.
        party : bool
            True if this StoryMode leads to the party.
        """

        def __init__(self, title, vn_label, trigger_time, who=None,
                plot_branch="None", party=False, save_img='auto'):
            """
            Create a StoryMode object to keep track of information for a 
            Story Mode section.

            Parameters:
            -----------
            title : string
                The title of this story mode section.
            vn_label : string
                The label to jump to to play this story mode.
            trigger_time : string
                Formatted as "00:00" in 24-hour time. The time this story
                mode should appear at, if it is not attached to a chatroom.
            who : ChatCharacter
                The character whose picture is on the StoryMode icon in
                the timeline.
            plot_branch : bool
                True if this story mode should have a plot branch following it
                and the StoryMode associated with the chatroom should appear
                after the plot branch has been proceeded through; False if 
                there is a plot branch but no corresponding StoryMode.
            party : bool
                True if this story mode leads to the party.
            save_img : string
                A short version of the file path used to display the icon next
                to a save file when this is the active timeline item.
            """

            super(StoryMode, self).__init__(title, vn_label, trigger_time,
                plot_branch, save_img)

            if who is not None:
                self.who = who.file_id
            else:
                self.who = None
            self.party = party

        @property
        def vn_img(self):        
            """Return the image that should be used in the timeline."""

            if self.who:
                return 'vn_' + self.who
            else:
                return 'vn_other'
        @property 
        def expired(self):
            """StoryMode objects do not expire like other TimelineItems."""
            return False

        @expired.setter
        def expired(self, other):
            """
            StoryMode objects do not expire like other TimelineItems.
            """
            pass

        def on_available_message(self):
            """
            Return a message to display to the player when this item
            is available.
            """

            return "[[new story mode] " + self.title
        
        def can_expire(self):
            """Return True if there are items that can be expired."""
            
            if len(self.story_calls_list) > 0:
                for phonecall in self.story_calls_list:
                    if (not phonecall.played and not phonecall.buyahead
                            and not phonecall.buyback):
                        return True
            return False

        def get_timeline_img(self, was_played=True):
            """
            Return the hover image that should be used for this item.
            was_played is True if any prior items were played first.
            """
            
            if store.persistent.testing_mode:
                if self.party:
                    return 'vn_party'
                else:
                    return 'vn_active'

            if self.party:
                if self.available and was_played:
                    return 'vn_party'
                else:
                    return 'vn_party_inactive'
            if self.played:
                return 'vn_active'
            elif self.available and was_played:
                return 'vn_selected'
            else:
                return 'vn_inactive'

        def participated_percentage(self, check_all=False):
            """
            Return the number of timeline items that have been participated in.

            Parameters:
            -----------
            check_all : bool
                If True, return a tuple with the number of participated items
                vs the total number of items contained within this one.
                StoryMode cannot expire and so is not included in the total.
            """

            if not check_all:
                # Only return whether or not this item was played
                return 0.0
            
            # Otherwise, return a tuple
            total = len(self.story_calls_list)
            num_played = 0.0
            if len(self.story_calls_list) > 0:
                for phonecall in self.story_calls_list:
                    if phonecall.played and not phonecall.expired:
                        num_played += 1.0
            
            return (num_played, total)

    class StoryCall(TimelineItem):
        """
        Class that stores information needed to display mandatory phone
        calls on the timeine.

        Attributes:
        -----------
        caller : ChatCharacter
            The character who is calling the player.
        """

        def __init__(self, title, phone_label, trigger_time, caller,
                plot_branch="None", save_img='auto'):
            """
            Create a StoryCall object to keep track of information for a
            mandatory phone call.

            Parameters:
            -----------
            title : string
                Title of this phone call.
            phone_label : string
                The label to jump to to play this phone call.
            trigger_time : string
                Formatted as "00:00" in 24-hour time. The time this story
                call should appear at, if it is not attached to a chatroom.
            caller : ChatCharacter
                The character who is calling the player.
            plot_branch : bool
                True if this story call should have a plot branch following it
                and the StoryMode associated with the chatroom should appear
                after the plot branch has been proceeded through; False if 
                there is a plot branch but no corresponding StoryMode.
            save_img : string
                A short version of the file path used to display the icon next
                to a save file when this is the active timeline item.
            """

            super(StoryCall, self).__init__(title, phone_label, trigger_time,
                plot_branch, save_img)

            self.caller = caller

        def get_timeline_img(self, was_played=True):
            """
            Return the hover image that should be used for this item.
            was_played is True if any prior items were played first.
            """

            if store.persistent.testing_mode:
                return 'story_call_active'
            
            if self.played:
                return 'story_call_active'
            elif self.available and was_played:
                return 'story_call_selected'
            else:
                return 'story_call_inactive'

        @property
        def phone_label(self):
            """Maintain compatibility with PhoneCall objects."""
            
            return self.item_label

    def create_dependent_storycall(caller, phone_label):
        """
        Return a StoryCall which is tied to a chatroom or StoryMode and thus
        doesn't need additional information.
        """
        return StoryCall(title="", phone_label=phone_label, trigger_time=False,
            caller=caller)


    def create_dependent_VN(vn_label, who=None, party=False):
        """
        Return a StoryMode which is tied to a chatroom and thus doesn't need
        additional information.
        """
        # print("Making a StoryMode", vn_label)
        return StoryMode(title="", vn_label=vn_label, trigger_time=False,
                who=who, party=party)

    def vnmode_to_storymode(item, copy_everything=False):
        """Convert item to a StoryMode object and return it."""

        # print("LOOKING AT:", item.vn_label)
        if (item.plot_branch and item.plot_branch.stored_vn):
            pbranch = True
        elif isinstance(item.plot_branch, PlotBranch):
            pbranch = False
        else:
            pbranch = "None"

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

        # print("LOOKING AT:", item.title)

        if (item.plot_branch and item.plot_branch.stored_vn):
            pbranch = True
        elif isinstance(item.plot_branch, PlotBranch):
            pbranch = False
        else:
            pbranch = "None"

        new_obj = ChatRoom(title=item.title, chatroom_label=item.chatroom_label,
            trigger_time=item.trigger_time, participants=item.participants,
            plot_branch=pbranch, save_img=item.save_img)

        
        if copy_everything:
            # Need to check all other fields as well
            # It's okay to copy list addresses since the program won't be
            # using the originals any more
            new_obj.original_participants = item.original_participants
            new_obj.played = item.played
            new_obj.participated = item.participated
            new_obj.available = item.available
            new_obj.expired = item.expired
            new_obj.buyback = item.buyback
            new_obj.buyahead = item.buyahead
            new_obj.replay_log = item.replay_log
            if item.vn_obj:
                new_obj.story_mode.played = item.vn_obj.played
                new_obj.story_mode.available = item.vn_obj.available
           

        # Test to see if the two items are the same
        if item.title != new_obj.title:
            print("title:", item.title, new_obj.title)
        if item.chatroom_label != new_obj.item_label:
            print("label:", item.chatroom_label, new_obj.item_label)
        if item.expired_chat != new_obj.expired_label:
            print("expired:", item.expired_chat, new_obj.expired_label)
        if item.trigger_time != new_obj.trigger_time:
            print("time:", item.trigger_time, new_obj.trigger_time)
        if item.participants != new_obj.participants:
            print("participants:", item.participants, new_obj.participants)
        if (item.plot_branch != new_obj.plot_branch
                and not (item.plot_branch == False 
                    and new_obj.plot_branch is None)
                and not (isinstance(item.plot_branch, PlotBranch)
                    and isinstance(new_obj.plot_branch, PlotBranch))):
            print("plot_branch:", item.plot_branch, new_obj.plot_branch)
        if (item.plot_branch and item.plot_branch.stored_vn):
            if (item.plot_branch.stored_vn.vn_label 
                    != new_obj.plot_branch.stored_vn.item_label):
                print("plot_branch stored VN:", item.plot_branch.stored_vn.vn_label,
                    new_obj.plot_branch.stored_vn.item_label)
        if (item.vn_obj and new_obj.story_mode):
            if item.vn_obj.vn_label != new_obj.story_mode.item_label:
                print("vn/story mode:", item.vn_obj.vn_label, 
                    new_obj.story_mode.item_label)
        if (item.vn_obj and not new_obj.story_mode):
            print("\ \ \ So we don't have an equivalent story mode for some reason")
            print("vn/story mode:", item.vn_obj, new_obj.story_mode)
        if item.save_img != new_obj.save_img:
            print("save_img:", item.save_img, new_obj.save_img)
        if item.played != new_obj.played:
            print("played:", item.played, new_obj.played)
        if item.participated != new_obj.participated:
            print("participated:", item.participated, new_obj.participated)
        if item.available != new_obj.available:
            print("available:", item.available, new_obj.available)
        if item.expired != new_obj.expired:
            print("expired:", item.expired, new_obj.expired)
        if item.buyback != new_obj.buyback:
            print("buyback:", item.buyback, new_obj.buyback)
        if item.buyahead != new_obj.buyahead:
            print("buyahead:", item.buyahead, new_obj.buyahead)
        if item.outgoing_calls_list != new_obj.outgoing_calls_list:
            print("outgoing_calls_list:", item.outgoing_calls_list, new_obj.outgoing_calls_list)
        if item.incoming_calls_list != new_obj.incoming_calls_list:
            print("incoming_calls_list:", item.incoming_calls_list, new_obj.incoming_calls_list)
        if item.story_calls_list != new_obj.story_calls_list:
            print("story_calls_list:", item.story_calls_list, new_obj.story_calls_list)

        return new_obj
        
    

screen timeline_item_history(item):

    python:
        # Determine if the participants list needs to scroll or not
        part_anim = null_anim
        if isinstance(item, ChatRoom) and item.participants:
            if len(item.participants) > 4:
                part_anim = participant_scroll

        # ChatRoom story mode displays similarly to solo StoryMode in
        # some cases
        if isinstance(item, StoryMode):
            story_mode = item
        elif isinstance(item, ChatRoom) and item.story_mode:
            story_mode = item.story_mode
        else:
            story_mode = None

        # StoryCall items display the same if they are alone or not
        if isinstance(item, StoryCall):
            story_calls = [item]
        elif isinstance(item, TimelineItem) and item.story_calls_list:
            story_calls = item.story_calls_list
        else:
            story_calls = None


        replay_dictionary = {'observing': True,
                            'current_chatroom': item,
                            'current_day': current_day,
                            'current_day_num': current_day_num,
                            'name': persistent.name}

        expired_replay_dictionary = {'expired_replay': True,
                            'observing': True,
                            'current_chatroom': item,
                            'current_day': current_day,
                            'current_day_num': current_day_num,
                            'name': persistent.name}
    style_prefix None
    null height 10
    if not isinstance(item, TimelineItem):
        # It's the name/title of the ending
        frame:
            style_prefix 'history_item_text'
            text item
    elif isinstance(item, ChatRoom):
        frame:
            style_prefix 'history_chatroom'
            # These are the two buttons to replay the chat
            hbox:
                button:
                    if item.played_expired():
                        background 'history_chat_active'  
                        hover_foreground '#fff5'                      
                        action Replay(item.expired_label, 
                                        scope=expired_replay_dictionary)
                    else:
                        background Fixed('history_chat_inactive', "#000c")
                        foreground "#0003"
                        action Show("confirm", message=("You have not yet"
                                + " viewed this chat in-game."),
                            yes_action=Hide('confirm'))
                    add 'history_chat_alone' align (0.5, 0.5)
                    if not item.played_expired():
                        add 'plot_lock' align (0.5, 0.5)
                button:
                    if item.played_regular():
                        hover_foreground '#fff5'
                        background 'history_chat_active'                        
                        action Replay(item.item_label,
                                        scope=replay_dictionary)
                    else:
                        background Fixed('history_chat_inactive', "#000c")
                        foreground "#0003"
                        action Show("confirm", message=("You have not yet"
                                + " viewed this chat in-game."),
                            yes_action=Hide('confirm'))
                    add 'history_chat_participated' align (0.5, 0.5)
                    if not item.played_regular():
                        add 'plot_lock' align (0.5, 0.5)
                    
                
            vbox:
                style_prefix 'chat_timeline'
                # This box displays the trigger time and title of 
                # the chatroom; optionally at a scrolling transform 
                # so you can read the entire title
                hbox:
                    frame:
                        xoffset 77
                        yoffset 13
                        text item.trigger_time:
                            size 27 
                            xalign 0.5
                            text_align 0.5
                    viewport:               
                        xysize(400,27)
                        if get_text_width(item.title, 
                                'chat_timeline_text') >= 400:
                            frame:
                                xysize(400,27)
                                text item.title at chat_title_scroll
                        else:
                            text item.title
                # Shows a list of all the people who start in this chatroom
                viewport:
                    xysize(530, 85)
                    yoffset 13
                    xoffset 77            
                    yalign 0.5
                    frame:
                        xysize(355, 85)
                        hbox at part_anim:
                            yalign 0.5
                            spacing 5
                            if item.original_participants:
                                for person in item.original_participants:
                                    if person.participant_pic:
                                        add person.participant_pic

    # It's a solo StoryMode with a time
    if story_mode and story_mode.trigger_time and not story_mode.party:
        button:
            style_prefix 'solo_vn'     
            foreground 'solo_vn_active'
            hover_foreground Fixed('solo_vn_active', 'solo_vn_hover')
            action [Preference("auto-forward", "disable"),
                    Replay(story_mode.item_label,
                        scope=replay_dictionary)]          
            add story_mode.vn_img align (1.0, 1.0) xoffset 3 yoffset 5
            hbox:
                frame:
                    text story_mode.trigger_time
                viewport:
                    frame:
                        xsize 350
                        if get_text_width(story_mode.title,
                                'chat_timeline_text') >= 350:
                            text story_mode.title at chat_title_scroll
                        else:
                            text story_mode.title

    # It's a StoryMode without a time
    elif story_mode and not story_mode.party:
        frame:
            style_prefix 'reg_timeline_vn'            
            has hbox
            add 'vn_marker'            
            button:
                foreground 'vn_active'
                hover_foreground 'vn_active_hover'
                action [Preference("auto-forward", "disable"),
                        Replay(story_mode.item_label,
                                scope=replay_dictionary)]                 
                add story_mode.vn_img xoffset -5
    
    # It's the StoryMode that leads to the party
    elif story_mode and story_mode.party:
        frame:
            style_prefix 'party_timeline_vn'        
            button:
                background 'vn_party'
                hover_foreground 'vn_party'
                action [Preference("auto-forward", "disable"), 
                        Replay(story_mode.item_label,
                            scope=replay_dictionary)]  

    if story_calls:
        # There are story calls to display
        for phonecall in story_calls:
            use history_timeline_story_calls(phonecall, item)

    # Now add an hbox of the phone calls available after this chatroom
    if (isinstance(item, TimelineItem) 
            and (item.incoming_calls_list or item.outgoing_calls_list)):
        hbox:
            xalign 1.0
            xoffset -40
            add Transform('call_mainicon', size=(60,60)) align (0.5, 0.75)
            if item.incoming_calls_list:
                use history_calls_list(item, item.incoming_calls_list, 'incoming')
            if item.outgoing_calls_list:
                use history_calls_list(item, item.outgoing_calls_list, 'outgoing')

screen history_timeline_story_calls(phonecall, item):
    
    frame:
        xoffset 70
        background 'story_call_history'
        xysize (625, 111)
        xalign 0.0
        hbox:
            yoffset 12 xoffset 78
            spacing 25
            # First add the profile picture of the caller
            fixed:
                fit_first True
                add phonecall.caller.participant_pic:
                    xalign 0.0
                add Transform('call_mainicon', size=(28,28)) align (0.01, 0.99)
            vbox:
                spacing 25
                hbox:
                    spacing 30
                    # The time of the call
                    $ the_time = phonecall.trigger_time or item.trigger_time
                    text the_time style 'chat_timeline_text'
                    # The title of the chatroom
                    text phonecall.caller.name style 'chat_timeline_text'
                # Thing that says the caller's name
                fixed:
                    $ the_title = phonecall.title or "Story Call"
                    text the_title style 'chat_timeline_text'
                
        # The replay icons
        hbox:
            align (0.99,0.6)            
            spacing 10
            button:
                xysize (80,80)
                if phonecall.played_expired():
                    background 'history_chat_active'  
                    hover_foreground '#fff5'                      
                    action Replay(phonecall.expired_label, 
                                    scope={'expired_replay': True,
                            'observing': True,
                            'current_chatroom': item,
                            'current_day': current_day,
                            'current_day_num': current_day_num,
                            'name': persistent.name,
                            'current_call': PhoneCall(phonecall.caller, 'n/a')})
                else:
                    background Fixed('history_chat_inactive', "#000c")
                    foreground "#0003"
                    action Show("confirm", message=("You have not yet"
                        + " viewed this call in-game."),
                    yes_action=Hide('confirm'))
                add 'call_missed_outline' align (0.5, 0.5)
                if not phonecall.played_expired():
                    add 'plot_lock' align (0.5, 0.5)
            button:
                xysize(80,80)
                if phonecall.played_regular():
                    hover_foreground '#fff5'
                    background 'history_chat_active'                        
                    action Replay(phonecall.item_label,
                                    scope={'observing': True,
                    'current_chatroom': item,
                    'current_day': current_day,
                    'current_day_num': current_day_num,
                    'name': persistent.name,
                    'current_call': PhoneCall(phonecall.caller, 'n/a')})
                else:
                    background Fixed('history_chat_inactive', "#000c")
                    foreground "#0003"
                    action Show("confirm", message=("You have not yet"
                        + " viewed this call in-game."),
                    yes_action=Hide('confirm'))
                add 'call_incoming_outline' align (0.5, 0.5)
                if not phonecall.played_regular():
                    add 'plot_lock' align (0.5, 0.5)

screen history_calls_list(item, call_list, call_icon):    
    for c in call_list:
        if persistent.completed_chatrooms.get(c):
            button:
                background Transform(c.split('_')[-1] + '_contact', 
                                                size=(85,85))
                hover_background Fixed(Transform(c.split('_')[-1] + '_contact',
                                size=(85,85)), Transform(c.split('_')[-1]
                                + '_contact', size=(85,85)))
                add Transform('contact_darken', size=(85,85), alpha=0.3):
                    align (0.5,0.5)
                add Transform('call_' + call_icon + '_outline', size=(32, 32)):
                    align (1.0, 1.0)
                xysize (85,85)
                action Replay(c, scope={'observing': True,
                    'current_chatroom': item,
                    'current_day': current_day,
                    'current_day_num': current_day_num,
                    'name': persistent.name,
                    'current_call': get_caller(c)})

                       
screen timeline_story_calls(phonecall, item, was_played):
    python:
        if phonecall.expired:
            call_title_width = 300
            call_box_width = 520
        else:
            call_title_width = 400
            call_box_width = 620

    hbox:
        style 'timeline_hbox'
        ysize 111
        button:
            xysize (call_box_width, 111)
            background phonecall.get_timeline_img(was_played)
            hover_foreground 'story_call_hover'
            if phonecall.available and was_played:
                # Determine where to take the player based on whether this
                # item has expired or not
                if phonecall.expired and not phonecall.played:
                    action [SetVariable('current_chatroom', item), 
                        Preference("auto-forward", "enable"),                    
                        Jump(phonecall.expired_label)]
                else:
                    if (phonecall.played and not persistent.testing_mode):
                        action [SetVariable('current_chatroom', item),
                            SetVariable('observing', True),
                            Preference("auto-forward", "enable"),
                            Jump(phonecall.item_label)]
                    else:
                        action [SetVariable('current_chatroom', item),
                            Preference("auto-forward", "enable"),
                            # Make it look like an incoming call
                            Play('music', persistent.phone_tone),
                            Show('incoming_call', 
                                phonecall=phonecall)]
            hbox:
                yoffset 12 xoffset 78
                spacing 25
                # First add the profile picture of the caller
                fixed:
                    fit_first True
                    add phonecall.caller.participant_pic:
                        xalign 0.0
                    add Transform('call_mainicon', size=(28,28)) align (0.01, 0.99)
                vbox:
                    spacing 25
                    hbox:
                        spacing 30
                        # The time of the call
                        $ the_time = phonecall.trigger_time or item.trigger_time
                        text the_time style 'chat_timeline_text'
                        # The title of the chatroom
                        text phonecall.caller.name style 'chat_timeline_text'
                    # Thing that says the caller's name
                    fixed:
                        $ the_title = phonecall.title or "Story Call"
                        text the_title style 'chat_timeline_text'
        
        if phonecall.expired and not phonecall.buyback:
            imagebutton:
                yalign 0.85
                xalign 0.5
                idle 'expired_chat'
                hover_background 'btn_hover:expired_chat'
                if phonecall.available or persistent.testing_mode:
                    action Show('confirm', message=("Would you like to"
                                + " call " + phonecall.caller.name + " back to "
                                + " participate in this phone call?"),
                            yes_action=[SetField(phonecall, 'expired', False),
                            SetField(phonecall, 'buyback', True),
                            SetField(phonecall, 'played', False),
                            renpy.retain_after_load,
                            renpy.restart_interaction, Hide('confirm')], 
                            no_action=Hide('confirm'))    

