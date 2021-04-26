python early:

    class ChatCharacter(renpy.store.object):
        """
        Class that stores ChatCharacters along with relevant information
        such as their profile picture and file id.

        Attributes:
        -----------
        name : string
            Name of the character (may be a nickname e.g. "707").
        file_id : string
            String appended to file names associated with this character,
            such as speech bubbles.
        big_prof_pic : string
            File path to the large version of this character's profile picture.
        default_prof_pic : string
            File path to the original "default" profile picture for this
            character.
        homepage_pic : string
            File path to the image used on the homepage to display this
            character's profile.
        seen_updates : bool
            False if this character has updated their profile picture, status,
            or cover photo and the player has not yet clicked their profile.
        prof_pic : string
            File path to the image used for this character's profile picture.
            Expected size is 110x110. A larger version, up to 314x314 pixels,
            can be provided with the same file name + "-b" e.g. if prof_pic is
            "ja-default.webp", the program searches for a file called
            "ja-default-b.webp" for the big profile picture.
        bonus_pfp : string
            File path to the profile picture the player can manually set for
            this character. It automatically gets priority over their default
            profile picture.
        participant_pic : string
            File path to the "participant" picture for this character. Used
            on the Timeline screen to indicate this character was present.
        cover_pic : string
            File path to the cover photo for this character.
        status : string
            This character's current status update.
        voicemail : PhoneCall
            The PhoneCall object to jump to when this character doesn't
            pick up the phone.
        heart_points : int
            The number of heart points the player has earned with this
            character.
        good_heart : int
            The number of good heart points the player has earned with
            this character.
        bad_heart : int
            The number of bad heart points the player has earned with this
            character.
        heart_color : string
            A string denoting the colour of the heart point associated with
            this character. Typically of the format "#000000".
        glow_color : string
            A string denoting the colour of the glowing speech bubble
            associated with this character. Typically of the format "#000000".
        bubble_color : string
            A string denoting the colour of the character's regular speech
            bubbles. Typically in the format "#000000"
        right_msgr : bool
            True if this character is sending messages on the right side
            of the screen (usually only true for the MC).
        reg_bub_img : Displayable
            A Ren'Py displayable of the image used for this character's
            speech bubble.
        glow_bubble_img : Displayable
            A Ren'Py displayable of the image used for this character's
            glowing speech bubble.
        emote_list : string[] or False
            A list of the "{image=...}" lines corresponding to all emojis
            associated with this character. Currently unused.
        text_msg : TextMessage
            Stores text messages conversations with this character.
        real_time_text : bool
            True if text message conversations with this character should
            be carried out in real-time.
        phone_char : Character
            Character object associated with this character. Used for phone
            dialogue.
        vn_char : Character
            Character object associated with this character. Used for Visual
            Novel (VN) mode dialogue.
        p_name : string
            A string with the phoenetic pronunciation of this character's
            name. Used for self-voicing e.g. "seven oh seven"
        """

        def __init__(self, name, file_id=False, prof_pic=False,
                participant_pic=False, heart_color='#000000',
                cover_pic=False, status=False, bubble_color=False,
                glow_color=False, emote_list=False, voicemail=False,
                right_msgr=False, homepage_pic=False,
                phone_char=False, vn_char=False,
                pronunciation_help=False, voice_tag='other_voice',
                vn_name=renpy.character.NotSet, **properties
                ):

            """
            Creates a ChatCharacter object for use in the messenger.

            Parameters:
            -----------
            name : string
                Name of the character (may be a nickname e.g. "707").
            file_id : string
                String appended to file names associated with this character,
                such as speech bubbles.
            prof_pic : string
                File path to the image used for this character's profile
                picture. Expected size is 110x110. A larger version, up to
                314x314 pixels, can be provided with the same file name + "-b"
                e.g. if prof_pic is "ja-default.webp", the program searches for
                a file called "ja-default-b.webp" for the big profile picture.
            participant_pic : string
                File path to the "participant" picture for this character. Used
                on the Timeline screen to indicate this character was present.
            heart_color : string
                A string denoting the colour of the heart point associated with
                this character. Typically of the format "#000000".
            cover_pic : string
                File path to the cover photo for this character.
            status : string
                This character's current status update.
            bubble_color : string
                A string denoting the colour of the character's regular speech
                bubbles. Typically in the format "#000000"
            glow_color : string
                A string denoting the colour of the glowing speech bubble
                associated with this character. Typically formatted "#000000".
            emote_list : string[] or False
                A list of the "{image=...}" lines corresponding to all emojis
                associated with this character. Currently unused.
            voicemail : string
                The voicemail label to jump to when this character doesn't
                pick up the phone.
            right_msgr : bool
                True if this character is sending messages on the right side
                of the screen (usually only true for the MC).
            homepage_pic : string
                File path to the image used on the homepage to display this
                character's profile.
            phone_char : Character
                Character object associated with this character. Used for phone
                dialogue.
            vn_char : Character
                Character object associated with this character. Used for
                Visual Novel (VN) mode dialogue.
            pronunciation_help : string or False
                A string with the phoenetic pronunciation of this character's
                name. Used for self-voicing e.g. "seven oh seven"
            voice_tag : string
                The voice tag associated with this character for VN and
                phone calls.
            vn_name : string
                The name that should be used for this character during Story
                Mode (VN) sections. If not given, defaults to their chat name.
            """

            self.in_init = True

            self.name = name
            self.file_id = file_id
            self.big_prof_pic = prof_pic
            self.__prof_pic = False
            self.prof_pic = prof_pic
            if self.__prof_pic == False and self.file_id and self.file_id != 'delete':
                print("WARNING: Couldn't set profile picture to", prof_pic)
            self.default_prof_pic = prof_pic
            if not homepage_pic:
                self.homepage_pic = prof_pic
            else:
                self.homepage_pic = homepage_pic
            self.__seen_updates = False
            self.__bonus_pfp = None

            self.participant_pic = participant_pic
            self.cover_pic = cover_pic
            self.status = status
            if voicemail:
                self.__voicemail = PhoneCall(self, voicemail, 'voicemail',
                                            2, True)
            else:
                self.__voicemail = PhoneCall(self,
                                    'voicemail_1', 'voicemail', 2, True)

            # All heart points start at 0
            self.__heart_points = 0
            self.__good_heart = 0
            self.__bad_heart = 0
            self.heart_color = heart_color
            self.glow_color = glow_color
            self.bubble_color = bubble_color
            if self.bubble_color:
                # This is typically also the color of the character's name
                if not properties.get('who_color', False):
                    properties['who_color'] = self.bubble_color
            self.right_msgr = right_msgr

            self.emote_list = emote_list

            self.text_msg = TextMessage(self)
            self.real_time_text = False

            if vn_name is renpy.character.NotSet:
                vn_name = self.name

            if phone_char:
                self.phone_char = phone_char
            else:
                self.phone_char = Character(vn_name, kind=phone_character,
                    voice_tag=voice_tag)
            if vn_char:
                self.vn_char = vn_char
            else:
                self.vn_char = Character(vn_name, kind=vn_character,
                    voice_tag=voice_tag, **properties)

            if pronunciation_help:
                self.p_name = pronunciation_help
            else:
                self.p_name = self.name

            self.in_init = False

            try:
                # Any initialized character should go in all_characters
                if (self not in store.all_characters and self.prof_pic
                        and self.file_id):
                    store.all_characters.append(self)
            except AttributeError:
                # Generally expected for a character like name_only
                return

        @property
        def vn_name(self):
            return self.vn_char.name

        @vn_name.setter
        def vn_name(self, new_name):
            self.vn_char.name = new_name
            self.phone_char.name = new_name

        def greet_img(self, scale=1.0):
            """
            Return the greet image associated with this character,
            or their homepage picture if one isn't provided.
            """

            if renpy.get_registered_image('greet ' + self.file_id):
                return Transform('greet ' + self.file_id, zoom=scale)
            else:
                return Transform(self.homepage_pic, size=(110*scale, 110*scale))


        @property
        def reg_bubble_img(self):

            if not self.file_id:
                return Frame("Bubble/white-Bubble.webp", 25,18,18,18)

            if not self.bubble_color:
                reg_bub_img = "Bubble/" + self.file_id + "-Bubble.webp"
                # Can't find the image
                if not renpy.loadable(reg_bub_img):
                    ScriptError("Could not find the image \"", reg_bub_img,
                        "\" for use as a regular bubble.",
                        header="Creating Characters",
                        subheader="Adding a New Character to Chatrooms")
                    reg_bub_img = "cannot_find_img"
                # This person is the messenger; typically MC
                if self.right_msgr:
                    reg_bub_img = Transform(reg_bub_img, xzoom=-1)
                    return Frame(reg_bub_img, 18,18,25,18)
                else:
                    return Frame(reg_bub_img, 25,18,18,18)
            else:
                # Check if the program was given a valid colour
                try:
                    c = Color(self.bubble_color)
                    reg_bub_img = reg_bubble_fn(self.bubble_color)
                except:
                    # Couldn't initialize this as a colour
                    ScriptError("Could not recognize \"", self.bubble_color,
                        "\" as a color for a regular speech bubble.",
                        header="Creating Characters",
                        subheader="Adding a New Character to Chatrooms")
                    reg_bub_img = reg_bubble_fn("cannot_find_img")

                if self.right_msgr:
                    reg_bub_img = Transform(reg_bub_img, xzoom=-1)
                    return Frame(reg_bub_img, 18,18,25,18)
                else:
                    return Frame(reg_bub_img, 25,18,18,18)

        @property
        def glow_bubble_img(self):

            if not self.file_id:
                return Frame("Bubble/Special/sa_glow2.webp", 25,25)

            if not self.glow_color:
                glow_bub_img = "Bubble/" + self.file_id + "-Glow.webp"
                if not renpy.loadable(glow_bub_img):
                    ScriptError("Could not find the image \"", glow_bub_img,
                        "\" for use as a glowing bubble.",
                        header="Creating Characters",
                        subheader="Adding a New Character to Chatrooms")
                    glow_bub_img = "cannot_find_img"
                return Frame(glow_bub_img, 25,25)
            else:
                # Check if the program was given a valid colour
                try:
                    c = Color(self.glow_color)
                    glow_bub_img = glow_bubble_fn(self.glow_color)
                except:
                    # Couldn't initialize this as a colour
                    ScriptError("Could not recognize \"", self.glow_color,
                        "\" as a color for a regular speech bubble.",
                        header="Creating Characters",
                        subheader="Adding a New Character to Chatrooms")
                    glow_bub_img = glow_bubble_fn("cannot_find_img")
                return Frame(glow_bub_img, 25, 25)

        @property
        def voicemail(self):
            """Return this character's voicemail PhoneCall object."""
            return self.__voicemail

        @voicemail.setter
        def voicemail(self, new_label):
            """Update this character's voicemail label."""
            self.__voicemail.phone_label = new_label

        def finished_text(self):
            """
            Reset the text message label after the conversation is complete.
            """

            self.text_msg.reply_label = False

        @property
        def heart_points(self):

            # Try to sync Saeran and Ray's heart points
            try:
                if self == store.sa:
                    return store.r.heart_points
            except:
                print("ERROR: Couldn't sync Saeran and Ray's heart points")

            try:
                return self.__heart_points
            except:
                return self.__dict__['heart_points']

        @heart_points.setter
        def heart_points(self, points):

            # Try to sync Saeran and Ray's heart points
            try:
                if self == store.sa:
                    store.r.heart_points = points
                    return
            except:
                print("ERROR: Couldn't sync Saeran and Ray's heart points")

            self.__heart_points = points

        @property
        def good_heart(self):

            # Try to sync Saeran and Ray's heart points
            try:
                if self == store.sa:
                    return store.r.good_heart
            except:
                print("ERROR: Couldn't sync Saeran and Ray's heart points")

            try:
                return self.__good_heart
            except:
                return self.__dict__['good_heart']

        @good_heart.setter
        def good_heart(self, points):

            # Try to sync Saeran and Ray's heart points
            try:
                if self == store.sa:
                    store.r.good_heart = points
                    return
            except:
                print("ERROR: Couldn't sync Saeran and Ray's heart points")

            self.__good_heart = points

        @property
        def bad_heart(self):

            # Try to sync Saeran and Ray's heart points
            try:
                if self == store.sa:
                    return store.r.bad_heart
            except:
                print("ERROR: Couldn't sync Saeran and Ray's heart points")
            try:
                return self.__bad_heart
            except:
                return self.__dict__['bad_heart']

        @bad_heart.setter
        def bad_heart(self, points):
            # Try to sync Saeran and Ray's heart points
            try:
                if self == store.sa:
                    store.r.bad_heart = points
                    return
            except:
                print("ERROR: Couldn't sync Saeran and Ray's heart points")
            self.__bad_heart = points

        def increase_heart(self, bad=False):
            """
            Add a heart point to this character's total. Good heart points
            count towards good ends and bad points towards bad ends.
            """

            if self == store.sa:
                try:
                    store.r.increase_heart(bad)
                    return
                except:
                    print("ERROR: Couldn't sync Saeran and Ray's heart points")

            self.heart_points += 1
            if not bad:
                self.good_heart += 1
            else:
                self.bad_heart += 1

            # All hearts count towards spendable hearts
            if self.file_id not in store.persistent.spendable_hearts:
                store.persistent.spendable_hearts[self.file_id] = 1
            else:
                store.persistent.spendable_hearts[self.file_id] += 1


        def decrease_heart(self):
            """Decrement the good heart points for this character."""

            if self == store.sa:
                # Try to sync Saeran and Ray's heart points
                try:
                    if self == store.sa:
                        store.r.decrease_heart()
                        return
                except:
                    print_file("Couldn't sync Saeran and Ray's heart points.")


            self.heart_points -= 1
            self.good_heart -= 1

        def reset_heart(self):
            """Reset all heart points for this character."""

            self.heart_points = 0
            self.good_heart = 0
            self.bad_heart = 0

        @property
        def bonus_pfp(self):
            """Return this character's bonus profile picture."""

            try:
                return self.__bonus_pfp
            except:
                return False

        @bonus_pfp.setter
        def bonus_pfp(self, new_img):
            """Set the bonus profile picture for this character."""

            try:
                self.__bonus_pfp = new_img
            except:
                return

        @property
        def prof_pic(self):
            """Return this character's profile picture."""

            try:
                return self.__prof_pic
            except:
                return self.__dict__['prof_pic']

        @prof_pic.setter
        def prof_pic(self, new_img):
            """
            Set this character's profile picture and attempt to set
            big_prof_pic to a larger version of the given picture,
            if available.
            """

            if self.__prof_pic == new_img:
                # Don't bother
                return

            if (getattr(store, 'observing', False)
                    and store.current_timeline_item.played
                    and not store._in_replay):
                # Don't change profile pictures on a re-watch, unless
                # it's from the History replays.
                return

            if new_img == False:
                self.__prof_pic = False
                return
            # Check if it's a Transform; if so, can't perform string logic.
            is_transform = False
            try:
                if new_img[0] == '#':
                    new_img = Color(new_img)
                    raise
                split_img = new_img.split('.')
                if isImg(new_img):
                    self.__prof_pic = new_img
                    self.seen_updates = False
                elif isImg(new_img.split('.')[0] + '.webp'):
                    self.__prof_pic = new_img.split('.')[0] + '.webp'
                else:
                    # Couldn't figure out this image! It has to be a string
                    # if the program got to this point.
                    ScriptError("Could not find the image \"", new_img,
                        "\" for use as a profile picture.",
                        header="Creating Characters",
                        subheader="Adding a New Character to Chatrooms")
                    new_img = "cannot_find_img"
                    raise
            except:
                is_transform = True
                self.seen_updates = self.__prof_pic == new_img
                self.__prof_pic = new_img


            if self.file_id == 'm': # This is the MC
                #self.__prof_pic = store.persistent.MC_pic
                store.persistent.MC_pic = self.__prof_pic

            self.__big_prof_pic = self.__prof_pic
            if self.__prof_pic and not is_transform:
                big_name = self.__prof_pic.split('.')
                large_pfp = big_name[0] + '-b.' + big_name[1]
                if renpy.loadable(large_pfp):
                    self.__big_prof_pic = large_pfp
                elif renpy.loadable(big_name[0] + '-b.webp'):
                    self.big_prof_pic = big_name[0] + '-b.webp'

            # Add this profile picture to the persistent list of profile
            # pictures the player has seen.
            if self.file_id == 'm':
                return

            if (store.persistent.unlocked_prof_pics is None
                    or not isinstance(store.persistent.unlocked_prof_pics, set)):
                store.persistent.unlocked_prof_pics = set()

            try:
                if self.in_init:
                    # Don't add images during initialization
                    return
            except:
                pass
            if not self.__prof_pic in store.persistent.unlocked_prof_pics:
                add_img_to_set(store.persistent.unlocked_prof_pics,
                        self.__prof_pic)



        def get_pfp(self, the_size):
            """
            Return the large or small profile picture depending
            on the_size, resized to the given size.
            """

            max_small = 110 * 1.2
            # If this character has a bonus_pfp, it gets priority
            try:
                the_pic = self.__bonus_pfp
            except AttributeError:
                the_pic = False

            # Make sure MC's pic is up to date
            if self == store.m:
                self.prof_pic = store.persistent.MC_pic

            if the_pic and isinstance(the_pic, tuple):
                return tuple_to_pic(the_pic, the_size)
            elif isinstance(self.__prof_pic, tuple):
                return tuple_to_pic(self.__prof_pic, the_size)

            if the_pic and the_size <= max_small:
                return Transform(the_pic, size=(the_size, the_size))
            elif the_pic:
                # Check for a larger version of the bonus pfp.
                try:
                    big_name = the_pic.split('.')
                except:
                    return Transform(self.__prof_pic, size=(the_size, the_size))
                large_pfp = big_name[0] + '-b.' + big_name[1]
                if renpy.loadable(large_pfp):
                    return Transform(large_pfp, size=(the_size, the_size))
                else:
                    return Transform(the_pic, size=(the_size, the_size))


            # Regular profile pic is 110x110
            # Big pfp is 314x314
            if not self.__prof_pic:
                ScriptError("Could not find the image \"", self.__prof_pic,
                        "\" for use as a profile picture.",
                        header="Creating Characters",
                        subheader="Adding a New Character to Chatrooms")
                self.prof_pic = "cannot_find_img"

            # Make sure the pfp is still loadable
            if (isinstance(self.__prof_pic, basestring)
                    and not renpy.loadable(self.__prof_pic)):
                ScriptError("Could not load the image \"", self.__prof_pic,
                    "\" for use as a profile picture.",
                    header="Creating Characters",
                    subheader="Adding a New Character to Chatrooms")
                self.prof_pic = "cannot_find_img"

            if the_size <= max_small:
                return Transform(self.__prof_pic,
                                size=(the_size, the_size))
            else:
                return Transform(self.__big_prof_pic,
                                size=(the_size, the_size))

        def reset_pfp(self):
            """
            Reset the profile picture to its default image.
            Used in replay mode for the History screen.
            """

            self.prof_pic = self.default_prof_pic

        @property
        def cover_pic(self):
            """Return this character's cover photo."""

            return self.__cover_pic

        @cover_pic.setter
        def cover_pic(self, new_img):
            """Set this character's cover photo, if given an image."""

            if self.cover_pic == new_img:
                # No change
                return
            if not new_img:
                self.__cover_pic = False
            elif isImg(new_img):
                self.__cover_pic = new_img
                self.seen_updates = False

        @property
        def status(self):
            """Set this character's status update."""

            return self.__status

        @status.setter
        def status(self, new_status):
            """Set this character's status and set seen_updates to False."""

            if self.status == new_status:
                # No change
                return
            self.__status = new_status
            self.seen_updates = False

        @property
        def seen_updates(self):
            """
            Return True if the player has seen all changes to this character's
            profile; return False otherwise.
            """

            return self.__seen_updates

        @seen_updates.setter
        def seen_updates(self, new_bool):
            """Set seen_updates."""

            self.__seen_updates = new_bool

        @property
        def name(self):
            """Return this character's name."""

            try:
                return self.__name
            except:
                pass
            try:
                return self.__dict__['name']
            except:
                print_file("ERROR: Could not retrieve name.")
                return "DEFAULT"

        @name.setter
        def name(self, new_name):
            """Set this character's name to the given name."""

            self.__name = new_name

        @property
        def text_label(self):
            """
            Return the label used to reply to a text message with
            this character.
            """

            return self.text_msg.reply_label

        @text_label.setter
        def text_label(self, new_label):
            """
            Set the label to jump to when responding to this character's
            text messages.
            """

            self.text_msg.reply_label = new_label

        def set_real_time_text(self, new_status):
            """
            Set whether this character's next text message conversation
            will be in real-time or not.
            """

            if new_status:
                self.real_time_text = True
            else:
                self.real_time_text = False

        def text_backlog(self, who, what, when, img=False):
            """Add an entry to this character's text message backlog."""

            self.text_msg.msg_list.append(ChatEntry(who, what,
                when, img))
            self.text_msg.read = True

        def get_bubbles(self):
            """Get the special bubbles associated with this character."""

            spec_bubbles_1 = [ bub for bub in store.all_bubbles_list ]
            spec_bubbles_2 = [ ]
            for bub in spec_bubbles_1:
                if bub[-2:] == "_l" or "glow" in bub:
                    bub = "Bubble/Special/" + self.file_id + "_" + bub + '.webp'
                    spec_bubbles_2.append(bub)

            spec_bubbles = [ bub for bub in spec_bubbles_2
                if renpy.loadable(bub) ]
            return spec_bubbles

        def do_extend(self, **kwargs):
            """
            Allow this ChatCharacter object to act as a proxy for the
            VN and phone call Character objects.
            """

            if store.in_phone_call:
                self.phone_char.do_extend()
            elif store.vn_choice:
                self.vn_char.do_extend()

        def __call__(self, what, pauseVal=None, img=False,
                    bounce=False, specBubble=None, link_img=None,
                    link_title=None, link_text=None, link_action=None,
                    **kwargs):
            """
            Send this character's dialogue to the program.

            Parameters:
            -----------
            what : string
                Dialogue said by the character
            pauseVal : float or None
                Multiplier for how much time it takes this character to
                send this message. 0 indicates no wait time, and larger values
                indicate longer wait times.
            img : bool
                True if this message contains an image (e.g. an emoji or CG)
            bounce : bool
                True if this message should bounce when it animates in.
            specBubble : string
                Indicates what kind of special speech bubble this message uses.
            link_img : string
                A string with the image path to be used on the right side of
                a link message. Approx 81x81px.
            link_title : string
                The title to be used for the link message.
            link_text : string
                The text on a link message.
            link_action : Screen Action
                The action to be performed when a link message is clicked.

            Result:
            -------
            If the player is in a phone call, this ChatCharacter's phone call
            Character will be used to say the given dialogue. If the player
            is in Story Mode, use this ChatCharacter's VN Character to say the
            given dialogue. If the player is texting, add the given dialogue
            to the text message conversation. Otherwise, add these messages
            to the chat log and also to the replay log.
            """

            store.answer_shown = False
            # Check if the player just got out of a menu and there's dialogue
            # for the main character.
            if (self != store.main_character and not store.dialogue_paraphrase
                    and store.dialogue_picked != ""):
                say_choice_caption(store.dialogue_picked,
                    store.dialogue_paraphrase, store.dialogue_pv)

            if (self == store.main_character
                    and not kwargs.get('from_paraphrase', None)):
                # This didn't come from `say_choice_caption`, but the MC is
                # speaking. Is this the same dialogue that was going to be
                # posted?
                # print("what =", what, "dialogue_picked =", store.dialogue_picked)
                if what == store.dialogue_picked:
                    # Clear the stored no-paraphrase items
                    store.dialogue_picked = ""
                    store.dialogue_paraphrase = store.paraphrase_choices
                    store.dialogue_pv = 0
                    # If paraphrase_choices is None, set it to True
                    if store.paraphrase_choices is None:
                        store.paraphrase_choices = True


            # Allows you to still use this object even in phone
            # calls and Story Mode
            if store.in_phone_call:
                # If in phone call, use the phone_call character
                self.phone_char(what, **kwargs)
                return
            elif store.vn_choice:
                # If in Story Mode, use VN character
                self.vn_char(what, **kwargs)
                return

            if (specBubble and specBubble[:7] == "round"
                    and (self.file_id == 'r' or self.file_id == 'z')):
                # Correct this to the new 'flower' variant if applicable
                specBubble = "flower_" + specBubble[-1:]

            # If the player is texting, add this to the character's
            # TextMessage object instead
            if store.text_person is not None:
                # If they're on the text message screen, show the
                # message real-time
                if store.text_person.real_time_text and store.text_msg_reply:
                    addtext_realtime(self, what, pauseVal=pauseVal, img=img)
                # If they're not in the midst of a text conversation,
                # this is "backlog"
                else:
                    addtext(self, what, img)
                return
            else:
                # Make sure the player isn't observing; otherwise add
                # entries to the replay_log
                if not store.observing:
                    new_pv = pauseVal
                    # For replays, MC shouldn't reply instantly
                    if self == store.main_character and new_pv == 0:
                        new_pv = None
                    store.current_timeline_item.replay_log.append(ReplayEntry(
                        self, what, new_pv, img, bounce, specBubble,
                        link_img, link_title, link_text, link_action))

                addchat(self, what, pauseVal=pauseVal, img=img,
                            bounce=bounce, specBubble=specBubble,
                            link_img=link_img, link_title=link_title,
                            link_text=link_text, link_action=link_action)

        def __eq__(self, other):
            """Check for equality between two ChatCharacter objects."""

            if not isinstance(other, ChatCharacter):
                return False
            return self.file_id == other.file_id

        def __ne__(self, other):
            """Check for inequality between two ChatCharacter objects."""

            if not isinstance(other, ChatCharacter):
                return True
            return self.file_id != other.file_id

