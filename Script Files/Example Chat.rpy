label example_chat:

    $ first_choice = True
    $ choice_picked = None
    
    call hack      
    call chat_begin("hack")
    
    play music mystic_chat loop
    msg "Unknown has entered the chatroom" 
    u "{=curly}Hello, [name] ^^{/=curly}" 
    u "I thought you might come by." 
    u "{=curly}You want to learn more about how to make a chatroom, right?{/=curly}" (bounce=True)
    u "I've come to show off a few of its features." 
    
    call answer
    menu:
        "Let's get started!":
            m "Let's get started!" (pauseVal=0)
            u "Great! That's the kind of attitude I'm looking for ^^" 
        
        "What if I don't know any coding?":
            m "What if I don't know any coding?" (pauseVal=0)
            u "Don't worry! I've tried to make this as easy to use as possible." 
            u "You can always ask me questions on my blog, {a=http://www.zentherainbowunicorn.tumblr.com}which you can find here{/a}" 
            u "{=sser1}This project was coded in Ren'Py, so you can always check out their forums, too.{/=sser1}" 

    u "{=sser1}Anyway, you can see what we just did there was a menu!{/=sser1}" 
    u "{=sser1}It allows you to alter a conversation based on responses.{/=sser1}" 
    u "{=sser1}If you take a look Example Chat.rpy, you can get an idea of how to use them.{/=sser1}" 
    u "{=sser1}You'll want to type \"call answer\" before a menu.{/=sser1}" 
    u "{=sser1}That way the answer button will show up at the bottom of the screen instead of immediately jumping to a menu.{/=sser1}" 
    u "{=ser1}There are lots of things to learn about!{/=ser1}" 
    u "{=ser1b}What would you like to see first?{/=ser1b}" 
       
    call answer
    menu learn:    
    
        "Emojis and Images" if not choice_picked == "emojis":
            $ choice_picked = "emojis"
            if first_choice:
                m "I want to learn how to use emojis and images" (pauseVal=0) 
                $ first_choice = False
                u "{=ser1}Emojis and images, huh?{/=ser1}"
                u "{=ser1}Okay. I'll let someone else explain this.{/=ser1}"
                u "{=sser1}I'll be back later ^^{/=sser1}"
                msg "Unknown has left the chatroom"
            $ addchat("answer","",pv*0.5)   
            jump emojis
            
        "Banners" if not choice_picked == "banners":
            $ choice_picked = "banners"
            if first_choice:
                m "Can you teach me about banners?" (pauseVal=0) 
                $ first_choice = False
                u "{=ser1}Oh, banners?{/=ser1}"
                u "{=ser1}Okay. I'll let someone else explain this.{/=ser1}"
                u "{=sser1}I'll be back later ^^{/=sser1}"
                msg "Unknown has left the chatroom"
            $ addchat("answer","",pv*0.5)
            jump banners
            
        "Heart Icons" if not choice_picked == "heart icons":
            $ choice_picked = "heart icons"
            if first_choice:
                m "I'd like to learn about heart icons" (pauseVal=0) 
                $ first_choice = False
                u "{=curly}Heart icons?{/=curly}" (bounce=True)
                u "{=ser1}Hmm, sounds good. I'll let someone else explain this.{/=ser1}"
                u "{=sser1}I'll be back later ^^{/=sser1}" (bounce=True)
                msg "Unknown has left the chatroom"
            $ addchat("answer","",pv*0.5)
            jump heart_icons
            
        "Screen Shake and Special Bubbles" if not choice_picked == "spec bubbles":
            $ choice_picked = "spec bubbles"
            if first_choice:
                m "Screen shake and special bubbles, please" (pauseVal=0) 
                $ first_choice = False
                u "{=ser1}You want to know about special speech bubbles and screen shake?{/=ser1}" (bounce=True)
                u "{=ser1}Alright then. I'll let someone else explain this.{/=ser1}"
                u "{=sser1}I'll be back later ^^{/=sser1}" (bounce=True)
                msg "Unknown has left the chatroom"
            $ addchat("answer","",pv*0.5)
            jump screen_shake
            
        "I'm done for now" if not first_choice:
            jump ending
            
