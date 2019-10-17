init -6 python:
    from datetime import datetime
    from datetime import date
    import copy
    
    # This defines another voice channel which the emoji sound effects play on
    # It lets you adjust the volume of the emojis separately from voice, music, and sfx
    renpy.music.register_channel("voice_sfx", mixer="voice_sfx", loop=False)
    
    def set_voicesfx_volume(value=None):
        if value is None:
            return MixerValue('voice_sfx')
        else:
            return SetMixer('voice_sfx', value)
            
    
    # A class that makes it much easier to fetch the time for any
    # given chat entry/text message/phone call/etc
    class myTime(object):
        def __init__(self, day=None):
        
            self.short_weekday = datetime.now().strftime('%a')  #e.g. Mon
            self.weekday = datetime.now().strftime('%A')        #e.g. Monday
            
            self.short_month = datetime.now().strftime('%b')    #e.g. Aug
            self.month = datetime.now().strftime('%B')          #e.g. August
            self.month_num = datetime.now().strftime('%m')      #e.g. 8
            
            self.year = datetime.now().strftime('%y')           #e.g. 2018
            
            # This small function is so you can set the day
            # manually for testing purposes
            if day == None:
                self.day = datetime.now().strftime('%d')
            else:
                self.day = day
            
            self.twelve_hour = datetime.now().strftime('%I')
            self.military_hour = datetime.now().strftime('%H')
            self.minute = datetime.now().strftime('%M')
            self.second = datetime.now().strftime('%S')
            self.am_pm = datetime.now().strftime('%p')
            
    # Function that returns a myTime object with the current time
    # Also lets you manually set the day for testing purposes
    def upTime(day=None):
        if day != None:
            return myTime(day)
        else:
            return myTime()

# This tells the program to randomly shuffle the order
# of responses
default shuffle = True

init python:
    # This lets us shuffle menu options
    renpy_menu = menu
    def menu(items):
        items = list(items)
        global shuffle
        if shuffle and shuffle != "last":
            renpy.random.shuffle(items)
        elif shuffle == "last":
            last = items.pop()
            renpy.random.shuffle(items)
            items.append(last)
        shuffle = True
        return renpy_menu(items)
    
    
    config.keymap['rollback'].remove('mousedown_4')

            
# Name of the currently played day, e.g. '1st'
default current_day = False     
# Number of the day the player is currently
# going through
default current_day_num = 0   
# Number of the day considered 'today'
default today_day_num = 0    
# Useful when unlocking the next 24 hours
# of chats in real-time mode
default unlock_24_time = False
# Keeps track of how far the game should
# continue expiring chatrooms until
default days_to_expire = 1
# Keeps a record of the current time to compare
# with load times so it knows when to make days
# available
default current_game_day = date.today()
# Lets the program know how to advance days when loading
default persistent.load_instr = False
# List of calls the player can make (outgoing)
default available_calls = []
# History of phone calls
default call_history = []
# If there's an incoming call after a chatroom,
# it will be defined here
default incoming_call = False #e.g. Phone_Call(ju)
# Lets the program know we're in VN mode
default vn_choice = False
# Keeps track of the current call the player is in
default current_call = False
# True if the player is beginning a new game
default starter_story = False

default preferences.afm_time = 15
default preferences.skip_unseen = True
default preferences.skip_after_choices = True

default mm_auto = "mm_auto_save"
default persistent.testing_mode = False


#************************************
# Chatroom Backgrounds
#************************************

image morning = "bg-morning-shake.png"
image evening = "bg-evening-shake.png"
image night = "bg-night-shake.png"
image earlyMorn = "bg-earlyMorn-shake.png"
image noon = "bg-noon-shake.png"
image hack = "bg-hack-shake.png"
image redhack = "bg-redhack-shake.png"
image redcrack = "be-redhack-crack-shake.png"
image black = "#000000"

image bg morning = "bg-morning.jpg"
image bg evening = "bg-evening.jpg"
image bg night = "bg-night.jpg"
image bg earlyMorn = "bg-earlyMorn.jpg"
image bg noon = "bg-noon.jpg"
image bg hack = "bg-hack.jpg"
image bg redhack = "bg-redhack.jpg"
image bg redcrack = "bg-redhack-crack.png"
# A starry night background with some static stars;
# used in menu screens
image bg starry_night = "Phone UI/bg-starry-night.png"

# ********************************
# Short forms/Startup Variables
# ********************************

#Analogue or Digital, hours, minutes, size, second hand, military time
default myClock = Clock(False, 0, 0, 150, False, False) 

# Extra variables since the player can
# choose their pronouns
default they = "they"
default them = "them"
default their = "their"
default theirs = "theirs"
default themself = "themself"
default they_re = "they're"
default They_re = "They're"
default They = "They"
default Them = "Them"
default Their = "Their"
default Theirs = "Theirs"
default Themself = "Themself" 
default is_are = "are"
default has_have = "have"
default s_verb = ""

