## This is set of screens which handles displaying the
## messages in the chatlog to the screen
screen messenger_screen():

    tag menu
    zorder 1
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
            xfill True
                            
            has vbox
            spacing 10
            xfill True
            for i index id(i) in chatlog[begin:]:
                fixed:
                    yfit True
                    xfit True
                    # This trick means that the program displays
                    # an invisible bubble behind the visible one
                    # so the animation doesn't "slide" in
                    if i == finalchat:
                        use chat_animation(i, True, True)
                        use chat_animation(i, True)
                    else:
                        use chat_animation(i, False)
                null height 10
                        

## This screen does the heavy lifting for displaying
## all the messages, names, profile pictures, etc
screen chat_animation(i, animate=True, anti=False):


    # This displays the special messages like "xyz
    # has entered the chatroom"
    if (i.who.name == 'msg' or i.who.name == 'filler') and not anti:
        frame:
            style i.who.name + '_bubble'            
            text i.what:
                style i.who.name + '_bubble_text'
                if (i.who.name == 'msg' and persistent.dialogue_outlines):
                    outlines [ (1, "#000a", absolute(0), absolute(0))]
                    font gui.sans_serif_1b

            alt i.alt_text(anti)
            

    # Otherwise it's a regular character; add
    # their profile picture
    elif i.who.file_id and i.who.file_id != 'delete':
        frame:
            xysize (110, 110)
            style i.pfp_style
            if not anti:
                add i.who.get_pfp(110)

        # Add their nickname
        if not anti:
            text i.who.name style i.name_style:
                color nickColour
                alt i.alt_who(anti)
                if persistent.dialogue_outlines:
                    if nickColour == black:
                        outlines [ (1, "#fffa", 
                                absolute(0), absolute(0)) ]
                    else:
                        outlines [ (1, "#000a",
                                absolute(0), absolute(0))]
                    font gui.sans_serif_1b
        else:
            text i.who.name at invisible alt i.alt_who(anti)
        # Now add the dialogue
        if not i.has_new(animate): # Not a "regular" dialogue bubble
            frame at i.msg_animation(animate, anti):
                # Check if it's an image
                if i.img:
                    style i.img_style
                    if "{image" in i.what:
                        text i.what alt i.alt_text(anti)
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
                            alt i.alt_text(anti)

                # Not an image; check if it's a special bubble
                elif i.specBubble != None and i.specBubble != 'glow2':
                    style i.bubble_style
                    background i.bubble_bg # e.g. 'sigh_m'
                    text i.what style 'special_bubble' alt i.alt_text(anti)

                # Not img or special bubble; check if glow variant
                elif i.bounce:
                    # Note: MC has no glowing bubble so there is
                    # no variant for them
                    style 'glow_bubble'
                    background i.bubble_bg
                    # This checks if the text needs to wrap or not
                    if i.dialogue_width > gui.longer_than:
                        text i.what:
                            style 'bubble_text_long' 
                            min_width gui.long_line_min_width
                    else:            
                        text i.what style 'bubble_text'
                    alt i.alt_text(anti)

                # Otherwise it must be regular MC dialogue
                else:
                    style i.bubble_style
                    background i.bubble_bg
                    if i.dialogue_width > gui.longer_than:
                        text i.what:
                            style 'bubble_text_long'
                            min_width gui.long_line_min_width
                    else:            
                        text i.what style "bubble_text"
                    alt i.alt_text(anti)

        # This does indeed need the 'NEW' sign
        else:
            frame at i.msg_animation(animate, anti):
                pos (138,24)
                xsize 500
                background None
                vbox:
                    spacing -20
                    order_reverse True
                    add 'new_sign' align (1.0, 0.0) xoffset 40 at new_fade
                    frame:
                        padding (25,12,20,12)
                        background i.bubble_bg
                        text i.what:
                            if i.dialogue_width > gui.longer_than:
                                style 'bubble_text_long'
                                min_width gui.long_line_min_width
                            else:
                                style 'bubble_text'
                        alt i.alt_text(anti)
                                

   

                                
                            

        
                
     
            