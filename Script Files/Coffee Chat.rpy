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
    
    call answer
    menu:
        "Do you still feel tired?":
            # Note that MC's responses have a pv value of 0 after a menu
            # Both 'branches' have several lines of dialogue before they 'rejoin' later
            m "Do you still feel tired?" (pauseVal=0)
            s "No way."
            s "One of my strengths is that I feel completely refreshed after sleeping" (bounce=True, specBubble="cloud_l")
        "Seven, get a good night's rest?":
            m "{=sser2}Seven, get a good night's rest?{/=sser2}" (pauseVal=0)
            s "{=sser2}Heya [name]{/=sser2}"
            
            # You have to call heart icons yourself. Just pass it the variable
            # of the name of the character whose heart icon you want
            # (variables.rpy has the variable names if you're not sure)
            call heart_icon('s')
            s "{=sser2}Ya. Slept like a rock.{/=sser2}"
            
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
            call heart_icon('s')
        "You should play games.":
            m "You should play games." (pauseVal=0)
            s "{=sser1}o_o Game??{/=sser1}"
            s "lol"
            s "{=sser1}I'd rather make one. Playing it gets boring pretty fast lol{/=sser1}"
    s "{=sser1}Hmm.{/=sser1}"
    s "{size=+12}I summon Yoosung! Abracadabra{/size}" (bounce=True, specBubble="spike_l")
    msg "Yoosung★ has entered the chatroom"
    
    call answer
    menu:
        "Yoosung~ I missed you.":
            m "Yoosung~ I missed you." (pauseVal=0)
            y "Thanks for being so welcoming."
            call heart_icon('y')
            y "Hello ^^"
        "Omg. He really came.":
            m "Omg. He really came." (pauseVal=0)
            s "heya"
            call heart_icon('s')
            y "Hmm?"
            y "{=sser1}I smell a trap somewhere...{/=sser1}"
            
    s "{=sser1}What were u doing?{/=sser1}"
    s "{=sser1}So late at night lol{/=sser1}"
    y "{=sser1}I was just about to drink a cup of coffee and play games.{/=sser1}"
    y "{=sser1}I started learning how to brew coffee from a club yesterday.{/=sser1}"
    s "Coffee...?"
    s "Ur learning how to make coffee...???"
    y "Yup ^^"
    s "{=ser1}No way. U can't.{/=ser1}"
    y "What?"
    s "{=ser1}{size=+12}Did you already drink the coffee!?!?!?!?{/size}{/=ser1}"
    y "{=sser1}Yeah... Why?{/=sser1}"
    
    # Another play statement will automatically "override" the previous play statement
    # and only one set of background music will play on the music channel at once
    play music dark_secret loop
    s "{=ser1b}Big trouble...{/=ser1b}"
    y "{=sser1}What trouble?{/=sser1}"
    s "{=ser1}It's...{/=ser1}"
    
    call answer
    menu:
        "Yoosung... what do we do now?":
            m "Yoosung... what do we do now?" (pauseVal=0)
            y "Why?"
            y "{=sser2}Did something happen?{/=sser2}"
            s "{=ser1}Gah... I was about to tell [name].{/=ser1}"
        "What's big trouble?":
            m "What's big trouble?" (pauseVal=0)
            y "{=sser1}Yeah. What is it?{/=sser1}"
            s "{=ser1}It's...{/=ser1}"
            
    s "{=ser1}So, I check the health reports of all the members...{/=ser1}"
    y "{size=+12}Okay... Ur not saying that I can't dringak coffxee, r u?{/size}"
    y "*drink coffee?"
    
    call answer
    menu:
        "Ya. U'll be in trouble if u drink coffee.":
            m "Ya. U'll be in trouble if u drink coffee." (pauseVal=0)
            s "Ya..."
            call heart_icon('s')
            s "{size=+12}U can never ever!!! drink coffee.{/size}"
            s "Seeing ur typos above, it seems like ur symptoms are showing already."
        "Seven's just messing around lol":
            m "Seven's just messing around lol" (pauseVal=0)
            y "{=sser1}Right? lolol{/=sser1}"
            call heart_icon('y')
            s "{=ser1xb}Not joking.{/=ser1xb}"
            s "{=ser1}I'm dead serious.{/=ser1}"
            y "Puppy food?"
            
            # This is a nested menu; note the indentation levels. You'll only see this menu
            # if you choose 'Seven's just messing around lol' in the previous menu
            call answer
            menu:
                "-_-":
                    m "-_-" (pauseVal=0)
                    s "Cat food is serious meow"
                    y "I have no idea what ur saying."
                "lolololol":
                    m "lolololol" (pauseVal=0)
                    s "{=ser1b}This is funny to u?{/=ser1b}"
                    y "lololololol"                   
    
    s "{=ser1xb}U can never ever!!! drink coffee.{/=ser1xb}" (bounce=True, specBubble="spike_m")
    s "{=ser1xb}{size=+12}If u do, ur hands will start shaking and u'll faint eventually.{size=+12}{/=ser1xb}"
    y "{=sser1}Nah{/=sser1}"
    y "{=sser1}I don't have that kind of allergy.{/=sser1}"
    y "{=sser1}No way~{/=sser1}"
    s "..."
    s "{=ser1}I'm sorry.{/=ser1}"
    s "{=ser1}U've already lost trust in me.{/=ser1}"
    s "{=ser1}so u r not listening.{/=ser1}"
    y "?"
    y "{=sser1}For real?{/sser1}"
    s "{=ser1xb}Ur gonna faint. For real.{/=ser1xb}"
    y "Seriously?? Ur kidding right?" (bounce=True, specBubble="spike_m")
    
    # This is the shake animation; it plays during the previous line of dialogue
    show earlyMorn at shake
    
    call answer
    menu:
        "You should prepare yourself.":
            m "You should prepare yourself." (pauseVal=0)
            s "{=sser1}Ya. Go prepare to faint.{/=sser1}"
            call heart_icon('s')
        "I think fainting is a bit too much...":
            m "I think fainting is a bit too much..." (pauseVal=0)
            y "What?"
            y "{=sser1}What do u mean?{/=sser1}"
            s "Shh."
            s "{image=seven wow}" (img=True)
            s "{=ser1}Listen carefully.{/=ser1}"
            
    s "{=ser1b}You are going to faint today.{/=ser1}"
    s "{=ser1}And there's a chance you might never wake up again...{/=ser1}"
    y "{=sser1}{size=+12}Why!?{/size}{/=sser1}" (bounce=True, specBubble="spike_s")
    s "{=ser1b}You have the \"Pass Out After Drinking Caffeine Syndrome\"{/=ser1b}"
    y "{=sser1}??? What is that?{/=sser1}"
    y "{=sser1}I don't understand what you mean.{/=sser1}"
    y "{size=+12}A disease like that actually exists?!{/size}"
    
    call answer
    menu:
        "Ya. It exists":
            m "Ya. It exists" (pauseVal=0)
            y "{=sser1b}!!{/=sser1b}" 
            show earlyMorn at shake
            s "{=sser1}Ya{/=sser1}"
            call heart_icon('s')
        "Whoever named it is a bit...;;":
            m "Whoever named it is a bit...;;" (pauseVal=0)
            s "{=blocky}It was made up at the last min so no choice.{/=blocky}"
            y "What do u mean made up at the last min?!" (bounce=True, specBubble="spike_m")
            s "{size=+12}Your artificial heart{/size}"
            y "Stop saying weird things;;"
            y "Seven, ur joking right?" (bounce=True, specBubble="spike_m")
            s "{=sser1}I am doing whatever I can to save u.{/=sser1}"
            
    s "{=sser2}...Don't get so surprised.{/=sser2}"
    y "{=sser1}Okay...{/=sser1}"
    s "The disease called \"Pass Out After Drinking Caffeine Syndrome\""
    s "{=ser1b}It{/=ser1b}" (pauseVal=0.2)
    s "{=ser1b}exists{/=ser1b}" (pauseVal=0.2)
    s "{=ser1b}for sure{/=ser1b}" (pauseVal=0.3)
    s "{=sser1}I look at foreign reports every day.{/=sser1}"
    s "general_cg1" (img=True)
    y "{=sser1b}{size=+12}!!!{/size}{/=sser1b}"
    s "{=ser1}...It's a rare disease.{/=ser1}"
    
    call answer
    menu:
        "Last year there were about 1024 deaths in the country...":
            m "Last year there were about 1024 deaths in the country..." (pauseVal=0)
            s "Oh! That number's nice. It's the 10th multiple of 2."
            call heart_icon('s')
            y "Omg. Can't believe I have such a serious disease T_T"
            y "I'm so svchoecked to type pertoperly T_T"
        "What's wrong with the name lolololol A disease called Drink Caffeine and Faint lololol":
            m "What's wrong with the name lolololol A disease called Drink Caffeine and Faint lololol" (pauseVal=0)
            y "lololol I know... It is funny T_T"
            call heart_icon('y')
            y "But I can't believe I have it."
            y "{image=yoosung cry}" (img=True)
            
    y "{size=+12}What's going to happen to me T_T{/size}"
    y "{size=+12}Am I gonna faint soon???{/size}"
    s "{=sser1}According to my data{/=sser1}"
    s "{=sser1}u'll faint some time between 9 and 10.{/=sser1}"
    y "T_T..."
    y "{=sser1}I guess it could have been worse. I don't have class in the morning.{/=sser1}"
    
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
                    call heart_break('y')
                    y "{=curly}I thought u were crying by sweating{/=curly}"
                "T_T. You have to return.":
                    m "T_T. You have to return." (pauseVal=0)
                    y "{=curly}Yup T_T I will return!!{/=curly}"
                    call heart_icon('y')
                    s "Gahh... Tears r blocking my sight."
                    
        "A stroke of good luck in this misfortune":
            m "A stroke of good luck in this misfortune" (pauseVal=0)
            y "{=sser1}I should at least pass out at home T_T{/=sser1}"
            s "{=sser1}Ya{/=sser1}"
            call heart_icon('s')
    
    y "{image=yoosung cry}" (img=True)
    y "{=sser1}Thanks for telling me Seven.{/=sser1}"
    s "lol It's nothing."
    
    call answer
    menu:
        "Call Seven if something happens.":
            m "Call Seven if something happens." (pauseVal=0)
            s "Ya. I'll always be here for u ^^"
            call heart_icon('s')
            y "{=sser1}Thank you T_T{/=sser1}"
        "Call me if anything happens":
            m "Call me if anything happens" (pauseVal=0) 
            y "Okay. Thank you so much T_T"
            call heart_icon('y')
            
    s "Oh."
    s "{=sser2}I recommend drinking chocolate milk before u faint.{/=sser2}"
    s "{=sser2}U have to increase ur blood pressure if u want to wake up faster.{/=sser2}"
    s "I'm worried...T_T"
    y "Okay..."
    y "{=sser1}Thank you. [name], you too...{/=sser1}"
    s "{image=seven yoohoo}" (img=True)
    
    call answer
    menu:
        "^^;;;":
            m "^^;;;" (pauseVal=0)
            y "{=sser1}Why do u keep sweating...?{/=sser1}"
            y "U must be really worried for me."
            y "{=sser1}{size=+12}I'm touched!!{/size}{/=sser1}"
            call heart_icon('y')
        "No need ^^":
            m "No need ^^" (pauseVal=0) 
            y "{=sser1}I should know my body better.{/=sser1}"
            y "{=sser1}Never knew I had something like this...{/=sser1}"
            y "{=sser1}It's confusing but...{/=sser1}"
            y "I'll deal with it wisely."
            s "{=sser1}Ya. Dealing with it wisely is the way to go.{/=sser1}"
            
    s "...I'm glad to be of help."
    s "Ur young, so u'll wake up quickly if u do faint, so don't worry too much."
    y "{=curly}Okay...{/=curly}"
    y "{=curly}I shouldn't drink coffee anymore.{/=curly}"
    s "{=sser1}Oh... I got work again.{/=sser1}"
    s "Arrgghh!! Stress!!!" (bounce=True, specBubble="spike_m")
    y "Both Jumin and u"
    y "{=sser1}u guys r buried with work{/=sser1}"
    y "{image=yoosung cry}" (img=True)
    s "{=sser1}Can't do anything about it...{/=sser1}"
    s "{=sser1}Then I'll get going.{/=sser1}"
    y "{=sser1}Yup!{/=sser1}"
    y "{=sser1}Have a good night!!{/=sser1}"
    s "{=sser1}{size=+12}lol{/size}{/=sser1}"
    
    call answer
    menu:
        "Seven, look out for my health too":
            m "Seven, look out for my health too" (pauseVal=0)
            s "U can trust me...^^"
            call heart_icon('s')
            y "That's good thinking... [name]."
        ";;;":
            m ";;;" (pauseVal=0) 
            s "Then bye~!"
            
    msg "707 has left the chatroom."
    y "{=curly}T_T What am I gonna do...{/=curly}"
    y "{=curly}[name]...{/=curly}"
    y "{=curly}If I faint and don't wake up...{/=curly}"
    y "{=curly}Can u wake me up with a... a.. a kiss?{/=curly}" (bounce=True)
    y "{=curly}I'm not trying to be weird.{/=curly}"
    y "{=curly}I just want to wake up and help open the party...{/=curly}"
    
    call answer
    menu:
        # Note that this menu has three options; you can add as many as you like,
        # but the screen only has room for 5 different options so if you want more
        # you'll need to split it up into multiple menus with a Back/Next option
        # (see Example Chat.rpy for some examples of this)
        "Don't worry... Even if you don't wake up the party will be a success.":
            m "Don't worry... Even if you don't wake up the party will be a success." (pauseVal=0)
            y "{image=yoosung puff}" (img=True)
            y "{=curly}{size=+5}Do you mean that?{/=curly}"
            y "{=curly}I'm hurt...{/=curly}"
            call heart_break('y')
        "I'll wake you up...":
            m "I'll wake you up..." (pauseVal=0)
            y "{=sser1}Oh...! Thank you.{/=sser1}" (bounce=True)
            call heart_icon('y')
            y "{image=yoosung happy}" (img=True)
        "Seven is just playing with you lolol":
            m "Seven is just playing with you lolol" (pauseVal=0)
            y "I know that ur worried too"
            y "and don't want to believe what Seven said."
            y "But Seven's probably right."
            y "Seven is really knowledgeable."
            y "He once knew when my cold would get better."
            y "He said it'd be between the 3rd and 7th day"
            y "And it completely went away on the fifth day."
            y "Look at that image above..."
            y "I'm sure it's not a lie."
            
    y "First, I should get some chocolate milk..."
    y "I'm gonna go to the supermarket~!"
    msg "Yoosung★ has left the chatroom."
    
    # Call this to end the chat and return to the main menu
    call save_exit
