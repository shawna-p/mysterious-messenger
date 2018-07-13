init python:

    
    email_reply = False
    
    class Email(store.object):
        def __init__(self, guest, msg, sender_thumb, reply_label=False, read=False,
                        msg_num=0, failed=False, timeout_count=25, deliver_reply=False,
                        reply=False, timeout=False):
            self.guest = guest # Guest's name
            self.msg = msg  # Email content
            self.sender_thumb = sender_thumb    # Sender's contact thumbnail, ideally 155x155
            self.reply_label = reply_label  # Name of the label to jump to when replying
            self.read = read    # Read/Unread
            self.msg_num = msg_num  # = 0, 1, 2, or 3; reply number. 0 is the first message
                                      # sent to you, and 3 is the email accepting your invite
            self.failed = failed    # Whether or not the email chain has been failed
            self.timeout_count = timeout_count  # This is somewhat arbitrary; essentially if the
                                    # player doesn't respond within 25 chatrooms (~3 days; can
                                    # be changed) of receiving the message it will be failed
            self.deliver_reply = deliver_reply   # How long to wait before the guest replies to your email
                                            # This should be False if it's your turn to reply
            self.reply = reply   # This contains the message to be delivered when the guest replies to you
            self.timeout = timeout
            self.sent_time = upTime()
                                   
        def deliver(self):
            if self.deliver_reply:
                self.deliver_reply -= 1
                
            if self.deliver_reply and self.deliver_reply <= 0 and self.reply:
                self.read = False
                #self.msg_num += 1
                self.reply += "\n\n------------------------------------------------\n\n"
                self.msg = self.reply + self.msg
                self.reply = False
                
        def set_reply(self, reply, deliver_reply=False):
            self.reply = reply
            # If a number is given, the reply will be delivered within that many
            # chatrooms. Otherwise, it will be delivered within the next 5-16 chatrooms
            if deliver_reply:
                self.deliver_reply = deliver_reply
            else:
                self.deliver_reply = renpy.random.randint(5, 16)
                
        def add_msg(self, msg):
            self.msg_num += 1
            msg += "\n\n------------------------------------------------\n\n"
            self.msg = msg + self.msg
            
                
        def completed(self):
            if self.failed or not self.read:
                return False            
            if self.msg_num == 3:
                return True
            else:
                return False
                
        def is_failed(self):
            if self.failed and self.read and not self.reply:
                return True
            else:
                return False
                
        def first_msg(self):
            if self.msg_num <= 0:
                return 'email_inactive'
            elif self.msg_num == 1 and self.failed:
                return 'email_bad'
            else:
                return 'email_good'
        
        def second_msg(self):
            if self.msg_num <= 1:
                return 'email_inactive'
            elif self.msg_num == 2 and self.failed:
                return 'email_bad'
            else:
                return 'email_good'
        
        def third_msg(self):
            if self.msg_num <= 2:
                return 'email_inactive'
            elif self.msg_num == 3 and self.failed:
                return 'email_bad'
            else:
                return 'email_good'
                
        def send_reply(self):
            global email_reply
            email_reply = True
            renpy.call_in_new_context(self.reply_label)
            email_reply = False
            self.reply_label = False
                
            
    def update_emails(guest):
        for e in email_list:
            if e == guest:
                e.msg = guest.msg
                e.reply = guest.reply
                e.reply_label = guest.reply_label
                e.failed = guest.failed
                e.deliver_reply = guest.deliver_reply
                break
                
    def deliver_emails():
        global email_list
        for e in email_list:
            e.deliver()
                
                
default email_list = [Email('Example', """To the party coordinator, [name]:
    \nI was told to email you about an upcoming party. What I would like to know is if there will be any food at the party, and if so, what kind? This is a very important matter to me. Thank you.
    \nSincerely,
    \nExample Guest""", "Email/guest_unlock_icon.png", 'example_email_reply1'),
    Email('neuropsychiatry', 'Message', "Email/guest_unlock_icon.png"),
    Email('darkdragon', 'Message 2', "Email/guest_unlock_icon.png", False, True, 1),
    Email('bpmonster', 'Message 2', "Email/guest_unlock_icon.png", 'test', True, 2),
    Email('chickendelivery', 'Message 2', "Email/guest_unlock_icon.png", False, True, 1, True),
    Email('costume', 'Message 2', "Email/guest_unlock_icon.png", False, False, 3, True),
    Email('udon', 'Message 2', "Email/guest_unlock_icon.png", False, True, 2),
    Email('vampire', 'Message 2', "Email/guest_unlock_icon.png", False, True, 1)]
            
# The idea here is that if the user picks the option to invite
# this guest, you'll include a line `call invite(guest_name)` and
# it will trigger them to email you
label invite(guest):
    #if not observing:
    $ guest.sent_time = upTime()
    $ email_list.insert(0, guest) # Moves them to the front of the list
    return
    
    
default example_email = Email('Example', """To the party coordinator, [name]:
    \nI was told to email you about an upcoming party. What I would like to know is if there will be any food at the party, and if so, what kind? This is a very important matter to me. Thank you.
    \nSincerely,
    \nExample Guest""", "Email/guest_unlock_icon.png", 'example_email_reply1')
    
default current_email = None  

