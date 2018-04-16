init python:
    from datetime import datetime
    
    def upTime():
        thetime = datetime.now().strftime('%a, %b %d %I:%M:%S%p')
        return thetime

    ##************************************
    ## For ease of adding Chatlog entries
    ##************************************   

    def addchat(who, what, pauseVar, img=False, bounce=False, specBubble=""):  
        if len(chatlog) > 1:
            finalchat = chatlog[-2]
            if finalchat.who == "answer":
                # Not supposed to display this bubble
                del chatlog[-2]  
        if who != "pause":
            pauseFailsafe()
            global chatbackup
            chatbackup = Chatentry(who, what, upTime(), img, bounce, specBubble)
            global oldPV
            oldPV = pauseVar        
        global choosing
        choosing = False
        
        typeTime = what.count(' ') + 1 # should be the number of words
        # Since average reading speed is 200 wpm or 3.3 wps
        typeTime = typeTime / 3
        if typeTime < 1.5:
            typeTime = 1.5
        typeTime = typeTime * pauseVar
        if who == "answer" or who == "pause":
            renpy.pause(pauseVar)#, hard=True)
        else:
            renpy.pause(typeTime)#, hard=True)
        
        if img == True:
            if what in emoji_lookup:
                renpy.play(emoji_lookup[what], channel="voice_sfx")
           
        chatlog.append(Chatentry(who, what, upTime(), img, bounce, specBubble))
        
            
            
    ## Function that checks if an entry was successfully added to the chat
    ## A temporary fix for the pause button bug
    ## FIXME: tends to cause the last bubble to flicker slightly when pause is activated
    ## This also technically means a character may be unable to post the exact
    ## same thing twice in a row depending on when the pause button is used
    def pauseFailsafe():
        global chatbackup
        global oldPV
        if len(chatlog) > 0:
            last_entry = chatlog[-1]
            if last_entry.who == "answer":
                # Last entry is now two from the final entry
                if len(chatlog) > 1:
                    last_entry = chatlog[-2]
        if chatbackup.who == "filler" or chatbackup.who == "answer":
            return
        if last_entry.who == chatbackup.who and last_entry.what == chatbackup.what:
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
image cg1-small = "CGs/cg-1-small.png"
image cg1 = "CGs/cg-1.png"
image NEW = "Bubble/NEW-sign.png"
     
default myClock = Clock(True, 3, 0, 150, False, False) #Analogue or Digital, hours, minutes, size, second hand, military time


    

# The game starts here.

label start:
    
    $ global choosing
    $ choosing = False
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
        "Clickable Images":
            jump click_image
        "Visual Novel":
            jump vn_mode
            
            
label click_image:

    call chat_begin
    call redhack
    call chat_begin
    scene earlyMorn

    $ addchat(ra,"{=curly}I'm going to test posting some images!{/=curly}", pv, False, False)
    $ addchat(ra,"{image=cg1-small}", pv, True, False)
    $ addchat(ra,"That's how we usually post images,", pv, False, False)
    $ addchat(ra,"{=ser1}but you can't click them T_T{/=ser1}", pv, False, True, "sigh_m")
    $ addchat(ra,"cg1-small", pv, True, False)
    $ addchat(ra,"Gonna try that now.", pv, False, False)
    
    pause 10
    jump click_image



    
