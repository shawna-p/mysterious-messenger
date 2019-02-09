label example_text:

    call chat_begin("morning")
    
    # You'll generally never want to mess with the 'observing' variable yourself, 
    # but since this is a tutorial chatroom we want the user to be able to play
    # it over and over and not be restricted to the choices they've already made
    $ observing = False
    
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

    
# Put anything you want to have happen after the chatroom ends here, 
# like text messages or (in the future) phone calls
label after_example_text:


    ## Ray's text message
    $ addtext (r, "Here's a test text message, to show you how they work!", r)
    $ addtext (r, "Did you know you can also post photos?", r)
    $ addtext (r, "It will look like this:", r)
    $ addtext (r, "r/cg-1.png", r, True)

    $ add_reply_label(r, 'menu_a1')
            
    ## V's text message
    $ addtext (v, "Hello, [name].", v)
    $ addtext (v, "I'm supposed to demonstrate how to make a character post an emoji during a text message.", v)
    $ addtext (v, "{image=v smile}", v, True)
    $ addtext (v, "They won't play audio like they do in the chatrooms,", v)
    $ addtext (v, "But they can still be fun to use in a conversation, don't you think?", v)
    $ add_reply_label(v, 'menu_a2')
    
    ## Some extra messages
    #$ addtext (ju, "What do you think about adding Elizabeth the 3rd as a member?", ju)
    #$ addtext (ja, "I hope this ordeal hasn't been too difficult on you.", ja)
    #$ addtext (s, "I miss you!", s)
    #$ addtext (u, "You'll be fine ^^", u)
    $ addtext (z, "You know, you never send us any photos...", z)
    $ add_reply_label(z, 'menu_a3')
    #$ addtext (ri, "Weren't you curious, too?", ri)
    
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
    