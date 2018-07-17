#************************************
#************************************
#********Visual Novel Mode***********
#************************************
#************************************


## BACKGROUNDS **********************

image bg mint_eye_room = "VN Mode/Backgrounds/mint_eye_room.png"

        
default menutext = ''
        
label vn_mode_tutorial:

    call vn_setup
    
    scene bg mint_eye_room
    
    # You'll generally never want to mess with the 'observing' variable yourself, 
    # but since this is a tutorial chatroom we want the user to be able to play
    # it over and over and not be restricted to the choices they've already made
    $ observing = False
    
    show saeran vn smile
    r_vn "Hello! Welcome to Visual Novel mode."
    show saeran vn -smile
    r_vn "This mode is most similar to what you'll find in the majority of Ren'Py projects."
    show saeran vn happy
    r_vn "There are a couple of things to show you about VN mode. What would you like to learn about first?"
    $ menutext = "There are a couple of things to show you about VN mode. What would you like to learn about first?"
    jump vn_tutorial
    
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
            call press_save_and_exit(False)
            
    show saeran vn happy
    
label vn_writing:
    show saeran vn saeran neutral
    r_vn "Writing a VN section is pretty straightforward."
    r_vn "First, you'll define a label, and then you can start adding dialogue and characters!"
    r_vn "This part works in the 'traditional' Ren'Py manner, so if you're not sure how to start adding characters and dialogue,"
    extend " I'd recommend checking out the LemmaSoft forums and looking through the code in VN Mode.rpy"
    show saeran vn saeran smile
    r_vn "Other than that, there are two buttons on the screen in VN mode -- {b}Skip{/b} and {b}Log{/b}."
    r_vn "{b}Skip{/b} will start fast-forwarding you through the text,"
    extend " and {b}Log{/b} will show you a log of the dialogue history."
            
    
    
label vn_layeredimage:

    show saeran vn happy
    r_vn "To get different expressions and outfits, we make a lot of use of Ren'Py's {b}layeredimage{/b} feature."
    show saeran vn unknown neutral
    r_vn "It lets me change outfits and expressions very quickly just by adding the appropriate tags."
    show saeran vn mask happy
    r_vn "For example, the attributes used to display this sprite are {b}mask{/b} and {b}happy{/b}."
    show saeran vn unknown blush
    r_vn "Not all expressions are available with the mask on, however."
    show saeran vn suit nervous
    r_vn "Some characters have many outfits, and some have multiple poses as well."
    show saeran vn at vn_left with ease
    show v side at vn_midright with easeinright
    r_vn "Some characters also have 'accessories' like glasses."
    hide saeran vn with easeoutleft
    show v side at default with ease
    extend "We'll show you what I mean with V."
    
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
    v_vn "You'll get an error if you try to use the hood attribute when I'm not wearing my mint eye cloak, however."
    
    hide v with easeoutright
    show saeran vn with easeinleft
    
    r_vn "You'll want to take a look at the 'cheat sheet' in {b}character definitions.rpy{/b} that tells you all the expressions and accessories available to each character."
    r_vn "Anything else you'd like to know about?"
    $ menutext = "Anything else you'd like to know about?"
    jump vn_tutorial
    
label vn_position:
    r_vn "You might have noticed before, but you can position the characters in the middle,"
    extend " or to the left and right sides of the screen."
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
    extend " sometimes they'll be too far off-screen if you use {b}vn_left{/b}, so you'll need to use {b}vn_midleft{/b} instead."
    r_vn "You can always define your own transforms to position the characters exactly how you want, too."
    show saeran vn neutral
    r_vn "Anything else you'd like to learn about?"
    $ menutext = "Anything else you'd like to learn about?"
    jump vn_tutorial
    
    
 
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
    show seven front blush
    show seven front neutral
    show seven front surprised
    show seven front serious
    show seven front thinking
    show seven front sad
    show seven front worried
    show seven front dark
    show seven front angry
    show seven front hurt
    show seven front neutral
    s_vn "And here are my outfits~"
    show seven front normal
    show seven front arm
    show seven front party
    s_vn "I have another pose, too!"
    show seven side
    s_vn "Here are the expressions for this pose."
    show seven side happy
    show seven side concern
    show seven side surprised
    show seven side thinking
    show seven side sad
    show seven side neutral
    show seven side dark
    show seven side angry
    show seven side worried
    show seven side neutral
    s_vn "And here are the outfits."
    show seven side normal
    show seven side arm
    show seven side suit
    s_vn "That's it! Enjoy the rest of the program~"
    hide seven side
    jump vn_showcase
    
label saeran_showcase:
    r_vn "Oh, me?"
    r_vn "Okay. I have several different expressions."
    show saeran vn happy
    show saeran vn smile
    show saeran vn neutral
    show saeran vn angry
    show saeran vn thinking
    show saeran vn tense
    show saeran vn creepy
    show saeran vn cry
    show saeran vn blush
    show saeran vn sob
    show saeran vn teary
    show saeran vn nervous
    show saeran vn sad
    show saeran vn worried
    show saeran vn distant
    show saeran vn neutral
    r_vn "And then I have many outfits, too."
    show saeran vn ray
    show saeran vn saeran
    show saeran vn suit
    show saeran vn unknown
    show saeran vn mask
    r_vn "This outfit has fewer expressions than the other outfits since my face is partially covered"
    show saeran vn happy mask
    show saeran vn smile mask
    show saeran vn neutral mask
    show saeran vn angry mask
    show saeran vn thinking mask
    show saeran vn tense mask
    show saeran vn creepy mask
    show saeran vn ray smile
    r_vn "Hope that's what you were looking for!"
    jump vn_showcase
    
