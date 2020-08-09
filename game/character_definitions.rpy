init offset = -1
                        
# ****************************
# Phone Call Characters
# ****************************

# These are separate from the VN and chatroom character definitions since they
# display more like VN mode. You won't actually see their name in-game. 
# For most purposes, you can just copy any character besides m_phone 
# and replace the name with the name you want. The main difference is 
# in the voice tags, so that if you mute a character you won't hear their
# voice during phone calls or VN mode
# For ease of remembering, Phone Call characters are just their 
# ChatCharacter variables + '_phone' e.g. ja -> ja_phone

# This is a default phone character that you can "inherit" the style
# from rather than declaring all the individual properties
define phone_character = Character(None, 
    what_font=gui.sans_serif_1, 
    what_color="#fff", 
    what_xalign=0.5, 
    what_yalign=0.5, 
    what_text_align=0.5,
    voice_tag="other_voice",
    screen='phone_say')

define ja_phone = Character("Jaehee Kang", 
    kind=phone_character, voice_tag="ja_voice")
define ju_phone = Character("Jumin Han", 
    kind=phone_character, voice_tag="ju_voice")
define s_phone = Character("707", 
    kind=phone_character, voice_tag="s_voice")
define sa_phone = Character("Saeran", 
    kind=phone_character, voice_tag="sa_voice")
define r_phone = Character("Ray", 
    kind=phone_character, voice_tag="sa_voice")
define ri_phone = Character("Rika", 
    kind=phone_character, voice_tag="ri_voice")
define y_phone = Character("Yoosung★", 
    kind=phone_character, voice_tag="y_voice")
define v_phone = Character("V", 
    kind=phone_character, voice_tag="v_voice")
define u_phone = Character("Unknown", 
    kind=phone_character, voice_tag="sa_voice")
define z_phone = Character("Zen", 
    kind=phone_character, voice_tag="z_voice")
define m_phone = Character("[name]", 
    kind=phone_character, what_color="#a6a6a6", 
    what_suffix="{w=0.8}{nw}", dynamic=True)
define vmail_phone = Character('Voicemail', kind=phone_character)
                        
# ****************************
# Visual Novel Mode
# ****************************                        
## CHARACTER DEFINITIONS ****************

# Again, you can copy-paste a character definition from here and change the
# window_background and voice_tag as appropriate.
# For ease of remembering, VN characters are just their ChatCharacter variables
# + "_vn" e.g. s -> s_vn. The who_color is also the background of the
# characters' speech bubbles rather than the default #fff5ca 

# This is the 'generic' VN character, which you can inherit from
# for any new character you want to create
default vn_character = Character(None, 
    what_font=gui.sans_serif_1, 
    what_color="#ffffff", 
    window_background=Transform("VN Mode/Chat Bubbles/vnmode_9.png",
                                alpha=persistent.vn_window_alpha),
    who_color="#fff5ca", 
    who_size=40, 
    voice_tag="other_voice")

# Similarly, this is for characters you don't want to actually define and
# instead want to just use once or twice. You can write their dialogue like
# "Bodyguard" "Your dialogue"
default name_only = Character(None, 
    what_font=gui.sans_serif_1, 
    what_color="#ffffff", 
    window_background=Transform("VN Mode/Chat Bubbles/vnmode_9.png",
                                alpha=persistent.vn_window_alpha),
    who_color="#fff5ca", 
    who_size=40, 
    voice_tag="other_voice")

default ja_vn = Character("Jaehee", kind=vn_character,
    window_background=Transform("VN Mode/Chat Bubbles/vnmode_4.png",
                                alpha=persistent.vn_window_alpha),
    who_color="#fff5eb", voice_tag="ja_voice", 
    image="jaehee")
default ju_vn = Character("Jumin", kind=vn_character,
    window_background=Transform("VN Mode/Chat Bubbles/vnmode_0.png",
                                alpha=persistent.vn_window_alpha),
    who_color="#d2e6f7", voice_tag="ju_voice", 
    image="jumin")
default r_vn = Character("Ray", kind=vn_character,
    window_background=Transform("VN Mode/Chat Bubbles/vnmode_9.png",
                                alpha=persistent.vn_window_alpha),
    who_color="#f2ebfd", voice_tag="sa_voice", 
    image="saeran")
default ri_vn = Character("Rika", kind=vn_character,
    window_background=Transform("VN Mode/Chat Bubbles/vnmode_7.png",
                                alpha=persistent.vn_window_alpha),
    who_color="#fff9db", voice_tag="ri_voice", 
    image="rika")
