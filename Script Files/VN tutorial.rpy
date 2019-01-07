
default menutext = ''
  

label vn_mode_tutorial:

    # Make sure you call this at the start of a VN section
    call vn_setup
    
    # You use the "scene" command to set up the background of the VN section
    # It clears away any character sprites you have left showing and sets
    # the background to your desired image
    scene bg mint_eye_room
    
    # You'll generally never want to mess with the 'observing' variable yourself, 
    # but since this is a tutorial chatroom we want the user to be able to play
    # it over and over and not be restricted to the choices they've already made
    $ observing = False
    
    show saeran vn smile
    r_vn "Hello! Welcome to Visual Novel mode."
    show saeran vn -smile   # the -smile puts him in his 'neutral' expression
    r_vn "This mode is most similar to what you'll find in the majority of Ren'Py projects."
    show saeran vn happy
    r_vn "There are a couple of things to show you about VN mode. What would you like to learn about first?"
    
    # This menutext variable is a sort of work-around so that I can show different
    # text during the menu, even though the options are the same
    $ menutext = "There are a couple of things to show you about VN mode. What would you like to learn about first?"
    jump vn_tutorial
  
##************************************
## Tutorial Menu
##************************************    
label vn_tutorial():
    menu:
        r_vn '[menutext]{fast}'
        
        "How do I get different expressions and outfits?":
            m_vn "How do I get different expressions and outfits?"
            show saeran vn smile
            r_vn "Good question!"
            jump vn_layeredimage
        
        "How can I position characters on the screen?":
            m_vn "How can I position characters on the screen?"
            show saeran vn smile
            r_vn "Moving characters around is quite easy!"
            jump vn_position
            
        "How do I write a VN mode section?":
            m_vn "How do I write a VN mode section?"
            show saeran vn distant
            r_vn "Oh, of course! It's pretty easy, I promise."
            jump vn_writing
            
        "I want to look at all the available characters.":
            m_vn "I want to look at all the available characters."
            show saeran vn smile
            r_vn "Sure! Who do you want to see?"
            jump vn_showcase
            
        "That's enough explanation, thanks.":
            m_vn "That's enough explanation, thanks."
            r_vn "Alright! Hope this helped you."
            call vn_end # Call this to end the VN Mode section
            
    show saeran vn happy
    
##************************************
## Writing a VN mode section
##************************************  
label vn_writing:
    show saeran vn saeran neutral
    r_vn """
    Writing a VN section is pretty straightforward.
    
    First, you'll define a label, and then you can start adding dialogue and characters!
    
    This part works in the 'traditional' Ren'Py manner, so if you're not sure how to start adding characters and dialogue,
    
    I'd recommend checking out the LemmaSoft forums and looking through the code in VN Mode.rpy
    
    If you don't plan to change the speaking character's expression for a while,
    
    you can also look into Ren'Py's \"monologue\" feature, which you can see an example of in the code for this VN section.
    """
    show saeran vn saeran smile
    r_vn """
    Other than that, there are three buttons on the screen in VN mode -- {b}Auto{/b}, {b}Skip{/b}, and {b}Log{/b}.
    
    {b}Auto{/b} is unique to this program. When selected, it will automatically advance the text for you.
    
    You can adjust the auto-forward speed in Settings.
    
    Keep in mind that this will also affect how fast phone call text will auto-advance.
    
    {b}Skip{/b} will start fast-forwarding you through the text,
    
    and {b}Log{/b} will show you a log of the dialogue history.
    """
    show saeran vn thinking
    $ menutext = "Is there anything else you'd like to learn more about?"
    jump vn_tutorial
    
