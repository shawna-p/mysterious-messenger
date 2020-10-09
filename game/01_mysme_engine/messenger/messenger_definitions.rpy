init -4 python:

    class ChatEntry(renpy.store.object):
        """
        Class that stores the information needed for each chatroom message.

        Attributes:
        -----------
        who : ChatCharacter
            ChatCharacter object of the sender of the message.
        what : string
            Dialogue of the message.
        thetime : MyTime
            MyTime object containing the time the message was sent at.
        img : bool
            True if this message contains an image, such as an emoji or a CG.
        bounce : bool
            True if this message should 'bounce' when it animates in. Used
            for glowing and special speech bubble variants.
        specBubble : string or Nonee
            String containing part of the image path to the relevant
            speech bubble.
        """

        def __init__(self, who, what, thetime, img=False,
                        bounce=False, specBubble=None):
            """
            Creates a ChatEntry object to display a message in the messenger.

            Parameters:
            -----------
            who : ChatCharacter
                ChatCharacter object of the sender of the message.
            what : string
                Dialogue of the message.
            thetime : MyTime
                MyTime object containing the time the message was sent at.
            img : bool
                True if this message contains an image, such as an emoji
                or a CG.
            bounce : bool
                True if this message should 'bounce' when it animates in.
                Used for glowing and special speech bubble variants.
            specBubble : string or None
                String containing part of the image path to the relevant
                speech bubble.
            """

            self.who = who
            self.what = what
            self.thetime = thetime
            self.img = img
            self.bounce = bounce
            self.specBubble = specBubble


        @property
        def name_style(self):
            """Return the name style for this message."""

            if self.who.right_msgr:
                return 'chat_name_MC'
            else:
                return 'chat_name'

        @property
        def name_frame_style(self):
            """Return the style for the frame around the chat name."""

            if self.who.right_msgr:
                return 'chat_name_frame_MC'
            else:
                return 'chat_name_frame'

        @property
        def has_new(self):
            """Return True if this message should have a NEW sign."""

            if self.bounce:
                return False
            elif self.who.right_msgr:
                return False
            elif self.img:
                return False
            return True

        def msg_animation(self, anti, no_anim):
            """Return the animation used for this message."""

            if anti and self.bounce:
                return invisible_bounce
            elif anti:
                return invisible

            if no_anim:
                return null_anim

            if self.bounce:
                return incoming_message_bounce
            else:
                return incoming_message

        @property
        def pfp_style(self):
            """Return the style for the profile picture."""

            if self.who.right_msgr:
                return 'MC_profpic'
            else:
                return 'profpic'

        @property
        def reg_text_style(self):
            """Return the style used for regular text messages."""

            if self.who.right_msgr:
                return 'text_msg_mc_fixed'
            else:
                return 'text_msg_npc_fixed'

        @property
        def text_bubble_style(self):
            """Return the style used for regular text message bubbles."""

            if self.who.right_msgr:
                return 'reg_bubble_MC_text'
            else:
                return 'reg_bubble_text'

        @property
        def text_img_style(self):
            """Return the style used for images in text messages."""

            if self.who.right_msgr:
                return 'mc_img_text_message'
            else:
                return 'img_text_message'

        @property
        def bubble_style(self):
            """Return the style used for regular bubbles."""

            if self.who.right_msgr:
                return 'reg_bubble_MC'
            elif not self.specBubble and not self.bounce:
                return 'reg_bubble'
            elif not self.specBubble and self.bounce:
                return 'glow_bubble'
            elif self.specBubble == "glow2":
                return 'glow_bubble'

            # Otherwise, there is a special bubble
            bubble_style = self.specBubble

            # Allow for custom bubble styling
            try:
                custom_style = custom_bubble_style(self)
                if custom_style:
                    return custom_style
            except:
                print("WARNING: Could not evaluate the function 'custom_"
                    + "bubble_style'.")
                renpy.show_screen('script_error',
                        message=("Could not evaluate the function 'custom_"
                            + "bubble_style'."))

            # Multiple round/square variants have the same styling as
            # the original round/square bubble
            if self.specBubble == "round2_s" and self.who.file_id == 's':
                return self.who.file_id + '_' + bubble_style

            if self.specBubble[:6] == "round2":
                bubble_style = "round_" + self.specBubble[-1:]
            elif self.specBubble[:7] == "square2":
                bubble_style = "square_" + self.specBubble[-1:]

            return self.who.file_id + '_' + bubble_style

        @property
        def spec_bubble_offset(self):
            """Return the offset used for this special bubble."""

            bubble_style = self.specBubble
            # Multiple round/square variants have the same styling as
            # the original round/square bubble
            if self.specBubble[:6] == "round2":
                bubble_style = "round_" + self.specBubble[-1:]
            elif self.specBubble[:7] == "square2":
                bubble_style = "square_" + self.specBubble[-1:]
            bubble_style += '_offset'

            # Allow for custom bubble styling
            try:
                custom_offset = custom_bubble_offset(self)
                if custom_offset:
                    return custom_offset
            except:
                print("WARNING: Could not evaluate the function 'custom_"
                    + "bubble_offset'.")
                renpy.show_screen('script_error',
                        message=("Could not evaluate the function 'custom_"
                            + "bubble_offset'."))

            ## Rule exceptions
            full_style = self.who.file_id + '_' + self.specBubble
            if full_style == 'ju_cloud_l':
                return (115, 5)
            elif full_style == 'ju_square_m':
                return (140, 5)
            elif full_style == 'ju_round_l':
                return (110, 27)
            elif full_style == 'ju_square_s':
                return (140, 10)
            elif full_style == 'ju_square_l':
                return (135, 0)
            elif full_style == 'ju_round_m':
                return (130, 30)
            elif full_style == 'ja_square_l':
                return (120, 10)
            elif full_style == 'ja_cloud_m':
                return (125, 35)
            elif full_style == 'ja_round_l':
                return (110, 8)
            elif full_style == 'ja_square_m':
                return (135, 15)
            elif full_style == 'r_square_l':
                return (120, 5)
            elif full_style == 'r_square2_l':
                return (110, 2)
            elif full_style == 'r_square_m' or full_style == 'r_square2_m':
                return (135, 10)
            elif full_style == 'v_square_l':
                return (120, 15)
            elif full_style == 'v_round_s':
                return (150, 25)
            elif full_style == 'v_square_s':
                return (135, 30)
            elif full_style == 's_cloud_l':
                return (128, 34)
            elif full_style == 's_round2_s':
                return (120, 28)
            elif full_style == 's_round2_l' or full_style == 's_round_l':
                return (110, 15)
            elif full_style == 'sa_square_m':
                return (125, 15)
            elif full_style == 'sa_square_s':
                return (125, 18)
            elif full_style == 'sa_square_l':
                return (120, 0)
            elif full_style == 'y_cloud_l':
                return (100, 22)
            elif full_style == 'y_cloud_m':
                return (110, 25)
            elif full_style == 'y_round_l':
                return (120, 20)
            elif full_style == 'z_square_l':
                return (105, 10)
            elif full_style == 'z_flower_l':
                return (115, 10)

            return getattr(store.gui, bubble_style)


        @property
        def img_style(self):
            """Return the style used for images."""

            if self.who.right_msgr:
                return 'mc_img_message'
            else:
                return 'img_message'

        @property
        def bubble_bg(self):
            """Return the background used for this bubble."""

            # Allow for custom bubble backgrounds
            try:
                custom_bg = custom_bubble_bg(self)
                if custom_bg:
                    return custom_bg
            except:
                print("WARNING: Could not evaluate the function 'custom_"
                    + "bubble_bg'.")
                renpy.show_screen('script_error',
                        message=("Could not evaluate the function 'custom_"
                            + "bubble_bg'."))

            # If this is a special bubble, set the background to said bubble
            if self.specBubble and self.specBubble != 'glow2':
                return ("Bubble/Special/" + self.who.file_id + "_"
                    + self.specBubble + ".webp")
            # Special case for the second glowing bubble variant
            elif self.specBubble and self.specBubble == 'glow2':
                return Frame("Bubble/Special/" + self.who.file_id
                    + "_" + self.specBubble + ".webp", 25, 25)
            # Glow bubble
            elif self.bounce:
                return self.who.glow_bubble_img
            # Regular speech bubble
            elif self.who != answer:
                return self.who.reg_bubble_img
            else:
                return None

        def alt_text(self, anti):
            """Return text for self-voicing."""

            if anti:
                return ""

            if self.img:
                return self.who.p_name + " sent a photo"
            else:
                return renpy.filter_text_tags(self.what,
                                    allow=gui.history_allow_tags)

        def alt_who(self, anti):
            """Return the messenger name for self-voicing."""

            if anti or self.img:
                return ""
            else:
                return self.who.p_name

        @property
        def dialogue_width(self):
            """Return the width of this dialogue."""

            return int(Text(self.what).size()[0])




    class ReplayEntry(renpy.store.object):
        """
        Class that stores the information needed for chatroom messages that
        are replayed in the history.

        Attributes:
        -----------
        who : ChatCharacter
            ChatCharacter object of the sender of the message.
        what : string
            Dialogue of the message.
        pauseVal : float or None
            Stores the pauseVal multiplier for this particular message.
        img : bool
            True if this message contains an image, such as an emoji or a CG.
        bounce : bool
            True if this message should 'bounce' when it animates in. Used
            for glowing and special speech bubble variants.
        specBubble : string or Nonee
            String containing part of the image path to the relevant
            speech bubble.
        """

        def __init__(self, who, what, pauseVal=None, img=False,
                        bounce=False, specBubble=None):
            """
            Creates a ChatEntry object to display a message in the messenger.

            Parameters:
            -----------
            who : ChatCharacter
                ChatCharacter object of the sender of the message.
            what : string
                Dialogue of the message.
            pauseVal : float or None
                Stores the pauseVal multiplier for this particular message.
            img : bool
                True if this message contains an image, such as an emoji
                or a CG.
            bounce : bool
                True if this message should 'bounce' when it animates in.
                Used for glowing and special speech bubble variants.
            specBubble : string or Nonee
                String containing part of the image path to the relevant
                speech bubble.
            """

            self.who = who
            self.what = what
            self.pauseVal = pauseVal
            self.img = img
            self.bounce = bounce
            self.specBubble = specBubble

    ##************************************
    ## For ease of adding Chatlog entries
    ##************************************

    def addchat(who, what, pauseVal, img=False, bounce=False, specBubble=None):
        """
        Function that adds entries to the chatlog. Calculates how long it
        should take this message to be posted and then waits the appropriate
        length of time.

        Parameters:
        -----------
        who : ChatCharacter
            ChatCharacter object of the sender of the message.
        what : string
            Dialogue of the message.
        pauseVal : float or None
            Stores the pauseVal multiplier for this particular message.
        img : bool
            True if this message contains an image, such as an emoji
            or a CG.
        bounce : bool
            True if this message should 'bounce' when it animates in.
            Used for glowing and special speech bubble variants.
        specBubble : string or None
            String containing part of the image path to the relevant
            speech bubble.

        Result:
        -------
            A new entry is added to the chatlog.
        """

        global choosing, pre_choosing, pv, chatbackup, oldPV, observing
        global persistent, cg_testing
        choosing = False
        pre_choosing = False

        # If the program didn't get an explicit pauseVal,
        # use the default one
        if ((store.timed_menu_dict
                    or store.c_menu_dict.get('showing_choices', None))
                and persistent.use_timed_menus):
            if pauseVal is None:
                pauseVal = persistent.timed_menu_pv
            else:
                pauseVal *= persistent.timed_menu_pv
        elif pauseVal is None:
            pauseVal = persistent.pv
        else:
            pauseVal *= persistent.pv

        # If this is the first message after "filler", it gets a pv of 0
        if (len(store.chatlog) > 0
                and store.chatlog[-1].who.name == 'filler'
                and not ((store.timed_menu_dict
                    or store.c_menu_dict.get('showing_choices', None))
                and persistent.use_timed_menus)):
            pauseVal = 0.1
        elif who.name == 'filler':
            pauseVal = 0


        # Now check to see if the most recent message was skipped
        # Pausing in the middle of the chat often causes the
        # program to skip a message, and this will catch that
        if who.file_id != 'delete':
            # This ensures the message that was supposed to
            # be posted was, in fact, posted
            if chatbackup:
                pauseFailsafe()
            # Store the current message in the backup
            chatbackup = ChatEntry(who, what, upTime(),
                                    img, bounce, specBubble)
            oldPV = pauseVal

        # Now calculate how long to wait before
        # posting messages to simulate typing time
        if pauseVal == 0:
            pass
        elif who.file_id == 'delete':
            messenger_pause(persistent.pv)
            return
        elif who.name in ['msg', 'filler']:
            messenger_pause(pauseVal, True)
        else:
            typeTime = calculate_type_time(what)
            typeTime = typeTime * pauseVal
            messenger_pause(typeTime, True)

        # If it's an image, first check if it's an emoji
        # If so, it has an associated sound file
        if img:
            # Try to adjust the {image=seven_wow} etc statement to
            # suit the emoji dictionary
            if "{image =" in what:
                first, last = what.split('=')
                if len(last) > 0 and last[0] == ' ':
                    last.pop(0)
                what = "{image=" + last
            if what in emoji_lookup:
                renpy.play(emoji_lookup[what], channel="voice_sfx")
            elif "{image" not in what and not observing:
                # Unlock the CG in the gallery
                cg_helper(what, who, True)

        # Some special bubbles will award the player with a heart icon
        award_hourglass(specBubble)

        # Add this entry to the chatlog
        chatlog.append(ChatEntry(who, what, upTime(),
                            img, bounce, specBubble))
        # Create a rollback checkpoint
        renpy.checkpoint()

    def calculate_type_time(what):
        """Return the length of time to pause for 'what'."""

        typeTime = what.count(' ') + 1 # equal to the # of words
        # Since average reading speed is 200 wpm or 3.3 wps
        typeTime = typeTime / 3.0
        if typeTime < 1.5:
            typeTime = 1.5
        return typeTime

    def messenger_pause(length, actually_wait=False):
        """Pause for length, unless skipping."""

        if actually_wait and renpy.is_skipping():
            renpy.pause(0.1)
            return
        if not renpy.is_skipping():
            renpy.pause(length)

    def award_hourglass(specBubble):
        """Show the hourglass icon and award the player a heart point."""

        if specBubble not in ['cloud_l', 'round_l', 'square_l', 'flower_l',
                'square2_l', 'round2_l']:
            return

        # Don't give HG when rewatching a chatroom, or not participating,
        # or if receiving hourglasses is turned off
        if (store.observing or store.current_timeline_item.currently_expired
                or not store.persistent.receive_hg):
            return

        if store.hourglass_bag.draw():
            if not persistent.animated_icons:
                renpy.show_screen(allocate_notification_screen(True),
                    message="Hourglass +1")
            else:
                renpy.show_screen(allocate_hg_screen())
            renpy.music.play("audio/sfx/UI/select_4.mp3", channel='sound')
            store.collected_hg += 1

        # Hourglass awards are pseudo-random. The program draws from a 'bag'
        # that contains 10 choices, two of which are True. If it gets True,
        # it shows an hourglass. If all the True options are gone, even if
        # there are many False options left, it resets the bag.
        if True not in store.hourglass_bag.bag:
            store.hourglass_bag.new_choices([ False for i in range(8) ]
                + [True for i in range(2) ])



    def pauseFailsafe():
        """
        Check if the previous entry was successfully added to the chatlog,
        and add it if it was missed.
        """

        global reply_instant
        if len(chatlog) > 0:
            last_chat = chatlog[-1]
        else:
            return
        if last_chat.who.file_id == 'delete':
            if len(chatlog) > 1:
                last_chat = chatlog[-2]
            else:
                return
        elif last_chat.who == filler:
            return

        if (last_chat.who.file_id == chatbackup.who.file_id
                and last_chat.what == chatbackup.what):
            # the last entry was successfully added; return
            return

        print_file("EXECUTING pause failsafe")

        # add the backup entry to the chatlog
        if reply_instant:
            reply_instant = False
        else:
            typeTime = chatbackup.what.count(' ') + 1
            typeTime = typeTime / 3
            if typeTime < 1.5:
                typeTime = 1.5
            typeTime = typeTime * oldPV
            messenger_pause(typeTime, True)

        if chatbackup.img:
            if "{image =" in chatbackup.what:
                first, last = chatbackup.what.split('=')
                if len(last) > 0 and last[0] == ' ':
                    last.pop(0)
                chatbackup.what = "{image=" + last
            if chatbackup.what in emoji_lookup:
                renpy.play(emoji_lookup[chatbackup.what], channel="voice_sfx")
            elif "{image" not in chatbackup.what and not observing:
                # Unlock the CG in the gallery
                cg_helper(what, who, True)

        award_hourglass(chatbackup.specBubble)

        chatlog.append(ChatEntry(chatbackup.who, chatbackup.what,
                                    upTime(), chatbackup.img,
                                    chatbackup.bounce,
                                    chatbackup.specBubble))

