label tutorial_chat():
    # You can change the characters' profile pictures as the beginning like so
    $ s.prof_pic = 'Profile Pics/Seven/sev-16.webp'
    $ y.prof_pic = 'Profile Pics/Yoosung/yoo-11.webp'

    # First, you need a background for the chatroom. Several have been
    # pre-defined, but you can add more. See the documentation for information.
    scene earlyMorn

    # Look for music in variables_music_sound.rpy. Ren'Py's default
    # implementation has been overridden to support audio captions.
    play music geniusly_hacked_bebop

    menu:
        "Do you still feel tired?":
            # Both 'branches' have several lines of dialogue before they
            # 'rejoin' later
            s "{=sser2}No way.{/=sser2}"
            s "{=sser2}One of my strengths is that I feel completely refreshed after sleeping{/=sser2}" (bounce=True, specBubble="cloud_l")
        "Seven, get a good night's rest?":
            # Characters can say the player's name by using [name] in their
            # dialogue.
            s "{=sser2}Heya [name]{/=sser2}"
            # You have to award heart points yourself. Just pass it the variable
            # of the name of the character whose heart icon you want
            # (character_definitions.rpy has the variable names if you're
            # not sure).
            award heart s
            s "{=sser2}Ya. Slept like a rock.{/=sser2}"

    s "{=sser2}I don't feel tired physically...{/=sser2}"
    s "{=sser2}But{/=sser2}"
    s "{=sser1xb}{size=+12}mentally, my stress level is MAX{/size}{/=sser1xb}"
    s "{image=seven_huff}" (img=True)
    s "{=sser1xb}How do I get rid of this stress...?!{/=sser1xb}" (bounce=True, specBubble="spike_m")

    menu:
        "Just take it out on Yoosung.":
            s "{=sser2}[name]...{/=sser2}"
            s "{=sser2}Ur pretty smart lol{/=sser2}" (bounce=True, specBubble="cloud_m")
            award heart s
        "You should play games.":
            s "o_o Game??"
            s "{=sser2}lol{/=sser2}"
            s "I'd rather make one. Playing it gets boring pretty fast lol"
    s "Hmm."
    s "{size=+12}I summon Yoosung! Abracadabra{/size}" (bounce=True, specBubble="spike_l")

    # Use this to display the message "Yoosung★ has entered the chatroom"
    # Just use the variable for the character who's entering
    # This adds them to the 'participant' list you see on the chatroom select.
    enter chatroom y

    menu:
        "Yoosung~ I missed you.":
            y "{=sser2}Thanks for being so welcoming.{/=sser2}"
            award heart y
            y "{=sser2}Hello ^^{/=sser2}"
        "Omg. He really came.":
            s "{=sser2}heya{/=sser2}"
            award heart s
            y "{=sser2}Hmm?{/=sser2}"
            y "I smell a trap somewhere..."

    s "What were u doing?"
    s "So late at night lol"
    y "I was just about to drink a cup of coffee and play games."
    y "I started learning how to brew coffee from a club yesterday."
    s "{=sser2}Coffee...?{/=sser2}"
    s "{=sser2}Ur learning how to make coffee...???{/=sser2}"
    y "{=sser2}Yup ^^{/=sser2}"
    s "{=ser1}No way. U can't.{/=ser1}"
    y "{=sser2}What?{/=sser2}"
    s "{=ser1}{size=+12}Did you already drink the coffee!?!?!?!?{/size}{/=ser1}"
    y "Yeah... Why?"

    # Another `play music` will automatically "override" the previous play
    # statement and only one set of background music will play on the music
    # channel at once
    play music dark_secret
    s "{=ser1b}Big trouble...{/=ser1b}"
    y "What trouble?"
    s "{=ser1}It's...{/=ser1}"

    menu:
        "Yoosung... what do we do now?":
            y "{=sser2}Why?{/=sser2}"
            y "{=sser2}Did something happen?{/=sser2}"
            s "{=ser1}Gah... I was about to tell [name].{/=ser1}"
        "What's big trouble?":
            y "Yeah. What is it?"
            s "{=ser1}It's...{/=ser1}"

    s "{=ser1}So, I check the health reports of all the members...{/=ser1}"
    y "{=sser2}{size=+12}Okay... Ur not saying that I can't dringak coffxee, r u?{/size}{/=sser2}"
    y "{=sser2}*drink coffee?{/=sser2}"

    menu:
        "Ya. U'll be in trouble if u drink coffee.":
            s "{=sser2}Ya...{/=sser2}"
            award heart s
            s "{=sser2}{size=+12}U can never ever!!! drink coffee.{/size}{/=sser2}"
            s "{=sser2}Seeing ur typos above, it seems like ur symptoms are showing already.{/=sser2}"
        "Seven's just messing around lol":
            y "Right? lolol"
            award heart y
            s "{=ser1xb}Not joking.{/=ser1xb}"
            s "{=ser1}I'm dead serious.{/=ser1}"
            y "{=sser2}Puppy food?{/=sser2}"

            # This is a nested menu; note the indentation levels.
            # You only see this menu if you choose 'Seven's just
            # messing around lol' in the previous menu
            menu:
                "-_-":
                    s "Cat food is serious meow"
                    y "{=sser2}I have no idea what ur saying.{/=sser2}"
                "lolololol":
                    s "{=ser1b}This is funny to u?{/=ser1b}"
                    y "{=sser2}lololololol{/=sser2}"

    s "{=ser1xb}U can never ever!!! drink coffee.{/=ser1xb}" (bounce=True, specBubble="spike_m")
    s "{=ser1xb}{size=+12}If u do, ur hands will start shaking and u'll faint eventually.{/size}{/=ser1xb}"
    y "Nah"
    y "I don't have that kind of allergy."
    y "No way~"
    s "{=sser2}...{/=sser2}"
    s "{=ser1}I'm sorry.{/=ser1}"
    s "{=ser1}U've already lost trust in me.{/=ser1}"
    s "{=ser1}so u r not listening.{/=ser1}"
    y "{=sser2}?{/=sser2}"
    y "For real?"
    s "{=ser1xb}Ur gonna faint. For real.{/=ser1xb}"
    y "{=sser2}Seriously?? Ur kidding right?{/=sser2}" (bounce=True, specBubble="spike_m")

    # This is the shake animation; it plays during
    # the previous line of dialogue.
    show shake

    menu:
        "You should prepare yourself.":
            s "Ya. Go prepare to faint."
            award heart s
        "I think fainting is a bit too much...":
            y "{=sser2}What?{/=sser2}"
            y "What do u mean?"
            s "{=sser2}Shh.{/=sser2}"
            s "{image=seven_wow}" (img=True)
            s "{=ser1}Listen carefully.{/=ser1}"

    s "{=ser1b}You are going to faint today.{/=ser1}"
    s "{=ser1}And there's a chance you might never wake up again...{/=ser1}"
    y "{size=+12}Why!?{/size}" (bounce=True, specBubble="spike_s")
    s "{=ser1b}You have the \"Pass Out After Drinking Caffeine Syndrome\"{/=ser1b}"
    y "??? What is that?"
    y "I don't understand what you mean."
    y "{=sser2}{size=+12}A disease like that actually exists?!{/size}{/=sser2}"

    menu:
        "Ya. It exists":
            y "{=sser1b}!!{/=sser1b}"
            show shake
            s "Ya"
            award heart s
        "Whoever named it is a bit...;;":
            s "{=blocky}It was made up at the last min so no choice.{/=blocky}"
            y "{=sser2}What do u mean made up at the last min?!{/=sser2}" (bounce=True, specBubble="spike_m")
            s "{=sser2}{size=+12}Your artificial heart{/size}{/=sser2}"
            y "{=sser2}Stop saying weird things;;{/=sser2}"
            y "{=sser2}Seven, ur joking right?{/=sser2}" (bounce=True, specBubble="spike_m")
            s "I am doing whatever I can to save u."

    s "{=sser2}...Don't be so surprised.{/=sser2}"
    y "Okay..."
    s "{=sser2}The disease called \"Pass Out After Drinking Caffeine Syndrome\"{/=sser2}"
    s "{=ser1b}It{/=ser1b}" (pauseVal=0.2)
    s "{=ser1b}exists{/=ser1b}" (pauseVal=0.2)
    s "{=ser1b}for sure{/=ser1b}" (pauseVal=0.3)
    s "I look at foreign reports every day."
    # Here 707 posts a CG
    s "common_1" (img=True)
    y "{=sser1b}{size=+12}!!!{/size}{/=sser1b}"
    s "{=ser1}...It's a rare disease.{/=ser1}"

    menu:
        "Last year there were about 1024 deaths in the country...":
            s "{=sser2}Oh! That number's nice. It's the 10th multiple of 2.{/=sser2}"
            award heart s
            y "{=sser2}Omg. Can't believe I have such a serious disease T_T{/=sser2}"
            y "{=sser2}I'm so svchoecked to type pertoperly T_T{/=sser2}"
        "What's wrong with the name lolololol A disease called Drink Caffeine and Faint lololol":
            y "{=sser2}lololol I know... It is funny T_T{/=sser2}"
            award heart y
            y "{=sser2}But I can't believe I have it.{/=sser2}"
            y "{image=yoosung_cry}" (img=True)

    y "{=sser2}{size=+12}What's going to happen to me T_T{/size}{/=sser2}"
    y "{=sser2}{size=+12}Am I gonna faint soon???{/size}{/=sser2}"
    s "According to my data"
    s "u'll faint some time between 9 and 10."
    y "{=sser2}T_T...{/=sser2}"
    y "I guess it could have been worse. I don't have class in the morning."

    menu:
        "^^;;":
            y "{=curly}Don't cry, [name].{/=curly}"
            y "{=curly}Even if I do faint... I'll be able to wake up.{/=curly}"

            menu:
                "I wasn't crying.":
                    y "{=curly}I read the emoji wrong T_T{/=curly}"

                    # This is the 'heartbreak' animation; call it the same
                    # way you would a heart icon except use `break heart y`
                    # instead of `award heart y`. For the heart break animation,
                    # `heart break y` will also work.
                    break heart y
                    y "{=curly}I thought u were crying by sweating{/=curly}"
                "T_T. You have to return.":
                    y "{=curly}Yup T_T I will return!!{/=curly}"
                    award heart y
                    s "{=sser2}Gahh... Tears r blocking my sight.{/=sser2}"

        "A stroke of good luck in this misfortune":
            y "I should at least pass out at home T_T"
            s "Ya"
            award heart s

    y "{image=yoosung_cry}" (img=True)
    y "Thanks for telling me Seven."
    s "{=sser2}lol It's nothing.{/=sser2}"

    menu:
        "Call Seven if something happens.":
            s "{=sser2}Ya. I'll always be here for u ^^{/=sser2}"
            award heart s
            y "Thank you T_T"
        "Call me if anything happens":
            y "{=sser2}Okay. Thank you so much T_T{/=sser2}"
            award heart y

    s "{=sser2}Oh.{/=sser2}"
    s "{=sser2}I recommend drinking chocolate milk before u faint.{/=sser2}"
    s "{=sser2}U have to increase ur blood pressure if u want to wake up faster.{/=sser2}"
    s "{=sser2}I'm worried...T_T{/=sser2}"
    y "{=sser2}Okay...{/=sser2}"
    y "Thank you. [name], you too..."
    s "{image=seven_yoohoo}" (img=True)

    menu:
        "^^;;;":
            y "Why do u keep sweating...?"
            y "{=sser2}U must be really worried for me.{/=sser2}"
            y "{size=+12}I'm touched!!{/size}"
            award heart y
        "No need ^^":
            y "I should know my body better."
            y "Never knew I had something like this..."
            y "It's confusing but..."
            y "{=sser2}I'll deal with it wisely.{/=sser2}"
            s "Ya. Dealing with it wisely is the way to go."

    s "{=sser2}...I'm glad to be of help.{/=sser2}"
    s "{=sser2}Ur young, so u'll wake up quickly if u do faint, so don't worry too much.{/=sser2}"
    y "{=curly}Okay...{/=curly}"
    y "{=curly}I shouldn't drink coffee anymore.{/=curly}"
    s "Oh... I got work again."
    s "{=sser2}Arrgghh!! Stress!!!{/=sser2}" (bounce=True, specBubble="spike_m")
    y "{=sser2}Both Jumin and u{/=sser2}"
    y "u guys r buried with work"
    y "{image=yoosung_cry}" (img=True)
    s "Can't do anything about it..."
    s "Then I'll get going."
    y "Yup!"
    y "Have a good night!!"
    s "{size=+12}lol{/size}"

    menu:
        "Seven, look out for my health too":
            s "{=sser2}U can trust me...^^{/=sser2}"
            award heart s
            y "{=sser2}That's good thinking... [name].{/=sser2}"
        ";;;":
            s "{=sser2}Then bye~!{/=sser2}"

    # Similar to 'enter chatroom', use this when a character leaves
    # the chatroom. Passing it the character's ChatCharacter variable
    # will cause it to display '707 has left the chatroom.'
    exit chatroom s
    y "{=curly}T_T What am I gonna do...{/=curly}"
    y "{=curly}[name]...{/=curly}"
    y "{=curly}If I faint and don't wake up...{/=curly}"
    y "{=curly}Can u wake me up with a... a.. a kiss?{/=curly}" (bounce=True)
    y "{=curly}I'm not trying to be weird.{/=curly}"
    y "{=curly}I just want to wake up and help open the party...{/=curly}"

    menu coffee_last:
        # Note that this menu has three options; you can add as many as
        # you like, but the screen only has room for 5 different options
        # so if you want more you need to split it up into multiple menus
        # with a Back/Next option (see tutorial_1_chatroom.rpy for some
        # examples of this).
        "Don't worry... Even if you don't wake up the party will be a success.":
            y "{image=yoosung_puff}" (img=True)
            y "{=curly}{size=+5}Do you mean that?{/size}{/=curly}"
            y "{=curly}I'm hurt...{/=curly}"
            # Like awarding heart points, you can also take away heart points
            # and show a 'heart break' animation with `break heart y` where
            # `y` is the character whose heart point you're subtracting.
            break heart y
        "I'll wake you up...":
            y "Oh...! Thank you." (bounce=True)
            award heart y
            y "{image=yoosung_happy}" (img=True)
        "Seven is just playing with you lolol":
            y "{=sser2}I know that ur worried too{/=sser2}"
            y "{=sser2}and don't want to believe what Seven said.{/=sser2}"
            y "{=sser2}But Seven's probably right.{/=sser2}"
            y "{=sser2}Seven is really knowledgeable.{/=sser2}"
            y "{=sser2}He once knew when my cold would get better.{/=sser2}"
            y "{=sser2}He said it'd be between the 3rd and 7th day{/=sser2}"
            y "{=sser2}And it completely went away on the fifth day.{/=sser2}"
            y "{=sser2}Look at that image above...{/=sser2}"
            y "{=sser2}I'm sure it's not a lie.{/=sser2}"

    y "{=sser2}First, I should get some chocolate milk...{/=sser2}"
    y "{=sser2}I'm gonna go to the supermarket~!{/=sser2}"
    exit chatroom y

    # Use this to end the chat and return to the main menu
    return


