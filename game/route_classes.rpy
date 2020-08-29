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

            if self.parent:
                self.parent.unlock_all()
                return
            self.available = True
            if len(self.story_calls_list) > 0:
                for phonecall in self.story_calls_list:
                    phonecall.available = True

        # def __iter__(self):
        #     """Iterate over all the TimelineItems contained within this one."""
        #     # see Iterator Types
        #     # >> BASICMETHODS ATTRIBUTEMETHODS CALLABLEMETHODS
        #     # >> SEQUENCEMETHODS MAPPINGMETHODS NUMBERMETHODS CLASSES

        # def __contains__(self, item):
        #     """Determine if a certain item is in this object."""
        #     if item is self:
        #         return True
        #     if item in self.story_calls_list:
        #         return True
        #     return False

        def all_available(self):
            """
            Return True if everything associated with this item is available.
            """

            if self.parent:
                return self.parent.all_available()

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
                if self.currently_expired:
                    store.persistent.completed_story.add(
                        self.expired_label)
                else:
                    store.persistent.completed_story.add(
                        self.item_label)
                return True

            # Otherwise, check story calls
            if len(self.story_calls_list) > 0:
                for phonecall in self.story_calls_list:
                    if not phonecall.played:
                        phonecall.played = True
                        if phonecall.currently_expired:
                            store.persistent.completed_story.add(
                                phonecall.expired_label)
                        else:
                            store.persistent.completed_story.add(
                                phonecall.item_label)
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

        def deliver_next_after_content(self):
            """
            Ensure all played items have had their content delivered after a
            plot branch.
            """

            if self.played and not self.delivered_post_items:
                self.call_after_label(True)
                self.deliver_calls()

            for phonecall in self.story_calls_list:
               phonecall.deliver_next_after_content()


        def expire_all(self):
            """Expire all items related to this timeline item."""

            if not self.played and not self.buyahead and not self.buyback:
                self.expire(backed_out=False)

            # Also expire any story calls associated with this item
            if len(self.story_calls_list) > 0:
                for phonecall in self.story_calls_list:
                    if (not phonecall.played and not phonecall.buyahead
                            and not phonecall.buyback):
                        phonecall.expire(backed_out=False)

        def expire(self, backed_out=True):
            """Expire just this particular item due to player action."""

            self.expired = True
            self.buyback = False
            self.buyahead = False

            # If this item has an after_label, it is triggered
            if backed_out:
                self.call_after_label()
            else:
                store.expiring_item = self
                self.call_after_label(True)
                store.expiring_item = None

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
            """
            Return the final item that happens before a plot branch, if there
            is a plot branch on this item.
            """

            if self.parent and self.parent.plot_branch:
                if len(self.parent.story_calls_list) > 0:
                    return self.parent.story_calls_list[-1]
                # Otherwise this item is basically guaranteed to be a
                # StoryMode, since ChatRooms don't have parents
                return self
            elif self.parent:
                return None

            # Otherwise, this item doesn't have a parent
            if not item.plot_branch:
                return None
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

            return self.item_label in store.persistent.completed_story

        def played_expired(self):
            """Return True if the expired label of this item has been played."""

            return self.expired_label in store.persistent.completed_story

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

            print_file("Calling after_ label.", "\n   delivered_post_items:",
                self.delivered_post_items, "\n   this item's label:",
                self.item_label, "\n   This item's after_label:",
                self.after_label)

            if self.delivered_post_items:
                return

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

        def get_trigger_time(self):
            """Retrieve the trigger time of this item or its parent."""

            if self.trigger_time:
                return self.trigger_time
            elif self.parent and self.parent.trigger_time:
                return self.parent.trigger_time
            else:
                print_file("ERROR: Could not retrieve trigger_time")
                return "00:00"

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

        @property
        def currently_expired(self):
            """Return if this item is currently expired."""
            return (self.expired and not self.buyback)

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
                if self.currently_expired:
                    store.persistent.completed_story.add(
                        self.expired_label)
                    self.participated = False
                else:
                    store.persistent.completed_story.add(
                        self.item_label)
                    self.participated = True
                return True

            if self.story_mode and not self.story_mode.played:
                self.story_mode.played = True
                # StoryMode doesn't expire
                store.persistent.completed_story.add(
                    self.story_mode.item_label)

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

        def expire_all(self):
            """Expire all items related to this timeline item."""

            super(ChatRoom, self).expire_all()

            # Ensure if this item has a story_mode that its after_ label
            # is also called
            if self.story_mode:
                store.expiring_item = self.story_mode
                self.story_mode.call_after_label(True)
                store.expiring_item = None

        def expire(self, backed_out=False):
            """Expire just this particular item due to player action."""

            # This chatroom has no longer been participated in
            self.participated = False
            # Its replay log is reset
            self.replay_log = []
            # Participants are reset
            self.reset_participants()

            super(ChatRoom, self).expire(backed_out)

        def get_item_before_branch(self):
            """
            Return the final item that happens before a plot branch, if
            there is a plot branch on this item.
            """

            if not self.plot_branch:
                return None

            # ChatRooms don't have a parent
            if len(self.story_calls_list) > 0:
                return self.story_calls_list[-1]
            elif self.story_mode:
                return self.story_mode
            return self

        def deliver_next_after_content(self):
            """
            Ensure all played items have had their content delivered after a
            plot branch.
            """

            if self.played and not self.delivered_post_items:
                self.call_after_label(True)
                self.deliver_calls()

            if self.story_mode and not self.story_mode.delivered_post_items:
                self.story_mode.deliver_next_after_content()

            super(ChatRoom, self).deliver_next_after_content()

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
        is_nvl : bool
            True if this item should be displayed using NVL styling.
        """

        def __init__(self, title, vn_label, trigger_time, who=None,
                plot_branch=None, party=False, save_img='auto', is_nvl=False):
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
            self.is_nvl = is_nvl

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

        def deliver_calls(self):
            """Deliver phone calls associated with this item."""

            if (self.parent and self.phonecall_label
                    and self.phonecall_label != self.item_label):
                deliver_calls(self.phonecall_label, expired=self.parent.expired)
                return

            if self.phonecall_label:
                deliver_calls(self.phonecall_label, expired=self.expired)
            return

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
                return 1.0

            # Otherwise, return a tuple
            total = len(self.story_calls_list)
            num_played = 0.0
            if len(self.story_calls_list) > 0:
                for phonecall in self.story_calls_list:
                    if phonecall.played and not phonecall.currently_expired:
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


## The label that is called to begin and end a timeline item
label play_timeline_item():
    $ begin_timeline_item(current_timeline_item)
    $ print_file("Got to play_timeline_item with", current_timeline_item.item_label,
        "Which has been played:", current_timeline_item.played)
    # Call the item label so that it returns here when it's done
    if isinstance(current_timeline_item, ChatRoom):
        $ print_file("This item is a ChatRoom")
        if (current_timeline_item.expired
                and not current_timeline_item.played
                and not current_timeline_item.buyback):
            $ renpy.call(current_timeline_item.expired_label)
        elif (current_timeline_item.played
                and not store.persistent.testing_mode
                and len(current_timeline_item.replay_log) > 0):
            $ renpy.call('rewatch_chatroom')
        else:
            $ renpy.call(current_timeline_item.item_label)

    elif isinstance(current_timeline_item, StoryMode):
        $ print_file("This item is a StoryMode")
        if (not _in_replay and current_timeline_item.party
                and not renpy.has_label(
                    current_timeline_item.item_label + '_branch')):
            $ renpy.hide_screen('confirm')
            $ renpy.call('guest_party_showcase')
        elif current_timeline_item.party and not _in_replay:
            $ renpy.hide_screen('confirm')
            $ renpy.call(current_timeline_item.item_label + '_branch')
        else:
            $ renpy.call(current_timeline_item.item_label)

    elif isinstance(current_timeline_item, StoryCall):
        $ print_file("This item is a StoryCall. in_phone_call is", in_phone_call)
        if (current_timeline_item.expired
                and not current_timeline_item.buyback):
            $ renpy.show_screen('in_call', who=current_timeline_item.caller,
                story_call=True)
            $ renpy.call(current_timeline_item.expired_label)
        else:
            if not current_timeline_item.played and not _in_replay:
                play music persistent.phone_tone loop nocaption
                call screen incoming_call(phonecall=current_timeline_item)
            $ renpy.show_screen('in_call',
                who=current_timeline_item.caller, story_call=True)
            $ renpy.call(current_timeline_item.item_label)

    $ print_file("Finished the label and returned to play_timeline_item")
    if (not dialogue_paraphrase and dialogue_picked != ""):
        $ say_choice_caption(dialogue_picked, dialogue_paraphrase, dialogue_pv)
    $ end_timeline_item_checks()

    if isinstance(current_timeline_item, ChatRoom):
        call screen save_and_exit()
        if not observing:
            call screen signature_screen(True)
    elif isinstance(current_timeline_item, StoryMode):
        call screen signature_screen(False)

    if observing and not _in_replay:
        $ observing = False
        $ reset_story_vars()
        call screen timeline(current_day, current_day_num)
        return

    $ finish_timeline_item(current_timeline_item)

    if starter_story:
        $ starter_story = False
        call screen chat_home
        return
    call screen timeline(current_day, current_day_num)
    return

init python:
    ## Set up the correct variables and screens to view this TimelineItem.
    def begin_timeline_item(item, clearchat=True, resetHP=True, stop_music=True):
        # renpy.scene()
        # renpy.exports.show(name='bg', what=Solid(FUCHSIA))

        if store.starter_story:
            set_name_pfp()
        if stop_music:
            renpy.music.stop(channel='music')

        # Set this item as the current timeline item
        # current_timeline_item = item

        # Reset heart points
        if resetHP:
            store.collected_hp = {'good': [], 'bad': [], 'break': []}

        renpy.hide_screen('starry_night')
        renpy.hide_screen('animated_bg')
        renpy.hide_screen('timeline')
        hide_all_popups()

        store.text_msg_reply = False
        store.in_phone_call = False
        store.vn_choice = False
        store.email_reply = False

        # Special variable is set when rewatching an item to prevent changing
        # what was said or receiving heart points again, for example.
        if item not in [store.generic_chatroom, store.generic_storycall,
                store.generic_storymode]:
            if item.played:
                if not store.persistent.testing_mode:
                    store.observing = True
                else:
                    store.observing = False
            else:
                store.observing = False

        # If watching this item from the History, observing is always True.
        # Pronouns, name, and profile picture must be re-set and all characters'
        # profile pictures should be the default
        if store._in_replay:
            store.observing = True
            set_pronouns()
            set_name_pfp()
            for c in store.all_characters:
                c.reset_pfp()
            if store.expired_replay:
                item.expired = True

        print_file("Beginning timeline item with", item.item_label, "which is a",
            "chatroom?", isinstance(item, ChatRoom), "StoryMode?",
            isinstance(item, StoryMode), "StoryCall?", isinstance(item, StoryCall))
        # Chatroom setup
        if isinstance(item, ChatRoom):
            # Make sure messenger screens are showing
            renpy.show_screen('phone_overlay')
            renpy.show_screen('messenger_screen')
            renpy.show_screen('pause_button')

            # Clear the chatlog
            if clearchat:
                store.chatlog = []
                # Fill the beginning of the chat with 'empty space' so messages
                # appear at the bottom of the screen
                addchat(filler, "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", 0)

            store.text_person = None
            store._window_hide()

            # Set up the participants list
            if resetHP:
                store.in_chat = []
                if not store.observing:
                    item.reset_participants()
                for person in item.original_participants:
                    if person.name not in store.in_chat:
                        store.in_chat.append(person.name)

                # If the player is participating, add them to the
                # participants list
                if ((not item.expired or item.buyback or item.buyahead)
                        and not expired_replay):
                    store.in_chat.append(m.name)


        # Story Mode/VN setup
        elif isinstance(item, StoryMode):
            store._window_auto = True
            renpy.scene()
            renpy.show('bg black')

            renpy.hide_screen('phone_overlay')
            renpy.hide_screen('messenger_screen')
            renpy.hide_screen('pause_button')

            if item.is_nvl:
                nvl_clear()
            else:
                renpy.show_screen('vn_overlay')

            store.vn_choice = True
            # Clear the history log screen
            store._history_list = []
            store.history = True

            preferences.afm_enable = False #Preference('auto-forward', 'disable')

        # Story phone calls
        elif isinstance(item, StoryCall):
            store._history = False
            store.in_phone_call = True
            preferences.afm_enable = True
            store.current_call = item

            renpy.hide_screen('incoming_call')
            renpy.hide_screen('outgoing_call')


        renpy.retain_after_load()
        return

    ## Perform additional logic to finish off a TimelineItem, like resetting
    ## story variables to return to the menu screens.
    def end_timeline_item_checks():
        if store._in_replay:
            return

        if store.starter_story:
            store.persistent.first_boot = False
            store.persistent.on_route = True

        # First, ensure most_recent_item is not None
        if (store.most_recent_item is None
                and store.story_archive
                and store.story_archive[0].archive_list):
            store.most_recent_item = store.story_archive[0].archive_list[0]
        # Warn the user if no TimelineItems could be found
        elif store.most_recent_item is None:
            store.most_recent_item = ChatRoom('Example Chatroom',
                'example_chat', '00:01')
            print("WARNING: Could not find any TimelineItems for this route.")
            renpy.show_screen('script_error',
                message="Could not find any TimelineItems for this route.")

        return


    ## Finish resetting variables and screens for this TimelineItem.
    def finish_timeline_item(item, deliver_messages=True):

        # renpy.scene()
        # renpy.exports.show(name='bg', what=Solid(AQUA))

        # This item simply ends if the user is in Replay
        if _in_replay:
            renpy.end_replay()

        # Determine collected heart points (HP)
        store.persistent.HP += get_collected_hp()
        store.collected_hp = {'good': [], 'bad': [], 'break': []}
        # Give the player their hourglasses
        store.persistent.HG += store.collected_hg
        store.collected_hg = 0

        # Mark the most recent item as played
        if not item.parent:
            # This is the 'parent' item
            the_parent = item
        else:
            the_parent = item.parent

        # If the program was able to successfully mark the next item played,
        # then this is the most recent item if the player didn't buy it
        # back and it isn't the intro
        if (not store.starter_story
                and the_parent.mark_next_played()
                and not item.buyback):
            store.most_recent_item = the_parent

        # Deliver post-item content if this is not the last item before
        # a plot branch
        if item.get_item_before_branch():
            print_file("\n   And the item before the branch is:", item.get_item_before_branch().item_label)
        if deliver_messages and (not item == item.get_item_before_branch()):
            # Switch off variables so the program can deliver text messages
            store.vn_choice = False
            store.in_phone_call = False
            store.current_call = False
            item.call_after_label(True)
            item.deliver_calls()

        # Next, deliver emails and unlock the next story item
        deliver_emails()
        check_and_unlock_story()

        # Ensure any seen CGs are unlocked
        check_for_CGs(all_albums)

        # Save variables
        renpy.retain_after_load()

        # Check to see if honey buddha chips should be available
        if not store.chips_available:
            store.chips_available = hbc_bag.draw()

        deliver_next()

        # Reset variables
        reset_story_vars(item)
        return


## The label that is called when the program exits out of a timeline item
## early, expiring it
label exit_item_early():
    # This ends replays and resets variables
    # This item is only set as the most recent item if the player wasn't
    # replaying it
    $ end_timeline_item_checks()
    if not observing and (not current_timeline_item.expired
            or current_timeline_item.buyback):
        # Item expires
        $ expire_timeline_item(current_timeline_item)
    else:
        $ observing = False
    # Pop the return to play_timeline_item
    $ renpy.pop_call()
    $ reset_story_vars(current_timeline_item)
    call screen timeline(current_day, current_day_num)
    return


init python:
    ## Expire this timeline item and set the appropriate variables.
    ## This is a label and not a python function for performance reasons.
    def expire_timeline_item(item):

        # Get the parent of this item
        if not item.parent:
            the_parent = item
        else:
            the_parent = item.parent

        # This item expires
        item.expire()

        # Remove any heart points the player earned during this item
        rescind_collected_hp()
        # Hourglasses aren't added to the player's totals until the end,
        # so they can simply be reset
        store.collected_hg = 0

        # Deliver post-item content if it isn't the item immediately
        # prior to a plot branch
        if item == item.get_item_before_branch():
            item.call_after_label(True)
            item.deliver_calls()
            deliver_all_texts()

        renpy.retain_after_load()


        return

## The label that is called to play text messages
label play_text_message():
    # text_person should be set before the program gets here
    # Make sure variables are okay?
    $ print_file("Got to play text message")
    python:
        try:
            print_file("text_msg_reply is", text_msg_reply)
            print_file("For text messages, text_person is ", text_person.file_id)
        except:
            print_file("ERROR: Couldn't get text person")
    # $ text_message_begin()
    # TODO: check if they have a label to jump to?
    if text_person.real_time_text:
        show screen text_message_screen(text_person)
        show screen text_pause_button
    $ renpy.call(text_person.text_label)
    $ print_file("Returned from text message label")
    python:
        if (not dialogue_paraphrase and dialogue_picked != ""):
            say_choice_caption(dialogue_picked,
                dialogue_paraphrase, dialogue_pv)
        if text_person is not None and text_person.real_time_text:
            text_pauseFailsafe(text_person.text_msg.msg_list)
        text_msg_reply = False
        if text_person is not None:
            text_person.finished_text()
        # Determine collected heart points (HP)
        persistent.HP += get_collected_hp()
        collected_hp = {'good': [], 'bad': [], 'break': []}
        # Give the player their hourglasses
        persistent.HG += collected_hg
        collected_hg = 0
        textbackup = ChatEntry(filler,"","")
        who = text_person
        text_person = None
        renpy.retain_after_load()
    hide screen text_answer
    hide screen inactive_text_answer
    hide screen text_play_button
    hide screen text_pause_button
    if who is None:
        call screen timeline(current_day, current_day_num)
        return
    call screen text_message_screen(who, animate=False)
    return

## The label that is called to play a (non-story) phone call
label play_phone_call():
    $ print_file("Got to play phone call")
    if starter_story:
        $ set_name_pfp()
    stop music
    # This stops it from recording the dialogue
    # from the phone call in the history log
    $ _history = False
    $ in_phone_call = True
    hide screen incoming_call
    hide screen outgoing_call

    # Hide all the popup screens
    $ hide_all_popups()

    if _in_replay:
        $ observing = True
        $ set_name_pfp()
        $ set_pronouns()
    $ print_file("Also, in_phone_call is", in_phone_call)
    show screen in_call(current_call.caller, isinstance(current_call, StoryCall))
    if not starter_story:
        # Play the phone call
        $ print_file("About to call the label")
        $ renpy.call(current_call.phone_label)
        if (not dialogue_paraphrase and dialogue_picked != ""):
            $ say_choice_caption(dialogue_picked,
                dialogue_paraphrase, dialogue_pv)
        $ print_file("Returned from the phone call")
        $ renpy.end_replay()
        if not observing:
            $ current_call.finished()
            $ persistent.completed_story.add(current_call.phone_label)
        $ in_phone_call = False
        $ current_call = False
        $ observing = False
        $ _history = True
        $ renpy.retain_after_load()
        call screen phone_calls
    return

## Execute the plot branch for the given item.
label execute_plot_branch():

    $ most_recent_item = current_timeline_item
    $ item = current_timeline_item

    $ renpy.call(item.item_label + '_branch')

    # CASE 1:
    # Plot branch is actually the party
    if (isinstance(item, StoryMode) and item.party):
        # Need to send them to the party
        jump guest_party_showcase
        return

    # CASE 2
    # Can deliver the after_ contents of the item immediately before
    # the plot branch
    if not item.all_available():
        $ item.unlock_all()
    # Deliver content in after_ label as well as phone calls
    $ item.deliver_next_after_content()
    $ deliver_emails()

    # Now check if the player unlocked the next 24 hours
    # of chatrooms, and make those available
    if unlock_24_time:
        $ make_24h_available()
    $ check_and_unlock_story()
    $ renpy.retain_after_load
    call screen day_select
    return

## Label which shows the ending screen of the route and returns the player
## to the main menu
label end_route():
    if isinstance(current_timeline_item, ChatRoom):
        call screen save_and_exit()
    if not isinstance(current_timeline_item, StoryCall):
        call screen signature_screen(isinstance(current_timeline_item, ChatRoom))

    $ reset_story_vars()
    if ending == 'good':
        scene bg good_end
    elif ending == 'normal':
        scene bg normal_end
    elif ending == 'bad':
        scene bg bad_end
    else:
        scene
        show expression ending
    $ ending = False
    $ finish_timeline_item(current_timeline_item, deliver_messages=False)
    pause
    jump restart_game


init python:
    def text_message_begin(text_person):
        store.text_person = text_person
        store.CG_who = store.text_person
        if text_person.text_msg.reply_label:
            store.text_msg_reply = True
        store.text_person.text_msg.read = True
        renpy.retain_after_load()
        return

    def get_collected_hp():
        """Return the total number of heart points earned in a chatroom."""

        return (len(store.collected_hp['good'])
                    + len(store.collected_hp['bad'])
                    - len(store.collected_hp['break']))

    def rescind_collected_hp():
        """Resets the heart points earned during this chatroom."""

        global collected_hp

        for chara in collected_hp['good']:
            chara.decrease_heart()
        for chara in collected_hp['bad']:
            chara.heart_points -= 1
            chara.bad_heart -= 1
        for chara in collected_hp['break']:
            chara.increase_heart()

        # Remove points from persistent.HP
        store.persistent.HP -= get_collected_hp()

        # Reset collected_hp
        collected_hp = {'good': [], 'bad': [], 'break': []}


    def reset_story_vars(vn_jump=False):
        """
        Reset variables associated with the current item, such as hiding
        chatroom screens and resetting collected heart point totals.
        """

        renpy.scene()
        renpy.exports.show(name='bg', what=Solid(BLACK))

        if not vn_jump:
            renpy.music.stop()

        config.skipping = False
        config.skipping = False
        store.choosing = False

        # Switch off variables
        store.vn_choice = False
        store.in_phone_call = False
        store.current_call = False
        store._history = True

        # Hide chatroom screens
        renpy.hide_screen('phone_overlay')
        renpy.hide_screen('in_call')
        renpy.hide_screen('save_and_exit')
        renpy.hide_screen('play_button')
        renpy.hide_screen('answer_button')
        renpy.hide_screen('pause_button')
        renpy.hide_screen('messenger_screen')
        renpy.hide_screen('animated_bg')
        renpy.hide_screen('vn_overlay')
        hide_all_popups()


    def custom_show(name, at_list=None, layer='master', what=None,
            zorder=0, tag=None, behind=None, **kwargs):
        """
        A custom statement which replaces the default `show` statement in order
        to work with chatrooms.

        Parameters:
        -----------
        name : string
            The name of the image to show.
        at_list : transforms[]
            A list of transforms that are applied to the image. The equivalent
            of the `at` property.
        layer : string
            Gives the name of the layer on which the image will be shown. The
            equivalent of the `onlayer` property. If None, uses the default
            layer associated with the tag.
        what : Displayable or None
            A displayable that will be shown in lieu of looking on the image.
            (The equivalent of the `show expression` statement). When a `what`
            parameter is given, `name` can be used to associate a tag with
            the image.
        zorder : int
            The equivalent of the `zorder` property. If None, the zorder is
            preserved if it exists, and is otherwise set to 0.
        tag : string
            Specifies the image tag of the shown image. The equivalent of the
            `as` property.
        behind : string[]
            A list of image tags that this image is shown behind. The equivalent
            of the `behind` property.

        Result:
        -------
            Displays the image on the screen according to the given parameters.
        """

        # This helps paraphrasing to work with VN mode
        if (not store.dialogue_paraphrase and store.dialogue_picked != ""):
            say_choice_caption(store.dialogue_picked,
                store.dialogue_paraphrase, store.dialogue_pv)

        # The scrolling hack effect should be shown
        if ('hack' in name and 'effect' in name
                and renpy.get_screen('messenger_screen')
                and not at_list):
            renpy.call('hack')
            return
        elif ('redhack' in name and 'effect' in name
                and renpy.get_screen('messenger_screen')
                and not at_list):
            renpy.call('redhack')
            return
        ## Banners
        elif ('lightning' in name and 'banner' in name
                and renpy.get_screen('messenger_screen')
                and not at_list):
            renpy.call('banner', banner='lightning')
            return
        elif ('well' in name and 'banner' in name
                and renpy.get_screen('messenger_screen')
                and not at_list):
            renpy.call('banner', banner='well')
            return
        elif ('annoy' in name and 'banner' in name
                and renpy.get_screen('messenger_screen')
                and not at_list):
            renpy.call('banner', banner='annoy')
            return
        elif ('heart' in name and 'banner' in name
                and renpy.get_screen('messenger_screen')
                and not at_list):
            renpy.call('banner', banner='heart')
            return
        ## The shake effect
        elif ( name == ('shake',)
                and renpy.get_screen('messenger_screen')
                and not at_list):
            renpy.call('shake')
            return


        ## Chatroom backgrounds
        elif (not name == ('bg', 'black')
                and renpy.get_screen('messenger_screen')
                and not at_list):
            # The messenger screen is showing, therefore this statement is
            # likely being used in conjunction with `scene` to display a
            # chatroom background
            print('Using custom show statement with', name)
            if isinstance(name, tuple) and name[0] == 'bg':
                set_chatroom_background(name[1])
            elif isinstance(name, tuple):
                set_chatroom_background(name[0])
            else:
                set_chatroom_background(name)
            return

        at_list = at_list or []
        behind = behind or []

        renpy.exports.show(name, at_list, layer, what, zorder, tag, behind, **kwargs)

    def custom_hide(name, layer=None):
        """
        A custom statement which replaces the default `hide` statement for
        compatibility with other program features such as menu paraphrasing.

        Parameters:
        -----------
        name : string
            The name of the image to hide. Only the image tag is used, and any
            image with the tag is hidden (the precise name does not matter).
        layer : string
            The layer on which this function operates. If None, uses the
            default layer associated with the tag.

        Result:
        -------
            Executes a say statement for the main character if applicable and
            hides the given image.
        """

        # This helps paraphrasing to work with VN mode
        if (not store.dialogue_paraphrase and store.dialogue_picked != ""):
            say_choice_caption(store.dialogue_picked,
                store.dialogue_paraphrase, store.dialogue_pv)

        renpy.hide(name, layer)

    # Some colour names, mostly for testing
    WHITE = "#FFF"
    BLACK = "#000"
    SILVER = "#c0c0c0"
    GRAY = "#808080"
    RED = "#F00"
    MAROON = "#800000"
    YELLOW = "#FF0"
    OLIVE = "#808000"
    LIME = "#0F0"
    GREEN = "#008000"
    AQUA = "#0FF"
    TEAL = "#008080"
    BLUE = "#00F"
    NAVY = "#000080"
    FUCHSIA = "#F0F"
    PURPLE= "#800080"

define config.show = custom_show
define config.hide = custom_hide