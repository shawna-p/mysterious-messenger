label tutorial_chat():

    # You need to call chat_begin yourself; it's not an option
    # in the spreadsheet
    # Pass it the name of the background you want in quotes
    # You can find your background options in variables.rpy
    # Usually calling chat_begin will clear the chatlog, 
    # but if you want to keep previous messages, call it with 
    # clearchat=False (e.g. call chat_begin("night", clearchat=False))
    call chat_begin("earlyMorn") 
    
    # Look for music in variables_music_sound.rpy
    # This is a call rather than Ren'Py's built-in play music
    # feature so that it works with chatroom replay and accessibility
    # features such as audio captions
    call play_music(geniusly_hacked_bebop)
    
    # Use 'call answer' before any menu to bring up the answer button
    call answer 
    menu:
        "Do you still feel tired?":
            # Note that MC's responses have a pauseVal of 0 after a menu
            # Both 'branches' have several lines of dialogue before they
            # 'rejoin' later
            m "Do you still feel tired?" (pauseVal=0)
            s "{=sser2}No way.{/=sser2}"
            s "{=sser2}One of my strengths is that I feel completely refreshed after sleeping{/=sser2}" (bounce=True, specBubble="cloud_l")
        "Seven, get a good night's rest?":
            m "{=sser2}Seven, get a good night's rest?{/=sser2}" (pauseVal=0)
            s "{=sser2}Heya [name]{/=sser2}"
            
            # You have to call heart icons yourself. Just pass it the variable
            # of the name of the character whose heart icon you want
            # (character_definitions.rpy has the variable names if you're 
            # not sure) 
            call heart_icon(s) 
            s "{=sser2}Ya. Slept like a rock.{/=sser2}"
        # This is a special option which only appears if you've played
        # through this chatroom at least once across all playthroughs
        "(Jump to end)" if persistent.completed_chatrooms.get(
                                        current_chatroom.chatroom_label):
            # It's simply useful for test purposes as it jumps
            # to the end of the chatroom, and wouldn't be included
            # in a proper release
            jump coffee_last
            
    s "{=sser2}I don't feel tired physically...{/=sser2}"
    s "{=sser2}But{/=sser2}"
    s "{=sser1xb}{size=+12}mentally, my stress level is MAX{/size}{/=sser1xb}"
    s "{image=seven_huff}" (img=True)
    s "{=sser1xb}How do I get rid of this stress...?!{/=sser1xb}" (bounce=True, specBubble="spike_m")
    
    call answer 
    menu:
        "Just take it out on Yoosung.":
            m "Just take it out on Yoosung." (pauseVal=0)
            s "{=sser2}[name]...{/=sser2}"
            s "{=sser2}Ur pretty smart lol{/=sser2}" (bounce=True, specBubble="cloud_m")
            call heart_icon(s) 
        "You should play games.":
            m "You should play games." (pauseVal=0)
            s "o_o Game??"
            s "{=sser2}lol{/=sser2}"
            s "I'd rather make one. Playing it gets boring pretty fast lol"
    s "Hmm."
    s "{size=+12}I summon Yoosung! Abracadabra{/size}" (bounce=True, specBubble="spike_l")
    
    # Use this to display the message "Yoosung★ has entered the chatroom"
    # Just pass the variable for the character who's entering
    # This adds them to the 'participant' list you see on the chatroom select
    call enter(y) 
    
    call answer 
    menu:
        "Yoosung~ I missed you.":
            m "Yoosung~ I missed you." (pauseVal=0)
            y "{=sser2}Thanks for being so welcoming.{/=sser2}"
            call heart_icon(y) 
            y "{=sser2}Hello ^^{/=sser2}"
        "Omg. He really came.":
            m "Omg. He really came." (pauseVal=0)
            s "{=sser2}heya{/=sser2}"
            call heart_icon(s) 
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
    
    # Another play_music call will automatically "override" 
    # the previous play statement and only one set of 
    # background music will play on the music channel at once
    call play_music(dark_secret)
    s "{=ser1b}Big trouble...{/=ser1b}"
    y "What trouble?"
    s "{=ser1}It's...{/=ser1}"
    
    call answer 
    menu:
        "Yoosung... what do we do now?":
            m "Yoosung... what do we do now?" (pauseVal=0)
            y "{=sser2}Why?{/=sser2}"
            y "{=sser2}Did something happen?{/=sser2}"
            s "{=ser1}Gah... I was about to tell [name].{/=ser1}"
        "What's big trouble?":
            m "What's big trouble?" (pauseVal=0)
            y "Yeah. What is it?"
            s "{=ser1}It's...{/=ser1}"
            
    s "{=ser1}So, I check the health reports of all the members...{/=ser1}"
    y "{=sser2}{size=+12}Okay... Ur not saying that I can't dringak coffxee, r u?{/size}{/=sser2}"
    y "{=sser2}*drink coffee?{/=sser2}"
    
    call answer 
    menu:
        "Ya. U'll be in trouble if u drink coffee.":
            m "Ya. U'll be in trouble if u drink coffee." (pauseVal=0)
            s "{=sser2}Ya...{/=sser2}"
            call heart_icon(s) 
            s "{=sser2}{size=+12}U can never ever!!! drink coffee.{/size}{/=sser2}"
            s "{=sser2}Seeing ur typos above, it seems like ur symptoms are showing already.{/=sser2}"
        "Seven's just messing around lol":
            m "Seven's just messing around lol" (pauseVal=0)
            y "Right? lolol"
            call heart_icon(y) 
            s "{=ser1xb}Not joking.{/=ser1xb}"
            s "{=ser1}I'm dead serious.{/=ser1}"
            y "{=sser2}Puppy food?{/=sser2}"
            
            # This is a nested menu; note the indentation levels. 
            # You only see this menu if you choose 'Seven's just 
            # messing around lol' in the previous menu
            call answer 
            menu:
                "-_-":
                    m "-_-" (pauseVal=0)
                    s "Cat food is serious meow"
                    y "{=sser2}I have no idea what ur saying.{/=sser2}"
                "lolololol":
                    m "lolololol" (pauseVal=0)
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
    
    # This is the shake animation; it plays during the previous line of dialogue
    call shake
    
    call answer 
    menu:
        "You should prepare yourself.":
            m "You should prepare yourself." (pauseVal=0)
            s "Ya. Go prepare to faint."
            call heart_icon(s) 
        "I think fainting is a bit too much...":
            m "I think fainting is a bit too much..." (pauseVal=0)
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
    
    call answer 
    menu:
        "Ya. It exists":
            m "Ya. It exists" (pauseVal=0)
            y "{=sser1b}!!{/=sser1b}" 
            call shake
            s "Ya"
            call heart_icon(s) 
        "Whoever named it is a bit...;;":
            m "Whoever named it is a bit...;;" (pauseVal=0)
            s "{=blocky}It was made up at the last min so no choice.{/=blocky}"
            y "{=sser2}What do u mean made up at the last min?!{/=sser2}" (bounce=True, specBubble="spike_m")
            s "{=sser2}{size=+12}Your artificial heart{/size}{/=sser2}"
            y "{=sser2}Stop saying weird things;;{/=sser2}"
            y "{=sser2}Seven, ur joking right?{/=sser2}" (bounce=True, specBubble="spike_m")
            s "I am doing whatever I can to save u."
            
    s "{=sser2}...Don't get so surprised.{/=sser2}"
    y "Okay..."
    s "{=sser2}The disease called \"Pass Out After Drinking Caffeine Syndrome\"{/=sser2}"
    s "{=ser1b}It{/=ser1b}" (pauseVal=0.2)
    s "{=ser1b}exists{/=ser1b}" (pauseVal=0.2)
    s "{=ser1b}for sure{/=ser1b}" (pauseVal=0.3)
    s "I look at foreign reports every day."
    # Here 707 posts a CG
    s "common/cg-1.png" (img=True)
    y "{=sser1b}{size=+12}!!!{/size}{/=sser1b}"
    s "{=ser1}...It's a rare disease.{/=ser1}"
    
    call answer 
    menu:
        "Last year there were about 1024 deaths in the country...":
            m "Last year there were about 1024 deaths in the country..." (pauseVal=0)
            s "{=sser2}Oh! That number's nice. It's the 10th multiple of 2.{/=sser2}"
            call heart_icon(s) 
            y "{=sser2}Omg. Can't believe I have such a serious disease T_T{/=sser2}"
            y "{=sser2}I'm so svchoecked to type pertoperly T_T{/=sser2}"
        "What's wrong with the name lolololol A disease called Drink Caffeine and Faint lololol":
            m "What's wrong with the name lolololol A disease called Drink Caffeine and Faint lololol" (pauseVal=0)
            y "{=sser2}lololol I know... It is funny T_T{/=sser2}"
            call heart_icon(y) 
            y "{=sser2}But I can't believe I have it.{/=sser2}"
            y "{image=yoosung_cry}" (img=True)
            
    y "{=sser2}{size=+12}What's going to happen to me T_T{/size}{/=sser2}"
    y "{=sser2}{size=+12}Am I gonna faint soon???{/size}{/=sser2}"
    s "According to my data"
    s "u'll faint some time between 9 and 10."
    y "{=sser2}T_T...{/=sser2}"
    y "I guess it could have been worse. I don't have class in the morning."
    
    call answer 
    menu:
        "^^;;":
            m "^^;;" (pauseVal=0)
            y "{=curly}Don't cry, [name].{/=curly}"
            y "{=curly}Even if I do faint... I'll be able to wake up.{/=curly}"
            
            call answer 
            menu:
                "I wasn't crying.":
                    m "I wasn't crying." (pauseVal=0)
                    y "{=curly}I read the emoji wrong T_T{/=curly}"
                    
                    # This is the 'heartbreak' animation; call it the same 
                    # way you would a heart icon except use heart_break(y) 
                    # instead of heart_icon(y)
                    call heart_break(y) 
                    y "{=curly}I thought u were crying by sweating{/=curly}"
                "T_T. You have to return.":
                    m "T_T. You have to return." (pauseVal=0)
                    y "{=curly}Yup T_T I will return!!{/=curly}"
                    call heart_icon(y) 
                    s "{=sser2}Gahh... Tears r blocking my sight.{/=sser2}"
                    
        "A stroke of good luck in this misfortune":
            m "A stroke of good luck in this misfortune" (pauseVal=0)
            y "I should at least pass out at home T_T"
            s "Ya"
            call heart_icon(s) 
    
    y "{image=yoosung_cry}" (img=True)
    y "Thanks for telling me Seven."
    s "{=sser2}lol It's nothing.{/=sser2}"
    
    call answer 
    menu:
        "Call Seven if something happens.":
            m "Call Seven if something happens." (pauseVal=0)
            s "{=sser2}Ya. I'll always be here for u ^^{/=sser2}"
            call heart_icon(s) 
            y "Thank you T_T"
        "Call me if anything happens":
            m "Call me if anything happens" (pauseVal=0) 
            y "{=sser2}Okay. Thank you so much T_T{/=sser2}"
            call heart_icon(y) 
            
    s "{=sser2}Oh.{/=sser2}"
    s "{=sser2}I recommend drinking chocolate milk before u faint.{/=sser2}"
    s "{=sser2}U have to increase ur blood pressure if u want to wake up faster.{/=sser2}"
    s "{=sser2}I'm worried...T_T{/=sser2}"
    y "{=sser2}Okay...{/=sser2}"
    y "Thank you. [name], you too..."
    s "{image=seven_yoohoo}" (img=True)
    
    call answer 
    menu:
        "^^;;;":
            m "^^;;;" (pauseVal=0)
            y "Why do u keep sweating...?"
            y "{=sser2}U must be really worried for me.{/=sser2}"
            y "{size=+12}I'm touched!!{/size}"
            call heart_icon(y) 
        "No need ^^":
            m "No need ^^" (pauseVal=0) 
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
    
    call answer 
    menu:
        "Seven, look out for my health too":
            m "Seven, look out for my health too" (pauseVal=0)
            s "{=sser2}U can trust me...^^{/=sser2}"
            call heart_icon(s) 
            y "{=sser2}That's good thinking... [name].{/=sser2}"
        ";;;":
            m ";;;" (pauseVal=0) 
            s "{=sser2}Then bye~!{/=sser2}"
            
    # Similar to the 'enter' function, call this when a character leaves
    # the chatroom. Passing it the character's ChatCharacter variable
    # will cause it to display '707 has left the chatroom.'
    call exit(s) 
    y "{=curly}T_T What am I gonna do...{/=curly}"
    y "{=curly}[name]...{/=curly}"
    y "{=curly}If I faint and don't wake up...{/=curly}"
    y "{=curly}Can u wake me up with a... a.. a kiss?{/=curly}" (bounce=True)
    y "{=curly}I'm not trying to be weird.{/=curly}"
    y "{=curly}I just want to wake up and help open the party...{/=curly}"
    
    call answer 
    menu coffee_last:
        # Note that this menu has three options; you can add as many as 
        # you like, but the screen only has room for 5 different options 
        # so if you want more you need to split it up into multiple menus 
        # with a Back/Next option (see tutorial_1_chatroom.rpy for some 
        # examples of this)
        "Don't worry... Even if you don't wake up the party will be a success.":
            m "{=sser2}Don't worry... Even if you don't wake up the party will be a success.{/=sser2}" (pauseVal=0)
            y "{image=yoosung_puff}" (img=True)
            y "{=curly}{size=+5}Do you mean that?{/size}{/=curly}"
            y "{=curly}I'm hurt...{/=curly}"
            call heart_break(y) 
        "I'll wake you up...":
            m "I'll wake you up..." (pauseVal=0)
            y "Oh...! Thank you." (bounce=True)
            call heart_icon(y) 
            y "{image=yoosung_happy}" (img=True)
        "Seven is just playing with you lolol":
            m "{=sser2}Seven is just playing with you lolol{/=sser2}" (pauseVal=0)
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
    call exit(y) 
    
    # Use this to end the chat and return to the main menu
    jump chat_end

    
