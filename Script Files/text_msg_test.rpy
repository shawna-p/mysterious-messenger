label example_text:

    call chat_begin("morning")  
    
    r "{=sser2}Here's a quick test ^^{/=sser2}"
    r "Bye!"
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
    $ addtext (r, "saeran_cg1", r, True)

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
    #$ addtext (z, "I took a selfie this morning", z)
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
    
    
    
    