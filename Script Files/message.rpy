
init python:

    ## This is the object that each chat is stored in
    ##  Who = the speaker, What = the text they're saying, thetime keeps track
    ##  of the current time, 'bounce' indicates whether the message is
    ##  supposed to animate in with a bounce or not (by default is false), and
    ##  specBubble is a variable that holds the name of any special speech bubbles
    ##  that should be used when displaying the text (by default is empty and a regular
    ##  bubble is used)
    class Chatentry(object):
        def __init__(self, who, what, thetime, img=False, bounce=False, specBubble=None):
            self.who = who
            self.what = what
            self.thetime = thetime
            self.img = img
            self.bounce = bounce
            self.specBubble = specBubble
            
    # Class to store characters along with their profile picture and a 'file_id'
    # that's appended to things like their special bubble names and saves you from
    # typing out the full name every time
    class Chat(store.object):
        def __init__(self, name, file_id=False, prof_pic=False, participant_pic=False, cover_pic=False, status=False):
            self.name = name            
            self.file_id = file_id
            self.prof_pic = prof_pic
            self.participant_pic = participant_pic
            self.cover_pic = cover_pic
            self.status = status
            self.heart_points = 0  

        def add_heart(self):
            self.heart_points += 1
            
        def lose_heart(self):
            self.heart_points -= 1
            
        def reset_heart(self):
            self.heart_points = 0

        # This function makes it simpler to type out character dialogue
        def __call__(self, what, pauseVal=None, img=False, bounce=False, specBubble=None, **kwargs):
            addchat(self, what, pauseVal=pauseVal, img=img, bounce=bounce, specBubble=specBubble)
            
           
    ##************************************
    ## For ease of creating text messages
    ##************************************  
    
    def addtext(who, what, sender, img=False):
        # Adds the new text to the queue
        for msg in text_queue:
            if msg.sender == sender:
                msg.msg_list.append(Chatentry(who, what, upTime(), img))
                msg.read = False
                if who == m:
                    msg.deliver()
                    msg.reply_label = False
                    renpy.restart_interaction
                    
                

    
    ##************************************
    ## For ease of adding Chatlog entries
    ##************************************   
    
    def addchat(who, what, pauseVal, img=False, bounce=False, specBubble=None):
        global choosing, pre_choosing, pv, chatbackup, oldPV
        choosing = pre_choosing = False
        
        if pauseVal == None:
            pauseVal = pv
            
        if len(chatlog) > 1:
            finalchat = chatlog[-2]
            if finalchat.who.file_id == 'delete':
                # This bubble doesn't display; delete it
                del chatlog[-2]
                
        if who.file_id != 'delete':
            pauseFailsafe()
            chatbackup = Chatentry(who, what, upTime(), img, bounce, specBubble)
            oldPV = pauseVal
            
        if pauseVal == 0:
            pass
        elif who.file_id == 'delete':
            renpy.pause(pv)
        else:
            typeTime = what.count(' ') + 1 # equal to the number of words
            # Since average reading speed is 200 wpm or 3.3 wps
            typeTime = typeTime / 3
            if typeTime < 1.5:
                typeTime = 1.5
            typeTime = typeTime * pauseVal
            renpy.pause(typeTime)
            
        if img == True:
            if what in emoji_lookup:
                renpy.play(emoji_lookup[what], channel="voice_sfx")
        
        chatlog.append(Chatentry(who, what, upTime(), img, bounce, specBubble))
        
    
            
    ## Function that checks if an entry was successfully added to the chat
    ## A temporary fix for the pause button bug
    ## This also technically means a character may be unable to post the exact
    ## same thing twice in a row depending on when the pause button is used
    def pauseFailsafe():
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
                
        if last_chat.who.file_id == chatbackup.who.file_id and last_chat.what == chatbackup.what:
            # the last entry was successfully added; we're done
            return
        else:
            # add the backup entry
            typeTime = chatbackup.what.count(' ') + 1
            typeTime = typeTime / 3
            if typeTime < 1.5:
                typeTime = 1.5
            typeTime = typeTime * oldPV
            renpy.pause(typeTime)
            
            if chatbackup.img == True:
                if chatbackup.what in emoji_lookup:
                    renpy.play(emoji_lookup[chatbackup.what], channel="voice_sfx")
               
            chatlog.append(Chatentry(chatbackup.who, chatbackup.what, upTime(), chatbackup.img, chatbackup.bounce, chatbackup.specBubble))

   
    ### Set a variable to infinity, to be used later -- it keeps the viewport scrolling to the bottom
    yadjValue = float("inf")
    ### Create a ui.adjustment object and assign it to a variable so that we can reference it later. 
    # I'll assign it to the yadjustment property of our viewport later.
    yadj = ui.adjustment()
    
    # This is mostly changed automatically for you when you call
    # chat_begin("night") etc, but if you want to change it on an
    # individual basis this is the colour of the characters' nicknames
    nickColour = "#000000"   

default chatbackup = Chatentry(filler,"","")
default pv = 0.8
default oldPV = pv