default s_vn = Character("707", kind=vn_character,
    window_background=Transform("VN Mode/Chat Bubbles/vnmode_2.png",
                                alpha=persistent.vn_window_alpha),
    who_color="#fff1f1", voice_tag="s_voice", 
    image="seven")
default sa_vn = Character("Saeran", kind=vn_character,
    window_background=Transform("VN Mode/Chat Bubbles/vnmode_8.png",
                                alpha=persistent.vn_window_alpha),
    who_color="#f2ebfd", voice_tag="sa_voice", 
    image="saeran")
default u_vn = Character("???", kind=vn_character,
    window_background=Transform("VN Mode/Chat Bubbles/vnmode_9.png",
                                alpha=persistent.vn_window_alpha),
    who_color="#f2ebfd", voice_tag="sa_voice", 
    image="saeran")
default v_vn = Character("V", kind=vn_character,
    window_background=Transform("VN Mode/Chat Bubbles/vnmode_5.png",
                                alpha=persistent.vn_window_alpha),
    who_color="#cbfcfc", voice_tag="v_voice", 
    image="v")
default y_vn = Character("Yoosung", kind=vn_character,
    window_background=Transform("VN Mode/Chat Bubbles/vnmode_3.png",
                                alpha=persistent.vn_window_alpha),
    who_color="#effff3", voice_tag="y_voice", 
    image="yoosung")
default z_vn = Character("Zen", kind=vn_character,
    window_background=Transform("VN Mode/Chat Bubbles/vnmode_1.png",
                                alpha=persistent.vn_window_alpha),
    who_color="#d8e9f9", voice_tag="z_voice", 
    image="zen")
                            
## Note: The MC's name will show up in VN mode in this program. 
## If you'd like it to be blank, just replace "persistent.name" with None
default m_vn = Character("persistent.name", kind=vn_character, 
                        who_color="#ffffed", dynamic=True)

## This is the 'generic' template character -- if you want a 
## side character like Echo Girl, copy this character and 
## replace None with their name.
default narrator = Character(None, kind=vn_character)

# Giving Sarah the property `image='sarah'` means you can use her
# dialogue to also show images of her with a different expression
# See tutorial_6_meeting.rpy for an example of this
default sarah_vn = Character("Sarah", kind=vn_character, image='sarah')

default chief_vn = Character("Chief Han", kind=vn_character, 
                                        image='chairman_han')


##****************************
## Chatroom Characters
##****************************

## Chatroom character declarations. Format is: 
##  name - nickname for the chatrooms
##  file_id - short form appended to file names like speech bubbles
##  prof_pic - profile pic (110x110 - 314x314)
##  participant_pic - pic that shows they're present in a chatroom
##  heart_color - hex number of their heart colour
##  cover_pic/status  - as stated
##  bubble_color - colour of their regular speech bubbles. If not given,
##              the program looks for a bubble using the character's file_id
##  glow_color - same as above, for glowing speech bubbles
##  voicemail - generally set at the end of a chatroom, 
##              not during definition time
##  emote_list - used for chatroom creation (can be left False
##               if you don't need it/don't know what to do with it)
##  right_msgr - indicates this character will send messages from the right
##               side of the screen (this is usually true only for
##               MC, and it is automatically False for everyone else)
##  homepage_pic - the image used in the chat_hub screen to show if a 
##                 character has updated their profile
##  phone_char - The phone character you defined for this character earlier
##               (usually just the character's short form + _phone)
##  vn_char - The VN character you defined for this character earlier
##              (usually just the character's short form + _vn)

# This list populates itself with every character in the game
default all_characters = [] 

default ja = ChatCharacter("Jaehee Kang", 'ja', 
                'Profile Pics/Jaehee/ja-default.png', 
                'Profile Pics/ja_chat.png', "#d0b741", 
                "Cover Photos/profile_cover_photo.png", "Jaehee's status", 
                emote_list=jaehee_emotes,
                homepage_pic="Profile Pics/main_profile_jaehee.png",
                phone_char=ja_phone, vn_char=ja_vn,
                pronunciation_help="jayhee kang")
default ju = ChatCharacter("Jumin Han", 'ju', 
                'Profile Pics/Jumin/ju-default.png', 
                'Profile Pics/ju_chat.png', "#a59aef", 
                "Cover Photos/profile_cover_photo.png", "Jumin's status", 
                emote_list=jumin_emotes,
                homepage_pic="Profile Pics/main_profile_jumin.png",
                phone_char=ju_phone, vn_char=ju_vn,
                pronunciation_help="jumin han")
