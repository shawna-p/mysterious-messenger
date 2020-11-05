init python:

    class Emailv3(renpy.store.object):
        """
        Class that holds the information needed for handling emails. Updated
        for v3.0

        Attributes:
        -----------
        guest : Guestv3
            Guestv3 object who is the sender of this email.
        msg : string
            The content of the email. Updated as the guest and player send
            messages.
        msg_num : int
            The current message number. Each exchange is considered "one"
            message.
        timeout : int
            If the player doesn't respond before this timeout reaches zero,
            the email is considered "timed out" and cannot be interacted with.
        deliver_reply : int or None
            How many story items the player must wait before the guest replies
            to their email, or None if it's the player's turn to reply.
        reply : string
            Contains the message to be delivered when the guest replies to the
            player's message.
        read : bool
            True if this email has been read.
        notified : bool
            True if the player has received a popup informing them of this
            email.
        sent_time : MyTime
            MyTime object containing the time the last email was sent at.
        current_replies : EmailReply[]
            A list of the current replies available to the player.
        success_list : bool
            A list of the results from each individual email exchange, either
            True for "success" or False for "fail".
        """

        def __init__(self, guest):
            """Create an Emailv3 object for the given guest."""

            self.guest = guest
            self.msg = guest.start_msg
            self.msg_num = 0
            self.timeout = 25
            self.deliver_reply = None
            self.reply = None
            self.__read = False
            self.current_replies = guest.choices
            self.notified = False
            self.sent_time = upTime()
            self.success_list = list()


        def __eq__(self, other):
            """
            Check for equality between two Email objects.
            Allows this class to be persistent.
            """

            if getattr(other, 'guest', False):
                return (self.guest == other.guest
                    and self.sent_time == other.sent_time)
            else:
                return False

        def __ne__(self, other):
            """Check for inequality between two Email objects."""

            return not self.__eq__(other)

        @property
        def read(self):
            return self.__read

        @read.setter
        def read(self, new_status):
            old_status = self.__read
            self.__read = new_status
            self.set_attendance()
            if not old_status and new_status and self.completed:
                store.email_list.remove(self)
                store.email_list.append(self)


        @property
        def can_reply(self):
            """Return True if this email can be replied to."""

            return (self.current_replies and self.reply is None
                    and self.timeout > 0)

        def deliver(self):
            """
            Deliver the next email in the chain to the player and notify them
            of its delivery with a popup. Decrease the timeout counter if
            this email is waiting to be replied to.
            """

            global email_list

            if self.timeout <= 0:
                # This message has timed out; do nothing
                return

            if self.deliver_reply is not None:
                # Decrease the counter towards delivering this email reply
                self.deliver_reply -= 1
                renpy.retain_after_load()

            # If it's the player's turn to reply, decrease the timeout counter,
            # unless there are no further emails in the chain.
            elif (self.deliver_reply is None and self.timeout > 0
                    and self.msg_num < self.num_emails):
                self.timeout -= 1

            # Notify the player of the delivered message
            if not self.notified and self.msg_num == 0 and not self.read:
                self.show_popup()

            # If deliver_reply <= 0 and there is a reply to be delivered,
            # deliver it.
            if (self.deliver_reply is not None
                    and self.deliver_reply <= 0
                    and self.reply):
                self.read = False
                self.reply += "\n\n------------------------------------------------\n\n"
                self.msg = self.reply + self.msg
                self.reply = None
                self.deliver_reply = None
                self.sent_time = upTime()
                # Move this email to the front of the list
                email_list.remove(self)
                email_list.insert(0, self)
                # Notify the player of the delivered message
                self.show_popup()
            renpy.retain_after_load()

        def send_reply(self):
            """Maintain compatibility with the old Email class."""

            self.show_choices()

        def show_choices(self):
            """Show the choices the player has to reply to the email."""

            choices = [ ]
            # First, determine what the choices are
            for index, reply in enumerate(self.current_replies):
                choices.append((reply.choice_text, index))
            # Shuffle the choices
            renpy.random.shuffle(choices)
            # Show a screen with the choices
            return choices
            # renpy.show_screen('email_choice', items=choices, email=self)

        def finish_choice(self, reply_index):
            """Deliver the appropriate reply based on the user's choice."""

            # Get the reply
            player_choice = self.current_replies[reply_index]
            # Add the player's reply to the email
            player_choice.player_msg += ("\n\n-------------------------"
                + "-----------------------\n\n")
            self.msg = player_choice.player_msg + self.msg
            # Queue the guest's reply
            self.reply = player_choice.guest_reply
            # Set the current set of choices
            self.current_replies = player_choice.continue_chain

            # Check if the email's success is explicitly recorded
            if (player_choice.email_success is not None):
                if player_choice.email_success:
                    self.success_list.append(True)
                else:
                    self.success_list.append(False)
            # Otherwise, assume success if the list continues
            # and failure otherwise
            elif self.current_replies:
                self.success_list.append(True)
            else:
                self.success_list.append(False)

            # Increase the message number
            self.msg_num += 1

            # Calculate when to deliver the reply
            if store.persistent.testing_mode:
                self.deliver_reply = 1
            else:
                max_num = num_future_timeline_items(self.guest.thumbnail
                    == "Email/Thumbnails/rainbow_unicorn_guest_icon.webp") - 1
                min_num = 1
                msg_remain = max(self.num_emails - self.msg_num, 1)
                # Generate a random number of items to wait for completion
                # before this email is delivered, based on how many timeline
                # items remain to be completed.
                max_num = min(max_num / msg_remain, 13)
                min_num = max(max_num-7, 1)
                if max_num <= min_num:
                    self.deliver_reply = min_num
                else:
                    self.deliver_reply = renpy.random.randint(min_num, max_num)

            # Update the sent timestamp
            self.sent_time = upTime()
            # Reset the timeout counter
            self.timeout = 25
            # Replied-to messages are moved to the back of the email list
            store.email_list.remove(self)
            store.email_list.append(self)
            renpy.retain_after_load()

        def set_attendance(self):
            """Set whether this guest is attending the party or not."""

            if self.guest.attending is not None:
                return
            if not self.completed:
                return
            if self.timeout <= 0:
                self.guest.attending = False
                return

            # Add "False" to the success_list for each email that wasn't
            # able to be answered
            for i in range(self.num_emails - len(self.success_list)):
                self.success_list.append(False)
            # The email chain has been completed. Calculate probability for
            # the guest to attend
            self.guest.attending = renpy.random.choice(self.success_list)


        @property
        def completed(self):
            """Return True if this email chain is completed."""

            if not self.read:
                return False
            if self.timeout <= 0:
                return True
            if self.msg_num == self.num_emails and self.reply is None:
                return True
            if not self.current_replies and self.reply is None:
                return True
            return False

        @property
        def failed(self):
            """Return True if this email chain has been failed."""

            if self.current_replies or not self.read or self.reply:
                return False
            if self.timeout <= 0:
                return False
            if self.msg_num == 1 and not self.success_list[0]:
                return True
            if True not in self.success_list:
                return True
            return False

        def get_icon(self, num):
            """Get the icon for the num-th message."""

            if num >= len(self.success_list):
                return 'email_inactive'
            if self.success_list[num]:
                return 'email_good'
            else:
                return 'email_bad'

        @property
        def status(self):
            """Return the status of this email chain."""

            if not self.completed:
                return None
            if self.timeout <= 0:
                return 'email_timeout'
            if self.failed:
                return 'email_failed'

            correct_emails = len([ x for x in self.success_list if x ])
            incorrect_emails = len(self.success_list) - correct_emails

            if incorrect_emails == 0:
                return 'email_completed_3'
            percent_correct = (correct_emails * 100) // self.num_emails
            if percent_correct >= 50:
                return 'email_completed_2'
            else:
                return 'email_completed_1'


        @property
        def email_status_list(self):
            """Return a list of icons to use for each email reply."""

            result = [ ]
            for i in range(self.num_emails):
                result.append(self.get_icon(i))
            return result

        @property
        def num_emails(self):
            """Return the total number of emails in a successful chain."""

            return self.guest.num_emails

        def show_popup(self):
            """Show a popup for a new email delivery to the player."""

            self.notified = True
            renpy.music.play(persistent.email_tone, 'sound')
            renpy.show_screen('email_popup', e=self)
            renpy.retain_after_load()
            renpy.restart_interaction()

        def send_sooner(self):
            """Increase the timeout and deliver_reply counters. For testing."""

            if self.deliver_reply is not None:
                self.deliver_reply -= 5
            self.timeout -= 5


    class Guestv3(renpy.store.object):
        """
        This class stores necessary information about the guest, and will
        automatically generate the menus for the player to reply to their
        emails.

        Attributes:
        -----------
        name : string
            Name of the guest as it shows up in email replies.
        dialogue_name : string
            The name of the guest as it should appear in their dialogue box
            when they arrive at the party e.g. "Long Cat".
        thumbnail : string
            File path to the thumbnail used for this guest's emails. Ideally
            155x155 pixels.
        large_img : string
            File path to the full-body image of this guest. Shown when
            they attend the party.
        short_desc : string
            Short description of the guest, shown in the guestbook.
        personal_info : string
            A longer description of the guest, viewable in the guestbook only
            after they have attended the party.
        start_msg : string
            Initial message sent to the player upon agreeing to invite
            this guest.
        choices : EmailReply[]
            A list of EmailReply objects containing the choices offered to
            reply to each email.
        num_emails : int
            The number of emails the player must exchange with the guest to
            fully complete the email chain.
        dialogue_what : string
            The guest's comment upon arriving at the party.
        comment_who : ChatCharacter
            The ChatCharacter object of the character who will talk about
            this guest in the guestbook.
        comment_what : string
            What the comment_who character will say about the guest.
        comment_img : string
            A string corresponding to a defined image or layeredimage attributes
            that will be used to display the sprite of the character speaking
            about this guest e.g. "zen front party happy".
        attending : bool
            True if the guest is attending the party.
        reply_icons : string[]
            A list of the types of icons that should be used to display
            whether a particular email in the chain was passed or failed.
        """

        def __init__(self, name, dialogue_name, thumbnail, large_img,
                short_desc, personal_info, start_msg, choices,
                dialogue_what=None, comment_who=None, comment_what=None,
                comment_img=None, num_emails=3):

            self.name = name
            self.dialogue_name = dialogue_name
            self.thumbnail = thumbnail
            self.large_img = large_img
            self.short_desc = short_desc
            self.personal_info = personal_info
            self.start_msg = filter_whitespace(start_msg)
            self.choices = choices
            self.num_emails = num_emails
            self.dialogue_what = dialogue_what or ("This guest was not "
                + "given anything to say.")
            self.comment_who = comment_who or store.narrator
            self.comment_what = comment_what or ("No comment was entered "
                + "for this guest")
            self.comment_img = comment_img or "#000"

            self.attending = None
            self.reply_icons = []

            if self.name not in store.persistent.guestbook:
                store.persistent.guestbook[self.name] = None
            if self not in store.all_guests:
                store.all_guests.append(self)

        def __eq__(self, other):
            """Check for equality between Guestv3 objects."""

            if (getattr(other, 'name', False)
                    and getattr(other, 'thumbnail', False)):
                return (self.name == other.name
                        and self.thumbnail.split('.')[0]
                            == other.thumbnail.split('.')[0])
            else:
                return False

        def __ne__(self, other):
            """Check for inequality between Guestv3 objects."""

            return not self.__eq__(other)



    class EmailReply(renpy.store.object):
        """
        A class intended to facilitate writing email replies.

        Attributes:
        -----------
        choice_text : string
            The text of the choice to reply to the email.
        player_msg : string
            The message the player writes after the choice is made.
        guest_reply : string
            The guest's reply to the player's message.
        continue_chain : EmailReply[]
            If this email chain will continue after the player selects this
            reply, this is a list of EmailReply objects that will be available
            the next time the player is given the opportunity to reply.
        email_success : bool or None
            If explicitly set to a boolean value, this indicates if it ends
            the email chain in a good (True) or bad (False) way.
        """

        def __init__(self, choice_text, player_msg, guest_reply,
                continue_chain=None, email_success=None):

            self.choice_text = choice_text
            self.player_msg = filter_whitespace(player_msg)
            self.guest_reply = filter_whitespace(guest_reply)
            self.continue_chain = continue_chain or []
            self.email_success = email_success

    import re # Import regex
    def filter_whitespace(s):
        """Filter excess whitespace from a string. Used for emails."""

        s = s.strip()
        # Filter out excess leading whitespace
        pattern = "^ +"
        s = re.sub(pattern, '', s, flags=re.MULTILINE)
        # Ensure there are no spaces at the end of any lines
        pattern = ".* +$"
        s = re.sub(pattern, '', s, flags=re.MULTILINE)
        # Remove singular newlines and replace with a space
        pattern = "(?<!\n)(\n)(?!\n)"
        s = re.sub(pattern, ' ', s, flags=re.MULTILINE)
        return s

    def Guest(*args, **kwargs):
        # Returns an appropriate Guest object depending on which version the
        # user is on.
        if store.use_2_2_guest or (len(args) + len(kwargs)) > 14:
            # Use the old Guest style
            return Guestv2(*args, **kwargs)
        # Otherwise, use the new Guest style
        return Guestv3(*args, **kwargs)

    def unread_emails():
        """Return the number of unread emails in the player's inbox."""

        unread = [ x for x in store.email_list if not x.read]
        return len(unread)

    def deliver_emails():
        """Deliver the emails in email_list."""

        for e in store.email_list:
            e.deliver()

    def attending_guests():
        """
        Return the number of guests attending the party. If a guest's email
        chain is completed, they are guaranteed to come. If two email messages
        were correct and the third was incorrect, the guest has a 67% chance
        of coming. If the first message was correct and the second was not,
        the guest has a 33% chance of coming. Guests will only attend if all
        of their messages have been replied to and read.
        """

        num_guests = 0
        for e in store.email_list:
            if e.guest.attending:
                num_guests += 1
        return num_guests

