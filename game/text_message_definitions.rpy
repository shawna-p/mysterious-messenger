init -6 python:

    from random import randint
    import renpy.store as store
    
    ## The Text_Message class keeps track of a text message conversation
    ##  for each character. The actual messages are stored in msg_list
    class Text_Message(object):
        def __init__(self):
            # List of currently sent messages
            self.msg_list = []
            # List of messages waiting to be delivered
            self.msg_queue = []
            # Reply label to jump to when responding
            self.reply_label = False
            # Whether this message has been read
            self.read = False
            # If this message should trigger a heart icon when read
            self.heart = False
            # Who the heart icon should belong to
            self.heart_person = None
            # If the awarded heart is 'bad'
            self.bad_heart = False
            # List to keep track of CGs we should unlock after
            # the player has read this message chain
            self.cg_unlock_list = []
            # True if the player has already been told they have
            # an unread message
            self.notified = True
    
        ## Transfers messages from the msg_queue to 
        ## the player's inbox
        def deliver(self):
            # If we're not on the text message screen, we can add
            # these messages to the regular message list
            if self.msg_queue and not renpy.get_screen('text_message_screen'):
                self.msg_list.extend(self.msg_queue)
                self.msg_queue = []                
                # If the last message was sent by someone other
                # than the MC
                if not self.msg_list[-1].who.right_msgr:
                    # We notify the player of the delivered message
                    self.read = False
                    renpy.music.play(persistent.text_tone, 'sound')
                    popup_screen = allocate_text_popup()
                    renpy.show_screen(popup_screen, 
                        c=self.msg_list[-1].who)
                    self.notified = True
                else:
                    self.read = True
            renpy.retain_after_load()

            
        ## Marks the message as read and unlocks
        ## the appropriate CGs, if applicable
        def mark_read(self):
            self.read = True 
            # We also need to unlock any CG images they see
            for pair in self.cg_unlock_list:
                # pair[0] is persistent.??_album
                # pair[1] is the Album(filepath)   
                for photo in pair[0]:
                    if pair[1] == photo:
                        photo.unlock()
            self.cg_unlock_list = []
            renpy.retain_after_load()
            renpy.restart_interaction()         
            
        ## This takes you to the correct message reply label
        ## and indicates that the message has been read
        def reply(self):
            store.text_msg_reply = True
            old_reply = self.reply_label
            renpy.call_in_new_context(self.reply_label)
            # If we've updated the reply label, then we don't
            # erase it. Otherwise, the player shouldn't be able
            # to reply twice
            if self.reply_label == old_reply:
                self.reply_label = False
            store.text_msg_reply = False  
            
        ## Determines who to award the heart point to
        def heart_point(self, person=None, bad=False):
            self.heart = True
            self.heart_person = person
            self.bad_heart = bad
                    
    ## Lets the program know the response will trigger a heart point
    def add_heart(who, person=None, bad=False):
        who.text_msg.heart_point(person, bad)
             
    ## Delivers all of the text messages at once
    def deliver_all(): 
        for c in store.all_characters:
            c.text_msg.deliver()
        
    ## Returns the number of unread messages in text_messages
    def new_message_count():
        unread_messages = [ x for x in all_characters if (x.text_msg.msg_list
                                                    and not x.text_msg.read) ]
        return len(unread_messages)
    
    ## Returns the number of undelivered messages in text_queue
    def num_undelivered():
        undelivered = [ x for x in all_characters if x.text_msg.msg_queue ]
        return len(undelivered)
        
    ##************************************
    ## For ease of creating text messages
    ##************************************  
    ## This is used specifically for non-real time texting
    ## So new messages get added to a queue first before being delivered
    def addtext(who, what, img=False):
        sender = store.text_person
        # If the MC sent this message, we deliver it immediately
        if who.right_msgr:
            sender.text_msg.msg_list.append(Chatentry(who, what, upTime(), img))
            sender.text_msg.read = True
            sender.text_msg.notified = True
            sender.text_msg.reply_label = False
            
        else:
            # Otherwise another character sent this/is replying
            # We add this message to the sender's queue
            sender.text_msg.msg_queue.append(Chatentry(
                                                who, what, upTime(), img))
            # sender.text_msg.read = False
            sender.text_msg.notified = False
        
        # We also check if the sent message has a CG
        if img and "{image" not in what:
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

        renpy.restart_interaction()

    ## This version is used for real-time texting
    ## Each entry is added after a small pause to simulate typing time
    def addtext_realtime(who, what, pauseVal, img=False):
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
            textbackup = Chatentry(who, what, upTime(), img)
            oldPV = pauseVal
        
        if pauseVal == 0:
            pass
        # If we're not on the text message screen currently reading
        # this, it should be delivered instantly
        elif not renpy.get_screen('text_message_screen'):
            if not who.right_msgr:
                store.text_person.text_msg.notified = False
            pass
        elif who.file_id == 'delete':
            renpy.pause(pv)
        # Otherwise we pause to simulate typing time
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
            if (what in emoji_lookup
                    and renpy.get_screen('text_message_screen')):
                renpy.play(emoji_lookup[what], channel='voice_sfx')
            elif "{image" not in what:
                # We want to unlock the CG in the gallery
                # These will be equal to a path like
                # CGs/common_album/cg-1.png
                cg_filepath = cg_helper(what)
                album, cg_name = what.split('/')
                if album[-6:] != '_album':
                    album += '_album'                
                # Now we need to search for that CG
                for photo in getattr(persistent, album):
                    if cg_filepath == photo.img:
                        photo.unlock()
                        break
                    
        textlog.append(Chatentry(who, what, upTime(), img))
        renpy.checkpoint()

    ## This ensures we don't miss any messages being posted 
    def text_pauseFailsafe(textlog):
        global textbackup

        # If we're resetting the backup, we're done
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
            # The last entry was successfully added; we're done
            return

        if renpy.get_screen('text_message_screen'):
            typeTime = textbackup.what.count(' ') + 1
            typeTime /= 3
            if typeTime < 1.5:
                typeTime = 1.5
            typeTime = typeTime * oldPV
            renpy.pause(typeTime)

        if textbackup.img == True:
            if (textbackup.what in emoji_lookup 
                    and renpy.get_screen('text_message_screen')):
                renpy.play(emoji_lookup[textbackup.what], channel="voice_sfx")

        textlog.append(Chatentry(textbackup.who, textbackup.what,
                upTime(), textbackup.img))
        renpy.checkpoint()
               
        

    ## This simplifies some of the code that parses what's in the text 
    ## message so it can display a preview of the appropriate length
    def text_popup_preview(last_msg, num_char=48):
        global name
        name_cut = num_char + 6 - len(name)
        
        if last_msg and ("{image=" in last_msg.what or last_msg.img):
            if last_msg.who.right_msgr:
                return "You sent an image."
            else:
                return last_msg.who.name + " sent an image."

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
            if len(msg) < len(last_msg.what):
                return msg + '...'
            else:
                return msg

        if last_msg and len(last_msg.what) > num_char:
            return last_msg.what[:num_char] + '...'
        elif last_msg:
            return last_msg.what[:num_char]
            

