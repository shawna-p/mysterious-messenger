##****************************
## Chatroom Characters
##****************************

## Chatroom character declarations
## Format is: 
##  name - nickname for the chatrooms
##  file_id - short form appended to file names like speech bubbles
##  prof_pic - profile pic (110x110)
##  participant_pic - pic that shows they're present in a chatroom
##  heart_color - hex number of their heart colour
##  emoji_list - used for chatroom creation (can be left False if you don't need it/don't know what to do with it)
##  cover_pic/status  - as stated
##  voicemail - generally set at the end of a chatroom, not during definition time

default s = Chat("707", 's', 'Profile Pics/Seven/sev-default.png', 'Profile Pics/s_chat.png', "#ff2626", seven_emotes, "Cover Photos/profile_cover_photo.png", "707's status")
default y = Chat("Yoosung★", 'y', 'Profile Pics/Yoosung/yoo-default.png', 'Profile Pics/y_chat.png', "#31ff26", yoosung_emotes, "Cover Photos/profile_cover_photo.png", "Yoosung's status")
default m = Chat("MC", 'm', 'Profile Pics/MC/MC-1.png')
default ja = Chat("Jaehee Kang", 'ja', 'Profile Pics/Jaehee/ja-default.png', 'Profile Pics/ja_chat.png', "#d0b741", jaehee_emotes, "Cover Photos/profile_cover_photo.png", "Jaehee's status")
default ju = Chat("Jumin Han", 'ju', 'Profile Pics/Jumin/ju-default.png', 'Profile Pics/ju_chat.png', "#a59aef", jumin_emotes, "Cover Photos/profile_cover_photo.png", "Jumin's status")
default z = Chat("ZEN", 'z', 'Profile Pics/Zen/zen-default.png', 'Profile Pics/z_chat.png', "#c9c9c9", zen_emotes, "Cover Photos/profile_cover_photo.png", "Zen's status")
default ri = Chat("Rika", 'ri', 'Profile Pics/Rika/rika-default.png', 'Profile Pics/ri_chat.png', "#fcef5a", rika_emotes, "Cover Photos/profile_cover_photo.png", "Rika's status")
default r = Chat("Ray", 'r', 'Profile Pics/Ray/ray-default.png', 'Profile Pics/r_chat.png', "#b81d7b", ray_emotes, "Cover Photos/profile_cover_photo.png", "Ray's status")
default sa = Chat("Saeran", "sa", 'Profile Pics/Saeran/sae-1.png', 'Profile Pics/sa_chat.png', "#b81d7b", saeran_emotes, "Cover Photos/profile_cover_photo.png", "Saeran's status")
default u = Chat("Unknown", "u", 'Profile Pics/Unknown/Unknown-1.png', 'Profile Pics/u_chat.png', "#ffffff")
default v = Chat("V", 'v', 'Profile Pics/V/V-default.png', 'Profile Pics/v_chat.png', "#50b2bc", v_emotes, "Cover Photos/profile_cover_photo.png", "V's status")
   
# These are special 'characters' for additional features
define msg = Chat("msg")
define filler = Chat("filler")
define answer = Chat('answer', 'delete')
define chat_pause = Chat('pause', 'delete')

# You'll want to add a new character to this list so they show up
# in things like the profiles at the top of the screen
default character_list = [ju, z, s, y, ja, v, m, r, ri]
                        
                        
# ****************************
# Phone Call Characters
# ****************************

# These are separate from the characters above since they display more like VN mode
# You won't actually see their name in-game. For most purposes, you can just copy any character
# besides m_phone and replace the name with the name you want
# The main difference is in the voice tags, so that if you mute a character you won't hear their
# voice during phone calls or VN mode
# For ease of remembering, Phone Call characters are just their Chat variables + '_phone' e.g.
#  ja -> ja_phone

define ja_phone = Character("Jaehee Kang", what_font= "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf", 
                            what_color="#fff", what_xalign=0.5, what_yalign=0.5, what_text_align=0.5, voice_tag="jaehee_voice")
define ju_phone = Character("Jumin Han", what_font= "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf", 
                            what_color="#fff", what_xalign=0.5, what_yalign=0.5, what_text_align=0.5, voice_tag="jumin_voice")
define s_phone = Character("707", what_font= "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf", 
                            what_color="#fff", what_xalign=0.5, what_yalign=0.5, what_text_align=0.5, voice_tag="seven_voice")
define sa_phone = Character("Saeran", what_font= "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf", 
                            what_color="#fff", what_xalign=0.5, what_yalign=0.5, what_text_align=0.5, voice_tag="saeran_voice")
define r_phone = Character("Ray", what_font= "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf", 
                            what_color="#fff", what_xalign=0.5, what_yalign=0.5, what_text_align=0.5, voice_tag="saeran_voice")
define ri_phone = Character("Rika", what_font= "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf", 
                            what_color="#fff", what_xalign=0.5, what_yalign=0.5, what_text_align=0.5, voice_tag="rika_voice")
define y_phone = Character("Yoosung★", what_font= "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf", 
                            what_color="#fff", what_xalign=0.5, what_yalign=0.5, what_text_align=0.5, voice_tag="yoosung_voice")
