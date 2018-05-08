##******************************
## USEFUL PYTHON FUNCTIONS
##******************************
init python:
    from datetime import datetime
    
    # This defines another voice channel which the emoji sound effects play on
    # This lets you adjust the volume of the emojis separately from voice, music, and sfx
    renpy.music.register_channel("voice_sfx", mixer="voice_sfx", loop=False)
    
    def set_voicesfx_volume(value=None):
        if value is None:
            return MixerValue('voice_sfx')
        else:
            return SetMixer('voice_sfx', value)
            
    
    # A class that makes it much easier to fetch the time for any
    # given chat entry
    class myTime(object):
        def __init__(self, day=None):
        
            self.short_weekday = datetime.now().strftime('%a')
            self.weekday = datetime.now().strftime('%A')
            
            self.short_month = datetime.now().strftime('%b')
            self.month = datetime.now().strftime('%B')
            self.month_num = datetime.now().strftime('%m')
            
            self.year = datetime.now().strftime('%y')
            
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
    def upTime(day=None):
        if day != None:
            return myTime(day)
        else:
            return myTime()



##******************************
## BACKGROUND MUSIC DEFINITIONS
##******************************

## Casual/Deep Story
define mystic_chat = "Music/03 Mystic Chat.mp3"
define mystic_chat2 = "Music/04 Mystic Chat Ver.2.mp3"
define mysterious_clues = "Music/05 Mysterious Clues.mp3"
define urban_night_cityscape = "Music/06 Urban Night Cityscape.mp3"
define urban_night_cityscape_v2 = "Music/07 Urban Night Cityscape Ver.2.mp3"
define narcissistic_jazz = "Music/08 Narcissistic Jazz.mp3"
define lonely_but_passionate_way = "Music/09 Lonely But Passionate Way.mp3"
define geniusly_hacked_bebop = "Music/10 Geniusly Hacked Bedop.mp3"
define same_old_fresh_air = "Music/11 Same Old Fresh Air.mp3"
define silly_smile_again = "Music/12 Silly Smile Again.mp3"
define lonesome_practicalism = "Music/13 Lonesome Practicalism.mp3"
define lonesome_practicalism_v2 = "Music/14 Lonesome Practicalism Ver.2.mp3"
define i_miss_happy_rika = "Music/15 I Miss Happy Rika.mp3"
define dark_secret = "Music/16 Dark Secret.mp3"
define life_with_masks = "Music/17 Life With Masks.mp3"
define my_half_is_unknown = "Music/18 My Half Is Unknown.mp3"

## April Fool's
define april_dark_secret = "Music/Dark Secret (ver. April Fool's).mp3"
define april_mysterious_clues = "Music/Mysterious Clues (ver. April Fool's).mp3"
define april_mystic_chat = "Music/Mystic Chat (ver. April Fool's).mp3"

## Another Story
define endless_struggle = "Music/Endless Struggle.mp3"
define endless_struggle_guitar = "Music/Endless Struggle (ver. Guitar).mp3"
define endless_struggle_harp = "Music/Endless Struggle (ver. Harp).mp3"
define four_seasons_piano = "Music/Four Seasons (ver. Piano).mp3"
define i_am_the_strongest = "Music/I am the Strongest.mp3"
define i_am_the_strongest_piano = "Music/I am the Strongest (ver. Piano).mp3"
define i_am_the_strongest_harp = "Music/I am the Strongest (ver. Harp).mp3"
define i_draw = "Music/I Draw.mp3"
define i_draw_piano = "Music/I Draw (ver. Piano).mp3"
define light_and_daffodils_piano1 = "Music/Light and Daffodils (ver. Piano part 1).mp3"
define light_and_daffodils_piano2 = "Music/Light and Daffodils (ver. Piano part 2).mp3"
define mint_eye = "Music/Mint Eye.mp3"
define mint_eye_piano = "Music/Mint Eye (Piano ver.).mp3"
define suns_love = "Music/Sun's Love.mp3"
define suns_love_piano = "Music/Sun's Love (ver. Piano).mp3"
define the_compass_piano1 = "Music/The Compass (ver. Piano part 1).mp3"
define the_compass_piano2 = "Music/The Compass (ver. Piano part 2).mp3"

