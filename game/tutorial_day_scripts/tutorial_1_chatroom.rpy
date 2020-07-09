label example_chat():

    $ first_choice = True
    $ choice_picked = None
       
    # This sets up a very specific phone call which will never expire
    # You should generally never add phone calls this way
    $ available_calls.append(PhoneCall(r, 'test_call', 'outgoing', 'test'))
       
    call hack 
    call chat_begin("hack")  
    call play_music(mystic_chat)
    call enter(u) 
    u "{=curly}Hello, [name] ^^{/=curly}" 
    u "I thought you might come by." 
    u "{=curly}You want to learn more about how to make a chatroom, right?{/=curly}" (bounce=True)
    u "I've come to show off a few of its features." 
    
    call answer 
    menu:
        "Let's get started!":
            m "Let's get started!" (pauseVal=0)
            u "{=sser2}Great! That's the kind of attitude I'm looking for ^^{/=sser2}"  
        
        "What if I don't know any coding?":
            m "What if I don't know any coding?" (pauseVal=0)
            u "{=sser2}Don't worry! I've tried to make this as easy to use as possible.{/=sser2}" 
            u "{=sser2}There's an extensive {a=https://github.com/shawna-p/mysterious-messenger/wiki}Wiki{/a} included with the program to look at,{/=sser2}"
            u "{=sser2}and I'll also be monitoring the{a=https://discord.gg/BPbPcpk} Mysterious Messenger Discord server{/a} if you have questions.{/=sser2}" 
            u "This project was coded in Ren'Py, so you can always check out their forums, too." 

    u "Anyway, you can see what we just did there was a menu!" 
    u "It allows you to alter a conversation based on responses." 
    u "If you take a look {b}tutorial_1_chatroom.rpy{/b}, you can get an idea of how to use them." 
    u "{=ser1}There are lots of things to learn about!{/=ser1}" 
    u "{=ser1b}What would you like to see first?{/=ser1b}" 
       
    call answer 
    # This unusual bit of code tells the program to shuffle
    # all the choices except the last one
    # In general you won't mess with this
    if not first_choice:
        $ shuffle = "last"
    menu learn:    
    
        "Emojis and Images" if not choice_picked == "emojis":
            $ choice_picked = "emojis"
            if first_choice:
                m "I want to learn how to use emojis and images" (pauseVal=0) 
                $ first_choice = False
                u "{=ser1}Emojis and images, huh?{/=ser1}"
                u "{=ser1}Okay. I'll let someone else explain this.{/=ser1}"
                u "I'll be back later ^^"
                call exit(u) 
            pause 0.5  
            jump emojis
            
        "Banners & Other" if not choice_picked == "banners":
            $ choice_picked = "banners"
            if first_choice:
                m "Can you teach me about banners?" (pauseVal=0) 
                $ first_choice = False
                u "{=ser1}Oh, banners?{/=ser1}"
                u "{=ser1}Okay. I'll let someone else explain this.{/=ser1}"
                u "I'll be back later ^^"
                call exit(u) 
            pause 0.5
            jump banners
            
        "Heart Icons" if not choice_picked == "heart icons":
            $ choice_picked = "heart icons"
            if first_choice:
                m "I'd like to learn about heart icons" (pauseVal=0) 
                $ first_choice = False
                u "{=curly}Heart icons?{/=curly}" (bounce=True)
                u "{=ser1}Hmm, sounds good. I'll let someone else explain this.{/=ser1}"
                u "I'll be back later ^^" (bounce=True)
                call exit(u) 
            pause 0.5
            jump heart_icons
            
        "Screen Shake and Special Bubbles" if not choice_picked == "spec bubbles":
            $ choice_picked = "spec bubbles"
            if first_choice:
                m "Screen shake and special bubbles, please" (pauseVal=0) 
                $ first_choice = False
                u "{=ser1}You want to know about special speech bubbles and screen shake?{/=ser1}" (bounce=True)
                u "{=ser1}Alright then. I'll let someone else explain this.{/=ser1}"
                u "I'll be back later ^^" (bounce=True)
                call exit(u) 
            pause 0.5
            jump screen_shake
            
        "I'm done for now" if not first_choice:
            jump ending
            
