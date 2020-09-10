init -6 python:
    class DayGreeting(object):
        """
        Class to keep track of different daily greetings. Can include
        Korean/English translations.

        Attributes:
        -----------
        sound_file : string
            Path to the file for the greeting sound.
        english : string
            Dialogue of the greeting, in English.
        korean : string
            Dialogue of the greeting, in Korean.
        """

        def __init__(self, sound_file, english=False, korean=False):
            """Creates a DayGreeting object to store a daily greeting."""

            self.sound_file = (store.greeting_audio_path + sound_file
                    + store.greeting_audio_extension)
            self.english = english or "Welcome to Mysterious Messenger!"
            self.korean = korean or "제 프로그램으로 환영합니다!"


## Greeting Text
## These are defaults for when the DayGreeting object does not have
## a translation
default greet_text_korean = "제 프로그램으로 환영합니다!"
default greet_text_english = "Welcome to Mysterious Messenger!"

## This lets the program randomly pick a greet
## character to display for greetings
default greet_list = [x.file_id for x in all_characters if x not in no_greet_chars ]
default greet_char = greet_list[0]

# Path where the audio files for greetings are stored
define greeting_audio_path = "audio/sfx/Main Menu Greetings/"
define greeting_audio_extension = ".wav"

#************************************
# Menu Greeting Lookup
#************************************

## Dictionary with the speaking character as the key and a list of
## DayGreetings as the value. Allows the program to look up a greeting
## based on the time of day
define morning_greeting = {
    'ja': [ DayGreeting('Jaehee/Morning/ja-m-1'),
                DayGreeting('Jaehee/Morning/ja-m-2'),
                DayGreeting('Jaehee/Morning/ja-m-3'),
                DayGreeting('Jaehee/Morning/ja-m-4')],

    'ju': [ DayGreeting('Jumin/Morning/ju-m-1'),
                DayGreeting('Jumin/Morning/ju-m-2'),
                DayGreeting('Jumin/Morning/ju-m-3'),
                DayGreeting('Jumin/Morning/ju-m-4')],

    'sa': [ DayGreeting('Ray/Morning/ra-m-1'),
                DayGreeting('Ray/Morning/ra-m-2'),
                DayGreeting('Ray/Morning/ra-m-3'),
                DayGreeting('Ray/Morning/ra-m-4')],

    'ri': [ DayGreeting('Rika/Morning/r-m-1'),
                DayGreeting('Rika/Morning/r-m-2'),
                DayGreeting('Rika/Morning/r-m-3'),
                DayGreeting('Rika/Morning/r-m-4')],

    's': [ DayGreeting('Seven/Morning/s-m-1'),
                DayGreeting('Seven/Morning/s-m-2'),
                DayGreeting('Seven/Morning/s-m-3'),
                DayGreeting('Seven/Morning/s-m-4')],

    'u': [ DayGreeting('Unknown/Morning/u-m-1'),
                DayGreeting('Unknown/Morning/u-m-2'),
                DayGreeting('Unknown/Morning/u-m-3')],

    'v': [ DayGreeting('V/Morning/v-m-1'),
                DayGreeting('V/Morning/v-m-2'),
                DayGreeting('V/Morning/v-m-3'),
                DayGreeting('V/Morning/v-m-4')],

    'y': [ DayGreeting('Yoosung/Morning/y-m-1'),
                DayGreeting('Yoosung/Morning/y-m-2'),
                DayGreeting('Yoosung/Morning/y-m-3'),
                DayGreeting('Yoosung/Morning/y-m-4')],

    'z': [ DayGreeting('Zen/Morning/z-m-1'),
                DayGreeting('Zen/Morning/z-m-2'),
                DayGreeting('Zen/Morning/z-m-3'),
                DayGreeting('Zen/Morning/z-m-4')] }

