label example_chat:

    $ first_choice = True
    $ choice_picked = None
    
    call hack      
    call chat_begin("hack")
    
    play music mystic_chat loop
    $ addchat("msg","Unknown has entered the chatroom", pv, False, False)
    $ addchat(u,"{=curly}Hello, [name] ^^{/=curly}", pv, False, False)
    $ addchat(u,"I thought you might come by.", pv, False, False)
    $ addchat(u,"{=curly}You want to learn more about how to make a chatroom, right?{/=curly}", pv, False, True)
    $ addchat(u,"I've come to show off a few of its features.", pv, False, False)
    
    call answer
    menu:
        "Let's get started!":
            $ addchat(m,"Let's get started!", 0, False, False)
            $ addchat(u,"Great! That's the kind of attitude I'm looking for ^^", pv, False, False)
        
        "What if I don't know any coding?":
            $ addchat(m,"What if I don't know any coding?", 0, False, False)
            $ addchat(u,"Don't worry! I've tried to make this as easy to use as possible.", pv, False, False)
            $ addchat(u,"You can always ask me questions on my blog, {a=http://www.zentherainbowunicorn.tumblr.com}which you can find here{/a}", pv, False, False)
            $ addchat(u,"{=sser1}This project was coded in Ren'Py, so you can always check out their forums, too.{/=sser1}", pv, False, False)

    $ addchat(u,"{=sser1}Anyway, you can see what we just did there was a menu!{/=sser1}", pv, False, False)
    $ addchat(u,"{=sser1}It allows you to alter a conversation based on responses.{/=sser1}", pv, False, False)
    $ addchat(u,"{=sser1}If you take a look Example Chat.rpy, you can get an idea of how to use them.{/=sser1}", pv, False, False)
    $ addchat(u,"{=sser1}You'll want to type \"call answer\" before a menu.{/=sser1}", pv, False, False)
    $ addchat(u,"{=sser1}That way the answer button will show up at the bottom of the screen instead of immediately jumping to a menu.{/=sser1}", pv, False, False)
    $ addchat(u,"{=ser1}There are lots of things to learn about!{/=ser1}", pv, False, False)
    $ addchat(u,"{=ser1b}What would you like to see first?{/=ser1b}", pv, False, False)
    
    
    call answer
    menu learn:    
    
        "Emojis and Images" if not choice_picked == "emojis":
            $ choice_picked = "emojis"
            if first_choice:
                $ addchat(m,"I want to learn how to use emojis and images", 0, False, False)   
                $ first_choice = False
                $ addchat(u,"{=ser1}Emojis and images, huh?{/=ser1}", pv, False, False)
                $ addchat(u,"{=ser1}Okay. I'll let someone else explain this.{/=ser1}", pv, False, False)
                $ addchat(u,"{=sser1}I'll be back later ^^{/=sser1}", pv, False, True)
                $ addchat("msg","Unknown has left the chatroom", pv, False, False)
            $ addchat("answer","",pv*0.5)   
            jump emojis
            
        "Banners" if not choice_picked == "banners":
            $ choice_picked = "banners"
            if first_choice:
                $ addchat(m,"Can you teach me about banners?", 0, False, False)
                $ first_choice = False
                $ addchat(u,"{=ser1}Oh, banners?{/=ser1}", pv, False, False)
                $ addchat(u,"{=ser1}Okay. I'll let someone else explain this.{/=ser1}", pv, False, False)
                $ addchat(u,"{=sser1}I'll be back later ^^{/=sser1}", pv, False, True)
                $ addchat("msg","Unknown has left the chatroom", pv, False, False)
            $ addchat("answer","",pv*0.5)
            jump banners
            
        "Heart Icons" if not choice_picked == "heart icons":
            $ choice_picked = "heart icons"
            if first_choice:
                $ addchat(m,"I'd like to learn about heart icons", 0, False, False)
                $ first_choice = False
                $ addchat(u,"{=curly}Heart icons?{/=curly}", pv, False, True)
                $ addchat(u,"{=ser1}Hmm, sounds good. I'll let someone else explain this.{/=ser1}", pv, False, False)
                $ addchat(u,"{=sser1}I'll be back later ^^{/=sser1}", pv, False, True)
                $ addchat("msg","Unknown has left the chatroom", pv, False, False)
            $ addchat("answer","",pv*0.5)
            jump heart_icons
            
        "Screen Shake and Special Bubbles" if not choice_picked == "spec bubbles":
            $ choice_picked = "spec bubbles"
            if first_choice:
                $ addchat(m,"Screen shake and special bubbles, please", 0, False, False)
                $ first_choice = False
                $ addchat(u,"{=ser1}You want to know about special speech bubbles and screen shake?{/=ser1}", pv, False, True)
                $ addchat(u,"{=ser1}Alright then. I'll let someone else explain this.{/=ser1}", pv, False, False)
                $ addchat(u,"{=sser1}I'll be back later ^^{/=sser1}", pv, False, True)
                $ addchat("msg","Unknown has left the chatroom", pv, False, False)
            $ addchat("answer","",pv*0.5)
            jump screen_shake
            
        "I'm done for now" if not first_choice:
            jump ending
            
