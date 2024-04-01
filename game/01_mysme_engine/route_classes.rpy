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
        choices : string[]
            A list of the choices that were made when the player played this
            StoryMode.
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
                try:
                    new_branch = PlotBranch(plot_branch.vn_after_branch)
                    new_branch.story_mode = plot_branch.stored_vn
                    self.plot_branch = new_branch
                except:
                    self.plot_branch = plot_branch
            elif plot_branch:
                # plot branch should have branch_story_mode=True
                self.plot_branch = PlotBranch(True)
            else:
                self.plot_branch = PlotBranch(False)

            # Ensure the trigger time is set up properly
            # It corrects times like 3:45 to 03:45
            if trigger_time and ':' in trigger_time[:2]:
                self._trigger_time = '0' + trigger_time
            else:
                self._trigger_time = trigger_time

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
            elif save_img.startswith("save_"):
                self.save_img = save_img[5:]
            else:
                # e.g. auto / another / april / casual / deep / xmas
                self.save_img = save_img

            self.played = False
            self.available = False
            self.expired = False
            self.buyback = False
            self.buyahead = False
            self.parent = None
            self.choices = []
            self.delivered_post_items = False

            self.expired_label = None
            self.after_label = None
            self.phonecall_label = None
            self.outgoing_calls_list = [ ]
            self.incoming_calls_list = [ ]
            self.story_calls_list = [ ]

            if self.item_label is not None:
                self.set_label(self.item_label)


        def set_label(self, lbl):
            """Set a new item label for this TimelineItem."""

            self.item_label = lbl

            self.expired_label = lbl + "_expired"
            self.after_label = "after_" + self.item_label
            self.phonecall_label = self.item_label

            all_call_list = list(store.all_characters)
            all_call_list.extend(store.phone_only_characters)
            self.outgoing_calls_list = [ (self.item_label + '_outgoing_'
                + x.file_id) for x in all_call_list
                if renpy.has_label(self.item_label + '_outgoing_'
                    + x.file_id)]
            self.incoming_calls_list = [ (self.item_label + '_incoming_'
                + x.file_id) for x in all_call_list
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

        @property
        def all_available(self):
            """
            Return True if everything associated with this item is available.
            """

            if self.parent:
                return self.parent.all_available

            if not self.available:
                return False
            if len(self.story_calls_list) > 0:
                for phonecall in self.story_calls_list:
                    if not phonecall.available:
                        return False
            return True

        @property
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

        def mark_self_played(self):
            """
            Mark this item as played. Return True if this was successful.
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

            return False

        @property
        def on_available_message(self):
            """
            Return a message to display to the player when this item
            is available.
            """
            return "[[new story available]"

        @property
        def can_expire(self):
            """Return True if there are items that can be expired."""

            print_file("Can", self.item_label, "expire?")

            if not self.played and not self.buyahead and not self.buyback:
                print_file("Yes it can expire", self.played, self.buyahead, self.buyback)
                return True

            if len(self.story_calls_list) > 0:
                for phonecall in self.story_calls_list:
                    if phonecall.can_expire:
                        print_file("Yes it can expire", self.played, self.buyahead, self.buyback)
                        return True
            print_file("No it can't expire", self.played, self.buyahead, self.buyback)
            return False

        def deliver_next_after_content(self):
            """
            Ensure all played items have had their content delivered after a
            plot branch.
            """

            if self.played and (not self.delivered_post_items
                    or store.persistent.testing_mode):
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
            self.choices = []

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

            return (self.played_regular or self.played_expired)

        @property
        def final_item(self):
            """Return the final item to be played in this timeline item."""

            if self.plot_branch and self.plot_branch.branch_story_mode:
                return self.plot_branch.story_mode

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
            if not self.plot_branch:
                return None
            if len(self.story_calls_list) > 0:
                return self.story_calls[-1]
            return self

        def timeline_img(self, was_played=True):
            """
            Return the hover image that should be used for this item.
            was_played is True if any prior items were played first.
            """
            print_file("WARNING: Got default timeline image")
            return "#59efc7"

        @property
        def played_regular(self):
            """Return True if the regular label of this item has been played."""

            return self.item_label in store.persistent.completed_story

        @property
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

            renpy.retain_after_load()
            if self.plot_branch:
                return False
            return True

        def buy_back(self):
            """Make this item available again after it expired."""

            self.buyback = True
            self.played = False
            self.choices = []

            renpy.retain_after_load()


        def call_after_label(self, new_context=True):
            """Call this item's after_ label, if it exists."""

            if self.delivered_post_items and not store.persistent.testing_mode:
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

        @property
        def time_of_day(self):
            """
            Return the time of day which corresponds to this timeline item's
            trigger time.
            """

            trig = self.trigger_time
            hour = trig[:2]
            try:
                hour = int(hour)
            except Exception as e:
                return 'black'

            if hour < 6:
                # Early Morning 0:00-5:59
                return 'earlyMorn'
            elif hour < 10:
                # Morning 6:00 - 9:59
                return 'morning'
            elif hour < 17:
                # Afternoon 10:00 - 16:59
                return 'noon'
            elif hour < 20:
                # Evening 17:00 - 19:59
                return 'evening'
            else:
                # Night greeting 20:00 - 23:59
                return 'night'


        @property
        def trigger_time(self):
            """Return the trigger time of this item or its parent."""

            try:
                if self._trigger_time:
                    return self._trigger_time
            except:
                pass
            try:
                if self.__trigger_time:
                    return self.__trigger_time
            except:
                pass

            if self.parent and self.parent.trigger_time:
                return self.parent.trigger_time
            else:
                try:
                    if self.__dict__.get('trigger_time', False):
                        return self.__dict__.get('trigger_time')
                except:
                    pass
                ScriptError("Could not determine the time for the timeline",
                    "item at \"", self.item_label, '"',
                    header="route-setup", subheader="Adding Timeline Items")
                return "24:00"

        @trigger_time.setter
        def trigger_time(self, new_time):
            """Set the trigger time."""

            self._trigger_time = new_time

        def get_trigger_time(self):
            try:
                return self._trigger_time
            except:
                self._trigger_time = self.__trigger_time
                return self._trigger_time

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
            return num_played, total

        @property
        def currently_expired(self):
            """Return if this item is currently expired."""
            return (self.expired and not self.buyback)

        def add_to_choices(self, choice):
            """Add choice to the list of choices."""

            if not self.currently_expired and not store.observing:
                self.choices.append(choice)

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
                    or self.trigger_time != other.trigger_time)


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
        box_bg : string
            One of either "secure" or "colorhack". Causes an extra image to
            be shown under the timeline image box.
        """

        def __init__(self, title, chatroom_label, trigger_time,
                participants=None, story_mode=None, plot_branch=None,
                save_img='auto', box_bg=None):
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
            box_bg : string
                One of either "secure" or "colorhack". Causes an extra image to
                be shown under the timeline image box.
            """

            self.story_mode = None
            super(ChatRoom, self).__init__(title, chatroom_label, trigger_time,
                plot_branch, save_img)

            self.participants = participants or []
            if len(self.participants) == 0:
                self.original_participants = []
            else:
                self.original_participants = list(participants)

            self.box_bg = box_bg

            if story_mode:
                self.story_mode = story_mode
            elif self.item_label is not None:
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

            if self.item_label is not None:
                self.set_label(self.item_label)

            self.participated = False
            self.replay_log = []

        @property
        def timeline_box_bg(self):
            """Return the chat box background for this image."""

            try:
                if self.box_bg:
                    return 'chat_' + self.box_bg + '_box'
            except:
                pass
            return None

        def set_label(self, lbl):
            """Set a new item label for this TimelineItem."""

            super(ChatRoom, self).set_label(lbl)

            if self.story_mode is None:
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

        @property
        def party(self):
            if not self.story_mode:
                return False
            return self.story_mode.party

        def unlock_all(self):
            """Ensure all items associated with this chatroom are available."""

            super(ChatRoom, self).unlock_all()
            if self.story_mode:
                self.story_mode.available = True

        @property
        def all_available(self):
            """
            Return True if everything associated with this item is available.
            """

            if self.story_mode and not self.story_mode.available:
                return False
            return super(ChatRoom, self).all_available

        @property
        def all_played(self):
            """
            Return True if everything associated with this item has been
            played.
            """

            if self.story_mode and not self.story_mode.played:
                return False
            return super(ChatRoom, self).all_played

        @property
        def on_available_message(self):
            """
            Return a message to display to the player when this item
            is available.
            """

            return "[[new chatroom] " + self.title

        @property
        def final_item(self):
            """Return the final item to be played in this timeine item."""

            if self.plot_branch and self.plot_branch.vn_after_branch:
                return self.plot_branch.stored_vn

            if len(self.story_calls_list) > 0:
                return self.story_calls_list[-1]

            if self.story_mode:
                return self.story_mode

            return self

        def timeline_img(self, was_played=True):
            """
            Return the hover image that should be used for this item.
            was_played is True if any prior items were played first.
            """

            if store.persistent.unlock_all_story:
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

            if self.played and (not self.delivered_post_items
                    or store.persistent.testing_mode):
                self.call_after_label(True)
                self.deliver_calls()

            if self.story_mode and (not self.story_mode.delivered_post_items
                    or store.persistent.testing_mode):
                self.story_mode.deliver_next_after_content()

            super(ChatRoom, self).deliver_next_after_content()

        def mark_self_played(self):
            """
            Mark this item as played. Return True if this was successful.
            """

            successful = super(ChatRoom, self).mark_self_played()
            if not successful:
                return False
            # Otherwise, add the participants to a dictionary
            store.persistent.chatroom_participants[self.title] = [
                x.file_id for x in self.participants ]
            if not self.currently_expired:
                self.participated = True
            return True

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

        def buy_back(self):
            """Make this item available again after it expired."""

            self.replay_log = []
            self.reset_participants()
            super(ChatRoom, self).buy_back()

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

        @property
        def on_available_message(self):
            """
            Return a message to display to the player when this item
            is available.
            """

            return "[[new story mode] " + self.title

        def timeline_img(self, was_played=True):
            """
            Return the hover image that should be used for this item.
            was_played is True if any prior items were played first.
            """

            if store.persistent.unlock_all_story:
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

            return num_played, total




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

        @property
        def party(self):
            return False

        def timeline_img(self, was_played=True):
            """
            Return the hover image that should be used for this item.
            was_played is True if any prior items were played first.
            """

            if store.persistent.unlock_all_story:
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

        @property
        def on_available_message(self):
            """
            Return a message to display to the player when this item
            is available.
            """

            return "[[new story call] " + self.title

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

    def BranchStoryMode(vn_label, who=None, party=False):
        return StoryMode(title="", vn_label=vn_label, trigger_time=False,
            who=who, party=party)

