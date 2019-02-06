#************************************
# Emotes
#************************************
init offset = -10

init python:

    ## This list contains all of the emojis, linked to the correct sound effect
    ## Essentially, if the dialogue matches the item on the left
    ## (e.g. {image=jaehee angry}) then it will play the sound effect on the right
    ## If you add your own custom emojis, you'll need to add them to this list
    ## so that they play the correct sound effect
    emoji_lookup = {'{image=jaehee angry}': 'sfx/Emotes/Jaehee/jaehee_angry.wav', 
                    '{image=jaehee happy}': 'sfx/Emotes/Jaehee/jaehee_happy.wav', 
                    '{image=jaehee hehe}': 'sfx/Emotes/Jaehee/jaehee_hehe.wav', 
                    '{image=jaehee huff}': 'sfx/Emotes/Jaehee/jaehee_huff.wav', 
                    '{image=jaehee oops}': 'sfx/Emotes/Jaehee/jaehee_oops.wav', 
                    '{image=jaehee question}': 'sfx/Emotes/Jaehee/jaehee_question.wav', 
                    '{image=jaehee sad}': 'sfx/Emotes/Jaehee/jaehee_sad.wav', 
                    '{image=jaehee well}': 'sfx/Emotes/Jaehee/jaehee_well.wav', 
                    '{image=jaehee wow}': 'sfx/Emotes/Jaehee/jaehee_wow.wav', 
                    
                    '{image=jumin angry}': 'sfx/Emotes/Jumin/jumin_angry.wav', 
                    '{image=jumin sad}': 'sfx/Emotes/Jumin/jumin_sad.wav', 
                    '{image=jumin smile}': 'sfx/Emotes/Jumin/jumin_smile.wav', 
                    '{image=jumin well}': 'sfx/Emotes/Jumin/jumin_well.wav', 
                    
                    '{image=rika happy}': 'sfx/Emotes/Rika/rika_happy.mp3',
                    '{image=rika pout}': 'sfx/Emotes/Rika/rika_pout.mp3',
                    '{image=rika cry}': 'sfx/Emotes/Rika/rika_cry.mp3',
                    
                    '{image=ray cry}': 'sfx/Emotes/Ray/ray_cry.wav', 
                    '{image=ray happy}': 'sfx/Emotes/Ray/ray_happy.wav', 
                    '{image=ray huff}': 'sfx/Emotes/Ray/ray_huff.wav', 
                    '{image=ray question}': 'sfx/Emotes/Ray/ray_question.wav', 
                    '{image=ray smile}': 'sfx/Emotes/Ray/ray_smile.wav', 
                    '{image=ray well}': 'sfx/Emotes/Ray/ray_well.wav', 
                    '{image=ray wink}': 'sfx/Emotes/Ray/ray_wink.wav', 
                    
                    '{image=saeran2 cry}': 'sfx/Emotes/Ray/ray_cry.wav', 
                    '{image=saeran2 happy}': 'sfx/Emotes/Ray/ray_happy.wav', 
                    '{image=saeran2 huff}': 'sfx/Emotes/Ray/ray_huff.wav', 
                    '{image=saeran2 question}': 'sfx/Emotes/Ray/ray_question.wav', 
                    '{image=saeran2 smile}': 'sfx/Emotes/Ray/ray_smile.wav', 
                    '{image=saeran2 well}': 'sfx/Emotes/Ray/ray_well.wav', 
                    '{image=saeran2 wink}': 'sfx/Emotes/Ray/ray_wink.wav',
                    
                    '{image=saeran expecting}': 'sfx/Emotes/Saeran/saeran_expecting.wav', 
                    '{image=saeran happy}': 'sfx/Emotes/Saeran/saeran_happy.wav', 
                    '{image=saeran questioning}': 'sfx/Emotes/Saeran/saeran_questioning.wav', 
                    '{image=saeran well}': 'sfx/Emotes/Saeran/saeran_well.wav',                     
                    
                    '{image=seven cry}': 'sfx/Emotes/Seven/seven_cry.wav', 
                    '{image=seven huff}': 'sfx/Emotes/Seven/seven_huff.wav', 
                    '{image=seven khee}': 'sfx/Emotes/Seven/seven_khee.wav', 
                    '{image=seven love}': 'sfx/Emotes/Seven/seven_love.wav', 
                    '{image=seven question}': 'sfx/Emotes/Seven/seven_question.wav', 
                    '{image=seven what}': 'sfx/Emotes/Seven/seven_what.wav', 
                    '{image=seven wow}': 'sfx/Emotes/Seven/seven_wow.wav', 
                    '{image=seven yahoo}': 'sfx/Emotes/Seven/seven_yahoo.wav', 
                    '{image=seven yoohoo}': 'sfx/Emotes/Seven/seven_yoohoo.wav',

                    '{image=v shock}': 'sfx/Emotes/V/v_shock.wav', 
                    '{image=v smile}': 'sfx/Emotes/V/v_smile.wav',
                    '{image=v well}': 'sfx/Emotes/V/v_well.wav',
                    '{image=v wink}': 'sfx/Emotes/V/v_wink.wav',
                    
                    '{image=yoosung angry}': 'sfx/Emotes/Yoosung/yoosung_angry.wav',
                    '{image=yoosung cry}': 'sfx/Emotes/Yoosung/yoosung_cry.wav',
                    '{image=yoosung happy}': 'sfx/Emotes/Yoosung/yoosung_happy.wav',
                    '{image=yoosung huff}': 'sfx/Emotes/Yoosung/yoosung_huff.wav',
                    '{image=yoosung puff}': 'sfx/Emotes/Yoosung/yoosung_puff.wav',
                    '{image=yoosung question}': 'sfx/Emotes/Yoosung/yoosung_question.wav',
                    '{image=yoosung thankyou}': 'sfx/Emotes/Yoosung/yoosung_thankyou.wav',
                    '{image=yoosung what}': 'sfx/Emotes/Yoosung/yoosung_what.wav',
                    '{image=yoosung wow}': 'sfx/Emotes/Yoosung/yoosung_wow.wav',
                    '{image=yoosung yahoo}': 'sfx/Emotes/Yoosung/yoosung_yahoo.wav',
                    
                    '{image=zen angry}': 'sfx/Emotes/Zen/zen_angry.wav',
                    '{image=zen happy}': 'sfx/Emotes/Zen/zen_happy.wav',
                    '{image=zen hmm}': 'sfx/Emotes/Zen/zen_hmm.wav',
                    '{image=zen oyeah}': 'sfx/Emotes/Zen/zen_oyeah.wav',
                    '{image=zen question}': 'sfx/Emotes/Zen/zen_question.wav',
                    '{image=zen sad}': 'sfx/Emotes/Zen/zen_sad.wav',
                    '{image=zen shock}': 'sfx/Emotes/Zen/zen_shock.wav',
                    '{image=zen well}': 'sfx/Emotes/Zen/zen_well.wav',
                    '{image=zen wink}': 'sfx/Emotes/Zen/zen_wink.wav'
                    }

