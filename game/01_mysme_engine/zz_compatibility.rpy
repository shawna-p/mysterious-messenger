## This file contains deprecated functions, classes, screens, and labels
## that are no longer required for the current version of Mysterious Messenger
## but are maintained here for backwards compatibility. Use of old features
## often results in a printout to the console but no averse in-game effects.

init python:
    def set_pronouns():
        """Set the player's pronouns and pronoun variables."""
        ## Retained for compatibility, but no longer needed
        return

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

    ## Has now been replaced with the grid-style profile picture
    ## selection screen.
    def MC_pic_change():
        """
        Changes the MC's profile picture when pressed. Cycles through
        images present in a particular folder, allowing users to upload
        their own images.
        """

        global m, persistent

        # If not using a custom pic, check if one's available
        # Populate the list with the file names
        file_list = renpy.list_files()
        # This now has a list of the available images
        user_pic_list = [ pic for pic in file_list
                if 'Drop Your Profile Picture Here/' in pic and isImg(pic)]
        # Check if there are indeed available files
        if user_pic_list:
            if persistent.MC_pic in user_pic_list:
                # Go through the pics and set the pic to the
                # next available image
                # Assume the image provided is square (this is
                # the responsibility of the user)
                for i, pic in enumerate(user_pic_list):
                    if persistent.MC_pic == pic:
                        if i < len(user_pic_list) - 1:
                            persistent.MC_pic = user_pic_list[i+1]
                            break
                        elif i == len(user_pic_list) - 1:
                            persistent.MC_pic = user_pic_list[0]
                            break
            else:
                persistent.MC_pic = user_pic_list[-1]
        else:
            persistent.MC_pic = 'Profile Pics/MC/MC-1.webp'

        # m.prof_pic = persistent.MC_pic
        renpy.retain_after_load()

    ## Replaced by BasicScreenshot
    ## This class defines a renpy displayable made up of `number`
    ## of screen tear sections, that bounce back and forth, based
    ## on ontimeMult & offtimeMult and each piece is randomly offset
    ## by an amount between offsetMin & offsetMax
    class Tear(renpy.Displayable):
        def __init__(self, number, offtimeMult, ontimeMult,
                        offsetMin, offsetMax, srf=None):
            super(Tear, self).__init__()
            self.width, self.height = renpy.get_physical_size()
            self.width = int(self.width)
            self.height = int(self.height)
            print_file("1")
            # Force screen to 9:16 ratio
            if float(self.width) / float(self.height) > 9.0/16.0:
                self.width = int(self.height * 9 // 16)
            else:
                self.height = int(self.width * 16 // 9)
            print_file("2")
            self.number = number
            # Use a special image if specified, or tear
            # current screen by default
            if not srf: self.srf = screenshot_srf()
            else: self.srf = srf
            print_file("3")

            # Rip the screen into `number` pieces
            self.pieces = []
            tearpoints = [0, self.height]
            print_file("4")
            for i in range(number):
                tearpoints.append(random.randint(10, self.height - 10))
            print_file("5")
            tearpoints.sort()
            for i in range(number+1):
                self.pieces.append(TearPiece(tearpoints[i],
                                    tearpoints[i+1], offtimeMult,
                                    ontimeMult, offsetMin, offsetMax))
            print_file("6")

        ## Render the displayable
        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)
            print_file("7")
            render.blit(self.srf, (0,0))
            print_file("8")
            # Render each piece
            for piece in self.pieces:
                print_file("9")
                piece.update(st)
                subsrf = (self.srf.subsurface((0,
                            max(0, piece.start_y - 1),
                            self.width,
                            max(0, piece.end_y - piece.start_y))))
                            #.pygame_surface()
                render.blit(subsrf, (piece.offset, piece.start_y))
            print_file("10")
            renpy.redraw(self, 10)
            print_file("11")
            return render

## Replaced by the tear2 screen which uses BasicScreenshot
## Define the screen for Ren'Py; by default, tear the screen into 10 pieces
screen tear(number=10, offtimeMult=1, ontimeMult=1, offsetMin=0,
                            offsetMax=50, w_timer=False, srf=None):
    zorder 150 #Screen tear appears above pretty much everything

    add Tear(number, offtimeMult, ontimeMult, offsetMin,
                                offsetMax, srf) size (config.screen_width,config.screen_height)
    if w_timer:
        timer w_timer action Hide('tear')

## Listed for compatibility; renamed to just the plural variable
define is_are = PronounVerb("are", "is")
define has_have = PronounVerb("have", "has")
define do_does = PronounVerb("do", "does")

# Displays notifications instead of heart icons
# Replaced with persistent.animated_icons
default persistent.heart_notifications = False
# Allows the player to toggle timed menus on or off.
# Replaced with persistent.use_timed_menus
default persistent.autoanswer_timed_menus = None
# Replaced with persistent.pv
default pv = 0.8
# Replaced by story_archive
default chat_archive = None
# Replaced by current_timeline_item
default current_chatroom = None
# Replaced by most_recent_item
default most_recent_chat = None
# Replaced by collected_hp
default chatroom_hp = None
# Replaced by collected_hg
default chatroom_hg = None


## Deprecated. Used to begin writing a text message conversation.
label text_begin(who):
    return

## Deprecated. Used to tell the program the next lines of dialogue
## are intended for a text message conversation.
label compose_text(who, real_time=False):
    $ who.set_real_time_text(real_time)
    $ who.text_msg.read = False
    $ textbackup = 'Reset'
    $ text_person = who
    $ renpy.retain_after_load()
    return

## Deprecated. Used to finish writing the beginning
## of a text message conversation.
label compose_text_end(text_label=False):
    $ text_person.text_label = text_label
    $ text_person = None
    $ textbackup = 'Reset'
    $ renpy.retain_after_load()
    return

## Deprecated. Used to end text message conversations.
label text_end():
    return

## Deprecated. Now replaced by end_route.
label vn_end_route():
    jump end_route

# Deprecated. Used to show the 'answer' bar at the bottom
# of the screen before a chatroom menu.
label answer(from_cg=False):
    return

## Deprecated. Used to continue the game after a plot branch.
## Has now been replaced with the execute_plot_branch label.
label plot_branch_end():
    return

## Deprecated; replaced with `invite guest_var`. You can call this label with
## `call invite(guest_var)` and it will trigger the guest to email the player.
label invite(guest):
    $ execute_invite_guest(guest)
    return

# Deprecated; replaced with `award heart u` where `u` is the character to award
# the heart for. Call this to display the heart icon for a given character
label heart_icon(character, bad=False):
    if bad:
        award heart character bad
    else:
        award heart character
    return

# Deprecated; replaced with `break heart u` where `u` is the character to
# remove a heart for. Like the heart icon, call this to display the heart break.
label heart_break(character):
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
    enter chatroom chara
    return

# Deprecated; replaced with `exit chatroom u` where `u` is the character
# exiting the chatroom
label exit(chara):
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

init python:

    ## Old classes for Guest and Email declarations
    class Guest(renpy.store.object):
        """
        This class stores necessary information about the guest, including
        all of their email replies as well as their image thumbnail and name.
        It is used for program versions earlier than v3.0.

        Attributes:
        -----------
        name : string
            Name of the guest as it shows up in email replies.
        thumbnail : string
            File path to the thumbnail used for this guest's emails. Ideally
            155x155 pixels.
        start_msg : string
            Initial message sent to the player upon agreeing to invite
            this guest.
        msg1_good : string
            Player's correct response to the first email.
        msg2_good : string
            Player's correct response to the second email.
        msg3_good : string
            Player's correct response to the third email.
        reply1_good : string
            Guest's response to the first correct reply.
        reply2_good : string
            Guest's response to the second correct reply.
        reply3_good : string
            Guest's response to the third correct reply.
        reply1_bad : string
            Guest's response to the first incorrect reply.
        reply2_bad : string
            Guest's response to the second incorrect reply.
        reply3_bad : string
            Guest's response to the third incorrect reply.
        msg1_bad : string
            Player's incorrect response to the first email.
        msg2_bad : string
            Player's incorrect response to the second email.
        msg3_bad : string
            Player's incorrect response to the third email.
        label1 : string
            Label to jump to to answer the first email.
        label2 : string
            Label to jump to to answer the second email.
        label3 : string
            Label to jump to to answer the third email.
        attending : bool
            True if the guest is attending the party.
        large_img : string
            File path to the full-body image of this guest. Shown when
            they attend the party.
        short_desc : string
            Short description of the guest, shown in the guestbook.
        personal_info : string
            A longer description of the guest, viewable only after they
            have attended the party.
        comment_who : ChatCharacter
            The ChatCharacter object of the character who will talk about
            this guest in the guestbook.
        comment_what : string
            What the comment_who character will say about the guest.
        comment_img : string
            A string corresponding to a defined image or layeredimage attributes
            that will be used to display the sprite of the character speaking
            about this guest e.g. "zen front party happy".
        dialogue_name : string
            The name of the guest as it should appear in their dialogue box
            when they arrive at the party e.g. "Long Cat"
        dialogue_what : string
            The guest's comment upon arriving at the party.
        """

        def __init__(self, *args, **kwargs):

            # Check if this is using the old or new style of guest
            if (store.use_2_2_guest or (len(args) + len(kwargs) > 14)
                    or (len(args) > 8 and not isinstance(args[7], EmailReply))):
                # Old guest style
                try:
                    self.create_old_guest(*args, **kwargs)
                    self._v3_guest = None
                except:
                    # New guest style?
                    self._v3_guest = Guestv3(*args, **kwargs)
            else:
                # New guest style
                self._v3_guest = Guestv3(*args, **kwargs)

        @property
        def v3_guest(self):
            try:
                return self._v3_guest
            except:
                pass
            try:
                return self.__v3_guest
            except AttributeError:
                return None

        @property
        def attending(self):
            try:
                return self.v3_guest.attending
            except AttributeError:
                return None

        def create_old_guest(self, name, thumbnail, start_msg,
                        msg1_good, reply1_good, msg1_bad, reply1_bad,
                        msg2_good, reply2_good, msg2_bad, reply2_bad,
                        msg3_good, reply3_good, msg3_bad, reply3_bad,
                        large_img=False, short_desc="", personal_info="",
                        comment_who=None, comment_what="", comment_img='#000',
                        dialogue_name="", dialogue_what=""):
            """
            Create a Guest object to store information about their emails
            and guestbook details.

            Parameters:
            -----------
            name : string
                Name of the guest as it shows up in email replies.
            thumbnail : string
                File path to the thumbnail used for this guest's emails. Ideally
                155x155 pixels.
            start_msg : string
                Initial message sent to the player upon agreeing to invite
                this guest.
            msg1_good : string
                Player's correct response to the first email.
            reply1_good : string
                Guest's response to the first correct reply.
            msg1_bad : string
                Player's incorrect response to the first email.
            reply1_bad : string
                Guest's response to the first incorrect reply.
            msg2_good : string
                Player's correct response to the second email.
            reply2_good : string
                Guest's response to the second correct reply.
            msg2_bad : string
                Player's incorrect response to the second email.
            reply2_bad : string
                Guest's response to the second incorrect reply.
            msg3_good : string
                Player's correct response to the third email.
            reply3_good : string
                Guest's response to the third correct reply.
            msg3_bad : string
                Player's incorrect response to the third email.
            reply3_bad : string
                Guest's response to the third incorrect reply.
            large_img : string
                File path to the full-body image of this guest. Shown when
                they attend the party.
            short_desc : string
                Short description of the guest, shown in the guestbook.
            personal_info : string
                A longer description of the guest, viewable only after they
                have attended the party.
            comment_who : ChatCharacter
                The ChatCharacter object of the character who will talk about
                this guest in the guestbook.
            comment_what : string
                What the comment_who character will say about the guest.
            comment_img : string
                A string corresponding to a defined image or layeredimage
                attributes that will be used to display the sprite of the
                character speaking about this guest e.g. "zen front party happy"
            dialogue_name : string
                The name of the guest as it should appear in their dialogue box
                when they arrive at the party e.g. "Long Cat"
            dialogue_what : string
                The guest's comment upon arriving at the party.
            """

            self.name = name
            self.thumbnail = thumbnail

            self.start_msg = start_msg
            self.msg1_good = msg1_good
            self.msg2_good = msg2_good
            self.msg3_good = msg3_good

            self.reply1_good = reply1_good
            self.reply2_good = reply2_good
            self.reply3_good = reply3_good

            self.reply1_bad = reply1_bad
            self.reply2_bad = reply2_bad
            self.reply3_bad = reply3_bad

            self.msg1_bad = msg1_bad
            self.msg2_bad = msg2_bad
            self.msg3_bad = msg3_bad

            # Make sure the name does not have spaces or apostrophes
            name = convert_to_file_name(name)

            self.label1 = name + '_reply1'
            self.label2 = name + '_reply2'
            self.label3 = name + '_reply3'

            self.attending = False

            self.large_img = large_img
            self.short_desc = short_desc
            self.personal_info = personal_info
            self.comment_who = comment_who
            self.comment_what = comment_what
            self.comment_img = comment_img
            self.dialogue_name = dialogue_name
            self.dialogue_what = dialogue_what

            # Attempt to set some of the comment info manually if not provided
            if not self.large_img:
                self.large_img = self.thumbnail
            if not self.short_desc:
                self.short_desc = ("No description was entered in this guest's"
                    + " Guest definition.")
            if not self.personal_info:
                self.personal_info = ("No personal info was given in this"
                    " guest's Guest definition")
            if not self.comment_who:
                self.comment_who = store.narrator
            if not self.comment_what:
                self.comment_what = "No comment was entered for this guest."
            if not self.dialogue_name:
                self.dialogue_name = string.capwords(self.name)
            if not self.dialogue_what:
                self.dialogue_what = "This guest was not given anything to say."

            # Add the guest to the guestbook
            if self.name not in store.persistent.guestbook:
                store.persistent.guestbook[self.name] = None
            if self not in store.all_guests:
                store.all_guests.append(self)

        def __eq__(self, other):
            """Check for equality between Guestv2 objects."""

            if self.v3_guest:
                return self.v3_guest.__eq__(other)

            if (getattr(other, 'name', False)
                    and getattr(other, 'thumbnail', False)):
                return (self.name == other.name
                        and self.thumbnail.split('.')[0]
                            == other.thumbnail.split('.')[0])
            else:
                return False

        def __ne__(self, other):
            """Check for inequality between Guestv2 objects."""

            if self.v3_guest:
                return self.v3_guest.__ne__(other)
            return not self.__eq__(other)

init python:
    class Email(renpy.store.object):
        """
        Class that holds information needed for an email's delivery, timeout,
        failure, and more.

        Attributes:
        -----------
        guest : Guest
            Guest object of the sender of this email.
        msg : string
            Content of the email.
        reply_label : string
            Label to jump to in order to reply to this email.
        msg_num : int (0-3)
            Reply number. 0 is the first message sent to the player, and
            3 is the email accepting the player's invitation.
        failed : bool
            True if this email chain has been failed.
        timeout_count : int
            If the player doesn't respond within this many chatrooms, the
            email is considered "timed out" and cannot be interacted with.
        deliver_reply : int or "wait"
            How many chatrooms the player must wait before the guest replies
            to their email, or "wait" if it's the player's turn to reply.
        reply : string or False
            Contains the message to be delivered when the guest replies
            to the player's message, or False if it's the player's turn
            to send a message.
        timeout : bool
            True if this message has timed out.
        sent_time : MyTime
            MyTime object containing the time the last email was sent at.
        read : bool
            True if this email has been read
        notified : bool
            True if the player has received a popup informing them of this
            email.
        before_branch : bool
            Only used for the tutorial guest. If True, the program attempts
            to finish sending emails before it reaches a plot branch.
        """

        def __init__(self, guest, msg, reply_label):
            """
            Create an Email object.

            Parameters:
            -----------
            guest : Guest
                Guest object of the sender of this email.
            msg : string
                Content of the email.
            reply_label : string
                Label to jump to in order to reply to this email.
            """

            self.guest = guest
            self.msg = msg
            self.reply_label = reply_label
            self.msg_num = 0
            self.failed = False
            self.timeout_count = 25
            self.deliver_reply = "wait"
            self.reply = False
            self.timeout = False
            self.sent_time = upTime()
            self.__read = False
            self.notified = False
            self.before_branch = (guest.thumbnail
                == "Email/Thumbnails/rainbow_unicorn_guest_icon.webp")

        def __eq__(self, other):
            """
            Check for equality between two Email objects.
            Allows this class to be persistent.
            """

            if getattr(other, 'guest', False):
                return self.guest == other.guest
            else:
                return False

        def __ne__(self, other):
            """Check for inequality between two Email objects."""

            if getattr(other, 'guest', False):
                return self.guest != other.guest
            else:
                return False

        @property
        def read(self):
            """Return whether this email has been read."""
            try:
                return self.__read
            except:
                pass
            try:
                return self.__dict__['read']
            except:
                pass
            try:
                return self.__dict__['_m1_email_system__read']
            except:
                return True

        @read.setter
        def read(self, new_status):
            """
            Set this email's read status and whether or not the guest is
            attending the party, if this email chain is finished.
            """

            self.__read = new_status
            self.set_attendance()
            return

        @property
        def num_emails(self):
            """Return the number of emails in a successful email chain."""

            return 3

        @property
        def can_reply(self):
            """Return True if this email can be replied to."""

            return self.reply_label and not self.reply and not self.timeout

        @property
        def status(self):
            """Return the status of this email chain."""

            if self.completed():
                # 3/3 messages correct
                return 'email_completed_3'
            elif self.is_failed():
                # 2/3 messages correct
                if self.second_msg() == 'email_good':
                    return 'email_completed_2'
                # 1/3 messages correct
                elif self.first_msg() == 'email_good':
                    return 'email_completed_1'
                # 0/3 messages correct
                else:
                    return 'email_failed'
            elif self.timeout:
                return 'email_timeout'
            return None

        @property
        def email_status_list(self):
            """Return a list of icons to use for each email reply."""

            return [self.first_msg(), self.second_msg(), self.third_msg()]



        def deliver(self):
            """
            Deliver the next email in the chain to the player and
            notify them of its delivery with a popup.
            """

            global email_list

            # If you're waiting on a reply, decrease the timer
            if self.deliver_reply != "wait":
                self.deliver_reply -= 1
                renpy.retain_after_load()

            # If it's the player's turn to reply, decrease the timeout counter,
            # unless this is the final message and there's no need to reply.
            # If this is the first message, show a popup
            elif (self.deliver_reply == "wait"
                    and self.msg_num <= 2
                    and not self.timeout):
                self.timeout_count -= 1
                if not self.notified and self.msg_num == 0 and not self.read:
                    # Notify the player of the delivered message
                    renpy.show_screen('email_popup', e=self)
                    self.notified = True
                    renpy.retain_after_load()
                    renpy.restart_interaction()

            # If the timeout counter reaches 0, timeout becomes True
            if (self.timeout_count == 0
                    and self.msg_num <= 2
                    and not self.failed):
                self.timeout = True
                renpy.retain_after_load()

            # If the timer <= 0 and there's a reply to be
            # delivered, deliver it
            if (self.deliver_reply != "wait"
                    and self.deliver_reply <= 0
                    and self.reply):
                self.read = False
                self.reply += "\n\n------------------------------------------------\n\n"
                self.msg = self.reply + self.msg
                self.reply = False
                self.sent_time = upTime()
                self.timeout_count = 25 # resets the timeout counter
                self.deliver_reply = "wait"
                email_list.remove(self)
                email_list.insert(0, self) # Moves to the front of the list
                renpy.restart_interaction()
                # Notify the player of the delivered message
                self.notified = True
                renpy.music.play(persistent.email_tone, 'sound')
                renpy.show_screen('email_popup', e=self)
                renpy.retain_after_load()


        def set_reply(self, iscorrect, deliver_reply=False):
            """Set the guest's reply and decide when it should be delivered."""

            test = False

            if iscorrect:
                if self.msg_num == 0:
                    self.reply = self.guest.reply1_good
                    self.reply_label = self.guest.label2
                elif self.msg_num == 1:
                    self.reply = self.guest.reply2_good
                    self.reply_label = self.guest.label3
                elif self.msg_num == 2:
                    self.reply = self.guest.reply3_good
                    self.reply_label = False
                self.add_msg(True)
            else:
                if self.msg_num == 0:
                    self.reply = self.guest.reply1_bad
                elif self.msg_num == 1:
                    self.reply = self.guest.reply2_bad
                elif self.msg_num == 2:
                    self.reply = self.guest.reply3_bad
                self.add_msg(False)
                self.failed = True
                self.reply_label = False

            # If a number is given, the reply will be delivered
            # within that many chatrooms. Otherwise, the program
            # calculates a number range for the email so it can
            # be delivered before the party
            if deliver_reply != False:
                self.deliver_reply = deliver_reply
            else:
                if not test:
                    max_num = num_future_timeline_items(self.before_branch) - 1
                    min_num = 1
                    msg_remain = 3 - self.msg_num
                    if msg_remain == 0:
                        msg_remain = 1
                    # The program ensures there are enough
                    # chatrooms left to finish delivering the
                    # emails e.g. if there are 30 chatrooms left
                    # and there are another 3 replies to deliver,
                    # max_num will be 10 and min_num will be 3, so
                    # the message will be delivered sometime after
                    # the next 3-10 chatrooms
                    max_num = min(max_num // msg_remain, 13)
                    min_num = max(max_num-7, 1)
                    if max_num <= min_num:
                        self.deliver_reply = min_num
                    else:
                        self.deliver_reply = renpy.random.randint(min_num,
                                                                    max_num)
                else:
                    self.deliver_reply = renpy.random.randint(5, 10)

            self.sent_time = upTime()
            self.timeout_count = 25
            self.set_attendance()
            renpy.retain_after_load()

        def set_attendance(self):
            """Set whether this guest is attending the party."""

            if self.completed():
                # 3/3 messages correct
                self.guest.attending = True
            elif self.timeout:
                self.guest.attending = False
            elif self.is_failed():
                # 2/3 messages correct
                if self.second_msg() == 'email_good':
                    self.guest.attending = renpy.random.choice([True,
                                                            True, False])
                # 1/3 messages correct
                elif self.first_msg() == 'email_good':
                    self.guest.attending = renpy.random.choice([True,
                                                            False, False])
                else:
                    self.guest.attending = False
            return

        def add_msg(self, iscorrect):
            """Add the player's message to the guest to the email."""

            the_msg = ""

            if iscorrect:
                if self.msg_num == 0:
                    the_msg = self.guest.msg1_good
                elif self.msg_num == 1:
                    the_msg = self.guest.msg2_good
                elif self.msg_num == 2:
                    the_msg = self.guest.msg3_good
            else:
                if self.msg_num == 0:
                    the_msg = self.guest.msg1_bad
                elif self.msg_num == 1:
                    the_msg = self.guest.msg2_bad
                elif self.msg_num == 2:
                    the_msg = self.guest.msg3_bad

            self.msg_num += 1
            the_msg += "\n\n------------------------------------------------\n\n"
            self.msg = the_msg + self.msg
            renpy.retain_after_load()

        def completed(self):
            """Return True if the email chain was successfully completed."""

            if self.failed or not self.read:
                return False
            if self.msg_num == 3 and self.reply == False:
                return True
            else:
                return False

        def is_failed(self):
            """Return True if the email chain was failed."""
            if self.failed and self.read and not self.reply:
                return True
            else:
                return False

        def first_msg(self):
            """Return the email icon for the first message."""

            if self.msg_num <= 0:
                return 'email_inactive'
            elif self.msg_num == 1 and self.failed:
                return 'email_bad'
            else:
                return 'email_good'

        def second_msg(self):
            """Return the email icon for the second message."""

            if self.msg_num <= 1:
                return 'email_inactive'
            elif self.msg_num == 2 and self.failed:
                return 'email_bad'
            else:
                return 'email_good'

        def third_msg(self):
            """Return the email icon for the third message."""

            if self.msg_num <= 2:
                return 'email_inactive'
            elif self.msg_num == 3 and self.failed:
                return 'email_bad'
            else:
                return 'email_good'

        def send_reply(self):
            """Send the email reply."""

            global email_reply
            email_reply = True
            renpy.call_in_new_context(self.reply_label)
            email_reply = False
            renpy.retain_after_load()
            return

        def send_sooner(self):
            """Increase the timeout and deliver_reply counters. For testing."""

            if self.deliver_reply != "wait":
                self.deliver_reply -= 5
            self.timeout_count -= 5




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
            elif save_img.startswith("save_"):
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

############################################
## OLD CHARACTER DEFINITIONS
############################################
## The game will now automatically create Phone and VN characters
## to speak dialogue in those situations.

define ja_phone = Character("Jaehee Kang",
    kind=phone_character, voice_tag="ja_voice")
define ju_phone = Character("Jumin Han",
    kind=phone_character, voice_tag="ju_voice")
define s_phone = Character("707",
    kind=phone_character, voice_tag="s_voice")
define sa_phone = Character("Saeran",
    kind=phone_character, voice_tag="sa_voice")
define r_phone = Character("Ray",
    kind=phone_character, voice_tag="sa_voice")
define ri_phone = Character("Rika",
    kind=phone_character, voice_tag="ri_voice")
define y_phone = Character("Yoosung★",
    kind=phone_character, voice_tag="y_voice")
define v_phone = Character("V",
    kind=phone_character, voice_tag="v_voice")
define va_phone = Character("Vanderwood",
    kind=phone_character)
define u_phone = Character("Unknown",
    kind=phone_character, voice_tag="sa_voice")
define z_phone = Character("Zen",
    kind=phone_character, voice_tag="z_voice")

define ja_vn = Character("Jaehee", kind=vn_character,
    window_color="#C8954D",
    who_color="#fff5eb", voice_tag="ja_voice",
    image="jaehee")
define ju_vn = Character("Jumin", kind=vn_character,
    window_color="#648EFC",
    who_color="#d2e6f7", voice_tag="ju_voice",
    image="jumin")
define r_vn = Character("Ray", kind=vn_character,
    window_color="#FC9796",
    who_color="#f2ebfd", voice_tag="sa_voice",
    image="saeran")
define ri_vn = Character("Rika", kind=vn_character,
    window_color="#A774CC",
    who_color="#fff9db", voice_tag="ri_voice",
    image="rika")
define s_vn = Character("707", kind=vn_character,
    window_color="#F54848",
    who_color="#fff1f1", voice_tag="s_voice",
    image="seven")
define sa_vn = Character("Saeran", kind=vn_character,
    window_color="#FC9796",
    who_color="#f2ebfd", voice_tag="sa_voice",
    image="saeran")
define u_vn = Character("???", kind=vn_character,
    window_color="#FC9796",
    who_color="#f2ebfd", voice_tag="sa_voice",
    image="saeran")
define v_vn = Character("V", kind=vn_character,
    window_color="#7ED4C7",
    who_color="#cbfcfc", voice_tag="v_voice",
    image="v")
define y_vn = Character("Yoosung", kind=vn_character,
    window_color="#75C480",
    who_color="#effff3", voice_tag="y_voice",
    image="yoosung")
define z_vn = Character("Zen", kind=vn_character,
    window_color="#929292",
    who_color="#d8e9f9", voice_tag="z_voice",
    image="zen")




# Dummy image definitions to stop lint from complaining they don't exist
image hack effect = Null()
image hack = Null()
image morning = Null()
image noon = Null()
image evening = Null()
image night = Null()
image rainy_day = Null()
image snowy_day = Null()
image morning_snow = Null()
image secure anim = Null()
image secure = Null()
image redhack effect = Null()
image hack effect reverse = Null()
image redhack effect reverse = Null()
image shake = Null()
image earlyMorn = Null()
image heart banner = Null()
image well banner = Null()
image lightning banner = Null()
image annoy banner = Null()