label emojis:

    call hack
    call chat_begin("morning",False,False)
    
    play music geniusly_hacked_bebop loop
    $ addchat("msg","707 has entered the chatroom", pv, False, False)
    $ addchat(s,"{=sser1}O{/=sser1}", 0.1, False, False)
    $ addchat(s,"{=sser1}M{/=sser1}", 0.1, False, False)
    $ addchat(s,"{=sser1}G{/=sser1}", 0.1, False, False)
    $ addchat(s,"{size=+10}I get to explain emojis!!!{/size}", pv, False, False)
    $ addchat(s,"{image=seven wow}", pv, True, False)
    $ addchat(s,"{size=+10}Yay!!!{/size}", pv, False, True, "spike_m")
    $ addchat(s,"{=sser1}Okay so what you wanna do is go find the right emoji in the emojis.rpy file.{/=sser1}", pv, False, False)
    $ addchat(s,"{=sser1}Then you're gonna type {{image=seven wow} or whatever the emoji name is into the Dialogue part of the Script Generator spreadsheet{/=sser1}", pv, False, False)
    $ addchat(s,"{=sser1}The program will automatically add the right sound file for you ^^{/=sser1}", pv, False, False)
    $ addchat(s,"{=ser1b}You'll also want to tick the \"Image\" modifier in the spreadsheet{/=ser1b}", pv, False, False)
    $ addchat(s,"{=blocky}otherwise it'll look like this lolol{/=blocky}", pv, False, False)
    $ addchat(s,"{image=seven wow}", pv, False, False)
    $ addchat(s,"Which is probably not what you want!", pv, False, False)
    $ addchat(s,"You'll have to be careful to get the spelling right,", pv, False, False)
    $ addchat(s,"{=sser1}since otherwise you'll get an \"image not found\" message.{/=sser1}", pv, False, False)
    $ addchat(s,"{=blocky}And it won't play any sound files, either!{/=blocky}", pv, False, True)
    $ addchat(s,"{=ser1}If you want to add more emojis,{/=ser1}", pv, False, False)
    $ addchat(s,"{=ser1}just follow the rules you see in emojis.rpy{/=ser1}", pv, False, False)
    $ addchat(s,"{=ser1}You'll need to add it to the emoji_lookup dictionary list as well.{/=ser1}", pv, False, False)
    $ addchat(s,"{=ser1xb}Just use the existing entries as a guide.{/=ser1xb}", pv, False, False)
    $ addchat(s,"{=curly}Now I'll let you check out the emojis currently coded into the game.{/=curly}", pv, False, False)
    $ addchat(s,"Just select a character to see the available emojis or \"Done\" if you're finished", pv, False, True)
   
    
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
            $ addchat(s,"The last thing I'm here to explain is how to post CGs.", pv, False, False)
            $ addchat(s,"{=curly}That means images like this!{/=curly}", pv, False, True)
            $ addchat(s,"seven_cg1", pv, True, False)
            $ addchat(s,"{=sser1b}They're fully clickable like they are in-game; check it out!{/=sser1b}", pv, False, False)
            $ addchat(s,"You post these a little differently from emojis. ", pv, False, False)
            $ addchat(s,"{=ser1}You'll need to start by defining an image in variables.rpy{/=ser1}", pv, False, False)
            $ addchat(s,"{=ser1}For example, that last image is called \"seven_cg1\"{/=ser1}", pv, False, False)
            $ addchat(s,"{=ser1}It should be 750x1334 pixels, and it will be automatically resized for the chatroom.{/=ser1}", pv, False, False)
            $ addchat(s,"{=ser1}Then to call it, just type the name of the image you defined and check off the \"Image\" modifier in the spreadsheet.{/=ser1}", pv, False, False)
            $ addchat(s,"{=blocky}If you don't, it'll just show up in text, like this:{/=blocky}", pv, False, False)
            $ addchat(s,"seven_cg1", pv, False, False)
            $ addchat(s,"But if you check off the \"Image\" modifier, you get this:", pv, False, True, "round2_m")
            $ addchat(s,"seven_cg1", pv, True, False)
            $ addchat(s,"The ability to click the image/the full screen version is automatically taken care of for you.", pv, False, False)
            $ addchat(s,"{=curly}Hope this helped!{/=curly}", pv, False, True, "round_m")
            $ addchat(s,"{=sser1}Let me know if you have any questions later~{/=sser1}", pv, False, False)
            $ addchat("msg","707 has left the chatroom", pv, False, False)
            call answer
            jump learn