label emojis:

    call hack
    call chat_begin("morning",False,False)
    
    play music geniusly_hacked_bebop loop
    msg "707 has entered the chatroom"
    s "{=sser1}O{/=sser1}" (pauseVal=0.1)
    s "{=sser1}M{/=sser1}" (pauseVal=0.1)
    s "{=sser1}G{/=sser1}" (pauseVal=0.1)
    s "{size=+10}I get to explain emojis!!!{/size}"
    s "{image=seven wow}" (img=True)
    s "{size=+10}Yay!!!{/size}" (bounce=True, specBubble="spike_m")
    s "{=sser1}Okay so what you wanna do is go find the right emoji in the emojis.rpy file.{/=sser1}"
    s "{=sser1}Then you're gonna type {{image=seven wow} or whatever the emoji name is into the Dialogue part of the Script Generator spreadsheet{/=sser1}"
    s "{=sser1}The program will automatically add the right sound file for you ^^{/=sser1}"
    s "{=ser1b}You'll also want to tick the \"Image\" modifier in the spreadsheet{/=ser1b}"
    s "{=blocky}otherwise it'll look like this lolol{/=blocky}"
    s "{image=seven wow}"
    s "Which is probably not what you want!"
    s "You'll have to be careful to get the spelling right,"
    s "{=sser1}since otherwise you'll get an \"image not found\" message.{/=sser1}"
    s "{=blocky}And it won't play any sound files, either!{/=blocky}" (bounce=True)
    s "{=ser1}If you want to add more emojis,{/=ser1}"
    s "{=ser1}just follow the rules you see in emojis.rpy{/=ser1}"
    s "{=ser1}You'll need to add it to the emoji_lookup dictionary list as well.{/=ser1}"
    s "{=ser1xb}Just use the existing entries as a guide.{/=ser1xb}"
    s "{=curly}Now I'll let you check out the emojis currently coded into the game.{/=curly}"
    s "Just select a character to see the available emojis or \"Done\" if you're finished" (bounce=True)
   
    
    call answer
    menu emoji:
        "Jaehee":
            jump jaehee_emoji
        "Jumin":
            jump jumin_emoji
        "Ray":
            jump ray_emoji
        "Saeran":
            jump saeran_emoji
        "Next ->":
            jump emoji2

            
    menu emoji2:
        "<- Back":
            jump emoji
        "Saeran (sweater)":
            jump saeran2_emoji
        "Seven":
            jump seven_emoji
        "V":
            jump v_emoji
        "Next ->":
            jump emoji3
            
    menu emoji3:
        "<- Back":
            jump emoji2
        "Rika":
            jump rika_emoji
        "Yoosung":
            jump yoosung_emoji
        "Zen":
            jump zen_emoji
        "Done":
            s "The last thing I'm here to explain is how to post CGs."
            s "{=curly}That means images like this!{/=curly}" (bounce=True)
            s "seven_cg1" (img=True)
            s "{=sser1b}They're fully clickable like they are in-game; check it out!{/=sser1b}"
            s "You post these a little differently from emojis. "
            s "{=ser1}You'll need to start by defining an image in variables.rpy{/=ser1}"
            s "{=ser1}For example, that last image is called \"seven_cg1\"{/=ser1}"
            s "{=ser1}It should be 750x1334 pixels, and it will be automatically resized for the chatroom.{/=ser1}"
            s "{=ser1}Then to call it, just type the name of the image you defined and check off the \"Image\" modifier in the spreadsheet.{/=ser1}"
            s "{=blocky}If you don't, it'll just show up in text, like this:{/=blocky}"
            s "seven_cg1"
            s "But if you check off the \"Image\" modifier, you get this:" (bounce=True, specBubble="round2_m")
            s "seven_cg1" (img=True)
            s "The ability to click the image/the full screen version is automatically taken care of for you."
            s "{=curly}Hope this helped!{/=curly}" (bounce=True, specBubble="round_m")
            s "{=sser1}Let me know if you have any questions later~{/=sser1}"
            msg "707 has left the chatroom"
            call answer
            jump learn


