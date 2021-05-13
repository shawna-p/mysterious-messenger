
label example_text_vn_r():

    # You use the "scene" command to set up the background of the VN section
    # It clears away any character sprites you have left showing and sets
    # the background to your desired image
    scene bg mint_eye_room

    # This will play music during the VN.
    play music mint_eye

    show saeran smile
    r "Hello! Welcome to Story Mode, also known as Visual Novel mode."
    show saeran -smile   # the -smile puts him in his 'neutral' expression
    r "This mode is most similar to what you'll find in the majority of Ren'Py projects."
    # If Ray is already showing on the screen, his Character definition
    # has the image tag 'saeran' built into it so you can simplify
    # showing his image like so
    r happy "There are a couple of things to show you about Story Mode. What would you like to learn about first?"
    jump vn_tutorial


## This is put here for ease of finding it instead of burying it below all
## the example menus at the end of this Story Mode. As of v3.0, every individual
## story item can have its own after_ label. This one triggers at the end of
## this Story Mode (which is at the label example_text_vn_r, as seen above).
label after_example_text_vn_r():
    # ************************************************
    # Zen's text message
    # This is another example of real-time texting, but instead of being
    # delivered immediately after the Story Mode, it will be randomly delivered
    # sometime before the next story item if the player is playing in real-time.
    # If not, it gets delivered after this Story Mode as usual.
    # There are other arguments you can pass this as well; check the
    # documentation for more information!
    compose text z real_time deliver_at random:
        z "You know, you never send us any photos..."
        label menu_a3

    return

##************************************
## Tutorial Menu
##************************************
label vn_tutorial():
    # This tells it not to shuffle these menu choices for the
    # tutorial. You will usually not need to do this.
    $ shuffle = False
    menu:
        # This makes the previous line before the menu stay
        # on-screen while the player is making their choice.
        extend ''

        "Can I get an overview on the Story Mode (VN) features?":
            show saeran distant
            r "Oh, of course! Some features are new, after all."
            jump vn_writing

        "How do I get different expressions and outfits?":
            show saeran smile
            r "Good question!"
            jump vn_layeredimage

        "How can I position characters on the screen?":
            show saeran smile
            r "Moving characters around is quite easy!"
            jump vn_position

        "I want to look at all the available characters.":
            show saeran smile
            r "Sure! Who do you want to see?"
            jump vn_showcase

        "That's enough explanation, thanks.":
            show saeran smile
            r "Alright! Hope this helped you."
            return # Use this to end the VN Mode section