define v_phone = Character("V", what_font= "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf", 
                            what_color="#fff", what_xalign=0.5, what_yalign=0.5, what_text_align=0.5, voice_tag="v_voice")
define u_phone = Character("Unknown", what_font= "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf", 
                            what_color="#fff", what_xalign=0.5, what_yalign=0.5, what_text_align=0.5, voice_tag="saeran_voice")
define z_phone = Character("Zen", what_font= "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf", 
                            what_color="#fff", what_xalign=0.5, what_yalign=0.5, what_text_align=0.5, voice_tag="zen_voice")
define m_phone = Character("MC", what_font= "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf", 
                            what_color="#a6a6a6", what_xalign=0.5, what_yalign=0.5, what_text_align=0.5)
define vmail_phone = Character('', what_font= "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf", 
                            what_color="#fff", what_xalign=0.5, what_yalign=0.5, what_text_align=0.5, voice_tag="other_voice")
                            
# ****************************
# Text Messages
# ****************************         

# If you want a character to be able to send messages, define a
# Text_Message object with their Chat variable in the lists below                 
default text_messages = [Text_Message(ja, []),
                        Text_Message(ju, []),
                        Text_Message(r, []),
                        Text_Message(ri, []),
                        Text_Message(s, []),
                        Text_Message(v, []),
                        Text_Message(y, []),
                        Text_Message(z, []),
                        
                        Text_Message(u, []),
                        Text_Message(sa, [])
                        ]
default text_queue = [Text_Message(ja, []),
                        Text_Message(ju, []),
                        Text_Message(r, []),
                        Text_Message(ri, []),
                        Text_Message(s, []),
                        Text_Message(v, []),
                        Text_Message(y, []),
                        Text_Message(z, []),
                        
                        Text_Message(u, []),
                        Text_Message(sa, [])
                        ]
                        
# ****************************
# Visual Novel Mode
# ****************************                        
## CHARACTER DEFINITIONS ****************

# Again, you can mostly just copy-paste a character definition from here and change the window_background
# and voice_tag as appropriate
# For ease of remembering, VN characters are just their Chat variables + "_vn" e.g. s -> s_vn
# I've also changed the who_color from MysMe's #fff5ca to the background of the characters' speech bubbles

define ja_vn = Character("Jaehee", what_font="00 fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf", 
                            what_color="#ffffff", window_background="VN Mode/Chat Bubbles/vnmode_4.png",
                            who_color="#fff5eb", who_size=40, voice_tag="jaehee_voice", image="jaehee vn")
define ju_vn = Character("Jumin", what_font="00 fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf", 
                            what_color="#ffffff", window_background="VN Mode/Chat Bubbles/vnmode_0.png",
                            who_color="#d2e6f7", who_size=40, voice_tag="jumin_voice", image="jumin")
define r_vn = Character("Ray", what_font="00 fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf", 
                            what_color="#ffffff", window_background="VN Mode/Chat Bubbles/vnmode_9.png",
                            who_color="#f2ebfd", who_size=40, voice_tag="saeran_voice", image="saeran vn")
define ri_vn = Character("Rika", what_font="00 fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf", 
                            what_color="#ffffff", window_background="VN Mode/Chat Bubbles/vnmode_7.png",
                            who_color="#fff9db", who_size=40, voice_tag="rika_voice", image="rika vn")
define s_vn = Character("707", what_font="00 fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf", 
                            what_color="#ffffff", window_background="VN Mode/Chat Bubbles/vnmode_2.png",
                            who_color="#fff1f1", who_size=40, voice_tag="seven_voice", image="seven")
define sa_vn = Character("Saeran", what_font="00 fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf", 
                            what_color="#ffffff", window_background="VN Mode/Chat Bubbles/vnmode_8.png",
                            who_color="#f2ebfd", who_size=40, voice_tag="saeran_voice", image="saeran vn")
define u_vn = Character("???",what_font="00 fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf", 
                            what_color="#ffffff", window_background="VN Mode/Chat Bubbles/vnmode_9.png",
                            who_color="#f2ebfd", who_size=40, voice_tag="saeran_voice", image="saeran vn")
define v_vn = Character("V", what_font="00 fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf", 
                            what_color="#ffffff", window_background="VN Mode/Chat Bubbles/vnmode_5.png",
                            who_color="#cbfcfc", who_size=40, voice_tag="v_voice", image="v vn")
define y_vn = Character("Yoosung", what_font="00 fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf", 
                            what_color="#ffffff", window_background="VN Mode/Chat Bubbles/vnmode_3.png",
                            who_color="#effff3", who_size=40, voice_tag="yoosung_voice", image="yoosung vn")
define z_vn = Character("Zen", what_font="00 fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf", 
                            what_color="#ffffff", window_background="VN Mode/Chat Bubbles/vnmode_1.png",
                            who_color="#d8e9f9", who_size=40, voice_tag="zen_voice", image="zen")
                            
## Note: The MC's name will show up in VN mode in this program. If you'd like it to be blank,
## just replace "[name]" with None
define m_vn = Character("[name]", what_font="00 fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf", 
                            what_color="#ffffff", window_background="VN Mode/Chat Bubbles/vnmode_9.png",
                            who_color="#ffffed", who_size=40)
