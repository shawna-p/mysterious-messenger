

#********************
#**CLOCK*************
#********************
#Analogue or Digital, hours, minutes, size, second hand, military time
default myClock = Clock(False, 0, 0, 150, False, False) 

default they = "she"
default them= "her"
default their = "her"
default theirs = "hers"
default themself = "herself"

# Variable that checks if you're on a route or not
default persistent.on_route = False
# Variable that checks if it's the first time you've started the game
default persistent.first_boot = True

# This variable is set to True if you're viewing a chatroom
# in 'history'
default observing = False

##****************************
##DECLARE CHARACTERS HERE
##****************************

## Character declarations
default s = Chat("707", "s", 'Profile Pics/Seven/sev-default.png', 'Profile Pics/s_chat.png', "Cover Photos/profile_cover_photo.png", "707's status")
default y = Chat("Yoosung★", 'y', 'Profile Pics/Yoosung/yoo-default.png', 'Profile Pics/y_chat.png', "Cover Photos/profile_cover_photo.png", "Yoosung's status")
default m = Chat("MC", 'm', 'Profile Pics/MC/MC-1.png')
default ja = Chat("Jaehee Kang", 'ja', 'Profile Pics/Jaehee/ja-default.png', 'Profile Pics/ja_chat.png', "Cover Photos/profile_cover_photo.png", "Jaehee's status")
default ju = Chat("Jumin Han", 'ju', 'Profile Pics/Jumin/ju-default.png', 'Profile Pics/ju_chat.png', "Cover Photos/profile_cover_photo.png", "Jumin's status")
default z = Chat("ZEN", 'z', 'Profile Pics/Zen/zen-default.png', 'Profile Pics/z_chat.png', "Cover Photos/profile_cover_photo.png", "Zen's status")
default ri = Chat("Rika", 'ri', 'Profile Pics/Rika/rika-default.png', 'Profile Pics/ri_chat.png', "Cover Photos/profile_cover_photo.png", "Rika's status")
default r = Chat("Ray", 'r', 'Profile Pics/Ray/ray-default.png', 'Profile Pics/r_chat.png', "Cover Photos/profile_cover_photo.png", "Ray's status")
default sa = Chat("Saeran", "sa", 'Profile Pics/Saeran/sae-1.png', 'Profile Pics/sa_chat.png', "Cover Photos/profile_cover_photo.png", "Saeran's status")
default u = Chat("Unknown", "u", 'Profile Pics/Unknown/Unknown-1.png', 'Profile Pics/u_chat.png', "Cover Photos/profile_cover_photo.png", "Unknown's status")
default v = Chat("V", 'v', 'Profile Pics/V/V-default.png', 'Profile Pics/v_chat.png', "Cover Photos/profile_cover_photo.png", "V's status")
   
define msg = Chat("msg")
define filler = Chat("filler")
define answer = Chat('answer', 'delete')
define chat_pause = Chat('pause', 'delete')

default character_list = [ju, z, s, y, ja, v, m, r, ri]

default menu_list = ['chat_home', 'profile_pic', 'other_settings', 
                    'chara_profile', 'save', 'load', 'preferences', 
                    'text_message_hub', 'text_message_screen']
                    
default text_messages = [Text_Message(ju, []),
                        Text_Message(ja, []),
                        Text_Message(r, []),
                        Text_Message(ri, []),
                        Text_Message(s, []),
                        Text_Message(v, []),
                        Text_Message(y, []),
                        Text_Message(z, []),
                        
                        Text_Message(u, []),
                        Text_Message(sa, [])
                        ]
default text_later = []
default text_queue = [Text_Message(ju, []),
                        Text_Message(ja, []),
                        Text_Message(r, []),
                        Text_Message(ri, []),
                        Text_Message(s, []),
                        Text_Message(v, []),
                        Text_Message(y, []),
                        Text_Message(z, []),
                        
                        Text_Message(u, []),
                        Text_Message(sa, [])
                        ]
default contacts = []  
default chatlog = []
default current_chatroom = Chat_History('day', 'title', 'auto', 'chatroom_label', '00:00')

label define_variables:

    # Several variables are defined here so that Ren'Py
    # will save them after you begin a game
    
    python:                        
        myClock.runmode('real')
    
    if persistent.first_boot:
        call screen profile_pic
    
    python:
    
        persistent.first_boot = False
        name = persistent.name    
        
        menu_list = ['chat_home', 'profile_pic', 'other_settings', 
                    'chara_profile', 'save', 'load', 'preferences', 
                    'text_message_hub', 'text_message_screen']

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
    # Presumably an intro chat here

    call screen chat_home

    menu navi:
        "Go to Coffee Chatroom":
            jump coffee_chat
        "Go to example chatroom":
            jump example_chat
        "Timed Menus":
            jump timed_menus
        #"Visual Novel":
        #    jump vn_mode
        "Text test":
            jump text_msg_test
        "Chapter select":
            jump chapter_select1
       
            
            
# Some experiments with timed menus; MysMe doesn't use this feature
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


    