## Christmas
define xmax_life_with_masks = "Music/Life with Masks (ver. X-Mas Orgol).mp3"
define xmas_lonesome_practicalism = "Music/Lonesome Practicalism (ver. X-Mas Orgol).mp3"
define xmas_narcissistic_jazz = "Music/Narcissistic Jazz (ver. X-Mas Orgol).mp3"
define xmas_same_old_fresh_air = "Music/Same Old Fresh Air (ver. X-Mas Orgol).mp3"
define xmas_urban_night_cityscape = "Music/Urban Night Cityscape (ver. X-Mas Orgol).mp3"

#************************************
# Backgrounds
#************************************

image morning = "bg-morning-shake.png"
image evening = "bg-evening-shake.png"
image night = "bg-night-shake.png"
image earlyMorn = "bg-earlyMorn-shake.png"
image noon = "bg-noon-shake.png"
image hack = "bg-hack-shake.png"
image redhack = "bg-redhack-shake.png"
image black = "#000000"

image bg morning = "bg-morning.jpg"
image bg evening = "bg-evening.jpg"
image bg night = "bg-night.jpg"
image bg earlyMorn = "bg-earlyMorn.jpg"
image bg noon = "bg-noon.jpg"
image bg hack = "bg-hack.jpg"
image bg redhack = "bg-redhack.jpg"
# A starry night background with some static stars;
# used in menu screens
image bg starry_night = "Phone UI/bg-starry-night.png"

# ****************************
# Short forms/Other
# ****************************


# These are primarily used when setting the nickname colour
# via $ nickColour = black or $ nickColour = white
define white = "#ffffff"
define black = "#000000"

image new_sign = "Bubble/main01_new.png"

#************************************
# Menu Greeting Lookup
#************************************

# This *looks* long, but that's mostly just because there are a lot
# of different greetings. You can see in the function chat_greet defined
# at the top of menu screen.rpy that it essentially gets the time of day,
# then picks a random character for the greeting and picks a random
# greeting from those available. It's a dictionary where the item is a list
# and the key is the speaking character