default jaehee_emotes = ['{image=jaehee angry}', 
                    '{image=jaehee happy}',
                    '{image=jaehee hehe}', 
                    '{image=jaehee huff}', 
                    '{image=jaehee oops}',
                    '{image=jaehee question}',
                    '{image=jaehee sad}',
                    '{image=jaehee well}',
                    '{image=jaehee wow}'] 
                    
default jumin_emotes = [ '{image=jumin angry}',
                    '{image=jumin sad}', 
                    '{image=jumin smile}',
                    '{image=jumin well}']
                    
default rika_emotes = ['{image=rika happy}','{image=rika pout}','{image=rika cry}']
                    
default ray_emotes = ['{image=ray cry}', 
                    '{image=ray happy}', 
                    '{image=ray huff}', 
                    '{image=ray question}', 
                    '{image=ray smile}', 
                    '{image=ray well}', 
                    '{image=ray wink}',
                    
                    '{image=saeran2 cry}', 
                    '{image=saeran2 happy}', 
                    '{image=saeran2 huff}', 
                    '{image=saeran2 question}', 
                    '{image=saeran2 smile}', 
                    '{image=saeran2 well}', 
                    '{image=saeran2 wink}']
                    
default saeran_emotes = ['{image=saeran expecting}', 
                    '{image=saeran happy}', 
                    '{image=saeran questioning}', 
                    '{image=saeran well}']                  
                    
default seven_emotes = ['{image=seven cry}', 
                    '{image=seven huff}', 
                    '{image=seven khee}', 
                    '{image=seven love}', 
                    '{image=seven question}', 
                    '{image=seven what}', 
                    '{image=seven wow}', 
                    '{image=seven yahoo}', 
                    '{image=seven yoohoo}']

default v_emotes = ['{image=v shock}', 
                    '{image=v smile}',
                    '{image=v well}',
                    '{image=v wink}']
                    
default yoosung_emotes = ['{image=yoosung angry}',
                    '{image=yoosung cry}',
                    '{image=yoosung happy}',
                    '{image=yoosung huff}',
                    '{image=yoosung puff}',
                    '{image=yoosung question}',
                    '{image=yoosung thankyou}',
                    '{image=yoosung what}',
                    '{image=yoosung wow}',
                    '{image=yoosung yahoo}']
                    
