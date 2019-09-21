label example_chat:

    $ first_choice = True
    $ choice_picked = None
       
    # This sets up a very specific phone call which will never expire
    # You'll generally never want to add phone calls this way
    $ available_calls.append(Phone_Call(r, 'test_call', 'outgoing', 'test'))
       
    call hack 
    call chat_begin("hack") 
        
    play music mystic_chat loop
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
            u "{=sser2}There's an extensive {b}User Guide{/b} included with the program to look at,{/=sser2}"
            u "{=sser2}and I'll also be monitoring the{a=https://discord.gg/BPbPcpk} Mysterious Messenger Discord server{/a} if you have questions.{/=sser2}" 
            u "This project was coded in Ren'Py, so you can always check out their forums, too." 

    u "Anyway, you can see what we just did there was a menu!" 
    u "It allows you to alter a conversation based on responses." 
    u "If you take a look {b}Example Chat.rpy{/b}, you can get an idea of how to use them." 
    u "You'll want to type \"call answer\" before a menu." 
    u "That way the answer button will show up at the bottom of the screen instead of immediately jumping to a menu." 
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
            
label emojis:

    call hack 
    call chat_begin("morning",False,False) 
    
    play music geniusly_hacked_bebop loop
    call enter(s) 
    s "O" (pauseVal=0.1)
    s "M" (pauseVal=0.1)
    s "G" (pauseVal=0.1)
    s "{=sser2}{size=+10}I get to explain emojis!!!{/size}{/=sser2}" 
    s "{image=seven wow}"   (img=True)
    s "{=sser2}{size=+10}Yay!!!{/size}{/=sser2}"   (bounce=True, specBubble="spike_m")
    s "Okay, so what you wanna do is go find the right emoji in the {b}images/Gifs{/b} folder,"
    s "and find its corresponding name in the {b}emojis.rpy{/b} file."
    s "Then you're gonna type {{image=seven wow} or whatever the emoji name is into the Dialogue part of the Script Generator spreadsheet"
    s "The program will automatically add the right sound file for you ^^"
    s "{=ser1b}You'll also want to make sure the \"Image\" modifier in the spreadsheet is checked,{/=ser1b}"
    s "{=blocky}otherwise it'll look like this lolol{/=blocky}"
    s "{image=seven wow}"
    s "{=sser2}Which is probably not what you want!{/=sser2}" 
    s "{=sser2}You'll have to be careful to get the spelling right,{/=sser2}" 
    s "since otherwise you'll get an \"image not found\" message."
    s "{=blocky}And it won't play any sound files, either!{/=blocky}" (bounce=True)
    s "{=ser1}If you want to add more emojis,{/=ser1}"
    s "{=ser1}there's a whole section on just that in the User Guide.{/=ser1}"
    s "{=curly}Now I'll let you check out the emojis currently coded into the game.{/=curly}"
    s "{=sser2}Just select a character to see the available emojis or \"Done\" if you're finished{/=sser2}"   (bounce=True)

    
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
            s "{=sser2}The last thing I'm here to explain is how to post CGs.{/=sser2}" (pauseVal=0)
            s "{=curly}That means images like this!{/=curly}" (bounce=True)
            s "s/cg-1.png" (img=True)
            s "{=sser1b}They're fully clickable like they are in-game; check it out!{/=sser1b}"
            s "You can post CGs too!"
            call answer
            menu:
                "I can?":
                    m "I can?" (pauseVal=0)
                    s "Yeah! Give it a try!" 
                    m "s/cg-1.png" (img=True)                    
                "(Try posting)":
                    m "s/cg-1.png" (img=True, pauseVal=0)
            m "{image=seven wow}" (img=True)
            s "Yeah, just like that!"
            s "{=sser2}You post these a little differently from emojis. {/=sser2}" 
            s "{=ser1}You'll need to start by putting the image in the right album in the CGs folder.{/=ser1}"
            s "{=ser1}Then, you can define an Album object in {b}gallery.rpy{/b} using the file path.{/=ser1}"
            s "{=ser1}It should be in the list of the person whose gallery the image will be unlocked in.{/=ser1}"
            s "{=ser1}For example, that last image is defined under \"s_album\" as {b}Album(\"s_album/cg-1.png\"){/b}{/=ser1}"
            s "{=ser1}The CG should be 750x1334 pixels, and it will be automatically resized for the chatroom.{/=ser1}"
            s "{=ser1}Then to use it, you type in a simplified version of the path to the dialogue column,{/=ser1}"
            s "{=ser1}and check off the \"Image\" modifier in the spreadsheet.{/=ser1}"
            s "{=ser1}Simplified path just means {b}album ID/{/b} + {b}name of your cg{/b}.{/=ser1}"
            s "{=ser1}To use the example from before, we write {b}s/cg-1.png{/b} into the Dialogue column.{/=ser1}"
            s "{=blocky}If you don't also check off \"Image\", it'll just show up in text, like this:{/=blocky}"
            s "s/cg-1.png"
            s "But if you check off the \"Image\" modifier, you get this:" (bounce=True, specBubble="round2_m")
            s "s/cg-1.png" (img=True)
            s "{=sser2}The ability to click the image/the full screen version is automatically taken care of for you.{/=sser2}" 
            s "{=sser2}It'll also unlock it in the Album if it's your first time seeing the CG!{/=sser2}" 
            s "{=curly}Hope this helped!{/=curly}" (bounce=True, specBubble="round_m")
            s "Let me know if you have any questions later~"
            call exit(s) 
            call answer 
            jump learn


