## This is a fairly standard chatroom. If you're looking for more
## information on how to make the chatrooms, check out tutorial_5_coffee.rpy
## and tutorial_1_chatroom.rpy
## Otherwise, scroll down to the popcorn_vn label for an example of
## a typical VN
label popcorn_chat():

    call chat_begin("morning") 

    # This sets new profile pictures for Jaehee and Jumin. You can change 
    # cover photos this way (e.g. ja.cover_pic = "yourimg.png") as well as
    # their status (e.g. ju.status = "Jumin's status")
    # This should go after `call chat_begin(...)` so that the profile
    # pictures also update in the History screen
    $ ja.prof_pic = 'Profile Pics/Jaehee/jae-2.jpg'
    $ ju.prof_pic = 'Profile Pics/Jumin/ju-18.jpg'
    
    play music urban_night_cityscape
    
    ju "Zen's written some strange things." 
    ja "{image=jaehee_happy}" (img=True)
    ja "There is a meeting with the Women Artists group today." 
    ja "I'm telling you this before you come to the office..." 
    ja "The meeting's agenda will be about the \"Loss of the Muse\" exhibition... Please choose a more artistic tie that will suit today's meeting." 
    ju "{=sser1xb}He's not in his right mind to dream about Elizabeth the 3rd going missing.{/=sser1xb}" 
    ja "Isn't it up to him to dream about whatever he wants?" 
    ja "{image=jaehee_well}" (img=True)
    ju "Don't tell me you believe in his \"psychic\" dream." 
    ja "I don't believe in it..." 
    ja "{u}But why don't you first greet [name] here and then continue talking about the dream.{/u}" 
    ju "Oh, [name], hello." 
    ju "I didn't see you here." 
    ja "Hello, [name]." 
    
    call answer 
    menu:
        "Shouldn't you think of a plan to protect Elizabeth the 3rd just in case?":
            m "Shouldn't you think of a plan to protect Elizabeth the 3rd just in case?"   (pauseVal=0)
            
    ju "Fantastic idea."   (bounce=True)
    # This adds a 'bad' heart point for Jumin -- it still awards
    # the player a heart point, but you can use this to count 'bad'
    # responses while still giving heart points so you can make a
    # plot branch later and count the 'bad' responses
    award heart ju bad 
    ja "{image=jaehee_well}" (img=True)
    ja "This is not the time for that..." 
    ju "Perhaps Zen had that dream last night" 
    ju "because he harbors feelings towards her." 
    ja "{=blocky}I doubt that is the case, as he left the chatroom saying his nose got itchy.{/=blocky}" 
    ju "If he has a problem, I'll consider referring him to a therapist." 
    ja "{=curly}I don't think there's a need for that. We are free to imagine whatever we want, after all;;{/=curly}" 
    
    call answer 
    menu:
        "Why don't you gift a luxurious cage for Elizabeth the 3rd?":
            m "Why don't you gift a luxurious cage for Elizabeth the 3rd?"   (pauseVal=0)
            
    ja "Excuse me? ;;" 
    ja "{image=jaehee_question}" (img=True)
    ju "Oh..." 
    ju "{size=+10}Good idea!{/size}"   (bounce=True)
    award heart ju bad 
    ja "What...;;??" 
    ju "I feel like [name] understands me very well."   (bounce=True, specBubble="cloud_l")
    ju "{image=jumin_smile}" (img=True)
    ju "Assistant Kang." 
    ju "{=sser1xb}I'd like to invite [name] to the morning meeting today.{/=sser1xb}" 
    ja "What do you mean?" 
    ju "{u}Cancel the meeting that was planned and you, me, and [name], the three of us will discuss a plan that will ensure Elizabeth the 3rd's safety.{/u}" 
    ja "I don't think you should cancel a meeting that was already planned because of one dream." 
    ju "It's not because of the dream. I've always been bothered by how free she was to roam around the house..." 
    ja "{=blocky}The number of security cameras and guards in your penthouse is probably higher than the employees here.{/=blocky}" 
    ju "That's not what's important." 
    ju "I don't think you understand very well, so I'll need to hear [name]'s opinion."   (bounce=True)
    
    call answer 
    menu:
        "Hahaha~ of course. You should listen to my excellent ideas.":
            m "Hahaha~ of course. You should listen to my excellent ideas."   (pauseVal=0)
            
    ju "{=sser2}You're very quick to understand.{/=sser2}" 
    award heart ju bad 
    ju "{=sser2}Come to the C&R building right away.{/=sser2}" 
    ja "-_-" 
    ja "{image=jaehee_well}" (img=True)
    ja "{=curly}Why are we talking about this now?;;{/=curly}" 
    ja "{=curly}I don't feel good about this...{/=curly}" 
    ju "{=sser1xb}Stop talking about something else and prepare for the meeting.{/=sser1xb}" 
    ja "Yes, Mr. Han..." 
    ja "[name]," 
    ja "The C&R building is the second tallest building in the city so I'll assume you know where it is." 
    ja "Please go to the information desk and say your name and that you're an RFA member. I will tell them to show you to the conference room." 
    ju "Good." 
    ju "Then I'll have to go and get ready." 
    ju "[name]... I'll look forward to your wonderful ideas."   (bounce=True)
    call exit(ju) 
    ja "{image=jaehee_huff}" (img=True)
    ja "{=curly}There's not even an hour left until the meeting and he wants to cancel his appointment...{/=curly}" 
    ja "Haha..." 
    ja "So the three of us will have a meeting..." 
    ja "Weren't you flustered by Mr. Han's sudden suggestion?" 
    
    call answer 
    menu:
        "Not at all~ See ya later.":
            m "Not at all~ See ya later."   (pauseVal=0)
    ja "Yes..." 
    ja "Please let me know as soon as you're there."
    call exit(ja) 
    
    jump chat_end   
    