default email_list = []
default email_reply = False
# List of all the guests the player has successfully
# invited to the party
default persistent.guestbook = { }
default all_guests = [ ]
default current_email = None

########################################################
## This screen shows a popup to notify you when you
## have a new email
########################################################
screen email_popup(e):

    #modal True
    zorder 100

    frame:
        style_prefix 'email_popup'
        imagebutton:
            align (1.0, 0.0)
            idle 'input_close'
            hover 'input_close_hover'
            action Hide('email_popup')
        hbox:
            add 'new_text_envelope'
            text 'NEW'
        vbox:
            hbox:
                style_prefix 'email_popup2'
                add Transform(e.guest.thumbnail, zoom=0.6)
                text "You have a new message from @" + e.guest.name

            # This button takes you directly to the email. It is
            # included so long as the email popup is not shown
            # during phone calls or chatrooms.
            textbutton _('Go to'):
                if (not (renpy.get_screen('in_call')
                        or renpy.get_screen('incoming_call')
                        or renpy.get_screen('outgoing call')
                        or text_person)):
                    action If (((not (renpy.get_screen('in_call')
                            or renpy.get_screen('incoming_call')
                            or renpy.get_screen('outgoing call')
                            or text_person))),
                        [Hide('email_popup'),
                            Hide('save_load'),
                            Hide('menu'),
                            Hide('chat_footer'),
                            Hide('phone_overlay'),
                            Hide('settings_screen'),
                            Show('email_hub')], None)

    timer 3.25 action Hide('email_popup', Dissolve(0.25))

