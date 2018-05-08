#init python:

    ## You can declare characters here and their profile pictures
    ## As of now, you can either change profile pictures here or by updating
    ## the variable (see the example when MC is changed later in this label)
    ## Each entry is of the style:
    ## "Short Form": "address of profile photo"
default chatportrait = {'Ju': 'Profile Pics/Jumin/ju-default.png', 
                    'Zen': 'Profile Pics/Zen/zen-default.png', 
                    'Sev': 'Profile Pics/Seven/sev-default.png', 
                    'Yoo' : 'Profile Pics/Yoosung/yoo-default.png',                     
                    'Ja': 'Profile Pics/Jaehee/ja-default.png',                    
                    'V' : 'Profile Pics/V/V-default.png',
                    'MC' : 'Profile Pics/MC/MC-1.png', 
                    'Ray' : 'Profile Pics/Ray/ray-default.png',
                    'Rika' : 'Profile Pics/Rika/rika-default.png',
                    
                    'Unk' : 'Profile Pics/Unknown/Unknown-1.png',
                    'Sae' : 'Profile Pics/Saeran/sae-1.png'
                    } 

    ## This is where you store character nicknames so you don't
    ##  have to type out their full name every time
    ##  Somewhat moot as I've declared variables to hold the name of
    ##  their nickname elsewhere, but it's still useful
    ## Format:
    ## "Nickname/Short Form": "Full Name as it should appear in the chat"
default chatnick = {'Sev': '707', 
                'Zen': 'ZEN', 
                'Ja' : 'Jaehee Kang', 
                'Ju' : 'Jumin Han', 
                'Yoo' : 'Yoosung★', 
                'MC' : 'MC♥',     # This is the default name and is replaced when the user enters a custom one
                'Rika' : 'Rika',
                'V' : 'V',
                'Sae' : 'Saeran',
                'Unk' : 'Unknown',
                "msg" : "msg", 
                "filler" : "filler",
                'Ray' : 'Ray'
                } 
                
default text_msg_menu = {'Ju': '', 
                        'Zen': '', 
                        'Sev': '', 
                        'Yoo' : '',                     
                        'Ja': '',                    
                        'V' : '', 
                        'Ray' : '',
                        'Rika' : '',
                        
                        'Unk' : '',
                        'Sae' : ''
                        } 
                                                
default recent_texts = {'Ju': True, 
                        'Zen': True, 
                        'Sev': True, 
                        'Yoo' : True,                     
                        'Ja': True,                    
                        'V' : True, 
                        'Ray' : True,
                        'Rika' : True,
                        
                        'Unk' : True,
                        'Sae' : True
                        } 
                        
default show_queue = []
default new_notifications = False

#********************
#**CLOCK*************
#********************
#Analogue or Digital, hours, minutes, size, second hand, military time
default myClock = Clock(True, 3, 0, 150, False, False) 

    
default chatbackup = Chatentry("filler","","")
default pv = 0.8
default oldPV = pv
default they = "she"
default them= "her"
default their = "her"
default theirs = "hers"
default themself = "herself"

# Variable that checks if you're on a route or not
default persistent.on_route = False
# Variable that checks if it's the first time you've started the game
default persistent.first_boot = True
default route_title = 'casual'
default day_num = '1st'
default chatroom_name = 'What I Want to Say'

# Set this to the name of the label you want to jump to
# after your chatroom is finished
default post_chatroom = False

# This variable is set to True if you're viewing a chatroom
# in 'history'
default observing = False

default menu_list = ['chat_home', 'profile_pic', 'other_settings', 
                    'chara_profile', 'save', 'load', 'preferences', 
                    'text_message_hub', 'text_message_screen']
                    
default text_messages = [Text_Message('Ju', []),
                        Text_Message('Ja', []),
                        Text_Message('Ray', []),
                        Text_Message('Rika', []),
                        Text_Message('Sev', []),
                        Text_Message('V', []),
                        Text_Message('Yoo', []),
                        Text_Message('Zen', []),
                        
                        Text_Message('Unk', []),
                        Text_Message('Sae', [])
                        ]
default text_later = []
default text_queue = [Text_Message('Ju', []),
                        Text_Message('Ja', []),
                        Text_Message('Ray', []),
                        Text_Message('Rika', []),
                        Text_Message('Sev', []),
                        Text_Message('V', []),
                        Text_Message('Yoo', []),
                        Text_Message('Zen', []),
                        
                        Text_Message('Unk', []),
                        Text_Message('Sae', [])
                        ]