##************************************
## Writing a Story Mode section
##************************************
label vn_writing():
    show saeran neutral
    r """
    Writing a Story Mode section is pretty straightforward.

    First, you need to define a label, and then you can start adding dialogue and characters!

    This part works in the 'traditional' Ren'Py manner, so if you're not sure how to start adding characters and dialogue,

    I'd recommend checking out the LemmaSoft forums and looking through the Story Mode section in the documentation.

    If you don't plan to change the speaking character's expression for a while,

    you can also look into Ren'Py's \"monologue\" feature, which you can see an example of in the code for this Story Mode section.
    """
    show saeran smile
    r "Other than that, there are three buttons on the screen in Story Mode -- {b}Auto{/b}, {b}Skip{/b}, and {b}Log{/b}."
    show tut_arrow_vert:
        rotate -90
        xpos 340
        ypos 830
    r "{b}Auto{/b}, when selected, will automatically advance the text for you."
    r "You can adjust the auto-forward speed in Settings."
    r neutral "Keep in mind that this will also affect how fast phone call text will auto-advance if there is no voiceover."
    show tut_arrow_vert:
        rotate -90
        xpos 475
        ypos 830
    r "{b}Skip{/b} will start fast-forwarding you through the text,"
    show tut_arrow_vert:
        rotate -90
        xpos 578
        ypos 830
    r distant "and {b}Log{/b} will show you a log of the dialogue history."
    hide tut_arrow_vert
    r neutral "There are also some options in the {b}Preferences{/b} tab on the {b}Settings{/b} screen that affect Story Mode."
    show tut_prefs at tutorial_anim(100)
    pause 0.5
    show tut_arrow:
        rotate 180
        xpos 40
        ypos 470
    r "{b}Text Speed{/b} adjusts how fast the dialogue shows up. If it's all the way to the right, like in this screenshot, dialogue appears instantly."
    if preferences.text_cps == 0:
        r "{cps=50}Moving the slider to the left causes dialogue to show up like this.{/cps}"
    show tut_arrow:
        rotate 180
        xpos 40
        ypos 520
    r "{b}Auto-Forward Time{/b}, as mentioned, adjusts how long the game will wait before moving on to the next dialogue when {b}Auto{/b} is turned on."
    show tut_arrow:
        rotate 180
        xpos 40
        ypos 565
    r "{b}Timed Menu Speed{/b} is something you'll see later; it's a separate chat speed modifier for timed menus."
    show tut_arrow:
        rotate 180
        xpos 40
        ypos 615
    r "{b}VN Window Opacity{/b} will adjust how opaque the dialogue window is."
    hide tut_arrow
    hide tut_prefs
    $ old_opacity = persistent.window_darken_pct
    $ persistent.window_darken_pct = 100
    $ adjust_vn_alpha()
    r "Maximum opacity looks like this."
    $ persistent.window_darken_pct = 0
    $ adjust_vn_alpha()
    r smile "And minimum opacity looks like this. It automatically adds outlines to the text so it's still readable."
    $ persistent.window_darken_pct = old_opacity
    $ adjust_vn_alpha()
    show tut_prefs at tutorial_anim(100)
    pause 0.5
    show tut_arrow:
        rotate 180
        xpos 30
        ypos 785
    r neutral "Finally, there are also the Dialogue settings. If {b}Skip Unseen Text{/b} is on, the game will skip all dialogue."
    r "If it's off, however, the game will only skip dialogue you haven't seen yet on any playthrough."
    show tut_arrow:
        rotate 0
        xpos 500
        ypos 785
    r "{b}Skip After Choices{/b} means that the game will continue skipping after a choice."
    r "If it's off, the game will automatically stop skipping once you reach a choice."
    r smile "This can be good if you don't want to skip through too much of the game."
    show tut_arrow:
        rotate 180
        xpos 25
        ypos 812
    r neutral "{b}Skip Transitions{/b} will turn off transitions like backgrounds and characters fading in and out,"
    show tut_arrow:
        rotate 0
        xpos 520
        ypos 814
    r "And {b}Indicate Past Choices{/b} will include a little check mark on the choice screen next to choices you've already picked on any playthrough."
    hide tut_arrow
    hide tut_prefs
    r smile "And that's all for this overview!"
    r thinking "Is there anything else you'd like to learn more about?"
    jump vn_tutorial

##************************************
## Changing Expressions & Outfits
##************************************
label vn_layeredimage():

    show saeran happy
    r "To get different expressions and outfits, this program makes a lot of use of Ren'Py's {b}Layered Image{/b} feature."
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

# This is a variable used later in a profile picture callback. You can see
# it used in tutorial_0_introduction.rpy
default sent_zen_unknown_pic = False
label menu_a3():
    # This menu is paraphrased, but the rest of the route is not, so the
    # argument (paraphrased=True) is passed to the menu.
    menu (paraphrased=True):
        # The player can post both CGs and emojis
        "(Post a photo)":
            $ sent_zen_unknown_pic = True
            m "common_2" (pauseVal=0, img=True)
            m "You mean like this?"
        "(Post an emoji)":
            m "{image=zen_oyeah}" (pauseVal=0, img=True)
            m "How's this?"
        "(Post both)":
            $ sent_zen_unknown_pic = True
            m "common_2" (pauseVal=0, img=True)
            m "{image=zen_oyeah}" (img=True)
            m "What do you think?"

    z "Wow! I've never seen that before."
    z "You're pretty cool"
    z "{image=zen_wink}" (img=True)
    return


##************************************
## Changing Outfits/Expressions:
## Examples
##************************************
label vn_showcase():
    $ shuffle = False
    menu (paraphrased=True):
        "Who would you like to see?{fast}"

        "Major Characters":
            $ shuffle = False
            jump vn_showcase_major1

        "Minor Characters":
            $ shuffle = False
            jump vn_showcase_minor1

        "I'm done viewing characters" (paraphrased=False):
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

    "More ->" (paraphrased=True):
        $ shuffle = False
        jump vn_showcase_major2

menu vn_showcase_major2:

    "Who would you like to see?{fast}"

    "<- Back" (paraphrased=True):
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

    "More ->" (paraphrased=True):
        $ shuffle = False
        jump vn_showcase_minor2

menu vn_showcase_minor2:

    "Who would you like to see?{fast}"

    "<- Back" (paraphrased=True):
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

    "More ->" (paraphrased=True):
        $ shuffle = False
        jump vn_showcase_minor3