define morning_greeting = {'jaehee': [ 'sfx/Main Menu Greetings/Jaehee/Morning/ja-m-1.wav',
                                'sfx/Main Menu Greetings/Jaehee/Morning/ja-m-2.wav',
                                'sfx/Main Menu Greetings/Jaehee/Morning/ja-m-3.wav',
                                'sfx/Main Menu Greetings/Jaehee/Morning/ja-m-4.wav' ],
                                
                    'jumin': [ 'sfx/Main Menu Greetings/Jumin/Morning/ju-m-1.wav',
                                'sfx/Main Menu Greetings/Jumin/Morning/ju-m-2.wav',
                                'sfx/Main Menu Greetings/Jumin/Morning/ju-m-3.wav',
                                'sfx/Main Menu Greetings/Jumin/Morning/ju-m-4.wav' ],
                                
                    'ray': [ 'sfx/Main Menu Greetings/Ray/Morning/ra-m-1.wav',
                                'sfx/Main Menu Greetings/Ray/Morning/ra-m-2.wav',
                                'sfx/Main Menu Greetings/Ray/Morning/ra-m-3.wav',
                                'sfx/Main Menu Greetings/Ray/Morning/ra-m-4.wav' ],
                                
                    'rika': [ 'sfx/Main Menu Greetings/Rika/Morning/r-m-1.wav',
                                'sfx/Main Menu Greetings/Rika/Morning/r-m-2.wav',
                                'sfx/Main Menu Greetings/Rika/Morning/r-m-3.wav',
                                'sfx/Main Menu Greetings/Rika/Morning/r-m-4.wav' ],
                                
                    'seven': [ 'sfx/Main Menu Greetings/Seven/Morning/s-m-1.wav',
                                'sfx/Main Menu Greetings/Seven/Morning/s-m-2.wav',
                                'sfx/Main Menu Greetings/Seven/Morning/s-m-3.wav',
                                'sfx/Main Menu Greetings/Seven/Morning/s-m-4.wav' ],
                                
                    'unknown': [ 'sfx/Main Menu Greetings/Unknown/Morning/u-m-1.wav',
                                'sfx/Main Menu Greetings/Unknown/Morning/u-m-2.wav',
                                'sfx/Main Menu Greetings/Unknown/Morning/u-m-3.wav' ],
                                
                    'v': [ 'sfx/Main Menu Greetings/V/Morning/v-m-1.wav',
                                'sfx/Main Menu Greetings/V/Morning/v-m-2.wav',
                                'sfx/Main Menu Greetings/V/Morning/v-m-3.wav',
                                'sfx/Main Menu Greetings/V/Morning/v-m-4.wav' ],
                                
                    'yoosung': [ 'sfx/Main Menu Greetings/Yoosung/Morning/y-m-1.wav',
                                'sfx/Main Menu Greetings/Yoosung/Morning/y-m-2.wav',
                                'sfx/Main Menu Greetings/Yoosung/Morning/y-m-3.wav',
                                'sfx/Main Menu Greetings/Yoosung/Morning/y-m-4.wav' ],
                                
                    'zen': [ 'sfx/Main Menu Greetings/Zen/Morning/z-m-1.wav',
                                'sfx/Main Menu Greetings/Zen/Morning/z-m-2.wav',
                                'sfx/Main Menu Greetings/Zen/Morning/z-m-3.wav',
                                'sfx/Main Menu Greetings/Zen/Morning/z-m-4.wav' ] }
                                
define afternoon_greeting = {'jaehee': [ 'sfx/Main Menu Greetings/Jaehee/Afternoon/ja-a-1.wav',
                                'sfx/Main Menu Greetings/Jaehee/Afternoon/ja-a-2.wav',
                                'sfx/Main Menu Greetings/Jaehee/Afternoon/ja-a-3.wav',
                                'sfx/Main Menu Greetings/Jaehee/Afternoon/ja-a-4.wav' ],
                                
                    'jumin': [ 'sfx/Main Menu Greetings/Jumin/Afternoon/ju-a-1.wav',
                                'sfx/Main Menu Greetings/Jumin/Afternoon/ju-a-2.wav',
                                'sfx/Main Menu Greetings/Jumin/Afternoon/ju-a-3.wav',
                                'sfx/Main Menu Greetings/Jumin/Afternoon/ju-a-4.wav' ],
                                
                    'ray': [ 'sfx/Main Menu Greetings/Ray/Afternoon/ra-a-1.wav',
                                'sfx/Main Menu Greetings/Ray/Afternoon/ra-a-2.wav',
                                'sfx/Main Menu Greetings/Ray/Afternoon/ra-a-3.wav',
                                'sfx/Main Menu Greetings/Ray/Afternoon/ra-a-4.wav' ],
                                
                    'rika': [ 'sfx/Main Menu Greetings/Rika/Afternoon/r-a-1.wav',
                                'sfx/Main Menu Greetings/Rika/Afternoon/r-a-2.wav',
                                'sfx/Main Menu Greetings/Rika/Afternoon/r-a-3.wav',
                                'sfx/Main Menu Greetings/Rika/Afternoon/r-a-4.wav' ],
                                
                    'seven': [ 'sfx/Main Menu Greetings/Seven/Afternoon/s-a-1.wav',
                                'sfx/Main Menu Greetings/Seven/Afternoon/s-a-2.wav',
                                'sfx/Main Menu Greetings/Seven/Afternoon/s-a-3.wav',
                                'sfx/Main Menu Greetings/Seven/Afternoon/s-a-4.wav' ],
                                
                    'unknown': [ 'sfx/Main Menu Greetings/Unknown/Afternoon/u-a-1.wav',
                                'sfx/Main Menu Greetings/Unknown/Afternoon/u-a-2.wav',
                                'sfx/Main Menu Greetings/Unknown/Afternoon/u-a-3.wav' ],
                                
                    'v': [ 'sfx/Main Menu Greetings/V/Afternoon/v-a-1.wav',
                                'sfx/Main Menu Greetings/V/Afternoon/v-a-2.wav',
                                'sfx/Main Menu Greetings/V/Afternoon/v-a-3.wav',
                                'sfx/Main Menu Greetings/V/Afternoon/v-a-4.wav' ],
                                
                    'yoosung': [ 'sfx/Main Menu Greetings/Yoosung/Afternoon/y-a-1.wav',
                                'sfx/Main Menu Greetings/Yoosung/Afternoon/y-a-2.wav',
                                'sfx/Main Menu Greetings/Yoosung/Afternoon/y-a-3.wav',
                                'sfx/Main Menu Greetings/Yoosung/Afternoon/y-a-4.wav' ],
                                
                    'zen': [ 'sfx/Main Menu Greetings/Zen/Afternoon/z-a-1.wav',
                                'sfx/Main Menu Greetings/Zen/Afternoon/z-a-2.wav',
                                'sfx/Main Menu Greetings/Zen/Afternoon/z-a-3.wav',
                                'sfx/Main Menu Greetings/Zen/Afternoon/z-a-4.wav' ] }
                                
