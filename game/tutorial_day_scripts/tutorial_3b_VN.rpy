
label example_text_vn_r():

    # Make sure you call this at the start of a VN section
    call vn_begin 
    
    # You use the "scene" command to set up the background of the VN section
    # It clears away any character sprites you have left showing and sets
    # the background to your desired image
    scene bg mint_eye_room
    
    # This will play music during the VN.
    call play_music(mint_eye)
    
    show saeran smile
    r "Hello! Welcome to Story Mode, also known as Visual Novel mode."
    show saeran -smile   # the -smile puts him in his 'neutral' expression
    r "This mode is most similar to what you'll find in the majority of Ren'Py projects."
    # If Ray is already showing on the screen, his Character definition
    # has the image tag 'saeran' built into it so you can simplify
    # showing his image like so
    r happy "There are a couple of things to show you about VN mode. What would you like to learn about first?"
    jump vn_tutorial
  
##************************************
## Tutorial Menu
##************************************    
label vn_tutorial():
    # This tells it not to shuffle these menu choices for the 
    # tutorial. You will usually not need to do this
    $ shuffle = False   
    menu:
        # This makes the previous line before the menu stay
        # on-screen while the player is making their choice
        extend ''
        
        "How do I get different expressions and outfits?":
            m "How do I get different expressions and outfits?"
            show saeran smile
            r "Good question!"
            jump vn_layeredimage
        
        "How can I position characters on the screen?":
            m "How can I position characters on the screen?"
            show saeran smile
            r "Moving characters around is quite easy!"
            jump vn_position
            
        "How do I write a VN mode section?":
            m "How do I write a VN mode section?"
            show saeran distant
            r "Oh, of course! It's pretty easy, I promise."
            jump vn_writing
            
        "I want to look at all the available characters.":
            m "I want to look at all the available characters."
            show saeran smile
            r "Sure! Who do you want to see?"
            jump vn_showcase
            
        "That's enough explanation, thanks.":
            m "That's enough explanation, thanks."
            show saeran smile
            r "Alright! Hope this helped you."
            jump vn_end # Use this to end the VN Mode section
            
    
    
##************************************
## Writing a VN mode section
##************************************  
label vn_writing():
    show saeran neutral
    r """
    Writing a VN section is pretty straightforward.
    
    First, you need to define a label, and then you can start adding dialogue and characters!
    
    This part works in the 'traditional' Ren'Py manner, so if you're not sure how to start adding characters and dialogue,
    
    I'd recommend checking out the LemmaSoft forums and looking through the VN section in the wiki.
    
    If you don't plan to change the speaking character's expression for a while,
    
    you can also look into Ren'Py's \"monologue\" feature, which you can see an example of in the code for this VN section.
    """
    show saeran smile
    r """
    Other than that, there are three buttons on the screen in VN mode -- {b}Auto{/b}, {b}Skip{/b}, and {b}Log{/b}.
    
    {b}Auto{/b}, when selected, will automatically advance the text for you.
    
    You can adjust the auto-forward speed in Settings.
    
    Keep in mind that this will also affect how fast phone call text will auto-advance if there is no voiceover.
    
    {b}Skip{/b} will start fast-forwarding you through the text,
    
    and {b}Log{/b} will show you a log of the dialogue history.
    """
    r thinking "Is there anything else you'd like to learn more about?"
    jump vn_tutorial
    
##************************************
## Changing Expressions & Outfits
##************************************  
label vn_layeredimage():

    show saeran happy
    r "To get different expressions and outfits, this program makes a lot of use of Ren'Py's {b}layeredimage{/b} feature."
    r unknown neutral "It lets me change outfits and expressions very quickly just by adding the appropriate tags."
    r mask happy "For example, the attributes used to display this sprite are {b}mask{/b} and {b}happy{/b}."
    r unknown blush "Not all expressions are available with the mask on, however, like this one."
    r suit nervous "Some characters have many outfits, and some have multiple poses as well."
    show saeran at vn_left with ease
    show v side at vn_midright with easeinright
    r "Some characters also have 'accessories' like glasses."
    hide saeran with easeoutleft
    show v side at default with ease
    r "We'll show you what I mean with V."
    
    show v happy
    pause 0.5
    show v short_hair
    pause 0.5
    show v long_hair glasses
    pause 0.5
    show v thinking -glasses
    pause 0.5
    show v glasses short_hair
    pause 0.5
    show v front neutral    
    v "As you can see, there are several expressions both with and without my sunglasses."
    show v mint_eye
    v "I also have a 'hood' accessory for the {b}mint_eye{/b} outfit."
    show v hood_up
    v "The attribute {b}hood_up{/b}, when used with the {b}mint_eye{/b} attribute, will put the hood up."
    show v front arm talking
    v "You'll get an error if you try to use the hood attribute when I'm not wearing my Mint Eye cloak, however."
    
    hide v with easeoutright
    show saeran happy with easeinleft
    
    r "You should take a look at the 'cheat sheet' in {b}character_definitions.rpy{/b} that tells you all the expressions and accessories available to each character."
    r "Anything else you'd like to know about?"
    jump vn_tutorial
    