style email_popup_frame:
    xysize (510,300)
    background 'left_corner_menu_dark'
    xalign 0.5
    yalign 0.4

style email_popup_hbox:
    yalign 0.09
    xalign 0.05
    spacing 15

style email_popup_text:
    color '#73f1cf'
    yalign 1.0
    font gui.sans_serif_1b

style email_popup_vbox:
    align (0.5, 0.72)
    spacing 15
    xysize (450, 100)

style email_popup_button:
    xalign 0.5
    xsize 220
    ysize 70
    padding (20,20)
    background 'menu_select_btn'
    hover_foreground 'menu_select_btn_hover'

style email_popup_button_text:
    is mode_select
    size 28

style email_popup2_hbox:
    align (0.5, 0.5)
    xsize 470
    spacing 10

style email_popup2_text:
    color '#fff'
    size 25
    align(0.5, 0.5)


########################################################
## This screen shows a list of the emails you've
## received
########################################################
screen email_hub():

    tag menu

    default current_page = 0
    default num_pages = (len(email_list) + 7 - 1) // 7

    on 'replace' action FileSave(mm_auto, confirm=False)
    on 'show' action FileSave(mm_auto, confirm=False)


    use menu_header('Email', Show('chat_home', Dissolve(0.5))):
        frame:
            style_prefix 'email_hub'
            has vbox
            null height -15
            if len(email_list) == 0:
                text "Inbox is empty"
            for e in email_list[current_page*7:current_page*7+7]:
                use email_button(e)

        hbox:
            style_prefix 'email_hub'
            imagebutton:
                idle Transform("email_next", xzoom=-1)
                align (0.5, 0.5)
                if current_page > 0:
                    action SetScreenVariable('current_page', current_page-1)
                    activate_sound 'audio/sfx/UI/email_next_arrow.mp3'

            for index in range(num_pages):
                textbutton _(str(index+1)):
                    action SetScreenVariable('current_page', index)

            imagebutton:
                idle "email_next"
                align (0.5, 0.5)
                if current_page < num_pages - 1:
                    action SetScreenVariable('current_page', current_page+1)
                    activate_sound 'audio/sfx/UI/email_next_arrow.mp3'

