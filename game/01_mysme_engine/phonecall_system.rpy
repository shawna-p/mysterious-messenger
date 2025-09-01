python early:

    class PhoneCall():
        """
        Class that stores information needed to keep track of phone calls.

        Attributes:
        -----------
        caller : ChatCharacter
            ChatCharacter object of the other person in the phone call.
        phone_label : string
            The label to jump to for the phone call.
        call_time : upTime or False
            The time the phone call was made at.
        call_status : string
            Status of the phone call. One of 'incoming', 'outgoing', 'missed',
            or 'voicemail'.
        voicemail : bool
            True if this call is a voicemail message rather than a conversation.
            Not to be confused with voicemail_label, which contains the message
            a character will leave as a "voicemail" if this call is mandatory.
        playback : bool
            True if this conversation can be 'replayed' from the call history.
        avail_timeout : int
            How many chatrooms to wait until this call expires.
        choices : string[]
            A list of the choices the player selected when playing this call.
        """

        def __init__(self, caller, phone_label, call_status='incoming',
                avail_timeout=2, voicemail=False):
            """
            Creates a PhoneCall object to keep track of phone call information.

            Parameters:
            -----------
            caller : ChatCharacter
                ChatCharacter object of the other person in the phone call.
            phone_label : string
                The label to jump to for the phone call.
            call_status : string
                Status of the phone call. One of 'incoming', 'outgoing',
                'missed', or 'voicemail'.
            avail_timeout : int
                How many story items to wait until this call expires.
            voicemail : bool
                True if this call is a voicemail message rather than
                a conversation.
            """

            self.caller = caller
            self.phone_label = phone_label
            self.call_time = False
            if (call_status == 'incoming'
                    or call_status == 'outgoing'
                    or call_status == 'missed'
                    or call_status == 'voicemail'):
                self.call_status = call_status
            else:
                self.call_status = 'incoming'
            self.voicemail = voicemail
            self.playback = False
            self.avail_timeout = avail_timeout
            self._choices = []
            self._callback = False

        @property
        def get_label(self):
            """
            Return the label that should be played for this particular phone
            call, depending on things such as if the player is calling back
            the caller or if this is a replay.
            """

            if self.callback and renpy.has_label(self.phone_label + "_callback"):
                return self.phone_label + "_callback"
            return self.phone_label

        @property
        def played_regular(self):
            """
            Return True if the player has played the regular version of this
            phone call.
            """

            return self.phone_label in store.persistent.completed_story

        @property
        def played_callback(self):
            """
            Return True if the player has played the callback version of this
            phone call.
            """

            callback_lbl = self.phone_label + "_callback"
            return (renpy.has_label(callback_lbl)
                    and callback_lbl in store.persistent.completed_story)

        @property
        def callback(self):
            """
            Return True if the player is calling the character back after
            initially missing their call.
            """
            try:
                return self._callback
            except AttributeError:
                try:
                    self._callback = False
                    return self.__callback
                except AttributeError:
                    return False

        @callback.setter
        def callback(self, new_status):
            """Set the callback status."""

            try:
                self._callback = new_status
            except AttributeError:
                return

        @property
        def choices(self):
            try:
                return self._choices
            except AttributeError:
                try:
                    self._choices = self.__choices
                    return self.__choices
                except AttributeError:
                    self._choices = [ ]
                    return self._choices

        @choices.setter
        def choices(self, new_choices):
            try:
                self._choices = new_choices
            except AttributeError:
                return

        def add_to_choices(self, choice):
            """Add choice to list of choices."""

            if not store.observing:
                try:
                    self.choices.append(choice)
                except AttributeError:
                    return

        def decrease_time(self):
            """
            Count towards expiring this phone call so it is no longer
            available. By default phone calls will time out after two
            chatrooms.
            """

            global available_calls
            if self.avail_timeout is None or self.avail_timeout == 'test':
                # You generally shouldn't mess with this, but it
                # lets you make a call 'infinitely' available for testing
                pass
            else:
                self.avail_timeout -= 1
                if self.avail_timeout == 0:
                    available_calls.remove(self)

        def finished(self):
            """Move this phone call from available_calls to call_history"""

            global available_calls, call_history, observing
            self.playback = True
            self.call_time = upTime()
            if self.voicemail:
                self.call_status = 'voicemail'
            else:
                # You shouldn't be able to call a character back and get the
                # same conversation, so remove the call from available_calls
                if (self in available_calls
                        and self.avail_timeout not in ('test', None)):
                    available_calls.remove(self)

            # If you are calling back someone after missing their
            # call, it shows up in the history as an outgoing call
            if self.call_status == 'missed':
                self.call_status = 'outgoing'
            call_history.insert(0, self)
            observing = False

        def __eq__(self, other):
            """Check for equality between two PhoneCall objects."""
            if not isinstance(other, PhoneCall):
                return False
            return (self.phone_label == other.phone_label
                    and self.caller == other.caller)

        def __ne__(self, other):
            """Check for inequality between two PhoneCall objects."""
            if not isinstance(other, PhoneCall):
                return True

            return (self.phone_label != other.phone_label
                    or self.caller != other.caller)

