label example_text:

    call chat_begin("morning")
        
    play music mint_eye loop
    
    r "{=curly}Hi there!{/=curly}"   (bounce=True, specBubble="square2_s")
    r "This chatroom is here to demonstrate how text messages are sent." 
    r "You might have noticed that there's a Story Mode section after this chatroom, right?"   (bounce=True)
    
    call answer
    menu:
        "Does that mean anything specific?":
            m "Does that mean anything specific?"   (pauseVal=0)
            r "It does!" 
            r "Since there's a story mode VN," 
            r "{=sser2b}any incoming phone calls or text message won't be delivered until after the VN.{/=sser2b}" 
        "Yes, and I can't play it until after this chatroom, right?":
            m "Yes, and I can't play it until after this chatroom, right?"   (pauseVal=0)
            r "{=curly}Right! ^^{/=curly}"   (bounce=True, specBubble="round_s")
            r "Any incoming phone calls or text message won't be delivered until after the VN, too." 
            
    r "So even though there are text messages to be delivered after this chatroom," 
    r "{=ser1}{size=+10}you won't see them right away.{/size}{/=ser1}" 
    r "{=ser1}You can set up text messages using an {b}after_{/b} chatroom label.{/=ser1}" 
    r "See the User Guide for more ^^" 
    r "{image=ray happy}"   (img=True)
    r "Anyway, I won't keep you." 
    r "See you soon!" 

    call exit(r)
    
    # Use this to end the chat and return to the main menu
    jump chat_end
    
## This is the label you jump to if the chatroom
## is expired
label example_text_expired:
    call chat_begin('morning')
    play music mint_eye loop
    r "{=curly}Hi there!{/=curly}"   (bounce=True, specBubble="square2_s")
    r "This chatroom is here to demonstrate how text messages are sent." 
    r "But, well, since this chatroom is expired it won't act the same way." 
    r "You'll have already received the text messages and any missed phone calls." 
    r "Even if you buy this chatroom back, you won't receive the calls or messages again." 
    r "But you can often call characters back if not much time has passed since they called!" 
    r "Anyway, you can buy this chatroom back for some alternative information too." 
    r "Talk to you soon!" 
    call exit(r)
    jump chat_end
    
## Put anything you want to have happen after the chatroom ends here, 
## like text messages or (in the future) phone calls
label after_example_text:

    # There are two different versions of texting; this first one
    # is the 'regular' variant. You'll notice they're typed differently
    # as well. You will only ever see one or the other
    if not persistent.instant_texting:
        # Ray's text message
        $ addtext (r, "Here's a test text message, to show you how they work!", r)
        $ addtext (r, "Did you know you can also post photos?", r)
        $ addtext (r, "It will look like this:", r)
        $ addtext (r, "r/cg-1.png", r, True)

        $ add_reply_label(r, 'menu_a1')
                
        # V's text message
        $ addtext (v, "Hello, [name].", v)
        $ addtext (v, "I'm supposed to demonstrate how to make a character post an emoji during a text message.", v)
        $ addtext (v, "{image=v smile}", v, True)
        $ addtext (v, "They won't play audio like they do in the chatrooms,", v)
        $ addtext (v, "But they can still be fun to use in a conversation, don't you think?", v)
        $ add_reply_label(v, 'menu_a2')
        
        # Some extra messages
        #$ addtext (ju, "What do you think about adding Elizabeth the 3rd as a member?", ju)
        #$ addtext (ja, "I hope this ordeal hasn't been too difficult on you.", ja)
        #$ addtext (s, "I miss you!", s)
        #$ addtext (u, "You'll be fine ^^", u)
        $ addtext (z, "You know, you never send us any photos...", z)
        $ add_reply_label(z, 'menu_a3')
        #$ addtext (ri, "Weren't you curious, too?", ri)
    
    else:
        # Ray's instant text message
        call inst_text_begin(r)
        r "Here's a test text message, to show you how they work!"
        r "Did you know you can also post photos?"
        $ r.update_text('menu_a1_inst')
        call inst_text_end
        
        # V's instant text message
        call inst_text_begin(v)
        v "Hello, [name]."
        v "I'm supposed to demonstrate how to make a character post an emoji during a text message."
        v "{image=v smile}" (img=True)
        $ v.update_text('menu_a2_inst')
        call inst_text_end
        
        # Zen's instant text message
        call inst_text_begin(z)
        z "You know, you never send us any photos..."
        $ z.update_text('menu_a3_inst')
        call inst_text_end    
    
    return
    