screen email_hub:
    
    tag menu
        
    default current_page = 0
    default num_pages = (len(email_list) + 7 - 1) // 7
    
    use starry_night
    
    use menu_header('Email', Show('chat_home', Dissolve(0.5)))
    
    window:
        background 'left_corner_menu' padding(20,20)
        xysize (685, 1100)
        align (0.5, 0.75)
        has vbox
        spacing 40
        align (0.5, 0.0)
        null height -15
        
        if len(email_list) == 0:
            text "Inbox is empty" color '#fff' xalign 0.5 yalign 0.0
        for e in email_list[current_page*7:current_page*7+7]:      
            use email_button(e)
                
        
    hbox:
        align (0.5, 0.99)
        spacing 15
        imagebutton:
            idle im.Flip("Email/main03_email_next_button.png", horizontal=True)
            align (0.5, 0.5)
            if current_page > 0:
                action SetScreenVariable('current_page', current_page-1)     
            
        for index in range(num_pages):
            textbutton _(str(index+1)):
                text_color '#fff' 
                align (0.5, 0.5)
                action SetScreenVariable('current_page', index)
            
        imagebutton:
            idle "Email/main03_email_next_button.png"
            align (0.5, 0.5)
            if current_page < num_pages - 1:
                action SetScreenVariable('current_page', current_page+1)
            
            
screen email_button(e):
    button:
        align (0.5, 0.5)
        if e.read:
            background 'email_panel'
        else:
            background 'email_mint'
            
        xysize (644, 111)
        hover_foreground 'white_transparent'
        action [SetVariable("current_email", e), SetField(e, 'read', True), Show('open_email', e=e)]
          
        hbox:
            align (0.0, 0.0)
            spacing 10
            fixed:
                xysize (80,111)
                align (0.5, 0.5)
                if not e.read:
                    add 'email_unread' align(1.0, 0.5)
                elif e.reply_label:
                    add 'email_read' align(1.0, 0.5)
                else:
                    add 'email_replied' align(1.0, 0.5)
            add Transform(e.sender_thumb, zoom=0.61) align(0.5, 0.3)
            null width -10
            vbox:
                align(0.5, 0.4)
                spacing 15
                window:
                    align(0.0, 0.0)
                    xysize(190, 30)
                    text '@' + e.guest style 'email_address'
                hbox:
                    align(0.3, 0.5)
                    spacing 8
                    add e.first_msg()
                    add e.second_msg()
                    add e.third_msg()
            window:
                xysize(240,111)
                align (0.0, 0.0)
                if e.completed():
                    add 'email_completed' align(0.5, 0.5)
                elif e.is_failed():
                    add 'email_failed' align(0.5, 0.5)
                elif e.timeout:
                    add 'email_timeout' align(0.5, 0.5)
                    
screen open_email(e):
    modal True
    zorder 100
    
    add "Phone UI/choice_dark.png"
        
    window:
        maximum(685, 800)
        background 'left_corner_menu_dark' padding(20,20)
        align (0.5, 0.5)
        imagebutton:
            align (1.0, 0.0)
            xoffset 20
            yoffset -20
            idle 'input_close'
            hover 'input_close_hover'
            action Hide('open_email')
            
        vbox:
            spacing 15
            align (0.0, 0.0)
            hbox:
                spacing 10
                align (0.0, 0.0)
                add e.sender_thumb
                
                vbox:
                    align(0.0, 0.0)
                    spacing 10
                    fixed:
                        align (0.0, 0.0)
                        xsize 280
                        ysize 80
                        text 'From: ' + e.guest color '#fff'
                    text '[[Date] ' + e.sent_time.month_num + '/' + e.sent_time.day color '#fff' size 27
                    text '[[Time] ' + e.sent_time.twelve_hour + ':' + e.sent_time.minute + ' ' + e.sent_time.am_pm size 27 color '#fff'
                
                textbutton _('Reply'):
                    text_style 'mode_select'
                    align (0.5, 1.0)
                    xsize 170
                    ysize 70
                    text_size 28
                    background 'menu_select_btn' padding(20,20)
                    hover_background 'menu_select_btn_hover'
                    if e.reply_label and not e.reply:
                        action e.send_reply
                    else:
                        foreground 'menu_select_btn_inactive'

            window:
                background 'email_open_transparent' padding(20,20)
                xysize (625, 585)
                align (0.5,0.5)
                viewport:
                    align (0.5, 0.5)
                    xysize (585, 545)
                    scrollbars 'vertical'
                    mousewheel True
                    draggable True
                    
                    text e.msg size 28
            
                        
    
    
image email_completed = "Email/main03_email_completed_01.png"
image email_failed = "Email/main03_email_failed.png"
image email_timeout = "Email/main03_email_timeout.png"
image email_good = "Email/main03_email_good.png"
image email_bad = "Email/main03_email_bad.png"
image email_inactive = "Email/main03_email_inactive.png"
image email_panel = "Email/main03_email_panel.png"
image email_read = "Email/main03_email_read.png"
image email_replied = "Email/main03_email_replied.png"
image email_unread = "Email/main03_email_unread.png"
image email_next = "Email/main03_email_next_button.png"
image email_mint = "Email/main03_email_mint.png"
image white_transparent = Frame("Email/white_transparent.png", 0, 0)
image email_open_transparent = Frame("Email/email_open_transparent.png", 0, 0)
image left_corner_menu_dark = Frame("Email/left_corner_menu_dark.png", 45, 45)

style email_address:
    font "00 fonts/NanumBarunpenR.ttf"
    color '#fff'
    size 27