init -6 python:

    def call_hang_up_incoming(phonecall):
        """
        Create a missed phone call entry in call_history and add this
        call to available_calls so the player can call the character back.
        """

        global call_history, available_calls
        phonecall.call_status = 'missed'
        store.gamestate = None
        missed_call = copy(phonecall)
        missed_call.call_time = upTime()
        # Can't play this conversation back as it hasn't been viewed
        missed_call.playback = False
        if missed_call not in call_history:
            call_history.insert(0, missed_call)
        phonecall.callback = True
        if phonecall not in available_calls:
            available_calls.append(phonecall)
        renpy.retain_after_load()

    def call_hang_up(phonecall):
        """
        If the player hangs up during a call, the conversation is no longer
        available. Remove this call from available_calls and use the
        hang up callback, if it exists.
        """

        if phonecall in store.available_calls:
            store.available_calls.remove(phonecall)

        if store.phone_hangup_callback:
            try:
                lbl = store.phone_hangup_callback(phonecall)
            except:
                ScriptError("Could not use phone_hangup_callback. Do you",
                    "have at least one function parameter?",
                    header="Phone Calls",
                    subheader="Hanging Up")
                return
            if not lbl:
                return
            # Otherwise, there's a label to jump to for the callback
            if renpy.has_label(lbl):
                renpy.call_in_new_context(lbl)
        return

    def call_available(who):
        """
        Check if a character has any available calls. Return the call if
        found, otherwise return False.
        """

        for phonecall in store.available_calls:
            if who == phonecall.caller:
                return phonecall
        return False

    def toggle_afm():
        """Toggle auto-forward mode on and off."""
        _preferences.afm_enable = not _preferences.afm_enable
        renpy.restart_interaction()

    def deliver_calls(lbl, expired=False, call_time=False):
        """
        Make any phone calls associated with the current story item available.
        """

        global available_calls, incoming_call, call_history
        global unseen_calls, all_characters, phone_timeout_dict
        missed_call = False
        phonecall = False
        all_call_list = list(all_characters)
        all_call_list.extend(store.phone_only_characters)

        # Add available calls
        for c in all_call_list:
            # Add available outgoing calls to the list
            og_call = "{}_outgoing_{}".format(lbl, c.file_id)
            if renpy.has_label(og_call):
                # Check if there's a more specific timeout defined
                avail_timeout = phone_timeout_dict.get(og_call, 1) + 1
                available_calls.append(
                    PhoneCall(c, og_call, 'outgoing', avail_timeout)
                )

            ic_call = "{}_incoming_{}".format(lbl, c.file_id)
            # Update the incoming call, or move it if the call has expired
            if renpy.has_label(ic_call):
                # Check if there's a more specific timeout defined
                avail_timeout = phone_timeout_dict.get(ic_call, 1) + 1
                if expired:
                    phonecall = PhoneCall(c, ic_call, 'outgoing', avail_timeout)
                    phonecall.callback = True
                    missed_call = PhoneCall(c, ic_call, 'missed', avail_timeout)
                else:
                    incoming_call = PhoneCall(c, ic_call, 'incoming', avail_timeout)

        # The player backed out of the item; no missed call but should
        # add it to the outgoing calls list
        if expired and not call_time and missed_call and phonecall:
            if phonecall not in available_calls:
                available_calls.append(phonecall)

        # Otherwise, the chatroom expired so add the missed call as well
        # as an outgoing call
        elif expired and missed_call and phonecall:
            missed_call.playback = False
            missed_call.call_time = call_time
            if missed_call not in call_history:
                call_history.insert(0, missed_call)
            if phonecall not in available_calls:
                available_calls.append(phonecall)
            unseen_calls += 1

        renpy.retain_after_load()

    def create_incoming_call(lbl, who=None):
        """Create an incoming call."""

        if isinstance(lbl, PhoneCall):
            store.incoming_call = lbl
            return

        # Do some error checking
        if not isinstance(who, ChatCharacter):
            ScriptError("The ChatCharacter for the phone call at \"", lbl,
                "\" could not be evaluated.",
                header="Creating Characters",
                subheader="Adding a New Character to Phone Calls")
            return
        if not renpy.has_label(lbl):
            ScriptError("Could not find label \"", lbl,
                "\" for incoming phone call.",
                header="Phone Calls",
                subheader="Incoming Calls")
            return
        store.incoming_call = PhoneCall(who, lbl)
        renpy.retain_after_load()

    def create_outgoing_call(lbl, who=None):
        """Make an outgoing call available."""

        if isinstance(lbl, PhoneCall):
            lbl.call_status = 'outgoing'
            store.available_calls.append(lbl)
            return

        # Do some error checking
        if not isinstance(who, ChatCharacter):
            ScriptError("The ChatCharacter for the phonecall at \"", lbl,
                "\" could not be evaluated.",
                header="Creating Characters",
                subheader="Adding a New Character to Phone Calls")
            return
        if not renpy.has_label(lbl):
            ScriptError("Could not find label \"", lbl,
                "\" for outgoing phone call.",
                header="Phone Calls",
                subheader="Outgoing Calls")
            return
        store.available_calls.append(PhoneCall(who, lbl, 'outgoing'))
        renpy.retain_after_load()

    class PhoneCharacter(ChatCharacter):
        """
        Class that keeps track of information needed for phone call-only
        characters.

        Attributes:
        -----------
        name : string
            Name of this character as it should appear on the call display.
        prof_pic : string
            File path to this character's profile picture. Follows the same
            conventions as the ChatCharacter profile picture.
        """

        def __init__(self, name, prof_pic, file_id=False, **properties):
            super(PhoneCharacter, self).__init__(name=name, prof_pic=prof_pic,
                **properties)
            self.file_id = file_id

            try:
                if (self not in store.phone_only_characters
                        and self.file_id):
                    store.phone_only_characters.append(self)
                # Remove self from all_characters, if applicable
                if self in store.all_characters:
                    store.all_characters.remove(self)
            except AttributeError:
                return

    def MMReplayCall(phonecall):
        """Return the action for replaying a phone call."""
        return [SetVariable('observing', True),
                SetVariable('current_call', phonecall),
                Jump('play_phone_call')]

    def MMOutgoingCall(phonecall=None, caller=None):
        """Return the action for making an outgoing phone call."""

        if phonecall:
            i = phonecall.caller
        else:
            i = caller

        if call_available(i):
            return [Preference("auto-forward", "enable"),
                    SetVariable('gamestate', PHONE),

                    ## An achievement for making your first outgoing call
                    If(not make_a_call_achievement.has(),
                        [make_a_call_achievement.Grant(),
                        progress_stat_achievement.AddProgress(1)]),

                    Show('outgoing_call',
                        phonecall=call_available(i))]
        elif i in phone_only_characters:
            return None
        else:
            return [Preference("auto-forward", "enable"),
                    SetVariable('gamestate', PHONE),

                    ## An achievement for making your first outgoing call
                    If(not make_a_call_achievement.has(),
                        [make_a_call_achievement.Grant(),
                        progress_stat_achievement.AddProgress(1)]),

                    Show('outgoing_call',
                        phonecall=i.voicemail,
                        voicemail=True)]

    def MMStartCall():
        """Return the action for beginning a phone call (on show)."""
        return [Stop('music'),
                SetVariable('gamestate', PHONE),
                Preference('auto-forward after click', 'enable')]

    def MMEndCall():
        """Return the action for ending a phone call (on hide)."""
        return [SetVariable('gamestate', None),
                Preference('auto-forward after click', 'disable')]

    def MMHangupCall(story=False, incoming=False):
        """Return the action for hanging up the phone."""
        if incoming:
            return [Stop('music'),
                    Function(call_hang_up_incoming, current_call),
                    Show('chat_home')]
        if story:
            return If(observing or current_timeline_item.currently_expired,
                [Jump('exit_item_early')],

                CConfirm("Do you really want to hang up this call? Please note that you cannot participate once you leave. If you want to participate in this call again, you will need to buy it back.",
                [Hide('phone_say'),
                    Jump('exit_item_early')]
                ))
        else:
            return CConfirm("Do you really want to end this phone call? You may not be able to have this conversation again if you hang up.",
                    [Hide('phone_say'), Jump('hang_up')])

    def MMIncomingCall(phonecall, starter=False):
        """Return the action for an incoming call."""
        if starter:
            return [Stop('music'),
                    SetVariable('current_call', phonecall),
                    Return()]
        else:
            return [Stop('music'),
                    Preference("auto-forward", "enable"),
                    SetVariable('current_call', phonecall),
                    Jump('play_phone_call')]

    def MMIncomingCountdown(call_countdown):
        """
        Return the action which occurs as the timer counts down on an
        incoming call.
        """
        return If(call_countdown>1,
                SetScreenVariable("call_countdown",
                call_countdown-1),
                [Function(call_hang_up_incoming, current_call),
                Show('chat_home')])

    def MMPauseCall():
        """
        Return the action which pauses/unpauses a phone call in-progress.
        """
        if _preferences.afm_enable: #preferences.afm_time > 0:
            return [SetScreenVariable('show_timer', False),
                    PauseAudio('voice', value=True),
                    Function(toggle_afm)]
        else:
            return [SetScreenVariable('show_timer', True),
                    PauseAudio('voice', value=False),
                    Function(toggle_afm)]