## The multiplier for chat speed. Default modifier is 0.8; increasing the
## speed by one level puts it at 0.8 - chat_speed_increment (so, 0.65)
define chat_speed_increment = 0.15
## The number of seconds to wait to post an enter/exit chatroom message.
define enter_exit_modifier = 1.1

init python:
    # Increase/decrease the chat speed
    # It goes 1.4, 1.25, 1.1, 0.95, 0.8, 0.65, 0.5, 0.35, 0.2
    def slow_pv():
        global persistent
        if persistent.pv <= 1.3:
            persistent.pv += store.chat_speed_increment
        store.pv = persistent.pv
        return

    def fast_pv():
        global persistent
        if persistent.pv >= 0.3:
            persistent.pv -= store.chat_speed_increment
        store.pv = persistent.pv
        return

    def glow_bubble_fn(glow_color='#000'):
        """Recolour a generic glowing bubble with the given colour."""

        return im.MatrixColor('Bubble/Special/sa_glow2.webp',
                            im.matrix.colorize(glow_color, '#fff'))

    def reg_bubble_fn(bubble_color='#000'):
        """Recolour a generic message bubble with the given colour."""

        return im.MatrixColor('Bubble/white-Bubble.webp',
                            im.matrix.colorize('#000', bubble_color))


## Note: There is also a custom version of the chat footers
## (pause/play/save & exit/answer) that you can use by setting
## this variable to True. Otherwise, it will use the original assets
## If you change the variable here, you need to start the game over
## Otherwise it can also be changed from the Settings menu
default persistent.custom_footers = False
# Values in order to keep the viewport scrolling
# to the bottom - set a ui.adjustment() object
# to infinity so it stays at the maximum range
define yadjValue = float("inf")
default yadj = ui.adjustment()
# Default nickname colour for the characters' names
default nickColour = "#000000"
# Default variable to adjust chat speed by
default pv = 0.8
default persistent.pv = 0.8
# These two values are used for the pauseFailSafe function
default chatbackup = ChatEntry(filler,"","")
default oldPV = pv

# Number of bubbles to keep on the screen at once
# (larger numbers may slow down the program; too
# small and there may not be enough to fill the screen)
default bubbles_to_keep = 20
# Keeps track of the current background for calls such as "shake"
default current_background = "morning"
# Semi-randomizes awarding hourglasses
default hourglass_bag = RandomBag([ False for i in range(8) ]
    + [True for i in range(2) ])




