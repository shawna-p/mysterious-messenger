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

image morning = im.Scale("Morning Sky Background.png",750,1250)
image evening = im.Scale("Evening Background.png",750,1250)
image night = im.Scale("Deep Night Background.png",750,1250)
image earlyMorn = im.Scale("Night Background.png",750,1250)
image noon = im.Scale("Noon Background.png",750,1250)
image hack = im.Scale("Hack Background.png",750,1250)
image redhack = "Red-Hack-Background.png"    
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


default name = "MC"


# These are primarily used when setting the nickname colour
# via $ nickColour = black or $ nickColour = white
define white = "#ffffff"
define black = "#000000"



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