label emojis():

    call hack 
    call chat_begin("morning",False,False) 
    
    call play_music(geniusly_hacked_bebop)
    call enter(s) 
    s "O" (pauseVal=0.1)
    s "M" (pauseVal=0.1)
    s "G" (pauseVal=0.1)
    s "{=sser2}{size=+10}I get to explain emojis!!!{/size}{/=sser2}" 
    s "{image=seven_wow}"   (img=True)
    s "{=sser2}{size=+10}Yay!!!{/size}{/=sser2}"   (bounce=True, specBubble="spike_m")
    s "The program has a whole bunch of emojis defined in {b}emoji_definitions.rpy{/b} already,"
    s "and it will even play the right sound effect for you when the emoji is shown."    
    s "{=ser1b}You also need to make sure the program knows the the message contains an image (using {b}(img=True){/b} after the dialogue){/=ser1b}"
    s "{=blocky}otherwise it'll look like this lolol{/=blocky}"
    s "{image=seven_wow}"
    s "{=sser2}Which is probably not what you want!{/=sser2}" 
    s "{=sser2}You'll have to be careful to get the spelling right,{/=sser2}" 
    s "since otherwise you'll get an \"image not found\" message."
    s "{=blocky}And it won't play any sound files, either!{/=blocky}" (bounce=True)
    s "{=ser1}If you want to add more emojis,{/=ser1}"
    s "{=ser1}there's a whole section on just that in the wiki.{/=ser1}"
    s "{=curly}Now I'll let you check out the emojis currently coded into the game.{/=curly}"
    s "{=sser2}Just select a character to see the available emojis or \"Done\" if you're finished{/=sser2}"   (bounce=True)

    
    call answer 
    $ shuffle = False
    menu emoji:
        "Casual Story Characters":
            $ shuffle = False
            menu:
                "Jaehee":
                    $ shuffle = False
                    jump jaehee_emoji
                "Zen":
                    $ shuffle = False
                    jump zen_emoji
                "Yoosung":
                    $ shuffle = False
                    jump yoosung_emoji
                "<- Back":
                    $ shuffle = False
                    jump emoji

        "Deep Story Characters":
            $ shuffle = False
            menu:
                "Jumin":
                    $ shuffle = False
                    jump jumin_emoji
                "Seven":
                    $ shuffle = False
                    jump seven_emoji
                "<- Back":
                    $ shuffle = False
                    jump emoji

        "Another Story Characters":
            $ shuffle = False
            menu:
                "Ray":
                    $ shuffle = False
                    jump ray_emoji
                "Saeran":
                    $ shuffle = False
                    jump saeran_emoji
                "V":
                    $ shuffle = False
                    jump v_emoji
                "<- Back":
                    $ shuffle = False
                    jump emoji

        "Bonus/Other Characters":
            $ shuffle = False
            menu:
                "Rika":
                    $ shuffle = False
                    jump rika_emoji
                "Saeran (sweater)":
                    $ shuffle = False
                    jump saeran2_emoji
                "<- Back":
                    $ shuffle = False
                    jump emoji


     
        "Done":
            s "{=sser2}The last thing I'm here to explain is how to post CGs.{/=sser2}" (pauseVal=0)
            s "{=curly}That means images like this!{/=curly}" (bounce=True)
            s "s_1" (img=True)
            s "{=sser1b}They're fully clickable like they are in-game; check it out!{/=sser1b}"
            s "You can post CGs too!"
            call answer
            menu:
                "I can?":
                    m "I can?" (pauseVal=0)
                    s "Yeah! Give it a try!" 
                    # You can either write the "cg s_1" or just "s_1" so long
                    # as you check off (img=True)
                    m "cg s_1" (img=True)                    
                "(Try posting)":
                    m "s_1" (img=True, pauseVal=0)
            m "{image=seven_wow}" (img=True)
            s "Yeah, just like that!"
            s "{=sser2}You post these a little differently from emojis. {/=sser2}" 
            s "There's more information in the {b}wiki{/b}."
            s "{=ser1}The program will take care of unlocking the image in the gallery and letting players view it full-size!{/=ser1}"
            s "{=ser1}Just make sure you indicate that the message contains an image,{/=ser1}"
            s "{=blocky}Otherwise it'll just show up in text, like this:{/=blocky}"
            s "s_1"
            s "But if you check off the \"Image\" modifier, you get this:" (bounce=True, specBubble="round2_m")
            s "s_1" (img=True)
            s "{=curly}Hope this helped!{/=curly}" (bounce=True, specBubble="round_m")
            s "Let me know if you have any questions later~"
            call exit(s) 
            call answer 
            $ shuffle = "last"
            jump learn