## Put anything you want to have happen after the chatroom ends here,
## like text messages, spaceship thoughts, or changes to voicemail messages.
## You have to name this label after_ + the name of the label for the
## chatroom (in this case, the chatroom label was tutorial_chat, so this
## label is after_tutorial_chat).
label after_tutorial_chat():

    # ************************************************
    # Seven's text message
    compose text s:
        s "Thanks for not spoiling the secret~ ^^"
        s "You're a lot of fun to talk to meow!"
        # The optional `label coffee1` is the name of the label to jump
        # to when the player replies to Seven's text message. You can leave
        # this out if you don't want the player to be able to reply anymore.
        label coffee1

    # ************************************************
    # Yoosung's text message
    compose text y:
        y "[name]... what do I do..."
        label coffee2

    # Set everyone else's voicemails appropriately (In this case, everyone
    # gets the same label). Voicemails are defined in phonecall_system.rpy
    python:
        for char in all_characters:
            char.voicemail = 'voicemail_1'

    # All labels end with `return`
    return

## This is the label you jump to for the phone call with Zen
## Because it's an incoming call, it should be be the name of the
## chatroom's label + _incoming_ + the variable of the character who's
## calling you (so, ja/ju/r/ri/s/sa/u/v/y/z)
label tutorial_chat_incoming_z:
    # The following two calls both have voice acting using Ren'Py's
    # automatic tagging system.
    # See: https://www.renpy.org/doc/html/voice.html
    # You can also use the voice statement directly,
    # e.g. voice 'Path to your file.mp3' and it will
    # play during the line of dialogue directly after it.
    z "Good morning, hon~"
    z "Gahh~ (Stretches) I haven't slept this well in a while. I feel really good."
    z "When I don't sleep that well, just moving my neck in the morning can hurt."
    z "Did you sleep well?"

    # Paraphrasing is turned on for this menu in order for it to play nice
    # with auto-voicing, but if you aren't using auto-voicing you can take
    # advantage of non-paraphrased menu choices as usual.
    menu (paraphrased=True):
        # If you want the previous dialogue to show up behind the choice
        # menu, you must add extend '' just after the menu
        extend ''
        "Yeah, I didn't even dream.":
            m "Yeah, I didn't even dream."
            z "That's good."
            z "I'm a bit sad to hear you didn't dream."
            z "I was waiting for you... looking like prince charming."
        "I didn't sleep very well.":
            m "I didn't sleep very well."
            z "You didn't? You must be tired then."
            z "Call me next time you can't sleep."
            z "I'll sing you a lullaby. If you fall asleep while listening to my voice, we'll be able to meet in our dreams."
            z "Two birds with one stone, no?"
            z "I can sing anything you want, so tell me whenever. I'll practice just for you."

    z "Aw yeah~! Starting my day with hearing your voice gives me so much energy."
    z "I have to leave early for work. I hope only good things happen today! To you and to me, haha."
    z "Then I'll call you later."
    z "Bye bye."

    return

