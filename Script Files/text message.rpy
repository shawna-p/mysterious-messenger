init python:

    from random import randint

    ## This code is adapted from saguaro's email message system with contributions from
    ## xavimat, found at http://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=19295 and
    ## is used under the CC0 1.0 Universal license
    
    import renpy.store as store
    
    reply_screen = False
    draft_screen = False

    # The Text_Message class keeps track of a text message conversation for each character.
    # The actual messages are stored in msg_list
    class Text_Message(store.object):
        def __init__(self, sender, msg_list, reply_label=False, delay=True, read=False, heart=False):
            self.sender = sender
            self.msg_list = msg_list
            self.reply_label = reply_label
            self.delay = delay
            self.read = read
            self.heart = False
            self.heart_person = sender
    
        def deliver(self, instant=False):
            global text_messages
            # Move messages to 'inbox'
            for msg in text_messages:
                if msg.sender == self.sender:
                    if self.msg_list:
                        if instant or not renpy.get_screen('text_message_screen'):
                            msg.msg_list.extend(self.msg_list) 
                            # Clear the queued message; it's been delivered
                            self.msg_list = []
                            # Move the delivered message to the top of the list (newest)
                            text_messages.remove(msg)
                            text_messages.insert(0, msg)
                            if msg.msg_list[-1].who != m:
                                msg.read = False
                                renpy.restart_interaction()
                                # Notify the player of the delivered message
                                renpy.show_screen('text_msg_popup', the_msg=msg)
                            else:
                                msg.read = True
            
        def mark_read(self):
            self.read = True 
            renpy.restart_interaction()         
            
        # This takes you to the correct message reply label
        # and indicates that the message has been read
        def reply(self):
            global reply_screen
            reply_screen = True
            renpy.call_in_new_context(self.reply_label)                
            reply_screen = False             
            self.reply_label = False
            
        # Lets the program know that the person's response will trigger
        # a heart when they view the next reply
        def heart_point(self, person=False):
            if not person:
                self.heart = True
                self.heart_person = self.sender
            else:
                self.heart = True
                self.heart_person = person

    # Creates a new text message; rarely used
    def add_message(sender, msg_list, reply_label=False, delay=True):
        message = Text_Message(sender, msg_list, reply_label, delay)
        
    # Lets the program know the response will trigger a heart point
    def add_heart(who, person=False):
        for msg in text_messages:
            if msg.sender == who:
                if not person:
                    msg.heart_point()
                else:
                    msg.heart_point(person)
          
    # Returns whether or not the message has been read
    def check(sender):
        for item in text_messages:
            if item.sender == sender:
                if item.read:
                    return True
                else:
                    return False
           
    # Updates the message's reply label
    def add_reply_label(sender, reply_label):
        for item in text_messages:
            if item.sender == sender:
                item.reply_label = reply_label
        for item in text_queue:
            if item.sender == sender:
                item.reply_label = reply_label
             
    # Delivers all of the text messages at once
    def deliver_all(): 
        global text_queue
        for msg in text_queue:
            msg.deliver()
                
    # Checks who the sender of the next text message to be delivered is
    def who_deliver():
        global text_queue
        for msg in text_queue:
            if msg.msg_list:
                return msg.sender
        
    # Returns the number of unread messages in text_messages
    def new_message_count():
        unread_messages = [ x for x in text_messages if not x.read and x.msg_list]
        return len(unread_messages)
        
    def num_undelivered():
        undelivered = [ x for x in text_queue if x.msg_list ]
        return len(undelivered)
        
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
                    msg.deliver(True)
                    msg.reply_label = False
                    renpy.restart_interaction

  
default current_message = None
    
