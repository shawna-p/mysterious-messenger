## A quick example chatroom to show off a few ways
## you can created a 'hacked' effect within chatrooms
label hack_example():

    call chat_begin("night")
    call enter(u)
    u "Before we start -- are you okay with seeing flashing 'hacked' animations?"
    u "If not, we can turn them off."
    call answer
    menu:
        "No; I don't want any flashing animations.":
            m "No; I don't want any flashing animations." (pauseVal=0)
            $ persistent.hacking_effects = False
        "Yes, you can keep the flashing animations on.":
            m "Yes, you can keep the flashing animations on." (pauseVal=0)
            $ persistent.hacking_effects = False
    u "Got it. See you around."
    call exit(u)
    call enter(sa)
    call redhack    
    call chat_begin('redhack', False, False)
    call play_music(mysterious_clues_v2)
    sa "Oh, so you want to know more about glitchy effects, do you?" 
    sa "You want to make use of my hacking skills?" 
    sa "Freak out your users?"   (bounce=True, specBubble="glow2")
    sa "{size=+10}Get inside their minds?{/size}"   (bounce=True, specBubble="glow2")
    
    call answer
    menu:
        "Er... yes?":
            m "Er... yes?"   (pauseVal=0)
            sa "{=curly}Haha!{/=curly}" 
            sa "You asked for it!" 
            sa "{image=saeran_expecting}" (img=True)
        "I don't want to freak them out exactly...":
            m "I don't want to freak them out exactly..." (pauseVal=0)
            sa "You don't, hmm?" 
            sa "Just you wait a moment"                      
            m "Show me what to do." 
            # This deletes the last three items in the chatlog, discounting
            # the most recent message
            # You might have to experiment with how many messages to
            # delete/where to put the delete line since the program sometimes
            # has "hidden" chatlog entries that aren't shown to the user
            # In general you can put it one message after the last message
            # you want to delete
            call remove_entries(num=4)
            call hack_rectangle_screen(t=0.2, p=0.01)
            call invert_screen(t=0.19, p=0.01)
            call tear_screen(number=10, offtimeMult=0.4, ontimeMult=0.2, 
                                offsetMin=-10, offsetMax=30, w_timer=0.18,
                                p=0.01)
            call white_square_screen(t=0.16, p=0.17)
            sa "{image=saeran_happy}" (img=True)
            call answer
            menu:
                "I didn't type that!":
                    m "I didn't type that!" (pauseVal=0)
            sa "Oh, are you sure?" 
            sa "Just look at the chat log." 
    sa "I've got lots of ways to hack your screen." 
    sa "Inverted colours,"   (bounce=True)
    # The next several statements show how you can call
    # the various hacking effects. Combining several of
    # these screens often leads more interesting effects
    call invert_screen(t=0.2, p=0.5)
    sa "random glitchy squares,"   (bounce=True)
    call hack_rectangle_screen(t=0.2, p=0.01)
    call white_square_screen(t=0.19, p=0.5)
    sa "a tearing effect"   (bounce=True)
    call tear_screen(number=40, offtimeMult=0.4, ontimeMult=0.2, 
                        offsetMin=-10, offsetMax=30, w_timer=0.2, p=0.5)
    sa "You can delete messages and rewrite them."        
    sa "There are a lot of things you can do if you're creative~" 
    sa "{image=saeran_happy}"   (img=True)
    sa "{=ser1}You should probably space out the glitchy effects,{/=ser1}" 
    sa "{=ser1}otherwise it'll be bothersome for your users.{/=ser1}" 
    sa "Whoops, gotta go." 
    call redhack
    sa "Don't miss me too much~"   (bounce=True)
    sa "{image=saeran_expecting}"   (img=True)
    call exit(sa)

    jump chat_end
 
## The expired version for the example hack chatroom 
label hack_example_expired():

    call chat_begin("night")
    call redhack
    call chat_begin('redhack', False, False)
    call enter(sa)
    sa "Oh so I'm not good enough for you to log in?" 
    sa "I'm not good enough for you?"
    call white_square_screen(t=0.2, p=0.01) 
    call tear_screen(40, 0.4, 0.2, -30, 30, 0.2, p=0.5)
    sa "{size=+10}Hmm? Is that what you think?{/size}"
    call invert_screen(t=0.2, p=0.01)
    call tear_screen(60, 0.7, 0.1, -70, 70, 0.2, p=0.5)
    sa "{=ser1xb}{size=+10}Well FINE{/size}{/=ser1xb}"   (bounce=True, specBubble="glow2")
    call hack_rectangle_screen(t=0.2, p=0.01)
    call tear_screen(100, 0.7, 0.1, -200, 200, 0.2, p=0.5)
    sa "I'm sure you don't need to use this phone either" 
    sa "so I'll just go ahead and hack into it" 
    sa "You'll be hearing from me later"   (bounce=True)
    call hack_rectangle_screen(t=0.2, p=0.01)
    call invert_screen(t=0.2, p=0.01)
    call tear_screen(number=50, offtimeMult=0.4, ontimeMult=0.2, 
                        offsetMin=-50, offsetMax=50, w_timer=0.18, p=0.01)
    call white_square_screen(t=0.16, p=0.17)
    call exit(sa)
    call redhack
    call chat_begin('night', True, False)
    jump chat_end

    
    