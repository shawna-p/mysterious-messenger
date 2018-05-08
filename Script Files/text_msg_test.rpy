label text_msg_test:

    $ chatroom_name = 'Text Message Test'
    $ day_num = '3rd'
    $ route_title = 'deep'

    call chat_begin("morning")
             
    ra "{=sser2}Here's a quick test ^^{/=sser2}"
    ra "Bye!"
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

    #$ show_queue = []

    ## Ray's text message
    $ addtext ("Ray", "Hope this test worked!", "Ray")
    $ addtext ("Ray", "It's been a lot of trouble with all the screens and stuff...", "Ray")
    $ add_reply_label('Ray', 'menu_a1')
    
    
    ## V's text message
    $ addtext ("V", "I came to see how you were doing, [name]", "V")
    $ addtext ("V", "Since you're new to the organization and everything...", "V")
    $ addtext ("V", "I'm sure it's been difficult for you", "V")
    $ add_reply_label('V', 'menu_a2')
    
    #$ new_notifications = True
    #$ show_notifications()
    
    return
    
label menu_a1(current_message):


    menu:
        "It's definitely been a lot of trouble":
            $ addtext ("MC", "It's definitely been a lot of trouble", "Ray")
            $ addtext ("Ray", "I know! But we'll fix it.", "Ray")
            $ addtext ("Ray", "Let's cross our fingers ^^", "Ray")
            #call screen text_message_screen('Ray')
        
        "I'm just optimistic it'll work out!":
            $ addtext ("MC", "I'm just optimistic it'll work out!", "Ray")
            $ add_heart(current_message)
            $ addtext ("Ray", "Wow!! So optimistic ^^", "Ray")
            $ addtext ("Ray", "I'm sure it'll work out in the end", "Ray")

    $ renpy.retain_after_load()
    return
    
label menu_a2(current_message):

    menu:
    
        "Not difficult at all!":
            $ addtext ("MC", "Not difficult at all!", "V")
            $ add_heart(current_message)
            $ addtext ("V", "I'm happy to hear that", "V")
            $ addtext ("V", "We're all very grateful to be planning parties again.", "V") 
        
        "Thanks for checking on me":
            $ addtext ("MC", "Thanks for checking on me", "V")
            $ addtext ("V", "Of course", "V")
            $ addtext ("V", "Let me know if you need anything", "V")
        
    $ renpy.retain_after_load()
    return
    
    
    
    