## This is the 'generic' template character -- if you want a side character like Echo Girl, copy this 
## character and replace None with their name.
define narrator = Character(None, what_font="00 fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf", 
                            what_color="#ffffff", window_background="VN Mode/Chat Bubbles/vnmode_9.png",
                            who_color="#fff5ca", who_size=40, voice_tag="other_voice")
                            
## *************************************
## Character VN Expressions Cheat Sheet
## *************************************

## ********* MAIN CHARACTERS *********

## Jaehee:
# WITH OR WITHOUT GLASSES: happy, sad, neutral (default), thinking, worried
# WITH GLASSES: angry, sparkle, serious, surprised
# OUTFITS: normal (default), arm, party, dress, apron

## Jumin:
# FRONT: happy, upset, blush, neutral (default), surprised, angry, sad, unsure, thinking
# FRONT OUTFITS: normal (default), arm, party
# SIDE: happy, upset, blush, neutral (default), surprised, angry, thinking, worried
# SIDE OUTFITS: normal (default), suit

## Rika:
# EXPRESSIONS: happy, sad, neutral (default), thinking, worried, dark, angry, sob, crazy
# OUTFITS: normal (default), savior, dress
# ACCESSORIES: mask

## Seven:
# FRONT: happy, blush, neutral (default), surprised, serious, thinking, sad, worried,
#        dark, angry, hurt
# FRONT OUTFITS: normal (default), arm, party
# SIDE: happy, concern, surprised, thinking, sad, neutral (default), dark, angry, worried
# SIDE OUTFITS: normal (default), arm, suit

## Saeran:
# WITH OR WITHOUT MASK: happy, smile, neutral (default), angry, thinking, tense, creepy
# WITHOUT MASK: cry, blush, sob, teary, nervous, sad, worried, distant
# OUTFITS: unknown, mask, ray (default), saeran, suit

## V:
# FRONT: neutral (default), happy, angry, worried, thinking, talking, surprised,
#        tense, sweating, sad, upset, concerned, regret, unsure, afraid
# FRONT OUTFITS: normal (default), arm, hair_normal, hair_arm, mint_eye
# ACCESSORIES **mint_eye outfit only**: hood_up, hood_down (default)
# SIDE, WITH OR WITHOUT GLASSES: happy, angry, neutral (default), surprised, thinking,
#        worried, sweat, shock, afraid, blush, sad, unsure
# SIDE OUTFITS: normal (default), short_hair, long_hair

## Yoosung:
# WITH OR WITHOUT BANDAGE: happy, neutral (default), thinking
# WITH OR WITHOUT GLASSES: happy, neutral (default), thinking, surprised, sparkle, grin
# WITHOUT GLASSES OR BANDAGE: angry, sad, dark, tired, upset
# OUTFITS: normal (default), arm, sweater, suit, party, bandage

## Zen:
# FRONT: happy, angry, blush, wink, neutral (default), surprised, thinking,
#        worried, oh, upset
# FRONT OUTFITS: arm, party, normal (default)
# SIDE: happy, angry, blush, wink, neutral (default), surprised, thinking, worried, upset
# SIDE OUTFITS: normal (default), suit


## ********* SIDE CHARACTERS *********

## Bodyguards:
# FRONT: neutral (default), thinking, stressed
# SIDE: neutral (default), thinking, stressed

## Chairman Han:
# EXPRESSIONS: happy, thinking, neutral (default), stressed

## Echo Girl:
# EXPRESSIONS: neutral (default), happy, angry, smile, surprised

## Glam Choi:
# EXPRESSIONS: happy, smirk, thinking, neutral (default), stressed, worried

## Prime Minister:
# (He only has one expression, the default one)

## Sarah Choi:
# EXPRESSIONS: happy, excited, smirk, neutral (default), stressed, sad

## Vanderwood:
# EXPRESSIONS: neutral (default), unamused, unsure, determined, ouch, angry


## ***********************************
## Character Image Declarations
## ***********************************

## ********* MAIN CHARACTERS *********

## TO DECLARE YOUR OWN CHARACTER:
# For starters, I would really recommend keeping accessories like glasses separate
# from facial expressions, so you can avoid doing what I've done here, which is have
# two separate 'glasses' and 'regular' layeredimage variants. That aside, characters
# are generally declared with a body and face group, and sometimes have a 'yoffset' value
# that simply puts their sprite lower down on the screen (so the characters have the 
# correct relative heights to one another). Other than that, everything is the same as
# you'll find in Ren'Py's layeredimage documentation

## ****************************
## Jaehee
## ****************************
layeredimage jaehee vn:
    yoffset 70
    
    group body:
        attribute normal default "VN Mode/Jaehee/jaehee_body_0.png"
        attribute arm "VN Mode/Jaehee/jaehee_body_1.png"
        attribute party "VN Mode/Jaehee/jaehee_body_2.png"
        attribute dress "VN Mode/Jaehee/jaehee_body_3.png"
        attribute apron "VN Mode/Jaehee/jaehee_body_4.png"
        
    group face:
        attribute happy "VN Mode/Jaehee/jaehee_face_1.png" align(0.298, 0.108)
        attribute sad "VN Mode/Jaehee/jaehee_face_3.png" align(0.298, 0.108)
        attribute neutral default "VN Mode/Jaehee/jaehee_face_5.png" align(0.298, 0.108)
        attribute thinking "VN Mode/Jaehee/jaehee_face_7.png" align(0.298, 0.108)
        attribute worried "VN Mode/Jaehee/jaehee_face_9.png" align(0.298, 0.108)
        