##************************************
## Changing Expressions & Outfits
##************************************  
label vn_layeredimage:

    show saeran vn happy
    r_vn "To get different expressions and outfits, we make a lot of use of Ren'Py's {b}layeredimage{/b} feature."
    show saeran vn unknown neutral
    r_vn "It lets me change outfits and expressions very quickly just by adding the appropriate tags."
    show saeran vn mask happy
    r_vn "For example, the attributes used to display this sprite are {b}mask{/b} and {b}happy{/b}."
    show saeran vn unknown blush
    r_vn "Not all expressions are available with the mask on, however, like this one."
    show saeran vn suit nervous
    r_vn "Some characters have many outfits, and some have multiple poses as well."
    show saeran vn at vn_left with ease
    show v side at vn_midright with easeinright
    r_vn "Some characters also have 'accessories' like glasses."
    hide saeran vn with easeoutleft
    show v side at default with ease
    r_vn "We'll show you what I mean with V."
    
    show v side happy
    pause 1.0
    show v side happy short_hair
    pause 1.0
    show v side happy long_hair glasses
    pause 1.0
    show v side happy long_hair -glasses
    pause 1.0
    show v side thinking glasses
    pause 1.0
    show v side thinking -glasses
    pause 1.0
    show v side neutral glasses
    pause 1.0
    show v side neutral -glasses
    
    v_vn "As you can see, there are several expressions both with and without my sunglasses."
    show v front mint_eye
    v_vn "I also have a 'hood' accessory for the {b}mint_eye{/b} outfit."
    show v front mint_eye hood_up
    v_vn "The attribute {b}hood_up{/b}, when used with the {b}mint_eye{/b} attribute, will put the hood up."
    show v front arm talking
    v_vn "You'll get an error if you try to use the hood attribute when I'm not wearing my Mint Eye cloak, however."
    
    hide v with easeoutright
    show saeran vn happy with easeinleft
    
    r_vn "You'll want to take a look at the 'cheat sheet' in {b}character definitions.rpy{/b} that tells you all the expressions and accessories available to each character."
    r_vn "Anything else you'd like to know about?"
    $ menutext = "Anything else you'd like to know about?"
    jump vn_tutorial
    
##************************************
## Positioning Characters
##************************************  
label vn_position:
    r_vn "You might have noticed before, but you can position the characters in the middle,"
    r_vn "or to the left and right sides of the screen."
    show saeran vn at vn_left with ease
    r_vn "This position is called {b}vn_left{/b}."
    show saeran vn at vn_right with ease
    r_vn "This is {b}vn_right{/b}."
    show saeran vn at vn_midleft with ease
    r_vn "This is {b}vn_midleft{/b}."
    show saeran vn at vn_midright with ease
    r_vn "And this is {b}vn_midright{/b}."
    show saeran vn at default with ease
    r_vn "The default position is just called {b}default{/b}, and characters will appear there if you don't specify a different location."
    show saeran vn thinking
    r_vn "Know that not all positions will look right for each character;"
    r_vn "sometimes they'll be too far off-screen if you use {b}vn_left{/b}, so you'll need to use {b}vn_midleft{/b} instead."
    r_vn "You can always define your own transforms to position the characters exactly how you want, too."
    show saeran vn neutral
    r_vn "Anything else you'd like to learn about?"
    $ menutext = "Anything else you'd like to learn about?"
    jump vn_tutorial
    
    
##************************************
## Changing Outfits/Expressions:
## Examples
##************************************  
menu vn_showcase:

    "Who would you like to see?"
    
    "Major Characters":
        jump vn_showcase_major1
    
    "Minor Characters":
        jump vn_showcase_minor1
        
    "I'm done viewing characters":
        jump vn_tutorial
    
menu vn_showcase_major1:

    "Who would you like to see?"
    
    "Jaehee":
        jump jaehee_showcase
    
    "Jumin":
        jump jumin_showcase
    
    "Rika":
        jump rika_showcase
    
    "Seven":
        jump seven_showcase
    
    "More ->":
        jump vn_showcase_major2
    
menu vn_showcase_major2:
    
    "Who would you like to see?"
    
    "<- Back":
        jump vn_showcase_major1
    
    "Saeran":
        jump saeran_showcase
    
    "V":
        jump v_showcase
    
    "Yoosung":
        jump yoosung_showcase
    
    "Zen":
        jump zen_showcase
    
menu vn_showcase_minor1:

    "Who would you like to see?"
    
    "Bodyguards":
        jump bodyguards_showcase
    
    "Chairman Han":
        jump chairman_showcase
    
    "Echo Girl":
        jump echo_showcase
    
    "Glam Choi":
        jump glam_showcase
    
    "More ->":
        jump vn_showcase_minor2
    
menu vn_showcase_minor2:

    "Who would you like to see?"
    
    "<- Back":
        jump vn_showcase_minor1
    
    "Prime Minister":
        jump minister_showcase
    
    "Sarah Choi":
        jump sarah_showcase
    
    "Vanderwood":
        jump vanderwood_showcase
        
#************************
# Major Characters
#************************