define evening_greeting = {'jaehee': [ 'sfx/Main Menu Greetings/Jaehee/Evening/ja-e-1.wav',
                                'sfx/Main Menu Greetings/Jaehee/Evening/ja-e-2.wav',
                                'sfx/Main Menu Greetings/Jaehee/Evening/ja-e-3.wav',
                                'sfx/Main Menu Greetings/Jaehee/Evening/ja-e-4.wav' ],
                                
                    'jumin': [ 'sfx/Main Menu Greetings/Jumin/Evening/ju-e-1.wav',
                                'sfx/Main Menu Greetings/Jumin/Evening/ju-e-2.wav',
                                'sfx/Main Menu Greetings/Jumin/Evening/ju-e-3.wav',
                                'sfx/Main Menu Greetings/Jumin/Evening/ju-e-4.wav' ],
                                
                    'ray': [ 'sfx/Main Menu Greetings/Ray/Evening/ra-e-1.wav',
                                'sfx/Main Menu Greetings/Ray/Evening/ra-e-2.wav',
                                'sfx/Main Menu Greetings/Ray/Evening/ra-e-3.wav',
                                'sfx/Main Menu Greetings/Ray/Evening/ra-e-4.wav' ],
                                
                    'rika': [ 'sfx/Main Menu Greetings/Rika/Evening/r-e-1.wav',
                                'sfx/Main Menu Greetings/Rika/Evening/r-e-2.wav',
                                'sfx/Main Menu Greetings/Rika/Evening/r-e-3.wav',
                                'sfx/Main Menu Greetings/Rika/Evening/r-e-4.wav' ],
                                
                    'seven': [ 'sfx/Main Menu Greetings/Seven/Evening/s-e-1.wav',
                                'sfx/Main Menu Greetings/Seven/Evening/s-e-2.wav',
                                'sfx/Main Menu Greetings/Seven/Evening/s-e-3.wav',
                                'sfx/Main Menu Greetings/Seven/Evening/s-e-4.wav' ],
                                
                    'unknown': [ 'sfx/Main Menu Greetings/Unknown/Evening/u-e-1.wav',
                                'sfx/Main Menu Greetings/Unknown/Evening/u-e-2.wav',
                                'sfx/Main Menu Greetings/Unknown/Evening/u-e-3.wav' ],
                                
                    'v': [ 'sfx/Main Menu Greetings/V/Evening/v-e-1.wav',
                                'sfx/Main Menu Greetings/V/Evening/v-e-2.wav',
                                'sfx/Main Menu Greetings/V/Evening/v-e-3.wav',
                                'sfx/Main Menu Greetings/V/Evening/v-e-4.wav' ],
                                
                    'yoosung': [ 'sfx/Main Menu Greetings/Yoosung/Evening/y-e-1.wav',
                                'sfx/Main Menu Greetings/Yoosung/Evening/y-e-2.wav',
                                'sfx/Main Menu Greetings/Yoosung/Evening/y-e-3.wav',
                                'sfx/Main Menu Greetings/Yoosung/Evening/y-e-4.wav' ],
                                
                    'zen': [ 'sfx/Main Menu Greetings/Zen/Evening/z-e-1.wav',
                                'sfx/Main Menu Greetings/Zen/Evening/z-e-2.wav',
                                'sfx/Main Menu Greetings/Zen/Evening/z-e-3.wav',
                                'sfx/Main Menu Greetings/Zen/Evening/z-e-4.wav' ] }                    