default chatlog = []
# A list of the characters currently
# in the chatroom
default in_chat = []
default current_chatroom = Chat_History('day', 'title', 'auto', 'chatroom_label', '00:00')
default most_recent_chat = None
default name = 'Rainbow'
default hacked_effect = False

# Variable that checks if you're on a route or not
default persistent.on_route = False
# Variable that checks if it's the first time you've started the game
default persistent.first_boot = True
# Variable that determines if the program should run in real-time or not
default persistent.real_time = False
# Variable to check if we need to manually load the chat home screen
default persistent.manual_load = False


# This variable is set to True if you're viewing a chatroom
# in 'history'
default observing = False

# This is a variable that detects if you're choosing an option from a menu
# If so, it uses this variable to know it should disable most buttons
default choosing = False

# Variable that detects if the answer screen should be
# showing. Largely only useful if you view a CG when you should
# be answering a prompt
default pre_choosing = False

# Keeps track of the total number of hp (heart points) you've received per chatroom
default chatroom_hp = 0
# Keeps track of the total number of hg (hourglasses) you've earned per chatroom
default chatroom_hg = 0



# These are primarily used when setting the nickname colour
# via $ nickColour = black or $ nickColour = white
define white = "#ffffff"
define black = "#000000"

image new_sign = "Bubble/main01_new.png"

define _preferences.show_empty_window = False

                           
                                
#************************************
# Persistent Variables
#************************************

default persistent.pronoun = "non binary"

default persistent.jumin_voice = True
default persistent.zen_voice = True
default persistent.seven_voice = True
default persistent.yoosung_voice = True
default persistent.jaehee_voice = True
default persistent.other_voice = True

default persistent.MC_pic = 'Profile Pics/MC/MC-1.png'
default persistent.name = "Rainbow"

default persistent.HP = 0
default persistent.HG = 100

#************************************
# CGs
#************************************

# CGs are automatically resized in the chatroom, but you'll have to
# make sure the original dimensions are 750x1334
image general_cg1 = "CGs/common_album/cg-1.png"
image general_cg2 = "CGs/common_album/cg-2.png"
image seven_cg1 = "CGs/s_album/cg-1.png"
image saeran_cg1 = "CGs/r_album/cg-1.png"

default fullsizeCG = "general_cg1"
# This lets you know if there are new CGs in
# the album
default new_cg = False

image cg_frame = 'CGs/photo_frame.png'
image cg_frame_dark = 'CGs/photo_frame_dark.png'
image cg_label_common = 'CGs/label_bg_common.png'  
image cg_label_ja = 'CGs/label_bg_ja.png'  
image cg_label_ju = 'CGs/label_bg_ju.png'  
image cg_label_other = 'CGs/label_bg_other.png'  
image cg_label_r = 'CGs/label_bg_r.png'  
image cg_label_s = 'CGs/label_bg_s.png'  
image cg_label_u = 'CGs/label_bg_u.png'  
image cg_label_v = 'CGs/label_bg_v.png'  
image cg_label_y = 'CGs/label_bg_y.png'  
image cg_label_z = 'CGs/label_bg_z.png' 

image ja_album_cover = 'CGs/ja_album_cover.png'
image ju_album_cover = 'CGs/ju_album_cover.png'
image r_album_cover = 'CGs/r_album_cover.png'
image s_album_cover = 'CGs/s_album_cover.png'
image u_album_cover = 'CGs/u_album_cover.png'
image v_album_cover = 'CGs/v_album_cover.png'
image y_album_cover = 'CGs/y_album_cover.png'
image z_album_cover = 'CGs/z_album_cover.png'
image common_album_cover = 'CGs/common_album_cover.png'





##******************************
## Image Definitions - Menu
##******************************

# Character Greetings
image greet jaehee = "Phone UI/Main Menu/jaehee_greeting.png"
image greet jumin = "Phone UI/Main Menu/jumin_greeting.png"
image greet ray = "Phone UI/Main Menu/ray_greeting.png"
image greet rika = "Phone UI/Main Menu/rika_greeting.png"
image greet seven = "Phone UI/Main Menu/seven_greeting.png"
image greet unknown = "Phone UI/Main Menu/unknown_greeting.png"
image greet v = "Phone UI/Main Menu/v_greeting.png"
image greet yoosung = "Phone UI/Main Menu/yoosung_greeting.png"
image greet zen = "Phone UI/Main Menu/zen_greeting.png"
    
image greeting_bubble = Frame("Phone UI/Main Menu/greeting_bubble.png", 40, 10, 10, 10)
image greeting_panel = Frame("Phone UI/Main Menu/greeting_panel.png", 20, 20)

image rfa_greet:
    Text("{k=-1}>>>>>>>{/k}  Welcome to Rika's Fundraising Association", 
                color="#ffffff", size=30, slow=True, 
                font="fonts/NanumBarunpenR.ttf", slow_cps=8, bold=True)
    10.0
    "transparent.png"
    0.2
    repeat