label v_showcase:
    hide saeran vn
    show v front
    v_vn "Hello there."
    v_vn "I'm told I'm supposed to show you my expressions."
    show v front neutral
    show v front happy
    show v front angry
    show v front worried
    show v front thinking
    show v front talking
    show v front surprised
    show v front tense
    show v front sweating
    show v front sad
    show v front upset
    show v front concerned
    show v front regret
    show v front unsure
    show v front afraid
    show v front neutral
    v_vn "And then here are my outfits."
    show v front normal
    show v front arm
    show v front hair_normal
    show v front hair_arm
    show v front mint_eye
    v_vn "I also have a hood accessory with this outfit."
    show v front mint_eye hood_down
    show v front mint_eye hood_up
    show v front mint_eye hood_down
    v_vn "And then I have a side pose, too."
    show v side
    v_vn "Here are the poses for this pose."
    show v side happy
    show v side angry
    show v side neutral
    show v side surprised
    show v side thinking
    show v side worried
    show v side sweat
    show v side shock
    show v side afraid
    show v side blush
    show v side sad
    show v side unsure
    show v side neutral
    v_vn "All of these expressions also have a version with sunglasses."
    show v side glasses happy
    show v side glasses angry
    show v side glasses neutral
    show v side glasses surprised
    show v side glasses thinking
    show v side glasses worried
    show v side glasses sweat
    show v side glasses shock
    show v side glasses afraid
    show v side glasses blush
    show v side glasses sad
    show v side glasses unsure
    show v side glasses neutral
    v_vn "And then I have different outfits for this position."
    show v side normal
    show v side short_hair
    show v side long_hair
    v_vn "And that's all. Please enjoy the program."
    hide v side
    jump vn_showcase
    
label yoosung_showcase:
    hide saeran vn
    show yoosung vn happy
    y_vn "Hi! It's nice to see you~"
    y_vn "I can show you the expressions I have in VN mode."
    show yoosung vn happy
    show yoosung vn neutral
    show yoosung vn thinking
    show yoosung vn surprised
    show yoosung vn sparkle
    show yoosung vn angry
    show yoosung vn sad
    show yoosung vn dark
    show yoosung vn tired
    show yoosung vn upset
    show yoosung vn happy
    y_vn "I've also got a set of expressions when I'm wearing glasses."
    show yoosung vn glasses happy
    show yoosung vn glasses neutral
    show yoosung vn glasses thinking
    show yoosung vn glasses surprised
    show yoosung vn glasses sparkle
    show yoosung vn happy -glasses
    y_vn "And here are my outfits!"
    show yoosung vn normal
    show yoosung vn arm
    show yoosung vn sweater
    show yoosung vn suit
    show yoosung vn party
    show yoosung vn bandage
    y_vn "I've only got a few expressions when I have the bandage."
    show yoosung vn bandage happy
    show yoosung vn bandage neutral
    show yoosung vn bandage thinking
    show yoosung vn normal happy
    y_vn "That's all! Have fun with the program~!"
    hide yoosung vn
    jump vn_showcase
    
label zen_showcase:
    hide saeran vn
    show zen front happy
    z_vn "Hey babe~ Glad you came by!"
    z_vn "Here are my available expressions!"
    show zen front happy
    show zen front angry
    show zen front blush
    show zen front wink
    show zen front neutral
    show zen front surprised
    show zen front thinking
    show zen front worried
    show zen front oh
    show zen front upset
    show zen front neutral
    
    
    
    

    
transform vn_left:
    xalign 0.0
    yalign 1.0
    xoffset -100
    
transform vn_right:
    xalign 1.0
    yalign 1.0
    xoffset 100
    
transform vn_midright:
    xalign 1.0
    yalign 1.0
    xoffset 50
    
transform vn_midleft:
    xalign 0.0
    yalign 1.0
    xoffset -50
    
label vn_setup:
    window auto
    $ chatroom_hp = 0
    hide screen starry_night
    hide screen phone_overlay
    hide screen messenger_screen 
    hide screen pause_button
    hide screen chatroom_timeline
    show screen vn_overlay
    $ vn_choice = True
    
    if current_chatroom.vn_obj.played:
        $ observing = True
    else:
        $ observing = False
        
    return
        
screen vn_overlay:

    $ my_menu_clock.runmode("real")
    hbox:
        add my_menu_clock xalign 0.0 yalign 0.0 xpos -50
        $ am_pm = time.strftime('%p', time.localtime())
        text am_pm style 'header_clock' 
        
    imagebutton:
        xalign 0.77
        yalign 0.74
        idle Text("Skip", style="vn_button")
        hover Text("Skip", style="vn_button_hover")
        selected config.skipping
        selected_idle Text("Stop", style="vn_button")
        selected_hover Text("Stop", style="vn_button_hover")
        action Function(toggle_skipping)
        
    imagebutton:
        xalign 0.95
        yalign 0.74
        idle Text("Log", style="vn_button")
        hover Text("Log", style="vn_button_hover")
        action ShowMenu('history')
        
        
screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    add "Phone UI/choice_dark.png"
    add "Phone UI/choice_dark.png"
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        focus_mask True
        idle "close_button"
        action Return
        
    text "Close" style "CG_close"
    
    
    viewport:
        yinitial 1.0
        scrollbars "vertical"
        mousewheel True
        draggable True
        side_yfill True

        ysize 1235
        yalign 1.0

        vbox:
            style_prefix "history"
            spacing 20

            for h in _history_list:

                fixed:
                    yfit True

                    if h.who:

                        label h.who + ':':
                            style "history_name"

                            ## Take the color of the who text from the Character, if
                            ## set.
                            if "color" in h.who_args:
                                text_color h.who_args["color"]

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what

            if not _history_list:
                label _("The dialogue history is empty.")
