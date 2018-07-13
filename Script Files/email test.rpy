
default rainbow = Email('Rainbow', """Hi [name]!
\nReally excited to hear about this party you're holding! Can't wait to see how things will turn out for you.
Seven told me to make sure your inbox is working, and well, if you're reading this, I guess it is! So that's good.
I did have one quick question though -- will the party be held inside or outside? Please let me know as soon as possible!
\nThanks,
\nRainbow Unicorn""", 'Email/rainbow_unicorn_guest_icon.png', 'rainbow_reply_1')

label email_test:

    call chat_begin('evening')
    $ observing = False
    
    s 'Hey, [name], I had an idea for a guest we should invite.'
    s 'Can we invite zentherainbowunicorn?'
    
    call answer
    menu:
        "That sounds great!":
            m 'That sounds great!' (pauseVal=0)
            call invite(rainbow)
        
        
        "I'll pass":
            m "I'll pass." (pauseVal=0)
            
    call save_exit
            


label rainbow_reply_1:

    menu:
        'Indoor party.':
            $ rainbow.add_msg("""Dear Rainbow,
\nI'm pleased to inform you that the party will be indoors. No need for umbrellas or sunscreen!
Hope to see you there,
\nSincerely,
\n[name], the party coordinator""")
            
            $ rainbow.set_reply("""Hi again,
\nOh, how wonderful! I was worried about what the weather would be like on the day of the party.
I thought of another question: what kind of music will there be at the party?
\nHope to hear from you soon,
\nRainbow Unicorn""")
            
            $ rainbow.reply_label = 'rainbow_reply_2'
            
            $ update_emails(rainbow)
            $ renpy.retain_after_load()
        
        'Outdoor party.':
            $ rainbow.add_msg("""Dear Rainbow,
\nWe're planning for an outdoor party! There are gardens at the venue that will be perfect for an elegant party.
Hope to see you there!
\nSincerely,
\n[name], the party coordinator""")
            
            $ rainbow.set_reply("""Hi again,
\nOh dear, I'm afraid I have terrible allergies and that may not work out well for me. I appreciate the time you've taken to email me but I may have to decline.
\nThank you for the invitation, and best of luck to you and the party.
\nRainbow Unicorn""")
            
            $ rainbow.reply_label = False
            
            $ rainbow.failed = True
            
            $ update_emails(rainbow)
            $ renpy.retain_after_load()
                    
            
    return