layeredimage jaehee vn glasses:
    yoffset 70
    
    group body:
        attribute normal default "VN Mode/Jaehee/jaehee_body_0.png"
        attribute arm "VN Mode/Jaehee/jaehee_body_1.png"
        attribute party "VN Mode/Jaehee/jaehee_body_2.png"
        attribute dress "VN Mode/Jaehee/jaehee_body_3.png"
        attribute apron "VN Mode/Jaehee/jaehee_body_4.png"
        
    group face:
        attribute happy "VN Mode/Jaehee/jaehee_face_0.png" align(0.299, 0.108)
        attribute angry "VN Mode/Jaehee/jaehee_face_2.png" align(0.299, 0.108)
        attribute sad "VN Mode/Jaehee/jaehee_face_4.png" align(0.299, 0.108)
        attribute sparkle "VN Mode/Jaehee/jaehee_face_6.png" align(0.299, 0.108)
        attribute neutral default "VN Mode/Jaehee/jaehee_face_8.png" align(0.299, 0.108)
        attribute thinking "VN Mode/Jaehee/jaehee_face_10.png" align(0.299, 0.108)
        attribute serious "VN Mode/Jaehee/jaehee_face_11.png" align(0.299, 0.108)
        attribute worried "VN Mode/Jaehee/jaehee_face_12.png" align(0.299, 0.108)
        attribute surprised "VN Mode/Jaehee/jaehee_face_13.png" align(0.299, 0.108)
        
        
## ****************************
## Jumin
## ****************************
layeredimage jumin front:
    yoffset 30

    group body:
        attribute normal default "VN Mode/Jumin/jumin_body_0.png"
        attribute arm "VN Mode/Jumin/jumin_body_1.png"
        attribute party "VN Mode/Jumin/jumin_body_2.png"
        
    group face:
        attribute happy "VN Mode/Jumin/jumin_face_0.png" align(0.326, 0.121)
        attribute upset "VN Mode/Jumin/jumin_face_1.png" align(0.326, 0.121)
        attribute blush "VN Mode/Jumin/jumin_face_2.png" align(0.326, 0.121)
        attribute neutral default "VN Mode/Jumin/jumin_face_3.png" align(0.326, 0.121)
        attribute surprised "VN Mode/Jumin/jumin_face_4.png" align(0.326, 0.121)
        attribute angry "VN Mode/Jumin/jumin_face_5.png" align(0.326, 0.121)
        attribute sad "VN Mode/Jumin/jumin_face_6.png" align(0.326, 0.121)
        attribute unsure "VN Mode/Jumin/jumin_face_7.png" align(0.326, 0.121)
        attribute thinking "VN Mode/Jumin/jumin_face_8.png" align(0.326, 0.121)
        
layeredimage jumin side:

    yoffset 15
    
    group body:
        attribute normal default "VN Mode/Jumin/jumin_sidebody_0b.png"
        attribute suit "VN Mode/Jumin/jumin_sidebody_1.png."
            
    group face:
        attribute happy "VN Mode/Jumin/jumin_sideface_0.png" align(0.177, 0.097)
        attribute upset "VN Mode/Jumin/jumin_sideface_1.png" align(0.172, 0.094)
        attribute blush "VN Mode/Jumin/jumin_sideface_2.png" align(0.177, 0.097)
        attribute neutral default "VN Mode/Jumin/jumin_sideface_3.png" align(0.177, 0.097)
        attribute surprised "VN Mode/Jumin/jumin_sideface_4.png" align(0.177, 0.097)
        attribute angry "VN Mode/Jumin/jumin_sideface_5.png" align(0.177, 0.097)
        attribute thinking "VN Mode/Jumin/jumin_sideface_6.png" align(0.177, 0.097)
        attribute worried "VN Mode/Jumin/jumin_sideface_7.png" align(0.177, 0.097)
        
        
## ****************************
## Rika
## ****************************
layeredimage rika vn:
    yoffset 80

    group body:
        attribute normal default "VN Mode/Rika/rika01_body_0.png"
        attribute savior "VN Mode/Rika/rika01_body_1.png"
        attribute dress "VN Mode/Rika/rika01_body_2.png"
        
    group face:
        attribute happy "VN Mode/Rika/rika01_face_0.png" align(0.21, 0.097)
        attribute sad "VN Mode/Rika/rika01_face_1.png" align(0.21, 0.097)
        attribute neutral default "VN Mode/Rika/rika01_face_2.png" align(0.21, 0.097)
        attribute thinking "VN Mode/Rika/rika01_face_3.png" align(0.21, 0.097)
        attribute worried "VN Mode/Rika/rika01_face_4.png" align(0.21, 0.097)
        attribute dark "VN Mode/Rika/rika01_face_5.png" align(0.21, 0.097)
        attribute angry "VN Mode/Rika/rika01_face_6.png" align(0.21, 0.097)
        attribute sob "VN Mode/Rika/rika01_face_7.png" align(0.21, 0.097)
        attribute crazy "VN Mode/Rika/rika01_face_8.png" align(0.21, 0.097)
        
    group head:
        attribute mask "VN Mode/Rika/rika01_head_0.png" align(0.172, 0.05)
        
        