style email_hub_frame:
    background 'left_corner_menu'
    padding (20,20)
    xysize (685, 1100)
    align (0.5, 0.75)

style email_hub_vbox:
    spacing 40
    align (0.5, 0.0)

style email_hub_text:
    color '#fff'
    xalign 0.5
    yalign 0.0

style email_hub_hbox:
    align (0.5, 0.99)
    spacing 15

style email_hub_button:
    align (0.5, 0.5)
    activate_sound 'audio/sfx/UI/email_next_arrow.mp3'

style email_hub_image_button:
    is email_hub_button

style email_hub_button_text:
    color '#fff'


########################################################
## This shows the buttons you can click on in order to
## open and read your emails
########################################################
screen email_button(e):
    button:
        style_prefix 'email_btn'
        if e.read:
            background 'email_panel'
        else:
            background 'email_mint'

        action [SetVariable("current_email", e),
                SetField(e, 'read', True),
                Show('open_email', e=e)]

        hbox:
            fixed:
                if not e.read:
                    add 'email_unread' align(1.0, 0.5)
                elif e.can_reply:
                    add 'email_read' align(1.0, 0.5)
                else:
                    add 'email_replied' align(1.0, 0.5)
            add Transform(e.guest.thumbnail, size=(94, 94)) align(0.5, 0.3)
            null width -10
            vbox:
                frame:
                    text '@' + e.guest.name
                hbox:
                    align(0.3, 0.5)
                    spacing 8
                    for icon in e.email_status_list:
                        if len(e.email_status_list) > 5:
                            $ icon_zoom = 0.6
                        elif len(e.email_status_list) > 4:
                            $ icon_zoom = 0.7
                        elif len(e.email_status_list) > 3:
                            $ icon_zoom = 0.8
                        else:
                            $ icon_zoom = 1.0
                        add Transform(icon, zoom=icon_zoom) align (0.5, 0.5)
            frame:
                xysize(240,90)
                align (0.0, 0.3)
                if e.status is not None:
                    add e.status align (0.5, 0.5)