########################################################               
## This is the text message hub, where you can click
## on any of your ongoing text conversations
########################################################
screen text_message_hub:

    tag menu
    
    use starry_night
    
    use menu_header('Text Message', Show('chat_home', Dissolve(0.5)))
            
    fixed:
        viewport:
            xsize 725
            ysize 1150
            draggable True
            mousewheel True

            xalign 0.5
            yalign 0.95
            
            vbox:
                spacing 10

                for i in text_messages:
                    if i.msg_list != []:    # if it's not empty
                        $ text_log = i.msg_list
                        $ last_text = text_log[len(text_log) - 1]
                        $ text_time = last_text.thetime

                        if i.read:
                            button:                                                       
                                background 'message_idle_bkgr'
                                hover_background 'message_hover_bkgr'   
                                action [SetVariable("current_message", i), i.mark_read,
                                        SetVariable("CG_who", i), Show('text_message_screen', the_msg=i)]
                                activate_sound 'sfx/UI/email_next_arrow.mp3'
                                
                                ysize 150
                                xsize 725

                                hbox:
                                    align (0.5, 0.5)
                                    spacing 10                                
                                    window:
                                        xysize (135, 135)
                                        align (0.0, 0.5)
                                        add last_text.who.prof_pic align(0.5,0.5) at text_zoom
                                    
                                    window:
                                        xysize(320,135)
                                        yalign 0.5
                                        has vbox
                                        align (0.0, 0.5)
                                        text last_text.who.name style "save_slot_text"
                                        spacing 40     
                                        if "{image=" in last_text.what or last_text.img:
                                            text "[last_text.who.name] sent an image." style "save_slot_text"
                                        else:
                                            text last_text.what[:16] + '...' style "save_slot_text"
                                        
                                    window:
                                        xmaximum 230
                                        has vbox
                                        align (0.5, 0.5)
                                        spacing 30
                                        text text_time.day + '/' + text_time.month_num + '/' + text_time.year + ' ' + text_time.twelve_hour + ':' + text_time.minute + text_time.am_pm style "save_timestamp"
                                        add 'read_text_envelope' xalign 1.0
                                        
                                            
                        else:
                            button:                                                       
                                background 'unread_message_idle_bkgr'
                                hover_background 'unread_message_hover_bkgr' 
                                action [SetVariable("current_message", i), i.mark_read, 
                                        SetVariable("CG_who", i), Show('text_message_screen', the_msg=i)]
                                activate_sound 'sfx/UI/email_next_arrow.mp3'
                                
                                ysize 150
                                xsize 725

                                hbox:
                                    align (0.5, 0.5)
                                    spacing 10                                
                                    window:
                                        xysize(135,135)
                                        align (0.0, 0.5)
                                        add last_text.who.prof_pic yalign 0.5 xalign 0.5 at text_zoom
                                    
                                    window:
                                        xysize (320, 135)
                                        yalign 0.5
                                        has vbox
                                        align (0.0, 0.5)
                                        text last_text.who.name style "save_slot_text"
                                        spacing 40      
                                        if "{image=" in last_text.what or last_text.img:
                                            text "[last_text.who.name] sent an image." style "save_slot_text"   
                                        else:
                                            text last_text.what[:16] + '...' style "save_slot_text"
                                        
                                    window:
                                        xmaximum 230
                                        has vbox
                                        align (0.5, 0.5)
                                        spacing 50
                                        text text_time.day + '/' + text_time.month_num + '/' + text_time.year + ' ' + text_time.twelve_hour + ':' + text_time.minute + text_time.am_pm style "save_timestamp"                                   
                                        
                                        hbox:
                                            spacing 10
                                            xalign 1.0
                                            add 'new_text'
                                            add 'new_text_envelope'
                                            
########################################################               
## This screen takes care of the popups that notify
## the user when there is a new text message   
########################################################            
screen text_msg_popup(the_msg):

    #modal True
    zorder 100
    default current_message = None
    

    if len(the_msg.msg_list) > 0:
        $ last_msg = the_msg.msg_list[-1]
    else:
        $ last_msg = False
    
    window:
        maximum(621,373)
        background 'text_popup_bkgr'
        xalign 0.5
        yalign 0.4
        imagebutton:
            align (1.0, 0.22)
            idle 'input_close'
            hover 'input_close_hover'
            if randint(0,1):
                action [Hide('text_msg_popup'), deliver_next]
            else:
                action Hide('text_msg_popup')
            
        hbox:
            yalign 0.05
            xalign 0.03
            spacing 15
            add 'new_text_envelope'
            text 'NEW' color '#73f1cf' yalign 1.0 font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Bold.ttf"
        
        vbox:
            xalign 0.3
            yalign 0.85
            spacing 20
            hbox:
                spacing 20                
                add the_msg.sender.prof_pic
                
                vbox:
                    spacing 10
                    text "From: " + the_msg.sender.name color '#fff'
                    
                    window:
                        maximum(420,130)
                        background 'text_popup_msg'       
                        if last_msg and ("{image=" in last_msg.what or last_msg.img):
                            text "[last_msg.who.name] sent an image." size 30 xalign 0.5 yalign 0.5 text_align 0.5 
                        elif last_msg and len(last_msg.what) > 48:
                            text last_msg.what[:48] + '...' size 30 xalign 0.5 yalign 0.5 text_align 0.5
                        elif last_msg:
                            text last_msg.what[:48] size 30 xalign 0.5 yalign 0.5 text_align 0.5
                        
            textbutton _('Go to'):
                text_style 'mode_select'
                xalign 0.5
                xsize 220
                ysize 70
                text_size 28
                background 'menu_select_btn' padding(20,20)
                hover_background 'menu_select_btn_hover'
                action [Hide('text_msg_popup'), SetVariable("current_message", the_msg), 
                        the_msg.mark_read, SetVariable("CG_who", the_msg), 
                        Show('text_message_screen', the_msg=the_msg)]
                
    timer 3.25:
        if randint(0,1):
            action [Hide('text_msg_popup', Dissolve(0.25)), deliver_next]
        else:
            action Hide('text_msg_popup', Dissolve(0.25))
        