label banners():

    call hack 
    call chat_begin("noon",False,False) 
    call play_music(same_old_fresh_air)
    
    call enter(y) 
    y "{=curly}Hello!{/=curly}"
    y "{=sser2}I'm supposed to explain banners to you.{/=sser2}" 
    y "{=sser2}It's pretty quick, I promise!{/=sser2}" 
    y "{image=yoosung_happy}"   (img=True)
    y "You call them with \"call banner('__')\","
    y "where '__' is the name of the banner you want."
    if not persistent.banners:
        y "It looks like you've got banner animations turned off though!"
        y "So you won't see them."
    else:
        y "Since the animations can be kind of distracting, there's a toggle to turn them off."

    y "Do you want to see banner animations?"
    call answer
    menu:
        "Yes, I want to see banner animations.":
            m "Yes, I want to see banner animations." (pauseVal=0)
            $ persistent.banners = True
            y "Okay!"
        "No, turn banner animations off.":
            m "No, turn banner animations off." (pauseVal=0)
            $ persistent.banners = False
            y "Alright, got it!"
                
    if persistent.banners:
        y "{=sser2}There are four different types of banners:{/=sser2}" 
        y "The lightning banner!" (bounce=True)
        call banner('lightning') 
        y "{=sser2}For when you're feeling angry ^^;;{/=sser2}"
        y "The heart banner!" (bounce=True)
        call banner('heart') 
        y "For happy stuff!"
        y "The annoy banner" (bounce=True)
        call banner('annoy') 
        y "{=sser2}For when you're irritated{/=sser2}"
        y "{=sser2}And last but not least,{/=sser2}"
        y "{=ser1}the 'well' banner!{/=ser1}" (bounce=True)
        call banner('well') 
        y "{=ser1}...{/=ser1}"
        y "{=sser2}It's for times when you're a little lost for words.{/=sser2}"
        y "{image=yoosung_thankyou}"   (img=True)

    y "I have one more thing I was going to show you:" 
    y "{=ser1}it's not in the base game, but in this program you can pick your pronouns.{/=ser1}" 
    y "{=curly}You said you use [they]/[them] pronouns, right?{/=curly}"   (bounce=True, specBubble="square_m")
    y "{=sser2}So we'll use [they]/[them] whenever we talk about you.{/=sser2}"  (bounce=True)
    y "You can check out {b}Short forms/Startup Variables{/b} under {b}variables.rpy{/b} - at the start there are some variables so you know how to use pronouns when writing a script" 
    y "If you want to add any new variables, there's a section in the wiki about doing just that."
    y "And if you ever want to change your pronouns, just go to the profile page (accessed from the main menu)." 
    y "That's all from me!"
    y "{=sser2}Good luck with the program ^^{/=sser2}"
    y "{image=yoosung_wow}" (img=True)
    call exit(y) 

    call answer 
    $ shuffle = "last"
    jump learn
    
