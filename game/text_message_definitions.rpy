init -6 python:

    from random import randint
    import renpy.store as store
    
    ## This class keeps track of a text message conversation
    ## for each character.
    class TextMessage(renpy.store.object):
        """
        A class to keep track of text message conversations for each character.

        Attributes:
        -----------
        msg_list : ChatEntry[]
            List of currently sent messages in the conversation.
        msg_queue : ChatEntry[]
            List of messages waiting to be delivered.
        reply_label : string
            Reply label to jump to when responding.
        read : bool
            Whether this message has been read.
        heart : bool
            Whether this message should trigger a heart icon when read.
        heart_person : ChatCharacter
            Who the heart icon should belong to.
        bad_heart : bool
            True if the awarded heart counts towards a 'bad' ending.
        cg_unlock_list : [Album[], Album]
            A list that keeps track of CGs to unlock after the player
            has read this message chain.
        notified : bool
            True if the player has already been told they have an unread
            message.
        """

        def __init__(self):
            """Create a TextMessage object."""

            self.msg_list = []
            self.msg_queue = []
            self.reply_label = False
            self.__read = False
            self.heart = False
            self.heart_person = None
            self.bad_heart = False
            self.cg_unlock_list = []
            self.notified = True

        @property
        def read(self):
            """Return whether this conversation has been read."""

            return self.__read
            
        @read.setter
        def read(self, new_bool):
            """Mark the message as read and unlock appropriate CGs."""

            self.__read = new_bool
            if new_bool: 
                # Unlock any CG images the player saw
                for pair in self.cg_unlock_list:
                    # pair[0] is persistent.??_album
                    # pair[1] is the Album(filepath)   
                    for photo in pair[0]:
                        if pair[1] == photo:
                            photo.unlock()
                self.cg_unlock_list = []
            renpy.retain_after_load()
            renpy.restart_interaction()         
    
        def deliver(self):
            """Transfer messages from the msg_queue to the player's inbox."""
            
            # If not on the text message screen, add these 
            # messages to the regular message list
            if self.msg_queue and not renpy.get_screen('text_message_screen'):
                self.msg_list.extend(self.msg_queue)
                self.msg_queue = []                
                # If the last message was sent by someone other
                # than the MC
                if not self.msg_list[-1].who.right_msgr:
                    # Notify the player of the delivered message
                    self.read = False
                    renpy.music.play(persistent.text_tone, 'sound')
                    popup_screen = allocate_text_popup()
                    renpy.show_screen(popup_screen, 
                        c=self.msg_list[-1].who)
                    self.notified = True
                else:
                    self.read = True
            renpy.retain_after_load()
            
        def reply(self):
            """Mark the message as read and jump to the reply label."""

            store.text_msg_reply = True
            old_reply = self.reply_label
            renpy.call_in_new_context(self.reply_label)
            # If the reply label was updated, then don't
            # erase it. Otherwise, the player shouldn't be able
            # to reply twice
            if self.reply_label == old_reply:
                self.reply_label = False
            store.text_msg_reply = False  
            
        def heart_point(self, person=None, bad=False):
            """Award a heart point to the correct character."""

            self.heart = True
            self.heart_person = person
            self.bad_heart = bad
                    
    def add_heart(who, person=None, bad=False):
        """Let the program know this response will trigger a heart point."""

        who.text_msg.heart_point(person, bad)
             
    def deliver_all_texts(): 
        """Deliver all queued text messages at once."""

        for c in store.all_characters:
            # First check for regular texts
            if (c.text_msg.msg_queue 
                    and not c.real_time_text):
                c.text_msg.deliver()
            # Deliver real-time texts
            elif (c.real_time_text and not c.text_msg.read 
                    and not c.text_msg.notified):
                c.text_msg.notified = True
                renpy.music.play(persistent.text_tone, 'sound')
                popup_screen = allocate_text_popup()
                renpy.show_screen(popup_screen, c=c) 
        
    def new_message_count():
        """Return the number of unread messages from all characters."""

        unread_messages = [ x for x in store.all_characters 
            if (x.text_msg.msg_list and not x.text_msg.read) ]
        return len(unread_messages)
    
    def num_undelivered():
        """Return the number of undelivered messages in the queue."""
        
        undelivered = [ x for x in store.all_characters
                        if x.text_msg.msg_queue ]
        return len(undelivered)
        
    def addtext(who, what, img=False):
        """
        Queue a text message to be sent to the player. Not for real-time
        texting.

        Parameters:
        -----------
        who : ChatCharacter
            Character who is sending this text message.
        what : string
            Text content of the message.
        img : bool
            True if this message contains an image (CG or an emoji).
        """

        sender = store.text_person
        # If the MC sent this message, deliver it immediately
        if who.right_msgr:
            sender.text_msg.msg_list.append(ChatEntry(who, what, 
                                                      upTime(), img))
            sender.text_msg.read = True
            sender.text_msg.notified = True
            sender.text_msg.reply_label = False
            
        else:
            # Otherwise another character sent this/is replying
            # Add this message to the sender's queue
            sender.text_msg.msg_queue.append(ChatEntry(
                                                who, what, upTime(), img))
            sender.text_msg.notified = False
        
        # Check if the sent message has a CG
        if img and "{image" not in what:
            # Unlock the CG in the gallery/add it to the unlock list
            cg_helper(what, who, who.right_msgr)

        renpy.restart_interaction()

    def addtext_realtime(who, what, pauseVal, img=False):
        """
        Send a text message to the player in real-time.

        Parameters:
        -----------
        who : ChatCharacter
            Character who is sending this text message.
        what : string
            Text content of the message.
        pauseVal : float
            Multiplier to determine time this character spends "typing" before
            the message is sent.
        img : bool
            True if this message contains an image (CG or an emoji).
        """

        global textbackup
        store.choosing = False
        store.pre_choosing = False
        
        if not who.right_msgr:
            textlog = who.text_msg.msg_list
        elif store.text_person:
            textlog = store.text_person.text_msg.msg_list
        else:
            print("There's no one to text")
            return

        if pauseVal == None:
            pauseVal = store.pv

        if who.file_id != 'delete':
            text_pauseFailsafe(textlog)
            textbackup = ChatEntry(who, what, upTime(), img)
            oldPV = pauseVal
        
        if pauseVal == 0:
            pass
        elif who.file_id == 'delete':
            renpy.pause(pv)
        # Otherwise, pause to simulate typing time
        else:
            # Get the number of words in the message
            typeTime = what.count(' ') + 1
            # Divide by 3 since average reading speed is 200wpm or 3.3wps
            typeTime /= 3
            if typeTime < 1.5:
                typeTime = 1.5
            typeTime = typeTime * pauseVal
            renpy.pause(typeTime)

        if img:
            #Adjust the {image=seven_wow} etc statement to 
            # suit the emoji dictionary
            if "{image =" in what:
                first, last = what.split('=')
                if len(last) > 0 and last[0] == ' ':
                    last.pop(0)
                what = "{image=" + last
            if what in emoji_lookup:
                renpy.play(emoji_lookup[what], channel='voice_sfx')
            elif "{image" not in what:
                cg_helper(what, who, True)
                    
        textlog.append(ChatEntry(who, what, upTime(), img))
        renpy.checkpoint()

    def text_pauseFailsafe(textlog):
        """
        Ensure that the program doesn't miss any messages being posted to
        this conversation in the event that the user pauses the conversation.
        
        Parameters:
        -----------
        textlog : ChatEntry[]
            The text message conversation to check for missed messages.
        """

        global textbackup

        # If the backup is being reset, return
        if textbackup == "Reset":
            return
        
        if len(textlog) > 0:
            last_text = textlog[-1]
        else:
            return

        if last_text.who == filler:
            return
        if textbackup.who == filler:
            return
        if textbackup.what == '':
            return

        if (last_text.who.file_id == textbackup.who.file_id
                and last_text.what == textbackup.what):
            # The last entry was successfully added; return
            return

        if renpy.get_screen('text_message_screen'):
            typeTime = textbackup.what.count(' ') + 1
            typeTime /= 3
            if typeTime < 1.5:
                typeTime = 1.5
            typeTime = typeTime * oldPV
            renpy.pause(typeTime)

        if textbackup.img == True:
            # Adjust the {image=seven_wow} etc statement to 
            # suit the emoji dictionary
            if "{image =" in textbackup.what:
                first, last = textbackup.what.split('=')
                if len(last) > 0 and last[0] == ' ':
                    last.pop(0)
                textbackup.what = "{image=" + last
            if (textbackup.what in emoji_lookup 
                    and renpy.get_screen('text_message_screen')):
                renpy.play(emoji_lookup[textbackup.what], channel="voice_sfx")

        textlog.append(ChatEntry(textbackup.who, textbackup.what,
                upTime(), textbackup.img))
        renpy.checkpoint()
               
        

    def text_popup_preview(last_msg, num_char=48):
        """
        Parse the contents of last_msg to display a popup notification with
        a preview of the appropriate length.

        Parameters:
        -----------
        last_msg : string
            Content of the message to preview.
        num_char : int
            Number of characters the text preview should display.
        """

        global name
        name_cut = num_char + 6 - len(name)
        
        if last_msg and ("{image" in last_msg.what or last_msg.img):
            if last_msg.who.right_msgr:
                return "You sent an image."
            else:
                return last_msg.who.name + " sent an image."

        if "[" in last_msg.what:
            # Do some cleanup to ensure variables aren't cut up
            # First check if the variable is [name]
            if "[name]" in last_msg.what:
                msg = last_msg.what[:name_cut]
            else:
                msg = last_msg.what[:num_char]
            n = msg.rfind(' ')
            if n > 0:
                msg = msg[:n]
            if len(msg) < len(last_msg.what):
                return msg + '...'
            else:
                return msg

        if last_msg and len(last_msg.what) > num_char:
            return last_msg.what[:num_char] + '...'
        elif last_msg:
            return last_msg.what[:num_char]
            

