## MUSIC AND OTHER SHORT FORM DECLARATIONS

init python:
    # This defines another voice channel which the emoji sound effects play on
    # There's also an additional slider in options.rpy 
    # This lets you adjust the volume of the emojis separately from voice, music, and sfx
    renpy.music.register_channel("voice_sfx", mixer="voice_sfx", loop=False)
    
    def set_voicesfx_volume(value=None):
        if value is None:
            return MixerValue('voice_sfx')
        else:
            return SetMixer('voice_sfx', value)


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

image morning = "bg-morning.jpg"
image evening = "bg-evening.jpg"
image night = "bg-night.jpg"
image earlyMorn = "bg-earlyMorn.jpg"
image noon = "bg-noon.jpg"
image hack = "bg-hack.jpg"
image redhack = "bg-redhack.jpg"
image black = "#000000"

image bg morning = "morning"
image bg evening = "evening"
image bg noon = "noon"
image bg night = "night"
image bg earlyMorn = "earlyMorn"
image bg hack = "hack"
image bg redhack = "redhack"


# ****************************
# *******Short Forms**********
# ****************************


# These are primarily used when setting the nickname colour
# via $ nickColour = black or $ nickColour = white
define white = "#ffffff"
define black = "#000000"

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
image seven_cg1 = "CGs/Seven/cg-1.png"
image saeran_cg1 = "CGs/Saeran/cg-1.png"

default fullsizeCG = "cg1"
         
## Currently unused
image new_messages = "Phone UI/new_message_banner.png"

