## This file contains deprecated functions, classes, screens, and labels
## that are no longer required for the current version of Mysterious Messenger
## but are maintained here for backwards compatibility. Use of old features
## often results in a printout to the console but no averse in-game effects.

init python:

    # Renamed to next_story_time
    def next_chat_time():
        print("WARNING: Deprecated function next_chat_time used.")
        return next_story_time()

    # Renamed to make_24h_available
    def chat_24_available():
        print("WARNING: Deprecated function chat_24_available used.")
        return make_24h_available()

    # Renamed to check_and_unlock_story
    def next_chatroom():
        print("WARNING: Deprecated function next_chatroom used.")
        return check_and_unlock_story()

    # Renamed to num_future_timeline_items
    def num_future_chatrooms(break_for_branch=False):
        print("WARNING: Deprecated function num_future_chatrooms used.")
        return num_future_timeline_items(break_for_branch)

    # Renamed to reset_story_vars
    def reset_chatroom_vars(for_vn=False):
        print("WARNING: Deprecated function reset_chatroom_vars used.")
        return reset_story_vars(for_vn)

    ## Split into several functions; most similar to finish_timeline_item
    def post_chat_actions(deliver_messages=True):
        return finish_timeline_item(store.current_timeline_item,
            deliver_messages=deliver_messages)

# Displays notifications instead of heart icons
# Replaced with persistent.animated_icons
default persistent.heart_notifications = False

## Deprecated; replaced with `invite guest_var`. You can call this label with
## `call invite(guest_var)` and it will trigger the guest to email the player.
label invite(guest):
    $ print("WARNING: Deprecated label invite(guest) used.")
    invite guest
    return

# Deprecated; replaced with `award heart u` where `u` is the character to award
# the heart for. Call this to display the heart icon for a given character
label heart_icon(character, bad=False):
    $ print("WARNING: Deprecated label heart_icon(character) used.")
    if bad:
        award heart character bad
    else:
        award heart character
    return

# Deprecated; replaced with `break heart u` where `u` is the character to
# remove a heart for. Like the heart icon, call this to display the heart break.
label heart_break(character):
    $ print("WARNING: Deprecated label heart_break(character) used.")
    break heart character
    return


## Deprecated; replaced with `exit_item_early`. Determines what happens
## when the 'back' button is pressed during a chatroom.
label chat_back():
    jump exit_item_early


#************************************
# Chatroom Enter/Exit
#************************************
# This does some of the code for you when you want a character
# to enter/exit a chatroom. It adds characters to the chatroom's
# participant list if they enter during a chatroom.

# Deprecated; replaced with `enter chatroom u` where `u` is the
# character entering the chatroom
label enter(chara):
    $ print("WARNING: Deprecated label enter(chara) used.")
    enter chatroom chara
    return

# Deprecated; replaced with `exit chatroom u` where `u` is the character
# exiting the chatroom
label exit(chara):
    $ print("WARNING: Deprecated label exit(chara) used.")
    exit chatroom chara
    return

#************************************
# Play audio/music/SFX
#************************************
# This allows the program to keep track of when to play
# music during a chatroom or VN. This call has now been integrated
# into a CDS but is left in for backwards compatibility
label play_music(file):
    play music file loop
    return

## This label plays sound effects and also shows an audio
## caption if the player has that option turned on.
## This call has now been integrated into a CDS but is left in
## for backwards compatibility
label play_sfx(sfx):
    play sound sfx
    return



init -6 python:

    ## Deprecated classes for route setup
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
                # print_file("ChatHistory getattr with", name)
                # if name == 'chatroom_label':
                #     raise AttributeError(name)
                # print_file("with", self.__dict__['chatroom_label'])
                return super(ChatHistory, self).__getattribute__(name)
            except (KeyError, AttributeError) as e:
                raise AttributeError(name)

        def add_participant(self, chara):
            """Add a participant to the chatroom."""

            if not (chara in self.participants):
                print_file("added", chara.name, "to the participants list of", self.title)
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

            try:
                # print_file("VNMode getattr with", name)
                # if name == 'vn_label':
                #     raise AttributeError(name)
                # print_file("with", self.__dict__['vn_label'])
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