define afternoon_greeting = {
    'ja': [ DayGreeting('Jaehee/Afternoon/ja-a-1'),
                DayGreeting('Jaehee/Afternoon/ja-a-2'),
                DayGreeting('Jaehee/Afternoon/ja-a-3'),
                DayGreeting('Jaehee/Afternoon/ja-a-4')],

    'ju': [ DayGreeting('Jumin/Afternoon/ju-a-1'),
                DayGreeting('Jumin/Afternoon/ju-a-2'),
                DayGreeting('Jumin/Afternoon/ju-a-3'),
                DayGreeting('Jumin/Afternoon/ju-a-4')],

    'sa': [ DayGreeting('Ray/Afternoon/ra-a-1'),
                DayGreeting('Ray/Afternoon/ra-a-2'),
                DayGreeting('Ray/Afternoon/ra-a-3'),
                DayGreeting('Ray/Afternoon/ra-a-4')],

    'ri': [ DayGreeting('Rika/Afternoon/r-a-1'),
                DayGreeting('Rika/Afternoon/r-a-2'),
                DayGreeting('Rika/Afternoon/r-a-3'),
                DayGreeting('Rika/Afternoon/r-a-4')],

    's': [ DayGreeting('Seven/Afternoon/s-a-1'),
                DayGreeting('Seven/Afternoon/s-a-2'),
                DayGreeting('Seven/Afternoon/s-a-3'),
                DayGreeting('Seven/Afternoon/s-a-4')],

    'u': [ DayGreeting('Unknown/Afternoon/u-a-1'),
                DayGreeting('Unknown/Afternoon/u-a-2'),
                DayGreeting('Unknown/Afternoon/u-a-3')],

    'v': [ DayGreeting('V/Afternoon/v-a-1'),
                DayGreeting('V/Afternoon/v-a-2'),
                DayGreeting('V/Afternoon/v-a-3'),
                DayGreeting('V/Afternoon/v-a-4')],

    'y': [ DayGreeting('Yoosung/Afternoon/y-a-1'),
                DayGreeting('Yoosung/Afternoon/y-a-2'),
                DayGreeting('Yoosung/Afternoon/y-a-3'),
                DayGreeting('Yoosung/Afternoon/y-a-4')],

    'z': [ DayGreeting('Zen/Afternoon/z-a-1'),
                DayGreeting('Zen/Afternoon/z-a-2'),
                DayGreeting('Zen/Afternoon/z-a-3'),
                DayGreeting('Zen/Afternoon/z-a-4')] }

define evening_greeting = {
    'ja': [ DayGreeting('Jaehee/Evening/ja-e-1'),
                DayGreeting('Jaehee/Evening/ja-e-2'),
                DayGreeting('Jaehee/Evening/ja-e-3'),
                DayGreeting('Jaehee/Evening/ja-e-4')],

    'ju': [ DayGreeting('Jumin/Evening/ju-e-1'),
                DayGreeting('Jumin/Evening/ju-e-2'),
                DayGreeting('Jumin/Evening/ju-e-3'),
                DayGreeting('Jumin/Evening/ju-e-4')],

    'sa': [ DayGreeting('Ray/Evening/ra-e-1'),
                DayGreeting('Ray/Evening/ra-e-2'),
                DayGreeting('Ray/Evening/ra-e-3'),
                DayGreeting('Ray/Evening/ra-e-4')],

    'ri': [ DayGreeting('Rika/Evening/r-e-1'),
                DayGreeting('Rika/Evening/r-e-2'),
                DayGreeting('Rika/Evening/r-e-3'),
                DayGreeting('Rika/Evening/r-e-4')],

    's': [ DayGreeting('Seven/Evening/s-e-1'),
                DayGreeting('Seven/Evening/s-e-2'),
                DayGreeting('Seven/Evening/s-e-3'),
                DayGreeting('Seven/Evening/s-e-4')],

    'u': [ DayGreeting('Unknown/Evening/u-e-1'),
                DayGreeting('Unknown/Evening/u-e-2'),
                DayGreeting('Unknown/Evening/u-e-3')],

    'v': [ DayGreeting('V/Evening/v-e-1'),
                DayGreeting('V/Evening/v-e-2'),
                DayGreeting('V/Evening/v-e-3'),
                DayGreeting('V/Evening/v-e-4')],

    'y': [ DayGreeting('Yoosung/Evening/y-e-1'),
                DayGreeting('Yoosung/Evening/y-e-2'),
                DayGreeting('Yoosung/Evening/y-e-3'),
                DayGreeting('Yoosung/Evening/y-e-4')],

    'z': [ DayGreeting('Zen/Evening/z-e-1'),
                DayGreeting('Zen/Evening/z-e-2'),
                DayGreeting('Zen/Evening/z-e-3'),
                DayGreeting('Zen/Evening/z-e-4')] }