## This is the label you jump to for the phone call with Yoosung
## It should be the name of the chatroom's label + _outgoing_ + the variable
## of the character you're calling (so, ja/ju/r/ri/s/sa/u/v/y/z)
label tutorial_chat_outgoing_y():
    y "I have not died."
    y "I will not die."
    y "To live, I must drink chocolate milk..."

    # Paraphrasing is turned on for this menu in order for it to play nice
    # with auto-voicing.
    menu (paraphrased=True):
        extend ''
        "The ones who wish to live will die and those who wish to die will live!":
            m "The ones who wish to live will die and those who wish to die will live!" (pauseVal=0)
            y "Uh-uh I know there's a super intelligent saying on that!"
            y "What was it...!!!!! I think Shakespears said it."
            y "Whatever... noo... that's not what's important..."
        "Yoo-Yoosung?":
            m "Yoo-Yoosung?" (pauseVal=0)
            y "nooooooooooooooooooooooooo"
            y "haaaaaaaaaaaaaaaaaaaaarggh"

    # This is 'monologue mode'; it's most useful here during phone calls.
    # Since you won't be changing expressions or speakers very often, this
    # can be faster than writing out 'y' before every line of dialogue.
    y """

    I went to the convenience store but I didn't bring my loyalty card so I didn't get a discount on the chocolate milk.

    This is a bad sign!!!

    Huahhhh......

    noooooooooooooo.....

    I'm sorry... I can't talk to you right now.

    My heart's about to explode...

    Even if you don't hear from me... it'll be fine...

    Even if I faint, I'll faint at home.

    ...Even if I faint... I'll resurrect myself...

    Please... God of Games... Let me play LOLOL tonight...

    Please cure me of this strange disease...!!!

    I... (sniffling) I have to go wipe off my snot. Bye...

    """

    return


