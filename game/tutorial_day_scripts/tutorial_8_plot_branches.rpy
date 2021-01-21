## This is a short chatroom explaining how plot
## branching works
label plot_branch_tutorial():
    scene hack
    show hack effect
    play music mystic_chat
    enter chatroom u

    u "{=curly}Hello again!{/=curly}" (bounce=True)
    u "{=ser2}You're getting close to the end of the Tutorial day, huh?{/=ser2}"
    u "What do you think of the program so far?"

    menu:
        "It seems quite complicated.":
            u "A lot of work has been put into it!" (bounce=True)
            u "So there are lots of new things to learn."
            u "If you need more help, there's always the {b}Mysterious Messenger Documentation{/b}, which you can open by clicking the {b}Documentation{/b} button in the Developer options."
        "I'm excited to start using it!":
            u "{=curly}That's great!{/=curly}" (bounce=True)
            u "If you ever need help with some features, you can also take a look at the {b}Documentation{/b} by clicking the button in the Developer options."

    u "{=ser1}The last feature I'll show you is how to create a plot branch.{/=ser1}"
    u "{=ser1}You might have noticed that after this chatroom there's a \"Tap to unlock\" icon, right?{/=ser1}"
    u "{=ser1}If you click it, the program will calculate whether or not you've fulfilled certain conditions,{/=ser1}"
    u "{=ser1}and then it'll put you on a path based on the results.{/=ser1}"
    u "{=ser1}In this case, it's going to check if you have the {b}Modified UI{/b} turned on.{/=ser1}"

    # By using the argument (wait=5), this timed menu will wait ~5 seconds
    # for the player to choose an answer before the menu goes away. It doesn't
    # show any new messages while the menu choices are on-screen. The exact
    # time the program will wait depends on the user's settings.
    timed menu (wait=5):
        "Modified UI?":
            u "{=ser1}Yes, it's an option in the {b}Settings{/b}.{/=ser1}"
            u "{=ser1}It's under the {b}Preferences{/b} tab, below a couple of sliders.{/=ser1}"


    # This is one way you can alter responses based on certain conditions
    # In this case, the dialogue changes depending on whether or not the player
    # has the custom UI enabled or not
    if persistent.custom_footers:
        u "It looks like you've already got it turned on!"
        u "So if you go through the plot branch now,"
        u "{=curly}you'll continue on to the Good End ^^{/=curly}" (bounce=True)
        u "You can switch it off if you want the Bad Story End instead."
    else:
        u "{=ser1}You've currently got the \"Classic\" UI on,{/=ser1}"
        u "{=ser1}So if you go through the plot branch now,{/=ser1}"
        u "{=blocky}you'll get the Bad Story End.{/=blocky}"
        u "{=ser1}Just head to {b}Preferences{/b} to toggle the UI changes.{/=ser1}"

        menu:
            "Can you change the UI for me now?":
                u "{=curly}Oh! That's a good idea{/=curly}"
                u "I'll do that right now."
                u "{=curly}Tadaa!{/=curly}" (bounce=True)
                if not observing:
                    $ persistent.custom_footers = True
                u "{=curly}What do you think?{/=curly}"
                u "You can switch it back whenever you like."
                u "{=sser2}Now you'll continue on to the Good End if you go through the plot branch~{/=sser2}"
            "I understand how to change the UI.":
                u "All right!"

    u "This is to demonstrate that you can have the plot branch for lots of different things."
    u "Anyway, that's enough from me."
    u "{=curly}Click the Plot Branch icon to see what happens next!{/=curly}" (bounce=True)
    exit chatroom u
    return


