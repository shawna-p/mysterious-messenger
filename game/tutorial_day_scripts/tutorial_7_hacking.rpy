## A quick example chatroom to show off a few ways
## you can created a 'hacked' effect within chatrooms
label hack_example():

    scene night
    enter chatroom u
    u "Before we start -- are you okay with seeing flashing 'hacked' animations?"
    u "If not, we can turn them off."
    menu:
        "No; I don't want any flashing animations.":
            # Don't change settings on a replay
            if not observing:
                $ persistent.hacking_effects = False
        "Yes, you can keep the flashing animations on.":
            if not observing:
                $ persistent.hacking_effects = True
    u "Got it. See you around."
    exit chatroom u
    enter chatroom sa
    # This shows the red version of the "scrolled hacking" effect.
    show redhack effect
    # And this sets the background again, but doesn't clear the chatroom.
    scene redhack
    play music mysterious_clues_v2
    sa "Oh, so you want to know more about glitchy effects, do you?"
    sa "You want to make use of my hacking skills?"
    sa "Freak out your users?" (bounce=True, specBubble="glow2")
    sa "{size=+10}Get inside their minds?{/size}" (bounce=True, specBubble="glow2")

    menu:
        "Er... yes?":
            sa "{=curly}Haha!{/=curly}"
            sa "You asked for it!"
            sa "{image=saeran_expecting}" (img=True)
        "I don't want to freak them out exactly...":
            sa "You don't, hmm?"
            sa "Just you wait a moment"
            m "Show me what to do."
            # This deletes the last three items in the chatlog, discounting
            # the most recent message.
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
            menu:
                "I didn't type that!":
                    pass
            sa "Oh, are you sure?"
            sa "Just look at the chat log."
    sa "I've got lots of ways to hack your screen."
    sa "Inverted colours," (bounce=True)
    # The next several statements show how you can call
    # the various hacking effects. Combining several of
    # these screens often leads more interesting effects
    call invert_screen(t=0.2, p=0.5)
    sa "random glitchy squares," (bounce=True)
    call hack_rectangle_screen(t=0.2, p=0.01)
    call white_square_screen(t=0.19, p=0.5)
    sa "a tearing effect" (bounce=True)
    call tear_screen(number=40, offtimeMult=0.4, ontimeMult=0.2,
                        offsetMin=-10, offsetMax=30, w_timer=0.2, p=0.5)
    sa "You can delete messages and rewrite them."
    sa "There are a lot of things you can do if you're creative~"
    sa "{image=saeran_happy}" (img=True)
    sa "{=ser1}You should probably space out the glitchy effects,{/=ser1}"
    sa "{=ser1}otherwise it'll be bothersome for your users.{/=ser1}"
    sa "Whoops, gotta go."
    show redhack effect
    sa "Don't miss me too much~" (bounce=True)
    sa "{image=saeran_expecting}" (img=True)
    exit chatroom sa

    return

## The expired version for the example hack chatroom
label hack_example_expired():

    scene night
    show redhack effect
    scene redhack
    enter chatroom sa
    sa "Oh so I'm not good enough for you to log in?"
    sa "I'm not good enough for you?"
    call white_square_screen(t=0.2, p=0.01)
    call tear_screen(40, 0.4, 0.2, -30, 30, 0.2, p=0.5)
    sa "{size=+10}Hmm? Is that what you think?{/size}"
    call invert_screen(t=0.2, p=0.01)
    call tear_screen(60, 0.7, 0.1, -70, 70, 0.2, p=0.5)
    sa "{=ser1xb}{size=+10}Well FINE{/size}{/=ser1xb}" (bounce=True, specBubble="glow2")
    call hack_rectangle_screen(t=0.2, p=0.01)
    call tear_screen(100, 0.7, 0.1, -200, 200, 0.2, p=0.5)
    sa "I'm sure you don't need to use this phone either"
    sa "so I'll just go ahead and hack into it"
    sa "You'll be hearing from me later" (bounce=True)
    call hack_rectangle_screen(t=0.2, p=0.01)
    call invert_screen(t=0.2, p=0.01)
    call tear_screen(number=50, offtimeMult=0.4, ontimeMult=0.2,
                        offsetMin=-50, offsetMax=50, w_timer=0.18, p=0.01)
    call white_square_screen(t=0.16, p=0.17)
    exit chatroom sa
    show redhack effect
    clear chat # This clears all messages in the chat log
    scene night
    return


label after_hack_example():
    # This turns on the hacked effect on the timeline and in the
    # chat home screen.
    $ hacked_effect = True
    return