label heart_icons():

    call hack 
    call chat_begin("evening",False,False) 
    call play_music(narcissistic_jazz)
    
    call enter(z) 
    z "{image=zen_wink}" (img=True)
    z "{=curly}Hey cutie ^^{/=curly}" (bounce=True)
    z "{=sser2}I'm here to explain heart icons!{/=sser2}"
    z "If you're having a hard time looking at the animation for the heart icons,"
    z "or it's hard to tell them apart,"
    z "There's also an option to turn them into text popups that look like this:"
    show screen stackable_notifications(z.name + " +1")
    z "The animation when you receive an hourglass in a chatroom will also be turned into a text popup."
    z "Would you like to use animated icons or the text notifications?"
    call answer
    menu:
        "I want the regular animated icons.":
            m "I want the regular animated icons." (pauseVal=0)
            $ persistent.animated_icons = True
            z "{=curly}Got it!{/=curly}" (bounce=True)
            z "You'll see the regular heart animation then."

        "I want the text notifications.":
            m "I want the text notifications." (pauseVal=0)
            $ persistent.animated_icons = False
            z "{=curly}Got it!{/=curly}" (bounce=True)
            z "You'll see the text popup whenever someone likes your response."

    z "If you change your mind on what kind of icon you want,"
    z "There's a toggle in the {b}Settings{/b} called {b}Animated Icons{/b}"
    
    z "{=sser2}Anyway, so getting a heart point will look like this:{/=sser2}"
    call heart_icon(z) 
    if not persistent.animated_icons:
        z "And you can lose heart points, too."
        z "You just write {b}call heart_break(z){/b} and give it the ChatCharacter variable you're losing a point with instead of z"
    else:
        z "{=sser2}And each character has a different one{/=sser2}"
        z "{=sser1b}They all use the same white heart, this one{/=sser1b}"
        call heart_icon(u) 
        z "and just recolour it depending on what argument you pass via \"call heart_icon(z)\""
        z "You can easily add your own colours, too, whenever you define a ChatCharacter like in character_definitions.rpy"
        z "{=blocky}Here are the currently available colours:{/=blocky}"
        z "Seven"
        call heart_icon(s) 
        z "{=curly}Me!{/=curly}"
        call heart_icon(z) 
        z "Jaehee"
        call heart_icon(ja) 
        z "Jumin"
        call heart_icon(ju) 
        z "Yoosung"
        call heart_icon(y) 
        z "Ray"
        call heart_icon(r) 
        z "V"
        call heart_icon(v) 
        z "{=ser1}and then there are a few special ones{/=ser1}"
        z "The white heart I mentioned before (tied to the username 'Unknown')"
        call heart_icon(u) 
        z "You can also get this heart by passing heart_icon the short form for Saeran (sa)"
        call heart_icon(sa) 
        z "{=sser2}And then there is this heart{/=sser2}"
        call heart_icon(ri) 
        z "{=sser2}which in this game is for Rika.{/=sser2}"
        z "The last thing I'm here to explain is the 'heartbreak' icon"
        z "It works the same as the regular heart icons -- just call \"heart_break\" with that character"
        z "{=ser1}It will automatically colour itself{/=ser1}"
        z "{=sser2}They look like this!{/=sser2}"

    call heart_break(z) 
    z "{=sser2}But you don't really want to hurt any of our feelings, right?{/=sser2}" (bounce=True)
    z "{image=zen_happy}" (img=True)
    call heart_icon(z) 
    z "{=ser1}The program automatically tallies the heart points you've earned during a chatroom and displays the total after you hit Save&Exit.{/=ser1}"
    z "It keeps track of both the total points earned during a chatroom,"
    z "as well as how many points you have with each individual character"
    z "There's also a second argument you can pass it to have heart points count towards a bad end."
    z "Check out the wiki for more on that!"
    z "{=blocky}Also note that Ray and Saeran's heart points count towards the same character{/=blocky}"
    z "{=curly}Good luck with the rest of the program!{/=curly}" (bounce=True)
    call exit(z) 
    
    call answer 
    $ shuffle = "last"
    jump learn
    
label screen_shake():
    
    call hack 
    call chat_begin("night",False,False) 
    call play_music(lonesome_practicalism)

    call enter(ja) 
    ja "{=ser1}Hello, [name].{/=ser1}"
    ja "{=ser1}Mr. Han will be with us shortly. {/=ser1}"
    ja "{=ser1}Before we begin though, I should ask:{/=ser1}"
    ja "{=ser1}Do you want to see screen shake animations?{/=ser1}"
    call answer
    $ shuffle = False
    menu:
        "Yes, I want to see the screen shake animation.":
            m "Yes, I want to see the screen shake animation." (pauseVal=0)
            $ persistent.screenshake = True
        "No, turn screen shake animation off.":
            m "No, turn screen shake animation off." (pauseVal=0)
            $ persistent.screenshake = False
    
    ja "{=ser1}Understood.{/=ser1}" (bounce=True)
    if persistent.animated_backgrounds:
        $ persistent.screenshake = False
        ja "It looks like you have animated backgrounds turned on."
        ja "Currently screen shake isn't compatible with animated backgrounds,"
        ja "so you won't be able to see screen shake effects."
        ja "You can toggle animated backgrounds and screen shake from the Settings."
    call enter(ju) 
    ja "{=curly}Ah, right on time.{/=curly}" (bounce=True, specBubble="cloud_s")
    ja "{=ser1}Shall we get started then?{/=ser1}"
    pause 1
    ja "{=ser1}...{/=ser1}"
    call banner('well') 
    ja "{=ser1}Mr. Han?{/=ser1}"
    ja "{image=jaehee_well}" (img=True)
    ja "Mr. Han."
    ja "{size=+10}MR. HAN!!{/size}" (bounce=True, specBubble="spike_m")
    call shake
    ju "{=curly}Is something the matter?{/=curly}" (bounce=True, specBubble="cloud_m")
    ja "Oh." (bounce=True, specBubble="sigh_s")
    ja "{=ser1}You weren't responding so I thought perhaps you were asleep.{/=ser1}"
    ju "Elizabeth the 3rd was sleeping on my lap so I couldn't disturb her." (bounce=True, specBubble="cloud_l")
    ja "{=sser2}Of course;;{/=sser2}" (bounce=True, specBubble="sigh_m")
    ja "{=ser1}...As I was saying.{/=ser1}"
    ja "{=sser2}We're supposed to teach [name] about some other chatroom features.{/=sser2}" (bounce=True)
    ju "{=ser1}Like the special speech bubbles?{/=ser1}" (bounce=True, specBubble="square_m")
    ja "{=sser2}Yes ^^{/=sser2}" (bounce=True, specBubble="cloud_s")
    ja "There are many special speech bubbles built into the game."
    ja "{=sser2}Most bubbles come in three sizes:{/=sser2}" (bounce=True)
    ja "{=sser1b}small{/=sser1b}" (bounce=True, specBubble="spike_s")
    ja "{=sser1b}medium{/=sser1b}" (bounce=True, specBubble="spike_m")
    ja "{=sser1b}and large{/=sser1b}" (bounce=True, specBubble="spike_l")
    ja "{=ser1}The text should usually resize itself to fit, but you need to choose the size yourself.{/=ser1}"
    ja "{color=#f00}For example, this bubble might be too small.{/color}" (bounce=True, specBubble="cloud_s")
    if persistent.screenshake:
        ja "{=ser1}As for screen shake,{/=ser1}"
        ja "{=ser1}you simply need to use the call{/=ser1}"
        ja "{=ser1xb}\"call shake\" {/=ser1xb}"
        ja "{=sser2}And it does this{/=sser2}" (bounce=True)
        call shake
    ja "{=ser1}Lastly, you can check out all of the special bubbles present in the game.{/=ser1}"
    ja "{=ser1xb}Just select \"Done\" when you're finished.{/=ser1xb}"
    call answer 
    $ shuffle = False
    jump bubbles
    