label banners:

    call hack
    call chat_begin("noon",False,False)
    play music same_old_fresh_air loop
    
    msg "Yoosung★ has entered the chatroom"
    y "{=curly}Hello!{/=curly}"
    y "I'm supposed to explain banners to you."
    y "It's pretty quick, I promise!"
    y "{image=yoosung yahoo}" (img=True)
    y "There are four different types of banners:"
    y "{=sser1}The lightning banner!{/=sser1}" (bounce=True)
    call banner_lightning
    y "For when you're feeling angry ^^;;"
    y "{=sser1}The heart banner!{/=sser1}" (bounce=True)
    call banner_heart
    y "{=sser1}For happy stuff!{/=sser1}"
    y "{=sser1}The annoy banner{/=sser1}" (bounce=True)
    call banner_annoy
    y "For when you're irritated"
    y "And last but not least, "
    y "{=ser1}the 'well' banner!{/=ser1}" (bounce=True)
    call banner_well
    y "{=ser1}...{/=ser1}"
    y "It's for times when you're a little lost for words."
    y "{=sser1}That's all from me!{/=sser1}"
    y "Good luck with the program ^^"
    y "{image=yoosung wow}" (img=True)
    msg "Yoosung★ has left the chatroom"

    call answer
    jump learn
    
label heart_icons:

    call hack
    call chat_begin("evening",False,False)
    play music narcissistic_jazz loop
    
    msg "Zen has entered the chatroom"
    z "{image=zen wink}" (img=True)
    z "{=curly}Hey cutie ^^{/=curly}" (bounce=True)
    z "I'm here to explain heart icons!"
    z "{=sser2}They look like this:{/=sser2}"
    call heart_icon('z')
    z "{=sser2}And each character has a different one{/=sser2}"
    z "{=sser1b}They all use the same white heart, this one{/=sser1b}"
    call heart_icon('u')
    z "{=sser1}and just recolour it depending on what argument you pass via \"call heart_icon('z')\"{/=sser1}"
    z "{=sser1}You can easily add your own colours, too, by adding the character and colour to the heartcolour list in MysMe Screen Effects.rpy{/=sser1}"
    z "{=blocky}Here are the currently available colours:{/=blocky}"
    z "{=sser1}Seven{/=sser1}"
    call heart_icon('s')
    z "{=curly}Me!{/=curly}"
    call heart_icon('z')
    z "{=sser1}Jaehee{/=sser1}"
    call heart_icon('ja')
    z "{=sser1}Jumin{/=sser1}"
    call heart_icon('ju')
    z "{=sser1}Yoosung{/=sser1}"
    call heart_icon('y')
    z "{=sser1}Ray{/=sser1}"
    call heart_icon('ra')
    z "{=sser1}V{/=sser1}"
    call heart_icon('v')
    z "{=ser1}and then there are a few special ones{/=ser1}"
    z "{=sser1}The white heart I mentioned before (tied to the username 'Unknown'){/=sser1}"
    call heart_icon('u')
    z "{=sser1}You can also get this heart by passing heart_icon the short form for Saeran (sa or \"Sae\"){/=sser1}"
    call heart_icon('sa')
    z "And then there is this heart"
    call heart_icon('r')
    z "which is for Rika, but isn't found in-game"
    z "{=sser1}The last thing I'm here to explain is the 'heartbreak' icon{/=sser1}"
    z "{=sser1}It works the same as the regular heart icons -- just add a colour to the heartcolour list and call \"heart_break\" with that character{/=sser1}"
    z "{=ser1}It will automatically colour itself{/=ser1}"
    z "They look like this!"
    call heart_break('z')
    z "But you don't really want to hurt any of our feelings, right?" (bounce=True)
    z "{image=zen happy}" (img=True)
    call heart_icon('z')
    z "{=ser1}The program automatically tallies the heart points you've earned during a chatroom and displays the total after you hit Save&Exit.{/=ser1}"
    z "{=sser1}It keeps track of both the total points earned during a chatroom,{/=sser1}"
    z "{=sser1}as well as how many points you have with each individual character{/=sser1}"
    z "{=curly}Just to keep the door open for other uses ^^{/=curly}" (bounce=True, specBubble="round_m")
    z "{=blocky}Also note that Ray and Saeran's heart points count towards the same character{/=blocky}"
    z "{=curly}Good luck with the rest of the program!{/=curly}" (bounce=True)
    msg "Zen has left the chatroom"
    
    call answer
    jump learn
    