label jaehee_showcase:
    hide saeran vn
    show jaehee vn glasses
    ja_vn "Hello! I have several outfits and expressions to show you."
    show jaehee vn glasses sparkle arm
    ja_vn "First, I'll show you the expressions I have with my glasses."
    show jaehee vn glasses happy -arm
    pause 0.8
    show jaehee vn glasses sad
    pause 0.8
    show jaehee vn glasses neutral
    pause 0.8
    show jaehee vn glasses thinking
    pause 0.8
    show jaehee vn glasses worried
    pause 0.8
    show jaehee vn glasses angry
    pause 0.8
    show jaehee vn glasses sparkle
    pause 0.8
    show jaehee vn glasses serious
    pause 0.8
    show jaehee vn glasses surprised
    ja_vn "And now I'll show you the expressions I have without my glasses."
    show jaehee vn happy -glasses
    pause 0.8
    show jaehee vn sad
    pause 0.8
    show jaehee vn neutral
    pause 0.8
    show jaehee vn thinking
    pause 0.8
    show jaehee vn worried
    pause 0.8
    show jaehee vn neutral
    ja_vn "These are my available outfits."
    show jaehee vn normal
    pause 0.8
    show jaehee vn arm
    pause 0.8
    show jaehee vn party
    pause 0.8
    show jaehee vn dress
    pause 0.8
    show jaehee vn apron
    ja_vn "That is all from me."
    hide jaehee vn
    jump vn_showcase
    
label jumin_showcase:
    hide saeran vn
    show jumin front
    ju_vn "Hello. You can view my outfits and poses here."
    ju_vn "First, here are the expressions I have in my 'front' pose."
    show jumin front happy
    pause 0.8
    show jumin front upset
    pause 0.8
    show jumin front blush
    pause 0.8
    show jumin front neutral
    pause 0.8
    show jumin front surprised
    pause 0.8
    show jumin front angry
    pause 0.8
    show jumin front sad
    pause 0.8
    show jumin front unsure
    pause 0.8
    show jumin front thinking
    pause 0.8
    show jumin front neutral
    ju_vn "And here are my available outfits."
    show jumin front 
    pause 0.8
    show jumin front arm
    pause 0.8
    show jumin front party
    pause 0.8
    ju_vn "I also have a second position."
    show jumin side
    ju_vn "These are the available expressions."
    show jumin side happy
    pause 0.8
    show jumin side upset
    pause 0.8
    show jumin side blush
    pause 0.8
    show jumin side neutral
    pause 0.8
    show jumin side surprised
    pause 0.8
    show jumin side angry
    pause 0.8
    show jumin side thinking
    pause 0.8
    show jumin side worried
    pause 0.8
    show jumin side neutral
    ju_vn "And here are the available outfits."
    show jumin side normal
    pause 0.8
    show jumin side suit
    pause 0.8
    ju_vn "That is all."
    hide jumin side
    jump vn_showcase
    
label rika_showcase:
    hide saeran vn
    show rika vn happy
    ri_vn "Hello~! You've come to see my expressions and outfits, right?"
    show rika vn -happy
    ri_vn "I'll show you my expressions, first."
    show rika vn happy
    pause 0.8
    show rika vn sad
    pause 0.8
    show rika vn neutral
    pause 0.8
    show rika vn thinking
    pause 0.8
    show rika vn worried
    pause 0.8
    show rika vn dark
    pause 0.8
    show rika vn angry
    pause 0.8
    show rika vn sob
    pause 0.8
    show rika vn crazy
    pause 0.8
    show rika vn neutral
    pause 0.8
    ri_vn "And these are my available outfits."
    show rika vn normal
    pause 0.8
    show rika vn savior
    pause 0.8
    show rika vn dress
    pause 0.8
    ri_vn "I also have a mask accessory available to me."
    show rika vn dress mask
    pause 0.8
    show rika vn dress -mask
    ri_vn "That's all from me!"
    hide rika vn
    jump vn_showcase
    