## The label that is called to begin and end a timeline item
label play_timeline_item():
    $ begin_timeline_item(current_timeline_item)
    # Call the item label so that it returns here when it's done
    if isinstance(current_timeline_item, ChatRoom):
        if skip_story_item:
            pass
        elif (_in_replay and current_timeline_item.expired):
            $ renpy.call(current_timeline_item.expired_label)
        elif (_in_replay):
            $ renpy.call(current_timeline_item.item_label)
        elif (current_timeline_item.expired
                and not current_timeline_item.played
                and not current_timeline_item.buyback):
            ## Achievement for playing an expired chatroom
            if not expired_achievement.has():
                $ expired_achievement.grant()
                $ progress_stat_achievement.add_progress(1)
            ##
            $ renpy.call(current_timeline_item.expired_label)
        elif (current_timeline_item.played
                and not store.persistent.testing_mode
                and not store.persistent.unlock_all_story
                and len(current_timeline_item.replay_log) > 0):
            $ renpy.call('rewatch_chatroom')
        else:
            $ renpy.call(current_timeline_item.item_label)

    elif isinstance(current_timeline_item, StoryMode):
        if (not _in_replay and current_timeline_item.party
                and not renpy.has_label(
                    current_timeline_item.item_label + '_branch')):
            $ skip_story_item = False
            $ renpy.hide_screen('confirm')
            $ renpy.call('guest_party_showcase')
        elif current_timeline_item.party and not _in_replay:
            $ skip_story_item = False
            $ renpy.hide_screen('confirm')
            $ renpy.call(current_timeline_item.item_label + '_branch')
            $ renpy.call('guest_party_showcase')
        elif skip_story_item:
            pass
        else:
            $ renpy.call(current_timeline_item.item_label)

    elif isinstance(current_timeline_item, StoryCall):
        if skip_story_item:
            pass
        elif (_in_replay and current_timeline_item.expired):
            $ renpy.show_screen('in_call', who=current_timeline_item.caller,
                story_call=True)
            $ renpy.call(current_timeline_item.expired_label)
        elif (_in_replay):
            $ renpy.show_screen('in_call',
                who=current_timeline_item.caller, story_call=True)
            $ renpy.call(current_timeline_item.item_label)
        elif (current_timeline_item.expired
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

    if (not dialogue_paraphrase and dialogue_picked != ""):
        $ say_choice_caption(dialogue_picked, dialogue_paraphrase, dialogue_pv)

    if ending is not None:
        jump end_route

    $ end_timeline_item_checks()

    if not skip_story_item:
        if isinstance(current_timeline_item, ChatRoom) and gamestate != VNMODE:
            call screen save_and_exit()
            if not observing:
                call screen signature_screen(True)
        elif isinstance(current_timeline_item, StoryMode) or gamestate == VNMODE:
            call screen signature_screen(False)

        if observing and not _in_replay:
            $ observing = False
            $ reset_story_vars()
            call screen timeline(current_day, current_day_num)
            return
    else:
        $ skip_story_item = False

    $ finish_timeline_item(current_timeline_item)

    if starter_story:
        $ starter_story = False
        call screen chat_home
        return
    call screen timeline(current_day, current_day_num)
    return

init python:

    def begin_timeline_item(item, clearchat=True, resetHP=True, stop_music=True,
            is_vn=False):
        """
        Set up the correct variables and screens to view this TimelineItem.
        """

        # renpy.scene()
        # renpy.exports.show(name='bg', what=Solid(FUCHSIA))

        if store.starter_story:
            set_name_pfp()
        if stop_music:
            renpy.music.stop(channel='music')

        # Reset heart points
        if resetHP:
            store.collected_hp = {'good': [], 'bad': [], 'break': []}

        renpy.hide_screen('starry_night')
        renpy.hide_screen('animated_bg')
        renpy.hide_screen('screen_crack_overlay_bg')
        renpy.hide_screen('timeline')
        hide_all_popups()

        store.text_msg_reply = False
        store.in_phone_call = False
        store.vn_choice = False
        store.email_reply = False
        store.gamestate = None
        if item not in store.generic_timeline_items:
            store.current_choices = []
            store.current_call = None

        # Special variable is set when rewatching an item to prevent changing
        # what was said or receiving heart points again, for example.
        if item not in store.generic_timeline_items:
            if item.played:
                if not store.persistent.testing_mode:
                    store.observing = True
                else:
                    item.replay_log = [ ]
                    store.observing = False
            else:
                store.observing = False
                item.replay_log = [ ]

        # If watching this item from the History, observing is always True.
        # Pronouns, name, and profile picture must be re-set and all characters'
        # profile pictures should be the default
        if store._in_replay:
            store.observing = True
            set_name_pfp()
            for c in store.all_characters:
                c.reset_pfp()
            if store.expired_replay:
                item.expired = True
            else:
                item.expired = False

        # Only allow the player to pick choices they've seen on this playthrough
        if (store.observing and not store._in_replay
                and item not in store.generic_timeline_items):
            store.current_choices = list(item.choices)

        # Chatroom setup
        if isinstance(item, ChatRoom):
            store.gamestate = CHAT
            # Make sure messenger screens are showing
            renpy.show_screen('phone_overlay')
            renpy.show_screen('messenger_screen')
            renpy.show_screen('pause_button')
            store.gamestate = CHAT

            # Clear the chatlog
            if clearchat:
                store.chatlog = []
                # Fill the beginning of the chat with 'empty space' so messages
                # appear at the bottom of the screen
                addchat(filler, "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", 0)
                # Set up the "automatic" background (which can be replaced)
                set_chatroom_background('autobackground')
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
                        and not store.expired_replay):
                    store.in_chat.append(store.main_character.name)

        # Story Mode/VN setup
        elif isinstance(item, StoryMode):
            store._window_auto = True
            renpy.scene()
            renpy.show('bg black')

            renpy.hide_screen('phone_overlay')
            renpy.hide_screen('messenger_screen')
            renpy.hide_screen('pause_button')

            if item.is_nvl or is_vn:
                nvl_clear()
            else:
                renpy.show_screen('vn_overlay')

            store.gamestate = VNMODE
            # Clear the history log screen
            store._history_list = []
            store.history = True

            preferences.afm_enable = False

        # Story phone calls
        elif isinstance(item, StoryCall):
            renpy.scene()
            renpy.show('bg black')

            renpy.hide_screen('phone_overlay')
            renpy.hide_screen('messenger_screen')
            renpy.hide_screen('pause_button')

            store._history = False
            store.gamestate = PHONE
            preferences.afm_enable = True
            if not starter_story and not item == generic_storycall:
                store.current_call = item

            renpy.hide_screen('incoming_call')
            renpy.hide_screen('outgoing_call')


        renpy.retain_after_load()
        return



    def end_timeline_item_checks():
        """
        Perform additional logic to finish off a TimelineItem, like resetting
        story variables to return to the menu screens.
        """

        store.gamestate = None

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
            if not in_chat_creator:
                ScriptError("Could not find any TimelineItems for this route.",
                    link="route-setup", link_text="Setting up a Route")
        return


    def finish_timeline_item(item, deliver_messages=True):
        """Finish resetting variables and screens for this TimelineItem."""

        # This item simply ends if the user is in Replay
        if _in_replay:
            renpy.music.stop()
            renpy.end_replay()

        # Determine collected heart points (HP)
        store.persistent.HP += get_collected_hp()
        store.collected_hp = {'good': [], 'bad': [], 'break': []}
        # Give the player their hourglasses
        store.persistent.HG += store.collected_hg
        store.collected_hg = 0

        # Silently deliver any temporary text messages
        send_temp_texts()

        # Mark the most recent item as played
        if not item.parent:
            # This is the 'parent' item
            the_parent = item
        else:
            the_parent = item.parent

        # If this item hasn't been played before, then this is the most
        # recent item if the player didn't buy it back and it isn't the intro
        if (not store.starter_story
                and item.mark_self_played()
                and not item.buyback):
            store.most_recent_item = the_parent

        # Check to see if honey buddha chips should be available
        if not store.chips_available:
            store.chips_available = hbc_bag.draw()

        # Ensure any seen CGs are unlocked
        check_for_CGs(all_albums)

        # Reset variables and hide screens
        reset_story_vars()

        # Deliver post-item content if this is not the last item before
        # a plot branch
        if deliver_messages and (not item == item.get_item_before_branch()):
            item.call_after_label(True)
            item.deliver_calls()

        # Next, deliver emails and unlock the next story item
        deliver_emails()
        if not store.starter_story:
            check_and_unlock_story()

        store.dialogue_picked = ""
        store.dialogue_paraphrase = store.paraphrase_choices
        store.dialogue_pv = 0

        # Save variables
        renpy.retain_after_load()

        if not store.starter_story:
            deliver_next()
        return