style email_btn_button:
    align (0.5, 0.5)
    xysize (644, 111)
    hover_foreground 'white_transparent'

style email_btn_hbox:
    align (0.0, 0.0)
    spacing 10

style email_btn_fixed:
    xysize (80,111)
    align (0.5, 0.5)

style email_btn_vbox:
    align(0.5, 0.2)
    spacing 12

style email_btn_frame:
    align(0.0, 0.0)
    xysize(185, 38)

style email_btn_text:
    font gui.curlicue_font
    color '#fff'
    size 27
    align (0.0, 0.0)


########################################################
## This is the screen that displays the email you've
## selected, and lets you reply
########################################################
screen open_email(e):
    modal True
    zorder 100

    add 'choice_darken'

    frame:
        style_prefix 'open_email'
        imagebutton:
            idle 'input_close'
            hover 'input_close_hover'
            action Hide('open_email')
        vbox:
            hbox:
                add e.guest.thumbnail
                vbox:
                    spacing 10
                    fixed:
                        text 'From: ' + e.guest.name
                    text ('[[Date] ' + e.sent_time.month_num
                            + '/' + e.sent_time.day):
                                size 27
                    text ('[[Time] ' + e.sent_time.get_twelve_hour()):
                                size 27

                textbutton _('Reply'):
                    if e.can_reply and isinstance(e, Email):
                        action Function(e.send_reply)
                    elif e.can_reply:
                        action [Show('email_choice', items=e.show_choices(),
                            email=e)]
                    else:
                        foreground 'menu_select_btn_inactive'

            frame:
                style 'open_email_frame2'
                viewport:
                    scrollbars 'vertical'
                    mousewheel True
                    draggable True
                    text e.msg size 28 color "#000"

