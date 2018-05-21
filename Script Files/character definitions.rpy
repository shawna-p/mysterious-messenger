##****************************
##DECLARE CHARACTERS HERE
##****************************

## Chatroom character declarations
## Format is: name - nickname for the chatrooms; file_id - short form appended to file names
##  like speech bubbles and used in the heartcolour lookup; prof_pic - profile pic (110x110);
##  participant_pic - pic show show they're present in a chatroom; cover_pic/status  - as stated;
##  voicemail - generally set at the end of a chatroom, not during definition time

default s = Chat("707", 's', 'Profile Pics/Seven/sev-default.png', 'Profile Pics/s_chat.png', "Cover Photos/profile_cover_photo.png", "707's status")
default y = Chat("Yoosung★", 'y', 'Profile Pics/Yoosung/yoo-default.png', 'Profile Pics/y_chat.png', "Cover Photos/profile_cover_photo.png", "Yoosung's status")
default m = Chat("MC", 'm', 'Profile Pics/MC/MC-1.png')
default ja = Chat("Jaehee Kang", 'ja', 'Profile Pics/Jaehee/ja-default.png', 'Profile Pics/ja_chat.png', "Cover Photos/profile_cover_photo.png", "Jaehee's status")
default ju = Chat("Jumin Han", 'ju', 'Profile Pics/Jumin/ju-default.png', 'Profile Pics/ju_chat.png', "Cover Photos/profile_cover_photo.png", "Jumin's status")
default z = Chat("ZEN", 'z', 'Profile Pics/Zen/zen-default.png', 'Profile Pics/z_chat.png', "Cover Photos/profile_cover_photo.png", "Zen's status")
default ri = Chat("Rika", 'ri', 'Profile Pics/Rika/rika-default.png', 'Profile Pics/ri_chat.png', "Cover Photos/profile_cover_photo.png", "Rika's status")
default r = Chat("Ray", 'r', 'Profile Pics/Ray/ray-default.png', 'Profile Pics/r_chat.png', "Cover Photos/profile_cover_photo.png", "Ray's status")
default sa = Chat("Saeran", "sa", 'Profile Pics/Saeran/sae-1.png', 'Profile Pics/sa_chat.png', "Cover Photos/profile_cover_photo.png", "Saeran's status")
default u = Chat("Unknown", "u", 'Profile Pics/Unknown/Unknown-1.png', 'Profile Pics/u_chat.png', "Cover Photos/profile_cover_photo.png", "Unknown's status")
default v = Chat("V", 'v', 'Profile Pics/V/V-default.png', 'Profile Pics/v_chat.png', "Cover Photos/profile_cover_photo.png", "V's status")
   
# These are special 'characters' for additional features
define msg = Chat("msg")
define filler = Chat("filler")
define answer = Chat('answer', 'delete')
define chat_pause = Chat('pause', 'delete')

# You'll want to add a new character to this list so they show up
# in things like the profiles at the top of the screen
default character_list = [ju, z, s, y, ja, v, m, r, ri]

# Add a name & colour here if you'd like to add another heart icon
# The 'key' should be equal to the character's file_id
default heartcolour = {'s' : "#ff2626", 
                        'z' : "#c9c9c9", 
                        'ja' : "#d0b741", 
                        'ju' : "#a59aef", 
                        'y' : "#31ff26", 
                        'ri' : "#fcef5a",
                        'r' : "#b81d7b",
                        'v' : "#50b2bc",
                        'u' : "#ffffff",
                        'sa' : "#b81d7b",
                        } 
                        
                        
# ****************************
# Phone Call Characters
# ****************************

# These are separate from the characters above since they display more like VN mode
# You won't actually see their name in-game. For most purposes, you can just copy any character
# besides m_phone and replace the name with the name you want
define ja_phone = Character("Jaehee Kang", what_font= "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf", 
                            what_color="#fff", what_xalign=0.5, what_yalign=0.5, what_text_align=0.5)
define ju_phone = Character("Jumin Han", what_font= "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf", 
                            what_color="#fff", what_xalign=0.5, what_yalign=0.5, what_text_align=0.5)
define s_phone = Character("707", what_font= "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf", 
                            what_color="#fff", what_xalign=0.5, what_yalign=0.5, what_text_align=0.5)
define sa_phone = Character("Saeran", what_font= "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf", 
                            what_color="#fff", what_xalign=0.5, what_yalign=0.5, what_text_align=0.5)
define r_phone = Character("Ray", what_font= "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf", 
                            what_color="#fff", what_xalign=0.5, what_yalign=0.5, what_text_align=0.5)
define ri_phone = Character("Rika", what_font= "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf", 
                            what_color="#fff", what_xalign=0.5, what_yalign=0.5, what_text_align=0.5)
define y_phone = Character("Yoosung★", what_font= "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf", 
                            what_color="#fff", what_xalign=0.5, what_yalign=0.5, what_text_align=0.5)
define v_phone = Character("V", what_font= "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf", 
                            what_color="#fff", what_xalign=0.5, what_yalign=0.5, what_text_align=0.5)
define u_phone = Character("Unknown", what_font= "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf", 
                            what_color="#fff", what_xalign=0.5, what_yalign=0.5, what_text_align=0.5)
define z_phone = Character("Zen", what_font= "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf", 
                            what_color="#fff", what_xalign=0.5, what_yalign=0.5, what_text_align=0.5)
define m_phone = Character("MC", what_font= "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf", 
                            what_color="#a6a6a6", what_xalign=0.5, what_yalign=0.5, what_text_align=0.5)
define vmail_phone = Character('', what_font= "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf", 
                            what_color="#fff", what_xalign=0.5, what_yalign=0.5, what_text_align=0.5)
                            
# ****************************
# Text Messages
# ****************************         

# If you want a character to be able to send messages, define
# a Text_Message object with their Chat variable in the list below                 
default text_messages = [Text_Message(ju, []),
                        Text_Message(ja, []),
                        Text_Message(r, []),
                        Text_Message(ri, []),
                        Text_Message(s, []),
                        Text_Message(v, []),
                        Text_Message(y, []),
                        Text_Message(z, []),
                        
                        Text_Message(u, []),
                        Text_Message(sa, [])
                        ]
default text_queue = [Text_Message(ju, []),
                        Text_Message(ja, []),
                        Text_Message(r, []),
                        Text_Message(ri, []),
                        Text_Message(s, []),
                        Text_Message(v, []),
                        Text_Message(y, []),
                        Text_Message(z, []),
                        
                        Text_Message(u, []),
                        Text_Message(sa, [])
                        ]