# Background Menu Squares
image right_corner_menu = Frame("Phone UI/Main Menu/right_corner_menu.png", 45, 45)
image left_corner_menu = Frame("Phone UI/Main Menu/left_corner_menu.png", 45, 45)
image right_corner_menu_selected = Frame("Phone UI/Main Menu/right_corner_menu_selected.png", 45, 45)
image left_corner_menu_selected = Frame("Phone UI/Main Menu/left_corner_menu_selected.png", 45, 45)

# Menu Icons
image menu_after_ending = "Phone UI/Main Menu/after_ending.png"
image menu_dlc = "Phone UI/Main Menu/dlc.png"
image menu_history = "Phone UI/Main Menu/history.png"
image menu_save_load = "Phone UI/Main Menu/save_load.png"
image menu_original_story = "Phone UI/Main Menu/original_story.png"

# Settings panel
image menu_settings_panel = Frame("Phone UI/Main Menu/settings_sound_panel.png",60,200,60,120)
image menu_settings_panel_bright = Frame("Phone UI/Main Menu/settings_sound_panel_bright.png",60,200,60,120)
image menu_sound_sfx = "Phone UI/Main Menu/settings_sound_sfx.png"
image menu_other_box = Frame("Phone UI/Main Menu/settings_sound_sfx.png", 10, 10)
image menu_default_sounds = Frame("Phone UI/Main Menu/settings_sound_default.png",10,10)
image menu_ringtone_box = Frame("Phone UI/Main Menu/daychat01_3.png", 35, 35)

# Settings tabs
image menu_tab_inactive = Frame("Phone UI/Main Menu/settings_tab_inactive.png",10,10)
image menu_tab_inactive_hover2 = Frame("Phone UI/Main Menu/settings_tab_inactive_hover2.png",10,10)
image menu_tab_active = Frame("Phone UI/Main Menu/settings_tab_active.png",25,25)
image menu_tab_inactive_hover = Frame("Phone UI/Main Menu/settings_tab_inactive_hover.png",10,10)

# Header Images
image header_plus = "Phone UI/Main Menu/header_plus.png"
image header_plus_hover = "Phone UI/Main Menu/header_plus_hover.png"
image header_tray = "Phone UI/Main Menu/header_tray.png"
image header_hg = "Phone UI/Main Menu/header_hg.png"
image header_heart = "Phone UI/Main Menu/header_heart.png"

# Profile Page
image menu_header = Frame("Phone UI/Main Menu/menu_header.png", 0, 50) 
image menu_back = "Phone UI/Main Menu/menu_back_btn.png"
image save_btn = "Phone UI/Main Menu/menu_save_btn.png"
image load_btn = "Phone UI/Main Menu/menu_load_btn.png"
image name_line = "Phone UI/Main Menu/menu_underline.png"
image menu_edit = "Phone UI/Main Menu/menu_pencil_long.png"
image menu_check_edit = "Phone UI/Main Menu/menu_check_long.png"
          
image radio_on = "Phone UI/Main Menu/menu_radio_on.png"
image radio_off = "Phone UI/Main Menu/menu_radio_off.png"

image settings_gear = "Phone UI/Main Menu/menu_settings_gear.png"

# Save/Load
image save_auto_idle = Frame("Phone UI/Main Menu/save_auto_idle.png", 20, 20)
image save_auto_hover = Frame("Phone UI/Main Menu/save_auto_hover.png", 20, 20)

# Just for fun, this is the animation when you hover over the settings
# button. It makes the gear look like it's turning
image settings_gear_rotate:
    "Phone UI/Main Menu/menu_settings_gear.png"
    xpos 10
    ypos -10
    block:
        rotate 0
        linear 1.0 rotate 45
        repeat
        
# Other Settings
image menu_select_btn = Frame("Phone UI/Main Menu/menu_select_button.png",60,60)
image menu_select_btn_inactive = Frame("Phone UI/Main Menu/menu_select_button_inactive.png",60,60)
image menu_account_btn = "Phone UI/Main Menu/menu_account_button.png"
image menu_select_btn_hover = Frame("Phone UI/Main Menu/menu_select_button_hover.png",60,60)


## ********************************
## Chat Home Screen 
## ********************************

image gray_chatbtn = "Phone UI/Main Menu/Original Story/main01_chatbtn.png"
image gray_chatbtn_hover = "Phone UI/Main Menu/Original Story/main01_chatbtn_hover.png"
image rfa_chatcircle:
    "Phone UI/Main Menu/Original Story/main01_chatcircle.png"
    block:
        rotate 0
        alignaround(.5, .5)
        linear 13.0 rotate -360
        repeat        
image blue_chatcircle:
    "Phone UI/Main Menu/Original Story/main01_chatcircle_big.png"
    block:
        rotate 60
        alignaround(.5, .5)
        linear 4 rotate 420
        repeat