# Track characters who only appear in phone calls
default -5 phone_only_characters = [ ]

# Number of calls the player missed
default unseen_calls = 0
# True if the player is in a phone call (for choice menus etc)
default in_phone_call = False
# Number of seconds to wait for the player to pick up incoming calls
define call_countdown = 10
# List of calls the player can make (outgoing)
default available_calls = []
# History of phone calls
default call_history = []
# If there's an incoming call after a chatroom,
# it will be defined here
default incoming_call = False # e.g. PhoneCall(ju, 'some_label')
# Keeps track of the current call the player is in
default current_call = False


########################################################
## The phone menu screen, which displays a list of all
## the phone calls the player has received
########################################################
screen phone_calls():

    tag menu

    on 'show' action AutoSave()
    on 'replace' action AutoSave()

    use menu_header(_("Call History"), [Show('chat_home', Dissolve(0.5)),
                                    AutoSave()]):
        null height 3
        frame:
            style_prefix "phone_contacts"
            has hbox
            # History/Contacts tabs
            button:
                hover_background None
                background "menu_tab_active"
                has hbox
                add 'call_history_icon'
                text _("History")
            null width 10
            button:
                action Show("phone_contacts", Dissolve(0.5))
                has hbox
                add 'contact_icon'
                text _("Contacts")

        viewport:
            style_prefix 'call_display'
            draggable True
            mousewheel True
            scrollbars "vertical"
            has vbox
            for i in call_history:
                $ call_status = 'call_' + i.call_status

                frame:
                    style_prefix None
                    background 'message_idle_bkgr'
                    xysize (705, 150)

                    has hbox
                    spacing 10
                    align (0.5, 0.5)
                    frame:
                        xysize (135, 135)
                        align (0.5, 0.5)
                        add i.caller.get_pfp(127):
                            yalign 0.5 xalign 0.5

                    frame:
                        xsize 300
                        yalign 0.5
                        has vbox
                        align (0.0, 0.5)
                        text i.caller.name + ' {image=[call_status]}':
                            style "save_slot_text"
                        spacing 40
                        text i.call_time.get_phone_time() style "save_slot_text"

                    frame:
                        xysize (230, 135)
                        align (0.5, 0.5)
                        has hbox
                        align (0.5, 0.5)
                        spacing 30
                        imagebutton:
                            idle 'call_replay_active'
                            insensitive 'call_replay_inactive'
                            align(0.5, 0.5) alt _("Replay call")
                            xysize(96,85)
                            sensitive i.playback
                            hover Transform('call_replay_active', zoom=1.1,
                                            align=(.5, .5))
                            action MMReplayCall(i)

                        imagebutton:
                            idle 'call_back' alt _("Call Back")
                            insensitive Transform('call_back',
                                matrixcolor=SaturationMatrix(0.0))
                            align(0.5, 0.5)
                            xysize(96,85)
                            hover Transform('call_back', zoom=1.1)
                            action MMOutgoingCall(phonecall=i)