label screen_shake:
    
    call hack
    call chat_begin("night",False,False)
    play music lonesome_practicalism loop

    msg "Jaehee Kang has entered the chatroom"
    ja "{=ser1}Hello, [name].{/=ser1}"
    ja "{=ser1}Mr. Han will be with us shortly. {/=ser1}"
    msg "Jumin Han has entered the chatroom"
    ja "{=curly}Ah, right on time.{/=curly}" (bounce=True, specBubble="cloud_s")
    ja "{=ser1}Shall we get started then?{/=ser1}"
    ja "{=ser1}...{/=ser1}"
    call banner_well
    ja "{=ser1}Mr. Han?{/=ser1}"
    ja "{image=jaehee well}" (img=True)
    ja "{=sser1}Mr. Han.{/=sser1}"
    ja "{=sser1}{size=+10}MR. HAN!!{/size}{/=sser1}" (bounce=True, specBubble="spike_m")
    show night at shake
    ju "{=curly}Is something the matter?{/=curly}" (bounce=True, specBubble="cloud_m")
    ja "{=sser1}Oh.{/=sser1}" (bounce=True, specBubble="sigh_s")
    ja "{=ser1}You weren't responding so I thought perhaps you were asleep.{/=ser1}"
    ju "{=sser1}Elizabeth the 3rd was sleeping on my lap so I couldn't disturb her.{/=sser1}" (bounce=True, specBubble="cloud_l")
    ja "Of course;;" (bounce=True, specBubble="sigh_m")
    ja "{=ser1}...As I was saying.{/=ser1}"
    ja "We're supposed to teach [name] about some other chatroom features." (bounce=True)
    ju "{=ser1}Like the special speech bubbles?{/=ser1}" (bounce=True, specBubble="square_m")
    ja "Yes ^^" (bounce=True, specBubble="cloud_s")
    ja "{=sser1}In the Script Generator spreadsheet, you'll see an option called \"special bubble\"{/=sser1}"
    ja "{=sser1}You can look in the folder \"Bubbles/Special\" and find the correct bubble{/=sser1}"
    ja "Most bubbles come in three sizes:" (bounce=True)
    ja "{=sser1b}small{/=sser1b}"
    ja "{=sser1b}medium{/=sser1b}"
    ja "{=sser1b}and large{/=sser1b}"
    ja "{=ser1}The text should usually resize itself to fit, but it might be finicky sometimes, since most bubbles have to be adjusted individually{/=ser1}"
    ja "{color=#f00}For example, this bubble might be too small.{/color}" (bounce=True, specBubble="cloud_s")
    ja "{=ser1}As for screen shake,{/=ser1}"
    ja "{=ser1}how you use it depends on which background you're using{/=ser1}"
    ja "{=ser1xb}For example, this is the \"night\" background{/=ser1xb}"
    ja "{=sser1}So we call \"show night at shake\"{/=sser1}"
    ja "And it does this" (bounce=True)
    show night at shake
    ja "{=ser1}Lastly, you can check out all of the special bubbles present in the game.{/=ser1}"
    ja "{=ser1xb}Just select \"Done\" when you're finished.{/=ser1xb}"
    call answer
    jump bubbles
    

