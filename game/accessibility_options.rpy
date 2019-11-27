## Accessibility functions #####################################################
##
## These are some additional functions and definitions intended to allow
## the player to configure the game to better suit themselves
##

# Allows the player to turn screenshake on/off
default persistent.screenshake = True
# Allows the player to turn banner animations on/off
default persistent.banners = True
# Allows players to turn the hacking effects on/off
default persistent.hacking_effects = True
# Shows a notification informing the player of audio cues
default persistent.audio_captions = False
# Allows the player to toggle timed menus on or off
default persistent.autoanswer_timed_menus = False

# A dictionary of all the music for the game and its corresponding
# audio caption
# Add your music to the bottom of the list so it will have a description
# when audio captions are turned on
default music_dictionary = {
    mystic_chat : "Upbeat saxophone music",
    mystic_chat2 : "Upbeat saxophone music with electric guitar",
    mysterious_clues : "Sinister bell music",
    urban_night_cityscape : "Sophisticated orchestral music",
    urban_night_cityscape_v2 : "Melancholy orchestral music",
    narcissistic_jazz : "Jazzy piano solo",
    lonely_but_passionate_way : "Wistful piano solo",
    geniusly_hacked_bebop : "Boistrous brass music",
    same_old_fresh_air : "Cheerful piano and harmonica music",
    silly_smile_again : "Cheerful music with percussion",
    lonesome_practicalism : "Calming blues music",
    lonesome_practicalism_v2 : "Melancholy blues music",
    i_miss_happy_rika : "Melancholy piano solo",
    dark_secret : "Suspenseful orchestral music",
    life_with_masks : "Somber piano solo",
    my_half_is_unknown : "Melancholy piano and violin",
    
    endless_struggle_guitar : "Slow guitar music",
    endless_struggle_harp : "Passionate harp solo",
    endless_struggle : "Passionate piano solo",
    four_seasons_piano : "Gentle piano solo",
    i_am_the_strongest_harp : "Dramatic harp music",
    i_am_the_strongest_piano : "Plaintive piano solo",
    i_am_the_strongest : "Dramatic string music",
    i_draw_piano : "Bittersweet piano solo",
    i_draw : "Bittersweet piano and guitar music",
    light_and_daffodils_piano1 : "Poignant piano solo",
    light_and_daffodils_piano2 : "Poignant piano solo",
    mint_eye_piano : "Elegant piano music",
    mint_eye : "Elegant violin music",
    mysterious_clues_v2 : "Sinister percussion music",
    mystic_chat_hacked : "Slowed upbeat saxophone music",
    suns_love_piano : "Mournful piano solo",
    suns_love : "Mournful piano and violin music",
    the_compass_piano1 : "Pensive piano solo",
    the_compass_piano2 : "Pensive piano solo",

    xmas_life_with_masks : "Somber music box melody with Joy to the World",
    xmas_lonesome_practicalism : "Calming Christmas music box music",
    xmas_narcissistic_jazz : "Jazzy music box melody with Little Drummer Boy",
    xmas_same_old_fresh_air : "Cheerful music box melody with Silent Night",
    xmas_urban_night_cityscape : "Melancholy music box melody with Jingle Bells",

    april_mystic_chat : "Upbeat 8-bit music",
    april_mysterious_clues : "Sinister 8-bit music",
    april_dark_secret : "Suspenseful 8-bit music"

}

default sfx_dictionary = {
    car_moving_sfx : "Sound of a car moving",
    door_knock_sfx : "A knock at the door",
    door_open_sfx : "The door opens"
}

## This label plays sound effects and also shows an audio
## caption if the player has that option turned on
label play_sfx(sfx):
    play sound sfx
    if persistent.audio_captions:
        $ notification = ("SFX: " + 
                sfx_dictionary[renpy.sound.get_playing('sound')])
        show screen notify(notification)
    return