style call_display_viewport:
    xalign 0.5
    yalign 0.95
    xsize 725
    ysize config.screen_width-264

style call_display_vbox:
    spacing 10

style call_display_side:
    spacing 5


########################################################
## This screen shows you all the player's phone contacts
## so they can call them
########################################################

screen phone_contacts():
    tag menu
    default contact_list = [ c for c in character_list if c != m]

    use menu_header(_("Contacts"), Show('chat_home', Dissolve(0.5))):

        null height 3

        frame:
            style_prefix "phone_contacts"
            has hbox
            # Call History/Contacts tabs
            button:
                action Show("phone_calls", Dissolve(0.5))
                has hbox
                add 'call_history_icon'
                text _("History")
            null width 10
            button:
                hover_background None
                background "menu_tab_active"
                has hbox
                add 'contact_icon'
                text _("Contacts")

        vpgrid:
            style_prefix 'call_display'
            if len(contact_list) <= 9:
                yoffset 60
                xoffset 15
            draggable True
            mousewheel True
            scrollbars "vertical"
            cols 3
            for person in contact_list:
                use phone_contact_btn(person)
            for i in range(-len(contact_list) % 3):
                add 'empty_contact'

style call_display_vpgrid:
    align (0.5, 0.3)
    xspacing 55
    yspacing 100
    xysize (705, config.screen_height-264)
    xalign 0.4

