
## This feature allows characters to continue talking
## while the player has an opportunity to interrupt/answer
label timed_menus():

    scene earlyMorn
    play music geniusly_hacked_bebop
    jump skipfortest
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

        "So I can choose between listening or interrupting?" :
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

    msg s "There's also a variation, which is called a continuous menu." bounce
    msg s "Continuous menus can have multiple answers with their own timers,"
    msg s "instead of all the answers showing up and disappearing at the same time."
    msg s "{image=seven_wow}"
    msg s "They're most fun to use when there's a really chaotic group chat."

label skipfortest:
    msg s "I summon everyone!! Alakazam!!" spike_l blocky
    enter chatroom y
    enter chatroom z
    enter chatroom ja
    enter chatroom ju

    # This variable isn't `default`ed, because we only use it in this small
    # section of the chatroom, so we can be sure that the player will get to
    # this line before the line which checks if this variable is defined.
    $ told_on_seven = False

    continuous menu:
        choice 1 "lolol omg everyone is here":
            msg s "Magic!!!" round2_m big
        msg ju "How strange. My phone opened the RFA app by itself and logged into the chatroom." ser1
        msg ju "Or did I do this? I was trying to open the camera app to take a photograph of Elizabeth the 3rd." ser1
        y "Nooooo I was in the middle of a LOLOL match;;;"
        choice 2 "You can play LOLOL later, Yoosung!":
            msg y "But I was doing a raid with my party T_T" sigh_m
            msg y "I'll never get that progress back..."
        msg y "{image=yoosung_cry}"
        y "All my progress... gone..."
        y "My computer just shut off and my phone logged me in here..."
        end choice 2
        z "Oh hey, [name] is here though~"
        choice 3 "I missed you, Zen~":
            award heart z
            msg z "{image=zen_wink}"
            msg z "Haha, I couldn't keep a cutie like you waiting long~" curly flower_m
        z "I was just thinking I'd log in to send a selfie lolol"
        end choice 1
        ja "Luciel, this wouldn't have anything to do with you, would it?"
        choice 4 "Seven made you all log in lol":
            $ told_on_seven = True
            msg s "{image=seven_what}"
            msg s "Betrayal!!! By mine own kin!!!"
            msg ja "What is he saying -_-" ser1
            msg s "I have summoned you all here today" glow pv 0.5
            msg s "On today," glow pv 0.5
            msg s "this glorious day" glow pv 0.5
            # This allows Seven to accurately say the current date.
            $ now = upTime()
            $ month = now.month
            $ weekday = now.weekday
            $ year = now.year
            msg s "This [weekday] in [month] in the year of Our Lord [year]..."
            msg ja "{image=jaehee_sad}"
        msg s "Oho no no I am very innocent~" curly
        msg s "{image=seven_love}"
        msg ja "{image=jaehee_huff}"

    msg ja "I was in the middle of something important, so if there isn't an emergency," ser1
    msg ja "I will be going."
    if told_on_seven:
        msg ja "Thank you for informing me of the situation, [name]."
    msg ja "Have a good night."
    exit chatroom ja
    msg ju "Yes, I will leave as well."
    msg ju "Elizabeth the 3rd is looking absolutely splendid curled up on the sofa" cloud_l curly
    msg ju "Good bye."
    exit chatroom ju
    if told_on_seven:
        msg s "[name]... they're all leaving..."
        call answer
        menu:
            "Hey, don't look at me lol":
                pass
            "I'm sorry, Seven T_T":
                msg s "Aw lolol"
                award heart s
                msg s "I don't want u to actually feel bad lolol"
    msg y "Oh! My computer's on again."
    msg y "I'll talk to you later, [name]!"
    exit chatroom y
    msg z "I don't have anything else to do"
    # We have no guarantees the player picked choice 4, so we redefine
    # 'now' here just in case, and also to get a more accurate time.
    $ now = upTime()
    if int(now.military_hour) > 21 or int(now.military_hour) < 6:
        msg z "Except, well, it IS late."
    elif 12 <= int(now.military_hour) <= 14:
        msg z "Except, well, I haven't had lunch yet."
    else:
        msg z "Except, well, I should probably go over my script before the end of the day."
    msg z "So maybe I'll log on later to talk to you~" curly
    call answer
    menu:
        "Bye, Zen!":
            msg z "{image=zen_wink}"
            msg z "See you, cutie~" glow curly
        "Everyone left so fast...":
            if told_on_seven:
                msg s "0_0"
            msg z "I'll be back later!"
            msg z "Bye for now~"
    exit chatroom z
    msg s "Ah, well, it was fun while it lasted."
    s "Anyway, I hope this gives you some cool ideas for ways to write chatrooms!"
    s "{image=seven_wow}" (img=True)
    s "{=curly}Toodles~!{/=curly}" (bounce=True, specBubble="cloud_s")
    exit chatroom s

    return

## A small work-around to prevent program errors; this just redirects the
## "expired" chatroom to the regular one
label timed_menus_expired():
    jump timed_menus


