label start():
    
    # This call sets up which route the game is going to use -- in this
    # case, tutorial_good_end, defined in route_setup.rpy. You will pass
    # it the name of whatever you'd like your own route to be.
    # You cannot have a VN mode after this chatroom unless you include it
    # in this label as a call, but you can have text messages or phone 
    # calls after it by using labels such as `starter_chat_incoming_ja` or 
    # `after_starter_chat`. You can also include a VN section before this
    # chatroom.
    $ new_route_setup(route=tutorial_route)

    # This tells the program which characters' profiles you want to see
    # on the hub screen / available for phone calls / etc
    $ character_list = [ju, z, s, y, ja, v, m, r, ri]
    # This tells the program which characters to show on the Profile screen
    # next to how many heart points the player has earned
    $ heart_point_chars = [ju, z, s, y, ja, v, r, ri]

    # If you don't want an introduction, you can uncomment this line
    # When the player starts the game, they will be immediately taken
    # to the hub screen
    # jump skip_intro_setup

    # If you want to begin with a phone call, this is
    # how you do it. Just replace 'u' with whatever
    # character you want to call the player
    call new_incoming_call(PhoneCall(u, 'n/a')) 
    # Begin and end the phone call like you would anywhere else
    call phone_begin 
    
    u """
    
    Oh! You picked up; I'm so relieved.
    
    I thought maybe you wouldn't since my number wouldn't be listed in your phone.
    
    I'm calling because I was hoping you could help me test a new app I made. What do you think?
    
    """
    menu:
        extend ''
        "Testing? What would I need to do?":
            m "Testing? What would I need to do?"
        "Sounds like a lot of work.":
            m "Sounds like a lot of work."
            u "Oh, it's not bad, I promise!"
        "I've actually already seen this; can you take me to the home screen?" if persistent.HP:
            m "I've actually already seen this; can you take me to the home screen?"
            u "Oh, sure! See you later~"
            # This is pretty specific to this particular chat; you
            # should not have to do this. It simply makes it easier
            # for players who have already played through the game
            # to get to the chat hub
            $ persistent.first_boot = False
            $ persistent.on_route = True
            $ vn_choice = True
            jump press_save_and_exit
            
    u """
    
    All you have to do is use the app, and then you let me know if you run into problems or bugs.
    
    It'll help me make a much better program, in the end.
    
    You only need to use it as much as you have time for. And in return you get to test out my program earlier than anyone else!
    
    So what do you say?
    
    """
    
    menu:
        extend ''
        "I suppose I'll give it a shot.":
            m "I suppose I'll give it a shot."
            
    u """
    
    You will? Wonderful!

    I also wanted to ask -- how do you feel about short flashing animations?

    Sometimes the program has animations like the scrolling hacked code effect, or banners in the chatrooms. There is also a screen shake animation.

    """

    menu:
        extend ''
        "I don't want to see any flashing animations or screenshake.":
            $ persistent.screenshake = False
            $ persistent.banners = False
            $ persistent.hacking_effects = False
            m "I don't want to see any flashing animations or screenshake."
            u "Understandable! I've turned all those animations off for you."

        "I'm okay with some effects but not with others.":
            $ persistent.hacking_effects = False
            m "I'm okay with some effects but not with others."
            u "Okay! I've just turned the hacking effect off for now since it shows up in the next chatroom."

        "You can keep all the animations on.":
            $ persistent.screenshake = True
            $ persistent.banners = True
            $ persistent.hacking_effects = True
            m "You can keep all the animations on."
            u "Got it!"

    u """

    If you ever want to change which animations you see, you can find toggles for each of them in the {b}Settings{/b}.

    There are other accessibility options there as well, such as audio captions for background music and sound effects.

    Alright, so when this call ends I'll send you a chatroom message with a bit more information on getting started from here.
    
    Good luck!
    
    """
    
    # Note that this is 'call' instead of 'jump'; this
    # allows you to continue on with a chatroom instead of
    # ending the introduction here
    call phone_end 
    # This ensure the transition from phone to chatroom is smoother
    scene bg black
    
    # Instead of ending the label here, you can continue with
    # a chatroom. If you don't want the phonecall beforehand,
    # just delete that section
    # Feel free to modify the chatroom beyond this point
    call hack 
    call chat_begin('hack') 
        
    call play_music(mystic_chat)
    
    call enter(u) 
    u "You're here!" 
    u "Thank you for helping me ^^" 
    u "As you can see, this is a sort of \"introductory\" chatroom. It works a lot like the other chatrooms," 
    u "but with a couple of changes you can see in {b}tutorial_0_introduction.rpy{/b}" 
    u "I recommend you get familiar with how regular chatrooms and phonecalls work before you look at this chat, though!" 
    
    call answer 
    menu:
        "What should I look at first?":
            m "What should I look at first?"   (pauseVal=0)
            u "Well, the first thing I recommend is to just play through the Tutorial Day." 
            u "It showcases some of the features so you know what sorts of things you can do with the program." 
    
    u "I won't keep you much longer. Enjoy the program!" 
    call exit(u) 
    
    jump chat_end