default m = ChatCharacter("[persistent.name]", 'm', 
                persistent.MC_pic, right_msgr=True,
                phone_char=m_phone, vn_char=m_vn,
                pronunciation_help="you")
default r = ChatCharacter("Ray", 'r', 'Profile Pics/Ray/ray-default.png', 
                'Profile Pics/r_chat.png', "#b81d7b", 
                "Cover Photos/profile_cover_photo.png", "Ray's status", 
                emote_list=ray_emotes,
                homepage_pic="Profile Pics/main_profile_ray.png",
                phone_char=r_phone, vn_char=r_vn,
                pronunciation_help="ray")
default ri = ChatCharacter("Rika", 'ri', 'Profile Pics/Rika/rika-default.png', 
                'Profile Pics/ri_chat.png', "#fcef5a", 
                "Cover Photos/profile_cover_photo.png", "Rika's status", 
                emote_list=rika_emotes,
                homepage_pic="Profile Pics/main_profile_rika.png",
                phone_char=ri_phone, vn_char=ri_vn,
                pronunciation_help="rika")
default s = ChatCharacter("707", 's', 'Profile Pics/Seven/sev-default.png', 
                'Profile Pics/s_chat.png', "#ff2626", 
                "Cover Photos/profile_cover_photo.png", "707's status", 
                emote_list=seven_emotes,
                homepage_pic="Profile Pics/main_profile_seven.png",
                phone_char=s_phone, vn_char=s_vn,
                pronunciation_help="seven oh seven")
default sa = ChatCharacter("Saeran", "sa", 'Profile Pics/Saeran/sae-1.png', 
                'Profile Pics/sa_chat.png', "#b81d7b", 
                "Cover Photos/profile_cover_photo.png", "Saeran's status", 
                emote_list=saeran_emotes,
                homepage_pic="Profile Pics/main_profile_sa1.png",
                phone_char=sa_phone, vn_char=sa_vn,
                pronunciation_help="sairan")
default u = ChatCharacter("Unknown", "u", 'Profile Pics/Unknown/Unknown-1.png', 
                'Profile Pics/u_chat.png', "#ffffff",
                phone_char=u_phone, vn_char=u_vn)
default v = ChatCharacter("V", 'v', 'Profile Pics/V/V-default.png', 
                'Profile Pics/v_chat.png', "#50b2bc", 
                "Cover Photos/profile_cover_photo.png", "V's status", 
                emote_list=v_emotes,
                homepage_pic="Profile Pics/main_profile_v.png",
                phone_char=v_phone, vn_char=v_vn)
default y = ChatCharacter("Yoosung★", 'y', 
                'Profile Pics/Yoosung/yoo-default.png', 
                'Profile Pics/y_chat.png', "#31ff26", 
                "Cover Photos/profile_cover_photo.png", "Yoosung's status", 
                emote_list=yoosung_emotes,
                homepage_pic="Profile Pics/main_profile_yoosung.png",
                phone_char=y_phone, vn_char=y_vn,
                pronunciation_help="yoosung")
default z = ChatCharacter("ZEN", 'z', 'Profile Pics/Zen/zen-default.png', 
                'Profile Pics/z_chat.png', "#c9c9c9", 
                "Cover Photos/profile_cover_photo.png", "Zen's status", 
                emote_list=zen_emotes,
                homepage_pic="Profile Pics/main_profile_zen.png",
                phone_char=z_phone, vn_char=z_vn)

# These are special 'characters' for additional features
default special_msg = ChatCharacter("msg")
default filler = ChatCharacter("filler")
default answer = ChatCharacter('answer', 'delete')
default chat_pause = ChatCharacter('pause', 'delete')

# This list is used *specifically* to display characters you can see on the
# main menu -- they have profiles and show up in your phone contacts
default character_list = [ju, z, s, y, ja, v, m, r, ri]
# This is the list of characters who you can see your heart points for in the
# Profile screen. Currently it is a duplicate of the above list, but without
# 'm'. You could also write it as default heart_point_chars = [ju, ja, s, y, z]
# for example. Every character in the list should have an image called 
# 'greet ' + their file id
default heart_point_chars = [ c for c in character_list if not c.right_msgr ]