label banners:

    call hack 
    call chat_begin("noon",False,False) 
    play music same_old_fresh_air loop
    
    call enter(y) 
    y "{=curly}Hello!{/=curly}"
    y "{=sser2}I'm supposed to explain banners to you.{/=sser2}" 
    y "{=sser2}It's pretty quick, I promise!{/=sser2}" 
    y "{image=yoosung happy}"   (img=True)
    y "You call them with \"call banner('__')\","
    y "where '__' is the name of the banner you want."
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
    y "{image=yoosung thankyou}"   (img=True)
    y "I have one more thing I was going to show you:" 
    y "{=ser1}it's not in the base game, but in this program you can pick your pronouns.{/=ser1}" 
    y "{=curly}You said you identify as [persistent.pronoun], right?{/=curly}"   (bounce=True, specBubble="square_m")
    y "{=sser2}So we'll use pronouns like [they]/[them] whenever we talk about you.{/=sser2}"   (bounce=True)
    y "You can check out {b}Short forms/Startup Variables{/b} under {b}variables.rpy{/b} - at the start there are some variables so you know how to use pronouns when writing a script" 
    y "If you want to add any new variables, there's a section in the User Guide about doing just that."
    y "And if you ever want to change your pronouns, just go to the profile page (currently accessed from the main menu)." 
    y "That's all from me!"
    y "{=sser2}Good luck with the program ^^{/=sser2}"
    y "{image=yoosung wow}" (img=True)
    call exit(y) 

    call answer 
    jump learn
    
label heart_icons:

    call hack 
    call chat_begin("evening",False,False) 
    play music narcissistic_jazz loop
    
    call enter(z) 
    z "{image=zen wink}" (img=True)
    z "{=curly}Hey cutie ^^{/=curly}" (bounce=True)
    z "{=sser2}I'm here to explain heart icons!{/=sser2}"
    z "{=sser2}They look like this:{/=sser2}"
    call heart_icon(z) 
    z "{=sser2}And each character has a different one{/=sser2}"
    z "{=sser1b}They all use the same white heart, this one{/=sser1b}"
    call heart_icon(u) 
    z "and just recolour it depending on what argument you pass via \"call heart_icon(z)\""
    z "You can easily add your own colours, too, by adding the character and colour to the heartcolour list in MysMe Screen Effects.rpy"
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
    z "{=sser2}which is for Rika, but isn't found in-game{/=sser2}"
    z "The last thing I'm here to explain is the 'heartbreak' icon"
    z "It works the same as the regular heart icons -- just add a colour to the heartcolour list and call \"heart_break\" with that character"
    z "{=ser1}It will automatically colour itself{/=ser1}"
    z "{=sser2}They look like this!{/=sser2}"
    call heart_break(z) 
    z "{=sser2}But you don't really want to hurt any of our feelings, right?{/=sser2}" (bounce=True)
    z "{image=zen happy}" (img=True)
    call heart_icon(z) 
    z "{=ser1}The program automatically tallies the heart points you've earned during a chatroom and displays the total after you hit Save&Exit.{/=ser1}"
    z "It keeps track of both the total points earned during a chatroom,"
    z "as well as how many points you have with each individual character"
    z "There's also a second argument you can pass it to have heart points count towards a bad end."
    z "Check out the User Guide for more on that!"
    z "{=blocky}Also note that Ray and Saeran's heart points count towards the same character{/=blocky}"
    z "{=curly}Good luck with the rest of the program!{/=curly}" (bounce=True)
    call exit(z) 
    
    call answer 
    jump learn
    
