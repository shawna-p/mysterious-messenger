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
    class Chatentry(object):
        def __init__(self, who, what, thetime, img=False, 
                        bounce=False, specBubble=None):
            self.who = who
            self.what = what
            self.thetime = thetime
            self.img = img
            self.bounce = bounce
            self.specBubble = specBubble

    ## Class that is functionally the same as a Chatentry, but
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
    
    ## This corrects the dialogue into a filepath for the program
    def cg_helper(what):
        album, cg_name = what.split('/')
        if album[-6:] != '_album':
            album += '_album'
        # These will be equal to a path like
        # CGs/common_album/cg-1.png
        return 'CGs/' + album + '/' + cg_name

    def smallCG(bigCG):
        return Transform(bigCG, zoom=0.35)

    ## This function adds entries to the chatlog
    ## It also takes care of several "behind-the-scenes" functions,
    ## such as how long to wait before each character replies
    def addchat(who, what, pauseVal, img=False, bounce=False, specBubble=None):
        global choosing, pre_choosing, pv, chatbackup, oldPV, observing
        global persistent, cg_testing
        choosing = False
        pre_choosing = False
                
        # If we didn't get an explicit pauseVal, we use
        # the default one
        if pauseVal is None:
            pauseVal = pv

        # Now we have a function that's going to act as a 
        # check to see if the most recent message was skipped
        # Pausing in the middle of the chat often causes the
        # program to skip a message, and this will catch that
        if who.file_id != 'delete':
            pauseFailsafe() # This ensures the message that was
                            # supposed to be posted was, in fact,
                            # posted
            chatbackup = Chatentry(who, what, upTime(), 
                                    img, bounce, specBubble)
            oldPV = pauseVal
            
        # Now we calculate how long we should wait before 
        # posting messages, to simulate typing time
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
            
        # If it's an image, we first check if it's an emoji
        # If so, it has an associated sound file
        if img == True:
            if what in emoji_lookup:
                renpy.play(emoji_lookup[what], channel="voice_sfx")
            elif "{image=" not in what and not observing:
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
        
        # We're done and can add this entry to the chatlog
        chatlog.append(Chatentry(who, what, upTime(), 
                            img, bounce, specBubble))
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
            # the last entry was successfully added; we're done
            return
        else:
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
            
            if chatbackup.img == True:
                if chatbackup.what in emoji_lookup:
                    renpy.play(emoji_lookup[chatbackup.what], 
                        channel="voice_sfx")
               
            chatlog.append(Chatentry(chatbackup.who, chatbackup.what, 
                                        upTime(), chatbackup.img, 
                                        chatbackup.bounce, 
                                        chatbackup.specBubble))

# Values in order to keep the viewport scrolling
# to the bottom - we set a ui.adjustment() object
# to infinity so it stays at the maximum range
define yadjValue = float("inf")
default yadj = ui.adjustment()
# Default nickname colour for the characters' names
default nickColour = "#000000"
# Default variable to adjust chat speed by
default pv = 0.8
# These two values are used for the pauseFailSafe function
default chatbackup = Chatentry(filler,"","")
default oldPV = pv

# Number of bubbles to keep on the screen at once
# (larger numbers may slow down the program; too
# small and there may not be enough to fill the screen)
default bubbles_to_keep = 10

#####################################
# Chat Setup
#####################################

# This simplifies things when you're setting up a chatroom,
# so call it when you're about to begin
# If you pass it the name of the background you want (enclosed in
# single ' or double " quotes) it'll set that up too
# Note that it automatically clears the chatlog, so if you want
# to change the background but not clear the messages on-screen,
# you'll also have to pass it 'False' as its second argument