image chat_text = "Phone UI/Main Menu/Original Story/main01_chattext.png"
image chat_icon = "Phone UI/Main Menu/Original Story/main01_chaticon.png"
image gray_mainbtn = "Phone UI/Main Menu/Original Story/main01_mainbtn.png"
image blue_mainbtn = "Phone UI/Main Menu/Original Story/main01_mainbtn_lit.png"
image gray_mainbtn_hover = "Phone UI/Main Menu/Original Story/main01_mainbtn_hover.png"
image blue_mainbtn_hover = "Phone UI/Main Menu/Original Story/main01_mainbtn_lit_hover.png"
image gray_maincircle:
    "Phone UI/Main Menu/Original Story/main01_maincircle.png"
    block:
        rotate -120
        alignaround(.5, .5)
        linear 4 rotate -480
        repeat
image blue_maincircle:
    "Phone UI/Main Menu/Original Story/main01_maincircle_lit.png"
    block:
        rotate 180
        alignaround(.5, .5)
        linear 4 rotate 540
        repeat
image call_mainicon = "Phone UI/Main Menu/Original Story/main01_mainicon_call.png"
image email_mainicon = "Phone UI/Main Menu/Original Story/main01_mainicon_email.png"
image msg_mainicon = "Phone UI/Main Menu/Original Story/main01_mainicon_message.png"
image call_maintext = "Phone UI/Main Menu/Original Story/main01_maintext_call.png"
image email_maintext = "Phone UI/Main Menu/Original Story/main01_maintext_email.png"
image msg_maintext = "Phone UI/Main Menu/Original Story/main01_maintext_message.png"

image profile_pic_select_square = "Phone UI/Main Menu/Original Story/profile_pic_select_square.png"

image white_hex = "Phone UI/Main Menu/Original Story/main01_subbtn.png"
image blue_hex = "Phone UI/Main Menu/Original Story/main01_subbtn_lit.png"
image red_hex = "Phone UI/Main Menu/Original Story/main01_subbtn_shop.png"
image white_hex_hover = "Phone UI/Main Menu/Original Story/main01_subbtn_hover.png"
image blue_hex_hover = "Phone UI/Main Menu/Original Story/main01_subbtn_lit_hover.png"
image red_hex_hover = "Phone UI/Main Menu/Original Story/main01_subbtn_shop_hover.png"

image album_icon = "Phone UI/Main Menu/Original Story/main01_subicon_album.png"
image guest_icon = "Phone UI/Main Menu/Original Story/main01_subicon_guest.png"
image link_icon = "Phone UI/Main Menu/Original Story/main01_subicon_link.png"
image notice_icon = "Phone UI/Main Menu/Original Story/main01_subicon_notice.png"
image shop_icon = "Phone UI/Main Menu/Original Story/main01_subicon_shop.png"
image album_text = "Phone UI/Main Menu/Original Story/main01_subtext_album.png"
image guest_text = "Phone UI/Main Menu/Original Story/main01_subtext_guest.png"
image link_text = "Phone UI/Main Menu/Original Story/main01_subtext_link.png"
image notice_text = "Phone UI/Main Menu/Original Story/main01_subtext_notice.png"
image shop_text = "Phone UI/Main Menu/Original Story/main01_subtext_shop.png"


## ********************************
## Profile Picture Screen
## ********************************
image profile_outline = "Phone UI/Main Menu/Original Story/profile_outline.png"
image profile_cover_photo = "Cover Photos/profile_cover_photo.png"


image input_close = "Phone UI/Main Menu/main02_close_button.png"
image input_close_hover = "Phone UI/Main Menu/main02_close_button_hover.png"
image input_square = Frame("Phone UI/Main Menu/main02_text_input.png",40,40)
image input_popup_bkgr = Frame("Phone UI/Main Menu/menu_popup_bkgrd.png",70,70)
image input_popup_bkgr_hover = Frame("Phone UI/Main Menu/menu_popup_bkgrd_hover.png",70,70)
    
    



## ********************************
## Save & Load Images
## ********************************
image save_auto = "Phone UI/Main Menu/msgsl_icon_m.png"
image save_another = "Phone UI/Main Menu/msgsl_image_another.png"
image save_april = "Phone UI/Main Menu/msgsl_image_april.png"
image save_casual = "Phone UI/Main Menu/msgsl_image_casual.png"
image save_deep = "Phone UI/Main Menu/msgsl_image_deep.png"
image save_jaehee = "Phone UI/Main Menu/msgsl_image_jaehee.png"
image save_jumin = "Phone UI/Main Menu/msgsl_image_jumin.png"
image save_ray = "Phone UI/Main Menu/msgsl_image_ray.png"
image save_empty = "Phone UI/Main Menu/msgsl_image_save.png"
image save_seven = "Phone UI/Main Menu/msgsl_image_seven.png"
image save_v = "Phone UI/Main Menu/msgsl_image_v.png"
image save_xmas = "Phone UI/Main Menu/msgsl_image_xmas.png"
image save_yoosung = "Phone UI/Main Menu/msgsl_image_yoosung.png"
image save_zen = "Phone UI/Main Menu/msgsl_image_zen.png"


