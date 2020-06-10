label other_storytelling():

    call chat_begin('evening')
    call play_music(same_old_fresh_air)
    y "Hi, [name]!" (bounce=True)
    y "I'm here to show off another feature you can use to tell stories with this program ^^"
    y "Remember how this route started with a phone call and then became a chatroom?"
    
    # This tells the program to show the answer button at the bottom of
    # the screen, but the chat continues in the meantime
    call continue_answer("other_storytelling_menu1", 5)
    # Since this is set to the same amount of time for the timed answer
    # above, the chat will "pause" for a few seconds to let the player
    # respond. If they don't, the chat moves on
    call timed_pause(5)
    
    if timed_choose:
        menu other_storytelling_menu1:
            "Yes.":
                m "Yes." (pauseVal=0)
            "No.":
                m "No." (pauseVal=0)
    
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
    call exit(y)

    # These second arguments tell the program to clear the chat when
    # the player returns after the VN. It sets the background of the
    # chatroom to the 'night' background when it returns.
    call vn_during_chat('other_storytelling_vn_2', clearchat_on_return=True,
                        new_bg='night')

    call play_music(same_old_fresh_air)
    call enter(y)
    y "{=curly}Hello again!{/=curly}" (bounce=True)
    y "See how the background has changed and the message history is gone?"
    y "{=curly}You can use this feature for a lot of neat things ^^{/=curly}"
    y "Good luck!" (bounce=True, specBubble="cloud_s")
    y "{image=yoosung_yahoo}" (img=True)
    call exit(y)
    jump chat_end

label other_storytelling_vn_1():
    # Note that there is no need to begin with `call vn_begin`
    # The music also carries over from the chatroom
    scene bg yoosung_room_day with fade
    show yoosung sparkle
    y "Tadaa!"
    y neutral "You can put whatever sort of scene you like in this part."
    y "And when the scene is done, it'll return to the chatroom."
    y happy "Like this!"
    # End with `return` instead of `jump vn_end`
    return

label other_storytelling_vn_2():
    scene bg yoosung_room_night with fade
    call play_music(mystic_chat)
    show yoosung neutral
    y "Okay so this is a different VN section."
    y grin "Pretend like it's a whole new scene! Time has passed!"
    y neutral "And now when we return, the chat log will be cleared."
    return

label other_storytelling_expired():
    call chat_begin('evening')
    call play_music(same_old_fresh_air)

    y "Aww, I wanted to talk to [name]..."
    y "Looks like [they_re] not here."
    y "{image=yoosung_cry}" (img=True)
    y "So, if you do come back and check out this chatroom,"
    y "There are some neat features!"
    y "An additional timed menu feature,"
    y "plus I can show you how we can switch to VN mode in the middle of a chat."
    y "Like this!" (bounce=True)

    # Note that in some cases, you can reuse the VN label for
    # expired chatrooms as well.
    call vn_during_chat('other_storytelling_vn_1')

    y "There are more neat things you can do with it too."
    y "I hope you'll check them out!"
    call exit(y)
    jump chat_end

    