default zen_emotes = ['{image=zen angry}',
                    '{image=zen happy}',
                    '{image=zen hmm}',
                    '{image=zen oyeah}',
                    '{image=zen question}',
                    '{image=zen sad}',
                    '{image=zen shock}',
                    '{image=zen well}',
                    '{image=zen wink}']
                    
default all_emotes = jaehee_emotes + jumin_emotes + rika_emotes + ray_emotes + seven_emotes + saeran_emotes + v_emotes + yoosung_emotes + zen_emotes

# ******** JAEHEE ******************

image jaehee angry:
    "Gifs/Jaehee/emo_jaehee_angry1.png"
    0.5
    "Gifs/Jaehee/emo_jaehee_angry2.png"
    0.5
    repeat
    
image jaehee happy:
    "Gifs/Jaehee/emo_jaehee_happy1.png"
    0.5
    "Gifs/Jaehee/emo_jaehee_happy2.png"
    0.5
    repeat
    
image jaehee hehe:
    "Gifs/Jaehee/emo_jaehee_hehe1.png"
    0.5
    "Gifs/Jaehee/emo_jaehee_hehe2.png"
    0.5
    repeat
    
image jaehee huff:
    "Gifs/Jaehee/emo_jaehee_huff1.png"
    0.5
    "Gifs/Jaehee/emo_jaehee_huff2.png"
    0.5
    repeat
    
image jaehee oops:
    "Gifs/Jaehee/emo_jaehee_oops1.png"
    0.5
    "Gifs/Jaehee/emo_jaehee_oops2.png"
    0.5
    repeat
    
image jaehee question:
    "Gifs/Jaehee/emo_jaehee_question1.png"
    0.5
    "Gifs/Jaehee/emo_jaehee_question2.png"
    0.5
    repeat
    
image jaehee sad:
    "Gifs/Jaehee/emo_jaehee_sad1.png"
    0.5
    "Gifs/Jaehee/emo_jaehee_sad2.png"
    0.5
    repeat
    
image jaehee well:
    "Gifs/Jaehee/emo_jaehee_well1.png"
    0.5
    "Gifs/Jaehee/emo_jaehee_well2.png"
    0.5
    repeat
    
image jaehee wow:
    "Gifs/Jaehee/emo_jaehee_wow1.png"
    0.5
    "Gifs/Jaehee/emo_jaehee_wow2.png"
    0.5
    repeat


# ******** JUMIN ******************

image jumin angry:
    "Gifs/Jumin/emo_jumin_angry1.png"
    0.5
    "Gifs/Jumin/emo_jumin_angry2.png"
    0.5
    repeat
    
image jumin sad:
    "Gifs/Jumin/emo_jumin_sad1.png"
    0.5
    "Gifs/Jumin/emo_jumin_sad2.png"
    0.5
    repeat
    
image jumin smile:
    "Gifs/Jumin/emo_jumin_smile1.png"
    0.5
    "Gifs/Jumin/emo_jumin_smile2.png"
    0.5
    repeat
    
image jumin well:
    "Gifs/Jumin/emo_jumin_well1.png"
    0.5
    "Gifs/Jumin/emo_jumin_well2.png"
    0.5
    repeat
    
    
# ******** RAY ******************

image ray cry:
    "Gifs/Ray/emo_ray_cry1.png"
    0.5
    "Gifs/Ray/emo_ray_cry2.png"
    0.5
    repeat    
    
image ray happy:
    "Gifs/Ray/emo_ray_happy1.png"
    0.5
    "Gifs/Ray/emo_ray_happy2.png"
    0.5
    repeat   
    
image ray huff:
    "Gifs/Ray/emo_ray_huff1.png"
    0.5
    "Gifs/Ray/emo_ray_huff2.png"
    0.5
    repeat   
    
image ray question:
    "Gifs/Ray/emo_ray_question1.png"
    0.5
    "Gifs/Ray/emo_ray_question2.png"
    0.5
    repeat   
    
image ray smile:
    "Gifs/Ray/emo_ray_smile1.png"
    0.5
    "Gifs/Ray/emo_ray_smile2.png"
    0.5
    repeat   
    
image ray well:
    "Gifs/Ray/emo_ray_well1.png"
    0.5
    "Gifs/Ray/emo_ray_well2.png"
    0.5
    repeat   
    
image ray wink:
    "Gifs/Ray/emo_ray_wink1.png"
    0.5
    "Gifs/Ray/emo_ray_wink2.png"
    0.5
    repeat   
    