screen messenger_screen:

    tag menu

    python:
        #if yadj.value == yadj.range:
        #    yadj.value = yadjValue
        #elif yadj.value == 0:
        #    yadj.value = yadjValue
            
        #if len(chatlog) > 0:
        #    finalchat = chatlog[-1]
        #    if finalchat.who == filler:
        #        yadj.value = yadjValue
        #if len(chatlog) < 3:
        #    yadj.value = yadjValue
        #yinitial = yadjValue
        yadj.value = yadjValue   
            
    #else:
        #image "Phone UI/new_message_banner.png" ypos 170
        #$ new_msg_clicked = False
        #imagebutton:
        #    xanchor 0.0
        #    yanchor 0.0
        #    xpos 0
        #    ypos 169
        #    focus_mask True
        #    idle "new_messages"
        #    action [SetVariable("new_msg_clicked", True), renpy.restart_interaction]
        #if new_msg_clicked:
        #    $ new_msg_clicked = False
        #    $ yadj.value = yadjValue
        #    $ renpy.hide_screen("new_message_screen")
    # else: could have a "new_messages" notification


    window:
        align (0.5, 0.6)
        xfill True
        ysize 1050

        viewport yadjustment yadj: # viewport id "VP":
            draggable True
            mousewheel True
            ysize 1050
                            
            has vbox:
                spacing gui.phone_spacing
                if gui.phone_height:
                    vpgrid:
                        cols 1
                        yinitial 1.0

                        use chat_dialogue()

                else:

                    use chat_dialogue()
                                
                            

screen chat_dialogue():
 
    python:
        chatLength = len(chatlog) - 1
        begin = chatLength - 10
        if begin >= 0:
            pass
        else:
            begin = 0
        
        if chatLength > 0:
            finalchat = chatlog[-1]
            if finalchat.who == answer:
                if begin > 0:
                    begin -= 1
                

    for i in chatlog[begin:]:
        use chat_animation(i)
                      
                      
                      
screen chat_animation(i):

    python:
        include_new = False
        
        if i.bounce:
            transformVar = incoming_message_bounce
            include_new = False
        else:
            transformVar = incoming_message
            include_new = True
            
        if i.who == m:
            nameStyle = 'chat_name_MC'
            include_new = False
        else:
            nameStyle = 'chat_name'
            
            
        if i.who.file_id:
            if i.specBubble != None:
                include_new = False
                bubbleBackground = "Bubble/Special/" + i.who.file_id + "_" + i.specBubble + ".png"    
            elif i.bounce: # Not a special bubble; just glow
                include_new = False
                bubbleBackground = "Bubble/" + i.who.file_id + "-Glow.png"
            elif i.who != 'answer':
                bubbleBackground = "Bubble/" + i.who.file_id + "-Bubble.png"
            
            
            if i.specBubble != None:
                # Some characters have more than one round or square bubble
                # but they follow the same style as "round" or "square"
                if i.specBubble[:6] == "round2":
                    bubbleStyle = "round_" + i.specBubble[-1:]
                elif i.specBubble[:7] == "square2":
                    bubbleStyle = "square_" + i.specBubble[-1:]
                else:
                    bubbleStyle = i.specBubble
            
            if i.img == True:
                include_new = False
                if "{image=" in i.what:
                    pass
                else:
                    transformVar = small_CG
                    
            ## This determines how long the line of text is. If it needs to wrap
            ## it, it will pad the bubble out to the appropriate length
            ## Otherwise each bubble would be exactly as wide as it needs to be and no more
            t = Text(i.what)
            z = t.size()
            my_width = int(z[0])
            my_height = int(z[1])
                    
            global choosing
            
        
    ## First, the profile picture and name, no animation
    if i.who.name == 'msg' or i.who.name == 'filler':
        window:
            style i.who.name + '_bubble'
            text i.what style i.who.name + '_bubble_text'
            
    elif i.who.file_id != 'delete':#i.who != answer and i.who != chat_pause:
        window:
            if i.who == m:
                style 'MC_profpic'
            else:
                style 'profpic'
                
            add i.who.prof_pic
            
        text i.who.name style nameStyle color nickColour
        
        ## Now add the dialogue
        
        if not include_new: # Not a 'regular' dialogue bubble
            window at transformVar:                 
                ## Check if it's an image
                if i.img == True:
                    style 'img_message'
                    # Check if it's an emoji
                    if "{image=" in i.what:
                        text i.what
                    else:   # it's a CG
                        # TODO: Could have a dictionary here that unlocks CGs in a gallery
                        # Would need persistent variables; if i.what in gallery ->
                        # gallery[i.what] = True and then it will be unlocked
                        $ fullsizeCG = i.what
                        imagebutton:
                            bottom_margin -100
                            focus_mask True
                            idle fullsizeCG
                            if not choosing:
                                action [SetVariable("fullsizeCG", i.what), Call("viewCG"), Return]
                                
                                
                ## Check if it's a special bubble
                elif i.specBubble != None:
                    style bubbleStyle 
                    background bubbleBackground # e.g. style "sigh_m" 
                    text i.what style "special_bubble"
                    
                ## Dialogue is either 'glow' or 'regular' variant
                elif i.bounce:
                    # Note: MC has no glowing bubble so there is no variant for them
                    style 'glow_bubble' 
                    background Frame(bubbleBackground, 25, 25)
                    # This checks if the text needs to wrap or not
                    if my_width > gui.longer_than:
                        text i.what style "bubble_text_long" min_width gui.long_line_min_width
                    else:            
                        text i.what style "bubble_text"
                        
                else:
                    style 'reg_bubble_MC'
                    if my_width > gui.longer_than:
                        text i.what style "bubble_text_long" min_width gui.long_line_min_width
                    else:            
                        text i.what style "bubble_text"
                        
        else:
            if my_width > gui.longer_than:
                fixed at transformVar:
                    pos (138, -85)
                    xanchor 0
                    yanchor 0
                    yfit True
                    
                    vbox:
                        spacing -55
                        order_reverse True
                        add 'new_sign' xalign 1.0 yalign 0.0 yoffset 0 xoffset 40 at new_fade
                        window:                        
                            background Frame(bubbleBackground, 25,18,18,18)
                            style 'reg_bubble'
                            text i.what style "bubble_text_long" min_width gui.long_line_min_width
                           
            else:
                fixed at transformVar:
                    pos (138, -85)
                    xanchor 0
                    yanchor 0
                    ysize my_height - 20
                    
                    vbox:
                        spacing -55
                        order_reverse True
                        add 'new_sign' xalign 1.0 yalign 0.0 yoffset 0 xoffset 40 at new_fade
                        window:                        
                            background Frame(bubbleBackground, 25,18,18,18)   
                            style 'reg_bubble_short'
                            text i.what style "bubble_text"
                    
        
        use anti_animation(i)  