## ********************************
## Text Message Screen
## ********************************

image new_text_envelope = 'Text Messages/main03_email_unread.png'
image read_text_envelope = 'Text Messages/main03_email_read.png'
image new_text = 'Text Messages/new_text.png'
image header_envelope = 'Text Messages/header_envelope.png'

image message_idle_bkgr = Frame('Text Messages/message_idle_background.png',20,20,20,20)
image message_hover_bkgr = Frame('Text Messages/message_hover_background.png',20,20,20,20)
image unread_message_idle_bkgr = Frame('Text Messages/message_idle_background_unread.png',20,20,20,20)
image unread_message_hover_bkgr = Frame('Text Messages/message_hover_background_unread.png',20,20,20,20)

image text_msg_line = Frame('Text Messages/msgsl_line.png', 40,2)
image text_answer_active = 'Text Messages/msgsl_button_answer_active.png'
image text_answer_inactive = 'Text Messages/msgsl_button_answer_inactive.png'
image text_answer_text = 'Text Messages/msgsl_text_answer.png'
image text_answer_animation:
    'Text Messages/answer_animation/1.png'
    0.1
    'Text Messages/answer_animation/2.png'
    0.1
    'Text Messages/answer_animation/3.png'
    0.1
    'Text Messages/answer_animation/4.png'
    0.1
    'Text Messages/answer_animation/5.png'
    0.1
    'Text Messages/answer_animation/6.png'
    0.1
    'Text Messages/answer_animation/7.png'
    0.1
    'Text Messages/answer_animation/8.png'
    0.1
    'Text Messages/answer_animation/9.png'
    0.1
    'Text Messages/answer_animation/10.png'
    0.1
    'Text Messages/answer_animation/11.png'
    0.1
    'Text Messages/answer_animation/12.png'
    0.1
    'Text Messages/answer_animation/13.png'
    0.1
    'Text Messages/answer_animation/14.png'
    0.1
    'Text Messages/answer_animation/15.png'
    0.1
    'Text Messages/answer_animation/16.png'
    0.1
    'Text Messages/answer_animation/17.png'
    0.1
    repeat
    
image text_pause_button = 'Text Messages/msgsl_text_pause.png'
image text_play_button = 'Text Messages/msgsl_text_play.png'
    
image text_popup_bkgr = "Text Messages/msgsl_popup_edge.png"
image text_popup_msg = Frame("Text Messages/msgsl_popup_text_bg.png", 0,0)
image text_answer_idle = "Text Messages/chat-bg02_2.png"
image text_answer_hover = "Text Messages/chat-bg02_3.png"
image new_text_count = "Text Messages/new_msg_count.png"

## ********************************
## Chat Select Screen
## ********************************

image day_common1 = 'Phone UI/Day Select/day_common1.png'
image day_common2 = 'Phone UI/Day Select/day_common2.png'
image day_ja = 'Phone UI/Day Select/day_ja.png'
image day_ju = 'Phone UI/Day Select/day_ju.png'
image day_r = 'Phone UI/Day Select/day_r.png'
image day_s = 'Phone UI/Day Select/day_s.png'
image day_v = 'Phone UI/Day Select/day_v.png'
image day_y = 'Phone UI/Day Select/day_y.png'
image day_z = 'Phone UI/Day Select/day_z.png'
image day_selected = Frame('Phone UI/Day Select/daychat01_day_mint.png', 50, 50)
image day_selected_hover = Frame('Phone UI/Day Select/daychat01_day_mint_hover.png', 50, 50)
image day_inactive = Frame('Phone UI/Day Select/daychat01_day_inactive.png', 50, 50)
image day_active = Frame('Phone UI/Day Select/daychat01_day_active.png', 50, 50)
image day_active_hover = Frame('Phone UI/Day Select/daychat01_day_active_hover.png', 50, 50)
image day_reg_hacked = 'Phone UI/Day Select/chatlist_hacking.png'#, 341,220,277,125)
image day_reg_hacked_long = 'Phone UI/Day Select/chatlist_hacking_long.png'#, 341,220,277,125)