## This is the expired version of the chatroom
label plot_branch_tutorial_expired():
    scene hack
    show hack effect
    play music mystic_chat
    enter chatroom u
    u "It seems [name] is getting close to the end of Tutorial day,"
    u "but [they_re] not here right now T_T"
    u "This is the last chatroom before a plot branch"
    u "{=curly}so some exciting things might happen!{/=curly}" (bounce=True)
    u "{=ser1}Once you click the plot branch button,{/=ser1}"
    u "{=ser1}the program will calculate whether or not you've fulfilled certain conditions,{/=ser1}"
    u "{=ser1}and then it'll set you on a path based on the results.{/=ser1}"
    u "{=ser1}In this case, it'll check whether or not you have {b}Modified UI{/b} turned on.{/=ser1}"
    u "{=ser1}Just head to {b}Preferences{/b} in the {b}Settings{/b} to toggle the UI changes.{/=ser1}"
    u "Well, I guess that's all from me. "
    u "{=curly}You'll log in later to talk to us though, right? ^^{/=curly}" (bounce=True)
    u "See you~"
    exit chatroom u
    return

label after_plot_branch_tutorial():
    # This turns off the hacked effect on the timeline and in the
    # chat home screen.
    $ hacked_effect = False
    return

## This is how the program knows what to do when it gets to a plot branch.
## It's the label of the item after which the plot branch occurs, + _branch
label plot_branch_tutorial_branch():
    ## This is where to write any functions you want to use to determine
    ## which route the player ends up on past this point.

    ## Some examples are below. You can mix and match any
    ## of these statements to create your own unique criteria.

    ## Checking if a character has enough heart points in total:
    # if s.heart_points >= 30:
    #     Seven route
    # else:
    #     Bad End

    ## Checking if a character has more 'bad' heart points than good:
    # if s.good_heart > s.bad_heart:
    #     Good End
    # else:
    #     Bad End

    ## Checking to see which character has the most heart points:
    # if sa.heart_points > v.heart_points:
    #     Saeran route
    # else:
    #     V route

    ## Checking to see how many guests have been successfully invited:
    # if attending_guests() >= 10:
    #     Good End
    # else:
    #     Normal End

    ## Checking to see if the player has participated in enough chatrooms
    ## across days 1-4 (really only relevant for real-time mode).
    ## The function returns a percentage out of 100; you can use it to check
    ## if they participated in more than X% of the chatrooms.
    # if participated_percentage(1, 4) > 32:
    #     Good End
    # else:
    #     Bad Relationship End

    # This particular branch will check whether or not the player
    # has the Modified UI turned on.
    if persistent.custom_footers and participated_percentage(1) >= 20:
        # Continue on to the good end and the party.
        # Since this means the program should simply continue
        # on with the rest of the route, you can use
        $ continue_route()
        # which tells the program to get rid of the plot branch
        # icon and continue the game as normal.
    elif participated_percentage(1) < 20:
        # If the player has participated in less than 20% of the
        # chatrooms across Tutorial Day ("Day 1"), then they're put
        # on the Bad Relationship End.
        $ merge_routes(tutorial_bre)
    else:
        # Bad End
        $ merge_routes(tutorial_bad_end)

    # This label ends like every other label
    return


## This is the chatroom you get if you get the Bad End on Tutorial Day
label tutorial_bad_end():
    $ v.prof_pic = "Profile Pics/V/V-6.webp"
    scene night
    play music i_miss_happy_rika

    v "Hello, [name]."
    v "{=ser2}I came to make an announcement.{/=ser2}"
    v "It doesn't look like we'll be able to have the party after all,"
    v "since we don't have enough guests." (bounce=True, specBubble="sigh_m")

    menu:
        "That's terrible!":
            v "Of course, I wish things could have been different too, but we were operating on a rather short timeframe. "
            v "So it's understandable."
        "I'm really sorry, V.":
            v "No need to apologize, [name]." (bounce=True)
            award heart v
            v "I'm sure you did the best you could."
            v "{=sser2}We simply didn't have enough time...{/=sser2}"

    v "Anyway, that's all I had to say."
    v "I hope you have a good day."
    v "{image=v_smile}" (img=True)
    exit chatroom v

    # This brings up the Save & Exit screen, after which it will show either
    # the 'good', 'normal', or 'bad' ending screen depending on what you pass
    # `ending`
    $ ending = 'bad'
    # If you've set `ending`, then after `return` the route will end.
    return