label seven_showcase:
    hide saeran vn
    show seven front
    s_vn "Hey hey hey~! I get to show off my expressions, hmm~?"
    s_vn "Here they are!"
    show seven front happy
    pause 0.8
    show seven front blush
    pause 0.8
    show seven front neutral
    pause 0.8
    show seven front surprised
    pause 0.8
    show seven front serious
    pause 0.8
    show seven front thinking
    pause 0.8
    show seven front sad
    pause 0.8
    show seven front worried
    pause 0.8
    show seven front dark
    pause 0.8
    show seven front angry
    pause 0.8
    show seven front hurt
    pause 0.8
    show seven front neutral
    pause 0.8
    s_vn "And here are my outfits~"
    show seven front normal
    pause 0.8
    show seven front arm
    pause 0.8
    show seven front party
    pause 0.8
    s_vn "I have another pose, too!"
    show seven side
    pause 0.8
    s_vn "Here are the expressions for this pose."
    show seven side happy
    pause 0.8
    show seven side concern
    pause 0.8
    show seven side surprised
    pause 0.8
    show seven side thinking
    pause 0.8
    show seven side sad
    pause 0.8
    show seven side neutral
    pause 0.8
    show seven side dark
    pause 0.8
    show seven side angry
    pause 0.8
    show seven side worried
    pause 0.8
    show seven side neutral
    pause 0.8
    s_vn "And here are the outfits."
    show seven side normal
    pause 0.8
    show seven side arm
    pause 0.8
    show seven side suit
    pause 0.8
    s_vn "That's it! Enjoy the rest of the program~"
    hide seven side
    jump vn_showcase
    
label saeran_showcase:
    r_vn "Oh, me?"
    r_vn "Okay. I have several different expressions."
    show saeran vn happy
    pause 0.8
    show saeran vn smile
    pause 0.8
    show saeran vn neutral
    pause 0.8
    show saeran vn angry
    pause 0.8
    show saeran vn thinking
    pause 0.8
    show saeran vn tense
    pause 0.8
    show saeran vn creepy
    pause 0.8
    show saeran vn cry
    pause 0.8
    show saeran vn blush
    pause 0.8
    show saeran vn sob
    pause 0.8
    show saeran vn teary
    pause 0.8
    show saeran vn nervous
    pause 0.8
    show saeran vn sad
    pause 0.8
    show saeran vn worried
    pause 0.8
    show saeran vn distant
    pause 0.8
    show saeran vn neutral
    pause 0.8
    r_vn "And then I have many outfits, too."
    show saeran vn ray
    pause 0.8
    show saeran vn saeran
    pause 0.8
    show saeran vn suit
    pause 0.8
    show saeran vn unknown
    pause 0.8
    show saeran vn mask
    pause 0.8
    r_vn "This outfit has fewer expressions than the other outfits since my face is partially covered"
    show saeran vn happy mask
    pause 0.8
    show saeran vn smile mask
    pause 0.8
    show saeran vn neutral mask
    pause 0.8
    show saeran vn angry mask
    pause 0.8
    show saeran vn thinking mask
    pause 0.8
    show saeran vn tense mask
    pause 0.8
    show saeran vn creepy mask
    pause 0.8
    show saeran vn ray smile
    r_vn "Hope that's what you were looking for!"
    jump vn_showcase
    
label v_showcase:
    hide saeran vn
    show v front
    v_vn "Hello there."
    v_vn "I'm told I'm supposed to show you my expressions."
    show v front neutral
    pause 0.8
    show v front happy
    pause 0.8
    show v front angry
    pause 0.8
    show v front worried
    pause 0.8
    show v front thinking
    pause 0.8
    show v front talking
    pause 0.8
    show v front surprised
    pause 0.8
    show v front tense
    pause 0.8
    show v front sweating
    pause 0.8
    show v front sad
    pause 0.8
    show v front upset
    pause 0.8
    show v front concerned
    pause 0.8
    show v front regret
    pause 0.8
    show v front unsure
    pause 0.8
    show v front afraid
    pause 0.8
    show v front neutral
    pause 0.8
    v_vn "And then here are my outfits."
    show v front normal
    pause 0.8
    show v front arm
    pause 0.8
    show v front hair_normal
    pause 0.8
    show v front hair_arm
    pause 0.8
    show v front mint_eye
    pause 0.8
    v_vn "I also have a hood accessory with this outfit."
    show v front mint_eye hood_down
    pause 0.8
    show v front mint_eye hood_up
    pause 0.8
    show v front mint_eye hood_down
    pause 0.8
    v_vn "And then I have a side pose, too."
    show v side
    pause 0.8
    v_vn "Here are the poses for this pose."
    pause 0.8
    show v side happy
    pause 0.8
    show v side angry
    pause 0.8
    show v side neutral
    pause 0.8
    show v side surprised
    pause 0.8
    show v side thinking
    pause 0.8
    show v side worried
    pause 0.8
    show v side sweat
    pause 0.8
    show v side shock
    pause 0.8
    show v side afraid
    pause 0.8
    show v side blush
    pause 0.8
    show v side sad
    pause 0.8
    show v side unsure
    pause 0.8
    show v side neutral
    pause 0.8
    v_vn "All of these expressions also have a version with sunglasses."
    show v side glasses happy
    pause 0.8
    show v side glasses angry
    pause 0.8
    show v side glasses neutral
    pause 0.8
    show v side glasses surprised
    pause 0.8
    show v side glasses thinking
    pause 0.8
    show v side glasses worried
    pause 0.8
    show v side glasses sweat
    pause 0.8
    show v side glasses shock
    pause 0.8
    show v side glasses afraid
    pause 0.8
    show v side glasses blush
    pause 0.8
    show v side glasses sad
    pause 0.8
    show v side glasses unsure
    pause 0.8
    show v side glasses neutral
    pause 0.8
    v_vn "And then I have different outfits for this position."
    show v side normal
    pause 0.8
    show v side short_hair
    pause 0.8
    show v side long_hair
    pause 0.8
    v_vn "And that's all. Please enjoy the program."
    hide v side
    jump vn_showcase
    
