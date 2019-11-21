
## This feature may require more testing than other parts
## of the program. It allows characters to continue talking
## while the player has an opportunity to interrupt/answer
## See explanation below
label timed_menus():

    call chat_begin("earlyMorn") 
    call play_music(geniusly_hacked_bebop)
    s "{size=+10}Hiya!{/size}"   (bounce=True, specBubble="round2_s")
    s "Did you know there's this super-secret feature called timed menus?" 
    s "I've been experimenting with it for a while, and it's finally ready to show off!" (bounce=True)
    s "It works mostly like regular menus," 
    s "{=ser1}except the characters will keep talking even after the answer button shows up at the bottom of the screen.{/=ser1}" 
    s "Like now!"   (bounce=True)
    
    # Anything after this call may or may not be seen by the player depending on
    # how fast they reply and how fast their chat speed is
    # The first value is the menu to jump to if the player hits 'answer'
    # The second value passed to continue_answer (in this case, 8) is how
    # many seconds the player has to decide on an answer
    # Most of these screens/labels are in screen effects.rpy at the bottom
    call continue_answer("menu1", 8) 
    
    s "You only have so long to reply," 
    s "and when the spaceship at the bottom of the screen reaches the right side," 
    s "BAM!!"   (bounce=True, specBubble="spike_s")
    s "The opportunity to answer has passed!!!" 
    # The time given to reply will change depending on the chat speed, so players
    # who need more time to read will also have a longer time window to reply
    # This means that everyone will see the same number of speech bubbles. In this
    # example, they will see up to these messages, but unless they don't reply
    # they won't see the dialogue after this comment. You may need some trial/error 
    # to know how much dialogue you can include before a timer runs out
    # If the player is using MAX speed, it will skip over the timer entirely and there
    # will be no opportunity to interrupt
    s "You write these menus a bit differently than regular menus" 
    s "You'll see an example of it in this code." 
   
    # You'll need to preface the menu with 'if timed_choose:' or else the menu
    # will simply show up after the dialogue before it is exhausted (though if you
    # need the player to reply regardless, you may want to leave it out)
    # If the player chooses an option, it will finish displaying the most recent
    # line of dialogue from above, then move on to the dialogue after the choice
    # If nothing is chosen, it will finish displaying the above dialogue, skip
    # over the menu, and keep going
    if timed_choose:
        menu menu1: # Don't forget to name the menu whatever you called it before
            "Slow down! Timed menus??":
                m "Slow down! Timed menus??" 
                s "Whoops lolol I got a bit excited" 
                s "{=sser2}Yup! Maybe try playing through this chatroom a few times to see what happens?{/=sser2}" 
                s "Don't forget to turn Testing Mode on from the settings so you can make different choices." 

            "So I can choose between listening or interrupting?" :
                m "So I can choose between listening or interrupting?" 
                s "Yeah! If you just let the chat play out," 
                s "you'll see different dialogue than if you'd decided to answer." 

                
    else:
        # This is optional additional dialogue the player will
        # only see if they don't reply
        s "If you don't reply and just listen," 
        s "maybe you'll see some interesting dialogue!" 
            
    s "I hope this gives you some cool ideas for ways to write chatrooms!" 
    s "{image=seven wow}"   (img=True)
    s "{=curly}Toodles~!{/=curly}"   (bounce=True, specBubble="cloud_s")
    call exit(s)
    
    jump chat_end
    
## A small work-around to prevent program errors; this just redirects the
## "expired" chatroom to the regular one
label timed_menus_expired():
    jump timed_menus

    
