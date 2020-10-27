## This feature allows characters to continue talking
## while the player has an opportunity to interrupt/answer
label timed_menus():

    scene earlyMorn
    play music geniusly_hacked_bebop

    s "{size=+10}Hiya!{/size}" (bounce=True, specBubble="round2_s")
    s "{=curly}I'm here to tell you all about timed menus~{/=curly}"
    s "They work mostly like regular menus,"
    s "{=ser2}except the characters will keep talking even after choices appear at the bottom of the screen.{/=ser2}"
    s "Like now!" (bounce=True)

    timed menu:
        s "You only have so long to reply,"
        s "and when the planet at the bottom of the screen reaches the right side,"
        s "BAM!!" (bounce=True, specBubble="spike_s")
        s "The opportunity to answer has passed!!!"
        s "You write these menus a bit differently than regular menus"
        s "You'll see an example of it in this code."
        "Slow down! Timed menus??":
            s "Whoops lolol I got a bit excited"
            s "{=sser2}Yup! Maybe try playing through this chatroom a few times to see what happens?{/=sser2}"
            s "Don't forget to turn Testing Mode on from the developer settings so you can make different choices."

        "So I can choose between listening or interrupting?":
            s "Yeah! If you just let the chat play out,"
            s "you'll see different dialogue than if you'd decided to answer."

    s "{=ser1}There's a special slider for how fast timed menus are in the Settings,{/=ser1}"
    s "{=ser1}so you can have the chatroom speed be really fast{/=ser1}"
    msg s "but the timed menus will slow down to give you time to think!" ser1
    s "So if you've got the timed menu speed all the way to the left,"
    s "the planet will take longer to reach the other side of the screen."
    s "There's also an option in {b}Settings{/b} to turn off timed menus altogether," (bounce=True)
    s "in case you find the timing stressful!" (bounce=True)
    s "Do you want timed menus on, or should I turn them off for you?"
    call answer
    menu:
        "Keep timed menus on.":
            # Don't want to adjust the preferences for a player who is
            # just replaying a chatroom from the History screen.
            if not observing:
                $ persistent.use_timed_menus = True
            s "Sure thing!"
        "Turn timed menus off.":
            if not observing:
                $ persistent.use_timed_menus = False
            s "Got it."
            s "You can always turn them on later and adjust the speed to your liking!"
    s "Anyway, I hope this gives you some cool ideas for ways to write chatrooms!"
    s "{image=seven_wow}" (img=True)
    s "{=curly}Toodles~!{/=curly}" (bounce=True, specBubble="cloud_s")
    exit chatroom s
    return


## A small work-around to prevent program errors; this just redirects the
## "expired" chatroom to the regular one
label timed_menus_expired():
    jump timed_menus


