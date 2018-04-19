init python:
    from datetime import datetime
    
    def upTime():
        thetime = datetime.now().strftime('%a, %b %d %I:%M:%S%p')
        return thetime

    ##************************************
    ## For ease of adding Chatlog entries
    ##************************************   

    def addchat(who, what, pauseVal, img=False, bounce=False, specBubble=""):  
        global choosing
        choosing = False
        global pre_choosing
        pre_choosing = False
        
    
        global pv
        if pauseVal == None:
            pauseVal = pv;
    
        if len(chatlog) > 1:
            finalchat = chatlog[-2]
            if finalchat.who == "answer" or finalchat.who == "pause":
                # Not supposed to display this bubble
                del chatlog[-2]  
                
        if who != "pause":
            pauseFailsafe()
            global chatbackup
            chatbackup = Chatentry(who, what, upTime(), img, bounce, specBubble)
            global oldPV
            oldPV = pauseVal        
                    
        
        if who == "answer" or who == "pause":
            renpy.pause(pauseVal)#, hard=True)
        elif pauseVal == 0:
            pass
        else:
            typeTime = what.count(' ') + 1 # should be the number of words
            # Since average reading speed is 200 wpm or 3.3 wps
            typeTime = typeTime / 3
            if typeTime < 1.5:
                typeTime = 1.5
            typeTime = typeTime * pauseVal
            renpy.pause(typeTime)#, hard=True)
        
        if img == True:
            if what in emoji_lookup:
                renpy.play(emoji_lookup[what], channel="voice_sfx")
           
        chatlog.append(Chatentry(who, what, upTime(), img, bounce, specBubble))
        
            
            
    ## Function that checks if an entry was successfully added to the chat
    ## A temporary fix for the pause button bug
    ## This also technically means a character may be unable to post the exact
    ## same thing twice in a row depending on when the pause button is used
    def pauseFailsafe():
        global chatbackup
        global oldPV
        last_entry = None
        if len(chatlog) > 0:
            last_entry = chatlog[-1]
            if last_entry.who == "answer":
                # Last entry is now two from the final entry
                if len(chatlog) > 1:
                    last_entry = chatlog[-2]
        if chatbackup.who == "filler" or chatbackup.who == "answer":
            return
        if last_entry != None and last_entry.who == chatbackup.who and last_entry.what == chatbackup.what:
            # Means the last entry successfully made it to the chat log
            return
        else:
            # User may have paused somewhere in there and the program skipped a
            # dialogue bubble; post it first before posting the current entry
            typeTime = chatbackup.what.count(' ') + 1 # should be the number of words
            # Since average reading speed is 200 wpm or 3.3 wps
            typeTime = typeTime / 3
            if typeTime < 1.5:
                typeTime = 1.5
            typeTime = typeTime * oldPV
            renpy.pause(typeTime)
            
            if chatbackup.img == True:
                if chatbackup.what in emoji_lookup:
                    renpy.play(emoji_lookup[chatbackup.what], channel="voice_sfx")
               
            chatlog.append(Chatentry(chatbackup.who, chatbackup.what, upTime(), chatbackup.img, chatbackup.bounce, chatbackup.specBubble))
            
     
        

    
default chatbackup = Chatentry("filler","","")
default pv = 0.8
default oldPV = pv
image photo = im.FactorScale("photo.png",0.4)
image NEW = "Bubble/NEW-sign.png"

     
default myClock = Clock(True, 3, 0, 150, False, False) #Analogue or Digital, hours, minutes, size, second hand, military time


default player_present = True

# The game starts here.

label start:
    
    $ choosing = False
    $ player_present = True
    stop music
    #********************
    #**CLOCK*************
    #********************

    ###Digital Clock###
    $ myClock.analogue = False
    $ myClock.mil_time = False
    $ myClock.set_time(0,0)
    $ myClock.second_hand_visible = False
    $ myClock.runmode("real")


    # ****************************
    # *******Fetch Name***********
    # ****************************

    $ chatlog = []
    scene evening
    
    $ name = renpy.call_screen("input", prompt="Please enter a username", defAnswer = "Sujin")
    $ name = name.strip()
    
    $ mcImage = {"MC": 'Profile Pics/MC/MC-2.png'}
    $ mcName = {"MC": "[name]"}

    $ chatportrait.update(mcImage)
    $ chatnick.update(mcName)

    $ stutter = name[:1]
    $ nameLength = len(name)
    $ nameEnd = name[nameLength - 1]
    $ nameCaps = name.upper()
    $ nameLow = name.lower()
    $ nameTypo = name[:nameLength - 1]

   
    
    #********************
    #Clear the chatlog
    #*******************
    $ chatlog = []

    show screen clock_screen
    scene evening

    menu navi:
        "Go to Coffee Chatroom":
            jump coffee_chat
        "Go to example chatroom":
            jump example_chat
        #"Chapter 18":
        #    jump chapter_18
        "Timed Menus":
            jump timed_menus
        "Visual Novel":
            jump vn_mode
       
            
            
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



    
