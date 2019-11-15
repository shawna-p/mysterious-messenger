init python:

    from random import randint

    ## This code is adapted from saguaro's email message system with 
    ## contributions from xavimat, found at 
    ## http://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=19295 
    ## and is used under the CC0 1.0 Universal license
    
    import renpy.store as store
    
    reply_screen = False

    ## The Text_Message class keeps track of a text message conversation
    ##  for each character. The actual messages are stored in msg_list
    class Text_Message(object):
        def __init__(self, sender, msg_list, reply_label=False, delay=True, 
                    read=False, heart=False):
            self.sender = sender
            self.msg_list = msg_list
            self.reply_label = reply_label
            self.delay = delay
            self.read = read
            self.heart = False
            self.heart_person = sender
            self.cg_unlock_list = []
            self.notified = True
    
        ## Transfers messages from the text_queue to 
        ## the player's inbox
        def deliver(self, instant=False):
            global text_messages
            # Move messages to 'inbox'
            for msg in text_messages:
                if msg.sender == self.sender:
                    if self.msg_list:
                        if (instant or 
                                not renpy.get_screen('text_message_screen')):
                            msg.msg_list.extend(self.msg_list) 
                            # Clear the queued message; it's been delivered
                            self.msg_list = []
                            # Transfer cg_unlock_list
                            msg.cg_unlock_list = self.cg_unlock_list
                            # Clear queued cg_unlock_list
                            self.cg_unlock_list = []
                            # Player has been notified
                            msg.notified = True
                            # Move the delivered message to the 
                            # top of the list (newest)
                            text_messages.remove(msg)
                            text_messages.insert(0, msg)
                            if msg.msg_list[-1].who != m:
                                msg.read = False
                                renpy.restart_interaction()
                                # Notify the player of the delivered message                                
                                renpy.music.play(persistent.text_tone, 'sound')
                                renpy.show_screen('text_msg_popup', the_msg=msg)                                
                            else:
                                msg.read = True
                            renpy.retain_after_load()
            
        ## Marks the message as read and unlocks
        ## the appropriate CGs, if applicable
        def mark_read(self):
            self.read = True 
            for pair in self.cg_unlock_list:
                # pair[0] is persistent.??_album
                # pair[1] is the Album(filepath)   
                for photo in pair[0]:
                    if pair[1] == photo:
                        photo.unlock()
            self.cg_unlock_list = []
            renpy.restart_interaction()         
            
        ## This takes you to the correct message reply label
        ## and indicates that the message has been read
        def reply(self):
            global reply_screen
            reply_screen = True
            old_reply = self.reply_label
            renpy.call_in_new_context(self.reply_label)
            # If we've updated the reply label, then we don't
            # erase it. Otherwise, the player shouldn't be able
            # to reply twice
            if self.reply_label == old_reply:
                self.reply_label = False
            reply_screen = False  
            
        ## Determines who to award the heart point to
        def heart_point(self, person=False):
            if not person:
                self.heart = True
                self.heart_person = self.sender
            else:
                self.heart = True
                self.heart_person = person
        
    ## Lets the program know the response will trigger a heart point
    def add_heart(who, person=False):
        for msg in text_messages:
            if msg.sender == who:
                if not person:
                    msg.heart_point()
                else:
                    msg.heart_point(person)
          
    ## Returns whether or not the message has been read
    def check(sender):
        for item in text_messages:
            if item.sender == sender:
                if item.read:
                    return True
                else:
                    return False
           
    ## Updates the message's reply label
    def add_reply_label(sender, reply_label):
        for item in text_messages:
            if item.sender == sender:
                item.reply_label = reply_label
        for item in text_queue:
            if item.sender == sender:
                item.reply_label = reply_label
             
    ## Delivers all of the text messages at once
    def deliver_all(): 
        global text_queue
        for msg in text_queue:
            msg.deliver()
                
    ## Checks who the sender of the next text message to be delivered is
    def who_deliver():
        global text_queue
        for msg in text_queue:
            if msg.msg_list:
                return msg.sender
        
    ## Returns the number of unread messages in text_messages
    def new_message_count():
        global persistent, text_messages, all_characters
        if not persistent.instant_texting:
            unread_messages = [ x for x in text_messages if (not x.read 
                                                            and x.msg_list)]
            return len(unread_messages)
        else:
            unread_messages = [ c for c in all_characters if (not c.right_msgr 
                                and c.private_text 
                                and (not c.private_text_read 
                                or c.private_text_read == "Notified")) ]
            return len(unread_messages)
    
    ## Returns the number of undelivered messages in text_queue
    def num_undelivered():
        undelivered = [ x for x in text_queue if x.msg_list ]
        return len(undelivered)
        
    ##************************************
    ## For ease of creating text messages
    ##************************************  
    
    def addtext(who, what, sender, img=False):
        global observing
        # Adds the new text to the queue
        for msg in text_queue:
            if msg.sender == sender:
                msg.msg_list.append(Chatentry(who, what, upTime(), img))
                msg.read = False
                if who.right_msgr:
                    msg.deliver(True)
                    msg.reply_label = False
                else:
                    msg.notified = False
            if img and "{image=" not in what and not observing:
                # We want to unlock the CG in the gallery
                # First, we split up the text
                cg_filepath = cg_helper(what)
                album, cg_name = what.split('/')
                if album[-6:] != '_album':
                    album += '_album'
                
                # Now we need to search for that CG
                cg_list = getattr(persistent, album)
                for photo in cg_list:
                    if Album(cg_filepath) == photo:
                        if who.right_msgr:
                            photo.unlock()
                        else:
                            msg.cg_unlock_list.append([cg_list, photo])
                        break
        renpy.restart_interaction

    ## This simplifies some of the code that parses what's in the text 
    ## message so it can display a preview of the appropriate length
    def text_popup_preview(last_msg, num_char=48):
        global name
        name_cut = num_char + 6 - len(name)
        
        if "[" in last_msg.what:
            # Means we have to do some cleanup to ensure
            # variables aren't cut up
            # First check if the variable is [name]
            if "[name]" in last_msg.what:
                msg = last_msg.what[:name_cut]
            else:
                msg = last_msg.what[:num_char]
            n = msg.rfind(' ')
            if n > 0:
                msg = msg[:n]
        
        if last_msg and ("{image=" in last_msg.what or last_msg.img):
            if last_msg.who.right_msgr:
                return "You sent an image."
            else:
                return last_msg.who.name + " sent an image."
        elif last_msg and len(last_msg.what) > 48:
            return last_msg.what[:num_char] + '...'
        elif last_msg:
            return last_msg.what[:num_char]
            

default current_message = None