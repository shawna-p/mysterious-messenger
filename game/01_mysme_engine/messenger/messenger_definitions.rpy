init -4 python:

    class ChatEntry(renpy.store.object):
        """
        Class that stores the information needed for each chatroom message.
        It contains many helper methods and properties to facilitate fetching
        the appropriate styles for each message.

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
        specBubble : string or None
            String containing part of the image path to the relevant
            speech bubble.
        saved_bubble_bg : string or None
            Saves the calculated bubble background, if applicable.
        saved_bubble_style : string or None
            Saves the calculated bubble style, if applicable.
        text_msg_font : string
            The font used for the text.
        link : bool
            True if this message is a link message.
        link_img : string
            The image used on the left side of a link message.
        link_title : string
            The title for a link message.
        link_text : string
            The clickable text for a link message.
        link_action : Screen Action
            The action to be performed when a link message is clicked.
        """

        def __init__(self, who, what, thetime, img=False,
                    bounce=False, specBubble=None, link_img=None,
                    link_title=None, link_text=None, link_action=None,
                    for_replay=None):
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
            link_img : string
                The image used on the left side of a link message.
            link_title : string
                The title for a link message.
            link_text : string
                The clickable text for a link message.
            link_action : Screen Action
                The action to be performed when a link message is clicked.
            for_replay : string
                A special field used in the chatroom creator to give
                instructions to the replay log.
            """

            self.who = who
            self.what = what
            self.thetime = thetime
            self.img = img
            self.bounce = bounce
            self.specBubble = specBubble

            self.saved_bubble_bg = None
            self.saved_bubble_style = None

            self.__text_msg_font = 'sser1'

            self.__link = link_img or link_title or link_text or link_action or False
            self.__link_img = link_img or 'Bubble/link_house_btn.webp'
            self.__link_title = link_title or ""
            self.__link_text = link_text
            self.__link_action = link_action

            self.for_replay = for_replay

        @property
        def album_obj(self):
            """
            If this message has an image relating to an in-game CG, return
            the CG image.
            """

            if self.what.startswith("cg "):
                # don't need to add cg to the start of this filepath
                filepath = self.what
            else:
                filepath = "cg " + self.what

            # Name of the album should be the letters before the first _
            # e.g. "cg common_1" -> common
            try:
                album_name = filepath.split('_')[0].split(' ')[1] + '_album'
                cg_list = getattr(store.persistent, album_name)
            except:
                ScriptError("Couldn't get album name from CG image \"", self.what, '"',
                header="CG Albums",
                subheader="Showing a CG in a Chatroom or Text Message")
                return

            if cg_list is None:
                try:
                    album_name = filepath.split('_')[0].split(' ')[1] + '_album'
                    cg_list = getattr(store, album_name)
                except:
                    ScriptError("Couldn't get album name from CG image \"", self.what, '"',
                    header="CG Albums",
                    subheader="Showing a CG in a Chatroom or Text Message")
                    return

            alb_obj = None
            for photo in cg_list:
                if photo.name == self.what or photo.name == filepath:
                    alb_obj = photo
                    photo.unlock()
                    break

                elif Album(filepath) == photo:
                    alb_obj = photo
                    photo.unlock()
                    break

            # Ensure the album for this photo is visible in the album screen.
            # Useful if you've hidden an album until an image in it is unlocked.
            if filepath.split('_')[0].split(' ')[1] not in store.all_albums:
                store.all_albums.append(filepath.split('_')[0].split(' ')[1])

            if alb_obj:
                return alb_obj

            return filepath

        @property
        def text_msg_what(self):
            """Return `what` with the font removed, for text messages."""

            text_what = self.what
            deny_list = [ x for x in get_dict_keys(font_dict) ]
            deny_list.append("font")
            deny_list.append("=")
            text_what = renpy.filter_text_tags(text_what, deny=deny_list)
            for tag in deny_list:
                remove = "{=" + tag + "}"
                if remove in text_what:
                    self.text_msg_font = tag
                    text_what = text_what.replace(remove, '')
                    remove = "{/=" + tag + "}"
                    text_what = text_what.replace(remove, '')
            return text_what

        @property
        def text_msg_font(self):
            """Return the font the text message should be displayed in."""

            try:
                return store.font_dict[self.__text_msg_font]
            except Exception as e:
                print_file("Exception with text font:", e)
            try:
                return getattr(store, self.__text_msg_font)
            except:
                return store.font_dict['sser1']

        @text_msg_font.setter
        def text_msg_font(self, ffont):
            try:
                if ffont in get_dict_keys(store.font_dict):
                    self.__text_msg_font = ffont
                else:
                    ScriptError("Given font \"", ffont, "\" is not in the",
                        "font dictionary.",
                        header="Chatrooms", subheader="Custom Fonts")
            except:
                self.__text_msg_font = 'sser1'

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
            elif self.link:
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
        def link_bubble_bg(self):
            """Return the background used for link messages."""

            try:
                c = Color(self.who.bubble_color)
                c = self.who.bubble_color
            except:
                # Couldn't initialize this as a colour
                c = "#fff"

            if self.link_action:
                # Return yellow flashing version
                return Fixed(Frame(Transform('Bubble/link_bubble.webp',
                        matrixcolor=ColorizeMatrix('#000', c)), 25, 25),
                    At(Frame(Transform('Bubble/link_bubble.webp',
                        matrixcolor=ColorizeMatrix('#000', "#e2ca53")),
                        25, 25), flash_yellow))
            else:
                return Frame(Transform('Bubble/link_bubble.webp',
                    matrixcolor=ColorizeMatrix('#000', c)), 25, 25)

        @property
        def link_img(self):
            """
            Return the image that should be used on the left of a
            posted link message.
            """

            try:
                if self.link:
                    return self.__link_img or 'Bubble/link_house_btn.webp'
                else:
                    return None
            except:
                return None

        @property
        def link_title(self):
            """Return the title for a link message."""

            try:
                if self.link and self.__link_title:
                    return self.__link_title
                else:
                    return None
            except:
                return None

        @property
        def link_text(self):
            """Return the text associated with this link message."""

            try:
                if self.link:
                    return self.__link_text or self.what or "Click Link"
                else:
                    return None
            except:
                return None

        @property
        def link_action(self):
            """Return the action associated with this link message."""

            try:
                if not self.link:
                    return None
                if not self.__link_action:
                    return None
                elif isinstance(self.__link_action, tuple):
                    # It's conditional on chat_stopped
                    if chat_stopped:
                        link_act = self.__link_action[0]
                    else:
                        link_act = self.__link_action[1]
                    if not link_act:
                        return None
                else:
                    link_act = self.__link_action

                if ((store.observing and not store._in_replay)
                        or (_menu and not main_menu)):
                    # Just replaying the chat in-game, or the player
                    # has paused the game (and should only be able to
                    # click CG links).
                    if (isinstance(link_act, ShowCG)):
                        return link_act
                    return None # Shouldn't have buttons in a replay
                elif (not isinstance(link_act, ShowCG)):
                    # Deactivate the button after it's been clicked once
                    the_action = [SetField(self, 'link_action', None)]
                    if isinstance(link_act, list):
                        the_action.extend(link_act)
                    else:
                        the_action.append(link_act)
                    return the_action
                elif link_act:
                    # This just shows a CG; don't need to remove the action
                    return link_act
                return None
            except:
                return None

        @link_action.setter
        def link_action(self, new_action):
            try:
                self.__link_action = new_action
            except:
                return

        @property
        def link(self):
            """Return whether this message is a link message."""

            try:
                return self.__link
            except:
                return False

        @property
        def bubble_style(self):
            """Return the style used for regular bubbles."""

            try:
                if self.saved_bubble_style is not None:
                    return self.saved_bubble_style
            except:
                pass

            # Allow for custom bubble styling
            try:
                custom_style = custom_bubble_style(self)
                if custom_style:
                    self.saved_bubble_style = custom_style
                    return custom_style
            except:
                ScriptError("Could not evaluate the function",
                    "'custom_bubble_style'.",
                    header="Chatrooms",
                    subheader="Custom Bubble Style Function")

            if self.who.right_msgr and not self.specBubble and not self.bounce:
                self.saved_bubble_style = 'reg_bubble_MC'
                return self.saved_bubble_style
            elif not self.specBubble and not self.bounce:
                if self.link:
                    self.saved_bubble_style = 'link_bubble'
                else:
                    self.saved_bubble_style = 'reg_bubble'
                return self.saved_bubble_style
            elif not self.specBubble and self.bounce:
                self.saved_bubble_style = 'glow_bubble'
                return self.saved_bubble_style
            elif self.specBubble in ["glow2", "glow3"]:
                self.saved_bubble_style = 'glow_bubble'
                return self.saved_bubble_style

            # Otherwise, there is a special bubble
            bubble_style = self.specBubble

            # Multiple round/square variants have the same styling as
            # the original round/square bubble
            if self.specBubble == "round2_s" and self.who.file_id == 's':
                self.saved_bubble_style = self.who.file_id + '_' + bubble_style
                return self.saved_bubble_style
            elif self.specBubble == "s_round2_s":
                self.saved_bubble_style = bubble_style
                return self.saved_bubble_style

            try:
                stylename = self.who.file_id + '_' + bubble_style
                if self.specBubble[-8:-2] == "round2":
                    bubble_style = "round_" + self.specBubble[-1]
                #elif self.specBubble[-9:-2] == "square2":
                #    bubble_style = "square_" + self.specBubble[-1]

                # Check if a character is using someone else's bubble
                if len(self.specBubble.split('_')) > 2:
                    if self.specBubble == bubble_style:
                        stylename = bubble_style
                    else:
                        stylename = self.specBubble.split('_')[0] + "_" + bubble_style
                else:
                    stylename = self.who.file_id + '_' + bubble_style
            except:
                pass

            try:
                renpy.style.get_style(stylename)
                self.saved_bubble_style = stylename
                return stylename
            except:
                # This style does not exist
                pass
            try:
                renpy.style.get_style(bubble_style)
                self.saved_bubble_style = bubble_style
                return bubble_style
            except:
                if self.who.right_msgr:
                    self.saved_bubble_style = 'reg_bubble_MC'
                    return self.saved_bubble_style
                ScriptError("Could not find the style", bubble_style,
                    header="Chatrooms",
                    subheader="Custom Bubbles")
            self.saved_bubble_style = 'default'
            return 'default'

        @property
        def spec_bubble_offset(self):
            """Return the offset used for this special bubble."""

            bubble_style = self.specBubble
            # Multiple round/square variants have the same styling as
            # the original round/square bubble
            try:
                if self.specBubble[-8:-2] == "round2":
                    bubble_style = "round_" + self.specBubble[-1:]
                elif self.specBubble[-9:-2] == "square2":
                    bubble_style = "square_" + self.specBubble[-1:]
                elif len(self.specBubble.split('_')) > 2:
                    bubble_style = '_'.join(self.specBubble.split('_')[1:])
            except:
                pass
            bubble_style += '_offset'

            # Allow for custom bubble styling
            try:
                custom_offset = custom_bubble_offset(self)
                if custom_offset:
                    return custom_offset
            except:
                ScriptError("Could not evaluate the function",
                    "'custom_bubble_offset'.",
                    header='Chatrooms',
                    subheader="Custom Bubble Offset Function")

            ## Rule exceptions
            if len(self.specBubble.split('_')) > 2:
                full_style = self.specBubble
            else:
                full_style = self.who.file_id + '_' + self.specBubble

            if full_style == 'ju_square_m':
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

            # Try for the specific style
            try:
                return getattr(store.gui, self.who.file_id + "_" + bubble_style)
            except:
                pass

            try:
                return getattr(store.gui, bubble_style)
            except:
                pass
            return (0, 0)

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

            try:
                if self.saved_bubble_bg is not None:
                    return self.saved_bubble_bg
            except:
                pass

            # Allow for custom bubble backgrounds
            try:
                custom_bg = custom_bubble_bg(self)
                if custom_bg:
                    self.saved_bubble_bg = custom_bg
                    return custom_bg
            except Exception as e:
                ScriptError("Could not evaluate the function",
                    "'custom_bubble_bg'.", header="Chatrooms",
                    subheader="Custom Bubble Background Function")

            # If this is a special bubble, set the background to said bubble
            # Is a character trying to use someone else's bubble?
            if self.specBubble and len(self.specBubble.split('_')) > 2:
                self.saved_bubble_bg = "Bubble/Special/" + self.specBubble + ".webp"
                return self.saved_bubble_bg

            if self.specBubble and self.specBubble not in ['glow2', 'glow3']:
                # First, check if there's a specific variant for the character
                possible_ext = [".webp", ".png", ".jpg"]
                bubble_name = ("Bubble/Special/" + self.who.file_id + "_"
                    + self.specBubble)
                for ext in possible_ext:
                    if renpy.loadable(bubble_name + ext):
                        self.saved_bubble_bg = bubble_name + ext
                        return bubble_name + ext
                bubble_name = "Bubble/Special/" + self.specBubble
                for ext in possible_ext:
                    if renpy.loadable(bubble_name + ext):
                        self.saved_bubble_bg = bubble_name + ext
                        return bubble_name + ext
                ScriptError("Could not find bubble background for",
                    self.specBubble, header="Chatrooms",
                    subheader="Custom Bubbles")
                self.saved_bubble_bg = None
                return None
            # Special case for the second glowing bubble variant
            elif self.specBubble and self.specBubble in ['glow2', 'glow3']:
                self.saved_bubble_bg = Frame("Bubble/Special/" + self.who.file_id
                    + "_" + self.specBubble + ".webp", 25, 25)
                return self.saved_bubble_bg
            # Glow bubble
            elif self.bounce:
                self.saved_bubble_bg = self.who.glow_bubble_img
                return self.saved_bubble_bg
            # Regular speech bubble
            elif self.who != answer:
                self.saved_bubble_bg = self.who.reg_bubble_img
                return self.saved_bubble_bg
            else:
                self.saved_bubble_bg = None
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
        are replayed from the Timeline screen.

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
        specBubble : string or None
            String containing part of the image path to the relevant
            speech bubble.
        link_img : string
            The image used on the left side of a link message.
        link_title : string
            The title for a link message.
        link_text : string
            The clickable text for a link message.
        link_action : Screen Action
            The action to be performed when a link message is clicked.
        """

        def __init__(self, who, what, pauseVal=None, img=False,
                        bounce=False, specBubble=None, link_img=None,
                        link_title=None, link_text=None, link_action=None):
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
            specBubble : string or None
                String containing part of the image path to the relevant
                speech bubble.
            link_img : string
                The image used on the left side of a link message.
            link_title : string
                The title for a link message.
            link_text : string
                The clickable text for a link message.
            link_action : Screen Action
                The action to be performed when a link message is clicked.
            """

            self.who = who
            self.what = what
            self.pauseVal = pauseVal
            self.img = img
            self.bounce = bounce
            self.specBubble = specBubble

            self.link_img = link_img
            self.link_title = link_title
            self.link_text = link_text
            self.link_action = link_action

    ##************************************
    ## For ease of adding Chatlog entries
    ##************************************

    def addchat(who, what, pauseVal, img=False, bounce=False, specBubble=None,
            link_img=None, link_title=None, link_text=None, link_action=None):
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
                and persistent.use_timed_menus
                and not store._in_replay):
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
                and persistent.use_timed_menus
                and not store._in_replay)):
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
                                    img, bounce, specBubble,
                                    link_img, link_title, link_text,
                                    link_action)
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
            show_msg_img(what, who)

        # Some special bubbles will award the player with a heart icon
        award_hourglass_auto(specBubble)

        # Add this entry to the chatlog
        chatlog.append(ChatEntry(who, what, upTime(),
                            img, bounce, specBubble,
                            link_img=link_img, link_title=link_title,
                            link_text=link_text, link_action=link_action))
        # Scroll to the bottom to see it
        if (not in_chat_creator) or is_main_menu_replay:
            if abs(store.yadj.range - store.yadj.value) < 200:
                # Adjust it if it's within 200 pixels of the bottom
                store.yadj.value = yadjValue
                # Reset the bubble value
                store.num_bubbles = store.bubbles_to_keep
            else:
                # They're not near the bottom; increase the bubbles
                # on-screen so it doesn't nudge them away
                store.num_bubbles += 1
        # Create a rollback checkpoint
        renpy.checkpoint()

    def show_msg_img(what, who):
        """
        Play the emoji sound effect associated with what, if it exists.
        Otherwise, unlock the CG in the gallery.
        """

        # Try to adjust the {image=seven_wow} etc statement to
        # suit the emoji dictionary
        if "{image =" in what:
            first, last = what.split('=')
            last.strip()
            what = "{image=" + last
        if what in emoji_lookup:
            try:
                if not renpy.music.get_playing('voice_sfx'):
                    renpy.play(emoji_lookup[what], channel='voice_sfx')
                elif not renpy.music.get_playing('voice_sfx2'):
                    renpy.play(emoji_lookup[what], channel='voice_sfx2')
                elif not renpy.music.get_playing('voice_sfx3'):
                    renpy.play(emoji_lookup[what], channel='voice_sfx3')
                else:
                    renpy.play(emoji_lookup[what], channel='voice_sfx')
            except:
                ScriptError("Could not find sound file in the emoji",
                    "dictionary associated with \"", what, "\".",
                    header="Miscellaneous",
                    subheader="Custom Emojis")
        elif "{image" not in what and not observing:
            # Unlock the CG in the gallery
            cg_helper(what, who, True)
        return

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

        if in_chat_creator and not is_main_menu_replay:
            return

        if actually_wait and renpy.is_skipping():
            renpy.pause(0.1)
            return
        if not renpy.is_skipping() and isinstance(length, (int, float)):
            renpy.pause(length)

    def award_hourglass_auto(specBubble):
        """Show the hourglass icon and award the player a heart point."""

        if specBubble not in store.hourglass_bubbles:
            return

        # Don't give HG when rewatching a chatroom, or not participating,
        # or if receiving hourglasses is turned off
        if (store.observing or store.current_timeline_item.currently_expired
                or not store.persistent.receive_hg
                or store.is_main_menu_replay):
            return

        if store.hourglass_bag.draw():
            if not persistent.animated_icons:
                popup_tag = get_random_screen_tag()
                renpy.show_screen('stackable_notifications',
                    hide_screen=popup_tag,
                    message="Hourglass +1", _tag=popup_tag)
            else:
                popup_tag = get_random_screen_tag()
                renpy.show_screen('hourglass_animation', hide_screen=popup_tag,
                    _tag=popup_tag)
            renpy.music.play("audio/sfx/UI/select_4.mp3", channel='sound')
            store.collected_hg += 1

        # Hourglass awards are pseudo-random. The program draws from a 'bag'
        # that contains 10 choices, two of which are True. If it gets True,
        # it shows an hourglass. If all the True options are gone, even if
        # there are many False options left, it resets the bag.
        if True not in store.hourglass_bag.bag:
            store.hourglass_bag.new_choices([ False for i in range(8) ]
                + [True for i in range(2) ])

    def award_hourglass(random=False, force=False):
        """
        Show the hourglass icon and award the player a heart point.
        Triggered manually.
        """

        if force:
            pass
        elif (store.observing or store.current_timeline_item.currently_expired
                or not store.persistent.receive_hg
                or store.is_main_menu_replay):
            return

        if force or not random or store.hourglass_bag.draw():
            # Give the hourglass
            if not persistent.animated_icons:
                popup_tag = get_random_screen_tag()
                renpy.show_screen('stackable_notifications',
                    hide_screen=popup_tag,
                    message="Hourglass +1", _tag=popup_tag)
            else:
                popup_tag = get_random_screen_tag()
                renpy.show_screen('hourglass_animation', hide_screen=popup_tag,
                    _tag=popup_tag)
            renpy.music.play("audio/sfx/UI/select_4.mp3", channel='sound')
            store.collected_hg += 1

        # Refill the hourglass bag, if needed
        if True not in store.hourglass_bag.bag:
            store.hourglass_bag.new_choices([ False for i in range(8) ]
                + [True for i in range(2) ])

    def chatbackup_posted():
        """Return True if the chatbackup was posted successfully."""

        global chatlog

        if in_chat_creator and not is_main_menu_replay:
            return True

        if len(chatlog) > 0:
            last_chat = chatlog[-1]
        else:
            return True

        if chatbackup is None:
            return True

        if last_chat.who.file_id == 'delete':
            if len(chatlog) > 1:
                last_chat = chatlog[-2]
            else:
                return True
        elif last_chat.who == store.filler:
            return True

        if (last_chat.who.file_id == chatbackup.who.file_id
                and last_chat.what == chatbackup.what):
            # the last entry was successfully added; return
            return True
        return False

    def pauseFailsafe(wait=True):
        """
        Check if the previous entry was successfully added to the chatlog,
        and add it if it was missed.
        """

        global reply_instant, chatbackup
        if chatbackup_posted():
            return

        print_file("EXECUTING pause failsafe")

        # add the backup entry to the chatlog
        if reply_instant:
            reply_instant = False
        elif wait:
            typeTime = chatbackup.what.count(' ') + 1
            typeTime = typeTime / 3.0
            if typeTime < 1.5:
                typeTime = 1.5
            typeTime = typeTime * oldPV
            messenger_pause(typeTime, True)

        if chatbackup.img:
            show_msg_img(chatbackup.what, chatbackup.who)

        award_hourglass_auto(chatbackup.specBubble)

        chatlog.append(ChatEntry(chatbackup.who, chatbackup.what,
                                    upTime(), chatbackup.img,
                                    chatbackup.bounce,
                                    chatbackup.specBubble,
                                    chatbackup.link_img,
                                    chatbackup.link_title,
                                    chatbackup.link_text,
                                    chatbackup.link_action))
        chatbackup = None

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

        return Transform('Bubble/Special/sa_glow2.webp',
            matrixcolor=ColorizeMatrix(glow_color, "#fff"))

    def reg_bubble_fn(bubble_color='#000'):
        """Recolour a generic message bubble with the given colour."""

        return Transform('Bubble/white-Bubble.webp',
            matrixcolor=ColorizeMatrix("#000", bubble_color))

    def reset_participants(participants=None):
        if participants is None:
            participants = [ ]
        store.in_chat = [ ]
        for person in participants:
            store.in_chat.append(person.name)
            if not observing:
                store.current_timeline_item.add_participant(person)


## There is a custom version of the chat footers (pause/play/save&exit/answer)
## that you can use by setting this variable to True. Otherwise, it will use
## the original assets. It can also be changed from the Settings menu.
default persistent.custom_footers = False
# Values in order to keep the viewport scrolling
# to the bottom - set a ui.adjustment() object
# to infinity so it stays at the maximum range
define yadjValue = float("inf")
default yadj = ui.adjustment()
# Default nickname colour for the characters' names
default nickColour = "#000000"
# Default variable to adjust chat speed by
default persistent.pv = 0.8
# These two values are used for the pauseFailSafe function
default chatbackup = ChatEntry(filler,"","")
default oldPV = 0.8
# Number of bubbles to keep on the screen at once
# (larger numbers may slow down the program; too
# small and there may not be enough to fill the screen)
default bubbles_to_keep = 20
# The number of bubbles that's *actually* on-screen. May be adjusted
# if the player isn't constantly at the bottom of the screen.
default num_bubbles = bubbles_to_keep
# Keeps track of the current background for calls such as "shake"
default current_background = "morning"
# Semi-randomizes awarding hourglasses
default hourglass_bag = RandomBag([ False for i in range(8) ]
    + [True for i in range(2) ])