default contacts = []  


label define_variables:

    # Several variables are defined here so that Ren'Py
    # will save them after you begin a game
    
    python:
        #************************************
        # Heart Points
        #************************************
        heart_points = {'Sev' : 0, 
                        'Zen' : 0, 
                        'Ja' : 0, 
                        'Ju' : 0, 
                        'Yoo' : 0, 
                        'Rika' : 0,
                        'V' : 0,
                        'Unk' : 0,
                        'Sae' : 0
                        }     
                        
        route_title = 'casual'
        day_num = '1st'
    
    if persistent.first_boot:
        call screen profile_pic
    
    python:
    
        persistent.first_boot = False
        name = persistent.name    
        
        text_messages = [Text_Message('Ju', []),
                        Text_Message('Ja', []),
                        Text_Message('Ray', []),
                        Text_Message('Rika', []),
                        Text_Message('Sev', []),
                        Text_Message('V', []),
                        Text_Message('Yoo', []),
                        Text_Message('Zen', []),
                        
                        Text_Message('Unk', []),
                        Text_Message('Sae', [])
                        ]
        text_later = []
        text_queue = [Text_Message('Ju', []),
                        Text_Message('Ja', []),
                        Text_Message('Ray', []),
                        Text_Message('Rika', []),
                        Text_Message('Sev', []),
                        Text_Message('V', []),
                        Text_Message('Yoo', []),
                        Text_Message('Zen', []),
                        
                        Text_Message('Unk', []),
                        Text_Message('Sae', [])
                        ]
        contacts = []  
                    
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
        # Currently these are unused
        chatArchive = {}    # this will be a dictionary
                            # that stores an entire chatroom per index
                            # The idea is to store chats in this dictionary with the key as the day,
                            # and then the value is a list of chatlog lists
                           
        ## You can declare characters here and their profile pictures
        ## As of now, you can either change profile pictures here or by updating
        ## the variable (see the example when MC is changed later in this label)
        ## Each entry is of the style:
        ## "Short Form": "address of profile photo"
        chatportrait = {'Ju': 'Profile Pics/Jumin/ju-default.png', 
                        'Zen': 'Profile Pics/Zen/zen-default.png', 
                        'Sev': 'Profile Pics/Seven/sev-default.png', 
                        'Yoo' : 'Profile Pics/Yoosung/yoo-default.png',                     
                        'Ja': 'Profile Pics/Jaehee/ja-default.png',                    
                        'V' : 'Profile Pics/V/V-default.png',
                        'MC' : 'Profile Pics/MC/MC-1.png', 
                        'Ray' : 'Profile Pics/Ray/ray-default.png',
                        'Rika' : 'Profile Pics/Rika/rika-default.png',
                        
                        'Unk' : 'Profile Pics/Unknown/Unknown-1.png',
                        'Sae' : 'Profile Pics/Saeran/sae-1.png'
                        } 

        ## This is where you store character nicknames so you don't
        ##  have to type out their full name every time
        ##  Somewhat moot as I've declared variables to hold the name of
        ##  their nickname elsewhere, but it's still useful
        ## Format:
        ## "Nickname/Short Form": "Full Name as it should appear in the chat"
        chatnick = {'Sev': '707', 
                    'Zen': 'ZEN', 
                    'Ja' : 'Jaehee Kang', 
                    'Ju' : 'Jumin Han', 
                    'Yoo' : 'Yoosung★', 
                    'MC' : 'MC♥',     # This is the default name and is replaced when the user enters a custom one
                    'Rika' : 'Rika',
                    'V' : 'V',
                    'Sae' : 'Saeran',
                    'Unk' : 'Unknown',
                    "msg" : "msg", 
                    "filler" : "filler",
                    'Ray' : 'Ray'
                    } 
                    
        ## The characters' status as it shows up on their profile page
        chatstatus = {'Sev': "707's status", 
                    'Zen': "Zen's status", 
                    'Ja' : "Jaehee's status", 
                    'Ju' : "Jumin's status", 
                    'Yoo' : "Yoosung's status",
                    'Rika' : "Rika's status",
                    'V' : "V's status",
                    'Sae' : "Saeran's status",
                    'Unk' : "Unknown's status",
                    'Ray' : "Ray's status"} 
                    
        ## The characters' cover photos as it shows up on their profile page
        chatcover = {'Sev': "Cover Photos/profile_cover_photo.png", 
                    'Zen': "Cover Photos/profile_cover_photo.png", 
                    'Ja' : "Cover Photos/profile_cover_photo.png", 
                    'Ju' : "Cover Photos/profile_cover_photo.png", 
                    'Yoo' : "Cover Photos/profile_cover_photo.png", 
                    'Rika' : "Cover Photos/profile_cover_photo.png", 
                    'V' : "Cover Photos/profile_cover_photo.png", 
                    'Sae' : "Cover Photos/profile_cover_photo.png", 
                    'Unk' : "Cover Photos/profile_cover_photo.png", 
                    'Ray' : "Cover Photos/profile_cover_photo.png"} 
                    
        # A dictionary corresponding to your text message history
        # for each character. They begin as empty lists
        #text_messages = {'Ju': [], 
        #                'Zen': [], 
        #                'Sev': [], 
        #                'Yoo' : [],                     
        #                'Ja': [],                    
        #                'V' : [], 
        #                'Ray' : [], 
        #                'Rika' : [],
                        
       #                 'Unk' : [],
       #                 'Sae' : []
       #                 } 
        
        # This list keeps track of who sent you the most recent message
        # The second value is True if the message has been read, and False if not
        recent_texts = {'Ju': True, 
                        'Zen': True, 
                        'Sev': True, 
                        'Yoo' : True,                     
                        'Ja': True,                    
                        'V' : True, 
                        'Ray' : True,
                        'Rika' : True,
                        
                        'Unk' : True,
                        'Sae' : True
                        } 
                    
        # Keeps track of the menu to go to if the player
        # wants to reply to a received text message
        text_msg_menu = {'Ju': '', 
                        'Zen': '', 
                        'Sev': '', 
                        'Yoo' : '',                     
                        'Ja': '',                    
                        'V' : '', 
                        'Ray' : '',
                        'Rika' : '',
                        
                        'Unk' : '',
                        'Sae' : ''
                        } 
        
        # This variable keeps track of whether or not the player
        # is making a choice/on a choice menu
        choosing = False
        
        # The code below updates MC's profile picture and name
        thepic = 'Profile Pics/MC/MC-[persistent.MC_pic].png'
        if chatportrait["MC"] != thepic:
            mcImage = {"MC": thepic}
            chatportrait.update(mcImage)
            
        if chatnick["MC"] != persistent.name:
            mcName = {"MC": persistent.name}
            chatnick.update(mcName)
               
        
    $ renpy.retain_after_load()

    return
        
