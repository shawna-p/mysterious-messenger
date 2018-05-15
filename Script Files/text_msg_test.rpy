label text_msg_test:

    call chat_begin("morning")  
    
    r "{=sser2}Here's a quick test ^^{/=sser2}"
    r "Bye!"
    msg "Ray has left the chatroom."
    
    #if renpy.seen_label('after_msg_test'):
    #    $ post_chatroom = False
    #else:
    $ post_chatroom = 'after_msg_test'
    
    # Call this to end the chat and return to the main menu
    call save_exit

    
# Put anything you want to have happen after the chatroom ends here, 
# like text messages or (in the future) phone calls
label after_msg_test:

    ## Ray's text message
    $ addtext (r, "Hope this test worked!", r)
    $ addtext (r, "It's been a lot of trouble with all the screens and stuff...", r)
    $ add_reply_label(r, 'menu_a1')
    
    
    ## V's text message
    $ addtext (v, "I came to see how you were doing, [name]", v)
    $ addtext (v, "Since you're new to the organization and everything...", v)
    $ addtext (v, "I'm sure it's been difficult for you", v)
    $ add_reply_label(v, 'menu_a2')
    
    ## Some extra messages
    $ addtext (ju, "What do you think about adding Elizabeth the 3rd as a member?", ju)
    $ addtext (ja, "I hope this ordeal hasn't been too difficult on you.", ja)
    $ addtext (s, "I miss you!", s)
    $ addtext (u, "You'll be fine ^^", u)
    $ addtext (z, "I took a selfie this morning", z)
    $ addtext (ri, "Weren't you curious, too?", ri)
    $ addtext (sa, "You're mine", sa)
    
    return
    
label menu_a1(current_message):


    menu:
        "It's definitely been a lot of trouble":
            $ addtext (m, "It's definitely been a lot of trouble", r)
            $ addtext (r, "I know! But we'll fix it.", r)
            $ addtext (r, "Let's cross our fingers ^^", r)
        
        "I'm just optimistic it'll work out!":
            $ addtext (m, "I'm just optimistic it'll work out!", r)
            $ add_heart(current_message)
            $ addtext (r, "Wow!! So optimistic ^^", r)
            $ addtext (r, "I'm sure it'll work out in the end", r)

    $ renpy.retain_after_load()
    return
    
label menu_a2(current_message):

    menu:
    
        "Not difficult at all!":
            $ addtext (m, "Not difficult at all!", v)
            $ add_heart(current_message)
            $ addtext (v, "I'm happy to hear that", v)
            $ addtext (v, "We're all very grateful to be planning parties again.", v) 
        
        "Thanks for checking on me":
            $ addtext (m, "Thanks for checking on me", v)
            $ addtext (v, "Of course", v)
            $ addtext (v, "Let me know if you need anything", v)
        
    $ renpy.retain_after_load()
    return
    
    
    
    