image hacked_white_squares:
    #'Phone UI/Day Select/chat_hacking_thick.png'
    #'Phone UI/Day Select/chat_hacking_thin.png'
    #'Phone UI/Day Select/chat-hacking_filled.png'

    block:
        choice:
            Transform('Phone UI/Day Select/chat_hacking_thin.png', yzoom=0.3, alpha=0.4, yoffset=800)
            pause 0.02
            Transform('Phone UI/Day Select/chat_hacking_thin.png', yzoom=0.3, alpha=0.0, yoffset=800)
            pause 0.02
        choice:
            Transform('Phone UI/Day Select/chat_hacking_thin.png', yzoom=0.3, alpha=0.4, yoffset=800)
            pause 0.02
            Transform('Phone UI/Day Select/chat_hacking_thin.png', yzoom=0.3, alpha=0.0, yoffset=800)
            pause 0.02
        choice:
            Transform('Phone UI/Day Select/chat_hacking_thin.png', yzoom=0.01, alpha=0.45, yoffset=720)
            pause 0.02
            Transform('Phone UI/Day Select/chat_hacking_thin.png', yzoom=1.0, alpha=0.95, yalign=0.6)
            pause 0.02
    block:
        choice:
            Transform('Phone UI/Day Select/chat_hacking_filled.png', yzoom=0.45, alpha=0.9, yalign=1.0)
            pause 0.02
            Transform('Phone UI/Day Select/chat_hacking_filled.png', yzoom=0.45, alpha=0.0, yalign=1.0)
            pause 0.03
        choice:
            Transform('Phone UI/Day Select/chat_hacking_thin.png', yzoom=1.0, alpha=0.95, yalign=0.6)
            pause 0.02
            Transform('Phone UI/Day Select/chat_hacking_filled.png', yzoom=0.3, alpha=0.8, yalign=1.0)
            pause 0.02
        choice:
            Transform('Phone UI/Day Select/chat_hacking_thick.png', yzoom=0.3, alpha=0.98, yalign=0.5)
            pause 0.02
            Transform('Phone UI/Day Select/chat_hacking_thick.png', yzoom=0.3, alpha=0.0, yalign=0.5)
            pause 0.04
    block:
        choice:
            Transform('Phone UI/Day Select/chat_hacking_thin.png', yzoom=1.0, alpha=0.95, yalign=0.6)
            pause 0.02
            Transform('Phone UI/Day Select/chat_hacking_filled.png', yzoom=0.4, alpha=0.8, yalign=0.85)
            pause 0.02
        choice:
            Transform('Phone UI/Day Select/chat_hacking_thin.png', yzoom=1.0, alpha=0.95, yalign=0.6)
            pause 0.02
            Transform('Phone UI/Day Select/chat_hacking_filled.png', yzoom=0.45, alpha=0.9, yalign=1.0)
            pause 0.02
        choice:
            Transform('Phone UI/Day Select/chat_hacking_filled.png', yzoom=0.45, alpha=0.0, yalign=1.0)
            pause 0.05
            Transform('Phone UI/Day Select/chat_hacking_thick.png', yzoom=0.3, alpha=0.98, yalign=0.5)
            pause 0.02
    block:
        choice:
            Transform('Phone UI/Day Select/chat_hacking_filled.png', yzoom=0.45, alpha=0.0, yalign=1.0)
            pause 0.1
            Transform('Phone UI/Day Select/chat_hacking_filled.png', yzoom=0.45, alpha=0.9, yalign=1.0)
            pause 0.02
        choice:
            Transform('Phone UI/Day Select/chat_hacking_thick.png', yzoom=0.3, alpha=0.98, yalign=0.5)
            pause 0.02
            Transform('Phone UI/Day Select/chat_hacking_thick.png', yzoom=0.1, alpha=0.7, yalign=0.6)
            pause 0.02
        choice:
            Transform('Phone UI/Day Select/chat_hacking_filled.png', yzoom=0.45, alpha=0.0, yalign=1.0)
            pause 0.05
            Transform('Phone UI/Day Select/chat_hacking_filled.png', yzoom=0.4, alpha=0.5, yalign=0.85)
            pause 0.02
    block:
        choice:
            Transform('Phone UI/Day Select/chat_hacking_filled.png', yzoom=0.45, alpha=0.0, yalign=1.0)
            pause 0.1
            Transform('Phone UI/Day Select/chat_hacking_filled.png', yzoom=0.45, alpha=0.9, yalign=1.0)
            pause 0.02
        choice:
            Transform('Phone UI/Day Select/chat_hacking_thick.png', yzoom=0.3, alpha=0.98, yalign=0.5)
            pause 0.02
            Transform('Phone UI/Day Select/chat_hacking_thick.png', yzoom=0.1, alpha=0.7, yalign=0.6)
            pause 0.02
        choice:
            Transform('Phone UI/Day Select/chat_hacking_filled.png', yzoom=0.45, alpha=0.0, yalign=1.0)
            pause 0.05
            Transform('Phone UI/Day Select/chat_hacking_filled.png', yzoom=0.4, alpha=0.5, yalign=0.85)
            pause 0.02
    block:
        choice:
            Transform('Phone UI/Day Select/chat_hacking_thin.png', yzoom=1.0, alpha=0.95, yalign=0.6)
            pause 0.02
            Transform('Phone UI/Day Select/chat_hacking_filled.png', yzoom=0.4, alpha=0.8, yalign=0.85)
            pause 0.02
        choice:
            Transform('Phone UI/Day Select/chat_hacking_thin.png', yzoom=1.0, alpha=0.95, yalign=0.6)
            pause 0.02
            Transform('Phone UI/Day Select/chat_hacking_filled.png', yzoom=0.45, alpha=0.9, yalign=1.0)
            pause 0.02
        choice:
            Transform('Phone UI/Day Select/chat_hacking_filled.png', yzoom=0.45, alpha=0.0, yalign=1.0)
            pause 0.05
            Transform('Phone UI/Day Select/chat_hacking_thick.png', yzoom=0.3, alpha=0.98, yalign=0.5)
            pause 0.02
    block:
        choice:
            Transform('Phone UI/Day Select/chat_hacking_thin.png', yzoom=0.3, alpha=0.4, yoffset=800)
            pause 0.02
            Transform('Phone UI/Day Select/chat_hacking_thin.png', yzoom=0.3, alpha=0.0, yoffset=800)
            pause 0.02
        choice:
            Transform('Phone UI/Day Select/chat_hacking_thin.png', yzoom=0.3, alpha=0.4, yoffset=800)
            pause 0.02
            Transform('Phone UI/Day Select/chat_hacking_thin.png', yzoom=0.3, alpha=0.0, yoffset=800)
            pause 0.02
        choice:
            Transform('Phone UI/Day Select/chat_hacking_thin.png', yzoom=0.01, alpha=0.45, yoffset=720)
            pause 0.02
            Transform('Phone UI/Day Select/chat_hacking_thin.png', yzoom=1.0, alpha=0.95, yalign=0.6)
            pause 0.02
    Transform('Phone UI/Day Select/chat_hacking_filled.png', yzoom=0.4, alpha=0.0, yalign=0.85)
            
  
    