label screen_shake:
    
    call hack 
    call chat_begin("night",False,False) 
    play music lonesome_practicalism loop

    call enter(ja) 
    ja "{=ser1}Hello, [name].{/=ser1}"
    ja "{=ser1}Mr. Han will be with us shortly. {/=ser1}"
    call enter(ju) 
    ja "{=curly}Ah, right on time.{/=curly}" (bounce=True, specBubble="cloud_s")
    ja "{=ser1}Shall we get started then?{/=ser1}"
    pause 1
    ja "{=ser1}...{/=ser1}"
    call banner('well') 
    ja "{=ser1}Mr. Han?{/=ser1}"
    ja "{image=jaehee well}" (img=True)
    ja "Mr. Han."
    ja "{size=+10}MR. HAN!!{/size}" (bounce=True, specBubble="spike_m")
    show night at shake
    ju "{=curly}Is something the matter?{/=curly}" (bounce=True, specBubble="cloud_m")
    ja "Oh." (bounce=True, specBubble="sigh_s")
    ja "{=ser1}You weren't responding so I thought perhaps you were asleep.{/=ser1}"
    ju "Elizabeth the 3rd was sleeping on my lap so I couldn't disturb her." (bounce=True, specBubble="cloud_l")
    ja "{=sser2}Of course;;{/=sser2}" (bounce=True, specBubble="sigh_m")
    ja "{=ser1}...As I was saying.{/=ser1}"
    ja "{=sser2}We're supposed to teach [name] about some other chatroom features.{/=sser2}" (bounce=True)
    ju "{=ser1}Like the special speech bubbles?{/=ser1}" (bounce=True, specBubble="square_m")
    ja "{=sser2}Yes ^^{/=sser2}" (bounce=True, specBubble="cloud_s")
    ja "In the Script Generator spreadsheet, you'll see an option called \"special bubble\""
    ja "You can look in the folder \"Bubbles/Special\" and find the correct bubble"
    ja "{=sser2}Most bubbles come in three sizes:{/=sser2}" (bounce=True)
    ja "{=sser1b}small{/=sser1b}" (bounce=True, specBubble="spike_s")
    ja "{=sser1b}medium{/=sser1b}" (bounce=True, specBubble="spike_m")
    ja "{=sser1b}and large{/=sser1b}" (bounce=True, specBubble="spike_l")
    ja "{=ser1}The text should usually resize itself to fit, but you need to choose the size yourself.{/=ser1}"
    ja "{color=#f00}For example, this bubble might be too small.{/color}" (bounce=True, specBubble="cloud_s")
    ja "{=ser1}As for screen shake,{/=ser1}"
    ja "{=ser1}how you use it depends on which background you're using{/=ser1}"
    ja "{=ser1xb}For example, this is the \"night\" background{/=ser1xb}"
    ja "So we call \"show night at shake\""
    ja "{=sser2}And it does this{/=sser2}" (bounce=True)
    show night at shake
    ja "{=ser1}Lastly, you can check out all of the special bubbles present in the game.{/=ser1}"
    ja "{=ser1xb}Just select \"Done\" when you're finished.{/=ser1xb}"
    call answer 
    jump bubbles
    

label ending:
    call hack 
    call chat_begin("hack",False,False) 
    play music mystic_chat loop
    
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
            u "{=ser1}I recommend checking out the User Guide, which will walk you through creating a chatroom.{/=ser1}"
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

label test_call:

    call phone_begin 
    
    r_phone "Hello?"
    
    menu:
        extend ''
        "Ray, it's me.":
            m_phone "Ray, it's me."
            r_phone "Oh! It's nice to hear from you, [name]."
            
        "Hello? Can you hear me?":
            m_phone "Hello? Can you hear me?"
            r_phone "Yes! [name], right? It's nice to hear from you."
            
    r_phone """
    
    Looks like you figured out the phone call function, huh?
    
    This is a test call for the program. It's always available on Tutorial Day.
    
    That means you'll never hear my voicemail message, but you can try calling the other characters to hear their voicemail.
    
    Usually, phone calls will timeout two chatrooms after it's first 'activated'.
    
    That means you won't be able to phone that character anymore to get that conversation. So be sure to call the characters often!
    
    You can find much more explanation on this feature and more in the User Guide.
    
    It was nice talking with you! Have a great day~
    
    """                       
    
    jump phone_end
    
