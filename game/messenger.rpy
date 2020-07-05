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
        finalchat = None
        if len(chatlog) > 0:
            finalchat = chatlog[-1]
            

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
            for i index id(i) in chatlog[-bubbles_to_keep:]:
                fixed:
                    yfit True
                    xfill True
                    if i.who.name == 'msg' or i.who.name == 'filler':
                        use special_msg(i)
                    # This trick means that the program displays
                    # an invisible bubble behind the visible one
                    # so the animation doesn't "slide" in
                    elif i == finalchat:
                        use chat_animation(i, True)
                    if i.who.name != 'msg' and i.who.name != 'filler':
                        use chat_animation(i)                    
                null height 10
                        
## This displays the special messages like "xyz
## has entered the chatroom"
screen special_msg(i):
    
    frame:
        style i.who.name + '_bubble'            
        text i.what:
            style i.who.name + '_bubble_text'
            if (i.who.name == 'msg' and persistent.dialogue_outlines):
                outlines [ (1, "#000a", absolute(0), absolute(0))]
                font gui.sans_serif_1b

        alt i.alt_text(False)

## This screen does the heavy lifting for displaying
## all the messages, names, profile pictures, etc
screen chat_animation(i, anti=False):

    frame:        
        style i.pfp_style
        if not anti:
            add i.who.get_pfp(110)

    # Add their nickname
    frame:
        ysize 40 xmaximum 435
        background None padding (0,0)
        style i.name_frame_style
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
    if not i.has_new: # Not a "regular" dialogue bubble
        # Not an image; check if it's a special bubble        
        if i.specBubble != None and i.specBubble != 'glow2':
            fixed at i.msg_animation(anti):
                offset i.spec_bubble_offset
                fit_first True
                add i.bubble_bg
                frame:                                    
                    style i.bubble_style
                    yfill True xfill True
                    text i.what style 'special_bubble' alt i.alt_text(anti)
        # Check if it's an image
        elif i.img:
            frame at i.msg_animation(anti):
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
                

        # Not img or special bubble; check if glow variant
        elif i.bounce:
            frame at i.msg_animation(anti):
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
            frame at i.msg_animation(anti):
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
        frame at i.msg_animation(anti):
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
                                

   

                                
                            

        
                
     
            