define night_greeting = {'jaehee': [ 'sfx/Main Menu Greetings/Jaehee/Night/ja-n-1.wav',
                                'sfx/Main Menu Greetings/Jaehee/Night/ja-n-2.wav',
                                'sfx/Main Menu Greetings/Jaehee/Night/ja-n-3.wav',
                                'sfx/Main Menu Greetings/Jaehee/Night/ja-n-4.wav' ],
                                
                    'jumin': [ 'sfx/Main Menu Greetings/Jumin/Night/ju-n-1.wav',
                                'sfx/Main Menu Greetings/Jumin/Night/ju-n-2.wav',
                                'sfx/Main Menu Greetings/Jumin/Night/ju-n-3.wav',
                                'sfx/Main Menu Greetings/Jumin/Night/ju-n-4.wav' ],
                                
                    'ray': [ 'sfx/Main Menu Greetings/Ray/Night/ra-n-1.wav',
                                'sfx/Main Menu Greetings/Ray/Night/ra-n-2.wav',
                                'sfx/Main Menu Greetings/Ray/Night/ra-n-3.wav',
                                'sfx/Main Menu Greetings/Ray/Night/ra-n-4.wav' ],
                                
                    'rika': [ 'sfx/Main Menu Greetings/Rika/Night/r-n-1.wav',
                                'sfx/Main Menu Greetings/Rika/Night/r-n-2.wav',
                                'sfx/Main Menu Greetings/Rika/Night/r-n-3.wav',
                                'sfx/Main Menu Greetings/Rika/Night/r-n-4.wav' ],
                                
                    'seven': [ 'sfx/Main Menu Greetings/Seven/Night/s-n-1.wav',
                                'sfx/Main Menu Greetings/Seven/Night/s-n-2.wav',
                                'sfx/Main Menu Greetings/Seven/Night/s-n-3.wav',
                                'sfx/Main Menu Greetings/Seven/Night/s-n-4.wav' ],
                                
                    'unknown': [ 'sfx/Main Menu Greetings/Unknown/Night/u-n-1.wav',
                                'sfx/Main Menu Greetings/Unknown/Night/u-n-2.wav',
                                'sfx/Main Menu Greetings/Unknown/Night/u-n-3.wav' ],
                                
                    'v': [ 'sfx/Main Menu Greetings/V/Night/v-n-1.wav',
                                'sfx/Main Menu Greetings/V/Night/v-n-2.wav',
                                'sfx/Main Menu Greetings/V/Night/v-n-3.wav',
                                'sfx/Main Menu Greetings/V/Night/v-n-4.wav' ],
                                
                    'yoosung': [ 'sfx/Main Menu Greetings/Yoosung/Night/y-n-1.wav',
                                'sfx/Main Menu Greetings/Yoosung/Night/y-n-2.wav',
                                'sfx/Main Menu Greetings/Yoosung/Night/y-n-3.wav',
                                'sfx/Main Menu Greetings/Yoosung/Night/y-n-4.wav' ],
                                
                    'zen': [ 'sfx/Main Menu Greetings/Zen/Night/z-n-1.wav',
                                'sfx/Main Menu Greetings/Zen/Night/z-n-2.wav',
                                'sfx/Main Menu Greetings/Zen/Night/z-n-3.wav',
                                'sfx/Main Menu Greetings/Zen/Night/z-n-4.wav' ] }
                                