label yoosung_showcase:
    hide saeran vn
    show yoosung vn happy
    y_vn "Hi! It's nice to see you~"
    y_vn "I can show you the expressions I have in VN mode."
    show yoosung vn happy
    pause 0.8
    show yoosung vn neutral
    pause 0.8
    show yoosung vn thinking
    pause 0.8
    show yoosung vn surprised
    pause 0.8
    show yoosung vn sparkle
    pause 0.8
    show yoosung vn angry
    pause 0.8
    show yoosung vn sad
    pause 0.8
    show yoosung vn dark
    pause 0.8
    show yoosung vn tired
    pause 0.8
    show yoosung vn upset
    pause 0.8
    show yoosung vn happy
    pause 0.8
    y_vn "I've also got a set of expressions when I'm wearing glasses."
    show yoosung vn glasses happy
    pause 0.8
    show yoosung vn glasses neutral
    pause 0.8
    show yoosung vn glasses thinking
    pause 0.8
    show yoosung vn glasses surprised
    pause 0.8
    show yoosung vn glasses sparkle
    pause 0.8
    show yoosung vn happy -glasses
    pause 0.8
    y_vn "And here are my outfits!"
    show yoosung vn normal
    pause 0.8
    show yoosung vn arm
    pause 0.8
    show yoosung vn sweater
    pause 0.8
    show yoosung vn suit
    pause 0.8
    show yoosung vn party
    pause 0.8
    show yoosung vn bandage
    pause 0.8
    y_vn "I've only got a few expressions when I have the bandage."
    show yoosung vn bandage happy
    pause 0.8
    show yoosung vn bandage neutral
    pause 0.8
    show yoosung vn bandage thinking
    pause 0.8
    show yoosung vn normal happy
    pause 0.8
    y_vn "That's all! Have fun with the program~!"
    hide yoosung vn
    jump vn_showcase
    
label zen_showcase:
    hide saeran vn
    show zen front happy
    z_vn "Hey babe~ Glad you came by!"
    z_vn "Here are my available expressions!"
    show zen front happy
    pause 0.8
    show zen front angry
    pause 0.8
    show zen front blush
    pause 0.8
    show zen front wink
    pause 0.8
    show zen front neutral
    pause 0.8
    show zen front surprised
    pause 0.8
    show zen front thinking
    pause 0.8
    show zen front worried
    pause 0.8
    show zen front oh
    pause 0.8
    show zen front upset
    pause 0.8
    show zen front neutral
    pause 0.8
    z_vn "I've got a few outfits for this front pose, too."
    show zen front arm
    pause 0.8
    show zen front party
    pause 0.8
    show zen front normal
    pause 0.8
    z_vn "Handsome, aren't I?"
    z_vn "Anyway, here are my side expressions."
    show zen side happy
    pause 0.8
    show zen side angry
    pause 0.8
    show zen side blush
    pause 0.8
    show zen side wink
    pause 0.8
    show zen side surprised
    pause 0.8
    show zen side thinking
    pause 0.8
    show zen side worried
    pause 0.8
    show zen side upset
    pause 0.8
    show zen side neutral
    pause 0.8
    z_vn "And then a few more outfits."
    show zen side suit
    pause 0.8
    show zen side normal
    pause 0.8
    z_vn "And that's it! Enjoy the program, hon~"
    hide zen side
    jump vn_showcase
    