label banners:

    call hack
    call chat_begin("noon",False,False)
    play music same_old_fresh_air loop
    
    $ addchat("msg","Yoosung★ has entered the chatroom", pv, False, False)
    $ addchat(y,"{=curly}Hello!{/=curly}", pv, False, False)
    $ addchat(y,"I'm supposed to explain banners to you.", pv, False, False)
    $ addchat(y,"It's pretty quick, I promise!", pv, False, False)
    $ addchat(y,"{image=yoosung yahoo}", pv, True, False)
    $ addchat(y,"There are four different types of banners:", pv, False, False)
    $ addchat(y,"{=sser1}The lightning banner!{/=sser1}", pv, False, True)
    call banner_lightning
    $ addchat(y,"For when you're feeling angry ^^;;", pv, False, False)
    $ addchat(y,"{=sser1}The heart banner!{/=sser1}", pv, False, True)
    call banner_heart
    $ addchat(y,"{=sser1}For happy stuff!{/=sser1}", pv, False, False)
    $ addchat(y,"{=sser1}The annoy banner{/=sser1}", pv, False, True)
    call banner_annoy
    $ addchat(y,"For when you're irritated", pv, False, False)
    $ addchat(y,"And last but not least, ", pv, False, False)
    $ addchat(y,"{=ser1}the 'well' banner!{/=ser1}", pv, False, True)
    call banner_well
    $ addchat(y,"{=ser1}...{/=ser1}", pv, False, False)
    $ addchat(y,"It's for times when you're a little lost for words.", pv, False, False)
    $ addchat(y,"{=sser1}That's all from me!{/=sser1}", pv, False, False)
    $ addchat(y,"Good luck with the program ^^", pv, False, False)
    $ addchat(y,"{image=yoosung wow}", pv, True, False)
    $ addchat("msg","Yoosung★ has left the chatroom", pv, False, False)

    call answer
    jump learn
    
label heart_icons:

    call hack
    call chat_begin("evening",False,False)
    play music narcissistic_jazz loop
    
    $ addchat("msg","Zen has entered the chatroom", pv, False, False)
    $ addchat(z,"{image=zen wink}", pv, True, False)
    $ addchat(z,"{=curly}Hey cutie ^^{/=curly}", pv, False, True)
    $ addchat(z,"I'm here to explain heart icons!", pv, False, False)
    $ addchat(z,"{=sser2}They look like this:{/=sser2}", pv, False, False)
    call heart_icon(z)
    $ addchat(z,"{=sser2}And each character has a different one{/=sser2}", pv, False, False)
    $ addchat(z,"{=sser1b}They all use the same white heart, this one{/=sser1b}", pv, False, False)
    call heart_icon(u)
    $ addchat(z,"{=sser1}and just recolour it depending on what argument you pass via \"call heart_icon(z)\"{/=sser1}", pv, False, False)
    $ addchat(z,"{=sser1}You can easily add your own colours, too, by adding the character and colour to the heartcolour list in MysMe Screen Effects.rpy{/=sser1}", pv, False, False)
    $ addchat(z,"{=blocky}Here are the currently available colours:{/=blocky}", pv, False, False)
    $ addchat(z,"{=sser1}Seven{/=sser1}", pv, False, False)
    call heart_icon(s)
    $ addchat(z,"{=curly}Me!{/=curly}", pv, False, False)
    call heart_icon(z)
    $ addchat(z,"{=sser1}Jaehee{/=sser1}", pv, False, False)
    call heart_icon(ja)
    $ addchat(z,"{=sser1}Jumin{/=sser1}", pv, False, False)
    call heart_icon(ju)
    $ addchat(z,"{=sser1}Yoosung{/=sser1}", pv, False, False)
    call heart_icon(y)
    $ addchat(z,"{=sser1}Ray{/=sser1}", pv, False, False)
    call heart_icon(ra)
    $ addchat(z,"{=sser1}V{/=sser1}", pv, False, False)
    call heart_icon(v)
    $ addchat(z,"{=ser1}and then there are a few special ones{/=ser1}", pv, False, False)
    $ addchat(z,"{=sser1}The white heart I mentioned before (tied to the username 'Unknown'){/=sser1}", pv, False, False)
    call heart_icon(u)
    $ addchat(z,"{=sser1}You can also get this heart by passing heart_icon the short form for Saeran (sa or \"Sae\"){/=sser1}", pv, False, False)
    call heart_icon(sa)
    $ addchat(z,"And then there is this heart", pv, False, False)
    call heart_icon(r)
    $ addchat(z,"which is for Rika, but isn't found in-game", pv, False, False)
    $ addchat(z,"{=sser1}The last thing I'm here to explain is the 'heartbreak' icon{/=sser1}", pv, False, False)
    $ addchat(z,"{=sser1}It works the same as the regular heart icons -- just add a colour to the heartcolour list and call \"heart_break\" with that character{/=sser1}", pv, False, False)
    $ addchat(z,"{=ser1}It will automatically colour itself{/=ser1}", pv, False, False)
    $ addchat(z,"They look like this!", pv, False, False)
    call heart_break(z)
    $ addchat(z,"But you don't really want to hurt any of our feelings, right?", pv, False, True)
    $ addchat(z,"{image=zen happy}", pv, True, False)
    call heart_icon(z)
    $ addchat(z,"{=ser1}The program automatically tallies the heart points you've earned during a chatroom and displays the total after you hit Save&Exit.{/=ser1}", pv, False, False)
    $ addchat(z,"{=sser1}It keeps track of both the total points earned during a chatroom,{/=sser1}", pv, False, False)
    $ addchat(z,"{=sser1}as well as how many points you have with each individual character{/=sser1}", pv, False, False)
    $ addchat(z,"{=curly}Just to keep the door open for other use possibilities ^^{/=curly}", pv, False, True, "round_m")
    $ addchat(z,"{=blocky}Also note that Ray and Saeran's heart points count towards the same character{/=blocky}", pv, False, False)
    $ addchat(z,"{=curly}Good luck with the rest of the program!{/=curly}", pv, False, True)
    $ addchat("msg","Zen has left the chatroom", pv, False, False)
    
    call answer
    jump learn
    