label chat_begin(background=None, clearchat=True, resetHP=True):
    stop music
    if clearchat:
        $ chatlog = []
        # $ pv = 0.8    # This resets the chatroom "speed"
                        # Ordinarily it would reset for every
                        # new chatroom, and if you want that
                        # functionality you can un-comment this
                        # line
    # We reset the heart points for this chatroom
    if resetHP:
        $ chatroom_hp = 0

    # Make sure we're showing the messenger screens
    hide screen starry_night
    show screen phone_overlay
    show screen messenger_screen 
    show screen pause_button
    
    # Hide all the popup screens
    hide screen text_msg_popup
    hide screen email_popup
    
    $ text_person = None
    window hide
    $ text_msg_reply = False
    $ in_phone_call = False
    $ vn_choice = False
    $ email_reply = False
    
    # Fills the beginning of the screen with 'empty space' 
    # so the messages begin showing up at the bottom of the 
    # screen (otherwise they start at the top)
    if clearchat:
        $ addchat(filler, "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", 0)
        
    # Sets the correct background and nickname colour
    # You'll need to add other backgrounds here if you define
    # new ones
    $ current_background = background
    if background == "morning":
        scene bg morning
        $ nickColour = black
    elif background == "noon":
        scene bg noon
        $ nickColour = black
    elif background == "evening":
        scene bg evening
        $ nickColour = black
    elif background == "night":
        scene bg night
        $ nickColour = white
    elif background == "earlyMorn":
        scene bg earlyMorn
        $ nickColour = white
    elif background == "hack":
        scene bg hack
        $ nickColour = white
    elif background == "redhack":
        scene bg redhack
        $ nickColour = white
    elif background == "redcrack":
        scene bg redcrack
        $ nickColour = white
    else:
        scene bg black
        $ nickColour = white
        $ current_background = "morning"

        
    # If you've already played this chatroom in your current runthrough,
    # viewing it again causes this variable to be True. It prevents you
    # from receiving heart points again and only lets you select choices
    # you've selected on this or previous playthroughs
    if current_chatroom.played:
        if not persistent.testing_mode:
            $ observing = True     
        else:
            $ observing = False
    else:
        $ observing = False
        
    # We add this background to the replay log
    if not observing and not persistent.testing_mode:
        $ bg_entry = ("background", "bg " + current_background)
        $ current_chatroom.replay_log.append(bg_entry)

    # This resets the heart points you've collected from
    # previous chatrooms so it begins at 0 again   
    if resetHP:
        $ in_chat = []
        python:
            for person in current_chatroom.original_participants:
                if person.name not in in_chat:
                    in_chat.append(person.name)
            
        # If the player is participating, add them to the list of
        # people in the chat
        if (not current_chatroom.expired 
                or current_chatroom.buyback 
                or current_chatroom.buyahead):
            $ in_chat.append(m.name)
        
    return

## Call this label to show the save & exit sign
label chat_end():
    if starter_story:        
        $ persistent.first_boot = False
        $ persistent.on_route = True
    call screen save_and_exit    
    return
    
## Call this label at the very end of the route
## to show a good/bad/normal ending sign and
## return the player to the main menu
label chat_end_route(type='good'):
    call screen save_and_exit(True)
    $ config.skipping = False
    $ greeted = False
    $ choosing = False
    hide screen phone_overlay
    hide screen messenger_screen
    stop music
    
    if type == 'good':
        scene bg good_end
    elif type == 'normal':
        scene bg normal_end
    elif type == 'bad':
        scene bg bad_end
    pause
    return

## This is set of screens which handles displaying the
## messages in the chatlog to the screen
screen messenger_screen():

    tag menu

    python:
        # This is the infinite value from earlier which
        # tells the viewport to always scroll to
        # the bottom
        yadj.value = yadjValue 
        # Now we also set up how many messages
        # we want the user to be able to scroll
        # back and see
        chatLength = len(chatlog) - 1
        begin = chatLength - bubbles_to_keep
        if begin >= 0:
            pass
        else:
            begin = 0
        
        finalchat = None
        if chatLength > 0:
            finalchat = chatlog[-1]
            if finalchat.who == answer:
                if begin > 0:
                    begin -= 1  

    window:
        align (0.5, 0.6)
        xfill True
        ysize 1050

        viewport yadjustment yadj: # viewport id "VP":
            draggable True
            mousewheel True
            ysize 1050
                            
            has vbox:
                spacing 10
                for i index id(i) in chatlog[begin:]:
                    fixed:
                        yfit True
                        xfit True
                        if i == finalchat:
                            use chat_animation(i, True, True)
                        use chat_animation(i)
                    null height 10
                        