menu vn_showcase_minor3:

    "Who would you like to see?{fast}"

    "<- Back" (paraphrased=True):
        $ shuffle = False
        jump vn_showcase_minor2

    "Mika":
        $ shuffle = False
        jump mika_showcase

    "The pastor":
        $ shuffle = False
        jump pastor_showcase

    "Rika's mom":
        $ shuffle = False
        jump rikamom_showcase


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
    with Pause(0.8)
    show jaehee sad
    with Pause(0.8)
    show jaehee neutral
    with Pause(0.8)
    show jaehee thinking
    with Pause(0.8)
    show jaehee worried
    with Pause(0.8)
    show jaehee angry
    with Pause(0.8)
    show jaehee sparkle
    with Pause(0.8)
    show jaehee serious
    with Pause(0.8)
    show jaehee surprised
    ja "And now I'll show you the expressions I have without my glasses."
    show jaehee happy -glasses
    with Pause(0.8)
    show jaehee sad
    with Pause(0.8)
    show jaehee neutral
    with Pause(0.8)
    show jaehee thinking
    with Pause(0.8)
    show jaehee worried
    with Pause(0.8)
    show jaehee neutral
    ja "These are my available outfits."
    show jaehee normal
    with Pause(0.8)
    show jaehee arm
    with Pause(0.8)
    show jaehee party
    with Pause(0.8)
    show jaehee dress
    with Pause(0.8)
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
    with Pause(0.8)
    show jumin upset
    with Pause(0.8)
    show jumin blush
    with Pause(0.8)
    show jumin neutral
    with Pause(0.8)
    show jumin surprised
    with Pause(0.8)
    show jumin angry
    with Pause(0.8)
    show jumin sad
    with Pause(0.8)
    show jumin unsure
    with Pause(0.8)
    show jumin thinking
    with Pause(0.8)
    show jumin neutral
    ju "And here are my available outfits."
    show jumin
    with Pause(0.8)
    show jumin arm
    with Pause(0.8)
    show jumin party
    with Pause(0.8)
    ju "I also have a second position."
    show jumin side
    ju "These are the available expressions."
    show jumin happy
    with Pause(0.8)
    show jumin upset
    with Pause(0.8)
    show jumin blush
    with Pause(0.8)
    show jumin neutral
    with Pause(0.8)
    show jumin surprised
    with Pause(0.8)
    show jumin angry
    with Pause(0.8)
    show jumin thinking
    with Pause(0.8)
    show jumin worried
    with Pause(0.8)
    show jumin neutral
    ju "And here are the available outfits."
    show jumin normal
    with Pause(0.8)
    show jumin suit
    with Pause(0.8)
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
    with Pause(0.8)
    show rika sad
    with Pause(0.8)
    show rika neutral
    with Pause(0.8)
    show rika thinking
    with Pause(0.8)
    show rika worried
    with Pause(0.8)
    show rika dark
    with Pause(0.8)
    show rika angry
    with Pause(0.8)
    show rika sob
    with Pause(0.8)
    show rika crazy
    with Pause(0.8)
    show rika neutral
    with Pause(0.8)
    ri "And these are my available outfits."
    show rika normal
    with Pause(0.8)
    show rika savior
    with Pause(0.8)
    show rika blue_dress
    with Pause(0.8)
    show rika dress
    with Pause(0.8)
    ri "I also have a mask accessory available to me."
    show rika dress mask
    with Pause(0.8)
    show rika dress -mask
    with Pause(0.8)
    ri "And then I have a younger version as well."
    show rika middle_school
    with Pause(0.8)
    show rika happy
    with Pause(0.8)
    show rika upset
    with Pause(0.8)
    show rika sad
    with Pause(0.8)
    ri happy "That's all from me!"
    hide rika
    jump vn_showcase