label screen_shake:
    
    call hack
    call chat_begin("night",False,False)
    play music lonesome_practicalism loop

    $ addchat("msg","Jaehee Kang has entered the chatroom", pv, False, False)
    $ addchat(ja,"{=ser1}Hello, [name].{/=ser1}", pv, False, False)
    $ addchat(ja,"{=ser1}Mr. Han will be with us shortly. {/=ser1}", pv, False, False)
    $ addchat("msg","Jumin Han has entered the chatroom", pv, False, False)
    $ addchat(ja,"{=curly}Ah, right on time.{/=curly}", pv, False, True, "cloud_s")
    $ addchat(ja,"{=ser1}Shall we get started then?{/=ser1}", pv, False, False)
    $ addchat(ja,"{=ser1}...{/=ser1}", pv, False, False)
    call banner_well
    $ addchat(ja,"{=ser1}Mr. Han?{/=ser1}", pv, False, False)
    $ addchat(ja,"{image=jaehee well}", pv, True, False)
    $ addchat(ja,"{=sser1}Mr. Han.{/=sser1}", pv, False, False)
    $ addchat(ja,"{=sser1}{size=+10}MR. HAN!!{/size}{/=sser1}", pv, False, True, "spike_m")
    show night at shake
    $ addchat(ju,"{=curly}Is something the matter?{/=curly}", pv, False, True, "cloud_m")
    $ addchat(ja,"{=sser1}Oh.{/=sser1}", pv, False, True, "sigh_s")
    $ addchat(ja,"{=ser1}You weren't responding so I thought perhaps you were asleep.{/=ser1}", pv, False, False)
    $ addchat(ju,"{=sser1}Elizabeth the 3rd was sleeping on my lap so I couldn't disturb her.{/=sser1}", pv, False, True, "cloud_l")
    $ addchat(ja,"Of course;;", pv, False, True, "sigh_m")
    $ addchat(ja,"{=ser1}...As I was saying.{/=ser1}", pv, False, False)
    $ addchat(ja,"We're supposed to teach [name] about some other chatroom features.", pv, False, True)
    $ addchat(ju,"{=ser1}Like the special speech bubbles?{/=ser1}", pv, False, True, "square_m")
    $ addchat(ja,"Yes ^^", pv, False, True, "cloud_s")
    $ addchat(ja,"{=sser1}In the Script Generator spreadsheet, you'll see an option called \"special bubble\"{/=sser1}", pv, False, False)
    $ addchat(ja,"{=sser1}You can look in the folder \"Bubbles/Special\" and find the correct bubble{/=sser1}", pv, False, False)
    $ addchat(ja,"Most bubbles come in three sizes:", pv, False, True)
    $ addchat(ja,"{=sser1b}small{/=sser1b}", pv, False, False)
    $ addchat(ja,"{=sser1b}medium{/=sser1b}", pv, False, False)
    $ addchat(ja,"{=sser1b}and large{/=sser1b}", pv, False, False)
    $ addchat(ja,"{=ser1}The text should usually resize itself to fit, but it might be finicky sometimes, since most bubbles have to be adjusted individually{/=ser1}", pv, False, False)
    $ addchat(ja,"{color=#f00}For example, this bubble might be too small.{/color}", pv, False, True, "cloud_s")
    $ addchat(ja,"{=ser1}As for screen shake,{/=ser1}", pv, False, False)
    $ addchat(ja,"{=ser1}how you use it depends on which background you're using{/=ser1}", pv, False, False)
    $ addchat(ja,"{=ser1xb}For example, this is the \"night\" background{/=ser1xb}", pv, False, False)
    $ addchat(ja,"{=sser1}So we call \"show night at shake\"{/=sser1}", pv, False, False)
    $ addchat(ja,"And it does this", pv, False, True)
    show night at shake
    $ addchat(ja,"{=ser1}Lastly, you can check out all of the special bubbles present in the game.{/=ser1}", pv, False, False)
    $ addchat(ja,"{=ser1xb}Just select \"Done\" when you're finished.{/=ser1xb}", pv, False, False)
    call answer
    jump bubbles
    