label ending():
    call hack 
    call chat_begin("hack",False,False) 
    call play_music(mystic_chat)
    
    call enter(u) 
    u "{=curly}You're back!{/=curly}" (bounce=True)
    u "{=sser2}So what did you think?{/=sser2}"
    u "{=sser2}Are you ready to start making your own chatrooms?{/=sser2}"
    call answer 
    menu:
        "Definitely!":
            m "Definitely!" (pauseVal=0)
            u "{=sser2}I'm glad! ^^{/=sser2}"
                    
        "I don't know if I'm ready yet...":
            m "I don't know if I'm ready yet..." (pauseVal=0)
            u "{=ser1}I recommend checking out the Beginner's Guide in the wiki, which will walk you through creating a chatroom.{/=ser1}"
            u "{=ser1}You can also go through these example chatrooms a few times and compare it with the code.{/=ser1}"

    u "I've put a lot of work into this program, so any feedback is welcome!"
    u "{=sser2}If you decide you'd like to use it somewhere,{/=sser2}"
    u "{=sser2}you must include credit and a link back to my GitHub in your project.{/=sser2}"
    u "{=sser2}Feel free to contact me if you have any questions.{/=sser2}"
    u "I hope you find this program helpful."
    u "Good luck!"
    call exit(u) 
    # Use this at the end of a chatroom
    jump chat_end

## This is a test call that's always available for Ray on Tutorial Day
label test_call():

    call phone_begin 
    
    r_phone "Hello?"
    
    menu:
        extend ''
        "Ray, it's me.":
            m "Ray, it's me."
            r_phone "Oh! It's nice to hear from you, [name]."
            
        "Hello? Can you hear me?":
            m "Hello? Can you hear me?"
            r_phone "Yes! [name], right? It's nice to hear from you."
            
    r_phone """
    
    Looks like you figured out the phone call function, huh?
    
    This is a test call for the program. It's always available on Tutorial Day.
    
    That means you'll never hear my voicemail message, but you can try calling the other characters to hear their voicemail.
    
    Usually, phone calls will timeout two chatrooms after it's first 'activated'.
    
    That means you won't be able to phone that character anymore to get that conversation. So be sure to call the characters often!
    
    You can find much more explanation on this feature and more in the wiki.
    
    It was nice talking with you! Have a great day~
    
    """                       
    
    jump phone_end
    