default text_msg_reply = False
# Store the ChatCharacter object of the other person in a text conversation
default text_person = None
# Keep track of whose text conversation the player is viewing
# so they can view CGs full-screen
default CG_who = None

## A label that lets the player leave instant text message
## conversations. The conversation is then lost
label leave_inst_text():
    $ text_msg_reply = False
    $ textlog = text_person.text_msg.msg_list                        
    $ config.skipping = False           
    $ choosing = False
    $ textbackup = 'Reset'
    hide screen text_play_button
    hide screen text_answer
    hide screen text_pause_button
    hide screen inactive_text_answer
    $ text_person.finished_text()
    $ text_person = None
    $ renpy.retain_after_load()    
    call screen text_message_hub
    return
    
label text_begin(who):    
    $ text_person = who
    $ text_msg_reply = True
    $ who.text_msg.read = True
    if who.real_time_text:
        show screen text_message_screen(who)
        show screen text_pause_button
    $ renpy.retain_after_load()
    return
        
label compose_text(who, real_time=False):
    $ who.set_real_time_text(real_time)
    $ who.text_msg.read = False
    $ textbackup = 'Reset'
    $ text_person = who
    $ renpy.retain_after_load()
    return

label compose_text_end(text_label=False):
    $ text_person.text_label = text_label
    $ text_person = None
    $ textbackup = 'Reset'
    $ renpy.retain_after_load()
    return
    

## Set end variables when a text message menu is completed 
label text_end():
    if text_person is not None and text_person.real_time_text:        
        $ text_pauseFailsafe(text_person.text_msg.msg_list) 
    $ text_msg_reply = False
    #if text_person is not None and text_person.real_time_text:
    $ text_person.finished_text()
    $ who = text_person
    $ text_person = None
    $ chatroom_hp = 0
    $ textbackup = ChatEntry(filler,"","")
    $ renpy.retain_after_load()        
    hide screen text_answer
    hide screen inactive_text_answer
    hide screen text_play_button
    hide screen text_pause_button  
    call screen text_message_screen(who, animate=False)  
    return       
    # else:
    #     $ renpy.retain_after_load()
    #     return