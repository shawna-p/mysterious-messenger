init -5 python:

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
            "ja-default.png", the program searches for a file called
            "ja-default-b.png" for the big profile picture.
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
                pronunciation_help=False):               
                
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
                e.g. if prof_pic is "ja-default.png", the program searches for 
                a file called "ja-default-b.png" for the big profile picture.
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
            """


            self.name = name            
            self.file_id = file_id
            self.big_prof_pic = prof_pic
            self.prof_pic = prof_pic
            self.default_prof_pic = prof_pic
            if not homepage_pic:
                self.homepage_pic = prof_pic
            else:
                self.homepage_pic = homepage_pic
            self.seen_updates = False

            # If the program finds a "big" version of this profile picture,
            # it uses that when displaying the profile picture at higher
            # resolutions
            if self.prof_pic:
                big_name = self.prof_pic.split('.')
                large_pfp = big_name[0] + '-b.' + big_name[1]
                if renpy.loadable(large_pfp):
                    self.big_prof_pic = large_pfp
            if self.file_id == 'm':
                self.prof_pic = store.persistent.MC_pic

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
            self.heart_points = 0  
            self.good_heart = 0
            self.bad_heart = 0
            self.heart_color = heart_color
            self.glow_color = glow_color
            self.bubble_color = bubble_color
            self.right_msgr = right_msgr

            if self.file_id:
                if not self.bubble_color:
                    reg_bub_img = "Bubble/" + self.file_id + "-Bubble.png"
                    # This person is the messenger; typically MC
                    if self.right_msgr: 
                        reg_bub_img = Transform(reg_bub_img, xzoom=-1)
                        self.reg_bubble_img = Frame(reg_bub_img, 18,18,25,18)
                    else:
                        self.reg_bubble_img = Frame(reg_bub_img, 25,18,18,18)
                else:
                    reg_bub_img = reg_bubble_fn(self.bubble_color)
                    if self.right_msgr: 
                        reg_bub_img = Transform(reg_bub_img, xzoom=-1)
                        self.reg_bubble_img = Frame(reg_bub_img, 18,18,25,18)
                    else:
                        self.reg_bubble_img = Frame(reg_bub_img, 25,18,18,18)

                if not self.glow_color:
                    glow_bub_img = "Bubble/" + self.file_id + "-Glow.png"
                    self.glow_bubble_img = Frame(glow_bub_img, 25,25)
                else:
                    self.glow_bubble_img = Frame(
                        glow_bubble_fn(self.glow_color), 25, 25
                    )
            else:
                self.reg_bubble_img = Frame("Bubble/white-Bubble.png", 
                                            25,18,18,18)
                self.glow_bubble_img = Frame("Bubble/Special/sa_glow2.png",
                                            25,25)

            self.emote_list = emote_list
            
            self.text_msg = TextMessage()
            self.real_time_text = False

            if phone_char:
                self.phone_char = phone_char
            else:
                self.phone_char = store.phone_character
            if vn_char:
                self.vn_char = vn_char
            else:
                self.vn_char = store.narrator

            if pronunciation_help:
                self.p_name = pronunciation_help
            else:
                self.p_name = self.name

            # Any initialized character should go in all_characters
            if self not in store.all_characters and self.prof_pic:
                store.all_characters.append(self)
            
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

        ## Adds a heart point to the character -- good or bad
        ## depending on the second argument
        def increase_heart(self, bad=False):
            """
            Add a heart point to this character's total. Good heart points
            count towards good ends and bad points towards bad ends.
            """

            self.heart_points += 1
            if not bad:
                self.good_heart += 1
            else:
                self.bad_heart += 1

            # Try to sync Saeran and Ray's heart points
            try:
                if self == store.sa:
                    store.r.heart_points += 1
                    if not bad:
                        store.r.good_heart += 1
                    else:
                        store.r.bad_heart += 1
                elif self == store.r:
                    store.sa.heart_points += 1
                    if not bad:
                        store.sa.good_heart += 1
                    else:
                        store.sa.bad_heart += 1
            except:
                print_file("Couldn't sync Saeran and Ray's heart points.")
        
        def decrease_heart(self):
            """Decrement the good heart points for this character."""

            self.heart_points -= 1
            self.good_heart -= 1

            # Try to sync Saeran and Ray's heart points
            try:
                if self == store.sa:
                    store.r.heart_points -= 1
                    store.r.good_heart -= 1
                elif self == store.r:
                    store.sa.heart_points -= 1
                    store.sa.good_heart -= 1
            except:
                print_file("Couldn't sync Saeran and Ray's heart points.")
            
        def reset_heart(self):
            """Reset all heart points for this character."""

            self.heart_points = 0
            self.good_heart = 0
            self.bad_heart = 0

            # Try to sync Saeran and Ray's heart points
            try:
                if self == store.sa:
                    store.r.heart_points = 0
                    store.r.good_heart = 0
                    store.r.bad_heart = 0
                elif self == store.r:
                    store.sa.heart_points = 0
                    store.sa.good_heart = 0
                    store.sa.bad_heart = 0
            except:
                print_file("Couldn't sync Saeran and Ray's heart points.")

        @property
        def prof_pic(self):
            """Return this character's profile picture."""

            return self.__prof_pic
            
        @prof_pic.setter
        def prof_pic(self, new_img):
            """
            Set this character's profile picture and attempt to set
            big_prof_pic to a larger version of the given picture,
            if available.
            """

            if new_img == False:
                self.__prof_pic = False
            elif isImg(new_img):            
                self.__prof_pic = new_img
                self.seen_updates = False

            if self.file_id == 'm': # This is the MC
                self.__prof_pic = store.persistent.MC_pic

            self.__big_prof_pic = self.__prof_pic
            if self.__prof_pic:
                big_name = self.__prof_pic.split('.')
                large_pfp = big_name[0] + '-b.' + big_name[1]
                if renpy.loadable(large_pfp):
                    self.__big_prof_pic = large_pfp
        
        def get_pfp(self, the_size):
            """
            Return the large or small profile picture depending
            on the_size, resized to the given size.
            """

            max_small = 110 * 1.5
            # If this character has a bonus_pfp, it gets priority
            try:
                the_pic = self.__bonus_pfp
            except AttributeError:
                the_pic = False

            if the_pic and the_size <= max_small:
                return Transform(the_pic, size=(the_size, the_size))
            elif the_pic:
                # Check for a larger version
                big_name = the_pic.split('.')
                large_pfp = big_name[0] + '-b.' + big_name[1]
                if renpy.loadable(large_pfp):
                    return Transform(large_pfp, size=(the_size, the_size))
                else:
                    return Transform(the_pic, size=(the_size, the_size))
                

            # Regular profile pic is 110x110
            # Big pfp is 314x314
            if self != store.m:
                if the_size <= max_small:
                    return Transform(self.__prof_pic, 
                                    size=(the_size, the_size))
                else:
                    return Transform(self.__big_prof_pic, 
                                    size=(the_size, the_size))
            else:
                return Transform(store.persistent.MC_pic, 
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

            return self.__name

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
                    bounce=False, specBubble=None, **kwargs):
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

            Result:
            -------
            If the player is in a phone call, this ChatCharacter's phone call
            Character will be used to say the given dialogue. If the player
            is in VN mode, use this ChatCharacter's VN Character to say the 
            given dialogue. If the player is texting, add the given dialogue
            to the text message conversation. Otherwise, add these messages
            to the chat log and also to the replay log.
            """


            # Allows you to still use this object even in phone
            # calls and VN mode
            if store.in_phone_call:
                # If in phone call, use the phone_call character
                self.phone_char(what, **kwargs)
                return
            elif store.vn_choice:
                # If in VN mode, use VN character
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
                elif store.text_person.real_time_text:
                    if not self.right_msgr:
                        store.text_person.text_msg.notified = False
                    if img and "{image" not in what:
                        cg_helper(what, self, False)
                    store.text_person.text_msg.msg_list.append(ChatEntry(
                        self, what, upTime(), img))
                # Otherwise this is a regular text conversation and
                # is added all at once
                else:
                    addtext(self, what, img)
            else:
                # Make sure the player isn't observing; otherwise add
                # entries to the replay_log
                if not store.observing:
                    new_pv = pauseVal
                    # For replays, MC shouldn't reply instantly
                    if self.right_msgr and new_pv == 0:
                        new_pv = None
                    store.current_chatroom.replay_log.append(ReplayEntry(
                        self, what, new_pv, img, bounce, specBubble))
                    
                addchat(self, what, pauseVal=pauseVal, img=img, 
                            bounce=bounce, specBubble=specBubble)
    
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
