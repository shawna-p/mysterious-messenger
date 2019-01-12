## This is a fairly standard chatroom. If you're looking for more
## information on how to make the chatrooms, check out Example Chat.rpy
## and Coffee Chat.rpy
## Otherwise, scroll down to the popcorn_vn label
label popcorn_chat:

    call chat_begin("morning")

    play music urban_night_cityscape loop
    
    ju "Zen's written some strange things." 
    ja "{image=jaehee happy}" (img=True)
    ja "There is a meeting with the Women Artists group today." 
    ja "I'm telling you this before you come to the office..." 
    ja "The meeting's agenda will be about the \"Loss of the Muse\" exhibition... Please choose a more artistic tie that will suit today's meeting." 
    ju "{=sser1xb}He's not in his right mind to dream about Elizabeth the 3rd going missing.{/=sser1xb}" 
    ja "Isn't it up to him to dream about whatever he wants?" 
    ja "{image=jaehee well}" (img=True)
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
    ja "{image=jaehee well}" (img=True)
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
    ja "{image=jaehee question}" (img=True)
    ju "Oh..." 
    ju "{size=+10}Good idea!{/size}"   (bounce=True)
    ja "What...;;??" 
    ju "I feel like [name] understands me very well."   (bounce=True, specBubble="cloud_l")
    ju "{image=jumin smile}" (img=True)
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
    ju "{=sser2}Come to the C&R building right away.{/=sser2}" 
    ja "-_-" 
    ja "{image=jaehee well}" (img=True)
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
    ja "{image=jaehee huff}" (img=True)
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
    
    call chat_end   
    