## The label that is called when the program exits out of a timeline item
## early, expiring it
label exit_item_early():
    if is_main_menu_replay:
        jump chatroom_creator_setup
    # This ends replays and resets variables.
    # This item is only set as the most recent item if the player wasn't
    # replaying it.
    $ end_timeline_item_checks()
    $ reset_story_vars()
    $ renpy.end_replay()
    $ purge_temp_texts()
    if not observing and (not current_timeline_item.expired
            or current_timeline_item.buyback):
        # Item expires
        $ expire_timeline_item(current_timeline_item)
    else:
        $ observing = False
    # Pop the return to play_timeline_item
    if len(renpy.get_return_stack()) > 0:
        $ renpy.pop_call()
    call screen timeline(current_day, current_day_num)
    return


init python:
    def expire_timeline_item(item):
        """Expire this timeline item and set the appropriate variables."""

        # This item expires
        item.expire()

        # Remove any heart points the player earned during this item
        rescind_collected_hp()
        # Hourglasses aren't added to the player's totals until the end,
        # so they can simply be reset
        store.collected_hg = 0

        # Deliver post-item content if it isn't the item immediately
        # prior to a plot branch
        if item != item.get_item_before_branch():
            item.call_after_label(True)
            item.deliver_calls()
            deliver_all_texts()

        renpy.retain_after_load()

        return