## This should be the label you told the program to go to if they
## reply to a text message (in this case, Seven's text messagge).
label coffee1():
    menu:
        "I like talking to you too meow!":
            # Add heart icons the same way as a chatroom. You can
            # only give one heart per reply if the conversation is not
            # real-time, like this one
            award heart s
            s "<3 <3 <3"
            s "Agent 707 will do his best to come to the chatroom more often meow!"

        "I feel bad for Yoosung though...":
            # You can also award heart points for characters
            # not in the conversation.
            award heart y
            s "Nah~ he'll be fine"
            s "I'm sure he'd be happy you're worried for him tho lolol"

    return

## This is the label to go to when replying to Yoosung's message
label coffee2():
    menu:
        "Drink that chocolate milk!":
            award heart y
            y "I will!! I bought a lot of it..."
            y "It could be worse... I could've had classes tomorrow T_T"
            y "Thanks for worrying."

        "You do know Seven's just teasing, right?":
            y "I appreciate you trying to comfort me but..."
            y "You saw the news article he posted, right?"
            y "And he really does keep track of all the members..."
            y "I'm sure it's not a lie."

    return

## This is the chatroom the player will see if the chatroom is expired.
## It's much the same as the original chatroom, but with several lines
## changed since the MC is no longer present.
label tutorial_chat_expired():
    # If you modified the characters' profile pictures, you should replicate
    # this change for the expired chat as well.
    $ s.prof_pic = 'Profile Pics/Seven/sev-16.webp'
    $ y.prof_pic = 'Profile Pics/Yoosung/yoo-11.webp'
    scene earlyMorn
    play music geniusly_hacked_bebop
    s "Phew... I almost died."
    enter chatroom y
    s "The insane amount of work I have is making me so stressed..."
    s "How do I get rid of this stress...?!"
    y "Hey Seven"
    s "heya"
    y "Try learning how to make coffee like me."
    y "I think it can help you to de-stress."
    s "Coffee...?"
    s "Ur learning how to make coffee...???"
    y "Yup^^"
    s "{=ser1b}No way. U can't.{/=ser1b}"
    play music dark_secret
    y "What?"
    s "{=ser1b}Did u drink the coffee already!?!?!?!?{/=ser1b}"
    y "Yeah... Why?"
    s "{=ser1}Big trouble...{/=ser1}"
    y "What trouble?"
    s "It's..."
    s "So I check the health reports of all the members, yeah...?"
    y "{size=+10}Okay... Ur not saying that I can't dringak coffxee, r u?{/size}"
    y "*drink coffee ?"
    s "No... U can never ever!!! drink coffee."
    s "{=sser1xb}Seeing ur typos above, ur symptoms are showing already.{/=sser1xb}"
    y "Nah"
    y "I don't have that kind of allergy."
    y "No way~"
    s "..."
    s "I'm sorry."
    s "U've already lost trust in me"
    s "so u r not listening."
    y "?"
    y "For real?"
    s "{=ser1xb}{size=+10}Ur gonna faint. For real.{/size}{/=ser1xb}"
    y "What??"
    s "{=ser1xb}{size=+10}You are going to faint today.{/size}{/=ser1xb}"
    y "Just by drinking coffee?"
    s "You have the \"Pass Out After Drinking Caffeine Syndrome\""
    y "{size=+10}Yeah right, that doesn't actually exist!!{/size}"
    s "...Don't be so surprised."
    y "Okay..."
    s "Pass Out After Drinking Caffeine Syndrome"
    s "{=ser1b}It{/=ser1b}" (pauseVal=0.2)
    s "{=ser1b}exists{/=ser1b}" (pauseVal=0.2)
    s "{=ser1b}for sure.{/=ser1b}" (pauseVal=0.3)
    s "I look at reports from all over the globe every day."
    s "common_1" (img=True)
    y "{size=+10}!!!{/size}"
    s "...It's a rare disease."
    y "{size=+10}Oh man{/size}"
    y "{size=+10}What am I gonna do?{/size}"
    y "{image=yoosung_huff}" (img=True)
    y "When will I pass out then?"
    s "u'll faint sometime between 9 and 10."
    y "T_T..."
    y "I guess it could have been worse. I don't have class in the morning."
    y "I should be home when I pass out at least T_T"
    s "Every cloud has a silver lining."
    y "{image=yoosung_cry}" (img=True)
    y "Thanks for telling me Seven."
    s "lol it's nothing."
    s "Call me if something happens."
    s "Oh."
    s "I recommend drinking chocolate milk before u faint."
    s "U have to increase ur blood pressure if u want to wake up faster."
    s "{=curly}I'm srsly worried too{/=curly}"
    y "Okay..."
    y "Thank you."
    s "{image=seven_yoohoo}" (img=True)
    s "{=curly}...I'm glad to be of help.{/=curly}"
    s "{=curly}Ur young, so u'll wake up quickly if u do faint, so don't worry too much.{/=curly}"
    y "Okay..."
    y "I shouldn't drink coffee anymore."
    s "Oh... I got work again."
    s "Arrgghh!! Stress!!!"
    y "Both Jumin and you,"
    y "you guys are buried with work."
    y "{image=yoosung_cry}" (img=True)
    s "Can't do anything about it... ^^"
    s "Then I'll get going."
    y "Yup!"
    y "Have a good night!!"
    s "{=blocky}{size=+10}lol{/size}{/=blocky}"
    exit chatroom s
    y "T_T What am I gonna do..."
    y "[name]"
    y "If I pass out and don't wake up..."
    y "Please work hard on my behalf"
    y "and host the party again.... T_T"
    y "I'd better go buy some chocolate milk."
    exit chatroom y
    return




