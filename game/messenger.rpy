## This is set of screens which handles displaying the
## messages in the chatlog to the screen
screen messenger_screen():

    tag menu

    python:
        # This is the infinite value from earlier which
        # tells the viewport to always scroll to
        # the bottom
        yadj.value = yadjValue 
        # Set up how many messages the player can scroll back and see
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

    frame:
        align (0.5, 1.0)
        yoffset -114
        xfill True
        ysize 1080

        viewport: # viewport id "VP":
            yadjustment yadj
            draggable True
            mousewheel True
            ysize 1080
                            
            has vbox:
                spacing 10
                for i index id(i) in chatlog[begin:]:
                    fixed:
                        yfit True
                        xfit True
                        # This trick means that the program displays
                        # an invisible bubble behind the visible one
                        # so the animation doesn't "slide" in
                        if i == finalchat:
                            use chat_animation(i, True, True)
                        use chat_animation(i, False)
                    null height 10
                        

## This screen does the heavy lifting for displaying
## all the messages, names, profile pictures, etc
screen chat_animation(i, animate=True, anti=False):

    python:
        # These python statements tell the program how to display
        # the given message

        # Include the 'NEW' sign?
        include_new = False

        # If this message bounces, use the bounce transformation
        if i.bounce:
            transformVar = incoming_message_bounce
            include_new = False
        else:
            transformVar = incoming_message
            include_new = True
            
        # If someone is on the right side of the messenger,
        # they require different styles
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
            # according to the given special bubble
            if i.specBubble != None and i.specBubble != 'glow2':
                include_new = False
                bubbleBackground = ("Bubble/Special/" 
                                        + i.who.file_id + "_" 
                                        + i.specBubble + ".png")  
            # Otherwise there's a special case with the 'glow2' bubble
            # which is another glow variant
            elif i.specBubble != None and i.specBubble == 'glow2':
                include_new = False
                bubbleBackground = Frame("Bubble/Special/" + i.who.file_id 
                                    + "_" + i.specBubble + ".png", 25, 25)

            elif i.bounce: # Not a special bubble; just glow
                include_new = False
                bubbleBackground = i.who.glow_bubble_img
            elif i.who != answer: # Regular speech bubble
                bubbleBackground = i.who.reg_bubble_img
            
            if i.specBubble != None:
                # Some characters have more than one round or square bubble
                # but they follow the same style as "round" or "square"
                if i.specBubble[:6] == "round2":
                    # Fetch the size of the bubble (e.g. s/m/l)
                    bubbleStyle = "round_" + i.specBubble[-1:]
                elif i.specBubble[:7] == "square2":
                    bubbleStyle = "square_" + i.specBubble[-1:]
                elif i.specBubble == "glow2":
                    bubbleStyle = 'glow_bubble'
                else:
                    bubbleStyle = i.specBubble
            
            # If it's a CG, no new sign
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

        # If this is cancelling out the animation, 
        # give it the correct counter-animation
        if anti and i.bounce:
            transformVar = invisible_bounce
        elif anti:
            transformVar = invisible

        ## Determining the text for self-voicing
        if anti:
            alt_text = ""
            alt_who = ""
        elif i.img:
            alt_who = ""
            alt_text = i.who.p_name + " sent a photo"
        else:
            alt_who = i.who.p_name
            alt_text = renpy.filter_text_tags(i.what, 
                                    allow=gui.history_allow_tags)
        


    # This displays the special messages like "xyz
    # has entered the chatroom"
    if (i.who.name == 'msg' or i.who.name == 'filler') and not anti:
        frame:
            style i.who.name + '_bubble'            
            text i.what style i.who.name + '_bubble_text'
            alt alt_text
            

    # Otherwise it's a regular character; add
    # their profile picture
    elif i.who.file_id and i.who.file_id != 'delete':
        frame:
            xysize (110, 110)
            style picStyle
            if not anti:
                add i.who.get_pfp(110)

        # Add their nickname
        if not anti:
            text i.who.name style nameStyle color nickColour alt alt_who
        else:
            text i.who.name at invisible alt alt_who
        # Now add the dialogue
        if not include_new: # Not a "regular" dialogue bubble
            frame at transformVar:
                # Check if it's an image
                if i.img:
                    style imgStyle
                    if "{image" in i.what:
                        text i.what alt alt_text
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
                            alt alt_text

                # Not an image; check if it's a special bubble
                elif i.specBubble != None and i.specBubble != 'glow2':
                    style bubbleStyle
                    background bubbleBackground # e.g. 'sigh_m'
                    text i.what style 'special_bubble' alt alt_text

                # Not img or special bubble; check if glow variant
                elif i.bounce:
                    # Note: MC has no glowing bubble so there is
                    # no variant for them
                    style 'glow_bubble'
                    background bubbleBackground
                    # This checks if the text needs to wrap or not
                    if my_width > gui.longer_than:
                        text i.what:
                            style 'bubble_text_long' 
                            min_width gui.long_line_min_width
                    else:            
                        text i.what style 'bubble_text'
                    alt alt_text

                # Otherwise it must be regular MC dialogue
                else:
                    style reg_style
                    background bubbleBackground
                    if my_width > gui.longer_than:
                        text i.what:
                            style 'bubble_text_long'
                            min_width gui.long_line_min_width
                    else:            
                        text i.what style "bubble_text"
                    alt alt_text

        # This does indeed need the 'NEW' sign
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
                        text i.what:
                            if my_width > gui.longer_than:
                                style 'bubble_text_long'
                                min_width gui.long_line_min_width
                            else:
                                style 'bubble_text'
                        alt alt_text
                                

   

                                
                            

        
                
     
            