##************************************
## Positioning Characters
##************************************  
label vn_position():
    r "You might have noticed before, but you can position the characters in the middle,"
    r "or to the left and right sides of the screen."
    show saeran at vn_farleft with ease
    r "This is {b}vn_farleft{/b}."
    show saeran at vn_farright with ease
    r "And this is {b}vn_farright{/b}."
    show saeran at vn_left with ease
    r "This position is called {b}vn_left{/b}."
    show saeran at vn_right with ease
    r "This is {b}vn_right{/b}."
    show saeran at vn_midleft with ease
    r "This is {b}vn_midleft{/b}."
    show saeran at vn_midright with ease
    r "And this is {b}vn_midright{/b}."
    show saeran at default with ease
    r "The default position is just called {b}default{/b}, and characters will appear there if you don't specify a different location."
    show saeran at vn_center
    r "There's also this position, {b}vn_center{/b}."
    r "It puts the character a bit closer to the screen, to imply they're talking directly to you."
    # If you use vn_center and want to put the character back to a different
    # position, you need to 'hide' them first
    hide saeran
    show saeran thinking at default
    r "If you do use the {b}vn_center{/b} position, you need to {b}hide{/b} the character before you put them in a new position."
    r neutral "Know that not all positions will look right for each character;"
    r "sometimes they'll be too far off-screen if you use {b}vn_left{/b}, so you need to use {b}vn_midleft{/b} instead."
    r "You can always define your own transforms to position the characters exactly how you want, too."
    r neutral "Anything else you'd like to learn about?"
    jump vn_tutorial
    
    
##************************************
## Changing Outfits/Expressions:
## Examples
##************************************  
label vn_showcase():
    $ shuffle = False
    menu:
        "Who would you like to see?{fast}"
        
        "Major Characters":
            $ shuffle = False
            jump vn_showcase_major1
        
        "Minor Characters":
            $ shuffle = False
            jump vn_showcase_minor1
            
        "I'm done viewing characters":
            $ shuffle = False
            jump vn_tutorial
    
menu vn_showcase_major1:

    "Who would you like to see?{fast}"
    
    "Jaehee":
        $ shuffle = False
        jump jaehee_showcase
    
    "Jumin":
        $ shuffle = False
        jump jumin_showcase
    
    "Rika":
        $ shuffle = False
        jump rika_showcase
    
    "Seven":
        $ shuffle = False
        jump seven_showcase
    
    "More ->":
        $ shuffle = False
        jump vn_showcase_major2
    
menu vn_showcase_major2:
    
    "Who would you like to see?{fast}"
    
    "<- Back":
        $ shuffle = False
        jump vn_showcase_major1
    
    "Saeran":
        $ shuffle = False
        jump saeran_showcase
    
    "V":
        $ shuffle = False
        jump v_showcase
    
    "Yoosung":
        $ shuffle = False
        jump yoosung_showcase
    
    "Zen":
        $ shuffle = False
        jump zen_showcase
    
menu vn_showcase_minor1:

    "Who would you like to see?{fast}"
    
    "Bodyguards":
        $ shuffle = False
        jump bodyguards_showcase
    
    "Chairman Han":
        $ shuffle = False
        jump chairman_showcase
    
    "Echo Girl":
        $ shuffle = False
        jump echo_showcase
    
    "Glam Choi":
        $ shuffle = False
        jump glam_showcase
    
    "More ->":
        $ shuffle = False
        jump vn_showcase_minor2
    
menu vn_showcase_minor2:

    "Who would you like to see?{fast}"
    
    "<- Back":
        $ shuffle = False
        jump vn_showcase_minor1
    
    "Prime Minister":
        $ shuffle = False
        jump minister_showcase
    
    "Sarah Choi":
        $ shuffle = False
        jump sarah_showcase
    
    "Vanderwood":
        $ shuffle = False
        jump vanderwood_showcase
        
#************************
# Major Characters
#************************