# Add ChatCharacter objects to this list if they should not have a 
# voice toggle in the settings screen
# Unknown and Saeran are lumped into Ray's voice button and MC doesn't speak
default novoice_chars = [u, sa, m]

init offset = 0

## *************************************
## Character VN Expressions Cheat Sheet
## *************************************

## ********* MAIN CHARACTERS *********

## Jaehee:
# WITH OR WITHOUT GLASSES: happy, sad, neutral (default), thinking, worried
# WITH GLASSES: angry, sparkle, serious, surprised
# OUTFITS: normal (default), arm, party, dress, apron

## Jumin:
# FRONT: happy, upset, blush, neutral (default), surprised, 
#        angry, sad, unsure, thinking
# FRONT OUTFITS: normal (default), arm, party
# SIDE: happy, upset, blush, neutral (default), surprised, 
#       angry, thinking, worried
# SIDE OUTFITS: normal (default), suit

## Rika:
# EXPRESSIONS: happy, sad, neutral (default), thinking, 
#              worried, dark, angry, sob, crazy
# OUTFITS: normal (default), savior, dress
# ACCESSORIES: mask

## Seven:
# FRONT: happy, blush, neutral (default), surprised, serious, 
#        thinking, sad, worried, dark, angry, hurt
# FRONT OUTFITS: normal (default), arm, party
# SIDE: happy, concern, surprised, thinking, sad, neutral (default), 
#       dark, angry, worried
# SIDE OUTFITS: normal (default), arm, suit

## Saeran:
# WITH OR WITHOUT MASK: happy, smile, neutral (default), 
#                       angry, thinking, tense, creepy
# WITHOUT MASK: cry, blush, sob, teary, nervous, sad, worried, distant
# OUTFITS: unknown, mask, ray (default), saeran, suit

## V:
# FRONT: neutral (default), happy, angry, worried, thinking, 
#        talking, surprised, tense, sweating, sad, upset, 
#        concerned, regret, unsure, afraid
# FRONT OUTFITS: normal (default), arm, hair_normal, hair_arm, mint_eye
# ACCESSORIES **mint_eye outfit only**: hood_up, hood_down (default)
# SIDE, WITH OR WITHOUT GLASSES: happy, angry, neutral (default),
#                                surprised, thinking, worried, sweat, 
#                                shock, afraid, blush, sad, unsure
# SIDE OUTFITS: normal (default), short_hair, long_hair

## Yoosung:
# WITH OR WITHOUT BANDAGE: happy, neutral (default), thinking
# WITH OR WITHOUT GLASSES: happy, neutral (default), thinking, 
#                          surprised, sparkle, grin
# WITHOUT GLASSES OR BANDAGE: angry, sad, dark, tired, upset
# OUTFITS: normal (default), arm, sweater, suit, party, bandage

## Zen:
# FRONT: happy, angry, blush, wink, neutral (default), surprised, thinking,
#        worried, oh, upset
# FRONT OUTFITS: arm, party, normal (default)
# SIDE: happy, angry, blush, wink, neutral (default), surprised, 
#       thinking, worried, upset
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
# For starters, keep accessories like glasses separate from facial expressions,
# so you can avoid doing what is done here, which includes having a transparent
# image as a sort of 'dummy' glasses attribute. That aside, characters are
# generally declared with a body and face group, and sometimes have a 'yoffset'
# value that simply puts their sprite lower down on the screen (so the
# characters have the correct relative heights to one another). Other than that, 
# everything is the same as you'll find in Ren'Py's layeredimage documentation

