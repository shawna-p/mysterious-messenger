init python:

    
    email_reply = False
    
    class Email(store.object):
        def __init__(self, sender, msg, sender_img, reply_label=False, read=False,
                        reply_num=1, failed=False):
            self.sender = sender
            self.msg = msg
            self.sender_img = sender_img
            self.reply_label = reply_label
            self.read = read
            self.reply_num = reply_num
            self.failed = failed