## This is the label you see if the previous chatroom has expired.
label tutorial_bad_end_expired():
    $ v.prof_pic = "Profile Pics/V/V-6.webp"
    scene night
    play music i_miss_happy_rika
    v "Hello, everyone."
    v "{=ser2}I came to make an announcement.{/=ser2}"
    v "It doesn't look like we'll be able to have the party after all,"
    v "since we don't have enough guests." (bounce=True, specBubble="sigh_m")
    v "Anyway, that's all I had to say."
    v "I hope you have a good day."
    v "{image=v_smile}" (img=True)
    exit chatroom v
    $ ending = 'bad'
    return

## You get this Story Mode after the Plot Branch Tutorial
## chatroom if you continue on to the Good End.
label plot_branch_tutorial_vn():

    scene bg rika_apartment with fade
    pause

    play music mysterious_clues_v2
    show saeran unknown # Show Saeran in his "Unknown" outfit.
    u "Hi, [name]."
    u smile "Looks like you've made it to the Good End! So I've come to take you to paradise."

    menu:
        extend ''
        "To paradise...?":
            u happy "Of course! Don't you want to come?"

            menu:
                extend ''
                "Of course I'll come.":
                    u smile "Perfect."
                    hide saeran
                    show saeran unknown blush at vn_center
                    u "Shall we, then?"
                    scene bg black with fade
                    pause

                "I'd rather stay here.":
                    u sad "Oh... I get it. Maybe you want to learn more about the program."
                    u "I'll let you stay, then."
                    u neutral "You can always go to the {b}Settings{/b} screen and click {b}Start Over{/b} on the {b}Others{/b} tab to play through the Tutorial Day again."
                    u happy "I hope you'll come visit me again!"

        "But I'm not done learning about the program.":
            u thinking "Oh, okay."
            u smile "Well, if you want to start over and go through this route again,"
            u "then you can go to the {b}Settings{/b} screen and click {b}Start Over{/b} on the {b}Others{/b} tab."
            u happy "I hope you'll come visit me again!"

    return



## This is the chatroom you see if you get the Good End on Tutorial Day.
label tutorial_end_example():
    scene hack
    show hack effect
    play music mystic_chat

    u "Congratulations! You've almost made it to the party!" (bounce=True)
    u "{=ser1}This particular party has a special kind of plot branch,{/=ser1}"
    u "{=ser1}which will check if you've fulfilled certain conditions before deciding which version of the party you'll get.{/=ser1}"
    u "{=ser1}In this case, it will check whether or not you've successfully invited at least one guest to the party.{/=ser1}"

    timed menu (wait=5):
        "I'm not sure how to invite guests.":
            u "{=ser1}The \"Inviting Guests\" chatroom lets you invite Rainbow. {/=ser1}"
            u "{=ser1}You can also use that chatroom to speed up how fast you receive replies so you can finish the email chain,{/=ser1}"
            u "{=ser1}but that only works if you have {b}Testing Mode{/b} turned on in the Developer settings, accessed from the main hub screen.{/=ser1}"

    # This is one way you can alter responses based on certain conditions.
    # In this case, the program checks if the player has invited enough guests,
    # and changes the dialogue accordingly.
    if attending_guests() >= 1:
        u "It looks like you've managed to invite at least one guest!"
        u "So if they do come to the party,"
        u "{=curly}you'll get the Good End.{/=curly}" (bounce=True)
    else:
        u "It doesn't look like you've finished any email chains yet,"
        u "{=sser2}so if you click the Plot Branch icon now, you'll get the Normal End.{/=sser2}"
        u "You can still go back to finish up your emails before you click the Plot Branch icon so you get a different ending."

    u "{=curly}Thanks very much for playing through this first day!{/=curly}"
    u "I hope it makes you excited to try programming your own things."
    u "Be sure to contact me if you run into any problems or bugs,"
    u "and I'll do my best to take care of it ^^" (bounce=True)
    u "See you later!"
    exit chatroom u
    return

