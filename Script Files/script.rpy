

label define_variables:

    # Several variables are defined here to ensure they're
    # set properly when you begin a game
    
    python:                        
        myClock.runmode('real')
    
    if persistent.first_boot:
        call screen profile_pic
    
    python:
    
        persistent.first_boot = False
        name = persistent.name

        if persistent.pronoun == "female":
            they = "she"
            them = "her"
            their = "her"
            theirs = "hers"
            themself = "herself"
        elif persistent.pronoun == "male":
            they = "he"
            them = "him"
            their = "his"
            theirs = "his"
            themself = "himself"
        elif persistent.pronoun == "nonbinary":
            they = "they"
            them = "them"
            their = "their"
            theirs = "theirs"
            themself = "themself"
        
        chatlog = []

        # This variable keeps track of whether or not the player
        # is making a choice/on a choice menu
        choosing = False
        
        # The code below updates MC's profile picture and name
        thepic = 'Profile Pics/MC/MC-[persistent.MC_pic].png'
        if m.prof_pic != thepic:
            m.prof_pic = thepic
        if m.name != persistent.name:
            m.name = persistent.name
            
        renpy.retain_after_load()

    return
        
label start:

    call define_variables
    
    # Presumably an intro chat here if you so desired; as it is,
    # the program just jumps right to the chat hub screen with
    # no preamble
    # TODO: If you do this, you'll need to modify the save/load button
    # so it doesn't load the next chatroom when clicked 

    call screen chat_home
            
            
# Some experiments with timed menus; Left in in case there is interest
# See explanation below
label timed_menus:

    call chat_begin("earlyMorn")

    r "{=curly}I'm going to test posting some images!{/=curly}"
    r "general_cg1" (img=True)
    r "seven_cg1" (img=True)
    r "saeran_cg1" (img=True)
    r "{image=ray happy}" (img=True)
    
    # Anything after this call may or may not be seen by the player depending on
    # how fast they reply. The second value passed to continue_answer (in this case, 8)
    # is how long the player has to decide on an answer
    call continue_answer("menu1", 8)
    
    s "This doesn't happen in-game, but"
    s "I was hoping to have some timed menus where the chat will keep going."
    r "Here are some lines of dialogue you may or may not see"
    s "Who knows where this will go~"
    
    # You'll need to preface the menu with 'if timed_choose:' or else the menu
    # will simply show up after the dialogue before it is exhausted
    # If the player chooses an option, it will finish displaying the most recent
    # line of dialogue from above, then move on to the dialogue after the choice
    # If nothing is chosen, it will finish displaying the above dialogue, skip
    # over the menu, and keep going
    if timed_choose:
        menu menu1:
            "Do you think it'll be more interesting with interrupts?":
                hide answer_countdown
                m "Do you think it'll be more interesting with interrupts?" (pauseVal=0)
                s "Yeah!!" (bounce=True, specBubble="round2_s")
                s "I mean it's hard to say for sure-for sure, but"
                s "Seems like a cool feature to me."
            "But it's not a feature in the base game":
                hide answer_countdown
                m "But it's not a feature in the base game" (pauseVal=0)
                s "I know!" (bounce=True)
                s "It's fun experimenting though, right?"
            
    r "What parts of the chat did you see?"
    s "Did it work?"
    r "I hope so!" (bounce=True)
    r "{image=ray happy}" (img=True)
    call save_exit
    return
    
label chat1:
    r "Did you not pick a reply?" (bounce=True, specBubble="sigh_m")
    r "{image=ray cry}" (img=True)
    call save_exit
    return


    