## Put anything you want to have happen after the chatroom ends here, 
## like text messages, spaceship thoughts, or changes to voicemail messages 
## You have to name this label after_ + the name of the label for the
## chatroom (in this case, the chatroom label was tutorial_chat, so this 
## label is after_tutorial_chat)
label after_tutorial_chat():

    # ************************************************
    # Seven's text message
    call compose_text(s)
    s "Thanks for not spoiling the secret~ ^^"
    s "You're a lot of fun to talk to meow!"
    # The optional parameter ('coffee1') is the name of the label to jump
    # to when you reply to Seven's text message. You can leave this
    # out if you don't want the player to be able to reply anymore
    call compose_text_end('coffee1')

    # ************************************************
    # Yoosung's text message
    call compose_text(y)
    y "[name]... what do I do..."
    call compose_text_end('coffee2')
    
    ## Set everyone else's voicemails appropriately
    # (In this case, everyone gets the same label)
    # Voicemails are defined in phonecall_system.rpy
    python:
        for char in all_characters:
            char.update_voicemail('voicemail_1')
    
    # Use this to end the after_ label
    return
    
## This is the label you jump to for the phone call with Zen
## Because it's an incoming call, it should be be the name of the
## chatroom's label + _incoming_ + the variable of the character who's
## calling you (so, ja/ju/r/ri/s/sa/u/v/y/z) 
label tutorial_chat_incoming_z:
    # Call this before the phone call begins
    call phone_begin 
    
    # The following two calls both have voice acting using Ren'Py's
    # automatic tagging system.
    # See: https://www.renpy.org/doc/html/voice.html
    # You can also use the voice statement directly, 
    # e.g. voice 'Path to your file.mp3' and it will 
    # play during the line of dialogue directly after it
    z_phone "Good morning, hon~"    
    z_phone "Gahh~ (Stretches) I haven't slept this well in a while. I feel really good."    
    z_phone "When I don't sleep that well, just moving my neck in the morning can hurt."    
    z_phone "Did you sleep well?"
    
    # You don't need call answer here because you go directly
    # into a choice menu during phone calls
    menu:
        # If you want the previous dialogue to show up behind the choice
        # menu, you must add "extend ''" just after the menu
        extend ''
        "Yeah, I didn't even dream.":
            m_phone "Yeah, I didn't even dream."            
            z_phone "That's good."            
            z_phone "I'm a bit sad to hear you didn't dream."            
            z_phone "I was waiting for you... looking like prince charming."
        "I didn't sleep very well.":
            m_phone "I didn't sleep very well."            
            z_phone "You didn't? You must be tired then."            
            z_phone "Call me next time you can't sleep."            
            z_phone "I'll sing you a lullaby. If you fall asleep while listening to my voice, we'll be able to meet in our dreams."            
            z_phone "Two birds with one stone, no?"            
            z_phone "I can sing anything you want, so tell me whenever. I'll practice just for you."
    
    
    z_phone "Aw yeah~! Starting my day with hearing your voice gives me so much energy."    
    z_phone "I have to leave early for work. I hope only good things happen today! To you and to me, haha."    
    z_phone "Then I'll call you later."    
    z_phone "Bye bye."
    
    # Use this when the call is finished
    jump phone_end
    