## ****************************
## Jaehee
## ****************************
layeredimage jaehee:
    yoffset 70
    
    group body:
        attribute normal default "VN Mode/Jaehee/jaehee_body_0.png"
        attribute arm "VN Mode/Jaehee/jaehee_body_1.png"
        attribute party "VN Mode/Jaehee/jaehee_body_2.png"
        attribute dress "VN Mode/Jaehee/jaehee_body_3.png"
        attribute apron "VN Mode/Jaehee/jaehee_body_4.png"
        
    group face:
        if_not "glasses"
        align (0.298, 0.108)
        attribute happy "VN Mode/Jaehee/jaehee_face_1.png"
        attribute sad "VN Mode/Jaehee/jaehee_face_3.png" 
        attribute neutral default "VN Mode/Jaehee/jaehee_face_5.png"
        attribute thinking "VN Mode/Jaehee/jaehee_face_7.png" 
        attribute worried "VN Mode/Jaehee/jaehee_face_9.png" 
        
    group face:
        if_any "glasses"
        align(0.299, 0.108)
        attribute happy "VN Mode/Jaehee/jaehee_face_0.png" 
        attribute angry "VN Mode/Jaehee/jaehee_face_2.png"
        attribute sad "VN Mode/Jaehee/jaehee_face_4.png"
        attribute sparkle "VN Mode/Jaehee/jaehee_face_6.png"
        attribute neutral default "VN Mode/Jaehee/jaehee_face_8.png"
        attribute thinking "VN Mode/Jaehee/jaehee_face_10.png"
        attribute serious "VN Mode/Jaehee/jaehee_face_11.png"
        attribute worried "VN Mode/Jaehee/jaehee_face_12.png"
        attribute surprised "VN Mode/Jaehee/jaehee_face_13.png"
    
    # This is an unusual little hack that lets the program
    # identify whether jaehee should be wearing her glasses or not
    group eyewear:
        attribute glasses Transform('transparent.png', size=(10,10))
        
        
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
        align(0.39, 0.121)
        attribute happy "VN Mode/Jumin/jumin_face_0.png"
        attribute upset "VN Mode/Jumin/jumin_face_1.png"
        attribute blush "VN Mode/Jumin/jumin_face_2.png"
        attribute neutral default "VN Mode/Jumin/jumin_face_3.png"
        attribute surprised "VN Mode/Jumin/jumin_face_4.png"
        attribute angry "VN Mode/Jumin/jumin_face_5.png"
        attribute sad "VN Mode/Jumin/jumin_face_6.png"
        attribute unsure "VN Mode/Jumin/jumin_face_7.png"
        attribute thinking "VN Mode/Jumin/jumin_face_8.png"
        
layeredimage jumin side:

    yoffset 15
    
    group body:
        attribute normal default "VN Mode/Jumin/jumin_sidebody_0b.png"
        attribute suit "VN Mode/Jumin/jumin_sidebody_1.png."
            
    group face:
        align(0.633, 0.097)
        attribute happy "VN Mode/Jumin/jumin_sideface_0.png"
        attribute upset "VN Mode/Jumin/jumin_sideface_1.png"
        attribute blush "VN Mode/Jumin/jumin_sideface_2.png"
        attribute neutral default "VN Mode/Jumin/jumin_sideface_3.png"
        attribute surprised "VN Mode/Jumin/jumin_sideface_4.png"
        attribute angry "VN Mode/Jumin/jumin_sideface_5.png"
        attribute thinking "VN Mode/Jumin/jumin_sideface_6.png"
        attribute worried "VN Mode/Jumin/jumin_sideface_7.png" 
        
        
## ****************************
## Rika
## ****************************
layeredimage rika:
    yoffset 80

    group body:
        attribute normal default "VN Mode/Rika/rika01_body_0.png"
        attribute savior "VN Mode/Rika/rika01_body_1.png"
        attribute dress "VN Mode/Rika/rika01_body_2.png"
        
    group face:
        align(0.666, 0.097)
        attribute happy "VN Mode/Rika/rika01_face_0.png"
        attribute sad "VN Mode/Rika/rika01_face_1.png"
        attribute neutral default "VN Mode/Rika/rika01_face_2.png"
        attribute thinking "VN Mode/Rika/rika01_face_3.png"
        attribute worried "VN Mode/Rika/rika01_face_4.png"
        attribute dark "VN Mode/Rika/rika01_face_5.png"
        attribute angry "VN Mode/Rika/rika01_face_6.png"
        attribute sob "VN Mode/Rika/rika01_face_7.png"
        attribute crazy "VN Mode/Rika/rika01_face_8.png" 
        
    group head:
        attribute mask "VN Mode/Rika/rika01_head_0.png" align(0.715, 0.05)
        
        
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
        align(0.427, 0.139)
        attribute happy "VN Mode/707/seven_face_0.png" 
        attribute blush "VN Mode/707/seven_face_1.png"
        attribute neutral default "VN Mode/707/seven_face_2.png"
        attribute surprised "VN Mode/707/seven_face_3.png"
        attribute serious "VN Mode/707/seven_face_4.png"
        attribute thinking "VN Mode/707/seven_face_5.png"
        attribute sad "VN Mode/707/seven_face_6.png"
        attribute worried "VN Mode/707/seven_face_7.png"
        attribute dark "VN Mode/707/seven_face_8.png"
        attribute angry "VN Mode/707/seven_face_9.png"
        attribute hurt "VN Mode/707/seven_face_10.png"
        