init -5 python:

    def register_pfp(files=None, condition='seen', folder="", ext="",
            filter_out=None, filter_keep=None):
        """
        Return a list of (folder + file + ext, condition) tuples. Used to
        construct the list of profile pictures the user is allowed to change
        the characters' picture to.

        Arguments:
        ----------
        files : string[] or string
            List of file paths that lead to a profile picture image.
        condition : string
            String that evaluates to a python condition which will be used
            to determine whether this image is unlocked or not. The default,
            'seen', evaluates whether or not this image has been seen by the
            player as a CG or a profile picture.
        folder : string
            Folder for where to find this file, e.g. "Profile Pics/Jaehee/".
            Automatically prepended to each file name when searching.
        ext : string
            Extension for this file e.g. "png". Automatically appended to each
            file name when searching.
        filter_out : string
            If included, searches through files in `folder` that do *not*
            contain filter_out.
        filter_keep : string
            If included, searches through files in `folder` that *do* contain
            filter_keep.
        """

        if len(folder) > 0 and folder[-1] != "/":
            folder += "/"
        if len(ext) > 0 and ext[0] != ".":
            ext = "." + ext
        result = []

        if filter_out is None and filter_keep is None:
            if not isinstance(files, list):
                # Just a single item
                item = folder + files + ext
                if isImg(item):
                    return [ (item, condition)]
                else:
                    ScriptError('"',item,'" is not recognized as an image file.',
                    header='Miscellaneous',
                    subheader='Profile Pictures for the Characters',
                    link_text="The register_pfp function")
                    return
            # Otherwise, iterate through the list
            for file in files:
                item = folder + file + ext
                if isImg(item):
                    result.append((item, condition))
                else:
                    ScriptError('"',item,'" is not recognized as an image file.',
                    header='Miscellaneous',
                    subheader='Profile Pictures for the Characters',
                    link_text="The register_pfp function")

            return result

        # Otherwise, one of the filter conditions is True
        file_list = [ pic for pic in renpy.list_files() if folder in pic
            and isImg(pic) ]
        # Filter by extension, if available
        if ext:
            result = [ pic for pic in file_list if ext in pic ]
        else:
            result = file_list

        if filter_out is None:
            # Just filter_keep
            file_list = [ pic for pic in result if filter_keep in pic ]
        elif filter_keep is None:
            # Just filter_out
            file_list = [ pic for pic in result if filter_out not in pic ]
        else:
            # Both
            file_list = [ pic for pic in result if (filter_out not in pic
                and filter_keep in pic) ]

        # Now construct an (item, condition) tuple out of each item
        result = []
        if len(file_list) > 0:
            for item in file_list:
                if item[:7] == 'images/':
                    result.append((item[7:], condition))
                else:
                    result.append((item, condition))
        return result

    def get_img_from_tuple(img):
        """Return the image filename if it's stored in a tuple."""

        # (str_img, crop, crop_rel
        if isinstance(img, tuple):
            return img[0]
        else:
            return img


    def change_mc_pfp_callback():
        """
        Function that is called whenever the main character changes their
        profile picture.
        """

        if not store.mc_pfp_callback:
            return

        if store.mc_pfp_time is None:
            time_diff = None
        elif store.mc_previous_pfp is None:
            # First time the picture has been changed this playthrough
            store.mc_previous_pfp = get_img_from_tuple(store.persistent.MC_pic)
            time_diff = None
        elif store.mc_previous_pfp == get_img_from_tuple(store.persistent.MC_pic):
            # Picture wasn't changed; time_diff is zero.
            time_diff = store.mc_pfp_time.datetime - store.mc_pfp_time.datetime
            return
        else:
            time_diff = upTime().datetime - store.mc_pfp_time.datetime

        store.mc_pfp_time = upTime()

        # Find whose profile picture this is
        who = None
        for chara in store.all_characters:
            try:
                pfp_list = [img for img, cond in getattr(store, chara.file_id + '_unlockable_pfps')]
                print_file("Looking at", chara.file_id,"unlockable pfps")
                if ((store.persistent.MC_pic in pfp_list)
                        or (get_img_from_tuple(store.persistent.MC_pic)
                                in pfp_list)):
                    who = chara
                    break
                elif ('images/' in get_img_from_tuple(store.persistent.MC_pic)
                        and get_img_from_tuple(store.persistent.MC_pic)[7:] in pfp_list):
                    who = chara
                    break
            except Exception as e:
                print_file("Couldn't look at", chara.file_id, "Error:", e)
                continue
        old_pfp = store.mc_previous_pfp
        store.mc_previous_pfp = get_img_from_tuple(store.persistent.MC_pic)

        # Wrap the time diff in a MyTimeDelta object
        time_diff = MyTimeDelta(time_diff)

        try:
            lbl = store.mc_pfp_callback(time_diff, old_pfp,
                get_img_from_tuple(store.persistent.MC_pic), who)
        except:
            ScriptError("Could not use mc_pfp_callback. Do you have at",
                "least four function parameters?",
                header='Miscellaneous',
                subheader="Profile Picture Callbacks")
            return
        if not lbl:
            print_file("Didn't get a pfp callback label")
            return
        # Otherwise, got a label to jump to. Only jump to it if it hasn't
        # been seen in this playthrough (or if testing mode is on).
        # First, check if the returned label is a list
        if not isinstance(lbl, list):
            lbl = [lbl]
        for l in lbl:
            if renpy.has_label(l) and (store.persistent.testing_mode
                    or l not in store.seen_pfp_callbacks):
                store.seen_pfp_callbacks.add(l)
                renpy.call_in_new_context(l)
                return
        return

    def add_img_to_set(set, img):
        """
        Safely add an image to a persistent set. Namely this means changing
        it to a tuple if the image is not a string (aka it's a Transform).
        """

        if isinstance(img, renpy.display.transform.Transform):
            str_img = None
            color = None
            crop = None
            # Get the child
            trans = img.child
            # Get the crop, if present
            if img.kwargs.get('crop', None) is not None:
                crop = img.kwargs['crop']
            if img.kwargs.get('crop_relative', False):
                crop_rel = True
            else:
                crop_rel = False

            while (isinstance(trans, renpy.display.core.Displayable)):
                try:
                    trans = trans.child
                except AttributeError:
                    break

            if isinstance(trans, renpy.display.im.Image):
                str_img = trans.filename
            elif isinstance(trans, renpy.display.imagelike.Solid):
                color = trans.color
            elif isinstance(trans, basestring) and trans[0] == "#":
                color = trans
            # May need to add more statements here

            # Check if str_img is already in the set with a different extension
            if str_img is not None:
                no_ext = str_img.split('.')[0]
                if no_ext + '.png' in set:
                    return
                elif no_ext + '.jpg' in set:
                    return
                elif crop is not None and (no_ext + '.png',
                        crop, crop_rel) in set:
                    return
                elif crop is not None and (no_ext + '.jpg',
                        crop, crop_rel) in set:
                    return


            if str_img is not None and crop is not None:
                set.add((str_img, crop, crop_rel))
            elif str_img is not None:
                set.add(str_img)
            elif color is not None:
                set.add(color)
            else:
                print("WARNING: Could not extract immutable string or tuple",
                    "from profile picture", img)

            return

        try:
            if not renpy.loadable(img):
                if '.webp' not in img:
                    new_img = img.split('.')[0] + '.webp'
                    if renpy.loadable(new_img):
                        set.add(new_img)
                        return
                raise
        except:
            # Couldn't display this profile picture
            print_file("WARNING: Couldn't evaluate given image", img)
            return

        set.add(img)
        return


    def add_mc_pfp(img, unlocked=False):
        """
        Safely adds a new profile picture for the main character to choose. If
        unlocked is True, it will not require the player use an hourglass to
        unlock it. Otherwise, it will be visible but require an hourglass to
        unlock.
        """

        if not isinstance(img, list):
            img = [img]

        if isinstance(img[0], tuple) and len(img[0]) == 2:
            # Should be an (img, condition) pair
            img = [ i for i, cond in img ]

        for i in img:
            add_img_to_set(store.unlocked_prof_pics, i)
            if unlocked:
                add_img_to_set(store.persistent.mc_unlocked_pfps, i)
        return

# The time the main character's profile picture was last changed at
default mc_pfp_time = None
# The previous picture the player had before the current one
default mc_previous_pfp = None
# Contains all the profile pictures you've seen in the game
default persistent.unlocked_prof_pics = set()
# Contains the profile pictures the player has purchased with heart points
default persistent.bought_prof_pics = set()
# Contains a dictionary of the heart points the player has to spend on
# each character
default persistent.spendable_hearts = {}
# This holds a list of the labels the program has already jumped to during
# profile picture callbacks
default seen_pfp_callbacks = set()

# These are special 'characters' for additional features
default special_msg = ChatCharacter("msg")
default filler = ChatCharacter("filler")
default answer = ChatCharacter('answer', 'delete')
default chat_pause = ChatCharacter('pause', 'delete')