style phone_contacts_frame:
    xalign 0.5
    yalign 0.13
    maximum(700,70)

style phone_contacts_hbox:
    xalign 0.5
    spacing 20
    yalign 0.5

style phone_contacts_text:
    color '#fff'
    font gui.sans_serif_1
    text_align 0.5
    xalign 0.5
    yalign 0.5

style phone_contacts_button:
    xsize 290
    ysize 65
    background "menu_tab_inactive"
    hover_background "menu_tab_inactive_hover"
    activate_sound 'audio/sfx/UI/phone_tab_switch.mp3'


image contact_available = Transform(
    'Text Messages/main02_new_icon.webp',
    zoom=0.7
)

## A small screen which contains a single contact button
screen phone_contact_btn(person):
    fixed:
        fit_first True
        vbox:
            style_prefix 'contacts_grid'
            imagebutton:
                background person.file_id + '_contact'
                idle person.file_id + '_contact'
                alt _("Call [person.name]")
                hover_foreground person.file_id + '_contact'
                action MMOutgoingCall(caller=person)
            text person.name style 'contact_text'
        if persistent.available_call_indicator and call_available(person):
            add 'contact_available' align (0.5, 0.0) yoffset 185

style contacts_grid_grid:
    align (0.5, 0.3)
    xspacing 60
    yspacing 100

