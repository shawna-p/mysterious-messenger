## This is a short chatroom explaining how plot
## branching works
label plot_branch_tutorial():
    stop music
    call hack 
    call chat_begin("hack") 
    play music mystic_chat loop
    call enter(u) 

    u "{=curly}Hello again!{/=curly}"   (bounce=True)
    u "{=ser2}You're getting close to the end of the Tutorial day, huh?{/=ser2}" 
    u "What do you think of the program so far?" 
    
    call answer 
    menu:
        "It seems quite complicated.":
            m "It seems quite complicated."   (pauseVal=0)
            u "A lot of work has been put into it!"   (bounce=True)
            u "So there are lots of new things to learn." 
            u "If you need more help, there's always the {b}User Guide{/b}, which is included with the program." 
        "I'm excited to start using it!":
            m "I'm excited to start using it!"   (pauseVal=0)
            u "{=curly}That's great!{/=curly}"   (bounce=True)
            u "If you ever need help with some features, you can also take a look at the {b}User Guide{/b} that was included with the program." 
            
    u "{=ser1}The last feature I'll show you is how to create a plot branch.{/=ser1}" 
    u "{=ser1}You might have noticed that after this chatroom there's a \"Tap to unlock\" icon, right?{/=ser1}" 
    u "{=ser1}If you click it, the program will calculate whether or not you've fulfilled certain conditions,{/=ser1}" 
    u "{=ser1}and then it'll put you on a path based on the results.{/=ser1}" 
    u "{=ser1}In this case, we're going to check whether or not you've successfully invited at least one guest to the party.{/=ser1}" 
    
    call answer 
    menu:
        "I'm not sure how to invite guests.":
            m "I'm not sure how to invite guests." (pauseVal=0)
            u "{=ser1}The \"Inviting Guests\" chatroom lets you invite Rainbow. {/=ser1}" 
            u "{=ser1}You can also use that chatroom to speed up how fast you receive replies so you can finish the email chain.{/=ser1}" 
        "(Continue listening)":
            pass
            
    # This is one way you can alter responses based on certain conditions
    # In this case, we check if the player has invited enough guests,
    # and change the dialogue accordingly
    # Note: sometimes Unknown will say you've invited a guest and you'll
    # still get the Bad End; this only happens when you've failed the second
    # or third response in an email since the guest will have a 33% or 67% 
    # chance of attending the party, respectively. Sometimes this statement
    # will calculate that they're coming, but the when the plot branch 
    # calculates the number of guests attending, the guest won't come
    if attending_guests() >= 1:
        u "It looks like you've managed to invite at least one guest!" 
        u "{=curly}So you'll get the Good End.{/=curly}" 
    else:
        u "It doesn't look like you've finished any email chains yet," 
        u "{=sser2}so if you click the Plot Branch icon now, you'll get the bad end.{/=sser2}" 
        u "You can still go back to finish up your emails before you click the Plot Branch icon so you get a different ending." 
        
    u "Anyway, that's enough from me." 
    u "{=curly}Click the Plot Branch icon to see what happens next!{/=curly}"   (bounce=True)
    call exit(u) 
    jump chat_end

## This is the label we jump to if this chatroom
## has expired
label plot_branch_tutorial_expired():
    stop music
    call hack 
    call chat_begin("hack") 
    play music mystic_chat loop
    call enter(u)
    u "It seems [name] is getting close to the end of Tutorial day," 
    u "but [they_re] not here right now T_T" 
    u "This is the last day before a plot branch" 
    u "{=curly}so some exciting things might happen!{/=curly}"   (bounce=True)
    u "{=ser1}Once you click the plot branch button,{/=ser1}" 
    u "{=ser1}the program will calculate whether or not you've fulfilled certain conditions,{/=ser1}" 
    u "{=ser1}and then it'll set you on a path based on the results.{/=ser1}" 
    u "{=ser1}In this case, we're going to check whether or not you've successfully invited 1 guest to the party.{/=ser1}" 
    u "If you haven't been getting emails, " 
    u "make sure you buy back the \"Inviting Guests\" chatroom!"   (bounce=True)
    u "It'll let you invite Rainbow," 
    u "and if you talk to Zen while you're working on an email chain, he'll make the guests send you replies faster." 
    u "{=ser1}You can go through the \"Inviting Guests\" chatroom as many times as you like to finish the email chain and invite Rainbow.{/=ser1}" 
    u "Well, I guess that's all from me. " 
    u "{=curly}You'll log in later to talk to us though, right? ^^{/=curly}"   (bounce=True)
    u "See you~" 
    call exit(u)
    jump chat_end

