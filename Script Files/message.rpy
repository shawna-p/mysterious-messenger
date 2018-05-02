
init python:

    ## This is the object that each chat is stored in
    ##  Who = the speaker, What = the text they're saying, thetime is a currently
    ##  unused variable that keeps track of the current time in case you wanted
    ##  to post that to the screen, 'bounce' indicates whether the message is
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
            
        def __call__(self, what, pauseVal=None, img=False, bounce=False, specBubble=None, **kwargs):
            addchat(self.who, what, pauseVal=pauseVal, img=img, bounce=bounce, specBubble=specBubble)
            
           
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
    
    chatlog = []
    # Currently these are unused
    chatArchive = {}    # this will be a dictionary
                        # that stores an entire chatroom per index
                        # The idea is to store chats in this dictionary with the key as the day,
                        # and then the value is a list of chatlog lists
                       
    ## You can declare characters here and their profile pictures
    ## As of now, you can either change profile pictures here or by updating
    ## the variable (see the example when MC is changed in script.rpy)
    ## Each entry is of the style:
    ## "Short Form": "address of profile photo"
    chatportrait = {'Ju': 'Profile Pics/Jumin/ju-default.png', 
                    'Zen': 'Profile Pics/Zen/zen-default.png', 
                    'Sev': 'Profile Pics/Seven/sev-default.png', 
                    'Yoo' : 'Profile Pics/Yoosung/yoo-default.png',                     
                    'Ja': 'Profile Pics/Jaehee/ja-default.png',                    
                    'V' : 'Profile Pics/V/V-default.png',
                    'MC' : 'Profile Pics/MC/MC-1.png', 
                    'Ray' : 'Profile Pics/Ray/ray-default.png',
                    'Rika' : 'Profile Pics/Rika/rika-default.png',
                    
                    'Unk' : 'Profile Pics/Unknown/Unknown-1.png',
                    'Sae' : 'Profile Pics/Saeran/sae-1.png'
                    } 

    ## This is where you store character nicknames so you don't
    ##  have to type out their full name every time
    ##  Somewhat moot as I've declared variables to hold the name of
    ##  their nickname elsewhere, but it's still useful
    ## Format:
    ## "Nickname/Short Form": "Full Name as it should appear in the chat"
    chatnick = {'Sev': '707', 
                'Zen': 'ZEN', 
                'Ja' : 'Jaehee Kang', 
                'Ju' : 'Jumin Han', 
                'Yoo' : 'Yoosung★', 
                'MC' : 'MC♥',     # This is the default name and is replaced when the user enters a custom one
                'Rika' : 'Rika',
                'V' : 'V',
                'Sae' : 'Saeran',
                'Unk' : 'Unknown',
                "msg" : "msg", 
                "filler" : "filler",
                'Ray' : 'Ray'
                } 
                
    ## The characters' status as it shows up on their profile page
    chatstatus = {'Sev': "707's status", 
                'Zen': "Zen's status", 
                'Ja' : "Jaehee's status", 
                'Ju' : "Jumin's status", 
                'Yoo' : "Yoosung's status",
                'Rika' : "Rika's status",
                'V' : "V's status",
                'Sae' : "Saeran's status",
                'Unk' : "Unknown's status",
                'Ray' : "Ray's status"} 
                
    ## The characters' cover photos as it shows up on their profile page
    chatcover = {'Sev': "Cover Photos/profile_cover_photo.png", 
                'Zen': "Cover Photos/profile_cover_photo.png", 
                'Ja' : "Cover Photos/profile_cover_photo.png", 
                'Ju' : "Cover Photos/profile_cover_photo.png", 
                'Yoo' : "Cover Photos/profile_cover_photo.png", 
                'Rika' : "Cover Photos/profile_cover_photo.png", 
                'V' : "Cover Photos/profile_cover_photo.png", 
                'Sae' : "Cover Photos/profile_cover_photo.png", 
                'Unk' : "Cover Photos/profile_cover_photo.png", 
                'Ray' : "Cover Photos/profile_cover_photo.png"} 
                
    ### Set a variable to infinity, to be used later -- it keeps the viewport scrolling to the bottom
    yadjValue = float("inf")
    ### Create a ui.adjustment object and assign it to a variable so that we can reference it later. 
    # I'll assign it to the yadjustment property of our viewport later.
    yadj = ui.adjustment()
    
    # This is mostly changed automatically for you when you call
    # chat_begin("night") etc, but if you want to change it on an
    # individual basis this is the colour of the characters' nicknames
    nickColour = "#000000"   


default new_msg_clicked = False

screen messenger_screen:

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

            
            

            
