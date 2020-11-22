label other_storytelling():

    scene evening
    play music same_old_fresh_air
    y "Hi, [name]!" (bounce=True)
    y "I'm here to show off another feature you can use to tell stories with this program ^^"
    y "Remember how this route started with a phone call and then became a chatroom?"

    # This is a special variant on timed menus where the game will pause for
    # the specified number of seconds before moving on. If you provide a `wait`
    # argument, you can't have any dialogue in the timed menu, just choices.
    timed menu (wait=5):
        "Yes":
            pass
        "No":
            pass

    y "{=curly}Well, you can also have VN sections in the middle of chatrooms!{/=curly}" (bounce=True, specBubble="square_l")
    y "I'll show you what I mean in a second."
    y "{=ser1}When the chatroom is about to switch to a VN section,{/=ser1}"
    y "{=ser1}you'll get a button at the bottom of the screen kinda like the 'answer' button.{/=ser1}"
    y "{=ser1xb}And if you press that, you'll be taken to the VN section.{/=ser1xb}"
    y "{=curly}Like now!{/=curly}" (bounce=True)

    # This will stop the chat and display a "Continue" button at the bottom
    # of the screen. Clicking it will take the player to the label you pass
    # it; here it goes to 'other_storytelling_vn_1'
    call vn_during_chat('other_storytelling_vn_1')

    y "{=sser2}See? We're back here in the chat.{/=sser2}"
    y "{=ser1}You might have noticed that the messages I sent you earlier are still in the history.{/=ser1}"
    y "{=ser1}If you want to start a new chatroom when you come back from the VN though, you can do that too.{/=ser1}"
    y "I'll demonstrate."
    exit chatroom y

    # This is the same as the above call, but on return, you can reset the
    # participants and the chatlog with `clear chat participants`, and then set
    # the background again. If you just want to clear the chatlog, not the
    # participants, just use `clear chat`. `clear chat participants` does both.
    call vn_during_chat('other_storytelling_vn_2')
    clear chat participants
    scene night

    play music same_old_fresh_air
    # Because the participants were cleared, Yoosung is not in the chatroom
    # any more, so he enters again.
    enter chatroom y
    y "{=curly}Hello again!{/=curly}" (bounce=True)
    y "See how the background has changed and the message history is gone?"
    y "{=curly}You can use this feature for a lot of neat things ^^{/=curly}"
    y "Good luck!" (bounce=True, specBubble="cloud_s")
    y "{image=yoosung_yahoo}" (img=True)
    exit chatroom y
    return

label other_storytelling_vn_1():
    # The music also carries over from the chatroom
    scene bg yoosung_room_day with fade
    show yoosung sparkle
    y "Tadaa!"
    y neutral "You can put whatever sort of scene you like in this part."
    y "And when the scene is done, it'll return to the chatroom."
    y happy "Like this!"
    # End with `return` like usual
    return

label other_storytelling_vn_2():
    scene bg yoosung_room_night with fade
    play music mystic_chat
    show yoosung neutral
    y "Okay so this is a different VN section."
    y grin "Pretend like it's a whole new scene! Time has passed!"
    y neutral "And now when we return, the chat log will be cleared."
    return

label other_storytelling_expired():
    scene evening
    play music same_old_fresh_air

    y "Aww, I wanted to talk to [name]..."
    y "Looks like [they_re] not here."
    y "{image=yoosung_cry}" (img=True)
    y "So, if you do come back and check out this chatroom,"
    y "There are some neat features!"
    y "An additional timed menu feature,"
    y "plus I can show you how we can switch to Story Mode in the middle of a chat."
    y "Like this!" (bounce=True)

    # Note that in some cases, you can reuse the VN label for
    # expired chatrooms as well.
    call vn_during_chat('other_storytelling_vn_1')

    y "There are more neat things you can do with it too."
    y "I hope you'll check them out!"
    exit chatroom y
    return