## This is the chatroom you'll play through if this chatroom
## has expired
label example_chat_expired:
    # This sets up a very specific phone call which will never expire
    # You'll generally never want to add phone calls this way
    $ available_calls.append(Phone_Call(r, 'test_call', 'outgoing', 'test'))   
    call hack 
    call chat_begin("hack") 
    play music mystic_chat loop
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
    u "{=ser1}You can switch real-time mode off from the Settings screen.{/=ser1}" 
    u "Anyway, you'll need to buy this chatroom back to go through the tutorial!" 
    u "Give it a shot ^^" 
    u "I'll see you soon!" 
    call exit(u)
    jump chat_end
    
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
        ju "{=sser2}I must excuse myself.{/=sser2}"
        call exit(ju) 
        ja "{=ser1}I'll be leaving too. Best of luck with the program.{/=ser1}"
        call exit(ja) 
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
    r "{image=ray cry}" (img=True)
    r "{image=ray happy}" (img=True)
    r "{image=ray huff}" (img=True)
    r "{image=ray question}" (img=True)
    r "{image=ray smile}" (img=True)
    r "{image=ray well}" (img=True)
    r "{image=ray wink}" (img=True)
    call answer 
    jump emoji

label saeran2_emoji:
    s "These Saeran sweater emotes were edited by {b}Manami{/b} from saeran-sexual.tumblr.com, used with permission."
    r "{image=saeran2 cry}" (img=True)
    r "{image=saeran2 happy}" (img=True)
    r "{image=saeran2 huff}" (img=True)
    r "{image=saeran2 question}" (img=True)
    r "{image=saeran2 smile}" (img=True)
    r "{image=saeran2 well}" (img=True)
    r "{image=saeran2 wink}" (img=True)
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
    s "These Rika emotes were created by {b}Sakekobomb{/b} on Tumblr, used with permission."
    ri "{image=rika happy}" (img=True)
    ri "{image=rika cry}" (img=True)
    ri "{image=rika pout}" (img=True)
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
    
    z "Some small text" (pauseVal=0.35, bounce=True, specBubble="cloud_s")
    ju "Some small text" (pauseVal=0.35, bounce=True, specBubble="cloud_s")
    ja "Some small text" (pauseVal=0.35, bounce=True, specBubble="cloud_s")
    s "Some small text" (pauseVal=0.35, bounce=True, specBubble="cloud_s")
    r "Some small text" (pauseVal=0.35, bounce=True, specBubble="cloud_s")
    sa "Some small text" (pauseVal=0.35, bounce=True, specBubble="cloud_s")
    v "Some small text" (pauseVal=0.35, bounce=True, specBubble="cloud_s")
    y "Some small text" (pauseVal=0.35, bounce=True, specBubble="cloud_s")
    
    call answer 
    jump bubbles
    
label sigh_s:
    z "Some small text" (pauseVal=0.35, bounce=True, specBubble="sigh_s")
    ju "Some small text" (pauseVal=0.35, bounce=True, specBubble="sigh_s")
    ja "Some small text" (pauseVal=0.35, bounce=True, specBubble="sigh_s")
    s "Some small text" (pauseVal=0.35, bounce=True, specBubble="sigh_s")
    r "Some small text" (pauseVal=0.35, bounce=True, specBubble="sigh_s")
    v "Some small text" (pauseVal=0.35, bounce=True, specBubble="sigh_s")
    y "Some small text" (pauseVal=0.35, bounce=True, specBubble="sigh_s")

    call answer 
    jump bubbles
    
label round_s:    
    z "Some small text" (pauseVal=0.35, bounce=True, specBubble="round_s")
    ju "Some small text" (pauseVal=0.35, bounce=True, specBubble="round_s")
    ja "Some small text" (pauseVal=0.35, bounce=True, specBubble="round_s")
    s "Some small text" (pauseVal=0.35, bounce=True, specBubble="round_s")
    r "Some small text" (pauseVal=0.35, bounce=True, specBubble="round_s")
    s "Some small text" (pauseVal=0.35, bounce=True, specBubble="round2_s")
    v "Some small text" (pauseVal=0.35, bounce=True, specBubble="round_s")
    y "Some small text" (pauseVal=0.35, bounce=True, specBubble="round_s")

    call answer 
    jump bubbles
    