#************************
# Minor Characters
#************************
    
label bodyguards_showcase:
    hide saeran vn
    show bodyguard_front at vn_left
    show bodyguard_side at vn_right
    "If you'd like the minor characters to speak, you'll need to define your own character for them."
    "It's pretty easy; just go to {b}character definitions.rpy{/b} and follow the guidelines there."
    "The bodyguards only have two other expressions:"
    show bodyguard_front thinking
    show bodyguard_side thinking
    pause 1.0
    show bodyguard_front stressed
    show bodyguard_side stressed
    pause 1.0
    "And that's all."
    hide bodyguard_side
    hide bodyguard_front
    jump vn_showcase
    
    
label chairman_showcase:
    hide saeran vn
    show chairman_han 
    "If you'd like the minor characters to speak, you'll need to define your own character for them."
    "It's pretty easy; just go to {b}character definitions.rpy{/b} and follow the guidelines there."
    "Chairman Han has the following expressions:"
    show chairman_han happy
    pause 0.8
    show chairman_han thinking
    pause 0.8
    show chairman_han stressed
    pause 0.8
    show chairman_han neutral
    pause 0.8
    "That's all."
    hide chairman_han
    jump vn_showcase

label echo_showcase:
    hide saeran vn
    show echo_girl 
    "If you'd like the minor characters to speak, you'll need to define your own character for them."
    "It's pretty easy; just go to {b}character definitions.rpy{/b} and follow the guidelines there."
    "Echo Girl has the following expressions:"
    show echo_girl happy
    pause 0.8
    show echo_girl angry
    pause 0.8
    show echo_girl smile
    pause 0.8
    show echo_girl surprised
    pause 0.8
    show echo_girl neutral
    pause 0.8
    "That's all."
    hide echo_girl
    jump vn_showcase
    
    
label glam_showcase:  
    hide saeran vn
    show glam_choi 
    "If you'd like the minor characters to speak, you'll need to define your own character for them."
    "It's pretty easy; just go to {b}character definitions.rpy{/b} and follow the guidelines there."
    "Glam Choi has the following expressions:"
    show glam_choi happy
    pause 0.8
    show glam_choi smirk
    pause 0.8
    show glam_choi thinking
    pause 0.8
    show glam_choi stressed
    pause 0.8
    show glam_choi worried
    pause 0.8
    show glam_choi neutral
    pause 0.8
    "And that's all."
    hide glam_choi
    jump vn_showcase
    
label minister_showcase:    
    hide saeran vn
    show prime_minister
    "If you'd like the minor characters to speak, you'll need to define your own character for them."
    "It's pretty easy; just go to {b}character definitions.rpy{/b} and follow the guidelines there."
    "The Prime Minister only has one expression, the one currently showing."
    "That's all."
    hide prime_minister
    jump vn_showcase    
    
label sarah_showcase:    
    hide saeran vn
    show sarah 
    "If you'd like the minor characters to speak, you'll need to define your own character for them."
    "It's pretty easy; just go to {b}character definitions.rpy{/b} and follow the guidelines there."
    "Sarah has the following expressions:"
    show sarah happy
    pause 0.8
    show sarah excited
    pause 0.8
    show sarah smirk
    pause 0.8
    show sarah stressed
    pause 0.8
    show sarah sad
    pause 0.8
    show sarah neutral
    pause 0.8
    "That's all."
    hide sarah
    jump vn_showcase
    
label vanderwood_showcase:
    hide saeran vn
    show vanderwood 
    "If you'd like the minor characters to speak, you'll need to define your own character for them."
    "It's pretty easy; just go to {b}character definitions.rpy{/b} and follow the guidelines there."
    "Vanderwood has the following expressions:"
    show vanderwood unamused
    pause 0.8
    show vanderwood unsure
    pause 0.8
    show vanderwood determined
    pause 0.8
    show vanderwood ouch
    pause 0.8
    show vanderwood angry
    pause 0.8
    show vanderwood neutral
    pause 0.8
    "And that's all."
    hide vanderwood
    jump vn_showcase
    