## This is how the program knows what to do when
## it gets to a plot branch. It's the label of the
## chatroom after which the plot branch occurs, 
## + _branch
label plot_branch_tutorial_branch():
    # This is where to write any functions we want to
    # use to determine which route the player ends
    # up on past this point
    
    # Some examples are below. You can mix and match any
    # of these statements to create your own unique criteria

    # Checking if a character has enough heart points 
    # in total
    # if s.heart_points >= 30:
    #     Seven route
    # else:
    #     Bad End
        
    # Checking if a character has more 'bad' heart
    # points than good
    # if s.good_heart > s.bad_heart:
    #     Good End
    # else:
    #     Bad End
        
    # Checking to see which character has the most
    # heart points
    # if sa.heart_points > v.heart_points:
    #     Saeran route
    # else:
    #     V route
        
    # Checking to see how many guests have been
    # successfully invited
    # if attending_guests() >= 10:
    #     Good End
    # else:
    #     Normal End
        
    # Checking to see if the player has participated
    # in enough chatrooms across days 1-4 (really only 
    # relevant for real-time mode)
    # The function returns a percentage, so we're checking
    # if they participated in more than 32% of the chatrooms
    # if participated_percentage(1, 4) > 32:
    #     Good End
    # else:
    #     Bad Relationship End
        
    # For the purposes of this program, we will check whether
    # or not you managed to successfully invite one guest to 
    # the party
    if attending_guests() >= 1:
        # Good End
        # tutorial_good_end is defined back in route_setup.rpy
        # We also pass the function a second argument, True, 
        # to tell it that there's a VN right after the chatroom
        # where the plot branch was
        $ merge_routes(tutorial_good_end, True)
    else:
        # Bad End
        # This Bad End route doesn't have a VN right after the
        # chatroom where the plot branch was, so we don't need
        # any other arguments
        $ merge_routes(tutorial_bad_end)
        
    # This is how you'll end a plot branch label; it'll trigger the
    # next chatroom for you
    jump plot_branch_end

## This is the chatroom you'll get if you get the Bad End
## of the Tutorial Day
label tutorial_bad_end():

    call chat_begin('noon') 
    play music i_miss_happy_rika loop

    v "Hello, [name]." 
    v "{=ser2}I came to make an announcement.{/=ser2}" 
    v "It doesn't look like we'll be able to have the party after all," 
    v "since we don't have enough guests."   (bounce=True, specBubble="sigh_m")
    
    call answer 
    menu:
        "That's terrible!":
            m "That's terrible!"   (pauseVal=0)
            v "Of course, I wish things could have been different too, but we were operating on a rather short timeframe. " 
            v "So it's understandable." 
        "I'm really sorry, V.":
            m "I'm really sorry, V."   (pauseVal=0)
            v "No need to apologize, [name]."   (bounce=True)
            call heart_icon(v) 
            v "I'm sure you did the best you could." 
            v "{=sser2}We simply didn't have enough time...{/=sser2}" 
            
    v "Anyway, that's all I had to say." 
    v "I hope you have a good day." 
    v "{image=v smile}"   (img=True)
    call exit(v) 
    
    # This brings up the Save & Exit screen, after which
    # it will show either the 'good', 'normal', or 'bad'
    # ending screens depending on which variable you pass
    call chat_end_route('bad') 
    # Use this to start the game over and return to the main menu
    jump restart_game
    