style open_email_frame:
    maximum(685, 800)
    background 'left_corner_menu_dark' padding(20,20)
    align (0.5, 0.5)

style open_email_image_button:
    align (1.0, 0.0)
    xoffset 20
    yoffset -20

style open_email_vbox:
    spacing 15
    align (0.0, 0.0)

style open_email_hbox:
    spacing 10
    align (0.0, 0.0)

style open_email_fixed:
    align (0.0, 0.0)
    xsize 280
    ysize 80

style open_email_text:
    color "#fff"

style open_email_button:
    align (0.5, 1.0)
    xsize 170
    ysize 70
    size 28
    background 'menu_select_btn'
    padding (20,20)
    hover_foreground 'menu_select_btn_hover'

style open_email_button_text:
    is mode_select

style open_email_frame2:
    background 'email_open_transparent'
    padding(20,20)
    xysize (625, 585)
    align (0.5,0.5)

style open_email_viewport:
    align (0.5, 0.5)
    xysize (585, 545)


screen email_choice(items, email):
    zorder 150
    modal True

    if persistent.custom_footers and not renpy.is_skipping():
        default the_anim = choice_anim
    else:
        default the_anim = null_anim

    add "#000c"
    vbox:
        style_prefix 'email_choice'
        for num, i in enumerate(items):
            $ fnum = float(num*0.2)
            textbutton i[0] at the_anim(fnum):
                action [Function(email.finish_choice, i[1]),
                    Hide('email_choice')]

        textbutton _("Reply later"):
            at the_anim(len(items)*0.2)
            xysize (280, 120)
            background Frame(Transform("Text Messages/chat-bg02_2.webp",
                size=(740, 120)), 50, 40)
            hover_background Frame(Transform("Text Messages/chat-bg02_3.webp",
                size=(740, 120)), 50, 40)
            xalign 0.995
            action Hide('email_choice')


## This is the label you call at the end of
## an email choice menu
label email_end():
    $ renpy.retain_after_load()
    return

image img_locked = "CGs/album_unlock.webp"