## This is the chatroom you play through if this chatroom has expired
label example_chat_expired():
    # This sets up a very specific phone call which will never expire
    # In general you should never add phone calls this way
    $ available_calls.append(PhoneCall(r, 'test_call', 'outgoing', 'test'))   
    call hack 
    call chat_begin("hack") 
    call play_music(mystic_chat)
    call enter(u) 
    u "Oh, [name]'s not here." 
    u "It looks like you let this chatroom expire, huh?" 
    u "When you're running the game in real-time, sometimes chatrooms will expire." 
    u "You can always buy them back, though, by clicking the icon next to the expired chatroom." 
    u "It doesn't even cost anything!"   (bounce=True)
    u "{=ser1}You can also use the \"Continue...\" button at the bottom of the timeline screen,{/=ser1}" 
    u "{=ser1}which lets you buy the next 24 hours of chatrooms in advance.{/=ser1}" 
    u "That way you can be sure you're not missing any chatrooms!" 
    u "{=curly}(Or if you're just tired of waiting...){/=curly}" 
    u "{=ser1}You can switch real-time mode off from the Developer settings on the chat home screen.{/=ser1}" 
    u "Anyway, you'll need to buy this chatroom back to go through the tutorial!" 
    u "Give it a shot ^^" 
    u "I'll see you soon!" 
    call exit(u)
    jump chat_end
    
menu bubbles:
    "Small bubbles":
        $ shuffle = False
        jump small_bubbles
    "Medium bubbles":
        $ shuffle = False
        jump medium_bubbles
    "Large bubbles":
        $ shuffle = False
        jump large_bubbles
    "Done":
        ju "{=ser1}That's all from us.{/=ser1}"
        ju "{=ser1}Note that currently you can only use the bubbles associated with the speaking character{/=ser1}"
        ju "{=ser1}For example, Assistant Kang cannot use my Elizabeth the 3rd bubble.{/=ser1}" (bounce=True, specBubble="cloud_l")
        ju "{=sser2}I must excuse myself.{/=sser2}"
        call exit(ju) 
        ja "{=ser1}I'll be leaving too. Best of luck with the program.{/=ser1}"
        call exit(ja) 
        call answer 
        $ shuffle = "last"
        jump learn
        
menu small_bubbles:
    "cloud_s":
        jump cloud_s
    "sigh_s":
        jump sigh_s    
    "round_s":
        jump round_s
    "square_s":
        jump square_s
    "spike_s":
        jump spike_s
        
menu medium_bubbles:
    "cloud_m":
        jump cloud_m
    "sigh_m":
        jump sigh_m    
    "round_m":
        jump round_m
    "square_m":
        jump square_m
    "spike_m":
        jump spike_m
        
menu large_bubbles:
    "cloud_l":
        jump cloud_l
    "sigh_l":
        jump sigh_l    
    "round_l":
        jump round_l
    "square_l":
        jump square_l
    "spike_l":
        jump spike_l
        
        
label jaehee_emoji():
    ja "{image=jaehee_angry}" (img=True)
    ja "{image=jaehee_happy}" (img=True)
    ja "{image=jaehee_hehe}" (img=True)
    ja "{image=jaehee_huff}" (img=True)
    ja "{image=jaehee_oops}" (img=True)
    ja "{image=jaehee_question}" (img=True)
    ja "{image=jaehee_sad}" (img=True)
    ja "{image=jaehee_well}" (img=True)
    ja "{image=jaehee_wow}" (img=True)
    call answer 
    $ shuffle = False
    jump emoji


label jumin_emoji():
    ju "{image=jumin_angry}" (img=True)
    ju "{image=jumin_sad}" (img=True)
    ju "{image=jumin_smile}" (img=True)
    ju "{image=jumin_well}" (img=True)
    call answer 
    $ shuffle = False
    jump emoji


label ray_emoji():
    r "{image=ray_cry}" (img=True)
    r "{image=ray_happy}" (img=True)
    r "{image=ray_huff}" (img=True)
    r "{image=ray_question}" (img=True)
    r "{image=ray_smile}" (img=True)
    r "{image=ray_well}" (img=True)
    r "{image=ray_wink}" (img=True)
    call answer 
    $ shuffle = False
    jump emoji

label saeran2_emoji():
    s "These saeran_sweater emotes were edited by {b}Manami{/b} from saeran-sexual.tumblr.com, used with permission."
    r "{image=saeran2_cry}" (img=True)
    r "{image=saeran2_happy}" (img=True)
    r "{image=saeran2_huff}" (img=True)
    r "{image=saeran2_question}" (img=True)
    r "{image=saeran2_smile}" (img=True)
    r "{image=saeran2_well}" (img=True)
    r "{image=saeran2_wink}" (img=True)
    call answer
    $ shuffle = False 
    jump emoji

label saeran_emoji():
    sa "{image=saeran_expecting}" (img=True)
    sa "{image=saeran_happy}" (img=True)
    sa "{image=saeran_well}" (img=True)
    sa "{image=saeran_questioning}" (img=True)
    call answer 
    $ shuffle = False
    jump emoji