label seven_showcase():
    hide saeran
    show seven front
    s "Hey hey hey~! I get to show off my expressions, hmm~?"
    s "Here they are!"
    show seven happy
    with Pause(0.8)
    show seven blush
    with Pause(0.8)
    show seven neutral
    with Pause(0.8)
    show seven surprised
    with Pause(0.8)
    show seven serious
    with Pause(0.8)
    show seven thinking
    with Pause(0.8)
    show seven sad
    with Pause(0.8)
    show seven worried
    with Pause(0.8)
    show seven dark
    with Pause(0.8)
    show seven angry
    with Pause(0.8)
    show seven hurt
    with Pause(0.8)
    show seven neutral
    with Pause(0.8)
    s "And here are my outfits~"
    show seven normal
    with Pause(0.8)
    show seven arm
    with Pause(0.8)
    show seven party
    with Pause(0.8)
    s "I have another pose, too!"
    show seven side
    with Pause(0.8)
    s "Here are the expressions for this pose."
    show seven happy
    with Pause(0.8)
    show seven concern
    with Pause(0.8)
    show seven surprised
    with Pause(0.8)
    show seven thinking
    with Pause(0.8)
    show seven sad
    with Pause(0.8)
    show seven neutral
    with Pause(0.8)
    show seven dark
    with Pause(0.8)
    show seven angry
    with Pause(0.8)
    show seven worried
    with Pause(0.8)
    show seven neutral
    with Pause(0.8)
    s "And here are the outfits."
    show seven normal
    with Pause(0.8)
    show seven arm
    with Pause(0.8)
    show seven suit
    with Pause(0.8)
    s "And finally, I also have a younger version."
    show seven young
    with Pause(0.8)
    show seven surprised
    with Pause(0.8)
    show seven serious
    with Pause(0.8)
    show seven worried
    with Pause(0.8)
    show seven side happy
    s "That's it! Enjoy the rest of the program~"
    hide seven
    jump vn_showcase

label saeran_showcase():
    show saeran neutral
    r "Oh, me?"
    r "Okay. I have several different expressions."
    show saeran happy
    with Pause(0.8)
    show saeran smile
    with Pause(0.8)
    show saeran neutral
    with Pause(0.8)
    show saeran angry
    with Pause(0.8)
    show saeran thinking
    with Pause(0.8)
    show saeran tense
    with Pause(0.8)
    show saeran creepy
    with Pause(0.8)
    show saeran cry
    with Pause(0.8)
    show saeran blush
    with Pause(0.8)
    show saeran sob
    with Pause(0.8)
    show saeran teary
    with Pause(0.8)
    show saeran nervous
    with Pause(0.8)
    show saeran sad
    with Pause(0.8)
    show saeran worried
    with Pause(0.8)
    show saeran distant
    with Pause(0.8)
    show saeran neutral
    with Pause(0.8)
    r "And then I have many outfits, too."
    show saeran ray
    with Pause(0.8)
    show saeran saeran
    with Pause(0.8)
    show saeran suit
    with Pause(0.8)
    show saeran unknown
    with Pause(0.8)
    show saeran mask
    with Pause(0.8)
    r "This outfit has fewer expressions than the other outfits since my face is partially covered"
    show saeran happy mask
    with Pause(0.8)
    show saeran smile mask
    with Pause(0.8)
    show saeran neutral mask
    with Pause(0.8)
    show saeran angry mask
    with Pause(0.8)
    show saeran thinking mask
    with Pause(0.8)
    show saeran tense mask
    with Pause(0.8)
    show saeran creepy mask
    with Pause(0.8)
    show saeran ray smile
    r "And now I have new positions as well!"
    show saeran front normal
    with Pause(0.8)
    show saeran blush
    with Pause(0.8)
    show saeran cry
    with Pause(0.8)
    show saeran sad
    with Pause(0.8)
    show saeran nervous
    with Pause(0.8)
    show saeran worried
    with Pause(0.8)
    show saeran tired
    with Pause(0.8)
    show saeran frown front arm
    with Pause(0.8)
    show saeran thinking
    with Pause(0.8)
    show saeran surprised
    with Pause(0.8)
    show saeran angry
    with Pause(0.8)
    show saeran happy
    with Pause(0.8)
    show saeran happy_cry
    with Pause(0.8)
    r "Hope that's what you were looking for!"
    jump vn_showcase

