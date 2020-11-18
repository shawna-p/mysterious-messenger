label example_text():

    scene morning
    play music mint_eye

    r "{=curly}Hi there!{/=curly}" (bounce=True, specBubble="square2_s")
    r "This chatroom is here to demonstrate how text messages are sent."
    r "You might have noticed that there's a Story Mode section after this chatroom, right?" (bounce=True)

    menu:
        "Does that mean anything specific?":
            r "It does!"
        "Yes, and I can't play it until after this chatroom, right?":
            r "{=curly}Right! ^^{/=curly}" (bounce=True, specBubble="flower_s")

    msg r "Usually, the program would delay sending text messages and phone calls" sser1
    msg r "until after both this chatroom and the Story Mode were played." sser1
    msg r "But since v3.0, things are more flexible!" flower_m
    msg r "If you declare a route using the new format,"
    msg r "you can have text messages and phone calls and the like after any story item,"
    msg r "even a chatroom that has a Story Mode attached" glow
    msg r "So, you'll receive some text messages after this chatroom,"
    msg r "and the rest after the Story Mode."
    r "{=ser1}You can set up text messages using an {b}after_{/b} chatroom label.{/=ser1}"
    r "See the wiki for more ^^"
    r "{image=ray_happy}" (img=True)
    r "Anyway, I won't keep you."
    r "See you soon!"

    exit chatroom r

    # Use this to end the chat and return to the main menu
    return

## This is the label you jump to if the chatroom is expired
label example_text_expired():
    scene morning
    play music mint_eye
    r "{=curly}Hi there!{/=curly}" (bounce=True, specBubble="square2_s")
    r "This chatroom is here to demonstrate how text messages are sent."
    r "But, well, since this chatroom is expired it won't act the same way."
    r "You'll have already received the text messages and any missed phone calls."
    r "Even if you buy this chatroom back, you won't receive the calls or messages again."
    r "But you can often call characters back if not much time has passed since they called!"
    r "Anyway, you can buy this chatroom back for some alternative information too."
    r "Talk to you soon!"
    exit chatroom r
    return

## Put anything you want to have happen after the chatroom ends here,
## like text messages, or changes to voicemail messages
label after_example_text():

    # There are two different variants on texting. The first, default
    # style is to have a character text the player many messages, wait
    # for the player's response, and then there is a delay and the character's
    # response is delivered all at once. This is demonstrated here.

    # ************************************************
    # V's text message
    # You start off with `compose text v` where v is the variable
    # of the character who's going to send the message. This message will just
    # be delivered after this chatroom, so there aren't any more arguments.
    compose text v:
        # Make sure you indent all the text messages under `compose text v`.
        v "Hello, [name]."
        v "I'm supposed to demonstrate how to make a character post an emoji during a text message."
        v "{image=v_smile}" # This is automatically recognized as an image
        v "They won't play audio like they do in the chatrooms,"
        v "But they can still be fun to use in a conversation, don't you think?"
        # And you're done with V's message! If you want the player to be able
        # to reply, you need to add a line telling the program which label to
        # find the reply at.
        label menu_a1

    # ************************************************
    # Ray's text message
    # The next style of texting happens in "real time", so you need to add
    # an extra variable to `compose text`.
    compose text r real_time:
        r "Here's a test text message, to show you how they work!"
        r "Did you know you can also post photos?"
        # Ray will continue sending messages once the player clicks on
        # his text message, so it ends here and you can add a label to
        # jump to like with V earlier.
        label menu_a2

    # End the whole label with return
    return

## This is the label included at the end of V's non-real time message.
label menu_a1():
    # If a text isn't in real-time, you should start with a menu right after
    # the label. You don't include `call answer` before this menu.
    menu:
        "Thanks for showing me this.":
            # If you have paraphrase_choices turned on, you won't need
            # (pauseVal=0) or `pv 0` after the MC's messages, because
            # they aren't sent in real-time e.g.
            # m "Thanks for showing me this."

            # You show heart icons in the same way as chatrooms.
            # It will appear after the player opens the text message
            # and sees V's response.
            award heart v
            v "You're very welcome!"
            v "Hope to talk to you again soon."

        "I'm not sure if they'll be useful...":
            m "I'm not sure if they'll be useful..."
            v "It's up to you whether to use them or not."
            v "I hope you enjoy the rest of the program."

    # End with `return` like usual
    return

## These are the labels for real-time text messaging.
label menu_a2():
    # Because this is real-time, you can continue to the conversation
    # before showing the player a menu.
    r "It will look like this:"
    r "r_1" (img=True) # You can show a CG in text messages as well.

    # You may notice these are written just like chatrooms, including
    # `call answer` to show the answer button.
    menu:
        "I'm not sure how I'll remember all this...":
            # Here, if paraphrase_choices is on, you *would* include `pv 0`
            # or (pauseVal=0), depending on how you're writing dialogue, for
            # the MC's response e.g.
            # m "I'm not sure how I'll remember all this..." (pauseVal=0)
            r "Don't worry! There are lots of resources to help."
            r "Let's do our best ^^"
        "That's a nice picture of you!":
            r "{image=ray_happy}" (img=True)
            award heart r
            r "Thank you ^^"

    # Everything ends with `return`
    return
