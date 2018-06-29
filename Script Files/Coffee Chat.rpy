label coffee_chat:

    # You'll need to call this yourself; it's not an option in the spreadsheet
    # Pass it the name of the background you want in quotes
    # You can find your options in variables.rpy
    # Usually calling chat_begin will clear the chatlog, but if you want to keep
    # previous messages, call it with False as a second argument (e.g. call chat_begin("night", False))
    call chat_begin("earlyMorn")
    
    # Again, look for music in variables.rpy
    # You'll want to tell background music to loop
    play music geniusly_hacked_bebop loop
    
    # use 'call answer' before any menu to bring up the answer button
    call answer
    menu:
        "Do you still feel tired?":
            # Note that MC's responses have a pv value of 0 after a menu
            # Both 'branches' have several lines of dialogue before they 'rejoin' later
            m "Do you still feel tired?" (pauseVal=0)
            s "{=sser2}No way.{/=sser2}"
            s "{=sser2}One of my strengths is that I feel completely refreshed after sleeping{/=sser2}" (bounce=True, specBubble="cloud_l")
        "Seven, get a good night's rest?":
            m "{=sser2}Seven, get a good night's rest?{/=sser2}" (pauseVal=0)
            s "{=sser2}Heya [name]{/=sser2}"
            
            # You have to call heart icons yourself. Just pass it the variable
            # of the name of the character whose heart icon you want
            # (character definitions.rpy has the variable names if you're not sure) 
            call heart_icon(s)
            s "{=sser2}Ya. Slept like a rock.{/=sser2}"
        "Jump to end":
            jump coffee_last
            
    s "{=sser2}I don't feel tired physically...{/=sser2}"
    s "{=sser2}But{/=sser2}"
    s "{=sser1xb}{size=+12}mentally, my stress level is MAX{/size}{/=sser1xb}"
    s "{image=seven huff}" (img=True)
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
    
    # Another play statement will automatically "override" the previous play statement
    # and only one set of background music will play on the music channel at once
    play music dark_secret loop
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
            
            # This is a nested menu; note the indentation levels. You'll only see this menu
            # if you choose 'Seven's just messing around lol' in the previous menu
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
    s "{=ser1xb}{size=+12}If u do, ur hands will start shaking and u'll faint eventually.{size=+12}{/=ser1xb}"
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
    show earlyMorn at shake
    
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
            s "{image=seven wow}" (img=True)
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
            show earlyMorn at shake
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
    s "general_cg1" (img=True)
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
            y "{image=yoosung cry}" (img=True)
            
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
                    
                    # This is the 'heartbreak' animation; call it the same way you
                    # would a heart icon except use heart_break(y) instead of heart_icon(y)
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
    
    y "{image=yoosung cry}" (img=True)
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
    s "{image=seven yoohoo}" (img=True)
    
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
    y "{image=yoosung cry}" (img=True)
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
            
    # Similar to the 'enter' function, call this when a character leaves the chatroom
    # Passing it the name of the character will cause it to display '707 has left the chatroom.'
    call exit(s)
    y "{=curly}T_T What am I gonna do...{/=curly}"
    y "{=curly}[name]...{/=curly}"
    y "{=curly}If I faint and don't wake up...{/=curly}"
    y "{=curly}Can u wake me up with a... a.. a kiss?{/=curly}" (bounce=True)
    y "{=curly}I'm not trying to be weird.{/=curly}"
    y "{=curly}I just want to wake up and help open the party...{/=curly}"
    
    call answer
    menu coffee_last:
        # Note that this menu has three options; you can add as many as you like,
        # but the screen only has room for 5 different options so if you want more
        # you'll need to split it up into multiple menus with a Back/Next option
        # (see Example Chat.rpy for some examples of this)
        "Don't worry... Even if you don't wake up the party will be a success.":
            m "{=sser2}Don't worry... Even if you don't wake up the party will be a success.{/=sser2}" (pauseVal=0)
            y "{image=yoosung puff}" (img=True)
            y "{=curly}{size=+5}Do you mean that?{/=curly}"
            y "{=curly}I'm hurt...{/=curly}"
            call heart_break(y)
        "I'll wake you up...":
            m "I'll wake you up..." (pauseVal=0)
            y "Oh...! Thank you." (bounce=True)
            call heart_icon(y)
            y "{image=yoosung happy}" (img=True)
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
    
    # Call this to end the chat and return to the main menu
    call save_exit
    return

    