label start:

    call define_variables
    # Presumably an intro chat here
    call screen chat_home

    stop music
    show screen starry_night    
    show screen clock_screen


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

    ra "{=curly}I'm going to test posting some images!{/=curly}"
    ra "general_cg1" (img=True)
    ra "seven_cg1" (img=True)
    ra "saeran_cg1" (img=True)
    ra "{image=ray happy}" (img=True)
    
    # Anything after this call may or may not be seen by the player depending on
    # how fast they reply. The second value passed to continue_answer (in this case, 8)
    # is how long the player has to decide on an answer
    call continue_answer("menu1", 8)
    
    s "This doesn't happen in-game, but"
    s "I was hoping to have some timed menus where the chat will keep going."
    ra "Here are some lines of dialogue you may or may not see"
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
            
    ra "What parts of the chat did you see?"
    s "Did it work?"
    ra "I hope so!" (bounce=True)
    ra "{image=ray happy}" (img=True)
    call save_exit
    return
    
label chat1:
    ra "Did you not pick a reply?" (bounce=True, specBubble="sigh_m")
    ra "{image=ray cry}" (img=True)
    call save_exit
    return

label add_texts:
    python:          
        text_messages['Ju'].append(Chatentry('Ju', "Some test text", upTime()))
        text_messages['Ju'].append(Chatentry('MC', "A reply", upTime()))
        text_messages['Ju'].append(Chatentry('Ju', "Honestly this would be so much easier if it would just save things", upTime()))
    
        addtext('Ju', "Testing if the dumb screen shows up", 'Ju')
        addtext('MC', "Test 2", 'Ju')
        addtext('Ju', "Have you seen Elizabeth the 3rd lately?", 'Ju')
    
    #show screen loading_screen
    #ju "Test message with the new system." (txtmsg=True, messager="Ju")
    #m "Sample reply." (txtmsg=True, messager="Ju")
    #ju "Thanks." (txtmsg=True, messager="Ju")    
    $ renpy.retain_after_load()
    #hide screen loading_screen
    call screen chat_home


    