label jaehee_showcase():
    hide saeran
    show jaehee glasses
    ja "Hello! I have several outfits and expressions to show you."
    show jaehee sparkle arm
    ja "First, I'll show you the expressions I have with my glasses."
    show jaehee happy -arm
    pause 0.8
    show jaehee sad
    pause 0.8
    show jaehee neutral
    pause 0.8
    show jaehee thinking
    pause 0.8
    show jaehee worried
    pause 0.8
    show jaehee angry
    pause 0.8
    show jaehee sparkle
    pause 0.8
    show jaehee serious
    pause 0.8
    show jaehee surprised
    ja "And now I'll show you the expressions I have without my glasses."
    show jaehee happy -glasses
    pause 0.8
    show jaehee sad
    pause 0.8
    show jaehee neutral
    pause 0.8
    show jaehee thinking
    pause 0.8
    show jaehee worried
    pause 0.8
    show jaehee neutral
    ja "These are my available outfits."
    show jaehee normal
    pause 0.8
    show jaehee arm
    pause 0.8
    show jaehee party
    pause 0.8
    show jaehee dress
    pause 0.8
    show jaehee apron
    ja "That is all from me."
    hide jaehee
    jump vn_showcase
    
label jumin_showcase():
    hide saeran
    show jumin front
    ju "Hello. You can view my outfits and poses here."
    ju "First, here are the expressions I have in my 'front' pose."
    show jumin happy
    pause 0.8
    show jumin upset
    pause 0.8
    show jumin blush
    pause 0.8
    show jumin neutral
    pause 0.8
    show jumin surprised
    pause 0.8
    show jumin angry
    pause 0.8
    show jumin sad
    pause 0.8
    show jumin unsure
    pause 0.8
    show jumin thinking
    pause 0.8
    show jumin neutral
    ju "And here are my available outfits."
    show jumin 
    pause 0.8
    show jumin arm
    pause 0.8
    show jumin party
    pause 0.8
    ju "I also have a second position."
    show jumin side
    ju "These are the available expressions."
    show jumin happy
    pause 0.8
    show jumin upset
    pause 0.8
    show jumin blush
    pause 0.8
    show jumin neutral
    pause 0.8
    show jumin surprised
    pause 0.8
    show jumin angry
    pause 0.8
    show jumin thinking
    pause 0.8
    show jumin worried
    pause 0.8
    show jumin neutral
    ju "And here are the available outfits."
    show jumin normal
    pause 0.8
    show jumin suit
    pause 0.8
    ju "That is all."
    hide jumin
    jump vn_showcase
    
label rika_showcase():
    hide saeran
    show rika happy
    ri "Hello~! You've come to see my expressions and outfits, right?"
    show rika -happy
    ri "I'll show you my expressions, first."
    show rika happy
    pause 0.8
    show rika sad
    pause 0.8
    show rika neutral
    pause 0.8
    show rika thinking
    pause 0.8
    show rika worried
    pause 0.8
    show rika dark
    pause 0.8
    show rika angry
    pause 0.8
    show rika sob
    pause 0.8
    show rika crazy
    pause 0.8
    show rika neutral
    pause 0.8
    ri "And these are my available outfits."
    show rika normal
    pause 0.8
    show rika savior
    pause 0.8
    show rika dress
    pause 0.8
    ri "I also have a mask accessory available to me."
    show rika dress mask
    pause 0.8
    show rika dress -mask
    ri "That's all from me!"
    hide rika
    jump vn_showcase
    
label seven_showcase():
    hide saeran
    show seven front
    s "Hey hey hey~! I get to show off my expressions, hmm~?"
    s "Here they are!"
    show seven happy
    pause 0.8
    show seven blush
    pause 0.8
    show seven neutral
    pause 0.8
    show seven surprised
    pause 0.8
    show seven serious
    pause 0.8
    show seven thinking
    pause 0.8
    show seven sad
    pause 0.8
    show seven worried
    pause 0.8
    show seven dark
    pause 0.8
    show seven angry
    pause 0.8
    show seven hurt
    pause 0.8
    show seven neutral
    pause 0.8
    s "And here are my outfits~"
    show seven normal
    pause 0.8
    show seven arm
    pause 0.8
    show seven party
    pause 0.8
    s "I have another pose, too!"
    show seven side
    pause 0.8
    s "Here are the expressions for this pose."
    show seven happy
    pause 0.8
    show seven concern
    pause 0.8
    show seven surprised
    pause 0.8
    show seven thinking
    pause 0.8
    show seven sad
    pause 0.8
    show seven neutral
    pause 0.8
    show seven dark
    pause 0.8
    show seven angry
    pause 0.8
    show seven worried
    pause 0.8
    show seven neutral
    pause 0.8
    s "And here are the outfits."
    show seven normal
    pause 0.8
    show seven arm
    pause 0.8
    show seven suit
    pause 0.8
    s "That's it! Enjoy the rest of the program~"
    hide seven
    jump vn_showcase
    