########################################################  
## Includes the 'answer' button at the bottom
########################################################
screen text_message_footer(the_msg):       
    
    vbox:
        yalign 0.98
        xalign 0.5
        window:
            ymaximum 40
            background 'text_msg_line'
        button:
            xsize 468
            ysize 95
            xalign 0.5
            if the_msg and the_msg.reply_label:
                background 'text_answer_active'
                hover_background 'text_answer_animation'  
                if not renpy.get_screen("choice"):
                    action the_msg.reply
                    activate_sound "sfx/UI/answer_screen.mp3"
            else:
                background 'text_answer_inactive'
            add 'text_answer_text' xalign 0.5 yalign 0.5
            
screen text_date_separator(text_time):

    $ the_time = '20' + text_time.year + '.' + text_time.month_num + '.'
    $ the_time = the_time + text_time.day + ' ' + text_time.weekday
    
    hbox:
        spacing 10
        xalign 0.5
        ysize 80
        xsize 750
        window:
            ymaximum 40
            xsize 240
            yalign 0.5
            background 'text_msg_line'
        text the_time size 25 color '#fff' yalign 0.5
        window:
            ymaximum 40
            yalign 0.5
            xsize 240
            background 'text_msg_line'
        
########################################################
## This is the screen that actually displays the
## message, though it mostly borrows from the chatroom
## display screen
########################################################
screen text_message_screen(the_msg):

    tag menu
    
    default HeartChar = the_msg.heart_person
    
    ## This looks a bit complicated, but it's just code to say "if this text message is
    ## supposed to trigger a heart icon, display the correctly-coloured heart, award
    ## a heart point, and increase the appropriate totals"
    on 'show':
        if the_msg.heart and len(the_msg.msg_list) > 0 and the_msg.msg_list[-1].who != m and HeartChar != r:
            action [SetVariable('heartColor', HeartChar.heart_color),
                    SetField(HeartChar, 'heart_points', HeartChar.heart_points+1),
                    SetField(persistent, 'HP', persistent.HP+1),
                    Show('heart_icon_screen', character=HeartChar), 
                    SetField(the_msg, 'heart', False)]
        elif the_msg.heart and len(the_msg.msg_list) > 0 and the_msg.msg_list[-1].who != m:
            action [SetVariable('heartColor', sa.heart_color),
                    SetField(sa, 'heart_points', sa.heart_points+1),
                    SetField(persistent, 'HP', persistent.HP+1),
                    Show('heart_icon_screen', character=sa), 
                    SetField(the_msg, 'heart', False)]
    on 'replace':
        if the_msg.heart and len(the_msg.msg_list) > 0 and the_msg.msg_list[-1].who != m and HeartChar != r:
            action [SetVariable('heartColor', HeartChar.heart_color),
                    SetField(HeartChar, 'heart_points', HeartChar.heart_points+1),
                    SetField(persistent, 'HP', persistent.HP+1),
                    Show('heart_icon_screen', character=HeartChar), 
                    SetField(the_msg, 'heart', False)]
        elif the_msg.heart and len(the_msg.msg_list) > 0 and the_msg.msg_list[-1].who != m:
            action [SetVariable('heartColor', sa.heart_color),
                    SetField(sa, 'heart_points', sa.heart_points+1),
                    SetField(persistent, 'HP', persistent.HP+1),
                    Show('heart_icon_screen', character=sa), 
                    SetField(the_msg, 'heart', False)]
        
    use starry_night
    
    use text_message_footer(the_msg)
    
    timer 3.0:
        if who_deliver != the_msg.sender:
            action deliver_next
    
    python:
        if yadj.value == yadj.range:
            yadj.value = yadjValue
        elif yadj.value == 0:
            yadj.value = yadjValue
            
        if len(chatlog) > 0:
            finalchat = chatlog[-1]
            if finalchat.who.name == "filler":
                yadj.value = yadjValue
        if len(chatlog) < 3:
            yadj.value = yadjValue
        yinitial = yadjValue

    use menu_header(the_msg.sender.name, Show('text_message_hub', Dissolve(0.5)), True)
            
    window:
        align (0.5, 0.54)
        xfill True
        ysize 1040

        viewport yadjustment yadj: # viewport id "VP":
            draggable True
            mousewheel True
            ysize 1040
                            
            has vbox:
                spacing -30
                use text_dialogue(the_msg.msg_list)
                                
                            