## ****************************
## Seven
## ****************************
layeredimage seven front:
    yoffset 150

    group body:
        attribute normal default "VN Mode/707/seven_body_0.png"
        attribute arm "VN Mode/707/seven_body_1.png"
        attribute party "VN Mode/707/seven_party_0.png"
            
    group face:
        attribute happy "VN Mode/707/seven_face_0.png" align(0.383, 0.139)
        attribute blush "VN Mode/707/seven_face_1.png" align(0.383, 0.139)
        attribute neutral default "VN Mode/707/seven_face_2.png" align(0.383, 0.139)
        attribute surprised "VN Mode/707/seven_face_3.png" align(0.383, 0.139)
        attribute serious "VN Mode/707/seven_face_4.png" align(0.383, 0.139)
        attribute thinking "VN Mode/707/seven_face_5.png" align(0.383, 0.139)
        attribute sad "VN Mode/707/seven_face_6.png" align(0.383, 0.139)
        attribute worried "VN Mode/707/seven_face_7.png" align(0.383, 0.139)
        attribute dark "VN Mode/707/seven_face_8.png" align(0.383, 0.139)
        attribute angry "VN Mode/707/seven_face_9.png" align(0.383, 0.139)
        attribute hurt "VN Mode/707/seven_face_10.png" align(0.383, 0.139)
        
layeredimage seven side:
    yoffset 160
    
    group body:
        attribute normal default "VN Mode/707/seven_sidebody_0.png"
        attribute arm "VN Mode/707/seven_sidebody_1.png"
        attribute suit "VN Mode/707/seven_valentines_0.png"
        
    group face:
        attribute happy "VN Mode/707/seven_sideface_0.png" align(0.435, 0.13)
        attribute concern "VN Mode/707/seven_sideface_1.png" align(0.435, 0.13)
        attribute surprised "VN Mode/707/seven_sideface_2.png" align(0.435, 0.13)
        attribute thinking  "VN Mode/707/seven_sideface_3.png" align(0.435, 0.13)
        attribute sad "VN Mode/707/seven_sideface_4.png" align(0.435, 0.13)
        attribute neutral default "VN Mode/707/seven_sideface_5.png" align(0.435, 0.13)
        attribute dark "VN Mode/707/seven_sideface_6.png" align(0.435, 0.13)
        attribute angry "VN Mode/707/seven_sideface_7.png" align(0.435, 0.13)
        attribute worried "VN Mode/707/seven_sideface_8.png" align(0.435, 0.13)
    
    
## ****************************
## Saeran
## ****************************
layeredimage saeran vn:   
    yoffset 170

    group body:
        attribute unknown "VN Mode/Unknown/unknown_body_unknown.png"
        attribute mask "VN Mode/Unknown/unknown_body_mask.png"
        attribute ray default "VN Mode/Unknown/unknown_body_ray.png"
        attribute saeran "VN Mode/Unknown/unknown_body_saeran.png"
        attribute suit "VN Mode/Unknown/unknown_body_suit.png"
    
    group face:
        if_not "mask"        
        attribute happy "VN Mode/Unknown/unknown_face_0.png" align(0.41, 0.142)
        attribute smile "VN Mode/Unknown/unknown_face_1.png" align(0.41, 0.142)
        attribute neutral default "VN Mode/Unknown/unknown_face_2.png" align(0.41, 0.142)
        attribute angry "VN Mode/Unknown/unknown_face_3.png" align(0.41, 0.142)
        attribute thinking "VN Mode/Unknown/unknown_face_4.png" align(0.41, 0.142)
        attribute tense "VN Mode/Unknown/unknown_face_5.png" align(0.41, 0.142)
        attribute creepy "VN Mode/Unknown/unknown_face_6.png" align(0.41, 0.142)
        attribute cry "VN Mode/Unknown/unknown_face_7.png" align(0.41, 0.142)
        attribute blush "VN Mode/Unknown/unknown_face_15.png" align(0.41, 0.142)
        attribute sob "VN Mode/Unknown/unknown_face_16.png" align(0.41, 0.142)
        attribute teary "VN Mode/Unknown/unknown_face_17.png" align(0.41, 0.142)
        attribute nervous "VN Mode/Unknown/unknown_face_18.png" align(0.41, 0.142)
        attribute sad "VN Mode/Unknown/unknown_face_19.png" align(0.41, 0.142)
        attribute worried "VN Mode/Unknown/unknown_face_20.png" align(0.41, 0.142)
        attribute distant "VN Mode/Unknown/unknown_face_21.png" align(0.41, 0.142)
        
    group face:
        if_any "mask"        
        attribute happy "VN Mode/Unknown/unknown_face_8.png" align(0.41, 0.142)
        attribute smile "VN Mode/Unknown/unknown_face_9.png" align(0.41, 0.142)
        attribute neutral default "VN Mode/Unknown/unknown_face_10.png" align(0.41, 0.142)
        attribute angry "VN Mode/Unknown/unknown_face_11.png" align(0.41, 0.142)
        attribute thinking "VN Mode/Unknown/unknown_face_12.png" align(0.41, 0.142)
        attribute tense "VN Mode/Unknown/unknown_face_13.png" align(0.41, 0.142)
        attribute creepy "VN Mode/Unknown/unknown_face_14.png" align(0.41, 0.142)
        
        
