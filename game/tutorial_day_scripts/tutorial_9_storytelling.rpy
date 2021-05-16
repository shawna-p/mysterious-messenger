label other_storytelling():
    $ y.prof_pic = "Profile Pics/Yoosung/yoo-13.webp"

    scene snowy_day
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

    y "{=curly}Well, you can also have Story Mode sections in the middle of chatrooms!{/=curly}" (bounce=True, specBubble="square_l")
    y "I'll show you what I mean in a second."
    compose text ju deliver_at now:
        ju "[name], I was hoping for a moment of your time."
    y "{=ser1}When the chatroom is about to switch to a story mode section,{/=ser1}"
    y "{=ser1}you'll get a button at the bottom of the screen kinda like the 'answer' button.{/=ser1}"
    compose text ju deliver_at now:
        ju 'ju_1' img
        label other_storytelling_ju_txt
    y "{=ser1xb}And if you press that, you'll be taken to the story mode section.{/=ser1xb}"
    y "{=curly}Like now!{/=curly}" (bounce=True)

    # This will stop the chat and display a "Continue" button at the bottom
    # of the screen. Clicking it will take the player to the label you pass
    # it; here it goes to 'other_storytelling_chat_vn_1'
    call vn_during_chat('other_storytelling_chat_vn_1')

    y "{=sser2}See? We're back here in the chat.{/=sser2}"
    y "{=ser1}You might have noticed that the messages I sent you earlier are still in the history.{/=ser1}"
    y "{=ser1}If you want to start a new chatroom when you come back from story mode though, you can do that too.{/=ser1}"
    y "I'll demonstrate."
    exit chatroom y

    # This is the same as the above call, but on return, you can reset the
    # participants and the chatlog with `clear chat participants`, and then set
    # the background again. If you just want to clear the chatlog, not the
    # participants, just use `clear chat`. `clear chat participants` does both.
    call vn_during_chat('other_storytelling_chat_vn_2')
    clear chat participants
    scene rainy_day

    play music same_old_fresh_air
    # Because the participants were cleared, Yoosung is not in the chatroom
    # any more, so he enters again.
    enter chatroom y
    y "{=curly}Hello again!{/=curly}" (bounce=True)
    y "See how the background has changed and the message history is gone?"
    y "{=curly}You can use this feature for a lot of neat things ^^{/=curly}"
    msg y "There's also another feature, customizable links."
    msg y "They look like this!"
    y "Click Link" (link_title="Address", link_action=JumpVN('other_storytelling_link_vn'))
    stop chat "Click on the link to continue"
    msg y "You might have noticed that the link can't be clicked anymore" ser1
    msg y "now that we're back in the chat" ser1
    msg y "Most links can only be clicked once," ser1
    msg y "But some, like links that show CG images, can be clicked more than once." ser1
    msg y "There's a lot you can do with these features!" curly glow
    msg y "I hope it inspires you to write some interesting chats~"
    y "Good luck!" (bounce=True, specBubble="cloud_s")
    y "{image=yoosung_yahoo}" (img=True)
    exit chatroom y
    return

# There aren't any restrictions on what you can call this label, but remember
# that if you call it the label of the chatroom + _vn, that makes an attached
# StoryMode, which isn't what you want. That's why this one is called
# other_storytelling_chat_vn_1 instead of other_storytelling_vn
label other_storytelling_chat_vn_1():
    # The music also carries over from the chatroom
    scene bg yoosung_room_day with fade
    show yoosung sparkle
    y "Tadaa!"
    y neutral "You can put whatever sort of scene you like in this part."
    y "And when the scene is done, it'll return to the chatroom."
    y happy "Like this!"
    # End with `return` like usual
    return

label other_storytelling_chat_vn_2():
    scene bg yoosung_room_night with fade
    play music mystic_chat
    show yoosung neutral
    y "Okay so this is a different story mode section."
    y grin "Pretend like it's a whole new scene! Time has passed!"
    y neutral "And now when we return, the chat log will be cleared."
    return

label other_storytelling_link_vn():
    scene bg yoosung_room_day with fade
    show yoosung happy
    y "Hi there!"
    y grin "Clicking this particular link took you to a story mode,"
    y "But you can use them to do all sorts of things."
    y "Any action you can give to a button, you can give to a link."
    y sparkle "So you could show an image, or toggle a variable, for example!"
    y neutral "Anyway, let's go back to the chat."
    return

label other_storytelling_ju_txt():
    menu:
        "She's so cuuuuuuute~!":
            award heart ju
            ju "Ah, thank you."
            ju "I presume the more 'u's used, the cuter you think she is."
        "Oof cat hair;;":
            award heart ja
            ju "I see you agree with Assistant Kang."
            ju "I simply do not understand how one can fault a creature as magnificent as Elizabeth the 3rd."
    ju "I hope the rest of your day is pleasant."
    return

label other_storytelling_expired():
    $ y.prof_pic = "Profile Pics/Yoosung/yoo-13.webp"
    scene snowy_day
    play music same_old_fresh_air

    y "Aww, I wanted to talk to [name]..."
    y "Looks like [they_re] not here."
    y "{image=yoosung_cry}" (img=True)
    y "So, if you do come back and check out this chatroom,"
    y "There are some neat features!"
    y "An additional timed menu feature,"
    y "plus I can show you how we can switch to Story Mode in the middle of a chat."
    y "Like this!" (bounce=True)

    # Note that in some cases, you can reuse the story mode label for
    # expired chatrooms as well.
    call vn_during_chat('other_storytelling_chat_vn_1')

    y "There are even in-chat links you can post"
    y "I hope you'll check them out!"
    exit chatroom y
    return