label ending:
    call hack
    call chat_begin("hack",False,False)
    
    play music mystic_chat loop
    
    $ addchat("msg","Unknown has entered the chatroom", pv, False, False)
    $ addchat(u,"{=curly}You're back!{/=curly}", pv, False, True)
    $ addchat(u,"So what did you think?", pv, False, False)
    $ addchat(u,"Are you ready to start making your own chatrooms?", pv, False, False)
    call answer
    menu:
        "Definitely!":
            $ addchat(m,"Definitely!", 0, False, False)
            $ addchat(u,"I'm glad! ^^", pv, False, False)
                    
        "I don't know if I'm ready yet...":
            $ addchat(m,"I don't know if I'm ready yet...", 0, False, False)
            $ addchat(u,"{=ser1}I recommend reading through the code for this chatroom and the coffee chatroom.{/=ser1}", pv, False, False)
            $ addchat(u,"{=ser1}And maybe go through this example chatroom a few times and compare it with the code!{/=ser1}", pv, False, False)

    $ addchat(u,"{=sser1}I've put a lot of work into this program, so any feedback is welcome!{/=sser1}", pv, False, False)
    $ addchat(u,"And please credit me if you do use it somewhere!", pv, False, False)
    $ addchat(u,"I hope you find this program helpful.", pv, False, False)
    $ addchat(u,"Good luck!", pv, False, False)
    $ addchat("msg","Unknown has left the chatroom", pv, False, False)
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
        $ addchat(ju,"{=ser1}That's all from us.{/=ser1}", pv, False, False)
        $ addchat(ju,"{=ser1}Note that currently you can only use the bubbles associated with the speaking character{/=ser1}", pv, False, False)
        $ addchat(ju,"{=ser1}For example, Assistant Kang cannot use my Elizabeth the 3rd bubble.{/=ser1}", pv, False, True, "cloud_l")
        $ addchat(ju,"I must excuse myself.", pv, False, False)
        $ addchat("msg","Jumin Han has left the chatroom", pv, False, False)
        $ addchat(ja,"{=ser1}I'll be leaving too. Best of luck with the program.{/=ser1}", pv, False, False)
        $ addchat("msg","Jaehee Kang has left the chatroom", pv, False, False)
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
    $ addchat(ja,"{image=jaehee angry}", pv, True, False)
    $ addchat(ja,"{image=jaehee happy}", pv, True, False)
    $ addchat(ja,"{image=jaehee hehe}", pv, True, False)
    $ addchat(ja,"{image=jaehee huff}", pv, True, False)
    $ addchat(ja,"{image=jaehee oops}", pv, True, False)
    $ addchat(ja,"{image=jaehee question}", pv, True, False)
    $ addchat(ja,"{image=jaehee sad}", pv, True, False)
    $ addchat(ja,"{image=jaehee well}", pv, True, False)
    $ addchat(ja,"{image=jaehee wow}", pv, True, False)
    call answer
    jump emoji