## This is the label the program jumps to if the previous chatroom expires.
label tutorial_end_example_expired():

    scene hack
    show hack effect
    play music mystic_chat
    u "Looks like [name] is nearly ready to go to the party~"
    u "Too bad [they_re] not here T_T"
    u "{=ser1}The party also has a plot branch condition,{/=ser1}"
    u "{=ser1}which it uses to determine which ending you should get.{/=ser1}"
    u "{=ser1}In this case, it'll check whether or not you've successfully invited 1 guest to the party.{/=ser1}"
    u "If you haven't been getting emails, "
    u "make sure you buy back the \"Inviting Guests\" chatroom!" (bounce=True)
    u "You can turn on {b}Testing Mode{/b} in the Developer settings to replay it as many times as you like."
    u "It'll let you invite Rainbow,"
    u "and if you talk to Zen while you're working on an email chain, he'll make the guests send you replies faster."
    u "{=ser1}You can go through the \"Inviting Guests\" chatroom as many times as you like to finish the email chain and invite Rainbow.{/=ser1}"
    u "All right, I should go."
    u "{=curly}See you at the party ^^{/=curly}" (bounce=True)
    exit chatroom u
    return

## If you would like the party to act as a plot branch, for example, as
## a "Normal" vs "Good" ending, you will do so in a label called
## the party's label name + _branch.
label tutorial_good_end_party_branch():
    # This particular branch will check whether or not you managed
    # to successfully invite one guest to the party
    if attending_guests() >= 1:
        # Good End
        $ continue_route()
    else:
        # Normal End
        $ merge_routes(tutorial_normal_end)
    return

label plot_branch_normal_end():
    play music mystic_chat
    scene bg rika_apartment with fade
    pause
    show saeran unknown at vn_center
    u "This is the normal end, which you got because no one is attending the party."
    u distant "If you did invite someone, you would have seen them arrive at the party."
    u happy "But that's okay!"
    u "It's good to see all the different endings, too."
    u smile "Did you have any questions about how to get the other endings?"
    call ending_descrip('Normal', u)
    $ ending = 'normal'
    return

## This is a convenience label to have 'who' explain the different endings
## to the player before the route ends.
label ending_descrip(ending_type, who):
    $ shuffle = False
    menu ending_top:
        extend ''
        "How do I get the Bad Relationship End?" if ending_type != "Bad Relationship":
            who neutral "You get the Bad Relationship End when you haven't participated in enough story items."
            who "Things like chatrooms and story calls expire if you're playing in real-time,"
            who "Or you can force a chatroom to expire by clicking the back button before it ends if it's your first time playing."
            who thinking "If you want to be sneaky..."
            who happy "You could also start a new game and check 'Unlock all story' in the Developer settings."
            who smile "That unlocks all story items and plot branches without having to play them sequentially."
            who "So you could just use that and click the plot branch icon right away."
            who "Do you want to know about any other endings?"
            $ shuffle = False
            jump ending_top
        "How do I get the Good End?" if ending_type != "Good":
            if ending_type == "Normal":
                who smile "The same way you got here, but with one guest invited!"
            else:
                who smile "First, you need a guest to attend the party."
            who "So, make sure you participate in the \"Inviting Guests\" chatroom and invite Rainbow."
            who -smile "You can turn {b}Testing Mode{/b} on from the Developer settings too so you can replay it and invite her again."
            who "She's guaranteed to attend the party if you answer all three of her emails correctly,"
            who happy "But she might still attend even if you get one or two emails wrong."
            who -happy "You also have to participate in at least 20\% of the chatrooms on Tutorial Day,"
            who "or else you'll get the Bad Relationship End."
            who "Finally, you need to have \"Modified UI\" turned on from the Settings when you click the plot branch icon."
            who "You can find it under the {b}Preferences{/b} tab."
            who happy "If you've done all that, and you see Rainbow attend the party, then you'll get the Good End!"
            who neutral "Are there any other endings you want to know about?"
            $ shuffle = False
            jump ending_top
        "How do I get the Bad End?" if ending_type != "Bad":
            who neutral "You can get the Bad End after the first plot branch, before the party."
            who "First, you need to participate in at least 20\% of the chatrooms on Tutorial Day before the plot branch."
            who "Then, make sure you have \"Modified UI\" turned {b}off{/b} from the {b}Preferences{/b} tab in the {b}Settings{/b}."
            who happy "If you do that, when you go through the plot branch, you should get the Bad End."
            who neutral "It won't matter how many guests you've invited."
            who "Are there any other endings you want to know about?"
            $ shuffle = False
            jump ending_top
        "How do I get the Normal End?" if ending_type != "Normal":
            who neutral "You'll get the Normal End if you get through the plot branch and no one attends the party."
            who "So, make sure you've participated in at least 20\% of the story on Tutorial Day,"
            who "and turn on \"Modified UI\" from the {b}Preferences{/b} tab in the Settings."
            who "Then you should be able to get through the first plot branch,"
            who "and if no one attends your party (or you never invited anyone), you'll get the Normal End."
            who smile "Do you want to know about how to get any of the other endings?"
            $ shuffle = False
            jump ending_top
        "That's all.":
            pass

    who smile "Thanks for playing through Tutorial Day!"

    # Determine which endings the player is missing
    $ missing_endings = [ ]
    if completed_branches(tutorial_route) < 4:
        if 'plot_branch_normal_end' not in persistent.completed_story:
            $ missing_endings.append('Normal')
        if 'tutorial_good_end_party' not in persistent.completed_story:
            $ missing_endings.append('Good')
        if 'tutorial_bad_end' not in persistent.completed_story:
            $ missing_endings.append('Bad')
        if 'plot_branch_bre' not in persistent.completed_story:
            $ missing_endings.append('Bad Relationship')

        if len(missing_endings) == 1:
            who neutral "It looks like you're only missing the [missing_endings[0]] End."
            if missing_endings[0] == ending_type:
                who smile "Which you'll get after this Story Mode ends!"
                who happy "Thanks for getting all the endings~"
            else:
                who "I hope you'll try collecting all the endings!"
        elif len(missing_endings) == 4:
            who neutral "It seems like this is the first ending you got!"
            who smile "I hope you'll go through Tutorial Day again to see the rest~"
        elif missing_endings:
            if ending_type in missing_endings:
                $ missing_endings.remove(ending_type)
            who "So far it looks like you're missing..."
            while missing_endings:
                $ e = missing_endings.pop()
                who "The [e] End"
            who happy "I hope you'll go through Tutorial Day again to see the rest of the endings!"
        else:
            who "It looks like you've gotten all the endings already!"
            who "I'm glad to see you've played the game again then~"

    return