default current_message = None
default text_msg_reply = False
# Stores the Chat object of the other person in a text conversation
default text_person = None
# This keeps track of whose text conversation the player is viewing
# so they can view CGs full-screen
default CG_who = None

## A label that lets you leave instant text message
## conversations, but you can't get them back
label leave_inst_text():
    $ textlog = text_person.text_msg.msg_list                        
    $ config.skipping = False   
    $ greeted = False         
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
    
label text_begin(who):    
    $ text_person = who
    $ text_msg_reply = True
    $ who.text_msg.mark_read()
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
    $ text_person.set_text_label(text_label)
    $ text_person = None
    $ textbackup = 'Reset'
    $ renpy.retain_after_load()
    return
    

## Sets end variables when a text message menu is completed 
label text_end():
    if text_person is not None and text_person.real_time_text:        
        $ text_pauseFailsafe(text_person.text_msg.msg_list)
        answer "" (pauseVal=1.0)
    if (len(text_person.text_msg.msg_list) > 0
            and text_person.text_msg.msg_list[-1].who.file_id == 'delete'):
        $ text_person.txt_msg.msg_list.pop()  
    $ text_msg_reply = False
    #if text_person is not None and text_person.real_time_text:
    $ text_person.finished_text()
    $ who = text_person
    $ text_person = None
    $ chatroom_hp = 0
    $ textbackup = Chatentry(filler,"","")
    $ renpy.retain_after_load()        
    hide screen text_answer
    hide screen inactive_text_answer
    hide screen text_play_button
    hide screen text_pause_button  
    call screen text_message_screen(who)         
    # else:
    #     $ renpy.retain_after_load()
    #     return