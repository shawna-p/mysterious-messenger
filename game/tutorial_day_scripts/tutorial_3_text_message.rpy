label example_text():

    call chat_begin("morning")
        
    call play_music(mint_eye)
    
    r "{=curly}Hi there!{/=curly}"   (bounce=True, specBubble="square2_s")
    r "This chatroom is here to demonstrate how text messages are sent." 
    r "You might have noticed that there's a Story Mode section after this chatroom, right?"   (bounce=True)
    
    call answer
    menu:
        "Does that mean anything specific?":
            m "Does that mean anything specific?"   (pauseVal=0)
            r "It does!" 
            r "Since there's a story mode VN (Visual Novel) section," 
            r "{=sser2b}any incoming phone calls or text message won't be delivered until after the VN.{/=sser2b}" 
        "Yes, and I can't play it until after this chatroom, right?":
            m "Yes, and I can't play it until after this chatroom, right?"   (pauseVal=0)
            r "{=curly}Right! ^^{/=curly}"   (bounce=True, specBubble="flower_s")
            r "Any incoming phone calls or text message won't be delivered until after the story mode VN (Visual Novel) section, too." 
            
    r "So even though there are text messages to be delivered after this chatroom," 
    r "{=ser1}{size=+10}you won't see them right away.{/size}{/=ser1}" 
    r "{=ser1}You can set up text messages using an {b}after_{/b} chatroom label.{/=ser1}" 
    r "See the wiki for more ^^" 
    r "{image=ray_happy}"   (img=True)
    r "Anyway, I won't keep you." 
    r "See you soon!" 

    call exit(r)
    
    # Use this to end the chat and return to the main menu
    jump chat_end
    
## This is the label you jump to if the chatroom is expired
label example_text_expired():
    call chat_begin('morning')
    call play_music(mint_eye)
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
## like text messages, or changes to voicemail messages
label after_example_text():

    # There are two different variants on texting. The first, default
    # style is to have a character text the player many messages, wait
    # for the player's response, and then there is a delay and the character's
    # response is delivered all at once. This is demonstrated here

    # ************************************************
    # V's text message
    # You always start off with compose_text(v) where v is the variable
    # of the character who's going to send the message
    call compose_text(v)
    v "Hello, [name]."
    v "I'm supposed to demonstrate how to make a character post an emoji during a text message."
    v "{image=v_smile}" (img=True)
    v "They won't play audio like they do in the chatrooms,"
    v "But they can still be fun to use in a conversation, don't you think?"
 
    # And you're done with V's message! Be sure to end it with this call
    # There's one optional parameter, text_label. This tells the program
    # which label to jump to so the player can reply to this message
    # If you just do `call compose_text_end()` the player won't be able
    # to reply
    call compose_text_end(text_label='menu_a1')

    # ************************************************
    # Ray's text message
    # The next style of texting means you must set a particular
    # variable for the character you want to text in real-time
    
    # Same thing here, start with call compose_text, but you also
    # need to tell it real_time=True
    call compose_text(r, real_time=True)
    r "Here's a test text message, to show you how they work!"
    r "Did you know you can also post photos?"

    # Ray will continue sending messages once the player clicks on 
    # his text message, so it ends here and you can add a label to 
    # jump to like with V earlier
    call compose_text_end('menu_a2')

    # ************************************************
    # Zen's text message
    # This is another example of real-time texting
    call compose_text(z, True)
    z "You know, you never send us any photos..."
    call compose_text_end('menu_a3')   
    
    # End the whole label with return
    return
    

## This is the label included at the end of
## V's non-real time message
label menu_a1():
    # You always start with `call text_begin` and pass it the
    # variable of the character you're texting
    call text_begin(v)
    # If a text isn't in real-time, you should start with 
    # a menu right after `call text_begin`
    # You don't include `call answer` before this menu
    menu:    
        "Thanks for showing me this.":
            m "Thanks for showing me this."
            # You show heart icons in the same way as chatrooms
            # It will appear after the player opens the text message
            # and sees V's response
            call heart_icon(v)
            v "You're very welcome!"
            v "Hope to talk to you again soon." 
        
        "I'm not sure if they'll be useful...":
            m "I'm not sure if they'll be useful..."
            v "It's up to you whether to use them or not."
            v "I hope you enjoy the rest of the program."
        
    # Always end with a `jump text_end`
    jump text_end
    
    
## These are the labels for instant text messaging
label menu_a2():
    # You pass `text_begin` the variable of the character
    # the player is texting
    call text_begin(r)
    
    # Because this is real-time, you can continue to the conversation
    # before showing the player a menu
    r "It will look like this:"
    r "r_1" (img=True)
    
    # You may notice these are written just like chatrooms
    call answer
    menu:
        "I'm not sure how I'll remember all this...":
            m "I'm not sure how I'll remember all this..." (pauseVal=0)
            r "Don't worry! There are lots of resources to help."
            r "Let's do our best ^^"
        "That's a nice picture of you!":
            m "That's a nice picture of you!" (pauseVal=0)
            r "{image=ray_happy}" (img=True)
            call heart_icon(r)
            r "Thank you ^^"
            
    # Real-time text messages end the same way as regular ones
    jump text_end

label menu_a3():
    call text_begin(z)
    # Even though this conversation begins with a menu, if it's
    # in real time you need to include 'call answer' before the menu
    call answer
    menu:
        # The player can post both CGs and emojis
        "(Post a photo)":
            m "common_2" (pauseVal=0, img=True)
            m "You mean like this?"
        "(Post an emoji)":
            m "{image=zen_oyeah}" (pauseVal=0, img=True)
            m "How's this?"
        "(Post both)":
            m "common_2" (pauseVal=0, img=True)
            m "{image=zen_oyeah}" (img=True)
            m "What do you think?"

    z "Wow! I've never seen that before."
    z "You're pretty cool"
    z "{image=zen_wink}" (img=True)
    jump text_end
    