label v_showcase():
    hide saeran
    show v front
    v "Hello there."
    v "I'm told I'm supposed to show you my expressions."
    show v neutral
    with Pause(0.8)
    show v happy
    with Pause(0.8)
    show v angry
    with Pause(0.8)
    show v worried
    with Pause(0.8)
    show v thinking
    with Pause(0.8)
    show v talking
    with Pause(0.8)
    show v surprised
    with Pause(0.8)
    show v tense
    with Pause(0.8)
    show v sweating
    with Pause(0.8)
    show v sad
    with Pause(0.8)
    show v upset
    with Pause(0.8)
    show v concerned
    with Pause(0.8)
    show v regret
    with Pause(0.8)
    show v unsure
    with Pause(0.8)
    show v afraid
    with Pause(0.8)
    show v neutral
    with Pause(0.8)
    v "And then here are my outfits."
    show v normal
    with Pause(0.8)
    show v arm
    with Pause(0.8)
    show v hair_normal
    with Pause(0.8)
    show v hair_arm
    with Pause(0.8)
    show v mint_eye
    with Pause(0.8)
    v "I also have a hood accessory with this outfit."
    show v mint_eye hood_down
    with Pause(0.8)
    show v mint_eye hood_up
    with Pause(0.8)
    show v mint_eye hood_down
    with Pause(0.8)
    v "And then I have a side pose, too."
    show v side
    with Pause(0.8)
    v "Here are the poses for this pose."
    with Pause(0.8)
    show v happy
    with Pause(0.8)
    show v angry
    with Pause(0.8)
    show v neutral
    with Pause(0.8)
    show v surprised
    with Pause(0.8)
    show v thinking
    with Pause(0.8)
    show v worried
    with Pause(0.8)
    show v sweat
    with Pause(0.8)
    show v shock
    with Pause(0.8)
    show v afraid
    with Pause(0.8)
    show v blush
    with Pause(0.8)
    show v sad
    with Pause(0.8)
    show v unsure
    with Pause(0.8)
    show v neutral
    with Pause(0.8)
    v "All of these expressions also have a version with sunglasses."
    show v glasses happy
    with Pause(0.8)
    show v angry
    with Pause(0.8)
    show v neutral
    with Pause(0.8)
    show v surprised
    with Pause(0.8)
    show v thinking
    with Pause(0.8)
    show v worried
    with Pause(0.8)
    show v sweat
    with Pause(0.8)
    show v shock
    with Pause(0.8)
    show v afraid
    with Pause(0.8)
    show v blush
    with Pause(0.8)
    show v sad
    with Pause(0.8)
    show v unsure
    with Pause(0.8)
    show v neutral
    with Pause(0.8)
    v "And then I have different outfits for this position."
    show v normal
    with Pause(0.8)
    show v short_hair
    with Pause(0.8)
    show v long_hair
    with Pause(0.8)
    v "And that's all. Please enjoy the program."
    hide v
    jump vn_showcase

label yoosung_showcase():
    hide saeran
    show yoosung happy
    y "Hi! It's nice to see you~"
    y "I can show you the expressions I have in Story Mode."
    show yoosung happy
    with Pause(0.8)
    show yoosung neutral
    with Pause(0.8)
    show yoosung thinking
    with Pause(0.8)
    show yoosung surprised
    with Pause(0.8)
    show yoosung sparkle
    with Pause(0.8)
    show yoosung angry
    with Pause(0.8)
    show yoosung sad
    with Pause(0.8)
    show yoosung dark
    with Pause(0.8)
    show yoosung tired
    with Pause(0.8)
    show yoosung upset
    with Pause(0.8)
    show yoosung happy
    with Pause(0.8)
    y "I've also got a set of expressions when I'm wearing glasses."
    show yoosung glasses happy
    with Pause(0.8)
    show yoosung neutral
    with Pause(0.8)
    show yoosung thinking
    with Pause(0.8)
    show yoosung surprised
    with Pause(0.8)
    show yoosung sparkle
    with Pause(0.8)
    show yoosung happy -glasses
    with Pause(0.8)
    y "And here are my outfits!"
    show yoosung normal
    with Pause(0.8)
    show yoosung arm
    with Pause(0.8)
    show yoosung sweater
    with Pause(0.8)
    show yoosung suit
    with Pause(0.8)
    show yoosung party
    with Pause(0.8)
    show yoosung bandage
    with Pause(0.8)
    y "I've only got a few expressions when I have the bandage."
    show yoosung bandage happy
    with Pause(0.8)
    show yoosung neutral
    with Pause(0.8)
    show yoosung thinking
    with Pause(0.8)
    show yoosung normal happy -bandage
    with Pause(0.8)
    y "That's all! Have fun with the program~!"
    hide yoosung
    jump vn_showcase