## And this is a very brief Story Mode for the party
label tutorial_good_end_party():
    play music mystic_chat
    scene bg rika_apartment with fade
    pause
    show saeran unknown
    u happy "Welcome to the party!"
    u thinking "Or, what would be the party for a normal route."
    u distant "The party works the same way as any other Story Mode section; the only thing that's different is the icon."
    u neutral "As this is probably the end of your game though, you should be sure you show the user which ending they got."
    u "Then you can reset the game so they can play through it again."
    u smile "As always, there's more information on that in the documentation."
    u neutral "As a bonus for getting to the Good End, there's one more thing I can show you:"
    u "How to show a CG in a Story Mode section."
    u smile "You'll be able to see it in the Album after this Story Mode section is over."
    scene cg common_3
    pause
    # Re-show the apartment here since it was hidden to show the CG
    scene bg rika_apartment
    show saeran unknown
    u "Do you want to know how to get the other endings before I go?"
    call ending_descrip('Good', u)
    $ ending = 'good'
    return


## This is an interesting case in which the ending only has one
## Story Mode section after the plot branch chatroom and then it ends
## You can write this much the same way as any regular Story Mode section
label plot_branch_bre():
    play music mint_eye_piano
    scene mint_eye_room with fade
    pause
    show saeran sad
    r "Did you not like my game?"
    r sob "It looks like you didn't participate much in the chatrooms."
    r "So now you're getting the \"Bad Relationship End\"."
    r distant "Well, that's okay I guess. Maybe you just got busy."
    r neutral "Try playing through the game again sometime, won't you?"
    r "And you can play through all the chatrooms."
    r "Maybe you just didn't understand how to get the rest of the endings."
    r "Was there an ending you wanted to know how to get?"
    call ending_descrip('Bad Relationship', r)
    $ ending = 'bad'
    return