screen text_dialogue(texts):
 
    python:
        chatLength = len(texts) - 1
        begin = chatLength - 10
        if begin >= 0:
            pass
        else:
            begin = 0
        
        if chatLength > 0:
            finalchat = texts[-1]
            if finalchat.who == "answer":
                if begin > 0:
                    begin -= 1
                
    for index, i in enumerate(texts[begin:]):

        if chatLength > 0 and (index != 0 or begin != 0):
            if i.thetime.day != texts[index + begin - 1].thetime.day:
                use text_date_separator(i.thetime)     
        elif begin == 0 and index == 0:
            use text_date_separator(i.thetime)
                       
        use text_animation(i)


screen text_animation(i):
    python:       
        transformVar = incoming_message
        if i.img == True:
            include_new = False
            if "{image=" in i.what:
                pass
            else:
                transformVar = small_CG
                
        ## This determines how long the line of text is. If it needs to wrap
        ## it, it will pad the bubble out to the appropriate length
        ## Otherwise each bubble would be exactly as wide as it needs to be and no more
        if not i.img:
            t = Text(i.what)
            z = t.size()
            my_width = int(z[0])
            my_height = int(z[1])
        
        text_time = i.thetime.twelve_hour + ':' + i.thetime.minute + ' ' + i.thetime.am_pm
        
        
    ## First, the profile picture, no animation
    
    if i.who != 'answer' and i.who != 'pause':
        window:
            if i.who == m:
                style 'MC_profpic_text'
            else:
                style 'profpic_text'
                
            add i.who.prof_pic
        
        ## Now add the dialogue
             

        fixed:
            if i.who != m:
                style 'text_msg_npc_fixed'
            else:
                style 'text_msg_mc_fixed'
            
            hbox:
                spacing 5 
                if i.who != m:
                    ypos -10
                    
                else:
                    ypos 5    
                    text text_time color "#fff" yalign 1.0 size 23                    
                
                window:# at transformVar:                 
                    ## Check if it's an image
                    if i.img == True:
                        style 'img_text_message'
                        # Check if it's an emoji
                        if "{image=" in i.what:
                            style 'reg_bubble_text'
                            text i.what style "bubble_text"
                        else:   # it's a CG
                            # TODO: Could have a dictionary here that unlocks CGs in a gallery
                            # Would need persistent variables; if i.what in gallery ->
                            # gallery[i.what] = True and then it will be unlocked
                            $ fullsizeCG = i.what
                            imagebutton at small_CG_text:
                                bottom_margin 50
                                focus_mask True
                                idle fullsizeCG
                                if not choosing:
                                    action [SetVariable("fullsizeCG", i.what), Call("viewCG", textmsg=True), Return]
            
                    
                    else:        
                        if i.who != m:
                            style 'reg_bubble_text'
                        else:
                            style 'reg_bubble_MC_text'
                        if my_width > gui.longer_than:
                            text i.what style "bubble_text_long" min_width gui.long_line_min_width color '#fff'
                        else:            
                            text i.what style "bubble_text" color '#fff'
                            
                if i.who != m:
                    if i.img == True and not "{image=" in i.what:
                        text text_time color '#fff' yalign 1.0 size 23 yoffset 40 xoffset 10
                    else:
                        text text_time color "#fff" yalign 1.0 size 23
                                            
        