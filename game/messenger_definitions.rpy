init -4 python:

    ## This is the object that each chat is stored in
    ##  who = the speaker
    ##  what = the text they're saying
    ##  thetime keeps track of the current time
    ##  img indicates whether this post includes an image
    ##  bounce indicates whether the message is supposed to animate in 
    ##      with a bounce or not (by default is false)
    ##  specBubble is a variable that holds the name of any special 
    ##      speech bubbles that should be used when displaying the text
    ##      (by default is empty and a regular bubble is used)
    class ChatEntry(object):
        def __init__(self, who, what, thetime, img=False, 
                        bounce=False, specBubble=None):
            self.who = who
            self.what = what
            self.thetime = thetime
            self.img = img
            self.bounce = bounce
            self.specBubble = specBubble

    ## Class that is functionally the same as a ChatEntry, but
    ## keeps track of "replay" entries for the replay function
    class ReplayEntry(object):
        def __init__(self, who, what, pauseVal=None, img=False,
                        bounce=False, specBubble=None):
            self.who = who
            self.what = what
            self.pauseVal = pauseVal
            self.img = img
            self.bounce = bounce
            self.specBubble = specBubble

    ##************************************
    ## For ease of adding Chatlog entries
    ##************************************   

    ## This function adds entries to the chatlog
    ## It also takes care of several "behind-the-scenes" functions,
    ## such as how long to wait before each character replies
    def addchat(who, what, pauseVal, img=False, bounce=False, specBubble=None):
        global choosing, pre_choosing, pv, chatbackup, oldPV, observing
        global persistent, cg_testing
        choosing = False
        pre_choosing = False
                
        # If the program didn't get an explicit pauseVal,
        # use the default one
        if pauseVal is None:
            pauseVal = pv

        # Now check to see if the most recent message was skipped
        # Pausing in the middle of the chat often causes the
        # program to skip a message, and this will catch that
        if who.file_id != 'delete':
            pauseFailsafe() # This ensures the message that was
                            # supposed to be posted was, in fact,
                            # posted
            # Store the current message in the backup
            chatbackup = ChatEntry(who, what, upTime(), 
                                    img, bounce, specBubble)
            oldPV = pauseVal
            
        # Now calculate how long to wait before 
        # posting messages to simulate typing time
        if pauseVal == 0:
            pass
        elif who.file_id == 'delete':
            renpy.pause(pv)
        else:
            typeTime = what.count(' ') + 1 # equal to the # of words
            # Since average reading speed is 200 wpm or 3.3 wps
            typeTime = typeTime / 3
            if typeTime < 1.5:
                typeTime = 1.5
            typeTime = typeTime * pauseVal
            renpy.pause(typeTime)
            
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
                # This will be equal to a path like
                # CGs/common_album/cg-1.png
                cg_filepath = cg_helper(what)
                album, cg_name = what.split('/')
                if album[-6:] != '_album':
                    album += '_album'
                # Now search for the CG
                for photo in getattr(persistent, album):
                    if cg_filepath == photo.img:
                        photo.unlock()
                        break
        
        # Add this entry to the chatlog
        chatlog.append(ChatEntry(who, what, upTime(), 
                            img, bounce, specBubble))
        # Create a rollback checkpoint
        renpy.checkpoint()
        
    
            
    ## Function that checks if an entry was successfully added
    ## to the chat. This also technically means a character may be 
    ## unable to post the exact same thing twice in a row depending
    ## on when the pause button is used
    def pauseFailsafe():
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
       
        # add the backup entry to the chatlog
        if reply_instant:
            reply_instant = False
        else:
            typeTime = chatbackup.what.count(' ') + 1
            typeTime = typeTime / 3
            if typeTime < 1.5:
                typeTime = 1.5
            typeTime = typeTime * oldPV
            renpy.pause(typeTime)
        
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
                # This will be equal to a path like
                # CGs/common_album/cg-1.png
                cg_filepath = cg_helper(chatbackup.what)
                album, cg_name = chatbackup.what.split('/')
                if album[-6:] != '_album':
                    album += '_album'
                # Now search for the CG
                for photo in getattr(persistent, album):
                    if cg_filepath == photo.img:
                        photo.unlock()
                        break
            
        chatlog.append(ChatEntry(chatbackup.who, chatbackup.what, 
                                    upTime(), chatbackup.img, 
                                    chatbackup.bounce, 
                                    chatbackup.specBubble))
                                        
init python:
    # Increase/decrease the chat speed
    def slow_pv():
        global pv
        if pv <= 1.1:
            pv += 0.09  
        return
        
    def fast_pv():
        global pv
        if pv >= 0.53:
            pv -= 0.09
        return

    # This is a helper function for the heart icon that dynamically 
    # recolours a generic white heart depending on the character
    # See character_definitions.rpy to define your own character 
    # & heart point
    def heart_icon(character):
        if character.heart_color:
            return im.MatrixColor("Heart Point/Unknown Heart Point.png", 
                    im.matrix.colorize("#000000", character.heart_color))
        else:
            return "Heart Point/Unknown Heart Point.png"
        
    # Similarly, this recolours the heartbreak animation
    def heart_break_img(picture, character):
        if character.heart_color:
            return im.MatrixColor(picture, 
                    im.matrix.colorize("#000000", character.heart_color))
        else:
            return "Heart Point/heartbreak_0.png"
        
    ## These next two functions recolour "generic" speech bubbles
    ## so you can have custom glow/regular bubbles
    def glow_bubble_fn(glow_color='#000'):
        return im.MatrixColor('Bubble/Special/sa_glow2.png', 
                            im.matrix.colorize(glow_color, '#fff'))
    
    def reg_bubble_fn(bubble_color='#000'):
        return im.MatrixColor('Bubble/white-Bubble.png', 
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
# These two values are used for the pauseFailSafe function
default chatbackup = ChatEntry(filler,"","")
default oldPV = pv

# Number of bubbles to keep on the screen at once
# (larger numbers may slow down the program; too
# small and there may not be enough to fill the screen)
default bubbles_to_keep = 10
# Keeps track of the current background for calls such as "shake"
default current_background = "morning"


    
    
        