image day_today:
    'Phone UI/Day Select/daychat_today.png'
    block:
        easein 0.5 yoffset -20
        easeout 0.5 yoffset 0
        repeat
image final_day = 'Phone UI/Day Select/daychat_finalday.png'
image day_percent = Frame('Phone UI/Day Select/daychat_percent.png', 15, 15)
image day_percent_bg = Frame('Phone UI/Day Select/daychat_percent_bg.png', 15, 15)
image day_percent_border = Frame('Phone UI/Day Select/daychat_percent_border.png', 15, 15)
image day_hlink = 'Phone UI/Day Select/daychat_hlink.png'
image plot_lock = 'Phone UI/Day Select/plot_lock.png'
image expired_chat = 'Phone UI/Day Select/daychat_hg.png'

image day_vlink = im.Tile('Phone UI/Day Select/daychat_vlink.png',(15,1180))
image vn_inactive = 'Phone UI/Day Select/vn_inactive.png'
image vn_selected = 'Phone UI/Day Select/daychat01_vn_mint.png'
image vn_active = 'Phone UI/Day Select/vn_active.png'
image vn_selected_hover = 'Phone UI/Day Select/daychat01_vn_mint_hover.png'
image vn_active_hover = 'Phone UI/Day Select/vn_active_hover.png'
image vn_marker = 'Phone UI/Day Select/daychat01_vn_marker.png'
image vn_time_bg = 'Phone UI/Day Select/daychat01_chat_timebg.png'

image chat_active = Frame('Phone UI/Day Select/daychat01_chat_active.png',190, 70, 40, 50)
image chat_inactive = Frame('Phone UI/Day Select/daychat01_chat_inactive.png',190, 70, 40, 50)
image chat_selected = Frame('Phone UI/Day Select/daychat01_chat_mint.png',190, 70, 40, 50)
image chat_active_hover = Frame('Phone UI/Day Select/daychat01_chat_active_hover.png',190, 70, 40, 50)
image chat_continue = Frame('Phone UI/Day Select/daychat01_chat_continue.png',190, 70, 40, 20)
image chat_selected_hover = Frame('Phone UI/Day Select/daychat01_chat_mint_hover.png',190, 70, 40, 50)
image chat_hover_box = Frame('Phone UI/Day Select/daychat_vn_selectable.png', 0,0,0,0)

image vn_other = 'Phone UI/Day Select/vn_other.png'
image vn_ja = 'Phone UI/Day Select/vn_ja.png'
image vn_ju = 'Phone UI/Day Select/vn_ju.png'
image vn_r = 'Phone UI/Day Select/vn_r.png'
image vn_ri = 'Phone UI/Day Select/vn_ri.png'
image vn_sa = 'Phone UI/Day Select/vn_sa.png'
image vn_s = 'Phone UI/Day Select/vn_s.png'
image vn_v = 'Phone UI/Day Select/vn_v.png'
image vn_y = 'Phone UI/Day Select/vn_y.png'
image vn_z = 'Phone UI/Day Select/vn_z.png'
image vn_party = 'Phone UI/Day Select/vn_party.png'
image vn_party_inactive = 'Phone UI/Day Select/vn_party_inactive.png'