layeredimage seven side:
    yoffset 160
    
    group body:
        attribute normal default "VN Mode/707/seven_sidebody_0.png"
        attribute arm "VN Mode/707/seven_sidebody_1.png"
        attribute suit "VN Mode/707/seven_valentines_0.png"
        
    group face:
        align(0.435, 0.13)
        attribute happy "VN Mode/707/seven_sideface_0.png" 
        attribute concern "VN Mode/707/seven_sideface_1.png"
        attribute surprised "VN Mode/707/seven_sideface_2.png"
        attribute thinking  "VN Mode/707/seven_sideface_3.png"
        attribute sad "VN Mode/707/seven_sideface_4.png"
        attribute neutral default "VN Mode/707/seven_sideface_5.png"
        attribute dark "VN Mode/707/seven_sideface_6.png"
        attribute angry "VN Mode/707/seven_sideface_7.png"
        attribute worried "VN Mode/707/seven_sideface_8.png"
    
    
## ****************************
## Saeran
## ****************************
layeredimage saeran:   
    yoffset 170
    xoffset 70

    group body:
        attribute unknown "VN Mode/Unknown/unknown_body_unknown.png"
        attribute mask "VN Mode/Unknown/unknown_body_mask.png"
        attribute ray default "VN Mode/Unknown/unknown_body_ray.png"
        attribute saeran "VN Mode/Unknown/unknown_body_saeran.png"
        attribute suit "VN Mode/Unknown/unknown_body_suit.png"
    
    group face:
        align(0.41, 0.142)
        if_not "mask"        
        attribute happy "VN Mode/Unknown/unknown_face_0.png" 
        attribute smile "VN Mode/Unknown/unknown_face_1.png"
        attribute neutral default "VN Mode/Unknown/unknown_face_2.png"
        attribute angry "VN Mode/Unknown/unknown_face_3.png"
        attribute thinking "VN Mode/Unknown/unknown_face_4.png"
        attribute tense "VN Mode/Unknown/unknown_face_5.png"
        attribute creepy "VN Mode/Unknown/unknown_face_6.png"
        attribute cry "VN Mode/Unknown/unknown_face_7.png"
        attribute blush "VN Mode/Unknown/unknown_face_15.png"
        attribute sob "VN Mode/Unknown/unknown_face_16.png"
        attribute teary "VN Mode/Unknown/unknown_face_17.png"
        attribute nervous "VN Mode/Unknown/unknown_face_18.png"
        attribute sad "VN Mode/Unknown/unknown_face_19.png"
        attribute worried "VN Mode/Unknown/unknown_face_20.png"
        attribute distant "VN Mode/Unknown/unknown_face_21.png"
        
    group face:
        align(0.41, 0.142)
        if_any "mask"        
        attribute happy "VN Mode/Unknown/unknown_face_8.png" 
        attribute smile "VN Mode/Unknown/unknown_face_9.png"
        attribute neutral default "VN Mode/Unknown/unknown_face_10.png"
        attribute angry "VN Mode/Unknown/unknown_face_11.png"
        attribute thinking "VN Mode/Unknown/unknown_face_12.png"
        attribute tense "VN Mode/Unknown/unknown_face_13.png"
        attribute creepy "VN Mode/Unknown/unknown_face_14.png"
        
        
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
        align(0.4343, 0.111)
        attribute neutral default "VN Mode/V/v02_face_0.png" 
        attribute happy "VN Mode/V/v02_face_1.png"
        attribute angry "VN Mode/V/v02_face_2.png"
        attribute worried "VN Mode/V/v02_face_3.png"
        attribute thinking "VN Mode/V/v02_face_4.png"
        attribute talking "VN Mode/V/v02_face_5.png"
        attribute surprised "VN Mode/V/v02_face_6.png"
        attribute tense "VN Mode/V/v02_face_7.png"
        attribute sweating "VN Mode/V/v02_face_8.png"
        attribute sad "VN Mode/V/v02_face_9.png"
        attribute upset "VN Mode/V/v02_face_10.png"
        attribute concerned "VN Mode/V/v02_face_11.png"
        attribute regret "VN Mode/V/v02_face_12.png"
        attribute unsure "VN Mode/V/v02_face_13.png"
        attribute afraid "VN Mode/V/v02_face_14.png"
        
    group head:
        if_any "mint_eye"
        attribute hood_up "VN Mode/V/v02_hood_1.png" align(0.4, 0.0) yoffset -25
        attribute hood_down default "VN Mode/V/v02_hood_1_1.png" align(0.378, 0.2035)
        