## Execute the plot branch for the given item.
label execute_plot_branch():

    $ most_recent_item = current_timeline_item
    $ item = current_timeline_item

    $ renpy.call(item.item_label + '_branch')

    # Ensure continue_route() is run to resolve the plot branch
    $ continue_route()

    # CASE 1:
    # Plot branch is actually the party
    if (isinstance(item, StoryMode) and item.party):
        # Need to send them to the party
        jump guest_party_showcase

    # CASE 2
    # Can deliver the after_ contents of the item immediately before
    # the plot branch
    if not item.all_available:
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
    $ is_chat = False
    if (isinstance(current_timeline_item, ChatRoom)
            and not (gamestate in (PHONE, VNMODE))):
        call screen save_and_exit()
        $ is_chat = True
    if not isinstance(current_timeline_item, StoryCall):
        call screen signature_screen(is_chat)

    $ reset_story_vars()
    $ finish_timeline_item(current_timeline_item, deliver_messages=False)
    if ending == 'good':
        scene bg good_end
    elif ending == 'normal':
        scene bg normal_end
    elif ending == 'bad':
        scene bg bad_end
    else:
        scene
        show expression ending
    pause 10.0
    $ ending = None
    jump restart_game

label end_prologue():
    $ define_variables()
    if gamestate not in (PHONE, VNMODE):
        # It's a chatroom
        $ chat = True
    else:
        $ chat = False
    if ending is not None:
        jump end_route
    $ end_timeline_item_checks()
    if chat:
        call screen save_and_exit()
    call screen signature_screen(chat)
    $ finish_timeline_item(current_timeline_item)
    $ starter_story = False
    $ check_and_unlock_story()
    $ deliver_next()
    call screen chat_home
    return

