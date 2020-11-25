# Inviting a Guest

**Example files to look at: [tutorial_2_emails.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_2_emails.rpy "tutorial_2_emails")**

After you've defined your guest as per [[Writing an Email Chain]], in the chatroom or VN section that you'd like to invite the guest in, use the call:

```renpy
call invite(your_guest)
```

where `your_guest` is the variable that you made when you defined the guest using

```renpy
default your_guest = Guest("test", "thumbnail.png", ...)
```

After the chatroom or VN section is over, the player will receive the first email from that guest.