label jumin_emoji:
    $ addchat(ju,"{image=jumin angry}", pv, True, False)
    $ addchat(ju,"{image=jumin sad}", pv, True, False)
    $ addchat(ju,"{image=jumin smile}", pv, True, False)
    $ addchat(ju,"{image=jumin well}", pv, True, False)
    call answer
    jump emoji


label ray_emoji:
    $ addchat(ra,"{image=ray cry}", pv, True, False)
    $ addchat(ra,"{image=ray happy}", pv, True, False)
    $ addchat(ra,"{image=ray huff}", pv, True, False)
    $ addchat(ra,"{image=ray question}", pv, True, False)
    $ addchat(ra,"{image=ray smile}", pv, True, False)
    $ addchat(ra,"{image=ray well}", pv, True, False)
    $ addchat(ra,"{image=ray wink}", pv, True, False)
    call answer
    jump emoji

label saeran2_emoji:
    $ addchat(ra,"{image=saeran2 cry}", pv, True, False)
    $ addchat(ra,"{image=saeran2 happy}", pv, True, False)
    $ addchat(ra,"{image=saeran2 huff}", pv, True, False)
    $ addchat(ra,"{image=saeran2 question}", pv, True, False)
    $ addchat(ra,"{image=saeran2 smile}", pv, True, False)
    $ addchat(ra,"{image=saeran2 well}", pv, True, False)
    $ addchat(ra,"{image=saeran2 wink}", pv, True, False)
    call answer
    jump emoji

label saeran_emoji:
    $ addchat(sa,"{image=saeran expecting}", pv, True, False)
    $ addchat(sa,"{image=saeran happy}", pv, True, False)
    $ addchat(sa,"{image=saeran well}", pv, True, False)
    $ addchat(sa,"{image=saeran questioning}", pv, True, False)
    call answer
    jump emoji


label seven_emoji:
    $ addchat(s,"{image=seven cry}", pv, True, False)
    $ addchat(s,"{image=seven huff}", pv, True, False)
    $ addchat(s,"{image=seven khee}", pv, True, False)
    $ addchat(s,"{image=seven love}", pv, True, False)
    $ addchat(s,"{image=seven question}", pv, True, False)
    $ addchat(s,"{image=seven what}", pv, True, False)
    $ addchat(s,"{image=seven wow}", pv, True, False)
    $ addchat(s,"{image=seven yahoo}", pv, True, False)
    $ addchat(s,"{image=seven yoohoo}", pv, True, False)
    call answer
    jump emoji

label rika_emoji:
    $ addchat(r,"{image=rika happy}", pv, True, False)
    $ addchat(r,"{image=rika cry}", pv, True, False)
    $ addchat(r,"{image=rika pout}", pv, True, False)
    call answer
    jump emoji

label v_emoji:
    $ addchat(v,"{image=v shock}", pv, True, False)
    $ addchat(v,"{image=v smile}", pv, True, False)
    $ addchat(v,"{image=v well}", pv, True, False)
    $ addchat(v,"{image=v wink}", pv, True, False)
    call answer
    jump emoji

label yoosung_emoji:
    $ addchat(y,"{image=yoosung angry}", pv, True, False)
    $ addchat(y,"{image=yoosung cry}", pv, True, False)
    $ addchat(y,"{image=yoosung happy}", pv, True, False)
    $ addchat(y,"{image=yoosung huff}", pv, True, False)
    $ addchat(y,"{image=yoosung puff}", pv, True, False)
    $ addchat(y,"{image=yoosung question}", pv, True, False)
    $ addchat(y,"{image=yoosung thankyou}", pv, True, False)
    $ addchat(y,"{image=yoosung what}", pv, True, False)
    $ addchat(y,"{image=yoosung wow}", pv, True, False)
    $ addchat(y,"{image=yoosung yahoo}", pv, True, False)
    call answer
    jump emoji

label zen_emoji:
    $ addchat(z,"{image=zen angry}", pv, True, False)
    $ addchat(z,"{image=zen happy}", pv, True, False)
    $ addchat(z,"{image=zen hmm}", pv, True, False)
    $ addchat(z,"{image=zen oyeah}", pv, True, False)
    $ addchat(z,"{image=zen question}", pv, True, False)
    $ addchat(z,"{image=zen sad}", pv, True, False)
    $ addchat(z,"{image=zen shock}", pv, True, False)
    $ addchat(z,"{image=zen well}", pv, True, False)
    $ addchat(z,"{image=zen wink}", pv, True, False)
    call answer
    jump emoji
        