label ending:
    call hack
    call chat_begin("hack",False,False)
    
    play music mystic_chat loop
    
    msg "Unknown has entered the chatroom"
    u "{=curly}You're back!{/=curly}" (bounce=True)
    u "So what did you think?"
    u "Are you ready to start making your own chatrooms?"
    call answer
    menu:
        "Definitely!":
            m "Definitely!" (pauseVal=0)
            u "I'm glad! ^^"
                    
        "I don't know if I'm ready yet...":
            m "I don't know if I'm ready yet..." (pauseVal=0)
            u "{=ser1}I recommend reading through the code for this chatroom and the coffee chatroom.{/=ser1}"
            u "{=ser1}And maybe go through this example chatroom a few times and compare it with the code!{/=ser1}"

    u "{=sser1}I've put a lot of work into this program, so any feedback is welcome!{/=sser1}"
    u "And please credit me if you do use it somewhere!"
    u "I hope you find this program helpful."
    u "Good luck!"
    msg "Unknown has left the chatroom"
    # Call this at the end of a chatroom
    call save_exit

    

menu bubbles:
    "Small bubbles":
        jump small_bubbles
    "Medium bubbles":
        jump medium_bubbles
    "Large bubbles":
        jump large_bubbles
    "Done":
        ju "{=ser1}That's all from us.{/=ser1}"
        ju "{=ser1}Note that currently you can only use the bubbles associated with the speaking character{/=ser1}"
        ju "{=ser1}For example, Assistant Kang cannot use my Elizabeth the 3rd bubble.{/=ser1}" (bounce=True, specBubble="cloud_l")
        ju "I must excuse myself."
        msg "Jumin Han has left the chatroom"
        ja "{=ser1}I'll be leaving too. Best of luck with the program.{/=ser1}"
        msg "Jaehee Kang has left the chatroom"
        call answer
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
        
        
label jaehee_emoji:
    ja "{image=jaehee angry}" (img=True)
    ja "{image=jaehee happy}" (img=True)
    ja "{image=jaehee hehe}" (img=True)
    ja "{image=jaehee huff}" (img=True)
    ja "{image=jaehee oops}" (img=True)
    ja "{image=jaehee question}" (img=True)
    ja "{image=jaehee sad}" (img=True)
    ja "{image=jaehee well}" (img=True)
    ja "{image=jaehee wow}" (img=True)
    call answer
    jump emoji


label jumin_emoji:
    ju "{image=jumin angry}" (img=True)
    ju "{image=jumin sad}" (img=True)
    ju "{image=jumin smile}" (img=True)
    ju "{image=jumin well}" (img=True)
    call answer
    jump emoji


label ray_emoji:
    ra "{image=ray cry}" (img=True)
    ra "{image=ray happy}" (img=True)
    ra "{image=ray huff}" (img=True)
    ra "{image=ray question}" (img=True)
    ra "{image=ray smile}" (img=True)
    ra "{image=ray well}" (img=True)
    ra "{image=ray wink}" (img=True)
    call answer
    jump emoji

label saeran2_emoji:
    ra "{image=saeran2 cry}" (img=True)
    ra "{image=saeran2 happy}" (img=True)
    ra "{image=saeran2 huff}" (img=True)
    ra "{image=saeran2 question}" (img=True)
    ra "{image=saeran2 smile}" (img=True)
    ra "{image=saeran2 well}" (img=True)
    ra "{image=saeran2 wink}" (img=True)
    call answer
    jump emoji

label saeran_emoji:
    sa "{image=saeran expecting}" (img=True)
    sa "{image=saeran happy}" (img=True)
    sa "{image=saeran well}" (img=True)
    sa "{image=saeran questioning}" (img=True)
    call answer
    jump emoji


label seven_emoji:
    s "{image=seven cry}" (img=True)
    s "{image=seven huff}" (img=True)
    s "{image=seven khee}" (img=True)
    s "{image=seven love}" (img=True)
    s "{image=seven question}" (img=True)
    s "{image=seven what}" (img=True)
    s "{image=seven wow}" (img=True)
    s "{image=seven yahoo}" (img=True)
    s "{image=seven yoohoo}" (img=True)
    call answer
    jump emoji

