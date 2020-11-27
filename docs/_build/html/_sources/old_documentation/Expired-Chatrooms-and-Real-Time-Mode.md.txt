# Expired Chatrooms and Real-Time Mode

**Example files to look at: [tutorial_5_coffee.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_5_coffee.rpy "tutorial_5_coffee"), [tutorial_6_meeting.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_6_meeting.rpy)**

In this program, you can switch between two different play styles: real-time, and sequential. Sequential is currently the default. You can toggle real-time from the **Developer** settings button in the main chat hub or on the main menu screen.

In sequential mode, chatrooms and VN mode sections unlock sequentially. In other words, once you finish a chatroom, the next one will automatically unlock. Chatrooms don't expire unless you back out of them (aka hitting the Back arrow while in an active chatroom), and you can proceed through chatrooms regardless of what the current time is.

In real-time mode, chatrooms unlock based on the current time. You also have the option to buy the next 24 hours' worth of chatrooms in advance. If an old chatroom has not been viewed before a new one unlocks it will expire, and you will miss any incoming calls that were triggered to occur after the now-expired chatroom (though you can usually call the characters back).

Each chatroom you create should have both a "regular" version and an "expired" version. The expired version is the version the player will play through if the chatroom has expired and they have not bought it back. Generally this means the player will not have the opportunity to participate in this chatroom or make choices.

To create the expired chatroom, simply take the name of the regular chatroom and add `_expired`. So, if your chatroom has the label

```renpy
label mychat:
```

then the expired chatroom should have the label

```renpy
label mychat_expired:
```

The rest can be filled out as any other chatroom.

### Note: Backing out of chatrooms vs. real-time expiry

There are two different ways for chatrooms to expire: first, chatrooms expire if you are playing in real-time and miss a chatroom before the next one triggers. Second, chatrooms expire if you use the back arrow during a chat you haven't seen before.

In the first case (expiry due to real-time mode being active), the following will happen:

* You will receive a missed call from any character who was going to call you after the expired chatroom. You can call that character back to receive that conversation.
* Any text messages that would have been delivered after the chatroom (or VN) will be automatically delivered to your inbox
* Any outgoing calls that were to be made available after the chatroom (or VN) will be made available

Note that phone calls will "time out" two chatrooms after they were set to appear. So, for example, say you have three chatrooms: A, B, and C. Bob is supposed to call you after chatroom A. If chatroom B becomes available before you've seen chatroom A, then chatroom A will expire and you will receive a missed phone call from Bob. You can call Bob back to receive this phone call up until chatroom C becomes available, at which point that phone call will become unavailable and you won't be able to call Bob back to get that conversation anymore.

In the second case, where the player backs out of an active chatroom and causes it to expire, the following will happen:

* Any incoming calls that would have been triggered after the chatroom are instead turned into outgoing calls, __though the player receives no missed call notification__
* Any text messages that would have been delivered after the chatroom (or VN) will be automatically delivered to your inbox
* Any outgoing calls that were to be made available after the chatroom (or VN) will be made available

As you can see, the only real difference is in the first point. Incoming phone conversations will still be available, but you will not receive a missed call notification for it.