## ****************************
## V
## ****************************
layeredimage v front:
    yoffset 200

    group body:
        attribute normal default "VN Mode/V/v02_body_1.png"
        attribute arm "VN Mode/V/v02_body_0.png"
        attribute hair_normal "VN Mode/V/v02_body_2.png"
        attribute hair_arm "VN Mode/V/v02_body_3.png"
        attribute mint_eye "VN Mode/V/v02_body_4.png"
        
    group face:
        attribute neutral default "VN Mode/V/v02_face_0.png" align(0.4345, 0.111)
        attribute happy "VN Mode/V/v02_face_1.png" align(0.4345, 0.111)
        attribute angry "VN Mode/V/v02_face_2.png" align(0.4345, 0.111)
        attribute worried "VN Mode/V/v02_face_3.png" align(0.4345, 0.111)
        attribute thinking "VN Mode/V/v02_face_4.png" align(0.4345, 0.111)
        attribute talking "VN Mode/V/v02_face_5.png" align(0.4345, 0.111)
        attribute surprised "VN Mode/V/v02_face_6.png" align(0.4345, 0.111)
        attribute tense "VN Mode/V/v02_face_7.png" align(0.4345, 0.111)
        attribute sweating "VN Mode/V/v02_face_8.png" align(0.4345, 0.111)
        attribute sad "VN Mode/V/v02_face_9.png" align(0.4345, 0.111)
        attribute upset "VN Mode/V/v02_face_10.png" align(0.4345, 0.111)
        attribute concerned "VN Mode/V/v02_face_11.png" align(0.4345, 0.111)
        attribute regret "VN Mode/V/v02_face_12.png" align(0.4345, 0.111)
        attribute unsure "VN Mode/V/v02_face_13.png" align(0.4345, 0.111)
        attribute afraid "VN Mode/V/v02_face_14.png" align(0.4345, 0.111)
        
    group head:
        if_any "mint_eye"
        attribute hood_up "VN Mode/V/v02_hood_1.png" align(0.4, 0.0) yoffset -25
        attribute hood_down default "VN Mode/V/v02_hood_1_1.png" align(0.4, 0.212)
        
layeredimage v side:    
    yoffset 210
    
    group body:
        attribute normal default "VN Mode/V/v_body_0.png"
        attribute short_hair "VN Mode/V/v_body_1.png"
        attribute long_hair "VN Mode/V/v_body_2.png"
        
    group face:
        ## No sunglasses
        attribute happy "VN Mode/V/v_face_1.png" align(0.411, 0.109)
        attribute angry "VN Mode/V/v_face_3.png" align(0.411, 0.108)
        attribute neutral default "VN Mode/V/v_face_5.png" align(0.411, 0.108)
        attribute surprised "VN Mode/V/v_face_7.png" align(0.411, 0.108)
        attribute thinking "VN Mode/V/v_face_9.png" align(0.411, 0.108)
        attribute worried "VN Mode/V/v_face_11.png" align(0.4, 0.108)
        attribute sweat "VN Mode/V/v_face_13.png" align(0.411, 0.108)
        attribute shock "VN Mode/V/v_face_15.png" align(0.411, 0.108)
        attribute afraid "VN Mode/V/v_face_17.png" align(0.411, 0.108)
        attribute blush "VN Mode/V/v_face_19.png" align(0.405, 0.108)
        attribute sad "VN Mode/V/v_face_21.png" align(0.411, 0.108)
        attribute unsure "VN Mode/V/v_face_23.png" align(0.411, 0.108)

layeredimage v side glasses:    
    yoffset 210
    
    group body:
        attribute normal default "VN Mode/V/v_body_0.png"
        attribute short_hair "VN Mode/V/v_body_1.png"
        attribute long_hair "VN Mode/V/v_body_2.png"
        
    group face:
        attribute happy "VN Mode/V/v_face_0.png" align(0.411, 0.108)
        attribute angry "VN Mode/V/v_face_2.png" align(0.411, 0.108)
        attribute neutral "VN Mode/V/v_face_4.png" align(0.411, 0.1072)
        attribute surprised "VN Mode/V/v_face_6.png" align(0.411, 0.108)
        attribute thinking "VN Mode/V/v_face_8.png" align(0.411, 0.108)
        attribute worried "VN Mode/V/v_face_10.png" align(0.411, 0.108)
        attribute sweat "VN Mode/V/v_face_12.png" align(0.411, 0.108)
        attribute shock "VN Mode/V/v_face_14.png" align(0.411, 0.108)
        attribute afraid "VN Mode/V/v_face_16.png" align(0.411, 0.108)
        attribute blush "VN Mode/V/v_face_18.png" align(0.411, 0.108)
        attribute sad "VN Mode/V/v_face_20.png" align(0.411, 0.108)
        attribute unsure "VN Mode/V/v_face_22.png" align(0.411, 0.108)
        
        