label rika_emoji:
    r "{image=rika happy}" (img=True)
    r "{image=rika cry}" (img=True)
    r "{image=rika pout}" (img=True)
    call answer
    jump emoji

label v_emoji:
    v "{image=v shock}" (img=True)
    v "{image=v smile}" (img=True)
    v "{image=v well}" (img=True)
    v "{image=v wink}" (img=True)
    call answer
    jump emoji

label yoosung_emoji:
    y "{image=yoosung angry}" (img=True)
    y "{image=yoosung cry}" (img=True)
    y "{image=yoosung happy}" (img=True)
    y "{image=yoosung huff}" (img=True)
    y "{image=yoosung puff}" (img=True)
    y "{image=yoosung question}" (img=True)
    y "{image=yoosung thankyou}" (img=True)
    y "{image=yoosung what}" (img=True)
    y "{image=yoosung wow}" (img=True)
    y "{image=yoosung yahoo}" (img=True)
    call answer
    jump emoji

label zen_emoji:
    z "{image=zen angry}" (img=True)
    z "{image=zen happy}" (img=True)
    z "{image=zen hmm}" (img=True)
    z "{image=zen oyeah}" (img=True)
    z "{image=zen question}" (img=True)
    z "{image=zen sad}" (img=True)
    z "{image=zen shock}" (img=True)
    z "{image=zen well}" (img=True)
    z "{image=zen wink}" (img=True)
    call answer
    jump emoji
        
## SMALL BUBBLES
label cloud_s:
    
    z "Some small text" (pauseVal=0.5, bounce=True, specBubble="cloud_s")
    ju "Some small text" (pauseVal=0.5, bounce=True, specBubble="cloud_s")
    ja "Some small text" (pauseVal=0.5, bounce=True, specBubble="cloud_s")
    s "Some small text" (pauseVal=0.5, bounce=True, specBubble="cloud_s")
    ra "Some small text" (pauseVal=0.5, bounce=True, specBubble="cloud_s")
    sa "Some small text" (pauseVal=0.5, bounce=True, specBubble="cloud_s")
    v "Some small text" (pauseVal=0.5, bounce=True, specBubble="cloud_s")
    y "Some small text" (pauseVal=0.5, bounce=True, specBubble="cloud_s")
    
    call answer
    jump bubbles
    
label sigh_s:
    z "Some small text" (pauseVal=0.5, bounce=True, specBubble="sigh_s")
    ju "Some small text" (pauseVal=0.5, bounce=True, specBubble="sigh_s")
    ja "Some small text" (pauseVal=0.5, bounce=True, specBubble="sigh_s")
    s "Some small text" (pauseVal=0.5, bounce=True, specBubble="sigh_s")
    ra "Some small text" (pauseVal=0.5, bounce=True, specBubble="sigh_s")
    v "Some small text" (pauseVal=0.5, bounce=True, specBubble="sigh_s")
    y "Some small text" (pauseVal=0.5, bounce=True, specBubble="sigh_s")

    call answer
    jump bubbles
    
label round_s:    
    z "Some small text" (pauseVal=0.5, bounce=True, specBubble="round_s")
    ju "Some small text" (pauseVal=0.5, bounce=True, specBubble="round_s")
    ja "Some small text" (pauseVal=0.5, bounce=True, specBubble="round_s")
    s "Some small text" (pauseVal=0.5, bounce=True, specBubble="round_s")
    ra "Some small text" (pauseVal=0.5, bounce=True, specBubble="round_s")
    s "Some small text" (pauseVal=0.5, bounce=True, specBubble="round2_s")
    v "Some small text" (pauseVal=0.5, bounce=True, specBubble="round_s")
    y "Some small text" (pauseVal=0.5, bounce=True, specBubble="round_s")

    call answer
    jump bubbles
    