##*****************************
## VN Mode after the chatroom
##*****************************
label popcorn_vn:

    # Call this when you start a VN section. It sets some
    # variables for you and shows the right screens
    call vn_begin
    
    # You'll generally never want to mess with the 'observing' variable yourself, 
    # but since this is a tutorial chatroom we want the user to be able to play
    # it over and over and not be restricted to the choices they've already made
    $ observing = False
    
    # Use the 'scene' statement to set a background. Here it's also given the
    # 'with fade' modifier so it fades in from black
    scene bg rika_apartment with fade
    pause   # this is so the user has to click before the menu choice shows up
    
    menu:
        "(Heads to the C&R building)":
            pass    # this choice doesn't make anything special happen, so we
                    # say 'pass' to continue on with the VN
            
    scene bg black
    pause
    
    # This is how you'll play sound effects during a VN. Some are already defined in VN Mode.rpy
    play sound car_moving_sfx
    # If you don't specify a speaker, the 'narrator' will say this line
    "(Moving...)"
    
    scene bg cr_meeting_room with fade
    pause
    
    # You'll set the background music the same way you do for chatrooms
    play music urban_night_cityscape loop
    
    # This is how we show the characters. Some, like Jumin, have both 'front' and 'side' positions,
    # so we need to specify which one. If a major character only has one pose, we generally follow it
    # with 'vn' as in 'jaehee vn'. 
    # In this case, we're showing Jumin in his front pose ('jumin front') with his arm up ('arm') and
    # the happy expression ('happy'). We say 'at vn_right' to put him on the right of the screen
    # Check out 'character definitions.rpy' for a cheat-sheet on the different expressions and poses
    # available for each character
    show jumin front arm happy at vn_right
    ju_vn "You're here on time, [name]."
    
    # This is an example where Jaehee looks a little too far off-screen if we use vn_left,
    # so instead we put her at vn_midleft. You might need some trial and error for this
    show jaehee vn glasses at vn_midleft
    
    # Note the capitalization of the variable [They] so you get a capitalized pronoun
    ja_vn "[They] arrived much earlier than expected..."
    show jumin front upset  # since Jumin is already on the screen, we don't have to specify 'at' for this expression
    ju_vn "That's good. Then let's proceed with the meeting."
    hide jaehee vn
    
    # The program will recognize that Jumin is already showing and will hide him from his previous position at
    # vn_right and show him at vn_center so we don't need to hide Jumin's portrait like we did Jaehee
    show jumin front angry at vn_center 
    ju_vn "There are three large issues concerning Elizabeth the 3rd's safety."
    show jumin front upset
    ju_vn "First, under the sofa. The maid cleans that spot every day, but if some unforeseen danger occurs beneath the sofa, I won't be able to know right away."
    
    # By adding a '-' in front of arm, we 'subtract' that attribute from his image. Another way to write this
    # might have been 'show jumin front normal angry', since we want his 'normal' outfit instead of his 'arm' one
    # However, since his 'normal' outfit is also the default, it suffices to write '-arm'
    show jumin front -arm angry
    ju_vn "Second, the gate. The gate needs to be redesigned so that a human can pass through but not a cat. Elizabeth might run out when the door is open. I'm thinking of installing a double door system."
    ju_vn "And lastly, the kitchen. She's climbing up to the bar more and more often. Look at the graph here. Last week, she climbed up there 6.25 times every day on average. I think I need [name]'s opinions on this."
    hide jumin front
    
    # Each time we show Jaehee we'll need to add the 'glasses' attribute if we want her to wear them.
    show jaehee vn glasses worried at vn_midleft
    ja_vn "...Should I write all this down?"
    show jumin front angry at vn_right
    ju_vn "Every single word."
    # KNOCK SFX
    "(!!)"
    
    # Now that Jaehee is on screen, we don't need to repeat the 'glasses' attribute if we change her expression
    show jaehee vn surprised
    ja_vn "Someone is knocking."
    ju_vn "I can't let anyone interfere with such an important meeting."
    show jaehee vn worried
    ja_vn "Something could have occurred in your home. I'll open the door."
    # DOOR OPEN SFX
    "(Door opened)"
    show jaehee vn serious
    ja_vn "Come in..."
    hide jumin front
    u_vn "Oh my~ It's so serious in here."
    show chairman_han at vn_right
    chief_vn "I hope we are not interfering too much."
    show jaehee vn surprised
    ja_vn "Mr. Chairman...! And..."
    hide jaehee vn
    show sarah excited at vn_midleft
    sarah_vn "I'm Sarah~! We met yesterday, right? Haha! I just came here to say hello."
    chief_vn "I heard that this meeting is very important, so I thought it would be very educational for Sarah here."
    hide sarah
    show jumin side angry at vn_farleft
    ju_vn "You've left your schedule behind to come, how passionate of you."
    show chairman_han happy 
    chief_vn "Haha, no need to be so stern. Sarah, go and sit there."
    hide chairman_han
    hide jumin side
    show sarah smirk at vn_center
    sarah_vn "I will~ Oh my, but I don't think I've seen you before. I'm Jumin's fiancee, Sarah! Oh... but your mascara's a bit clumpy. I think you should go to the bathroom and fix it."
    
    play music mysterious_clues_v2 loop
    
    menu:
        extend ''   # you'll want to put this after every menu option; it will keep the previous line of text on the screen
        "Haha~ Thanks for pointing that out. But Sarah, your hair looks super greasy. You want to go to the bathroom with me?":
            m_vn "Haha~ Thanks for pointing that out. But Sarah, your hair looks super greasy. You want to go to the bathroom with me?"
        # Although this menu has only one option, you can continue to add menu options and dialogue as you would in a chatroom menu
    
    show sarah stressed
    sarah_vn "What did you say?!"
    hide sarah
    show chairman_han neutral at vn_right
    chief_vn "Is there a problem?"
    show sarah happy at vn_midleft
    sarah_vn "Oh... it's nothing, hahaha."
    hide chairman_han
    show jaehee vn worried glasses at vn_midright
    ja_vn "Mr. Han... I think we should postpone this meeting."
    show sarah excited
    sarah_vn "What are you talking about~! I won't interfere at all! I'm just happy to see Jumin looking so handsome standing right there~!!"
    hide jaehee vn
    show chairman_han happy at vn_right
    chief_vn "How kind of you, Jumin. If this meeting isn't that important, why don't you go for a chat with Sarah?"
    show sarah happy
    sarah_vn "I wanted to impress you so I wore all designer clothes. Do you want to take a photo later to commemorate?"
    
    menu:
        extend ''
        "I thought you were wearing clothes from the dollar store... but oh, I see the label. Sorry!":
            m_vn "I thought you were wearing clothes from the dollar store... but oh, I see the label. Sorry!"
            
    show sarah stressed
    sarah_vn "!?!?"
    hide sarah
    show jumin side neutral at vn_farleft
    ju_vn "Father, please take a look at the reports from last quarter since you've come such a long way. There's a pile of documents that need your signature."
    show chairman_han neutral
    chief_vn "Yes, give them here. I guess I made all of you uncomfortable. I'll be at your office signing the documents, so why don't you talk with Sarah?"
    ju_vn "Alright."
    hide jumin side
    show chairman_han happy
    show sarah happy at vn_midleft
    sarah_vn "Mr. Han~ Promise me that we'll have lunch together later on~ Okay~~?"
    chief_vn "Hahaha, of course..."
    hide sarah
    
    # Here we have some different transitions to move the characters around on the screen
    # You can take a look at Ren'Py's transition and transformation pages for more
    show jaehee vn neutral glasses at center with easeinleft
    hide chairman_han with easeoutright
    ja_vn "This way, Mr. Chairman."
    show jaehee vn at vn_midright with ease
    show jumin side thinking at vn_farleft with easeinleft
    ju_vn "...He's gone."    
    hide jumin side
    hide jaehee vn
    show sarah smirk at vn_center
    
    # Since we let the player pick their pronouns, we need to be careful about verb conjugations
    # If we just wrote "who are [they]" then a player who's picked she/her pronouns will get a sentence
    # like "but who are she". Similarly we don't want "but who is they", so we use the variable [is_are]
    sarah_vn "Haha... but Jumin, who [is_are] [they]? An intern??"
    hide sarah
    show jaehee vn surprised glasses at vn_midright
    ja_vn "Are you talking about [name]...? Oh..."
    show jumin side neutral at vn_farleft
    ju_vn "[They_re] my friend."
    show jaehee vn worried
    ja_vn "Something like that..."
    hide jaehee vn
    hide jumin side
    show sarah smirk at vn_center
    
    # You might notice at this point that we're using vn_center to indicate that Sarah is talking primarily to us,
    # the player, while Jaehee and Jumin have a conversation in the background. This is common in most VN mode
    # conversations in the game
    sarah_vn "Friend~? Are you sure [they_re] just a friend? I feel like [they_re] super jealous..."
    
    menu:
        extend ''
        "Sarah, don't take it the wrong way. Seeing you wear last season's Shanel just reminded me of when I was little, so I guess I wasn't polite enough.":
            m_vn "Sarah, don't take it the wrong way. Seeing you wear last season's Shanel just reminded me of when I was little, so I guess I wasn't polite enough."
      
    show sarah stressed
    sarah_vn "Ha... haha... last season Shanel? This is from the last FW collection. You must have a lot going for you to call that last season."
    show sarah smirk
    sarah_vn "I guess you were super elegant and sensible like me when you were little? But you've grown up to become really nosy and tacky. I should be careful not to end up like that."
    hide sarah
    show jaehee vn worried glasses at vn_midright
    ja_vn "Sarah... that was a bit..."
    show jumin side neutral at vn_farleft
    ju_vn "...Just leave them. It's fun to watch."
    ja_vn "Mr. Han, I don't think you should call this fun..."
    
    menu:
        extend ''
        "But... where did you get your eyes done? I feel like you got a boob job too.":
            hide jaehee vn
            hide jumin side
            show sarah smirk at vn_center
            m_vn "But... where did you get your eyes done? I feel like you got a boob job too."
    
    show sarah stressed       
    sarah_vn "What?! These are natural!"
    
    menu:
        extend ''
        "I don't think so... But whatever, sure.":
            m_vn "I don't think so... But whatever, sure."
            
    show sarah smirk
    sarah_vn "Ha... hahahaha..."
    hide sarah
    show jaehee vn worried glasses at vn_midright
    ja_vn "Sarah seems to be really mad right now..."
    show jumin side surprised at vn_farleft
    ju_vn "But [name] looks very collected. Assistant Kang, do you have any popcorn?"
    show jaehee vn thinking
    ja_vn "I bought some the other day to snack on when working late... I'll bring you some."
    hide jaehee vn
    hide jumin side
    show sarah stressed at vn_center
    sarah_vn "Who do you think you are? Your hair is long and tacky... And your clothes, eww."
    
    menu:
        extend ''
        "Jumin styled my hair himself this morning. I don't need anyone else to approve, so I don't know what to tell you, haha...":
            m_vn "Jumin styled my hair himself this morning. I don't need anyone else to approve, so I don't know what to tell you, haha..."
            
    sarah_vn "What?!?!?!?!? Are you serious?!"
    hide sarah
    show jumin front happy at vn_left
    ju_vn "The popcorn tastes like honey and butter, strange."
    show jaehee vn happy glasses at vn_midright
    ja_vn "That's been popular these days."
    hide jaehee vn
    hide jumin front
    show sarah stressed at vn_center
    sarah_vn "God... Hey! I don't know who your dad is to be so rude to me in front of Jumin, but the minute I marry him, you'll be out of his life! Just know that!"
    show sarah smirk
    sarah_vn "Jumin... You can't be friends with people like this. It brings you down!"
    
    menu:
        extend ''
        "I think the problem here is that his whole family will be ruined once he marries you.":
            m_vn "I think the problem here is that his whole family will be ruined once he marries you."
    
    show sarah stressed
    sarah_vn "Wow, is there anything you can't say?!"
    hide sarah
    show jaehee vn surprised glasses at vn_midright
    ja_vn "...Should we stop them?"
    show jumin front happy at vn_left
    ju_vn "[name]'s talented."
    sarah_vn "I'll never let him go!! Let's decide today who gets to live and who dies!! Jumin!!! Argh!! [They_re] pulling my hair!!"
    
    scene bg black with fade
    pause 
    
    # Use this to end the VN section
    call vn_end
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        