# ******** RIKA ******************
# Credit to Sakekobomb for the emotes
# Used with permission

image rika happy:
    "Gifs/Rika/emo_rika_happy1.png"
    0.5
    "Gifs/Rika/emo_rika_happy2.png"
    0.5
    repeat   

image rika pout:
    "Gifs/Rika/emo_rika_pout1.png"
    0.5
    "Gifs/Rika/emo_rika_pout2.png"
    0.5
    repeat  
    
image rika cry:
    "Gifs/Rika/emo_rika_cry1.png"
    0.5
    "Gifs/Rika/emo_rika_cry2.png"
    0.5
    repeat  
    
    
# ******** SAERAN ******************

image saeran expecting:
    "Gifs/Saeran/emo_saeran_expecting1.png"
    0.5
    "Gifs/Saeran/emo_saeran_expecting2.png"
    0.5
    repeat  
    
image saeran happy:
    "Gifs/Saeran/emo_saeran_happy1.png"
    0.5
    "Gifs/Saeran/emo_saeran_happy2.png"
    0.5
    repeat  
    
image saeran questioning:
    "Gifs/Saeran/emo_saeran_questioning1.png"
    0.5
    "Gifs/Saeran/emo_saeran_questioning2.png"
    0.5
    repeat  
    
image saeran well:
    "Gifs/Saeran/emo_saeran_well1.png"
    0.5
    "Gifs/Saeran/emo_saeran_well2.png"
    0.5
    repeat  

# ******** SAERAN (Sweater) ******************
# ** Credit to its-a-me-haruhi.tumblr.com for 
#     the recolours

image saeran2 cry:
    "Gifs/Saeran2/emo_sae_cry1.png"
    0.5
    "Gifs/Saeran2/emo_sae_cry2.png"
    0.5
    repeat    
    
image saeran2 happy:
    "Gifs/Saeran2/emo_sae_happy1.png"
    0.5
    "Gifs/Saeran2/emo_sae_happy2.png"
    0.5
    repeat   
    
image saeran2 huff:
    "Gifs/Saeran2/emo_sae_huff1.png"
    0.5
    "Gifs/Saeran2/emo_sae_huff2.png"
    0.5
    repeat   
    
image saeran2 question:
    "Gifs/Saeran2/emo_sae_question1.png"
    0.5
    "Gifs/Saeran2/emo_sae_question2.png"
    0.5
    repeat   
    
image saeran2 smile:
    "Gifs/Saeran2/emo_sae_smile1.png"
    0.5
    "Gifs/Saeran2/emo_sae_smile2.png"
    0.5
    repeat   
    
image saeran2 well:
    "Gifs/Saeran2/emo_sae_well1.png"
    0.5
    "Gifs/Saeran2/emo_sae_well2.png"
    0.5
    repeat   
    
image saeran2 wink:
    "Gifs/Saeran2/emo_sae_wink1.png"
    0.5
    "Gifs/Saeran2/emo_sae_wink2.png"
    0.5
    repeat 
    
# ******** SEVEN ******************

image seven cry:
    "Gifs/Seven/emo_seven_cry1.png"
    0.5
    "Gifs/Seven/emo_seven_cry2.png"
    0.5
    repeat  
    
image seven huff:
    "Gifs/Seven/emo_seven_huff1.png"
    0.5
    "Gifs/Seven/emo_seven_huff2.png"
    0.5
    repeat  
    
image seven khee:
    "Gifs/Seven/emo_seven_khee1.png"
    0.5
    "Gifs/Seven/emo_seven_khee2.png"
    0.5    
    repeat  
    
image seven love:
    "Gifs/Seven/emo_seven_love1.png"
    0.5
    "Gifs/Seven/emo_seven_love2.png"
    0.5
    repeat  
    
image seven question:
    "Gifs/Seven/emo_seven_question1.png"
    0.5
    "Gifs/Seven/emo_seven_question2.png"
    0.5
    repeat  
    
image seven what:
    "Gifs/Seven/emo_seven_what1.png"
    0.5
    "Gifs/Seven/emo_seven_what2.png"
    0.5
    repeat  
    
image seven wow:
    "Gifs/Seven/emo_seven_wow1.png"
    0.5
    "Gifs/Seven/emo_seven_wow2.png"
    0.5
    repeat  
    
image seven yahoo:
    "Gifs/Seven/emo_seven_yahoo1.png"
    0.5
    "Gifs/Seven/emo_seven_yahoo2.png"
    0.5
    repeat  
    
