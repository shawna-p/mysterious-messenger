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
            $ addchat(m,"Do you still feel tired?",0)
            $ addchat(s,"No way.",pv)
            $ addchat(s,"One of my strengths is that I feel completely refreshed after sleeping",pv,False,True, "cloud_l")
        "Seven, get a good night's rest?":
            $ addchat("MC", "{=sser2}Seven, get a good night's rest?{/=sser2}", 0)
            $ addchat("Sev", "{=sser2}Heya [name]{/=sser2}", pv)
            # You have to call heart icons yourself. Just pass it the variable
            # of the name of the character whose heart icon you want
            # (variables.rpy has the variable names if you're not sure)
            call heart_icon(s)
            $ addchat("Sev", "{=sser2}Ya. Slept like a rock.{/=sser2}", pv)
    $ addchat("Sev", "{=sser2}I don't feel tired physically...{/=sser2}", pv)
    $ addchat("Sev", "{=sser2}But{/=sser2}", pv)
    $ addchat("Sev", "{=sser1xb}{size=+12}mentally, my stress level is MAX{/size}{/=sser1xb}",pv)
    $ addchat("Sev", "{image=seven huff}", pv, True)
    $ addchat("Sev", "{=sser1xb}How do I get rid of this stress...?!{/=sser1xb}",pv, False, True, "spike_m")
    
    call answer
    menu:
        "Just take it out on Yoosung.":
            $ addchat("MC", "Just take it out on Yoosung.",0)
            $ addchat("Sev", "{=sser2}[name]...{/=sser2}",pv)
            $ addchat("Sev", "{=sser2}Ur pretty smart lol{/=sser2}",pv,False,True,"cloud_m")
            call heart_icon(s)
        "You should play games.":
            $ addchat("MC", "You should play games.", 0)
            $ addchat(s, "{=sser1}o_o Game??{/=sser1}",pv)
            $ addchat(s,"lol",pv)
            $ addchat(s,"{=sser1}I'd rather make one. Playing it gets boring pretty fast lol{/=sser1}",pv)
    $ addchat("Sev", "{=sser1}Hmm.{/=sser1}",pv)
    $ addchat(s,"{size=+12}I summon Yoosung! Abracadabra{/size}",pv, False, True, "spike_l")
    $ addchat("msg", "Yoosung★ has entered the chatroom",pv)
    
    call answer
    menu:
        "Yoosung~ I missed you.":
            $ addchat("MC", "Yoosung~ I missed you.",0)
            $ addchat(y,"Thanks for being so welcoming.",pv)
            call heart_icon(y)
            $ addchat(y,"Hello ^^",pv)
        "Omg. He really came.":
            $ addchat("MC","Omg. He really came.",0)
            $ addchat("Sev", "heya",pv)
            call heart_icon(s)
            $ addchat("Yoo", "Hmm?",pv)
            $ addchat("Yoo", "{=sser1}I smell a trap somewhere...{/=sser1}",pv)
    $ addchat("Sev", "{=sser1}What were u doing?{/=sser1}",pv)
    $ addchat('Sev', "{=sser1}So late at night lol{/=sser1}",pv)
    $ addchat("Yoo", "{=sser1}I was just about to drink a cup of coffee and play games.{/=sser1}",pv)
    $ addchat("Yoo", "{=sser1}I started learning how to brew coffee from a club yesterday.{/=sser1}",pv)
    $ addchat("Sev", "Coffee...?",pv)
    $ addchat("Sev", "Ur learning how to make coffee...???",pv)
    $ addchat(y, "Yup ^^",pv)
    $ addchat(s, "{=ser1}No way. U can't.{/=ser1}",pv)
    $ addchat(y, "What?",pv)
    $ addchat(s,"{=ser1}{size=+12}Did you already drink the coffee!?!?!?!?{/size}{/=ser1}",pv)
    $ addchat(y,"{=sser1}Yeah... Why?{/=sser1}",pv)
    # Another play statement will automatically "override" the previous play statement
    # and only one set of background music will play on the music channel at once
    play music dark_secret loop
    $ addchat(s,"{=ser1b}Big trouble...{/=ser1b}",pv)
    $ addchat(y,"{=sser1}What trouble?{/=sser1}",pv)
    $ addchat(s,"{=ser1}It's...{/=ser1}",pv)
    
    call answer
    menu:
        "Yoosung... what do we do now?":
            $ addchat(m,"Yoosung... what do we do now?",0)
            $ addchat(y,"Why?",pv)
            $ addchat(y,"{=sser2}Did something happen?{/=sser2}",pv)
            $ addchat(s,"{=ser1}Gah... I was about to tell [name].{/=ser1}",pv)
        "What's big trouble?":
            $ addchat(m,"What's big trouble?",0)
            $ addchat(y,"{=sser1}Yeah. What is it?{/=sser1}",pv)
            $ addchat(s,"{=ser1}It's...{/=ser1}",pv)
    $ addchat(s,"{=ser1}So, I check the health reports of all the members...{/=ser1}",pv)
    $ addchat(y,"{size=+12}Okay... Ur not saying that I can't dringak coffxee, r u?{/size}",pv)
    $ addchat(y,"*drink coffee?",pv)
    
    call answer
    menu:
        "Ya. U'll be in trouble if u drink coffee.":
            $ addchat(m,"Ya. U'll be in trouble if u drink coffee.",0)
            $ addchat(s,"Ya...",pv)
            call heart_icon(s)
            $ addchat(s,"{size=+12}U can never ever!!! drink coffee.{/size}",pv)
            $ addchat(s,"Seeing ur typos above, it seems like ur symptoms are showing already.",pv)
        "Seven's just messing around lol":
            $ addchat(m,"Seven's just messing around lol",0)
            $ addchat(y,"{=sser1}Right? lolol{/=sser1}",pv)
            call heart_icon(y)
            $ addchat(s,"{=ser1xb}Not joking.{/=ser1xb}",pv)
            $ addchat(s,"{=ser1}I'm dead serious.{/=ser1}",pv)
            $ addchat(y,"Puppy food?",pv)
            
            # This is a nested menu; note the indentation levels. You'll only see this menu
            # if you choose 'Seven's just messing around lol' in the previous menu
            call answer
            menu:
                "-_-":
                    $ addchat(m,"-_-",0)
                    $ addchat(s, "Cat food is serious meow",pv)
                    $ addchat(y,"I have no idea what ur saying.",pv)
                "lolololol":
                    $ addchat(m,"lolololol",0)
                    $ addchat(s,"{=ser1b}This is funny to u?{/=ser1b}",pv)
                    $ addchat(y,"lololololol",pv)                   
    
    $ addchat(s,"{=ser1xb}U can never ever!!! drink coffee.{/=ser1xb}",pv, False, True, "spike_m")
    $ addchat(s,"{=ser1xb}{size=+12}If u do, ur hands will start shaking and u'll faint eventually.{size=+12}{/=ser1xb}",pv)
    $ addchat(y,"{=sser1}Nah{/=sser1}",pv)
    $ addchat(y,"{=sser1}I don't have that kind of allergy.{/=sser1}",pv)
    $ addchat(y,"{=sser1}No way~{/=sser1}",pv)
    $ addchat(s,"...",pv)
    $ addchat(s,"{=ser1}I'm sorry.{/=ser1}",pv)
    $ addchat(s,"{=ser1}U've already lost trust in me.{/=ser1}",pv)
    $ addchat(s,"{=ser1}so u r not listening.{/=ser1}",pv)
    $ addchat(y,"?",pv)
    $ addchat(y,"{=sser1}For real?{/sser1}",pv)
    $ addchat(s,"{=ser1xb}Ur gonna faint. For real.{/=ser1xb}",pv)
    $ addchat(y,"Seriously?? Ur kidding right?",pv, False, True, "spike_m")
    show earlyMorn at shake
    
    call answer
    menu:
        "You should prepare yourself.":
            $ addchat(m,"You should prepare yourself.",0)
            $ addchat(s,"{=sser1}Ya. Go prepare to faint.{/=sser1}",pv)
            call heart_icon(s)
        "I think fainting is a bit too much...":
            $ addchat(m,"I think fainting is a bit too much...",0)
            $ addchat(y,"What?",pv)
            $ addchat(y,"{=sser1}What do u mean?{/=sser1}",pv)
            $ addchat(s,"Shh.",pv)
            $ addchat(s,"{image=seven wow}",pv,True)
            $ addchat(s,"{=ser1}Listen carefully.{/=ser1}",pv)
    $ addchat(s,"{=ser1b}You are going to faint today.{/=ser1}",pv)
    $ addchat(s,"{=ser1}And there's a chance you might never wake up again...{/=ser1}",pv)
    $ addchat(y,"{=sser1}{size=+12}Why!?{/size}{/=sser1}",pv,False, True, "spike_s")
    $ addchat(s,"{=ser1b}You have the \"Pass Out After Drinking Caffeine Syndrome\"{/=ser1b}",pv)
    $ addchat(y,"{=sser1}??? What is that?{/=sser1}",pv)
    $ addchat(y,"{=sser1}I don't understand what you mean.{/=sser1}",pv)
    $ addchat(y,"{size=+12}A disease like that actually exists?!{/size}",pv)
    
    call answer
    menu:
        "Ya. It exists":
            $ addchat(m,"Ya. It exists",0)
            $ addchat(y,"{=sser1b}!!{/=sser1b}",pv) 
            show earlyMorn at shake
            $ addchat(s,"{=sser1}Ya{/=sser1}",pv)
            call heart_icon(s)
        "Whoever named it is a bit...;;":
            $ addchat(m,"Whoever named it is a bit...;;",0)
            $ addchat(s,"{=blocky}It was made up at the last min so no choice.{/=blocky}",pv)
            $ addchat(y,"What do u mean made up at the last min?!",pv,False,True,"spike_m")
            $ addchat(s,"{size=+12}Your artificial heart{/size}",pv)
            $ addchat(y,"Stop saying weird things;;",pv)
            $ addchat(y,"Seven, ur joking right?",pv,False,True,"spike_m")
            $ addchat(s,"{=sser1}I am doing whatever I can to save u.{/=sser1}",pv)
    $ addchat(s, "{=sser2}...Don't get so surprised.{/=sser2}",pv)
    $ addchat(y,"{=sser1}Okay...{/=sser1}",pv)
    $ addchat(s, "The disease called \"Pass Out After Drinking Caffeine Syndrome\"",pv)
    $ addchat(s, "{=ser1b}It{/=ser1b}",0.2*pv)
    $ addchat(s, "{=ser1b}exists{/=ser1b}",0.2*pv)
    $ addchat(s, "{=ser1b}for sure{/=ser1b}",0.3*pv)
    $ addchat(s,"{=sser1}I look at foreign reports every day.{/=sser1}",pv)
    $ addchat(s,"{image=cg1-small}",pv,True)
    $ addchat(y,"{=sser1b}{size=+12}!!!{/size}{/=sser1b}",pv)
    $ addchat(s,"{=ser1}...It's a rare disease.{/=ser1}",pv)
    
    call answer
    menu:
        "Last year there were about 1024 deaths in the country...":
            $ addchat(m,"Last year there were about 1024 deaths in the country...",0)
            $ addchat(s,"Oh! That number's nice. It's the 10th multiple of 2.",pv)
            call heart_icon(s)
            $ addchat(y,"Omg. Can't believe I have such a serious disease T_T",pv)
            $ addchat(y,"I'm so svchoecked to type pertoperly T_T",pv)
        "What's wrong with the name lolololol A disease called Drink Caffeine and Faint lololol":
            $ addchat(m,"What's wrong with the name lolololol A disease called Drink Caffeine and Faint lololol",0)
            $ addchat(y,"lololol I know... It is funny T_T",pv)
            call heart_icon(y)
            $ addchat(y,"But I can't believe I have it.",pv)
            $ addchat (y,"{image=yoosung cry}",pv,True)
    $ addchat(y,"{size=+12}What's going to happen to me T_T{/size}",pv)
    $ addchat(y,"{size=+12}Am I gonna faint soon???{/size}",pv)
    $ addchat(s,"{=sser1}According to my data{/=sser1}",pv)
    $ addchat(s,"{=sser1}u'll faint some time between 9 and 10.{/=sser1}", pv)
    $ addchat(y,"T_T...",pv)
    $ addchat(y,"{=sser1}I guess it could have been worse. I don't have class in the morning.{/=sser1}",pv)
    
    call answer
    menu:
        "^^;;":
            $ addchat(m,"^^;;",0)
            $ addchat(y,"{=curly}Don't cry, [name].{/=curly}",pv)
            $ addchat(y,"{=curly}Even if I do faint... I'll be able to wake up.{/=curly}",pv)
            
            call answer
            menu:
                "I wasn't crying.":
                    $ addchat(m,"I wasn't crying.",0)
                    $ addchat(y,"{=curly}I read the emoji wrong T_T{/=curly}",pv)
                    $ addchat(y,"{=curly}I thought u were crying by sweating{/=curly}",pv)
                "T_T. You have to return.":
                    $ addchat(m,"T_T. You have to return.",0)
                    $ addchat(y,"{=curly}Yup T_T I will return!!{/=curly}",pv)
                    call heart_icon(y)
                    $ addchat(s,"Gahh... Tears r blocking my sight.",pv)
        "A stroke of good luck in this misfortune":
            $ addchat(m,"A stroke of good luck in this misfortune",0)
            $ addchat(y,"{=sser1}I should at least pass out at home T_T{/=sser1}",pv)
            $ addchat(s,"{=sser1}Ya{/=sser1}",pv)
            call heart_icon(s)
    
    $ addchat(y,"{image=yoosung cry}",pv,True)
    $ addchat(y,"{=sser1}Thanks for telling me Seven.{/=sser1}",pv)
    $ addchat(s,"lol It's nothing.",pv)
    
    call answer
    menu:
        "Call Seven if something happens.":
            $ addchat(m,"Call Seven if something happens.",0)
            $ addchat(s,"Ya. I'll always be here for u ^^",pv)
            call heart_icon(s)
            $ addchat(y,"{=sser1}Thank you T_T{/=sser1}",pv)
        "Call me if anything happens":
            $ addchat(m,"Call me if anything happens",0) 
            $ addchat(y,"Okay. Thank you so much T_T",pv)
            call heart_icon(y)
    $ addchat(s,"Oh.",pv)
    $ addchat(s,"{=sser2}I recommend drinking chocolate milk before u faint.{/=sser2}",pv)
    $ addchat(s,"{=sser2}U have to increase ur blood pressure if u want to wake up faster.{/=sser2}",pv)
    $ addchat(s,"I'm worried...T_T",pv)
    $ addchat(y,"Okay...",pv)
    $ addchat(y,"{=sser1}Thank you. [name], you too...{/=sser1}",pv)
    $ addchat(s,"{image=seven yoohoo}",pv,True)
    
    call answer
    menu:
        "^^;;;":
            $ addchat(m,"^^;;;",0)
            $ addchat(y,"{=sser1}Why do u keep sweating...?{/=sser1}",pv)
            $ addchat(y,"U must be really worried for me.",pv)
            $ addchat(y,"{=sser1}{size=+12}I'm touched!!{/size}{/=sser1}",pv)
            call heart_icon(y)
        "No need ^^":
            $ addchat(m,"No need ^^",0) 
            $ addchat(y,"{=sser1}I should know my body better.{/=sser1}",pv)
            call heart_icon(y)
            $ addchat(y,"{=sser1}Never knew I had something like this...{/=sser1}",pv)
            $ addchat(y,"{=sser1}It's confusing but...{/=sser1}",pv)
            $ addchat(y,"I'll deal with it wisely.",pv)
            $ addchat(s,"{=sser1}Ya. Dealing with it wisely is the way to go.{/=sser1}",pv)
    $ addchat(s,"...I'm glad to be of help.",pv)
    $ addchat(s,"Ur young, so u'll wake up quickly if u do faint, so don't worry too much.",pv)
    $ addchat(y,"{=curly}Okay...{/=curly}",pv)
    $ addchat(y,"{=curly}I shouldn't drink coffee anymore.{/=curly}",pv)
    $ addchat(s,"{=sser1}Oh... I got work again.{/=sser1}",pv)
    $ addchat(s,"Arrgghh!! Stress!!!",pv,False,True,"spike_m")
    $ addchat(y,"Both Jumin and u",pv)
    $ addchat(y,"{=sser1}u guys r buried with work{/=sser1}",pv)
    $ addchat(y,"{image=yoosung cry}",pv,True)
    $ addchat(s,"{=sser1}Can't do anything about it...{/=sser1}",pv)
    $ addchat(s,"{=sser1}Then I'll get going.{/=sser1}",pv)
    $ addchat(y,"{=sser1}Yup!{/=sser1}",pv)
    $ addchat(y,"{=sser1}Have a good night!!{/=sser1}",pv)
    $ addchat(s,"{=sser1}{size=+12}lol{/size}{/=sser1}",pv)
    
    call answer
    menu:
        "Seven, look out for my health too":
            $ addchat(m,"Seven, look out for my health too",0)
            $ addchat(s,"U can trust me...^^",pv)
            call heart_icon(s)
            $ addchat(y,"That's good thinking... [name].",pv)
        ";;;":
            $ addchat(m,";;;",0) 
            $ addchat(s,"Then bye~!",pv)
    $ addchat("msg","707 has left the chatroom.",pv)
    $ addchat(y,"{=curly}T_T What am I gonna do...{/=curly}",pv)
    $ addchat(y,"{=curly}[name]...{/=curly}",pv)
    $ addchat(y,"{=curly}If I faint and don't wake up...{/=curly}",pv)
    $ addchat(y,"{=curly}Can u wake me up with a... a.. a kiss?{/=curly}",pv, False,True)
    $ addchat(y,"{=curly}I'm not trying to be weird.{/=curly}",pv)
    $ addchat(y,"{=curly}I just want to wake up and help open the party...{/=curly}",pv)
    
    call answer
    menu:
        "Don't worry... Even if you don't wake up the party will be a success.":
            $ addchat(m,"Don't worry... Even if you don't wake up the party will be a success.",0)
            $ addchat(y,"{image=yoosung puff}",pv,True)
            $ addchat(y,"{=curly}{size=+5}Do you mean that?{/=curly}",pv)
            $ addchat(y,"{=curly}I'm hurt...{/=curly}",pv)
            call heart_break(y)
        "I'll wake you up...":
            $ addchat(m,"I'll wake you up...",0)
            $ addchat(y,"{=sser1}Oh...! Thank you.{/=sser1}",pv,False,True)
            call heart_icon(y)
            $ addchat(y,"{image=yoosung happy}",pv,True)
        "Seven is just playing with you lolol":
            $ addchat(m,"Seven is just playing with you lolol",0)
            $ addchat(y,"I know that ur worried too",pv)
            $ addchat(y,"and don't want to believe what Seven said.",pv)
            $ addchat(y,"But Seven's probably right.",pv)
            $ addchat(y,"Seven is really knowledgeable.",pv)
            $ addchat(y,"He once knew when my cold would get better.",pv)
            $ addchat(y,"He said it'd be between the 3rd and 7th day",pv)
            $ addchat(y,"And it completely went away on the fifth day.",pv)
            $ addchat(y,"Look at that image above...",pv)
            $ addchat(y,"I'm sure it's not a lie.",pv)
    $ addchat(y,"First, I should get some chocolate milk...",pv)
    $ addchat(y,"I'm gonna go to the supermarket~!",pv)
    $ addchat("msg","Yoosung★ has left the chatroom.",pv)
    
    # Call this to end the chat and return to the main menu
    call save_exit