## This is the expired version of the chatroom
## It's very similar to the regular version, but with
## a few dialogue changes since MC is not present
label popcorn_chat_expired():
    call chat_begin("morning") 
    $ ja.prof_pic = 'Profile Pics/Jaehee/jae-2.jpg'
    $ ju.prof_pic = 'Profile Pics/Jumin/ju-18.jpg'   
    play music urban_night_cityscape
    # This is an alternative way of writing chatroom dialogue.
    # It's a little easier to write, though you need to use the right keywords.
    msg ju "Zen's written some strange things." 
    msg ja "{image=jaehee_happy}" # Note this is automatically recognized as
                                   # an image
    msg ja "There is a meeting with the Women Artists group today." 
    msg ja "I'm telling you this before you come to the office..." 
    msg ja "The meeting's agenda will be about the \"Loss of the Muse\" exhibition... Please choose a more artistic tie that will suit today's meeting." 
    msg ju "He's not in his right mind to dream about Elizabeth the 3rd going missing." sser1 xbold
    msg ja "Isn't it up to him to dream about whatever he wants?" 
    msg ja "{image=jaehee_well}"
    msg ju "Don't tell me you believe in his \"psychic\" dream." 
    msg ja "I don't believe in it..." 
    msg ju "Even if it isn't true..." 
    msg ju "It might be good to come up with a plan to protect Elizabeth the 3rd just in case." 
    msg ja "{image=jaehee_well}"
    msg ja "This is not the time for that..." 
    msg ju "Perhaps Zen had that dream last night" 
    msg ju "because he harbors feelings towards her." 
    msg ja "I doubt that is the case, as he left the chatroom saying his nose got itchy." blocky
    msg ju "If he has a problem, I'll consider referring him to a therapist." 
    msg ja "I don't think there's a need for that. We are free to imagine whatever we want, after all;;" curly
    msg ju "Hmm" 
    msg ju "I wish [name] was here." 
    msg ju "I feel like [they] understand[s_verb] me very well." 
    msg ju "{image=jumin_smile}"
    msg ju "Assistant Kang." 
    msg ju "I'd like to invite [name] to the morning meeting today." sser1 xbold
    msg ja "What do you mean?" 
    msg ju "{u}Cancel the meeting that was planned and you, me, and [name], the three of us will discuss a plan that will ensure Elizabeth the 3rd's safety.{/u}" 
    msg ja "I don't think you should cancel a meeting that was already planned because of one dream." 
    msg ju "It's not because of the dream. I've always been bothered by how free she was to roam around the house..." 
    msg ja "The number of security cameras and guards in your penthouse is probably higher than the employees here." blocky
    msg ju "That's not what's important." 
    msg ju "I don't think you understand very well, so I'll need to hear [name]'s opinion." bounce
    msg ja "But [they_re] not even here...;;" 
    msg ju "I'm sure [they]'ll read the messenger soon. Call [them] if you must." sser2
    msg ju "Tell [them] to come to the C&R building right away." sser2
    msg ja "-_-" 
    msg ja "{image=jaehee_well}"
    msg ja "Why are we talking about this now?;;" curly
    msg ja "I don't feel good about this..." curly
    msg ju "Stop talking about something else and prepare for the meeting." sser1 xbold
    msg ja "Yes, Mr. Han..." 
    msg ja "[name], when you read this," 
    msg ja "The C&R building is the second tallest building in the city so I'll assume you know where it is." 
    msg ja "Please go to the information desk and say your name and that you're an RFA member. I will tell them to show you to the conference room." 
    msg ju "Good." 
    msg ju "Then I'll have to go and get ready." 
    msg ju "[name]... I'll look forward to your wonderful ideas." bounce
    call exit(ju)
    msg ja "{image=jaehee_huff}"
    msg ja "There's not even an hour left until the meeting and he wants to cancel his appointment..." curly
    msg ja "Haha..." 
    msg ja "So the three of us will have a meeting..." 
    msg ja "I must go as well." 
    call exit(ja)
    jump chat_end