## This is the label you'll see if the previous chatroom
## has expired
label tutorial_bad_end_expired():
    call chat_begin('noon')
    play music i_miss_happy_rika loop
    v "Hello, everyone." 
    v "{=ser2}I came to make an announcement.{/=ser2}" 
    v "It doesn't look like we'll be able to have the party after all," 
    v "since we don't have enough guests."   (bounce=True, specBubble="sigh_m")
    v "Anyway, that's all I had to say." 
    v "I hope you have a good day." 
    v "{image=v smile}"   (img=True)
    call exit(v)
    call chat_end_route('bad')
    jump restart_game

## You'll get this VN after the Plot Branch Tutorial
## chatroom if you got the Good End
label plot_branch_vn():
    call vn_begin 
    
    # You'll generally never want to mess with the 'observing' variable 
    # yourself, but since this is a tutorial chatroom we want the user 
    # to be able to play it over and over and not be restricted to the 
    # choices they've already made
    $ observing = False

    scene bg rika_apartment with fade
    pause
    
    play music mysterious_clues_v2 loop
    show saeran vn unknown
    u_vn "Hi, [name]."
    show saeran vn smile
    u_vn "Looks like you've made it to the Good End! So I've come to take you to paradise."
    
    menu:
        extend ''
        "To paradise...?":
            m_vn "To paradise...?"
            show saeran vn happy
            u_vn "Of course! Don't you want to come?"
            
            menu:
                extend ''
                "Of course I'll come.":
                    m_vn "Of course I'll come."
                    show saeran vn smile
                    u_vn "Perfect."
                    hide saeran vn
                    show saeran vn unknown blush at vn_center
                    u_vn "Shall we, then?"
                    scene bg black with fade
                    pause
                
                "I'd rather stay here.":
                    m_vn "I'd rather stay here."
                    show saeran vn sad
                    u_vn "Oh... I get it. Maybe you want to learn more about the program."
                    u_vn "I'll let you stay, then."
                    show saeran vn neutral
                    u_vn "You can always go to the {b}Settings{/b} screen and click {b}Start Over{/b} on the {b}Others{/b} tab to play through the Tutorial Day again."
                    show saeran vn happy
                    u_vn "I hope you'll come visit me again!"
        "But I'm not done learning about the program.":
            m_vn "But I'm not done learning about the program."
            show saeran vn thinking
            u_vn "Oh, okay."
            show saeran vn smile
            u_vn "Well, if you want to start over and go through this route again,"
            u_vn "then you can go to the {b}Settings{/b} screen and click {b}Start Over{/b} on the {b}Others{/b} tab."
            show saeran vn happy
            u_vn "I hope you'll come visit me again!"
            
    jump vn_end



## This is the chatroom you'll get if you get the Good End
## of the Tutorial Day
label tutorial_good_end():
    stop music
    call hack 
    call chat_begin('hack') 
    play music mystic_chat loop
    u "{=curly}Thanks very much for playing through this first day!{/=curly}" 
    u "I hope it makes you excited to try programming your own things." 
    u "Be sure to contact me if you run into any problems or bugs," 
    u "and I'll do my best to take care of it ^^"   (bounce=True)
    u "See you later!" 
    call exit(u) 
    jump chat_end
    
## This is the label the program jumps to if
## the previous chatroom expires. However, in this
## case it's the same as the original chatroom,
## so to save code we'll just jump to it
label tutorial_good_end_expired():
    jump tutorial_good_end

## And this is a very brief VN for the party    
label good_end_party():
    call vn_begin 
    scene bg rika_apartment with fade
    pause
    show saeran vn unknown
    u_vn "This is where you'd likely put a VN section for a party."
    show saeran vn distant
    u_vn "It works the same way as any other VN section; the only thing that's different is the icon."
    show saeran vn neutral
    u_vn "As this is probably the end of your game though, you'll want to make sure you show the user which ending they got."
    u_vn "Then you can reset the game so they can play through it again."
    show saeran vn smile
    u_vn "As always, there's more information on that in the User Guide."
    show saeran vn happy
    u_vn "Thanks for playing through Tutorial Day!"
    
    # For VN modes, we can just manually show which
    # ending screen we like
    scene bg good_end
    pause
    # This is the end of the Tutorial Day; we
    # restart the game to indicate this
    jump restart_game