label zen_showcase():
    hide saeran
    show zen front happy
    z "Hey babe~ Glad you came by!"
    z "Here are my available expressions!"
    show zen happy
    with Pause(0.8)
    show zen angry
    with Pause(0.8)
    show zen blush
    with Pause(0.8)
    show zen wink
    with Pause(0.8)
    show zen neutral
    with Pause(0.8)
    show zen surprised
    with Pause(0.8)
    show zen thinking
    with Pause(0.8)
    show zen worried
    with Pause(0.8)
    show zen oh
    with Pause(0.8)
    show zen upset
    with Pause(0.8)
    show zen neutral
    with Pause(0.8)
    z "I've got a few outfits for this front pose, too."
    show zen arm
    with Pause(0.8)
    show zen party
    with Pause(0.8)
    show zen normal
    with Pause(0.8)
    z "Handsome, aren't I?"
    z "Anyway, here are my side expressions."
    show zen side happy
    with Pause(0.8)
    show zen angry
    with Pause(0.8)
    show zen blush
    with Pause(0.8)
    show zen wink
    with Pause(0.8)
    show zen surprised
    with Pause(0.8)
    show zen thinking
    with Pause(0.8)
    show zen worried
    with Pause(0.8)
    show zen upset
    with Pause(0.8)
    show zen neutral
    with Pause(0.8)
    z "And then a few more outfits."
    show zen suit
    with Pause(0.8)
    show zen normal
    with Pause(0.8)
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
    with Pause(0.8)
    show chairman_han thinking
    with Pause(0.8)
    show chairman_han stressed
    with Pause(0.8)
    show chairman_han neutral
    with Pause(0.8)
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
    with Pause(0.8)
    show echo_girl angry
    with Pause(0.8)
    show echo_girl smile
    with Pause(0.8)
    show echo_girl surprised
    with Pause(0.8)
    show echo_girl neutral
    with Pause(0.8)
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
    with Pause(0.8)
    show glam_choi smirk
    with Pause(0.8)
    show glam_choi thinking
    with Pause(0.8)
    show glam_choi stressed
    with Pause(0.8)
    show glam_choi worried
    with Pause(0.8)
    show glam_choi neutral
    with Pause(0.8)
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
    with Pause(0.8)
    show sarah excited
    with Pause(0.8)
    show sarah smirk
    with Pause(0.8)
    show sarah stressed
    with Pause(0.8)
    show sarah sad
    with Pause(0.8)
    show sarah neutral
    with Pause(0.8)
    "That's all."
    hide sarah
    jump vn_showcase

label vanderwood_showcase():
    hide saeran
    show vanderwood
    va "While I'm not part of the main RFA cast, I do have a character defined."
    va unamused "So I you can add me to chatrooms, phone calls, story mode and more."
    va neutral "I even have my own heart icon now."
    award heart va
    va "Anyway, these are all my expressions."
    show vanderwood unamused
    with Pause(0.8)
    show vanderwood unsure
    with Pause(0.8)
    show vanderwood determined
    with Pause(0.8)
    show vanderwood ouch
    with Pause(0.8)
    show vanderwood angry
    with Pause(0.8)
    va "And thanks to {a=https://twitter.com/RomRom1705}Rom (@RomRom1705 on Twitter){/a}, I have four new expressions as well."
    show vanderwood smile
    with Pause(0.8)
    show vanderwood angry_blush
    with Pause(0.8)
    show vanderwood blush
    with Pause(0.8)
    show vanderwood thinking
    with Pause(0.8)
    show vanderwood neutral
    with Pause(0.8)
    va "That's it."
    hide vanderwood
    jump vn_showcase

label mika_showcase():
    hide saeran
    show mika
    "If you'd like the minor characters to speak, you need to define your own character for them."
    "It's pretty easy; just go to {b}character_definitions.rpy{/b} and follow the guidelines there."
    "Mika has the following expressions:"
    show mika blank
    with Pause(0.8)
    show mika happy
    with Pause(0.8)
    show mika smiling
    with Pause(0.8)
    show mika upset
    with Pause(0.8)
    show mika worried
    with Pause(0.8)
    "And that's all."
    hide mika
    jump vn_showcase

label pastor_showcase():
    hide saeran
    show pastor
    "If you'd like the minor characters to speak, you need to define your own character for them."
    "It's pretty easy; just go to {b}character_definitions.rpy{/b} and follow the guidelines there."
    "The pastor has the following expressions:"
    show pastor pleased
    with Pause(0.8)
    show pastor happy
    with Pause(0.8)
    show pastor shocked
    with Pause(0.8)
    "And that's all."
    hide pastor
    jump vn_showcase

label rikamom_showcase():
    hide saeran
    show rika_mom
    "If you'd like the minor characters to speak, you need to define your own character for them."
    "It's pretty easy; just go to {b}character_definitions.rpy{/b} and follow the guidelines there."
    "Rika's mom has the following expressions:"
    show rika_mom angry
    with Pause(0.8)
    show rika_mom tired
    with Pause(0.8)
    show rika_mom ugh
    with Pause(0.8)
    "And that's all."
    hide rika_mom
    jump vn_showcase