## SMALL BUBBLES
label cloud_s:
    
    $ addchat(z,"Some small text", 0.5, False, True, "cloud_s")
    $ addchat(ju,"Some small text", 0.5, False, True, "cloud_s")
    $ addchat(ja,"Some small text", 0.5, False, True, "cloud_s")
    $ addchat(s,"Some small text", 0.5, False, True, "cloud_s")
    $ addchat(ra,"Some small text", 0.5, False, True, "cloud_s")
    $ addchat(sa,"Some small text", 0.5, False, True, "cloud_s")
    $ addchat(v,"Some small text", 0.5, False, True, "cloud_s")
    $ addchat(y,"Some small text", 0.5, False, True, "cloud_s")
    
    call answer
    jump bubbles
    
label sigh_s:
    $ addchat(z,"Some small text", 0.5, False, True, "sigh_s")
    $ addchat(ju,"Some small text", 0.5, False, True, "sigh_s")
    $ addchat(ja,"Some small text", 0.5, False, True, "sigh_s")
    $ addchat(s,"Some small text", 0.5, False, True, "sigh_s")
    $ addchat(ra,"Some small text", 0.5, False, True, "sigh_s")
    $ addchat(v,"Some small text", 0.5, False, True, "sigh_s")
    $ addchat(y,"Some small text", 0.5, False, True, "sigh_s")

    call answer
    jump bubbles
    
label round_s:    
    $ addchat(z,"Some small text", 0.5, False, True, "round_s")
    $ addchat(ju,"Some small text", 0.5, False, True, "round_s")
    $ addchat(ja,"Some small text", 0.5, False, True, "round_s")
    $ addchat(s,"Some small text", 0.5, False, True, "round_s")
    $ addchat(ra,"Some small text", 0.5, False, True, "round_s")
    $ addchat(s,"Some small text", 0.5, False, True, "round2_s")
    $ addchat(v,"Some small text", 0.5, False, True, "round_s")
    $ addchat(y,"Some small text", 0.5, False, True, "round_s")

    call answer
    jump bubbles
    
label square_s:  
    $ addchat(z,"Some small text", 0.5, False, True, "square_s")
    $ addchat(ju,"Some small text", 0.5, False, True, "square_s")
    $ addchat(ja,"Some small text", 0.5, False, True, "square_s")
    $ addchat(ra,"Some small text", 0.5, False, True, "square2_s")
    $ addchat(ra,"Some small text", 0.5, False, True, "square_s")
    $ addchat(sa,"Some small text", 0.5, False, True, "square_s")
    $ addchat(v,"Some small text", 0.5, False, True, "square_s")
    $ addchat(y,"Some small text", 0.5, False, True, "square_s")
    
    call answer
    jump bubbles
    
label spike_s:  
    $ addchat(z,"Some small text", 0.5, False, True, "spike_s")
    $ addchat(ju,"Some small text", 0.5, False, True, "spike_s")
    $ addchat(ja,"Some small text", 0.5, False, True, "spike_s")
    $ addchat(s,"Some small text", 0.5, False, True, "spike_s")
    $ addchat(y,"Some small text", 0.5, False, True, "spike_s")
    call answer
    jump bubbles
    
## MEDIUM BUBBLES
    
label cloud_m:
    
    $ addchat(z,"Longer text because this is a medium-sized bubble", 0.35, False, True, "cloud_m")
    $ addchat(ju,"Longer text because this is a medium-sized bubble", 0.35, False, True, "cloud_m")
    $ addchat(ja,"Longer text because this is a medium-sized bubble", 0.35, False, True, "cloud_m")
    $ addchat(s,"Longer text because this is a medium-sized bubble", 0.35, False, True, "cloud_m")
    $ addchat(ra,"Longer text because this is a medium-sized bubble", 0.35, False, True, "cloud_m")
    $ addchat(sa,"Longer text because this is a medium-sized bubble", 0.35, False, True, "cloud_m")
    $ addchat(v,"Longer text because this is a medium-sized bubble", 0.35, False, True, "cloud_m")
    $ addchat(y,"Longer text because this is a medium-sized bubble", 0.35, False, True, "cloud_m")
    
    call answer
    jump bubbles
    
label sigh_m:
    $ addchat(z,"Longer text because this is a medium-sized bubble", 0.35, False, True, "sigh_m")
    $ addchat(ju,"Longer text because this is a medium-sized bubble", 0.35, False, True, "sigh_m")
    $ addchat(ja,"Longer text because this is a medium-sized bubble", 0.35, False, True, "sigh_m")
    $ addchat(s,"Longer text because this is a medium-sized bubble", 0.35, False, True, "sigh_m")
    $ addchat(ra,"Longer text because this is a medium-sized bubble", 0.35, False, True, "sigh_m")
    $ addchat(v,"Longer text because this is a medium-sized bubble", 0.35, False, True, "sigh_m")
    $ addchat(y,"Longer text because this is a medium-sized bubble", 0.35, False, True, "sigh_m")

    call answer
    jump bubbles
    
