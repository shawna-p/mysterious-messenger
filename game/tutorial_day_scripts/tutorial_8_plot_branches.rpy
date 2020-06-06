## This is a short chatroom explaining how plot
## branching works
label plot_branch_tutorial():
    call chat_begin("hack") 
    call hack 
    call play_music(mystic_chat)
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
            u "If you need more help, there's always the {b}Mysterious Messenger wiki{/b}, which you can find on GitHub." 
        "I'm excited to start using it!":
            m "I'm excited to start using it!"   (pauseVal=0)
            u "{=curly}That's great!{/=curly}"   (bounce=True)
            u "If you ever need help with some features, you can also take a look at the {b}wiki{/b} on the Mysterious Messenger GitHub." 
            
    u "{=ser1}The last feature I'll show you is how to create a plot branch.{/=ser1}" 
    u "{=ser1}You might have noticed that after this chatroom there's a \"Tap to unlock\" icon, right?{/=ser1}" 
    u "{=ser1}If you click it, the program will calculate whether or not you've fulfilled certain conditions,{/=ser1}" 
    u "{=ser1}and then it'll put you on a path based on the results.{/=ser1}" 
    u "{=ser1}In this case, I'll to check whether or not you've successfully invited at least one guest to the party.{/=ser1}" 
    
    call answer 
    menu:
        "I'm not sure how to invite guests.":
            m "I'm not sure how to invite guests." (pauseVal=0)
            u "{=ser1}The \"Inviting Guests\" chatroom lets you invite Rainbow. {/=ser1}" 
            u "{=ser1}You can also use that chatroom to speed up how fast you receive replies so you can finish the email chain,{/=ser1}" 
            u "{=ser1}but that only works if you have {b}Testing Mode{/b} turned on in the Developer settings, accessed from the main hub screen.{/=ser1}" 
        "(Continue listening)":
            pass
            
    # This is one way you can alter responses based on certain conditions
    # In this case, the program checks if the player has invited enough guests,
    # and change the dialogue accordingly
    if attending_guests() >= 1:
        u "It looks like you've managed to invite at least one guest!" 
        u "So if they do come to the party," 
        u "{=curly}you'll get the Good End.{/=curly}" (bounce=True)
    else:
        u "It doesn't look like you've finished any email chains yet," 
        u "{=sser2}so if you click the Plot Branch icon now, you'll get a bad end.{/=sser2}" 
        u "You can still go back to finish up your emails before you click the Plot Branch icon so you get a different ending." 
        
    u "Anyway, that's enough from me." 
    u "{=curly}Click the Plot Branch icon to see what happens next!{/=curly}"   (bounce=True)
    call exit(u) 
    jump chat_end

## This is the expired version of this chatroom
label plot_branch_tutorial_expired():
    call chat_begin("hack") 
    call hack 
    call play_music(mystic_chat)
    call enter(u)
    u "It seems [name] is getting close to the end of Tutorial day," 
    u "but [they_re] not here right now T_T" 
    u "This is the last day before a plot branch" 
    u "{=curly}so some exciting things might happen!{/=curly}"   (bounce=True)
    u "{=ser1}Once you click the plot branch button,{/=ser1}" 
    u "{=ser1}the program will calculate whether or not you've fulfilled certain conditions,{/=ser1}" 
    u "{=ser1}and then it'll set you on a path based on the results.{/=ser1}" 
    u "{=ser1}In this case, it'll check whether or not you've successfully invited 1 guest to the party.{/=ser1}" 
    u "If you haven't been getting emails, " 
    u "make sure you buy back the \"Inviting Guests\" chatroom!"   (bounce=True)
    u "You can turn on {b}Testing Mode{/b} in the Developer settings to replay it as many times as you like."
    u "It'll let you invite Rainbow," 
    u "and if you talk to Zen while you're working on an email chain, he'll make the guests send you replies faster." 
    u "{=ser1}You can go through the \"Inviting Guests\" chatroom as many times as you like to finish the email chain and invite Rainbow.{/=ser1}" 
    u "Well, I guess that's all from me. " 
    u "{=curly}You'll log in later to talk to us though, right? ^^{/=curly}"   (bounce=True)
    u "See you~" 
    call exit(u)
    jump chat_end

## This is how the program knows what to do when it gets to a plot
##  branch. It's the label of the chatroom after which the plot 
## branch occurs, + _branch
label plot_branch_tutorial_branch():
    # This is where to write any functions you want to
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
    # The function returns a percentage; you can use it to check
    # if they participated in more than X% of the chatrooms
    # if participated_percentage(1, 4) > 32:
    #     Good End
    # else:
    #     Bad Relationship End
        
    # This particular branch will check whether or not you managed 
    # to successfully invite one guest to the party
    if attending_guests() >= 1:
        # Good End
        # Since this means the program should simply continue
        # on with the rest of the route, you can use
        $ continue_route()
        # which tells the program to get rid of the plot branch
        # icon and continue the game as normal
    elif participated_percentage(1) < 20:
        # If the player has participated in less than 20% of the
        # chatrooms across Tutorial Day ("Day 1"), then they're put
        # on the Bad Relationship End
        $ merge_routes(tutorial_bre)
    else:
        # Bad End
        $ merge_routes(tutorial_bad_end)
        
    # This is how you end a plot branch label; it'll trigger the
    # next chatroom for you
    jump plot_branch_end