define late_night_greeting = {'jaehee': [ 'sfx/Main Menu Greetings/Jaehee/Morning/ja-m-1.wav',
                                'sfx/Main Menu Greetings/Jaehee/Late Night/ja-ln-2.wav',
                                'sfx/Main Menu Greetings/Jaehee/Late Night/ja-ln-3.wav',
                                'sfx/Main Menu Greetings/Jaehee/Late Night/ja-ln-4.wav' ],
                                
                    'jumin': [ 'sfx/Main Menu Greetings/Jumin/Late Night/ju-ln-1.wav',
                                'sfx/Main Menu Greetings/Jumin/Late Night/ju-ln-2.wav',
                                'sfx/Main Menu Greetings/Jumin/Late Night/ju-ln-3.wav',
                                'sfx/Main Menu Greetings/Jumin/Late Night/ju-ln-4.wav' ],
                                
                    'ray': [ 'sfx/Main Menu Greetings/Ray/Late Night/ra-ln-1.wav',
                                'sfx/Main Menu Greetings/Ray/Late Night/ra-ln-2.wav',
                                'sfx/Main Menu Greetings/Ray/Late Night/ra-ln-3.wav',
                                'sfx/Main Menu Greetings/Ray/Late Night/ra-ln-4.wav' ],
                                
                    'rika': [ 'sfx/Main Menu Greetings/Rika/Late Night/r-ln-1.wav',
                                'sfx/Main Menu Greetings/Rika/Late Night/r-ln-2.wav',
                                'sfx/Main Menu Greetings/Rika/Late Night/r-ln-3.wav',
                                'sfx/Main Menu Greetings/Rika/Late Night/r-ln-4.wav' ],
                                
                    'seven': [ 'sfx/Main Menu Greetings/Seven/Late Night/s-ln-1.wav',
                                'sfx/Main Menu Greetings/Seven/Late Night/s-ln-2.wav',
                                'sfx/Main Menu Greetings/Seven/Late Night/s-ln-3.wav',
                                'sfx/Main Menu Greetings/Seven/Late Night/s-ln-4.wav' ],
                                
                    'unknown': [ 'sfx/Main Menu Greetings/Unknown/Late Night/u-ln-1.wav',
                                'sfx/Main Menu Greetings/Unknown/Late Night/u-ln-2.wav',
                                'sfx/Main Menu Greetings/Unknown/Late Night/u-ln-3.wav' ],
                                
                    'v': [ 'sfx/Main Menu Greetings/V/Late Night/v-ln-1.wav',
                                'sfx/Main Menu Greetings/V/Late Night/v-ln-2.wav',
                                'sfx/Main Menu Greetings/V/Late Night/v-ln-3.wav',
                                'sfx/Main Menu Greetings/V/Late Night/v-ln-4.wav' ],
                                
                    'yoosung': [ 'sfx/Main Menu Greetings/Yoosung/Late Night/y-ln-1.wav',
                                'sfx/Main Menu Greetings/Yoosung/Late Night/y-ln-2.wav',
                                'sfx/Main Menu Greetings/Yoosung/Late Night/y-ln-3.wav',
                                'sfx/Main Menu Greetings/Yoosung/Late Night/y-ln-4.wav' ],
                                
                    'zen': [ 'sfx/Main Menu Greetings/Zen/Late Night/z-ln-1.wav',
                                'sfx/Main Menu Greetings/Zen/Late Night/z-ln-2.wav',
                                'sfx/Main Menu Greetings/Zen/Late Night/z-ln-3.wav',
                                'sfx/Main Menu Greetings/Zen/Late Night/z-ln-4.wav' ] }                                
                                