label square_s:  
    z "Some small text" (pauseVal=0.35, bounce=True, specBubble="square_s")
    ju "Some small text" (pauseVal=0.35, bounce=True, specBubble="square_s")
    ja "Some small text" (pauseVal=0.35, bounce=True, specBubble="square_s")
    r "Some small text" (pauseVal=0.35, bounce=True, specBubble="square2_s")
    r "Some small text" (pauseVal=0.35, bounce=True, specBubble="square_s")
    sa "Some small text" (pauseVal=0.35, bounce=True, specBubble="square_s")
    v "Some small text" (pauseVal=0.35, bounce=True, specBubble="square_s")
    y "Some small text" (pauseVal=0.35, bounce=True, specBubble="square_s")
    
    call answer 
    jump bubbles
    
label spike_s:  
    z "Some small text" (pauseVal=0.35, bounce=True, specBubble="spike_s")
    ju "Some small text" (pauseVal=0.35, bounce=True, specBubble="spike_s")
    ja "Some small text" (pauseVal=0.35, bounce=True, specBubble="spike_s")
    s "Some small text" (pauseVal=0.35, bounce=True, specBubble="spike_s")
    y "Some small text" (pauseVal=0.35, bounce=True, specBubble="spike_s")
    call answer 
    jump bubbles
    
## MEDIUM BUBBLES
    
label cloud_m:
    
    z "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="cloud_m")
    ju "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="cloud_m")
    ja "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="cloud_m")
    s "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="cloud_m")
    r "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="cloud_m")
    sa "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="cloud_m")
    v "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="cloud_m")
    y "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="cloud_m")
    
    call answer 
    jump bubbles
    
label sigh_m:
    z "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="sigh_m")
    ju "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="sigh_m")
    ja "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="sigh_m")
    s "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="sigh_m")
    r "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="sigh_m")
    v "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="sigh_m")
    y "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="sigh_m")

    call answer 
    jump bubbles
    
label round_m:    
    z "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="round_m")
    ju "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="round_m")
    ja "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="round_m")
    s "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="round_m")
    r "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="round_m")
    s "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="round2_m")
    v "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="round_m")
    y "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="round_m")

    call answer 
    jump bubbles
    
label square_m:  
    z "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="square_m")
    ju "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="square_m")
    ja "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="square_m")
    r "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="square2_m")
    r "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="square_m")
    sa "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="square_m")
    v "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="square_m")
    y "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="square_m")
    
    call answer 
    jump bubbles
    
label spike_m:  
    z "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="spike_m")
    ju "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="spike_m")
    ja "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="spike_m")
    s "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="spike_m")
    y "Longer text because this is a medium-sized bubble" (pauseVal=0.2, bounce=True, specBubble="spike_m")
    call answer 
    jump bubbles

    
## LARGE BUBBLES
label cloud_l:
    
    z "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="cloud_l")
    ju "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="cloud_l")
    ja "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="cloud_l")
    s "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="cloud_l")
    r "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="cloud_l")
    sa "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="cloud_l")
    v "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="cloud_l")
    y "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="cloud_l")
    
    call answer 
    jump bubbles
    
label sigh_l:
    z "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="sigh_l")
    ju "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="sigh_l")
    ja "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="sigh_l")
    s "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="sigh_l")
    r "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="sigh_l")
    v "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="sigh_l")
    y "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="sigh_l")

    call answer 
    jump bubbles
    
label round_l:    
    z "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="round_l")
    ju "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="round_l")
    ja "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="round_l")
    s "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="round_l")
    r "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="round_l")
    s "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="round2_l")
    v "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="round_l")
    y "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="round_l")

    call answer 
    jump bubbles
    
label square_l:  
    z "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="square_l")
    ju "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="square_l")
    ja "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="square_l")
    r "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="square2_l")
    r "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="square_l")
    sa "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="square_l")
    v "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="square_l")
    y "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="square_l")
    
    call answer 
    jump bubbles
    
label spike_l:  
    z "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="spike_l")
    ju "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="spike_l")
    ja "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="spike_l")
    s "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="spike_l")
    y "Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble" (pauseVal=0.1, bounce=True, specBubble="spike_l")
    call answer 
    jump bubbles
    
    