## This is the chatroom you get if you get the Bad End
## of the Tutorial Day
label tutorial_bad_end():

    call chat_begin('noon') 
    call play_music(i_miss_happy_rika)

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
    v "{image=v_smile}"   (img=True)
    call exit(v) 
    
    # This brings up the Save & Exit screen, after which
    # it will show either the 'good', 'normal', or 'bad'
    # ending screen depending on what you pass `ending`
    $ ending = 'bad'
    jump chat_end_route
    
## This is the label you see if the previous chatroom has expired
label tutorial_bad_end_expired():
    call chat_begin('noon')
    call play_music(i_miss_happy_rika)
    v "Hello, everyone." 
    v "{=ser2}I came to make an announcement.{/=ser2}" 
    v "It doesn't look like we'll be able to have the party after all," 
    v "since we don't have enough guests."   (bounce=True, specBubble="sigh_m")
    v "Anyway, that's all I had to say." 
    v "I hope you have a good day." 
    v "{image=v_smile}"   (img=True)
    call exit(v)
    $ ending = 'bad'
    jump chat_end_route

## You get this VN after the Plot Branch Tutorial
## chatroom if you got the Good End
label plot_branch_tutorial_vn():
    call vn_begin 

    scene bg rika_apartment with fade
    pause
    
    call play_music(mysterious_clues_v2)
    show saeran unknown
    u "Hi, [name]."
    u smile "Looks like you've made it to the Good End! So I've come to take you to paradise."
    
    menu:
        extend ''
        "To paradise...?":
            m "To paradise...?"
            u happy "Of course! Don't you want to come?"
            
            menu:
                extend ''
                "Of course I'll come.":
                    m "Of course I'll come."
                    u smile "Perfect."
                    hide saeran
                    show saeran unknown blush at vn_center
                    u "Shall we, then?"
                    scene bg black with fade
                    pause
                
                "I'd rather stay here.":
                    m "I'd rather stay here."
                    u sad "Oh... I get it. Maybe you want to learn more about the program."
                    u "I'll let you stay, then."
                    u neutral "You can always go to the {b}Settings{/b} screen and click {b}Start Over{/b} on the {b}Others{/b} tab to play through the Tutorial Day again."
                    u happy "I hope you'll come visit me again!"
        
        "But I'm not done learning about the program.":
            m "But I'm not done learning about the program."
            u thinking "Oh, okay."
            u smile "Well, if you want to start over and go through this route again,"
            u "then you can go to the {b}Settings{/b} screen and click {b}Start Over{/b} on the {b}Others{/b} tab."
            u happy "I hope you'll come visit me again!"
            
    jump vn_end



## This is the chatroom you see if you get the Good End
## of the Tutorial Day
label tutorial_good_end():
    call chat_begin('hack') 
    call hack 
    call play_music(mystic_chat)
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
## so to save code it's just a jump to it
label tutorial_good_end_expired():
    jump tutorial_good_end

## And this is a very brief VN for the party    
label tutorial_good_end_party():
    call vn_begin 
    scene bg rika_apartment with fade
    pause
    show saeran unknown
    u "This is where you'd likely put a VN section for a party."
    u distant "It works the same way as any other VN section; the only thing that's different is the icon."
    u neutral "As this is probably the end of your game though, you should be sure you show the user which ending they got."
    u "Then you can reset the game so they can play through it again."
    u smile "As always, there's more information on that in the wiki."
    u neutral "However, before you go, there's one more thing I can show you:"
    u "How to show a CG in a Story Mode section."
    u smile "I'll show it to you just before I go, and then you'll be able to see it in your album."
    scene cg common_3
    pause
    scene bg rika_apartment
    show saeran unknown happy
    u "Thanks for playing through Tutorial Day!"
    # If you need to later, you can then write `hide cg`
    $ ending = 'good'
    jump vn_end_route
    

## This is an interesting case in which the ending only has one
## VN mode section after the plot branch chatroom and then it ends
## You can write this much the same way as any regular VN mode section
label plot_branch_bre():
    call vn_begin
    call play_music(mint_eye_piano)
    scene mint_eye_room with fade
    pause
    show saeran sad 
    r "Did you not like my game?"
    r sob "It looks like you didn't participate much in the chatrooms."
    r "So now you're getting the \"Bad Relationship End\"."
    r distant "Well, that's okay I guess. Maybe you just got busy."
    r neutral "Try playing through the game again sometime, won't you?"
    r "And you can play through all the chatrooms."
    r thinking "Well, I should go now."
    r "It's too bad we didn't get to spend much time together."
    $ ending = 'bad'
    jump vn_end_route