#******************************************
#  This code 'cancels out' the animation  *
#   for Mystic messenger; otherwise the   *
# bottom of the viewport would 'slide in' *
#******************************************           
screen anti_animation(i):
    
    python:
        include_new = False
        if i.bounce:
            transformVar = anti_incoming_message_bounce
            include_new = False
        else:
            transformVar = anti_incoming_message
            include_new = True
            
        if i.who == m:
            include_new = False
            
        if i.bounce:
            bubbleBackground = "Bubble/" + i.who.file_id + "-Glow.png"
            include_new = False
        else:
            bubbleBackground = "Bubble/" + i.who.file_id + "-Bubble.png"
            
        if i.specBubble != None:
            if i.specBubble[:6] == "round2":
                bubbleStyle = "round_" + i.specBubble[-1:]
            elif i.specBubble[:7] == "square2":
                bubbleStyle = "square_" + i.specBubble[-1:]
            else:
                bubbleStyle = i.specBubble
                
        if i.specBubble != None:
            include_new = False
            bubbleBackground = "Bubble/Special/" + i.who.file_id + "_" + i.specBubble + ".png"
            
        if i.img == True:
            include_new = False
            if "{image=" in i.what:
                pass
            else:
                transformVar = anti_small_CG
                
        t = Text(i.what)
        z = t.size()
        my_width = int(z[0])
        my_height = int(z[1])
        
        global choosing
        
    if not include_new:
        window at transformVar:
            if i.img == True:
                style "img_message"
                # Check if it's an emoji
                if "{image=" in i.what:
                    # there's an image to display
                    text i.what
                else:   # presumably it's a CG
                    bottom_margin -100
                    text "{image=" + i.what + "}" #"-small}"
                    
            elif i.specBubble != None:                        
                style bubbleStyle background bubbleBackground # e.g. style "sigh_m" 
                text i.what style "special_bubble"
                
            ## Dialogue is either 'glow' or 'regular' variant
            elif i.bounce:
                style 'glow_bubble' 
                background Frame(bubbleBackground, 25, 25)
                if my_width > gui.longer_than:
                    text i.what style "bubble_text_long" min_width gui.long_line_min_width
                else:            
                    text i.what style "bubble_text"
                    
            else:
                style 'reg_bubble_MC'
                if my_width > gui.longer_than:
                    text i.what style "bubble_text_long" min_width gui.long_line_min_width
                else:            
                    text i.what style "bubble_text"

    
    else:
        if my_width > gui.longer_than:
            fixed at transformVar:
                pos (138, -85)
                xanchor 0
                yanchor 0
                yfit True
                
                vbox:
                    spacing -55
                    order_reverse True
                    add 'new_sign' xalign 1.0 yalign 0.0 yoffset 0 xoffset 40 at new_fade
                    window:                        
                        background Frame(bubbleBackground, 25,18,18,18)
                        style 'reg_bubble'
                        text i.what style "bubble_text_long" min_width gui.long_line_min_width
                       
        else:
            fixed at transformVar:
                pos (138, -85)
                xanchor 0
                yanchor 0
                ysize my_height - 20
                
                vbox:
                    spacing -55
                    order_reverse True
                    add 'new_sign' xalign 1.0 yalign 0.0 yoffset 0 xoffset 40 
                    window:                        
                        background Frame(bubbleBackground, 25,18,18,18)   
                        style 'reg_bubble_short'
                        text i.what style "bubble_text"

            
            

            