label menu_a1:

    menu:
        "I'm not sure how I'll remember all this...":
            $ addtext (m, "I'm not sure how I'll remember all this...", r)
            $ addtext (r, "Don't worry! There are lots of resources to help.", r)
            $ addtext (r, "Let's do our best ^^", r)
        
        "That's a nice picture of you!":
            $ addtext (m, "That's a nice picture of you!", r)
            $ add_heart(r)
            $ addtext (r, "{image=ray happy}", r, True)
            $ addtext (r, "Thank you ^^", r)

    jump text_end
    
label menu_a2:

    menu:    
        "Thanks for showing me this.":
            $ addtext (m, "Thanks for showing me this.", v)
            $ add_heart(v)
            $ addtext (v, "You're very welcome!", v)
            $ addtext (v, "Hope to talk to you again soon.", v) 
        
        "I'm not sure if they'll be useful...":
            $ addtext (m, "I'm not sure if they'll be useful...", v)
            $ addtext (v, "It's up to you whether to use them or not.", v)
            $ addtext (v, "I hope you enjoy the rest of the program.", v)
        
    jump text_end
    
label menu_a3:
    menu:
        "(Post a photo)":
            $ addtext (m, "common/cg-2.png", z, True)
            $ addtext (m, "You mean like this?", z)
        "(Post an emoji)":
            $ addtext (m, "{image=zen oyeah}", z, True)
            $ addtext (m, "How's this?", z)
        "(Post both)":
            $ addtext (m, "common/cg-2.png", z, True)
            $ addtext (m, "{image=zen oyeah}", z, True)
            $ addtext (m, "What do you think?", z)
    $ addtext (z, "Wow! I've never seen that before.", z)
    $ addtext (z, "You're pretty cool", z)
    $ addtext (z, "{image=zen wink}", z, True)
    jump text_end
    
## These are the menus for instant text messaging
label menu_a1_inst:
    # You need to pass text_begin the variable of the character
    # whom the MC is texting
    call text_begin(r)
    
    r "It will look like this:"
    r "r/cg-1.png" (img=True)
    
    # You'll notice these are written just like chatrooms
    call answer
    menu:
        "I'm not sure how I'll remember all this...":
            m "I'm not sure how I'll remember all this..." (pauseVal=0)
            r "Don't worry! There are lots of resources to help."
            r "Let's do our best ^^"
        "That's a nice picture of you!":
            m "That's a nice picture of you!" (pauseVal=0)
            r "{image=ray happy}" (img=True)
            call heart_icon(r)
            r "Thank you ^^"
            
    # Instant text messages end the same way as regular ones
    jump text_end

label menu_a2_inst:
    call text_begin(v)
    v "Because this is 'instant text messaging',"
    v "these emojis will have audio, unlike regular texts."
    call answer
    menu:
        "Thanks for showing me this.":
            m "Thanks for showing me this." (pauseVal=0)
            v "You're very welcome!"
            call heart_icon(v)
            v "Hope to talk to you again soon."

        "I'm not sure if they'll be useful...":
            m "I'm not sure if they'll be useful..." (pauseVal=0)
            v "It's up to you whether to use them or not."
            v "I hope you enjoy the rest of the program."
    jump text_end

label menu_a3_inst:
    call text_begin(z)
    call answer
    menu:
        "(Post a photo)":
            m "common/cg-2.png" (pauseVal=0, img=True)
            m "You mean like this?"
        "(Post an emoji)":
            m "{image=zen oyeah}" (pauseVal=0, img=True)
            m "How's this?"
        "(Post both)":
            m "common/cg-2.png" (pauseVal=0, img=True)
            m "{image=zen oyeah}" (img=True)
            m "What do you think?"

    z "Wow! I've never seen that before."
    z "You're pretty cool"
    z "{image=zen wink}" (img=True)
    jump text_end
    