layeredimage v side:    
    yoffset 210
    
    group body:
        attribute normal default "VN Mode/V/v_body_0.png"
        attribute short_hair "VN Mode/V/v_body_1.png"
        attribute long_hair "VN Mode/V/v_body_2.png"
        
    group face:
        ## No sunglasses
        if_not "glasses"
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
    
    group face:
        align(0.411, 0.108)
        if_any "glasses"
        attribute happy "VN Mode/V/v_face_0.png" 
        attribute angry "VN Mode/V/v_face_2.png"
        attribute neutral "VN Mode/V/v_face_4.png"
        attribute surprised "VN Mode/V/v_face_6.png"
        attribute thinking "VN Mode/V/v_face_8.png"
        attribute worried "VN Mode/V/v_face_10.png"
        attribute sweat "VN Mode/V/v_face_12.png"
        attribute shock "VN Mode/V/v_face_14.png"
        attribute afraid "VN Mode/V/v_face_16.png"
        attribute blush "VN Mode/V/v_face_18.png"
        attribute sad "VN Mode/V/v_face_20.png"
        attribute unsure "VN Mode/V/v_face_22.png"

    group eyewear:
        attribute glasses Transform('transparent.png', size=(10,10))
        
            
## ****************************
## Yoosung
## ****************************
layeredimage yoosung:
    
    group body:
        attribute normal default "VN Mode/Yoosung/yoosung_body_0.png"
        attribute arm "VN Mode/Yoosung/yoosung_body_1.png"
        attribute sweater "VN Mode/Yoosung/yoosung_body_2.png"
        attribute suit "VN Mode/Yoosung/yoosung_body_3.png"
        attribute party "VN Mode/Yoosung/yoosung_body_5.png"
        attribute bandage "VN Mode/Yoosung/yoosung_body_4.png"
        
    group face:
        align(0.256, 0.111)
        if_not ["bandage", "glasses"]
        attribute happy "VN Mode/Yoosung/yoosung_face_0.png"
        attribute angry "VN Mode/Yoosung/yoosung_face_2.png"
        attribute sparkle "VN Mode/Yoosung/yoosung_face_4.png"
        attribute neutral default "VN Mode/Yoosung/yoosung_face_6.png"
        attribute surprised "VN Mode/Yoosung/yoosung_face_7.png"
        attribute thinking "VN Mode/Yoosung/yoosung_face_8.png"
        attribute sad "VN Mode/Yoosung/yoosung_face_9.png"
        attribute grin "VN Mode/Yoosung/yoosung_face_10.png"
        attribute dark "VN Mode/Yoosung/yoosung_face_11.png"
        attribute tired "VN Mode/Yoosung/yoosung_face_12.png"
        attribute upset "VN Mode/Yoosung/yoosung_face_13.png"
        
    group face:
        align(0.256, 0.111)
        if_any "bandage"
        attribute happy  "VN Mode/Yoosung/yoosung_face_1.png" 
        attribute neutral default  "VN Mode/Yoosung/yoosung_face_3.png"
        attribute thinking  "VN Mode/Yoosung/yoosung_face_5.png"

    group face:      
        align(0.256, 0.111)
        if_any "glasses"
        attribute happy "VN Mode/Yoosung/yoosung_face_14.png" 
        attribute sparkle "VN Mode/Yoosung/yoosung_face_15.png"
        attribute neutral default "VN Mode/Yoosung/yoosung_face_16.png"
        attribute surprised "VN Mode/Yoosung/yoosung_face_17.png"
        attribute thinking "VN Mode/Yoosung/yoosung_face_18.png"
        attribute grin "VN Mode/Yoosung/yoosung_face_19.png"

    group eyewear:
        attribute glasses Transform('transparent.png', size=(10,10))
               
    
        
## ****************************
## Zen
## ****************************
layeredimage zen front:

    group body:        
        attribute arm "VN Mode/Zen/zen_body_arm.png" 
        attribute party "VN Mode/Zen/zen_body_party.png"
        attribute normal default "VN Mode/Zen/zen_body_pocket.png"
        
    group face:    
        align(0.428, 0.121)
        attribute happy "VN Mode/Zen/zen_face_0.png" 
        attribute angry "VN Mode/Zen/zen_face_1.png"
        attribute blush "VN Mode/Zen/zen_face_2.png" 
        attribute wink "VN Mode/Zen/zen_face_3.png"
        attribute neutral default "VN Mode/Zen/zen_face_4.png"
        attribute surprised "VN Mode/Zen/zen_face_5.png"
        attribute thinking "VN Mode/Zen/zen_face_6.png"
        attribute worried "VN Mode/Zen/zen_face_7.png"
        attribute oh "VN Mode/Zen/zen_face_8.png"
        attribute upset "VN Mode/Zen/zen_face_9.png"
        
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