init python:
    def get_collected_hp():
        """Return the total number of heart points earned in a chatroom."""

        good = sum([ amt for who, amt in store.collected_hp['good'] ])
        bad = sum([ amt for who, amt in store.collected_hp['bad'] ])
        breakh = sum([ amt for who, amt in store.collected_hp['break'] ])
        return (good + bad + breakh)

    def rescind_collected_hp():
        """Resets the heart points earned during this chatroom."""

        global collected_hp

        for chara, amount in collected_hp['good']:
            chara.decrease_heart(amount=amount)
        for chara, amount in collected_hp['bad']:
            chara.heart_points -= amount
            chara.bad_heart -= amount
        for chara, amount in collected_hp['break']:
            chara.increase_heart(amount=amount)

        # Remove points from persistent.HP
        store.persistent.HP -= get_collected_hp()

        # Reset collected_hp
        collected_hp = {'good': [], 'bad': [], 'break': []}

    def reset_story_vars(vn_jump=False):
        """
        Reset variables associated with the current item, such as hiding
        chatroom screens and resetting collected heart point totals.
        """

        # Hide all screens and images
        renpy.scene()
        renpy.scene(layer='animated_bg')
        renpy.scene(layer='screens')
        renpy.exports.show(name='load', what=Solid(BLACK))

        if not vn_jump:
            renpy.music.stop()
            store.current_choices = []

        renpy.music.stop('voice', fadeout=0.1)
        renpy.music.stop('voice_sfx', fadeout=0.1)
        renpy.music.stop('voice_sfx2', fadeout=0.1)
        renpy.music.stop('voice_sfx3', fadeout=0.1)

        config.skipping = False
        store.choosing = False
        store.chat_stopped = False

        # Switch off variables
        store.vn_choice = False
        store.in_phone_call = False
        store.gamestate = None
        store.current_call = False
        store._history = True
        store.block_interrupts = False
        store.answer_shown = False

        store.dialogue_picked = ""
        store.dialogue_paraphrase = store.paraphrase_choices
        store.dialogue_pv = 0

        store.recently_shown_heart = [ ]

        # Reset timed menus
        store.timed_menu_dict = { }
        store.c_menu_dict = { }
        store.on_screen_choices = 0
        store.recently_hidden_choice_screens = []
        store.last_shown_choice_index = None