label seven_emoji():
    s "{image=seven_cry}" (img=True)
    s "{image=seven_huff}" (img=True)
    s "{image=seven_khee}" (img=True)
    s "{image=seven_love}" (img=True)
    s "{image=seven_question}" (img=True)
    s "{image=seven_what}" (img=True)
    s "{image=seven_wow}" (img=True)
    s "{image=seven_yahoo}" (img=True)
    s "{image=seven_yoohoo}" (img=True)
    call answer 
    $ shuffle = False
    jump emoji

label rika_emoji():
    s "These rika_emotes were created by {b}Sakekobomb{/b} on Tumblr, used with permission."
    ri "{image=rika_happy}" (img=True)
    ri "{image=rika_cry}" (img=True)
    ri "{image=rika_pout}" (img=True)
    call answer 
    $ shuffle = False
    jump emoji

label v_emoji():
    v "{image=v_shock}" (img=True)
    v "{image=v_smile}" (img=True)
    v "{image=v_well}" (img=True)
    v "{image=v_wink}" (img=True)
    call answer 
    $ shuffle = False
    jump emoji

label yoosung_emoji():
    y "{image=yoosung_angry}" (img=True)
    y "{image=yoosung_cry}" (img=True)
    y "{image=yoosung_happy}" (img=True)
    y "{image=yoosung_huff}" (img=True)
    y "{image=yoosung_puff}" (img=True)
    y "{image=yoosung_question}" (img=True)
    y "{image=yoosung_thankyou}" (img=True)
    y "{image=yoosung_what}" (img=True)
    y "{image=yoosung_wow}" (img=True)
    y "{image=yoosung_yahoo}" (img=True)
    call answer 
    $ shuffle = False
    jump emoji

label zen_emoji():
    z "{image=zen_angry}" (img=True)
    z "{image=zen_happy}" (img=True)
    z "{image=zen_hmm}" (img=True)
    z "{image=zen_oyeah}" (img=True)
    z "{image=zen_question}" (img=True)
    z "{image=zen_sad}" (img=True)
    z "{image=zen_shock}" (img=True)
    z "{image=zen_well}" (img=True)
    z "{image=zen_wink}" (img=True)
    call answer 
    $ shuffle = False
    jump emoji
        
## SMALL BUBBLES
label cloud_s():
    
    z "Some small text" (pauseVal=0.35, bounce=True, specBubble="cloud_s")
    ju "Some small text" (pauseVal=0.35, bounce=True, specBubble="cloud_s")
    ja "Some small text" (pauseVal=0.35, bounce=True, specBubble="cloud_s")
    s "Some small text" (pauseVal=0.35, bounce=True, specBubble="cloud_s")
    r "Some small text" (pauseVal=0.35, bounce=True, specBubble="cloud_s")
    sa "Some small text" (pauseVal=0.35, bounce=True, specBubble="cloud_s")
    v "Some small text" (pauseVal=0.35, bounce=True, specBubble="cloud_s")
    y "Some small text" (pauseVal=0.35, bounce=True, specBubble="cloud_s")
    
    call answer 
    $ shuffle = False
    jump bubbles
    
label sigh_s():
    z "Some small text" (pauseVal=0.35, bounce=True, specBubble="sigh_s")
    ju "Some small text" (pauseVal=0.35, bounce=True, specBubble="sigh_s")
    ja "Some small text" (pauseVal=0.35, bounce=True, specBubble="sigh_s")
    s "Some small text" (pauseVal=0.35, bounce=True, specBubble="sigh_s")
    r "Some small text" (pauseVal=0.35, bounce=True, specBubble="sigh_s")
    v "Some small text" (pauseVal=0.35, bounce=True, specBubble="sigh_s")
    y "Some small text" (pauseVal=0.35, bounce=True, specBubble="sigh_s")

    call answer 
    $ shuffle = False
    jump bubbles
    
label round_s():    
    z "Some small text" (pauseVal=0.35, bounce=True, specBubble="flower_s")
    ju "Some small text" (pauseVal=0.35, bounce=True, specBubble="round_s")
    ja "Some small text" (pauseVal=0.35, bounce=True, specBubble="round_s")
    s "Some small text" (pauseVal=0.35, bounce=True, specBubble="round_s")
    r "Some small text" (pauseVal=0.35, bounce=True, specBubble="flower_s")
    s "Some small text" (pauseVal=0.35, bounce=True, specBubble="round2_s")
    v "Some small text" (pauseVal=0.35, bounce=True, specBubble="round_s")
    y "Some small text" (pauseVal=0.35, bounce=True, specBubble="round_s")

    call answer 
    $ shuffle = False
    jump bubbles
    
