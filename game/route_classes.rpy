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
        parent : TimelineItem
            If this item is part of a "family" of TimelineItems, this links
            to its parent.
        delivered_post_items : bool
            True if the after_ label has been called for this TimelineItem.
        after_label : string
            Label to jump to to deliver post-item content.
        phonecall_label : string
            Label to use to construct phone calls that take place after
            this item.
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

        def __init__(self, title, item_label, trigger_time, plot_branch=None,
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

            if plot_branch is None:
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
            self.parent = None
            self.delivered_post_items = False
            self.after_label = "after_" + item_label
            self.phonecall_label = item_label

            self.outgoing_calls_list = [ (self.item_label + '_outgoing_' 
                + x.file_id) for x in store.all_characters 
                if renpy.has_label(self.item_label + '_outgoing_' 
                    + x.file_id)]
            self.incoming_calls_list = [ (self.item_label + '_incoming_' 
                + x.file_id) for x in store.all_characters 
                if renpy.has_label(self.item_label + '_incoming_' 
                    + x.file_id)]

            self.story_calls_list = [
                    create_dependent_storycall(self, x, 
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

        def expire_all(self):
            """Expire all items related to this timeline item."""

            if not self.played and not self.buyahead and not self.buyback:
                self.expired = True
            
            # Also expire any story calls associated with this item
            if len(self.story_calls_list) > 0:
                for phonecall in self.story_calls_list:
                    if (not phonecall.played and not phonecall.buyahead
                            and not phonecall.buyback):
                        phonecall.expired = True

        def expire(self):
            """Expire just this particular item due to player action."""

            self.expired = True
            self.buyback = False
            self.buyahead = False

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

            if self.plot_branch and self.plot_branch.vn_after_branch:
                return self.plot_branch.stored_vn
            
            if len(self.story_calls_list) > 0:
                return self.story_calls_list[-1]

            return self
        
        def get_item_before_branch(self):
            """Return the final item that happens before a plot branch."""

            if self.parent and self.parent.plot_branch:
                if len(self.parent.story_calls_list) > 0:
                    return self.parent.story_calls_list[-1]
                # Otherwise this item is basically guaranteed to be a
                # StoryMode, since ChatRooms don't have parents
                return self
            # Otherwise, this item doesn't have a parent
            if len(self.story_calls_list) > 0:
                return self.story_calls[-1]
            return self

        def get_timeline_img(self, was_played=True):
            """
            Return the hover image that should be used for this item.
            was_played is True if any prior items were played first.
            """
            print_file("Got default timeline image")
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

            self.delivered_post_items = True
            if not renpy.has_label(self.after_label):
                return
            
            store.was_expired = self.expired
            if new_context:
                renpy.call_in_new_context(self.after_label)
            else:
                renpy.call(self.after_label)
            store.was_expired = False
            return
        
        def deliver_calls(self):
            """Deliver phone calls associated with this item."""

            if self.phonecall_label:
                deliver_calls(self.phonecall_label, expired=self.expired)
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
                participants=None, story_mode=None, plot_branch=None,
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
                    self.story_mode = create_dependent_VN(self,
                        self.item_label + '_vn')
                # Check for a party label
                elif renpy.has_label(self.item_label + '_party'):
                    self.story_mode = create_dependent_VN(self,
                        self.item_label + '_party',
                        party=True)
                # Check for VNs associated with a character
                else:                    
                    for c in store.all_characters:
                        # VNs are called things like my_label_vn_r
                        vnlabel = self.item_label + '_vn_' + c.file_id
                        if renpy.has_label(vnlabel):
                            self.story_mode = create_dependent_VN(self, 
                                                                vnlabel, c)
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

            if self.plot_branch and self.plot_branch.vn_after_branch:
                return self.plot_branch.stored_vn
                
            if len(self.story_calls_list) > 0:
                return self.story_calls_list[-1]
            
            if self.story_mode:
                return self.story_mode

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

        def expire(self):
            """Expire just this particular item due to player action."""

            # This chatroom has no longer been participated in
            self.participated = False
            # Its replay log is reset
            self.replay_log = []
            # Participants are reset
            self.reset_participants()

            super(ChatRoom, self).expire()
        
        def get_item_before_branch(self):
            """Return the final item that happens before a plot branch."""

            # ChatRooms don't have a parent
            if len(self.story_calls_list) > 0:
                return self.story_calls[-1]
            elif self.story_mode:
                return self.story_mode
            return self

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
                plot_branch=None, party=False, save_img='auto'):
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
                plot_branch=None, save_img='auto'):
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

    def create_dependent_storycall(parent, caller, phone_label):
        """
        Return a StoryCall which is tied to a chatroom or StoryMode and thus
        doesn't need additional information.
        """
        temp = StoryCall(title="", phone_label=phone_label, trigger_time=False,
            caller=caller)
        temp.parent = parent
        return temp


    def create_dependent_VN(parent, vn_label, who=None, party=False):
        """
        Return a StoryMode which is tied to a chatroom and thus doesn't need
        additional information.
        """        
        temp = StoryMode(title="", vn_label=vn_label, trigger_time=False,
                who=who, party=party)
        temp.parent = parent
        return temp

    
        
## The label that is called when a timeline item has been completed
label end_timeline_item():
    $ end_timeline_item_checks()

    if observing:
        $ observing = False
        call screen timeline(current_day, current_day_num)
        return

    # Otherwise, this is the first time this item has been played
    if isinstance(current_timeline_item, ChatRoom):
        call screen signature_screen(True)
    elif isinstance(current_timeline_item, StoryMode):
        call screen signature_screen(False)

    $ finish_timeline_item(current_timeline_item)
    if starter_story:
        $ starter_story = False
        call screen chat_home
        return
    $ deliver_next()
    call screen timeline(current_day, current_day_num)
    return

## The label that is called when the program exits out of a timeline item
## early, expiring it
label exit_item_early():
    # This ends replays and resets variables
    # This item is only set as the most recent item if the player wasn't
    # replaying it
    $ end_timeline_item_checks()
    if observing:
        $ observing = False
        call screen timeline(current_day, current_day_num)
        return
    # Otherwise, this item will expire
    $ expire_timeline_item(current_timeline_item)
    $ renpy.set_return_stack([])
    call screen timeline(current_day, current_day_num)
    return

init python:

    def expire_timeline_item(item):
        """Expire this timeline item and set the appropriate variables."""

        # Show the loading screen while these actions are carried out
        renpy.show_screen('loading_screen')

        # Get the parent of this item
        if not item.parent:
            the_parent = item
        else:
            the_parent = item.parent
        
        # This item expires
        item.expire()
        
        # Remove any heart points the player earned during this item
        rescind_chatroom_hp()
        # Hourglasses aren't added to the player's totals until the end,
        # so they can simply be reset
        store.chatroom_hg = 0

        reset_story_vars(item)

        # Deliver post-item content if it isn't the item immediately
        # prior to a plot branch
        if item == item.get_item_before_branch():
            item.call_after_label()
            item.deliver_calls()
            deliver_all_texts()
        
        renpy.retain_after_load()

        # Clean up the transition between the end of an item and returning
        renpy.pause(0.1)
        renpy.hide_screen('loading_screen')
        return
        

    def end_timeline_item_checks():
        """
        Perform additional logic to finish off a TimelineItem, like resetting
        story variables to return to the menu screens.
        """
        
        # This item simply ends if the user is in Replay
        if _in_replay:
            renpy.end_replay()

        # First, ensure most_recent_item is not None
        if (store.most_recent_item is None
                and store.chat_archive
                and store.chat_archive[0].archive_list):
            store.most_recent_item = store.chat_archive[0].archive_list[0]
        # Warn the user if no TimelineItems could be found
        elif store.most_recent_item is None:
            store.most_recent_item = ChatRoom('Example Chatroom',
                'example_chat', '00:01')
            print("WARNING: Could not find any TimelineItems for this route.")
            renpy.show_screen('script_error',
                message="Could not find any TimelineItems for this route.")
        
        # Next, if the player was simply observing/replaying this item,
        # reset the appropriate variables and take them back to the 
        # timeline screen
        if store.observing:
            reset_story_vars(store.current_timeline_item)
            # Main label will take players back to the timeline screen            
        return
        
    def finish_timeline_item(item, deliver_messages=True):
        """Finish resetting variables and screens for this TimelineItem."""
        
        # Show the loading screen while these actions are carried out
        renpy.show_screen('loading_screen')

        # Determine chatroom heart points (HP)
        store.persistent.HP += get_chatroom_hp()
        store.chatroom_hp = {'good': [], 'bad': [], 'break': []}
        # Give the player their hourglasses
        store.persistent.HG += store.chatroom_hg
        store.chatroom_hg = 0

        # Mark the most recent item as played
        if not item.parent:
            # This is the 'parent' item
            the_parent = item   
        else:
            the_parent = item.parent            
        
        # If the program was able to successfully mark the next item played,
        # then this is the most recent item if the player didn't buy it
        # back and it isn't the intro
        if (the_parent.mark_next_played()
                and not store.starter_story
                and not item.buyback):
            store.most_recent_item = the_parent
        
        # Deliver post-item content if this is not the last item before
        # a plot branch
        if (not item.delivered_post_items
                and not item == item.get_item_before_branch()):
            item.call_after_label()
            item.deliver_calls()
                         
        
        # Next, deliver emails and unlock the next story item
        deliver_emails()
        check_and_unlock_story()

        # Reset variables
        reset_story_vars(item)

        # Ensure any seen CGs are unlocked
        check_for_CGs(store.all_albums)

        # Save variables
        renpy.retain_after_load()

        # Check to see if honey buddha chips should be available
        if not store.chips_available:
            store.chips_available = store.hbc_bag.draw()
        
        # Clean up the transition between the end of an item and returning
        renpy.pause(0.1)
        renpy.hide_screen('loading_screen')
        return


        


    def get_chatroom_hp():
        """Return the total number of heart points earned in a chatroom."""

        return (len(store.chatroom_hp['good'])
                    + len(store.chatroom_hp['bad'])
                    - len(store.chatroom_hp['break']))

    def rescind_chatroom_hp():
        """Resets the heart points earned during this chatroom."""

        global chatroom_hp

        for chara in chatroom_hp['good']:
            chara.decrease_heart()
        for chara in chatroom_hp['bad']:
            chara.heart_points -= 1
            chara.bad_heart -= 1
            # Saeran and Ray share heart points
            if chara == store.sa:
                store.r.heart_points -= 1
                store.r.bad_heart -= 1
            elif chara == store.r:
                store.sa.heart_points -= 1
                store.sa.bad_heart -= 1
        for chara in chatroom_hp['break']:
            chara.increase_heart()

        # Remove points from persistent.HP
        store.persistent.HP -= get_chatroom_hp()
        
        # Reset chatroom_hp
        chatroom_hp = {'good': [], 'bad': [], 'break': []}


    def reset_story_vars(item, vn_jump=False):
        """
        Reset variables associated with the current item, such as hiding
        chatroom screens and resetting chatroom heart point totals.
        """

        config.skipping = False
        config.skipping = False
        store.choosing = False

        # Hide chatroom screens
        renpy.hide_screen('phone_overlay')
        renpy.hide_screen('save_and_exit')
        renpy.hide_screen('play_button')
        renpy.hide_screen('answer_button')
        renpy.hide_screen('pause_button')
        renpy.hide_screen('messenger_screen')
        renpy.hide_screen('animated_bg')
        renpy.hide_screen('vn_overlay')        
        hide_all_popups()

        # Switch off variables
        store.vn_choice = False
        
        if not vn_jump:
            store.observing = False
            renpy.music.stop()


        