#************************************
# Persistent Variables
#************************************

default persistent.pronoun = "nonbinary"

default persistent.jumin_voice = True
default persistent.zen_voice = True
default persistent.seven_voice = True
default persistent.yoosung_voice = True
default persistent.jaehee_voice = True
default persistent.other_voice = True

default persistent.MC_pic = 1
default persistent.name = "Song"

default persistent.HP = 0
default persistent.HG = 100

#************************************
# CGs
#************************************

# CGs are automatically resized in the chatroom, but you'll have to
# make sure the original dimensions are 750x1334
image general_cg1 = "CGs/General/cg-1.png"
image general_cg2 = "CGs/General/cg-2.png"
image seven_cg1 = "CGs/Seven/cg-1.png"
image saeran_cg1 = "CGs/Saeran/cg-1.png"

default fullsizeCG = "cg1"
         
## Currently unused
image new_messages = "Phone UI/new_message_banner.png"


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
    Text("{k=-1}>>>>>>>{/k}  Welcome to Rika's Fundraising Association", color="#ffffff", size=30, slow=True, font="00 fonts/NanumBarunpenR.ttf", slow_cps=8, bold=True)
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
image menu_sound_sfx = "Phone UI/Main Menu/settings_sound_sfx.png"
image menu_default_sounds = Frame("Phone UI/Main Menu/settings_sound_default.png",10,10)

# Settings tabs
image menu_tab_inactive = Frame("Phone UI/Main Menu/settings_tab_inactive.png",10,10)
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

image MC_profpic = ConditionSwitch(
    "persistent.MC_pic == 1", im.FactorScale("Profile Pics/MC/MC-1.png",3.3),
    "persistent.MC_pic == 2", im.FactorScale("Profile Pics/MC/MC-2.png",3.3),
    "persistent.MC_pic == 3", im.FactorScale("Profile Pics/MC/MC-3.png",3.3),
    "persistent.MC_pic == 4", im.FactorScale("Profile Pics/MC/MC-4.png",3.3),
    "persistent.MC_pic == 5", im.FactorScale("Profile Pics/MC/MC-5.png",3.3),
    "True", "Profile Pics/MC/MC-1.png")
          
image radio_on = "Phone UI/Main Menu/menu_radio_on.png"
image radio_off = "Phone UI/Main Menu/menu_radio_off.png"

image settings_gear = "Phone UI/Main Menu/menu_settings_gear.png"

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
image menu_account_btn = "Phone UI/Main Menu/menu_account_button.png"
image menu_select_btn_hover = Frame("Phone UI/Main Menu/menu_select_button_hover.png",60,60)

## ********************************
## Chat Home Screen ***************
## ********************************
image gray_chatbtn = "Phone UI/Main Menu/Original Story/main01_chatbtn.png"
image gray_chatbtn_hover = "Phone UI/Main Menu/Original Story/main01_chatbtn_hover.png"
image rfa_chatcircle:
    "Phone UI/Main Menu/Original Story/main01_chatcircle.png"
    block:
        rotate 0
        alignaround(.5, .5)
        linear 13.0 rotate 360
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


# Profile Picture screen
image profile_outline = "Phone UI/Main Menu/Original Story/profile_outline.png"
image profile_cover_photo = "Phone UI/Main Menu/Original Story/profile_cover_photo.png"

### Spaceship
image space_chip_active:
    "Phone UI/Main Menu/Original Story/Spaceship/spaceship_chip_inactive.png"
    2.7
    block:
        "Phone UI/Main Menu/Original Story/Spaceship/spaceship_chip_active.png"
        1.16
        "Phone UI/Main Menu/Original Story/Spaceship/spaceship_chip_glow.png"
        1.16
        repeat
image space_chip_active2:
    "Phone UI/Main Menu/Original Story/Spaceship/spaceship_chip_active.png"
    1.16
    "Phone UI/Main Menu/Original Story/Spaceship/spaceship_chip_glow.png"
    1.16
    repeat    