label square_s:  
    z "Some small text" (pauseVal=0.5, bounce=True, specBubble="square_s")
    ju "Some small text" (pauseVal=0.5, bounce=True, specBubble="square_s")
    ja "Some small text" (pauseVal=0.5, bounce=True, specBubble="square_s")
    ra "Some small text" (pauseVal=0.5, bounce=True, specBubble="square2_s")
    ra "Some small text" (pauseVal=0.5, bounce=True, specBubble="square_s")
    sa "Some small text" (pauseVal=0.5, bounce=True, specBubble="square_s")
    v "Some small text" (pauseVal=0.5, bounce=True, specBubble="square_s")
    y "Some small text" (pauseVal=0.5, bounce=True, specBubble="square_s")
    
    call answer
    jump bubbles
    
label spike_s:  
    z "Some small text" (pauseVal=0.5, bounce=True, specBubble="spike_s")
    ju "Some small text" (pauseVal=0.5, bounce=True, specBubble="spike_s")
    ja "Some small text" (pauseVal=0.5, bounce=True, specBubble="spike_s")
    s "Some small text" (pauseVal=0.5, bounce=True, specBubble="spike_s")
    y "Some small text" (pauseVal=0.5, bounce=True, specBubble="spike_s")
    call answer
    jump bubbles
    
## MEDIUM BUBBLES
    
label cloud_m:
    
    z "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="cloud_m")
    ju "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="cloud_m")
    ja "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="cloud_m")
    s "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="cloud_m")
    ra "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="cloud_m")
    sa "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="cloud_m")
    v "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="cloud_m")
    y "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="cloud_m")
    
    call answer
    jump bubbles
    
label sigh_m:
    z "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="sigh_m")
    ju "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="sigh_m")
    ja "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="sigh_m")
    s "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="sigh_m")
    ra "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="sigh_m")
    v "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="sigh_m")
    y "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="sigh_m")

    call answer
    jump bubbles
    
label round_m:    
    z "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="round_m")
    ju "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="round_m")
    ja "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="round_m")
    s "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="round_m")
    ra "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="round_m")
    s "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="round2_m")
    v "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="round_m")
    y "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="round_m")

    call answer
    jump bubbles
    
label square_m:  
    z "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="square_m")
    ju "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="square_m")
    ja "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="square_m")
    ra "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="square2_m")
    ra "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="square_m")
    sa "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="square_m")
    v "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="square_m")
    y "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="square_m")
    
    call answer
    jump bubbles
    
label spike_m:  
    z "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="spike_m")
    ju "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="spike_m")
    ja "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="spike_m")
    s "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="spike_m")
    y "Longer text because this is a medium-sized bubble" (pauseVal=0.35, bounce=True, specBubble="spike_m")
    call answer
    jump bubbles

    
## LARGE BUBBLES
label cloud_l:
    
    z "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="cloud_l")
    ju "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="cloud_l")
    ja "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="cloud_l")
    s "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="cloud_l")
    ra "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="cloud_l")
    sa "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="cloud_l")
    v "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="cloud_l")
    y "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="cloud_l")
    
    call answer
    jump bubbles
    
label sigh_l:
    z "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="sigh_l")
    ju "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="sigh_l")
    ja "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="sigh_l")
    s "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="sigh_l")
    ra "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="sigh_l")
    v "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="sigh_l")
    y "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="sigh_l")

    call answer
    jump bubbles
    
label round_l:    
    z "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="round_l")
    ju "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="round_l")
    ja "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="round_l")
    s "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="round_l")
    ra "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="round_l")
    s "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="round2_l")
    v "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="round_l")
    y "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="round_l")

    call answer
    jump bubbles
    
label square_l:  
    z "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="square_l")
    ju "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="square_l")
    ja "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="square_l")
    ra "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="square2_l")
    ra "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="square_l")
    sa "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="square_l")
    v "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="square_l")
    y "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="square_l")
    
    call answer
    jump bubbles
    
label spike_l:  
    z "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="spike_l")
    ju "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="spike_l")
    ja "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="spike_l")
    s "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="spike_l")
    y "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.2, bounce=True, specBubble="spike_l")
    call answer
    jump bubbles
    
    