## This screen does the heavy lifting for displaying
## all the messages, names, profile pictures, etc
screen chat_animation(i, animate=True, anti=False):

    python:
        # First we set up a bunch of variables
        # so we know how to display the message
        include_new = False

        # If this message bounces, use that transformation
        if i.bounce:
            transformVar = incoming_message_bounce
            include_new = False
        else:
            transformVar = incoming_message
            include_new = True
            
        # MC's messages are displayed differently
        if i.who.right_msgr:
            nameStyle = 'chat_name_MC'
            include_new = False
            picStyle = 'MC_profpic'
            imgStyle = 'mc_img_message'
            reg_style = 'reg_bubble_MC'
        else:
            nameStyle = 'chat_name'
            picStyle = 'profpic'
            imgStyle = 'img_message'
            reg_style = 'reg_bubble'
            
            
        if i.who.file_id:
            # If this is a special bubble, set the background
            # according to the given bubble
            if i.specBubble != None and i.specBubble != 'glow2':
                include_new = False
                bubbleBackground = ("Bubble/Special/" 
                                        + i.who.file_id + "_" 
                                        + i.specBubble + ".png")  
            # Otherwise there's a special case where we might
            # get a 'glow2' bubble aka another glow variant
            elif i.specBubble != None and i.specBubble == 'glow2':
                include_new = False
                bubbleBackground = Frame("Bubble/Special/" + i.who.file_id 
                                    + "_" + i.specBubble + ".png", 25, 25)

            elif i.bounce: # Not a special bubble; just glow
                include_new = False
                bubbleBackground = i.who.glow_bubble_img
            elif i.who != 'answer':
                bubbleBackground = i.who.reg_bubble_img
            
            if i.specBubble != None:
                # Some characters have more than one round or square bubble
                # but they follow the same style as "round" or "square"
                if i.specBubble[:6] == "round2":
                    bubbleStyle = "round_" + i.specBubble[-1:]
                elif i.specBubble[:7] == "square2":
                    bubbleStyle = "square_" + i.specBubble[-1:]
                elif i.specBubble == "glow2":
                    bubbleStyle = 'glow_bubble'
                else:
                    bubbleStyle = i.specBubble
            
            # If it's a CG, we use a different
            # transform
            if i.img == True:
                include_new = False
                    
            # This determines how long the line of text is. 
            # If it needs to wrap it, it will pad the bubble 
            # out to the appropriate length
            # Otherwise each bubble would be exactly as wide 
            # as it needs to be and no more
            t = Text(i.what)
            z = t.size()
            my_width = int(z[0])
            my_height = int(z[1])
                    
            global choosing

        # This is used specifically in the create-a-chatroom
        # screens
        if not animate:
            global f_style_begin, f_style_end
            transformVar = null_anim
            nickColour = white
            dialogue = f_style_begin + i.what + f_style_end
        else:
            dialogue = i.what

        if anti and i.bounce:
            transformVar = invisible_bounce
        elif anti:
            transformVar = invisible


    # This displays the special messages like "xyz
    # has entered the chatroom"
    if (i.who.name == 'msg' or i.who.name == 'filler') and not anti:
        window:
            style i.who.name + '_bubble'            
            text dialogue style i.who.name + '_bubble_text'
            

    # Otherwise it's a regular character; add
    # their profile picture
    elif i.who.file_id and i.who.file_id != 'delete':
        window:
            xysize (110, 110)
            style picStyle
            if not anti:
                add Transform(i.who.prof_pic, size=(110, 110))

        # Add their nickname
        if not anti:
            text i.who.name style nameStyle color nickColour
        else:
            text i.who.name at invisible

        # Now we add the dialogue
        if not include_new: # Not a "regular" dialogue bubble
            window at transformVar:
                # Check if it's an image
                if i.img:
                    style imgStyle
                    if "{image=" in i.what:
                        text i.what
                    else: # it's a CG                            
                        $ fullsizeCG = cg_helper(i.what)
                        imagebutton:
                            focus_mask True
                            idle smallCG(fullsizeCG)
                            if not choosing:
                                action [SetVariable("fullsizeCG", 
                                            cg_helper(i.what)), 
                                            Call("viewCG"), 
                                            Return()]


                # Not an image; check if it's a special bubble
                elif i.specBubble != None and i.specBubble != 'glow2':
                    style bubbleStyle
                    background bubbleBackground # e.g. 'sigh_m'
                    text dialogue style 'special_bubble'

                # Not img or special bubble; check if glow variant
                elif i.bounce:
                    # Note: MC has no glowing bubble so there is
                    # no variant for them
                    style 'glow_bubble'
                    background bubbleBackground
                    # This checks if the text needs to wrap or not
                    if my_width > gui.longer_than:
                        text dialogue:
                            style 'bubble_text_long' 
                            min_width gui.long_line_min_width
                    else:            
                        text dialogue:
                            style 'bubble_text'

                # Otherwise it must be regular MC dialogue
                else:
                    style reg_style
                    background bubbleBackground
                    if my_width > gui.longer_than:
                        text dialogue:
                            style 'bubble_text_long'
                            min_width gui.long_line_min_width
                    else:            
                        text dialogue style "bubble_text"

        # This does indeed need the 'new' sign
        else:
            frame at transformVar:
                pos (138,24)
                xsize 500
                background None
                vbox:
                    spacing -20
                    order_reverse True
                    add 'new_sign' align (1.0, 0.0) xoffset 40 at new_fade
                    frame:
                        padding (25,12,20,12)
                        background bubbleBackground
                        text dialogue:
                            if my_width > gui.longer_than:
                                style 'bubble_text_long'
                                min_width gui.long_line_min_width
                            else:
                                style 'bubble_text'
                                

   

                                
                            

        
                
     
            