label square_s():  
    z "Some small text" (pauseVal=0.35, bounce=True, specBubble="square_s")
    ju "Some small text" (pauseVal=0.35, bounce=True, specBubble="square_s")
    ja "Some small text" (pauseVal=0.35, bounce=True, specBubble="square_s")
    r "Some small text" (pauseVal=0.35, bounce=True, specBubble="square2_s")
    r "Some small text" (pauseVal=0.35, bounce=True, specBubble="square_s")
    sa "Some small text" (pauseVal=0.35, bounce=True, specBubble="square_s")
    v "Some small text" (pauseVal=0.35, bounce=True, specBubble="square_s")
    y "Some small text" (pauseVal=0.35, bounce=True, specBubble="square_s")
    
    call answer 
    $ shuffle = False
    jump bubbles
    
label spike_s():  
    z "Some small text" (pauseVal=0.35, bounce=True, specBubble="spike_s")
    ju "Some small text" (pauseVal=0.35, bounce=True, specBubble="spike_s")
    ja "Some small text" (pauseVal=0.35, bounce=True, specBubble="spike_s")
    s "Some small text" (pauseVal=0.35, bounce=True, specBubble="spike_s")
    y "Some small text" (pauseVal=0.35, bounce=True, specBubble="spike_s")
    call answer 
    $ shuffle = False
    jump bubbles
    
## MEDIUM BUBBLES
    
label cloud_m():
    
    z "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="cloud_m")
    ju "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="cloud_m")
    ja "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="cloud_m")
    s "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="cloud_m")
    r "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="cloud_m")
    sa "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="cloud_m")
    v "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="cloud_m")
    y "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="cloud_m")
    
    call answer 
    $ shuffle = False
    jump bubbles
    
label sigh_m():
    z "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="sigh_m")
    ju "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="sigh_m")
    ja "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="sigh_m")
    s "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="sigh_m")
    r "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="sigh_m")
    v "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="sigh_m")
    y "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="sigh_m")

    call answer 
    $ shuffle = False
    jump bubbles
    
label round_m():    
    z "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="flower_m")
    ju "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="round_m")
    ja "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="round_m")
    s "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="round_m")
    r "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="flower_m")
    s "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="round2_m")
    v "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="round_m")
    y "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="round_m")

    call answer 
    $ shuffle = False
    jump bubbles
    
label square_m():  
    z "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="square_m")
    ju "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="square_m")
    ja "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="square_m")
    r "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="square2_m")
    r "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="square_m")
    sa "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="square_m")
    v "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="square_m")
    y "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="square_m")
    
    call answer 
    $ shuffle = False
    jump bubbles
    
label spike_m():  
    z "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="spike_m")
    ju "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="spike_m")
    ja "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="spike_m")
    s "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="spike_m")
    y "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="spike_m")
    call answer 
    $ shuffle = False
    jump bubbles

    
## LARGE BUBBLES
label cloud_l():
    
    z "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="cloud_l")
    ju "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="cloud_l")
    ja "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="cloud_l")
    s "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="cloud_l")
    r "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="cloud_l")
    sa "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="cloud_l")
    v "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="cloud_l")
    y "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="cloud_l")
    
    call answer 
    $ shuffle = False
    jump bubbles
    
label sigh_l():
    z "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="sigh_l")
    ju "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="sigh_l")
    ja "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="sigh_l")
    s "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="sigh_l")
    r "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="sigh_l")
    v "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="sigh_l")
    y "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="sigh_l")

    call answer 
    $ shuffle = False
    jump bubbles
    
label round_l():    
    z "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="flower_l")
    ju "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="round_l")
    ja "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="round_l")
    s "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="round_l")
    r "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="flower_l")
    s "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="round2_l")
    v "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="round_l")
    y "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="round_l")

    call answer 
    $ shuffle = False
    jump bubbles
    
label square_l():  
    z "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="square_l")
    ju "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="square_l")
    ja "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="square_l")
    r "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="square2_l")
    r "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="square_l")
    sa "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="square_l")
    v "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="square_l")
    y "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="square_l")
    
    call answer 
    $ shuffle = False
    jump bubbles
    
label spike_l():  
    z "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="spike_l")
    ju "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="spike_l")
    ja "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="spike_l")
    s "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="spike_l")
    y "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="spike_l")
    call answer 
    $ shuffle = False
    jump bubbles
    
    