# Put anything you want to have happen after the chatroom ends here, 
# like text messages, phone calls or (in the future) emails. You'll have to call
# this label whatever you've defined the afterchat_label to be when setting
# up the chat_archive
label after_coffee_chat:

    python: 
        ## Seven's text message
        addtext (s, "Thanks for not spoiling the secret~ ^^", s)
        addtext (s, "You're a lot of fun to talk to meow!", s)
        # This is the name of the label to jump to when you reply to Seven's
        # text message. You can leave this out if you don't want the player
        # to be able to reply anymore
        add_reply_label(s, 'coffee1')
        
        ## Yoosung's text message
        addtext (y, "[name]... what do I do...", y)
        add_reply_label(y, 'coffee2')
        
        ## Zen's Phone Call (incoming)
        # It takes a character, the name of the label to jump to for the phone
        # call, the title of the call (eventually this will be displayed in the History
        # section) and the type of call (in this case, incoming)
        incoming_call = Phone_Call(z, 'coffee_phone_zen', "Did you sleep well?", 'incoming')
        
        ## Yoosung's Phone Call (outgoing)
        # You'll always want to append calls to this list so it doesn't overwrite
        # previous calls
        available_calls.append(Phone_Call(y, 'coffee_phone_yoosung', 'I must drink chocolate milk...', 'outgoing'))
    
        ## Set everyone else's voicemails appropriately
        # (In this case, everyone gets the same label)
        # The different voicemails are defined in phone screen.rpy
        for char in character_list:
            char.update_voicemail = 'voicemail_1'
    
    return
    
## This is the label you jump to for the phone call with Zen
label coffee_phone_zen:
    # Call this before the phone call begins
    call phone_begin
    
    z_phone "Good morning, hon~"
    z_phone "Gahh~ (Stretches) I haven't slept this well in a while. I feel really good."
    z_phone "When I don't sleep that well, just moving my neck in the morning can hurt."
    z_phone "Did you sleep well?"
    
    menu:
        # If you want the previous dialogue to show up behind the choice menu,
        # you'll need to copy the last line of dialogue here, right after the menu
        z_phone "Did you sleep well?"
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
    
    # Call this when the call is finished
    call phone_end
    
## This is the label you jump to for the phone call with Yoosung
label coffee_phone_yoosung:
    
    call phone_begin
    
    y_phone "I have not died."
    y_phone "I will not die."
    y_phone "To live, I must drink chocolate milk..."
    
    menu:
        y_phone "To live, I must drink chocolate milk..."
        "The ones who wish to live will die and those who wish to die will live!":
            m_phone "The ones who wish to live will die and those who wish to die will live!"
            y_phone "Uh-uh I know there's a super intelligent saying on that!"
            y_phone "What was it...!!!!! I think Shakespears said it."
            y_phone "Whatever... noo... that's not what's important..."
        "Yoo-Yoosung?":
            m_phone "Yoo-Yoosung?"
            y_phone "nooooooooooooooooooooooooo"
            y_phone "haaaaaaaaaaaaaaaaaaaaarggh"
            
    y_phone "I went to the convenience store but I didn't bring my loyalty card so I didn't get a discount on the chocolate milk."
    y_phone "This is a bad sign!!!"
    y_phone "Huahhhh......"
    y_phone "noooooooooooooo....."
    y_phone "I'm sorry... I can't talk to you right now."
    y_phone "My heart's about to explode..."
    y_phone "Even if you don't hear from me... it'll be fine..."
    y_phone "Even if I faint, I'll faint at home."
    y_phone "...Even if I faint... I'll resurrect myself..."
    y_phone "Please... God of Games... Let me play LOLOL tonight..."
    y_phone "Please cure me of this strange disease...!!!"
    y_phone "I... (sniffling) I have to go wipe off my snot. Bye..."    
    
    call phone_end
 
    
## This should be the label you told the program to go to if they
## reply to a text message (in this case, Seven's text)
label coffee1():

    menu:
        "I like talking to you too meow!":
            $ addtext (m, "I like talking to you too meow!", s)
            # This will award the player a heart point when they view the message reply
            # You'll need to pass it the variable of the character whose conversation you're viewing
            $ add_heart(s)
            $ addtext (s, "<3 <3 <3", s)
            $ addtext (s, "Agent 707 will do his best to come to the chatroom more often meow!", s)
        
        "I feel bad for Yoosung though...":
            $ addtext (m, "I feel bad for Yoosung though...", s)
            # If you want to give the player a different heart point than the person whose
            # conversation you're viewing, pass it as a second argument like this
            $ add_heart(s, y)
            $ addtext (s, "Nah~ he'll be fine", s)
            $ addtext (s, "I'm sure he'd be happy you're worried for him tho lolol", s)

    $ renpy.retain_after_load()
    return
    
## This is the label to go to when replying to Yoosung's message
label coffee2():
    
    menu:
        "Drink that chocolate milk!":
            $ addtext (m, "Drink that chocolate milk!", y)
            $ add_heart(y)
            $ addtext (y, "I will!! I bought a lot of it...", y)
            $ addtext (y, "It could be worse... I could've had classes tomorrow T_T", y)
            $ addtext (y, "Thanks for worrying.", y)
        
        "You do know Seven's just teasing, right?":
            $ addtext (m, "You do know Seven's just teasing, right?", y)
            $ addtext (y, "I appreciate you trying to comfort me but...", y)
            $ addtext (y, "You saw the news article he posted, right?", y)
            $ addtext (y, "And he really does keep track of all the members...", y)
            $ addtext (y, "I'm sure it's not a lie.", y)

    $ renpy.retain_after_load()
    return
    
    
    
    
    
    
    
    
    