## ****************************
## Yoosung
## ****************************
layeredimage yoosung vn:
    
    group body:
        attribute normal default "VN Mode/Yoosung/yoosung_body_0.png"
        attribute arm "VN Mode/Yoosung/yoosung_body_1.png"
        attribute sweater "VN Mode/Yoosung/yoosung_body_2.png"
        attribute suit "VN Mode/Yoosung/yoosung_body_3.png"
        attribute party "VN Mode/Yoosung/yoosung_body_5.png"
        attribute bandage "VN Mode/Yoosung/yoosung_body_4.png"
        
    group face:
        if_not "bandage"
        attribute happy "VN Mode/Yoosung/yoosung_face_0.png" align(0.256, 0.111)
        attribute angry "VN Mode/Yoosung/yoosung_face_2.png" align(0.256, 0.111)
        attribute sparkle "VN Mode/Yoosung/yoosung_face_4.png" align(0.256, 0.111)
        attribute neutral default "VN Mode/Yoosung/yoosung_face_6.png" align(0.256, 0.111)
        attribute surprised "VN Mode/Yoosung/yoosung_face_7.png" align(0.256, 0.111)
        attribute thinking "VN Mode/Yoosung/yoosung_face_8.png" align(0.256, 0.111)
        attribute sad "VN Mode/Yoosung/yoosung_face_9.png" align(0.259, 0.111)
        attribute grin "VN Mode/Yoosung/yoosung_face_10.png" align(0.256, 0.111)
        attribute dark "VN Mode/Yoosung/yoosung_face_11.png" align(0.256, 0.111)
        attribute tired "VN Mode/Yoosung/yoosung_face_12.png" align(0.256, 0.111)
        attribute upset "VN Mode/Yoosung/yoosung_face_13.png" align(0.256, 0.111)
        
    group face:
        if_any "bandage"
        attribute happy  "VN Mode/Yoosung/yoosung_face_1.png" align(0.256, 0.111)
        attribute neutral default  "VN Mode/Yoosung/yoosung_face_3.png" align(0.256, 0.111)
        attribute thinking  "VN Mode/Yoosung/yoosung_face_5.png" align(0.256, 0.111)
        
layeredimage yoosung vn glasses:
    
    group body:
        attribute normal default "VN Mode/Yoosung/yoosung_body_0.png"
        attribute arm "VN Mode/Yoosung/yoosung_body_1.png"
        attribute sweater "VN Mode/Yoosung/yoosung_body_2.png"
        attribute suit "VN Mode/Yoosung/yoosung_body_3.png"
        attribute party "VN Mode/Yoosung/yoosung_body_5.png"
        
    group face:      
        attribute happy "VN Mode/Yoosung/yoosung_face_14.png" align(0.256, 0.111)
        attribute sparkle "VN Mode/Yoosung/yoosung_face_15.png" align(0.256, 0.111)
        attribute neutral default "VN Mode/Yoosung/yoosung_face_16.png" align(0.256, 0.111)
        attribute surprised "VN Mode/Yoosung/yoosung_face_17.png" align(0.256, 0.111)
        attribute thinking "VN Mode/Yoosung/yoosung_face_18.png" align(0.256, 0.111)
        attribute grin "VN Mode/Yoosung/yoosung_face_19.png" align(0.256, 0.111)
        
## ****************************
## Zen
## ****************************
layeredimage zen front:

    group body:        
        attribute arm "VN Mode/Zen/zen_body_arm.png" 
        attribute party "VN Mode/Zen/zen_body_party.png"
        attribute normal default "VN Mode/Zen/zen_body_pocket.png"
        
    group face:    
        attribute happy "VN Mode/Zen/zen_face_0.png" align(0.428, 0.121)
        attribute angry "VN Mode/Zen/zen_face_1.png" align(0.428, 0.121)
        attribute blush "VN Mode/Zen/zen_face_2.png" align(0.428, 0.121)
        attribute wink "VN Mode/Zen/zen_face_3.png" align(0.428, 0.121)
        attribute neutral default "VN Mode/Zen/zen_face_4.png" align(0.428, 0.121)
        attribute surprised "VN Mode/Zen/zen_face_5.png" align(0.428, 0.121)
        attribute thinking "VN Mode/Zen/zen_face_6.png" align(0.428, 0.121)
        attribute worried "VN Mode/Zen/zen_face_7.png" align(0.428, 0.121)
        attribute oh "VN Mode/Zen/zen_face_8.png" align(0.428, 0.121)
        attribute upset "VN Mode/Zen/zen_face_9.png" align(0.428, 0.121)
        
layeredimage zen side:
    
    group body:
        attribute normal default "VN Mode/Zen/zen_sidebody_normal.png"
        attribute suit "VN Mode/Zen/zen_sidebody_suit.png"
        
    group face:        
        attribute happy "VN Mode/Zen/zen_sideface_0.png" align(0.252, 0.118)
        attribute angry "VN Mode/Zen/zen_sideface_1.png" align(0.258, 0.120)
        attribute blush "VN Mode/Zen/zen_sideface_2.png" align(0.258, 0.120)
        attribute wink "VN Mode/Zen/zen_sideface_3.png" align(0.258, 0.120)
        attribute neutral default "VN Mode/Zen/zen_sideface_4.png" align(0.258, 0.120)
        attribute surprised "VN Mode/Zen/zen_sideface_5.png" align(0.258, 0.120)
        attribute thinking "VN Mode/Zen/zen_sideface_6.png" align(0.258, 0.120)
        attribute worried "VN Mode/Zen/zen_sideface_7.png" align(0.258, 0.120)
        attribute upset "VN Mode/Zen/zen_sideface_8.png" align(0.258, 0.120)
        