layeredimage bodyguard_front:
    yoffset 50
    group body:
        attribute normal default "VN Mode/B01/b01_body_0.png"
        
    group face:
        align(0.397, 0.083)
        attribute neutral default "VN Mode/B01/b01_face_0.png" 
        attribute thinking "VN Mode/B01/b01_face_1.png"
        attribute stressed "VN Mode/B01/b01_face_2.png"
        
layeredimage bodyguard_side:
    yoffset 40
    group body:
        attribute normal default "VN Mode/B02/b02_body_0.png"
        
    group face:
        align(0.239, 0.105)
        attribute neutral default "VN Mode/B02/b02_face_0.png" 
        attribute thinking "VN Mode/B02/b02_face_1.png"
        attribute stressed "VN Mode/B02/b02_face_2.png"
        
## ****************************
## Chairman Han
## ****************************        

layeredimage chairman_han:
    yoffset 45
    group body:
        attribute normal default "VN Mode/Mr Chairman/han_body_0.png"
    
    group face:
        align(0.263, 0.088)
        attribute happy "VN Mode/Mr Chairman/han_face_0.png"
        attribute thinking "VN Mode/Mr Chairman/han_face_1.png" 
        attribute neutral default "VN Mode/Mr Chairman/han_face_2.png"
        attribute stressed "VN Mode/Mr Chairman/han_face_3.png"
        
## ****************************
## Echo Girl
## ****************************

layeredimage echo_girl:
    yoffset 70
    group body:
        attribute normal default "VN Mode/Echo girl/eco_body_0.png"
        
    group face:
        align(0.508, 0.09)
        attribute neutral default "VN Mode/Echo girl/eco_face_0.png" 
        attribute happy "VN Mode/Echo girl/eco_face_1.png"
        attribute angry "VN Mode/Echo girl/eco_face_2.png"
        attribute smile "VN Mode/Echo girl/eco_face_3.png"
        attribute surprised "VN Mode/Echo girl/eco_face_4.png"
        
        
## ****************************
## Glam Choi
## ****************************

layeredimage glam_choi:
    yoffset 115
    group body:
        attribute normal default "VN Mode/Glam Choi/glam_body_0.png"
        
    group face:
        align(0.4585, 0.099)
        attribute happy "VN Mode/Glam Choi/glam_face_0.png" 
        attribute smirk "VN Mode/Glam Choi/glam_face_1.png"
        attribute thinking "VN Mode/Glam Choi/glam_face_2.png"
        attribute neutral default "VN Mode/Glam Choi/glam_face_3.png"
        attribute stressed "VN Mode/Glam Choi/glam_face_4.png"
        attribute worried "VN Mode/Glam Choi/glam_face_5.png"
        
        
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
        align(0.233, 0.097)
        attribute happy "VN Mode/Sarah Choi/sara_face_0.png" 
        attribute excited "VN Mode/Sarah Choi/sara_face_1.png"
        attribute smirk "VN Mode/Sarah Choi/sara_face_2.png"
        attribute neutral default "VN Mode/Sarah Choi/sara_face_3.png"
        attribute stressed "VN Mode/Sarah Choi/sara_face_4.png"
        attribute sad "VN Mode/Sarah Choi/sara_face_5.png"
        
## ****************************
## Vanderwood
## **************************** 

layeredimage vanderwood:
    yoffset 20
    group body:
        attribute normal default "VN Mode/Vanderwood/van_body_0.png"
   
    group face:
        align(0.57, 0.112)
        attribute neutral default "VN Mode/Vanderwood/ven_face_0.png" 
        attribute unamused "VN Mode/Vanderwood/ven_face_1.png"
        attribute unsure "VN Mode/Vanderwood/ven_face_2.png"
        attribute determined "VN Mode/Vanderwood/ven_face_3.png"
        attribute ouch "VN Mode/Vanderwood/ven_face_4.png"
        attribute angry "VN Mode/Vanderwood/ven_face_5.png"
        
        