label round_m:    
    $ addchat(z,"Longer text because this is a medium-sized bubble", 0.35, False, True, "round_m")
    $ addchat(ju,"Longer text because this is a medium-sized bubble", 0.35, False, True, "round_m")
    $ addchat(ja,"Longer text because this is a medium-sized bubble", 0.35, False, True, "round_m")
    $ addchat(s,"Longer text because this is a medium-sized bubble", 0.35, False, True, "round_m")
    $ addchat(ra,"Longer text because this is a medium-sized bubble", 0.35, False, True, "round_m")
    $ addchat(s,"Longer text because this is a medium-sized bubble", 0.35, False, True, "round2_m")
    $ addchat(v,"Longer text because this is a medium-sized bubble", 0.35, False, True, "round_m")
    $ addchat(y,"Longer text because this is a medium-sized bubble", 0.35, False, True, "round_m")

    call answer
    jump bubbles
    
label square_m:  
    $ addchat(z,"Longer text because this is a medium-sized bubble", 0.35, False, True, "square_m")
    $ addchat(ju,"Longer text because this is a medium-sized bubble", 0.35, False, True, "square_m")
    $ addchat(ja,"Longer text because this is a medium-sized bubble", 0.35, False, True, "square_m")
    $ addchat(ra,"Longer text because this is a medium-sized bubble", 0.35, False, True, "square2_m")
    $ addchat(ra,"Longer text because this is a medium-sized bubble", 0.35, False, True, "square_m")
    $ addchat(sa,"Longer text because this is a medium-sized bubble", 0.35, False, True, "square_m")
    $ addchat(v,"Longer text because this is a medium-sized bubble", 0.35, False, True, "square_m")
    $ addchat(y,"Longer text because this is a medium-sized bubble", 0.35, False, True, "square_m")
    
    call answer
    jump bubbles
    
label spike_m:  
    $ addchat(z,"Longer text because this is a medium-sized bubble", 0.35, False, True, "spike_m")
    $ addchat(ju,"Longer text because this is a medium-sized bubble", 0.35, False, True, "spike_m")
    $ addchat(ja,"Longer text because this is a medium-sized bubble", 0.35, False, True, "spike_m")
    $ addchat(s,"Longer text because this is a medium-sized bubble", 0.35, False, True, "spike_m")
    $ addchat(y,"Longer text because this is a medium-sized bubble", 0.35, False, True, "spike_m")
    call answer
    jump bubbles

    
## LARGE BUBBLES
label cloud_l:
    
    $ addchat(z,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "cloud_l")
    $ addchat(ju,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "cloud_l")
    $ addchat(ja,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "cloud_l")
    $ addchat(s,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "cloud_l")
    $ addchat(ra,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "cloud_l")
    $ addchat(sa,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "cloud_l")
    $ addchat(v,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "cloud_l")
    $ addchat(y,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "cloud_l")
    
    call answer
    jump bubbles
    
label sigh_l:
    $ addchat(z,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "sigh_l")
    $ addchat(ju,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "sigh_l")
    $ addchat(ja,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "sigh_l")
    $ addchat(s,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "sigh_l")
    $ addchat(ra,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "sigh_l")
    $ addchat(v,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "sigh_l")
    $ addchat(y,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "sigh_l")

    call answer
    jump bubbles
    
label round_l:    
    $ addchat(z,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "round_l")
    $ addchat(ju,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "round_l")
    $ addchat(ja,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "round_l")
    $ addchat(s,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "round_l")
    $ addchat(ra,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "round_l")
    $ addchat(s,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "round2_l")
    $ addchat(v,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "round_l")
    $ addchat(y,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "round_l")

    call answer
    jump bubbles
    
label square_l:  
    $ addchat(z,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "square_l")
    $ addchat(ju,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "square_l")
    $ addchat(ja,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "square_l")
    $ addchat(ra,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "square2_l")
    $ addchat(ra,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "square_l")
    $ addchat(sa,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "square_l")
    $ addchat(v,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "square_l")
    $ addchat(y,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "square_l")
    
    call answer
    jump bubbles
    
label spike_l:  
    $ addchat(z,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "spike_l")
    $ addchat(ju,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "spike_l")
    $ addchat(ja,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "spike_l")
    $ addchat(s,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "spike_l")
    $ addchat(y,"Longest text since this is a large bubble and as such should wrap text so it doesn't overflow from the bubble", 0.2, False, True, "spike_l")
    call answer
    jump bubbles
    
    