label saeran_showcase():
    show saeran neutral
    r "Oh, me?"
    r "Okay. I have several different expressions."
    show saeran happy
    pause 0.8
    show saeran smile
    pause 0.8
    show saeran neutral
    pause 0.8
    show saeran angry
    pause 0.8
    show saeran thinking
    pause 0.8
    show saeran tense
    pause 0.8
    show saeran creepy
    pause 0.8
    show saeran cry
    pause 0.8
    show saeran blush
    pause 0.8
    show saeran sob
    pause 0.8
    show saeran teary
    pause 0.8
    show saeran nervous
    pause 0.8
    show saeran sad
    pause 0.8
    show saeran worried
    pause 0.8
    show saeran distant
    pause 0.8
    show saeran neutral
    pause 0.8
    r "And then I have many outfits, too."
    show saeran ray
    pause 0.8
    show saeran saeran
    pause 0.8
    show saeran suit
    pause 0.8
    show saeran unknown
    pause 0.8
    show saeran mask
    pause 0.8
    r "This outfit has fewer expressions than the other outfits since my face is partially covered"
    show saeran happy mask
    pause 0.8
    show saeran smile mask
    pause 0.8
    show saeran neutral mask
    pause 0.8
    show saeran angry mask
    pause 0.8
    show saeran thinking mask
    pause 0.8
    show saeran tense mask
    pause 0.8
    show saeran creepy mask
    pause 0.8
    show saeran ray smile
    r "Hope that's what you were looking for!"
    jump vn_showcase
    
label v_showcase():
    hide saeran
    show v front
    v "Hello there."
    v "I'm told I'm supposed to show you my expressions."
    show v neutral
    pause 0.8
    show v happy
    pause 0.8
    show v angry
    pause 0.8
    show v worried
    pause 0.8
    show v thinking
    pause 0.8
    show v talking
    pause 0.8
    show v surprised
    pause 0.8
    show v tense
    pause 0.8
    show v sweating
    pause 0.8
    show v sad
    pause 0.8
    show v upset
    pause 0.8
    show v concerned
    pause 0.8
    show v regret
    pause 0.8
    show v unsure
    pause 0.8
    show v afraid
    pause 0.8
    show v neutral
    pause 0.8
    v "And then here are my outfits."
    show v normal
    pause 0.8
    show v arm
    pause 0.8
    show v hair_normal
    pause 0.8
    show v hair_arm
    pause 0.8
    show v mint_eye
    pause 0.8
    v "I also have a hood accessory with this outfit."
    show v mint_eye hood_down
    pause 0.8
    show v mint_eye hood_up
    pause 0.8
    show v mint_eye hood_down
    pause 0.8
    v "And then I have a side pose, too."
    show v side
    pause 0.8
    v "Here are the poses for this pose."
    pause 0.8
    show v happy
    pause 0.8
    show v angry
    pause 0.8
    show v neutral
    pause 0.8
    show v surprised
    pause 0.8
    show v thinking
    pause 0.8
    show v worried
    pause 0.8
    show v sweat
    pause 0.8
    show v shock
    pause 0.8
    show v afraid
    pause 0.8
    show v blush
    pause 0.8
    show v sad
    pause 0.8
    show v unsure
    pause 0.8
    show v neutral
    pause 0.8
    v "All of these expressions also have a version with sunglasses."
    show v glasses happy
    pause 0.8
    show v angry
    pause 0.8
    show v neutral
    pause 0.8
    show v surprised
    pause 0.8
    show v thinking
    pause 0.8
    show v worried
    pause 0.8
    show v sweat
    pause 0.8
    show v shock
    pause 0.8
    show v afraid
    pause 0.8
    show v blush
    pause 0.8
    show v sad
    pause 0.8
    show v unsure
    pause 0.8
    show v neutral
    pause 0.8
    v "And then I have different outfits for this position."
    show v normal
    pause 0.8
    show v short_hair
    pause 0.8
    show v long_hair
    pause 0.8
    v "And that's all. Please enjoy the program."
    hide v
    jump vn_showcase
    