## ********* SIDE CHARACTERS *********
     
## ****************************
## Bodyguards
## ****************************

layeredimage bodyguard front:
    yoffset 50
    group body:
        attribute normal default "VN Mode/B01/b01_body_0.png"
        
    group face:
        attribute neutral default "VN Mode/B01/b01_face_0.png" align(0.397, 0.083)
        attribute thinking "VN Mode/B01/b01_face_1.png" align(0.397, 0.083)
        attribute stressed "VN Mode/B01/b01_face_2.png" align(0.397, 0.083)
        
layeredimage bodyguard side:
    yoffset 40
    group body:
        attribute normal default "VN Mode/B02/b02_body_0.png"
        
    group face:
        attribute neutral default "VN Mode/B02/b02_face_0.png" align(0.239, 0.105)
        attribute thinking "VN Mode/B02/b02_face_1.png" align(0.239, 0.105)
        attribute stressed "VN Mode/B02/b02_face_2.png" align(0.239, 0.105)
        
## ****************************
## Chairman Han
## ****************************        

layeredimage chairman_han:
    yoffset 45
    group body:
        attribute normal default "VN Mode/Mr Chairman/han_body_0.png"
    
    group face:
        attribute happy "VN Mode/Mr Chairman/han_face_0.png" align(0.263, 0.088)
        attribute thinking "VN Mode/Mr Chairman/han_face_1.png" align(0.263, 0.088)
        attribute neutral default "VN Mode/Mr Chairman/han_face_2.png" align(0.263, 0.088)
        attribute stressed "VN Mode/Mr Chairman/han_face_3.png" align(0.263, 0.088)
        
## ****************************
## Echo Girl
## ****************************

layeredimage echo_girl:
    yoffset 70
    group body:
        attribute normal default "VN Mode/Echo girl/eco_body_0.png"
        
    group face:
        attribute neutral default "VN Mode/Echo girl/eco_face_0.png" align(1.007, 0.09)
        attribute happy "VN Mode/Echo girl/eco_face_1.png" align(1.007, 0.09)
        attribute angry "VN Mode/Echo girl/eco_face_2.png" align(1.007, 0.09)
        attribute smile "VN Mode/Echo girl/eco_face_3.png" align(1.007, 0.09)
        attribute surprised "VN Mode/Echo girl/eco_face_4.png" align(1.007, 0.09)
        
        
## ****************************
## Glam Choi
## ****************************

layeredimage glam_choi:
    yoffset 115
    group body:
        attribute normal default "VN Mode/Glam Choi/glam_body_0.png"
        
    group face:
        attribute happy "VN Mode/Glam Choi/glam_face_0.png" align(0.4585, 0.099)
        attribute smirk "VN Mode/Glam Choi/glam_face_1.png" align(0.4585, 0.098)
        attribute thinking "VN Mode/Glam Choi/glam_face_2.png" align(0.4585, 0.098)
        attribute neutral default "VN Mode/Glam Choi/glam_face_3.png" align(0.4585, 0.098)
        attribute stressed "VN Mode/Glam Choi/glam_face_4.png" align(0.4585, 0.098)
        attribute worried "VN Mode/Glam Choi/glam_face_5.png" align(0.4585, 0.098)
        
        
## ****************************
## Prime Minister
## **************************** 
        
image prime_minister:
    "VN Mode/Prime Minister/prime_minister_body.png"
    yoffset 75

## ****************************
## Sarah Choi
## ****************************        

layeredimage sarah:
    yoffset 115
    group body:
        attribute normal default "VN Mode/Sarah Choi/sarah_body_0.png"
    
    group face:
        attribute happy "VN Mode/Sarah Choi/sara_face_0.png" align(0.233, 0.097)
        attribute excited "VN Mode/Sarah Choi/sara_face_1.png" align(0.233, 0.097)
        attribute smirk "VN Mode/Sarah Choi/sara_face_2.png" align(0.233, 0.097)
        attribute neutral default "VN Mode/Sarah Choi/sara_face_3.png" align(0.233, 0.097)
        attribute stressed "VN Mode/Sarah Choi/sara_face_4.png" align(0.233, 0.097)
        attribute sad "VN Mode/Sarah Choi/sara_face_5.png" align(0.233, 0.097)
        
## ****************************
## Vanderwood
## **************************** 

layeredimage vanderwood:
    yoffset 20
    group body:
        attribute normal default "VN Mode/Vanderwood/van_body_0.png"
   
    group face:
        attribute neutral default "VN Mode/Vanderwood/ven_face_0.png" align(1.065, 0.112)
        attribute unamused "VN Mode/Vanderwood/ven_face_1.png" align(1.065, 0.112)
        attribute unsure "VN Mode/Vanderwood/ven_face_2.png" align(1.065, 0.112)
        attribute determined "VN Mode/Vanderwood/ven_face_3.png" align(1.065, 0.112)
        attribute ouch "VN Mode/Vanderwood/ven_face_4.png" align(1.065, 0.112)
        attribute angry "VN Mode/Vanderwood/ven_face_5.png" align(1.065, 0.112)
        
        
        