screen guestbook():
    tag menu

    if not main_menu:
        on 'replace' action FileSave(mm_auto, confirm=False)
        on 'show' action FileSave(mm_auto, confirm=False)

    if main_menu:
        $ return_action = Show('select_history', Dissolve(0.5))
    else:
        $ return_action = Show('chat_home', Dissolve(0.5))
    $ num_rows = -(-len(persistent.guestbook) // 4)
    use menu_header("Guest", return_action):
        vpgrid id 'guest_vp':
            xysize (740, 1200)
            yfill True
            rows num_rows
            cols 4
            draggable True
            mousewheel True
            scrollbars "vertical"
            side_xalign 1.0
            side_spacing 15
            align (0.5, 1.0)
            spacing 20

            for guest in all_guests:
                button:
                    xysize (155, 155)
                    # Do some checks on whether the player
                    # finished inviting the guest or not
                    if persistent.guestbook[guest.name] == "seen":
                        # The player has invited this guest but the
                        # guest hasn't attended the party
                        background guest.thumbnail
                        action Show('guest_info_popup',
                                guest=guest, unlocked=False)
                    elif (persistent.guestbook[guest.name] == "attended"
                            or persistent.guestbook[guest.name] == 'viewed'):
                        # The guest has attended the party
                        background guest.thumbnail
                        action Show('guest_info_popup',
                            guest=guest, unlocked=True)
                    else:
                        # This guest is unknown to the player
                        background 'img_locked'
                        action CConfirm("You have not yet\nencountered this guest")

            for i in range((4*num_rows) - len(persistent.guestbook)):
                null

image guest_story = 'Email/story_available.webp'
image guest_story_locked = 'Email/story_locked.webp'
image guest_descrip_bg = Frame('Email/guest_orange_shade.webp', 0, 0)

default viewing_guest = False
screen guest_info_popup(guest, unlocked):

    modal True
    add "#0005"
    frame:
        style_prefix "guest_info"
        has fixed
        yfit True
        imagebutton:
            idle 'input_close'
            hover 'input_close_hover'
            action [Hide('guest_info_popup')]
        vbox:
            text '@[guest.name]':
                size 40 font gui.sans_serif_1b xoffset 40
            text guest.short_desc:
                size 28 text_align 0.5 xalign 0.5 layout 'subtitle'
            null height 5
            hbox:
                style_prefix 'guest_desc'
                vbox:
                    text "[[Personal Info]" size 25 font gui.sans_serif_1b
                    frame:
                        if unlocked:
                            text guest.personal_info
                        else:
                            vbox:
                                null height 10
                                add 'plot_lock' align (0.5, 0.5)
                                text ("Information will be unlocked when"
                                + " this guest attends the party.")
                vbox:
                    fixed:
                        xsize 620//2
                        yfit True
                        align (0.5, 0.5)
                        add guest.large_img
                    fixed:
                        xysize (int(273*1.1), int(93*1.1))
                        imagebutton:
                            align (0.5, 0.5)
                            if unlocked:
                                idle 'guest_story'
                                hover Transform('guest_story', zoom=1.1)
                                action [Preference('auto-forward',
                                        'disable'),
                                    Replay('guest_info',
                                    {'guest_replay_info' :
                                        guest}, False),
                                    SetDict(persistent.guestbook,
                                        guest.name, 'viewed'),
                                    Function(renpy.retain_after_load)]
                            else:
                                idle 'guest_story_locked'

default guest_replay_info = None
label guest_info():
    python:
        who = guest_replay_info.comment_who
        what = guest_replay_info.comment_what
        expr = guest_replay_info.comment_img

        # Award an hourglass if this is the first time
        # the player has seen this guest's guestbook
        if persistent.guestbook[guest_replay_info.name] == 'attended':
            persistent.guestbook[guest_replay_info.name] = 'viewed'
            if not persistent.animated_icons:
                renpy.show_screen(allocate_notification_screen(False),
                    message="Hourglass +1")
            else:
                renpy.show_screen(allocate_hg_screen())
            renpy.music.play("audio/sfx/UI/select_4.mp3", channel='sound')
            persistent.HG += 1

    $ begin_timeline_item(StoryMode("Guest", "guest_info", "00:00"))
    $ viewing_guest = True
    scene bg rfa_party_3
    show expression expr
    who "[what]"
    $ viewing_guest = False
    $ renpy.end_replay()
    return

style guest_info_frame:
    background 'input_popup_bkgr'
    align (0.5, 0.5)
    xsize 630
    yminimum 400
    ymaximum 900

style guest_info_image_button:
    align (1.0, 0.0)
    yoffset -3 xoffset 3

style guest_info_vbox:
    xalign 0.5
    xsize 620
    spacing 30
    yoffset 20

style guest_info_text:
    color "#fff"

style guest_desc_vbox:
    spacing 10
    yalign 0.5

style guest_desc_text:
    color "#fff"

style guest_desc_frame:
    background 'guest_descrip_bg'
    padding (5, 5)
    xsize 620//2-30