## This is the label you jump to for the phone call with Yoosung
## It should be the name of the chatroom's label + _outgoing_ + the variable
## of the character you're calling (so, ja/ju/r/ri/s/sa/u/v/y/z)
label tutorial_chat_outgoing_y():
    
    call phone_begin 
    
    y_phone "I have not died."
    y_phone "I will not die."
    y_phone "To live, I must drink chocolate milk..."
    
    menu:
        extend ''
        "The ones who wish to live will die and those who wish to die will live!":
            m_phone "The ones who wish to live will die and those who wish to die will live!"
            y_phone "Uh-uh I know there's a super intelligent saying on that!"
            y_phone "What was it...!!!!! I think Shakespears said it."
            y_phone "Whatever... noo... that's not what's important..."
        "Yoo-Yoosung?":
            m_phone "Yoo-Yoosung?"
            y_phone "nooooooooooooooooooooooooo"
            y_phone "haaaaaaaaaaaaaaaaaaaaarggh"
                    
    # This is 'monologue mode'; it's most useful here during phone calls.
    # Since you won't be changing expressions or speakers very often, this 
    # can be faster than writing out 'y_phone' before every line of dialogue
    y_phone """
    
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
    
    jump phone_end
 
    
## This should be the label you told the program to go to if they
## reply to a text message (in this case, Seven's text)
label coffee1():

    call text_begin(s)
    menu:
        "I like talking to you too meow!":
            m "I like talking to you too meow!"
            # We add heart icons the same way we would in
            # a chatroom. You can only give one per reply
            # if the conversation is not real-time like this one
            call heart_icon(s)
            s "<3 <3 <3"
            s "Agent 707 will do his best to come to the chatroom more often meow!"
        
        "I feel bad for Yoosung though...":
            m "I feel bad for Yoosung though..."
            # You can also award heart points for characters
            # not in the conversation
            call heart_icon(y)
            s "Nah~ he'll be fine"
            s "I'm sure he'd be happy you're worried for him tho lolol"

    # Always end text conversations with this call
    jump text_end
    
## This is the label to go to when replying to Yoosung's message
label coffee2():
    call text_begin(y)
    menu:
        "Drink that chocolate milk!":
            m "Drink that chocolate milk!"
            call heart_icon(y)
            y "I will!! I bought a lot of it..."
            y "It could be worse... I could've had classes tomorrow T_T"
            y "Thanks for worrying."
        
        "You do know Seven's just teasing, right?":
            m "You do know Seven's just teasing, right?"
            y "I appreciate you trying to comfort me but..."
            y "You saw the news article he posted, right?"
            y "And he really does keep track of all the members..."
            y "I'm sure it's not a lie."

    jump text_end
    
## This is the chatroom the player will see if the chatroom
## is expired. It's much the same as the original chatroom,
## but with several lines changed since the MC is no longer
## present
label tutorial_chat_expired():

    call chat_begin("earlyMorn") 
    call play_music(geniusly_hacked_bebop)
    s "Phew... I almost died." 
    call enter(y)
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
    call play_music(dark_secret)
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
    s "...Don't get so surprised." 
    y "Okay..." 
    s "Pass Out After Drinking Caffeine Syndrome" 
    s "{=ser1b}It{/=ser1b}"   (pauseVal=0.2)
    s "{=ser1b}exists{/=ser1b}"   (pauseVal=0.2)
    s "{=ser1b}for sure.{/=ser1b}"   (pauseVal=0.3)
    s "I look at reports from all over the globe every day." 
    s "common/cg-1.png"   (img=True)
    y "{size=+10}!!!{/size}" 
    s "...It's a rare disease." 
    y "{size=+10}Oh man{/size}" 
    y "{size=+10}What am I gonna do?{/size}" 
    y "{image=yoosung_huff}"   (img=True)
    y "When will I pass out then?" 
    s "u'll faint sometime between 9 and 10." 
    y "T_T..." 
    y "I guess it could have been worse. I don't have class in the morning." 
    y "I should be home when I pass out at least T_T" 
    s "Every cloud has a silver lining." 
    y "{image=yoosung_cry}"   (img=True)
    y "Thanks for telling me Seven." 
    s "lol it's nothing." 
    s "Call me if something happens." 
    s "Oh." 
    s "I recommend drinking chocolate milk before u faint." 
    s "U have to increase ur blood pressure if u want to wake up faster." 
    s "{=curly}I'm srsly worried too{/=curly}" 
    y "Okay..." 
    y "Thank you." 
    s "{image=seven_yoohoo}"   (img=True)
    s "{=curly}...I'm glad to be of help.{/=curly}" 
    s "{=curly}Ur young, so u'll wake up quickly if u do faint, so don't worry too much.{/=curly}" 
    y "Okay..." 
    y "I shouldn't drink coffee anymore." 
    s "Oh... I got work again." 
    s "Arrgghh!! Stress!!!" 
    y "Both Jumin and you," 
    y "you guys are buried with work." 
    y "{image=yoosung_cry}"   (img=True)
    s "Can't do anything about it... ^^" 
    s "Then I'll get going." 
    y "Yup!" 
    y "Have a good night!!" 
    s "{=blocky}{size=+10}lol{/size}{/=blocky}" 
    call exit(s)
    y "T_T What am I gonna do..." 
    y "[name]" 
    y "If I pass out and don't wake up..." 
    y "Please work hard on my behalf" 
    y "and host the party again.... T_T" 
    y "I'd better go buy some chocolate milk." 
    call exit(y)
    jump chat_end




    