style contacts_grid_vbox:
    spacing 25

style contact_text:
    color '#fff'
    xalign 0.5
    text_align 0.5
    font gui.sans_serif_1b

style caller_id:
    color '#fff'
    xalign 0.5
    text_align 0.5
    font gui.sans_serif_1
    size 70
    yoffset 10

style call_text:
    color '#fff'
    xalign 0.5
    yalign 0.5
    text_align 0.5
    font gui.sans_serif_1

## This label ensures the rest of the phone conversation will
## not play out if the player hangs up
label hang_up():
    $ gamestate = None
    $ purge_temp_texts()
    if not observing:
        $ call_hang_up(phonecall=current_call)
        $ purge_temp_texts()
    $ end_timeline_item_checks()
    $ reset_story_vars()
    $ renpy.end_replay()
    $ current_call = False
    $ _history = True
    $ renpy.retain_after_load()
    # Pop the call to play_phone_call
    $ renpy.pop_call()
    call screen phone_calls
    return

########################################################
## This is the screen that displays the dialogue when
## you're in a phone call
########################################################
screen in_call(who=ja, story_call=False):

    tag menu
    on 'show' action MMStartCall()
    on 'replace' action MMStartCall()
    on 'hide' action MMEndCall()
    on 'replaced' action MMEndCall()

    default show_timer = True
    default countup = 0

    use menu_header(_("In Call")):
        fixed:
            xysize (config.screen_width, config.screen_height-84)
            vbox:
                style_prefix 'phone_timer'
                add AlphaMask(who.get_pfp(130),
                    'rounded-rectangle-mask.webp') xalign 0.5
                text who.name size 45
                hbox:
                    text "{0:01}:".format(countup//60)
                    text "{0:01}".format((countup%60)//10)
                    text "{0:01}".format((countup%60)%10)
            if not starter_story and not story_call:
                use phone_footer(False, "call_pause", MMHangupCall())
            elif story_call:
                use phone_footer(answer_action=False, center_item='call_pause',
                    hangup_action=MMHangupCall(story=True))
            else:
                use phone_footer(False, "call_pause", False)

    if show_timer:
        timer 1.0 action SetScreenVariable('countup', countup+1) repeat True

style phone_timer_text:
    color "#fff"
    text_align 0.5
    xalign 0.5
    size 28

style phone_timer_hbox:
    xalign 0.5
    spacing 1

style phone_timer_vbox:
    yalign 0.08
    xalign 0.5
    spacing 10


########################################################
## This is the screen when you're receiving an incoming
## call
########################################################
screen incoming_call(phonecall, countdown_time=10):
    tag menu

    on 'hide' action Stop('music')
    on 'show' action SetScreenVariable('call_countdown', countdown_time)
    on 'replace' action SetScreenVariable('call_countdown', countdown_time)

    use menu_header(_("In Call")):
        frame:
            xysize (config.screen_width, config.screen_height-84)
            frame:
                xfill True
                ysize 500
                yalign 0.1
                background 'call_overlay'
                has hbox
                align (0.5, 0.5)
                spacing -10
                frame:
                    xysize (120, 220)
                    align (1.0, 0.1)
                    has hbox
                    align (1.0, 0.5)
                    spacing -15
                    add 'call_signal_ll' align (0.5, 0.5)
                    null width 10
                    add 'call_signal_ml' align (0.5, 0.5)
                    add 'call_signal_sl' align (0.5, 0.5)
                frame:
                    align (0.5, 0.5)
                    xsize 350
                    has vbox
                    align (0.5, 0.5)
                    spacing 15
                    add phonecall.caller.get_pfp(237) align (0.5, 0.5)
                    text phonecall.caller.name style 'caller_id'
                frame:
                    xysize (120, 220)
                    align (0.0, 0.1)
                    has hbox
                    align (0.0, 0.5)
                    spacing -15
                    add 'call_signal_sr' align (0.5, 0.5)
                    add 'call_signal_mr' align (0.5, 0.5)
                    null width 10
                    add 'call_signal_lr' align (0.5, 0.5)

            frame:
                xfill True
                yalign 0.53
                has vbox
                align (0.5, 0.6)
                spacing 10
                text "Incoming Call" color '#fff' xalign 0.5 size 40
                if (not starter_story and not isinstance(phonecall, StoryCall)):
                    text "[call_countdown]" xalign 0.5  color '#fff' size 80

            if starter_story:
                use phone_footer(MMIncomingCall(phonecall, True),
                                "headphones", False)
            elif isinstance(phonecall, StoryCall):
                use phone_footer(Return(), "headphones", False)
            else:
                use phone_footer(MMIncomingCall(phonecall, False),
                                "headphones", MMHangupCall(incoming=True))


    if not starter_story and not isinstance(phonecall, StoryCall):
        timer 1.0 action MMIncomingCountdown(call_countdown) repeat True


## Screen that shows the pick up/answer buttons at the bottom
screen phone_footer(answer_action=False, center_item=False, hangup_action=False):
    frame:
        xysize(config.screen_width-40, 200)
        yalign 1.0 yoffset -70
        xalign 0.5
        has hbox
        align (0.5, 0.5)
        spacing 10
        frame:
            xysize (160, 160)
            align (0.5, 0.5)
            if answer_action:
                imagebutton:
                    align (0.5, 0.5)
                    idle 'call_answer'
                    hover Transform('call_answer', zoom=1.1)
                    action answer_action
        fixed:
            xysize (323, 160)
            if center_item == "headphones":
                add 'call_headphones' yalign 1.0 xalign 0.5
            elif center_item == "call_pause":
                imagebutton:
                    align (0.5, 0.5)
                    selected _preferences.afm_enable
                    selected_idle 'call_pause'
                    idle 'call_play'
                    action MMPauseCall()

        frame:
            xysize(160,160)
            align (0.5, 0.5)
            if hangup_action:
                imagebutton:
                    align (0.5, 0.5)
                    idle 'call_hang_up'
                    hover Transform('call_hang_up', zoom=1.1)
                    action hangup_action

########################################################
## This is the screen when you're making a phone call
## to another character
########################################################

define phone_dial_sfx = "audio/sfx/phone ring.mp3"

init python:
    def MMPlayDialtone():
        """Return the action for playing the phone ringing sound effect."""
        return Function(renpy.music.play, ["<silence 1.5>",
                phone_dial_sfx, "<silence 1.5>"], loop=True)

    def MMVoicemail(phonecall):
        """Return the action which triggers a voicemail."""
        return If(phonecall, [Stop('music'),
                SetVariable('current_call', phonecall),
                Jump('play_phone_call')],
                Show('phone_calls'))

    def MMCallPickup(phonecall):
        """Return the action when a character picks up a call."""
        return [Stop('music'),
                SetVariable('current_call', phonecall),
                Jump('play_phone_call')]

screen outgoing_call(phonecall, voicemail=False):
    tag menu

    on 'show' action MMPlayDialtone()
    on 'replace' action MMPlayDialtone()

    use menu_header("In Call"):
        frame:
            xysize (config.screen_width, config.screen_height-84)
            frame:
                xfill True
                ysize 500
                yalign 0.16
                background 'call_overlay'
                has vbox
                align (0.5, 0.5) xsize 350
                spacing 15
                add phonecall.caller.get_pfp(237):
                    align (0.5, 0.5)
                text phonecall.caller.name style 'caller_id'

            frame:
                xfill True
                yalign 0.55
                has hbox
                align (0.5, 0.5)
                spacing 30
                add 'call_connect_triangle' at delayed_blink2(0.0, 1.4)
                add 'call_connect_triangle' at delayed_blink2(0.2, 1.4)
                add 'call_connect_triangle' at delayed_blink2(0.4, 1.4)
                add 'call_connect_triangle' at delayed_blink2(0.6, 1.4)
                add 'call_connect_triangle' at delayed_blink2(0.8, 1.4)
                add 'call_connect_triangle' at delayed_blink2(1.0, 1.4)

            use phone_footer(False, "headphones",
                            [Stop('music'), Show('phone_calls')])

    if voicemail:
        timer random.randint(8, 10) action MMVoicemail(phonecall)
    else:
        timer random.randint(2, 7) action MMCallPickup(phonecall)

## Screen used to say dialogue for phone characters
screen phone_say(who, what):

    window:
        style_prefix None
        style 'call_window'
        text what id "what":
            if persistent.dialogue_outlines:
                outlines [ (2, "#000") ]

## Allows the program to jump to the incoming call; now only used for the
## intro.
label new_incoming_call(phonecall=None):
    play music persistent.phone_tone loop nocaption
    if phonecall is None:
        $ phonecall = current_call
    $ begin_timeline_item(generic_storycall, resetHP=False, stop_music=False)

    if isinstance(phonecall, PhoneCall):
        call screen incoming_call(phonecall=phonecall)
    else:
        call screen incoming_call(phonecall=PhoneCall(phonecall, 'n/a'))
    if starter_story:
        call phone_begin(resetHP=False)
    return

## This label sets up the appropriate variables/actions when you begin
## a phone call
label phone_begin(resetHP=True):
    if isinstance(current_call, StoryCall):
        return
    $ begin_timeline_item(generic_storycall, resetHP=resetHP)
    show screen in_call(current_call.caller, isinstance(current_call, StoryCall))
    return

## This label sets the appropriate variables/actions when you finish
## a phone call. Now largely moot.
label phone_end():
    $ gamestate = None
    if starter_story and not renpy.get_return_stack():
        jump end_prologue
    return

## The label that is called to play a (non-story) phone call
label play_phone_call():
    if starter_story:
        $ set_name_pfp()
    stop music
    # This stops it from recording the dialogue
    # from the phone call in the history log
    $ _history = False
    $ gamestate = PHONE
    $ preferences.afm_enable = True
    hide screen incoming_call
    hide screen outgoing_call

    # Hide all the popup screens
    $ hide_all_popups()

    if _in_replay:
        $ observing = True
        $ set_name_pfp()
    show screen in_call(current_call.caller, isinstance(current_call, StoryCall))
    if not starter_story:
        # Play the phone call
        if observing and not _in_replay:
            $ store.current_choices = list(current_call.choices)
        # If this is a replay, check if the player has seen both a version of
        # this call regularly and/or as a callback
        if _in_replay:
            if current_call.played_regular and current_call.played_callback:
                # Offer the player a menu
                $ shuffle = "default" # Don't modify this menu at all
                menu (paraphrased=True):
                    "(Answer the incoming call)":
                        m "(Pick up)"
                    "(Call back the missed call)":
                        m "(Call back)"
                        $ current_call.callback = True
            elif current_call.played_callback:
                $ current_call.callback = True

        $ renpy.call(current_call.get_label)
        if (not dialogue_paraphrase and dialogue_picked != ""):
            $ say_choice_caption(dialogue_picked,
                dialogue_paraphrase, dialogue_pv)
        if not observing:
            $ current_call.finished()
            $ persistent.completed_story.add(current_call.get_label)
        $ send_temp_texts()
        $ reset_story_vars()
        $ renpy.end_replay()
        $ gamestate = None
        $ current_call = False
        $ observing = False
        $ _history = True
        $ renpy.retain_after_load()
        call screen phone_calls
    return

##*************************************************
## VOICEMAILS
##*************************************************
## For ease of keeping track of the different voicemails,
## they are defined here
label voicemail_1():
    voice "voice files/voicemail_1.mp3"
    vmail_phone "The person you have called is unavailable right now. Please leave a message at the tone or try again."
    return