## ********************************
## Phone Call Screen
## ********************************

image call_back = 'Phone UI/Phone Calls/call.png'

image call_signal_sl:
    Transform('Phone UI/Phone Calls/call_ani_0.png', xzoom=-1)
    block:
        alpha 0.0
        1.0
        alpha 0.8
        3.0
        repeat
image call_signal_ml:
    Transform('Phone UI/Phone Calls/call_ani_1.png', xzoom=-1)
    block:
        alpha 0.0
        2.0
        alpha 0.8
        2.0
        repeat
image call_signal_ll:
    Transform('Phone UI/Phone Calls/call_ani_2.png', xzoom=-1)
    block:
        alpha 0.0
        3.0
        alpha 0.8
        1.0
        repeat
image call_signal_sr:
    'Phone UI/Phone Calls/call_ani_0.png'
    block:
        alpha 0.0
        1.0
        alpha 0.8
        3.0
        repeat
image call_signal_mr:
    'Phone UI/Phone Calls/call_ani_1.png'
    block:
        alpha 0.0
        2.0
        alpha 0.8
        2.0
        repeat
image call_signal_lr:
    'Phone UI/Phone Calls/call_ani_2.png'
    block:
        alpha 0.0
        3.0
        alpha 0.8
        1.0
        repeat

image call_overlay = Frame('Phone UI/Phone Calls/call_back_screen.png', 0, 0)
image call_answer = 'Phone UI/Phone Calls/call_button_answer.png'
image call_hang_up = 'Phone UI/Phone Calls/call_button_hang_up.png'
image call_pause = 'Phone UI/Phone Calls/call_button_pause.png'
image call_play = 'Phone UI/Phone Calls/call_button_play.png'
image call_replay_active = 'Phone UI/Phone Calls/call_button_replay_active.png'
image call_replay_inactive = 'Phone UI/Phone Calls/call_button_replay_inactive.png'
image call_connect_triangle = 'Phone UI/Phone Calls/call_connect_waiting.png'

image sa_contact = 'Phone UI/Phone Calls/call_contact_saeran.png'
image s_contact = 'Phone UI/Phone Calls/call_contact_707.png'
image empty_contact = 'Phone UI/Phone Calls/call_contact_empty.png'
image ja_contact = 'Phone UI/Phone Calls/call_contact_jaehee.png'
image ju_contact = 'Phone UI/Phone Calls/call_contact_jumin.png'
image r_contact = 'Phone UI/Phone Calls/call_contact_ray.png'
image v_contact = 'Phone UI/Phone Calls/call_contact_v.png'
image y_contact = 'Phone UI/Phone Calls/call_contact_yoosung.png'
image z_contact = 'Phone UI/Phone Calls/call_contact_zen.png'
image ri_contact = 'Phone UI/Phone Calls/call_contact_rika.png'

image contact_icon = 'Phone UI/Phone Calls/call_icon_contacts.png'
image call_headphones = 'Phone UI/Phone Calls/call_icon_earphone_en.png'
image call_history_icon = 'Phone UI/Phone Calls/call_icon_history.png'
image call_incoming = 'Phone UI/Phone Calls/call_icon_incoming.png'
image call_missed = 'Phone UI/Phone Calls/call_icon_missed.png'
image call_outgoing = 'Phone UI/Phone Calls/call_icon_outgoing.png'
image call_voicemail = 'Phone UI/Phone Calls/call_icon_voicemail.png'

image call_choice = Frame('Phone UI/Phone Calls/call_select_button.png', 70, 70)
image call_choice_hover = Frame('Phone UI/Phone Calls/call_select_button_hover.png', 90, 90)

## ********************************
## Create-A-Chatroom/Route
## ********************************

image char_foreground = 'Phone UI/char_select_foreground.png'
image char_foreground2 = 'Phone UI/char_select_foreground2.png'

## ********************************
## Email Screen
## ********************************

image email_completed_3 = "Email/main03_email_completed_01.png"
image email_completed_2 = "Email/main03_completed_02.png"
image email_completed_1 = "Email/main03_completed_03.png"
image email_failed = "Email/main03_email_failed.png"
image email_timeout = "Email/main03_email_timeout.png"
image email_good = "Email/main03_email_good.png"
image email_bad = "Email/main03_email_bad.png"
image email_inactive = "Email/main03_email_inactive.png"
image email_panel = "Email/main03_email_panel.png"
image email_read = "Email/main03_email_read.png"
image email_replied = "Email/main03_email_replied.png"
image email_unread = "Email/main03_email_unread.png"
image email_next = "Email/main03_email_next_button.png"
image email_mint = "Email/main03_email_mint.png"
image white_transparent = Frame("Email/white_transparent.png", 0, 0)
image email_open_transparent = Frame("Email/email_open_transparent.png", 0, 0)
image left_corner_menu_dark = Frame("Email/left_corner_menu_dark.png", 45, 45)

