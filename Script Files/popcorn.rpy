
label popcorn_vn:

    call vn_setup
    
    scene bg rika_apartment
    
    menu:
        "(Heads to the C&R building)":
            pass
            
    scene bg black
    
    "(Moving...)"
    
    scene bg cr_meeting_room
    
    show jumin front arm at vn_right
    ju_vn "You're here on time, [name]."
    show jaehee vn at vn_left
    $ cap_pronoun = they.capitalize()
    ja_vn "[cap_pronoun] arrived much earlier than expected..."
    ju_vn "That's good. Then let's proceed with the meeting."
    ju_vn "There are three large issues concerning Elizabeth the 3rd's safety."
    ju_vn "First, under the sofa. The maid cleans that spot every day, but if some unforeseen danger occurs beneath the sofa, I won't be able to know right away."
    ju_vn "Second, the gate. The gate needs to be redesigned so that a human can pass through but not a cat. Elizabeth might run out when the door is open. I'm thinking of installing a double door system."
    ju_vn "And lastly, the kitchen. She's climbing up to the bar more and more often. Look at the graph here. Last week, she climbed up there 6.25 times every day on average. I think I need [name]'s opinions on this."
    ja_vn "...Should I write all this down?"
    ju_vn "Every single word."
    "(!!)"
    ja_vn "Someone is knocking."
    ju_vn "I can't let anyone interfere with such an important meeting."
    ja_vn "Something could have occurred in your home. I'll open the door."
    "(Door opened)"
    ja_vn "Come in..."
    u_vn "Oh my~ It's so serious in here."
    chief_vn "I hope we are not interfering too much."
    ja_vn "Mr. Chairman...! And..."
    sarah_vn "I'm Sarah~! We met yesterday, right? Haha! I just came here to say hello."
    chief_vn "I heard that this meeting is very important, so I thought it would be very educational for Sarah here."
    ju_vn "You've left your schedule behind to come, how passionate of you."
    chief_vn "Haha, no need to be so stern. Sarah, go and sit there."
    sarah_vn "I will~ Oh my, but I don't think I've seen you before. I'm Jumin's fiancee, Sarah! Oh... but your mascara's a bit clumpy. I think you should go to the bathroom and fix it."
    
    menu:
        "Haha~ Thanks for pointing that out. But Sarah, your hair looks super greasy. You want to go to the bathroom with me?":
            m_vn "Haha~ Thanks for pointing that out. But Sarah, your hair looks super greasy. You want to go to the bathroom with me?"
    
    sarah_vn "What did you say?!"
    chief_vn "Is there a problem?"
    sarah_vn "Oh... it's nothing, hahaha."
    ja_vn "Mr. Han... I think we should postpone this meeting."
    sarah_vn "What are you talking about~! I won't interfere at all! I'm just happy to see Jumin looking so handsome standing right there~!!"
    chief_vn "How kind of you, Jumin. If this meeting isn't that important, why don't you go for a chat with Sarah?"
    sarah_vn "I wanted to impress you so I wore all designer clothes. Do you want to take a photo later to commemorate?"
    
    menu:
        "I thought you were wearing clothes from the dollar store... but oh, I see the label. Sorry!":
            m_vn "I thought you were wearing clothes from the dollar store... but oh, I see the label. Sorry!"
            
    sarah_vn "!?!?"
    ju_vn "Father, please take a look at the reports from last quarter since you've come such a long way. There's a pile of documents that need your signature."
    chief_vn "Yes, give them here. I guess I made all of you uncomfortable. I'll be at your office signing the documents, so why don't you talk with Sarah?"
    ju_vn "Alright."
    sarah_vn "Mr. Han~ Promise me that we'll have lunch together later on~ Okay~~?"
    chief_vn "Hahaha, of course..."
    ja_vn "This way, Mr. Chairman."
    ju_vn "...He's gone."
    
    python:
        if persistent.pronoun == "nonbinary":
            $ is_are = "are"
            $ is_are_short = "'re"
        else:
            $ is_are = "is"
            $ is_are_short = "'s"
    
    sarah_vn "Haha... but Jumin, who [is_are] [they]? An intern??"
    ja_vn "Are you talking about [name]...? Oh..."
    ju_vn "[cap_pronoun][is_are_short] my friend."
    ja_vn "Something like that..."
    sarah_vn "Friend~? Are you sure [they][is_are_short] just a friend? I feel like [they][is_are_short] super jealous..."
    
    menu:
        "Sarah, don't take it the wrong way. Seeing you wear last season's Shanel just reminded me of when I was little, so I guess I wasn't polite enough.":
            m_vn "Sarah, don't take it the wrong way. Seeing you wear last season's Shanel just reminded me of when I was little, so I guess I wasn't polite enough."
            
    sarah_vn "Ha... haha... last season Shanel? This is from the last FW collection. You must have a lot going for you to call that last season."
    sarah_vn "I guess you were super elegant and sensible like me when you were little? But you've grown up to become really nosy and tacky. I should be careful not to end up like that."
    ja_vn "Sarah... that was a bit..."
    ju_vn "...Just leave them. It's fun to watch."
    ja_vn "Mr. Han, I don't think you should call this fun..."
    
    menu:
        "But... where did you get your eyes done? I feel like you got a boob job too.":
            m_vn "But... where did you get your eyes done? I feel like you got a boob job too."
            
    sarah_vn "What?! These are natural!"
    
    menu:
        "I don't think so... But whatever, fun.":
            m_vn "I don't think so... But whatever, fun."
            
    sarah_vn "Ha... hahahaha..."
    ja_vn "Sarah seems to be really mad right now..."
    ju_vn "But [name] looks very collected. Assistant Kang, do you have any popcorn?"
    ja_vn "I bought some the other day to snack on when working late... I'll bring you some."
    sarah_vn "Who do you think you are? Your hair is long and tacky... And your clothes, eww."
    
    menu:
        "Jumin styled my hair himself this morning. I don't need anyone else to approve, so I don't know what to tell you, haha...":
            m_vn "Jumin styled my hair himself this morning. I don't need anyone else to approve, so I don't know what to tell you, haha..."
            
    sarah_vn "What?!?!?!?!? Are you serious?!"
    ju_vn "The popcorn tastes like honey and butter, strange."
    ja_vn "That's been popular these days."
    sarah_vn "God... Hey! I don't know who your dad is to be so rude to me in front of Jumin, but the minute I marry him, you'll be out of his life! Just know that!"
    sarah_vn "Jumin... You can't be friends with people like this. It brings you down!"
    
    menu:
        "I think the problem here is that his whole family will be ruined once he marries you.":
            m_vn "I think the problem here is that his whole family will be ruined once he marries you."
    
    sarah_vn "Wow, is there anything you can't say?!"
    ja_vn "...Should we stop them?"
    ju_vn "[cap_pronoun][is_are_short] talented."
    sarah_vn "I'll never let him go!! Let's decide today who gets to live and who dies!! Jumin!!! Argh!! [cap_pronoun][is_are_short] pulling my hair!!"
    
    scene bg black
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        