image seven yoohoo:
    "Gifs/Seven/emo_seven_yoohoo1.png"
    0.5
    "Gifs/Seven/emo_seven_yoohoo2.png"
    0.5
    repeat  


# ************* V ******************

image v shock:
    "Gifs/V/emo_v_shock1.png"
    0.5
    "Gifs/V/emo_v_shock2.png"
    0.5
    repeat  
    
image v smile:
    "Gifs/V/emo_v_smile1.png"
    0.5
    "Gifs/V/emo_v_smile2.png"
    0.5
    repeat  
    
image v well:
    "Gifs/V/emo_v_well1.png"
    0.5
    "Gifs/V/emo_v_well2.png"
    0.5
    repeat  
    
image v wink:
    "Gifs/V/emo_v_wink1.png"
    0.5
    "Gifs/V/emo_v_wink2.png"
    0.5
    repeat  

    
# ********* YOOSUNG ******************

image yoosung angry:
    "Gifs/Yoosung/emo_yoosung_angry1.png"
    0.5
    "Gifs/Yoosung/emo_yoosung_angry2.png"
    0.5
    repeat  
    
image yoosung cry:
    "Gifs/Yoosung/emo_yoosung_cry1.png"
    0.5
    "Gifs/Yoosung/emo_yoosung_cry2.png"
    0.5
    repeat  
    
image yoosung happy:
    "Gifs/Yoosung/emo_yoosung_happy1.png"
    0.5
    "Gifs/Yoosung/emo_yoosung_happy2.png"
    0.5
    repeat  
    
image yoosung huff:
    "Gifs/Yoosung/emo_yoosung_huff1.png"
    0.5
    "Gifs/Yoosung/emo_yoosung_huff2.png"
    0.5
    repeat  
    
image yoosung puff:
    "Gifs/Yoosung/emo_yoosung_puff1.png"
    0.5
    "Gifs/Yoosung/emo_yoosung_puff2.png"
    0.5
    repeat  
    
image yoosung question:
    "Gifs/Yoosung/emo_yoosung_question1.png"
    0.5
    "Gifs/Yoosung/emo_yoosung_question2.png"
    0.5
    repeat  
    
image yoosung thankyou:
    "Gifs/Yoosung/emo_yoosung_thankyou1.png"
    0.5
    "Gifs/Yoosung/emo_yoosung_thankyou2.png"
    0.5
    repeat  
    
image yoosung what:
    "Gifs/Yoosung/emo_yoosung_what1.png"
    0.5
    "Gifs/Yoosung/emo_yoosung_what2.png"
    0.5
    repeat  
    
image yoosung wow:
    "Gifs/Yoosung/emo_yoosung_wow1.png"
    0.5
    "Gifs/Yoosung/emo_yoosung_wow2.png"
    0.5
    repeat  
    
image yoosung yahoo:
    "Gifs/Yoosung/emo_yoosung_yahoo1.png"
    0.5
    "Gifs/Yoosung/emo_yoosung_yahoo2.png"
    0.5
    repeat  

    
# ************ ZEN ******************

image zen angry:
    "Gifs/Zen/emo_zen_angry1.png"
    0.5
    "Gifs/Zen/emo_zen_angry2.png"
    0.5
    repeat 

image zen happy:
    "Gifs/Zen/emo_zen_happy1.png"
    0.5
    "Gifs/Zen/emo_zen_happy2.png"
    0.5
    repeat 
    
image zen hmm:
    "Gifs/Zen/emo_zen_hmm1.png"
    0.5
    "Gifs/Zen/emo_zen_hmm2.png"
    0.5
    repeat 
    
image zen oyeah:
    "Gifs/Zen/emo_zen_oyeah1.png"
    0.5
    "Gifs/Zen/emo_zen_oyeah2.png"
    0.5
    repeat 
    
image zen question:
    "Gifs/Zen/emo_zen_q1.png"
    0.5
    "Gifs/Zen/emo_zen_q2.png"
    0.5
    repeat 
    
image zen sad:
    "Gifs/Zen/emo_zen_sad1.png"
    0.5
    "Gifs/Zen/emo_zen_sad2.png"
    0.5
    repeat 
    
image zen shock:
    "Gifs/Zen/emo_zen_shock1.png"
    0.5
    "Gifs/Zen/emo_zen_shock2.png"
    0.5
    repeat
    
image zen well:
    "Gifs/Zen/emo_zen_well1.png"
    0.5
    "Gifs/Zen/emo_zen_well2.png"
    0.5
    repeat
    
image zen wink:
    "Gifs/Zen/emo_zen_wink1.png"
    0.5
    "Gifs/Zen/emo_zen_wink2.png"
    0.5
    repeat
 