##****************************************************
## You can use the after_ label to do many things. In
## this case, it is used to change the spaceship 
## thoughts
    
label after_popcorn_chat():

    $ space_thoughts.new_choices( [
        SpaceThought(ja, "What I wouldn't give to go home and watch one of Zen's DVDs..."),
        SpaceThought(ju, "Elizabeth the 3rd's safety is the most important thing right now."),
        SpaceThought(s, "My poor Elly... I just want to cuddle her..."),
        SpaceThought(y, "I can't wait to get home and try the new LOLOL expansion."),
        SpaceThought(z, "I wish Mr. Trust Fund would stop talking about his cat."),
        SpaceThought(r, "Oh no... I added too much sugar."),
        SpaceThought(v, "Did I eat breakfast this morning?") 
        ] )
            
    return


##*****************************
## VN Mode after the chatroom
##*****************************
label popcorn_chat_vn_ju():

    # Call this when you start a VN section. It sets some
    # variables for you and shows the right screens
    call vn_begin 
    
    # Use the 'scene' statement to set a background. Here it's also given the
    # 'with fade' modifier so it fades in from black
    scene bg rika_apartment with fade
    pause   # this is so the user has to click before the menu choice shows up
    
    menu:
        "(Heads to the C&R building)":
            # this choice doesn't make anything special happen, so you
            # can write 'pass' to continue on with the VN
            pass    
            
    scene bg black
    pause
    
    # This is how you play sound effects during a VN. 
    # Some are already defined in variables_music_sound.rpy
    play sound car_moving_sfx
    # If you don't specify a speaker, the 'narrator' will say this line
    "(Moving...)"
    
    scene bg cr_meeting_room with fade
    pause
    
    # You set the background music the same way you do for chatrooms
    play music urban_night_cityscape
    
    # This is how you show the characters. Some, like Jumin, have both
    # 'front' and 'side' positions, so you need to specify which one.  
    # In this case, Jumin is shown in his front pose ('jumin front') 
    # with his arm up ('arm') and the happy expression ('happy'). 
    # 'at vn_right' positions him on the right of the screen
    # Check out 'character_definitions.rpy' for a cheat-sheet on 
    # the different expressions and poses available for each character
    show jumin front arm happy at vn_right
    ju "You're here on time, [name]."
    
    # This is an example where Jaehee looks a little too far off-screen 
    # if you use vn_left, so instead she's positioned at vn_midleft. 
    # You might need some trial and error for this
    show jaehee glasses at vn_midleft
    
    # Note the capitalization of the variable [They] 
    # so you get a capitalized pronoun
    ja "[They] arrived much earlier than expected..."
    # Since Jumin is already on the screen, you don't have to specify 
    # 'at' for this expression. The program will remember that he had the
    # attributes front/arm/happy as well and try to find an image that
    # matches as many attributes as it can if you give it a different
    # show statement, so this will match the jumin/front/arm/upset attributes
    show jumin upset
    ju "That's good. Then let's proceed with the meeting."
    hide jaehee
    
    # The program will recognize that Jumin is already showing and will
    # hide him from his previous position at vn_right and show him at
    # vn_center so you don't need to hide Jumin's portrait like Jaehee's
    # was hidden
    show jumin angry at vn_center 
    ju "There are three large issues concerning Elizabeth the 3rd's safety."
    # This is a fun trick -- since Jumin's character ju was declared 
    # with the image tag 'jumin' if you simply add attributes to his
    # say statement, it acts as though you did 'show jumin' + the attribute
    # given. So, this is the same as if you wrote "show jumin upset" before
    # this statement
    ju upset "First, under the sofa. The maid cleans that spot every day, but if some unforeseen danger occurs beneath the sofa, I won't be able to know right away."
    
    # By adding a '-' in front of arm, you can 'subtract' that attribute from
    # his image. Another way to write this might have been 'show jumin 
    # normal angry', if you want his 'normal' outfit instead of
    # his 'arm' one. However, since his 'normal' outfit is also the 
    # default, it suffices to write '-arm'
    ju -arm angry "Second, the gate. The gate needs to be redesigned so that a human can pass through but not a cat. Elizabeth might run out when the door is open. I'm thinking of installing a double door system."
    ju "And lastly, the kitchen. She's climbing up to the bar more and more often. Look at the graph here. Last week, she climbed up there 6.25 times every day on average. I think I need [name]'s opinions on this."
    hide jumin 
    
    # Each time you re-show Jaehee you need to add the 
    # 'glasses' attribute if you want her to wear them.
    show jaehee glasses worried at vn_midleft
    ja "...Should I write all this down?"
    show jumin front angry at vn_right
    ju "Every single word."
    play sound door_knock_sfx
    "(A knock on the door)"
    
    # Now that Jaehee is on screen, you don't need to repeat the
    # 'glasses' attribute if you change her expression. This could also
    # be simplified as `ja surprised "Someone is knocking."`
    show jaehee surprised
    ja "Someone is knocking."
    ju "I can't let anyone interfere with such an important meeting."
    ja worried "Something could have occurred in your home. I'll open the door."
    play sound door_open_sfx
    "(Door opened)"
    ja serious "Come in..."
    hide jumin
    # Note the use of strings here to denote the speaker instead of a
    # Character. This is best used in temporary situations, like in the
    # brief moment before the player knows who the speaker is
    "???" "Oh my~ It's so serious in here."
    show chairman_han at vn_right
    chief_vn "I hope we are not interfering too much."
    ja surprised "Mr. Chairman...! And..."
    hide jaehee
    show sarah excited at vn_midleft
    sarah_vn "I'm Sarah~! We met yesterday, right? Haha! I just came here to say hello."
    chief_vn "I heard that this meeting is very important, so I thought it would be very educational for Sarah here."
    hide sarah
    show jumin side angry at vn_farleft
    ju "You've left your schedule behind to come, how passionate of you."
    chief_vn happy "Haha, no need to be so stern. Sarah, go and sit there."
    hide chairman_han
    hide jumin
    show sarah smirk at vn_center
    sarah_vn "I will~ Oh my, but I don't think I've seen you before. I'm Jumin's fiancee, Sarah! Oh... but your mascara's a bit clumpy. I think you should go to the bathroom and fix it."
    
    play music mysterious_clues_v2
    
    menu:
        extend ''   # You should put this after every menu option; it
                    # will keep the previous line of text on the screen
        "Haha~ Thanks for pointing that out. But Sarah, your hair looks super greasy. You want to go to the bathroom with me?":
            m "Haha~ Thanks for pointing that out. But Sarah, your hair looks super greasy. You want to go to the bathroom with me?"
        # Although this menu has only one option, you can continue to 
        # add menu options and dialogue as you would in a chatroom menu
    
    sarah_vn stressed "What did you say?!"
    hide sarah
    show chairman_han neutral at vn_right
    chief_vn "Is there a problem?"
    show sarah happy at vn_midleft
    sarah_vn "Oh... it's nothing, hahaha."
    hide chairman_han
    show jaehee worried glasses at vn_midright
    ja "Mr. Han... I think we should postpone this meeting."
    sarah_vn excited "What are you talking about~! I won't interfere at all! I'm just happy to see Jumin looking so handsome standing right there~!!"
    hide jaehee
    show chairman_han happy at vn_right
    chief_vn "How kind of you, Jumin. If this meeting isn't that important, why don't you go for a chat with Sarah?"
    sarah_vn happy "I wanted to impress you so I wore all designer clothes. Do you want to take a photo later to commemorate?"
    
    menu:
        extend ''
        "I thought you were wearing clothes from the dollar store... but oh, I see the label. Sorry!":
            m "I thought you were wearing clothes from the dollar store... but oh, I see the label. Sorry!"
            
    sarah_vn stressed "!?!?"
    hide sarah
    show jumin side neutral at vn_farleft
    ju "Father, please take a look at the reports from last quarter since you've come such a long way. There's a pile of documents that need your signature."
    chief_vn neutral "Yes, give them here. I guess I made all of you uncomfortable. I'll be at your office signing the documents, so why don't you talk with Sarah?"
    ju "Alright."
    hide jumin
    show chairman_han happy
    show sarah happy at vn_midleft
    sarah_vn "Mr. Han~ Promise me that we'll have lunch together later on~ Okay~~?"
    chief_vn "Hahaha, of course..."
    hide sarah
    
    # Here there are some different transitions to move the 
    # characters around on the screen
    # You can take a look at Ren'Py's transition and 
    # transformation pages for more
    show jaehee neutral glasses at center with easeinleft
    hide chairman_han with easeoutright
    ja "This way, Mr. Chairman."
    show jaehee at vn_midright with ease
    show jumin side thinking at vn_farleft with easeinleft
    ju "...He's gone."    
    hide jumin
    hide jaehee
    show sarah smirk at vn_center
    
    # Since the player can pick their pronouns, you need to be careful 
    # about verb conjugations
    # If you just wrote "who are [they]" then a player who's picked 
    # she/her pronouns will get a sentence like "but who are she". 
    # Similarly you don't want "but who is they", so you can use 
    # the variable [is_are]
    sarah_vn "Haha... but Jumin, who [is_are] [they]? An intern??"
    hide sarah
    show jaehee surprised glasses at vn_midright
    ja "Are you talking about [name]...? Oh..."
    show jumin side neutral at vn_farleft
    ju "[They_re] my friend."
    ja worried "Something like that..."
    hide jaehee
    hide jumin
    show sarah smirk at vn_center
    
    # You might notice at this point that vn_center is being used to 
    # indicate that Sarah is talking primarily to the player, 
    # while Jaehee and Jumin have a conversation in the background. 
    # This is common in most VN mode conversations in the game
    sarah_vn "Friend~? Are you sure [they_re] just a friend? I feel like [they_re] super jealous..."
    
    menu:
        extend ''
        "Sarah, don't take it the wrong way. Seeing you wear last season's Shanel just reminded me of when I was little, so I guess I wasn't polite enough.":
            m "Sarah, don't take it the wrong way. Seeing you wear last season's Shanel just reminded me of when I was little, so I guess I wasn't polite enough."
      
    show sarah stressed
    sarah_vn "Ha... haha... last season Shanel? This is from the last FW collection. You must have a lot going for you to call that last season."
    show sarah smirk
    sarah_vn "I guess you were super elegant and sensible like me when you were little? But you've grown up to become really nosy and tacky. I should be careful not to end up like that."
    hide sarah
    show jaehee worried glasses at vn_midright
    ja "Sarah... that was a bit..."
    show jumin side neutral at vn_farleft
    ju "...Just leave them. It's fun to watch."
    ja "Mr. Han, I don't think you should call this fun..."
    
    menu:
        extend ''
        "But... where did you get your eyes done? I feel like you got a boob job too.":
            hide jaehee
            hide jumin
            show sarah smirk at vn_center
            m "But... where did you get your eyes done? I feel like you got a boob job too."
    
    show sarah stressed       
    sarah_vn "What?! These are natural!"
    
    menu:
        extend ''
        "I don't think so... But whatever, sure.":
            m "I don't think so... But whatever, sure."
            
    show sarah smirk
    sarah_vn "Ha... hahahaha..."
    hide sarah
    show jaehee worried glasses at vn_midright
    ja "Sarah seems to be really mad right now..."
    show jumin side surprised at vn_farleft
    ju "But [name] looks very collected. Assistant Kang, do you have any popcorn?"
    show jaehee thinking
    ja "I bought some the other day to snack on when working late... I'll bring you some."
    hide jaehee
    hide jumin
    show sarah stressed at vn_center
    sarah_vn "Who do you think you are? Your hair is long and tacky... And your clothes, eww."
    
    menu:
        extend ''
        "Jumin styled my hair himself this morning. I don't need anyone else to approve, so I don't know what to tell you, haha...":
            m "Jumin styled my hair himself this morning. I don't need anyone else to approve, so I don't know what to tell you, haha..."
            
    sarah_vn "What?!?!?!?!? Are you serious?!"
    hide sarah
    show jumin front happy at vn_left
    ju "The popcorn tastes like honey and butter, strange."
    show jaehee happy glasses at vn_midright
    ja "That's been popular these days."
    hide jaehee
    hide jumin
    show sarah stressed at vn_center
    sarah_vn "God... Hey! I don't know who your dad is to be so rude to me in front of Jumin, but the minute I marry him, you'll be out of his life! Just know that!"
    sarah_vn smirk "Jumin... You can't be friends with people like this. It brings you down!"
    
    menu:
        extend ''
        "I think the problem here is that his whole family will be ruined once he marries you.":
            m "I think the problem here is that his whole family will be ruined once he marries you."
    
    sarah_vn stressed "Wow, is there anything you can't say?!"
    hide sarah
    show jaehee surprised glasses at vn_midright
    ja "...Should we stop them?"
    show jumin front happy at vn_left
    ju "[name]'s talented."
    sarah_vn "I'll never let him go!! Let's decide today who gets to live and who dies!! Jumin!!! Argh!! [They_re] pulling my hair!!"
    
    scene bg black with fade
    pause 
    
    # Use this to end the VN section
    jump vn_end
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        