define night_greeting = {
    'ja': [ DayGreeting('Jaehee/Night/ja-n-1'),
                DayGreeting('Jaehee/Night/ja-n-2'),
                DayGreeting('Jaehee/Night/ja-n-3'),
                DayGreeting('Jaehee/Night/ja-n-4')],

    'ju': [ DayGreeting('Jumin/Night/ju-n-1'),
                DayGreeting('Jumin/Night/ju-n-2'),
                DayGreeting('Jumin/Night/ju-n-3'),
                DayGreeting('Jumin/Night/ju-n-4')],

    'sa': [ DayGreeting('Ray/Night/ra-n-1'),
                DayGreeting('Ray/Night/ra-n-2'),
                DayGreeting('Ray/Night/ra-n-3'),
                DayGreeting('Ray/Night/ra-n-4')],

    'ri': [ DayGreeting('Rika/Night/r-n-1'),
                DayGreeting('Rika/Night/r-n-2'),
                DayGreeting('Rika/Night/r-n-3'),
                DayGreeting('Rika/Night/r-n-4')],

    's': [ DayGreeting('Seven/Night/s-n-1'),
                DayGreeting('Seven/Night/s-n-2'),
                DayGreeting('Seven/Night/s-n-3'),
                DayGreeting('Seven/Night/s-n-4')],

    'u': [ DayGreeting('Unknown/Night/u-n-1'),
                DayGreeting('Unknown/Night/u-n-2'),
                DayGreeting('Unknown/Night/u-n-3')],

    'v': [ DayGreeting('V/Night/v-n-1'),
                DayGreeting('V/Night/v-n-2'),
                DayGreeting('V/Night/v-n-3'),
                DayGreeting('V/Night/v-n-4')],

    'y': [ DayGreeting('Yoosung/Night/y-n-1'),
                DayGreeting('Yoosung/Night/y-n-2'),
                DayGreeting('Yoosung/Night/y-n-3'),
                DayGreeting('Yoosung/Night/y-n-4')],

    'z': [ DayGreeting('Zen/Night/z-n-1'),
                DayGreeting('Zen/Night/z-n-2'),
                DayGreeting('Zen/Night/z-n-3'),
                DayGreeting('Zen/Night/z-n-4')] }

define late_night_greeting = {
    'ja': [ DayGreeting('Jaehee/Morning/ja-m-1'),
                DayGreeting('Jaehee/Late Night/ja-ln-2'),
                DayGreeting('Jaehee/Late Night/ja-ln-3'),
                DayGreeting('Jaehee/Late Night/ja-ln-4')],

    'ju': [ DayGreeting('Jumin/Late Night/ju-ln-1'),
                DayGreeting('Jumin/Late Night/ju-ln-2'),
                DayGreeting('Jumin/Late Night/ju-ln-3'),
                DayGreeting('Jumin/Late Night/ju-ln-4')],

    'sa': [ DayGreeting('Ray/Late Night/ra-ln-1'),
                DayGreeting('Ray/Late Night/ra-ln-2'),
                DayGreeting('Ray/Late Night/ra-ln-3'),
                DayGreeting('Ray/Late Night/ra-ln-4')],

    'ri': [ DayGreeting('Rika/Late Night/r-ln-1'),
                DayGreeting('Rika/Late Night/r-ln-2'),
                DayGreeting('Rika/Late Night/r-ln-3'),
                DayGreeting('Rika/Late Night/r-ln-4')],

    's': [ DayGreeting('Seven/Late Night/s-ln-1'),
                DayGreeting('Seven/Late Night/s-ln-2'),
                DayGreeting('Seven/Late Night/s-ln-3'),
                DayGreeting('Seven/Late Night/s-ln-4')],

    'u': [ DayGreeting('Unknown/Late Night/u-ln-1'),
                DayGreeting('Unknown/Late Night/u-ln-2'),
                DayGreeting('Unknown/Late Night/u-ln-3')],

    'v': [ DayGreeting('V/Late Night/v-ln-1'),
                DayGreeting('V/Late Night/v-ln-2'),
                DayGreeting('V/Late Night/v-ln-3'),
                DayGreeting('V/Late Night/v-ln-4')],

    'y': [ DayGreeting('Yoosung/Late Night/y-ln-1'),
                DayGreeting('Yoosung/Late Night/y-ln-2'),
                DayGreeting('Yoosung/Late Night/y-ln-3'),
                DayGreeting('Yoosung/Late Night/y-ln-4')],

    'z': [ DayGreeting('Zen/Late Night/z-ln-1'),
                DayGreeting('Zen/Late Night/z-ln-2'),
                DayGreeting('Zen/Late Night/z-ln-3'),
                DayGreeting('Zen/Late Night/z-ln-4')] }