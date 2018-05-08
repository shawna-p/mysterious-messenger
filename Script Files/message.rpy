
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
            
    # This class just makes it simpler to type out character dialogue
    class Chat(object):
        def __init__(self, who):
            self.who = who
            
        def __call__(self, what, pauseVal=None, img=False, bounce=False, specBubble=None, txtmsg=False, sender=None, **kwargs):
            if not txtmsg:
                addchat(self.who, what, pauseVal=pauseVal, img=img, bounce=bounce, specBubble=specBubble)
            else:
                addtext(self.who, what, sender=sender, img=img)
           
           
    ##************************************
    ## For ease of creating text messages
    ##************************************  
    
    def addtext(who, what, sender, img=False):
        # Adds the new text to the queue
        for msg in text_queue:
            if msg.sender == sender:
                msg.msg_list.append(Chatentry(who, what, upTime(), img))
                msg.read = False
                if who == 'MC':
                    msg.deliver()
                    msg.reply_label = False
                    renpy.restart_interaction
                    
                

    
    ##************************************
    ## For ease of adding Chatlog entries
    ##************************************   

    def addchat(who, what, pauseVal, img=False, bounce=False, specBubble=""):  
        global choosing, pre_choosing
        choosing = False
        pre_choosing = False
        
        global pv
        if pauseVal == None:
            pauseVal = pv;
    
        if len(chatlog) > 1:
            finalchat = chatlog[-2]
            if finalchat.who == "answer" or finalchat.who == "pause":
                # Not supposed to display this bubble; delete it
                # It's useful only as the most recent bubble as it
                # stops the previous bubbles from animating
                del chatlog[-2]  
                
        if who != "pause":
            pauseFailsafe()
            global chatbackup
            chatbackup = Chatentry(who, what, upTime(), img, bounce, specBubble)
            global oldPV
            oldPV = pauseVal        
                    
        
        if who == "answer" or who == "pause":
            renpy.pause(pauseVal)#, hard=True)
        elif pauseVal == 0:
            pass
        else:
            typeTime = what.count(' ') + 1 # should be the number of words
            # Since average reading speed is 200 wpm or 3.3 wps
            typeTime = typeTime / 3
            if typeTime < 1.5:
                typeTime = 1.5
            typeTime = typeTime * pauseVal
            renpy.pause(typeTime)#, hard=True)
        
        if img == True:
            if what in emoji_lookup:
                renpy.play(emoji_lookup[what], channel="voice_sfx")
           
        chatlog.append(Chatentry(who, what, upTime(), img, bounce, specBubble))
            
    ## Function that checks if an entry was successfully added to the chat
    ## A temporary fix for the pause button bug
    ## This also technically means a character may be unable to post the exact
    ## same thing twice in a row depending on when the pause button is used
    def pauseFailsafe():
        global chatbackup
        global oldPV
        last_entry = None
        if len(chatlog) > 0:
            last_entry = chatlog[-1]
            if last_entry.who == "answer":
                # Last entry is now two from the final entry
                if len(chatlog) > 1:
                    last_entry = chatlog[-2]
        if chatbackup.who == "filler" or chatbackup.who == "answer":
            return
        if last_entry != None and last_entry.who == chatbackup.who and last_entry.what == chatbackup.what:
            # Means the last entry successfully made it to the chat log
            return
        else:
            # User may have paused somewhere in there and the program skipped a
            # dialogue bubble; post it first before posting the current entry
            typeTime = chatbackup.what.count(' ') + 1 # should be the number of words
            # Since average reading speed is 200 wpm or 3.3 wps
            typeTime = typeTime / 3
            if typeTime < 1.5:
                typeTime = 1.5
            typeTime = typeTime * oldPV
            renpy.pause(typeTime)
            
            if chatbackup.img == True:
                if chatbackup.what in emoji_lookup:
                    renpy.play(emoji_lookup[chatbackup.what], channel="voice_sfx")
               
            chatlog.append(Chatentry(chatbackup.who, chatbackup.what, upTime(), chatbackup.img, chatbackup.bounce, chatbackup.specBubble))
            
           
    ##****************************
    ##DECLARE CHARACTERS HERE
    ##****************************
    
    ## Character declarations
    s = Chat("Sev")
    y = Chat("Yoo")
    m = Chat("MC")
    ja = Chat("Ja")
    ju = Chat("Ju")
    z = Chat("Zen")
    r = Chat("Rika")
    ra = Chat("Ray")
    sa = Chat("Sae")
    u = Chat("Unk")
    v = Chat("V")
    msg = Chat("msg")
    
   
    ### Set a variable to infinity, to be used later -- it keeps the viewport scrolling to the bottom
    yadjValue = float("inf")
    ### Create a ui.adjustment object and assign it to a variable so that we can reference it later. 
    # I'll assign it to the yadjustment property of our viewport later.
    yadj = ui.adjustment()
    
    # This is mostly changed automatically for you when you call
    # chat_begin("night") etc, but if you want to change it on an
    # individual basis this is the colour of the characters' nicknames
    nickColour = "#000000"   


screen messenger_screen:

    tag menu

    python:
        if yadj.value == yadj.range:
            yadj.value = yadjValue
        elif yadj.value == 0:
            yadj.value = yadjValue
            
        if len(chatlog) > 0:
            finalchat = chatlog[-1]
            if finalchat.who == "filler":
                yadj.value = yadjValue
        if len(chatlog) < 3:
            yadj.value = yadjValue
        yinitial = yadjValue
            
            
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
            if finalchat.who == "answer":
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
            
        if i.who == "MC":
            nameStyle = 'chat_name_MC'
            include_new = False
        else:
            nameStyle = 'chat_name'
            
        if i.specBubble != None:
            include_new = False
            bubbleBackground = "Bubble/Special/" + i.who + "_" + i.specBubble + ".png"    
        elif i.bounce: # Not a special bubble; just glow
            include_new = False
            bubbleBackground = "Bubble/" + i.who + "-Glow.png"
        elif i.who != 'answer':
            bubbleBackground = "Bubble/" + i.who + "-Bubble.png"
        
        
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
    
    if i.who == 'msg' or i.who == 'filler':
        window:
            style i.who + '_bubble'
            text i.what style i.who + '_bubble_text'
            
    elif i.who != 'answer' and i.who != 'pause':
        window:
            if i.who == 'MC':
                style 'MC_profpic'
            else:
                style 'profpic'
                
            add chatportrait[i.who]
            
        text chatnick[i.who] style nameStyle color nickColour
        
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
            
        if i.who == 'MC':
            include_new = False
            
        if i.bounce:
            bubbleBackground = "Bubble/" + i.who + "-Glow.png"
            include_new = False
        else:
            bubbleBackground = "Bubble/" + i.who + "-Bubble.png"
            
        if i.specBubble != None:
            if i.specBubble[:6] == "round2":
                bubbleStyle = "round_" + i.specBubble[-1:]
            elif i.specBubble[:7] == "square2":
                bubbleStyle = "square_" + i.specBubble[-1:]
            else:
                bubbleStyle = i.specBubble
                
        if i.specBubble != None:
            include_new = False
            bubbleBackground = "Bubble/Special/" + i.who + "_" + i.specBubble + ".png"
            
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

            
            

            