label yoosung_showcase():
    hide saeran
    show yoosung happy
    y "Hi! It's nice to see you~"
    y "I can show you the expressions I have in VN mode."
    show yoosung happy
    pause 0.8
    show yoosung neutral
    pause 0.8
    show yoosung thinking
    pause 0.8
    show yoosung surprised
    pause 0.8
    show yoosung sparkle
    pause 0.8
    show yoosung angry
    pause 0.8
    show yoosung sad
    pause 0.8
    show yoosung dark
    pause 0.8
    show yoosung tired
    pause 0.8
    show yoosung upset
    pause 0.8
    show yoosung happy
    pause 0.8
    y "I've also got a set of expressions when I'm wearing glasses."
    show yoosung glasses happy
    pause 0.8
    show yoosung neutral
    pause 0.8
    show yoosung thinking
    pause 0.8
    show yoosung surprised
    pause 0.8
    show yoosung sparkle
    pause 0.8
    show yoosung happy -glasses
    pause 0.8
    y "And here are my outfits!"
    show yoosung normal
    pause 0.8
    show yoosung arm
    pause 0.8
    show yoosung sweater
    pause 0.8
    show yoosung suit
    pause 0.8
    show yoosung party
    pause 0.8
    show yoosung bandage
    pause 0.8
    y "I've only got a few expressions when I have the bandage."
    show yoosung bandage happy
    pause 0.8
    show yoosung neutral
    pause 0.8
    show yoosung thinking
    pause 0.8
    show yoosung normal happy -bandage
    pause 0.8
    y "That's all! Have fun with the program~!"
    hide yoosung
    jump vn_showcase
    
label zen_showcase():
    hide saeran
    show zen front happy
    z "Hey babe~ Glad you came by!"
    z "Here are my available expressions!"
    show zen happy
    pause 0.8
    show zen angry
    pause 0.8
    show zen blush
    pause 0.8
    show zen wink
    pause 0.8
    show zen neutral
    pause 0.8
    show zen surprised
    pause 0.8
    show zen thinking
    pause 0.8
    show zen worried
    pause 0.8
    show zen oh
    pause 0.8
    show zen upset
    pause 0.8
    show zen neutral
    pause 0.8
    z "I've got a few outfits for this front pose, too."
    show zen arm
    pause 0.8
    show zen party
    pause 0.8
    show zen normal
    pause 0.8
    z "Handsome, aren't I?"
    z "Anyway, here are my side expressions."
    show zen side happy
    pause 0.8
    show zen angry
    pause 0.8
    show zen blush
    pause 0.8
    show zen wink
    pause 0.8
    show zen surprised
    pause 0.8
    show zen thinking
    pause 0.8
    show zen worried
    pause 0.8
    show zen upset
    pause 0.8
    show zen neutral
    pause 0.8
    z "And then a few more outfits."
    show zen suit
    pause 0.8
    show zen normal
    pause 0.8
    z "And that's it! Enjoy the program, hon~"
    hide zen 
    jump vn_showcase
    
#************************
# Minor Characters
#************************
    
label bodyguards_showcase():
    hide saeran
    show bodyguard_front at vn_left
    show bodyguard_side at vn_right
    "If you'd like the minor characters to speak, you need to define your own character for them."
    "It's pretty easy; just go to {b}character_definitions.rpy{/b} and follow the guidelines there."
    "If you're only going to have them speak once or twice though, you can also type out their name as a string like so"
    "Bodyguard" "This is example dialogue for the bodyguard to say."
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
    
    
label chairman_showcase():
    hide saeran
    show chairman_han 
    chief_vn "I already have a character defined so I can speak."
    chief_vn "These are my expressions:"
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

label echo_showcase():
    hide saeran
    show echo_girl 
    "If you'd like the minor characters to speak, you need to define your own character for them."
    "It's pretty easy; just go to {b}character_definitions.rpy{/b} and follow the guidelines there."
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
    
    
label glam_showcase():  
    hide saeran
    show glam_choi 
    "If you'd like the minor characters to speak, you need to define your own character for them."
    "It's pretty easy; just go to {b}character_definitions.rpy{/b} and follow the guidelines there."
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
    
label minister_showcase():    
    hide saeran
    show prime_minister
    "If you'd like the minor characters to speak, you need to define your own character for them."
    "It's pretty easy; just go to {b}character_definitions.rpy{/b} and follow the guidelines there."
    "The Prime Minister only has one expression, the one currently showing."
    "That's all."
    hide prime_minister
    jump vn_showcase    
    
label sarah_showcase():    
    hide saeran
    show sarah 
    sarah_vn "I already have a character defined so I can talk, haha~"
    sarah_vn "These are my expressions!"
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
    
label vanderwood_showcase():
    hide saeran
    show vanderwood 
    "If you'd like the minor characters to speak, you need to define your own character for them."
    "It's pretty easy; just go to {b}character_definitions.rpy{/b} and follow the guidelines there."
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
    