image space_chip_explode = "Phone UI/Main Menu/Original Story/Spaceship/spaceship_chip_explode.png"
image space_chip_inactive = "Phone UI/Main Menu/Original Story/Spaceship/spaceship_chip_inactive.png"
image space_dot_line = "Phone UI/Main Menu/Original Story/Spaceship/dot_line.png"
image space_gray_dot = "Phone UI/Main Menu/Original Story/Spaceship/spaceship_dot_white.png"
image space_yellow_dot = "Phone UI/Main Menu/Original Story/Spaceship/spaceship_dot_yellow.png"
image space_transparent_btn = "Phone UI/Main Menu/Original Story/Spaceship/space-transparent-button.png"
image spaceship = "Phone UI/Main Menu/Original Story/Spaceship/spaceship_craft.png"
image space_flame:
    "Phone UI/Main Menu/Original Story/Spaceship/spaceship_flame_big.png"
    0.6
    "Phone UI/Main Menu/Original Story/Spaceship/spaceship_flame_small.png"
    0.6
    repeat
image input_close = "Phone UI/Main Menu/main02_close_button.png"
image input_close_hover = "Phone UI/Main Menu/main02_close_button_hover.png"
image input_square = Frame("Phone UI/Main Menu/main02_text_input.png",40,40)
image input_popup_bkgr = Frame("Phone UI/Main Menu/menu_popup_bkgrd.png",70,70)
    
    

## Spaceship chip animation
image space_chip = "Phone UI/Main Menu/Original Story/Spaceship/chip.png"
image space_tap_large:
    "Phone UI/Main Menu/Original Story/Spaceship/tap_0.png"
    0.55
    "Phone UI/Main Menu/Original Story/Spaceship/tap_1.png"
    0.6
    repeat
image space_tap_med:
    "Phone UI/Main Menu/Original Story/Spaceship/tap_1.png"
    0.62
    "Phone UI/Main Menu/Original Story/Spaceship/tap_0.png"
    0.45
    repeat
image space_tap_small:
    "Phone UI/Main Menu/Original Story/Spaceship/tap_0.png"
    0.48
    "Phone UI/Main Menu/Original Story/Spaceship/tap_1.png"
    0.56
    repeat    
image space_tap_to_close = "Phone UI/Main Menu/Original Story/Spaceship/close.png"

image cloud_1 = "Phone UI/Main Menu/Original Story/Spaceship/cloud_1.png"
image cloud_2 = "Phone UI/Main Menu/Original Story/Spaceship/cloud_2.png"
image cloud_3 = "Phone UI/Main Menu/Original Story/Spaceship/cloud_3.png"
image cloud_4 = "Phone UI/Main Menu/Original Story/Spaceship/cloud_4.png"
image cloud_5 = "Phone UI/Main Menu/Original Story/Spaceship/cloud_5.png"

image spotlight:
    "Phone UI/Main Menu/Original Story/Spaceship/spotlight.png"
    alpha 0.6
    block:
        rotate 0
        linear 15.0 rotate 360
        repeat
        
image space_prize_box = "Phone UI/Main Menu/Original Story/Spaceship/space_prize_box.png"
image space_black_box = Frame("Phone UI/Main Menu/Original Story/Spaceship/main03_black_box.png",30,30,30,30)
image space_continue = "Phone UI/Main Menu/Original Story/Spaceship/Continue.png"
image space_continue_hover = "Phone UI/Main Menu/Original Story/Spaceship/Continue_hover.png"

## Save & Load Images
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
## Text Message Screen ************
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
    
image text_popup_bkgr = "Text Messages/msgsl_popup_edge.png"
image text_popup_msg = Frame("Text Messages/msgsl_popup_text_bg.png", 0,0)
image text_answer_idle = "Text Messages/chat-bg02_2.png"
image text_answer_hover = "Text Messages/chat-bg02_3.png"
image new_text_count = "Text Messages/new_msg_count.png"