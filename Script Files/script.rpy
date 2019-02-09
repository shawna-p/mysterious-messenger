label start:

    call define_variables 
    
    # This variable is set here simply so you can use the Save & Exit
    # function after your intro chatroom. You don't need to change these
    # values. You can, however, make a label called 'after_starter_chat'
    # to include text messages, or a phone call label called something
    # like 'starter_chat_incoming_ja'. You can't have VNs after this chatroom,
    # but it's possible to have VN sections mid-chatroom using 'call' or to write
    # a VN section before starting the chatroom
    $ current_chatroom = Chat_History('Starter Chat', 'auto', 'starter_chat', '00:00')
    # This sets a specific variable that lets you have phone calls/
    # VNs for this specific starter chat/opening
    $ starter_story = True
    
    # If you'd like to begin with a phone call, this is
    # how you'll do it. Just replace 'u' with whatever
    # character you want to call you
    call new_incoming_call(Phone_Call(u, 'n/a')) 
    
    # Begin and end the phone call like you would anywhere else
    call phone_begin 
    
    u_phone """
    
    Oh! You picked up; I'm so relieved.
    
    I thought maybe you wouldn't since my number wouldn't be listed in your phone.
    
    I'm calling because I was hoping you could help me test a new app I made. What do you think?
    
    """
    menu:
        extend ''
        "Testing? What would I need to do?":
            m_phone "Testing? What would I need to do?"
        "Sounds like a lot of work.":
            m_phone "Sounds like a lot of work."
            u_phone "Oh, it's not bad, I promise!"
            
    u_phone """
    
    I'll give you a couple of things to try doing with the program, and then you let me know if you run into problems or bugs.
    
    It'll help me make a much better program, in the end.
    
    You only need to do as much as you have time for. And in return you get to test out my program earlier than anyone else!
    
    So what do you say?
    
    """
    
    menu:
        extend ''
        "I suppose I'll give it a shot.":
            m_phone "I suppose I'll give it a shot."
            
    u_phone """
    
    You will? Wonderful!
    
    Alright, so when this call ends I'll send you a chatroom message with a bit more information.
    
    Good luck!
    
    """
    
    # Note that this is 'call' instead of 'jump'; this
    # allows us to continue on with a chatroom instead of
    # ending the introduction here
    call phone_end 
    scene bg black
    
    # Instead of ending the label here, we'll continue with
    # a chatroom. If you don't want the phonecall beforehand,
    # just delete that section
    # Feel free to modify the chatroom beyond this point
    call hack 
    call chat_begin('hack') 
        
    play music mystic_chat loop
    
    call enter(u) 
    u "You're here!" 
    u "Thank you for helping me ^^" 
    u "As you can see, this is a sort of \"introductory\" chatroom. It works a lot like the other chatrooms," 
    u "but with a couple of changes you can see in {b}script.rpy{/b}" 
    u "I recommend you get familiar with how regular chatrooms and phonecalls work before you look at this chat, though!" 
    
    call answer 
    menu:
        "What should I look at first?":
            m "What should I look at first?"   (pauseVal=0)
            u "Well, the first thing I recommend is to just play through the Tutorial Day." 
            u "It showcases some of the features so you know what sorts of things you can do with the program." 
    
        "I've actually already seen this; can you take me to the home screen?" if persistent.HP:
            m "I've actually already seen this; can you take me to the home screen?"   (pauseVal=0)
            u "Of course! See you later~" 
            call exit(u) 
            jump chat_end
    
    u "I won't keep you much longer. Enjoy the program!" 
    call exit(u) 
    
    jump chat_end


label define_variables:

    # Several variables are defined here to ensure they're
    # set properly when you begin a game
    
    python:                        
        myClock.runmode('real')
    
    if persistent.first_boot:
        call screen profile_pic
    
    python:
    
        name = persistent.name

        set_pronouns()
        
        chatlog = []

        # This variable keeps track of whether or not the player
        # is making a choice/on a choice menu
        choosing = False
        
        merge_albums(persistent.ja_album, ja_album)
        merge_albums(persistent.ju_album, ju_album)
        merge_albums(persistent.r_album, r_album)
        merge_albums(persistent.s_album, s_album)
        merge_albums(persistent.u_album, u_album)
        merge_albums(persistent.v_album, v_album)
        merge_albums(persistent.y_album, y_album)
        merge_albums(persistent.z_album, z_album)
        merge_albums(persistent.common_album, common_album)
        
        # The code below updates MC's profile picture and name
        thepic = 'Profile Pics/MC/MC-[persistent.MC_pic].png'
        if m.prof_pic != thepic:
            m.prof_pic = thepic
        if m.name != persistent.name:
            m.name = persistent.name
            
        renpy.retain_after_load()

    return
        

            
# Some experiments with timed menus; Left in in case there is interest
# If you decide to use it, know that it is not currently supported so
# you will need to do debugging yourself
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
    jump chat_end
    
label chat1:
    r "Did you not pick a reply?" (bounce=True, specBubble="sigh_m")
    r "{image=ray cry}" (img=True)
    jump chat_end


    
