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
        
            self.sound_file = sound_file
            self.english = english
            self.korean = korean


#************************************
# Menu Greeting Lookup
#************************************

## Dictionary with the speaking character as the key and a list of
## DayGreetings as the value. Allows the program to look up a greeting
## based on the time of day
define morning_greeting = {
    'ja': [ DayGreeting('audio/sfx/Main Menu Greetings/Jaehee/Morning/ja-m-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jaehee/Morning/ja-m-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jaehee/Morning/ja-m-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jaehee/Morning/ja-m-4.wav')],
                
    'ju': [ DayGreeting('audio/sfx/Main Menu Greetings/Jumin/Morning/ju-m-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jumin/Morning/ju-m-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jumin/Morning/ju-m-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jumin/Morning/ju-m-4.wav')],
                
    'sa': [ DayGreeting('audio/sfx/Main Menu Greetings/Ray/Morning/ra-m-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Ray/Morning/ra-m-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Ray/Morning/ra-m-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Ray/Morning/ra-m-4.wav')],
                
    'ri': [ DayGreeting('audio/sfx/Main Menu Greetings/Rika/Morning/r-m-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Rika/Morning/r-m-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Rika/Morning/r-m-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Rika/Morning/r-m-4.wav')],
                
    's': [ DayGreeting('audio/sfx/Main Menu Greetings/Seven/Morning/s-m-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Seven/Morning/s-m-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Seven/Morning/s-m-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Seven/Morning/s-m-4.wav')],
                
    'u': [ DayGreeting('audio/sfx/Main Menu Greetings/Unknown/Morning/u-m-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Unknown/Morning/u-m-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Unknown/Morning/u-m-3.wav')],
                
    'v': [ DayGreeting('audio/sfx/Main Menu Greetings/V/Morning/v-m-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/V/Morning/v-m-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/V/Morning/v-m-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/V/Morning/v-m-4.wav')],
                
    'y': [ DayGreeting('audio/sfx/Main Menu Greetings/Yoosung/Morning/y-m-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Yoosung/Morning/y-m-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Yoosung/Morning/y-m-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Yoosung/Morning/y-m-4.wav')],
                
    'z': [ DayGreeting('audio/sfx/Main Menu Greetings/Zen/Morning/z-m-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Zen/Morning/z-m-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Zen/Morning/z-m-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Zen/Morning/z-m-4.wav')] }
                                
define afternoon_greeting = {
    'ja': [ DayGreeting('audio/sfx/Main Menu Greetings/Jaehee/Afternoon/ja-a-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jaehee/Afternoon/ja-a-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jaehee/Afternoon/ja-a-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jaehee/Afternoon/ja-a-4.wav')],
                
    'ju': [ DayGreeting('audio/sfx/Main Menu Greetings/Jumin/Afternoon/ju-a-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jumin/Afternoon/ju-a-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jumin/Afternoon/ju-a-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jumin/Afternoon/ju-a-4.wav')],
                
    'sa': [ DayGreeting('audio/sfx/Main Menu Greetings/Ray/Afternoon/ra-a-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Ray/Afternoon/ra-a-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Ray/Afternoon/ra-a-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Ray/Afternoon/ra-a-4.wav')],
                
    'ri': [ DayGreeting('audio/sfx/Main Menu Greetings/Rika/Afternoon/r-a-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Rika/Afternoon/r-a-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Rika/Afternoon/r-a-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Rika/Afternoon/r-a-4.wav')],
                
    's': [ DayGreeting('audio/sfx/Main Menu Greetings/Seven/Afternoon/s-a-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Seven/Afternoon/s-a-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Seven/Afternoon/s-a-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Seven/Afternoon/s-a-4.wav')],
                
    'u': [ DayGreeting('audio/sfx/Main Menu Greetings/Unknown/Afternoon/u-a-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Unknown/Afternoon/u-a-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Unknown/Afternoon/u-a-3.wav')],
                
    'v': [ DayGreeting('audio/sfx/Main Menu Greetings/V/Afternoon/v-a-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/V/Afternoon/v-a-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/V/Afternoon/v-a-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/V/Afternoon/v-a-4.wav')],
                
    'y': [ DayGreeting('audio/sfx/Main Menu Greetings/Yoosung/Afternoon/y-a-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Yoosung/Afternoon/y-a-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Yoosung/Afternoon/y-a-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Yoosung/Afternoon/y-a-4.wav')],
                
    'z': [ DayGreeting('audio/sfx/Main Menu Greetings/Zen/Afternoon/z-a-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Zen/Afternoon/z-a-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Zen/Afternoon/z-a-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Zen/Afternoon/z-a-4.wav')] }
                                
define evening_greeting = {
    'ja': [ DayGreeting('audio/sfx/Main Menu Greetings/Jaehee/Evening/ja-e-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jaehee/Evening/ja-e-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jaehee/Evening/ja-e-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jaehee/Evening/ja-e-4.wav')],
                
    'ju': [ DayGreeting('audio/sfx/Main Menu Greetings/Jumin/Evening/ju-e-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jumin/Evening/ju-e-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jumin/Evening/ju-e-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jumin/Evening/ju-e-4.wav')],
                
    'sa': [ DayGreeting('audio/sfx/Main Menu Greetings/Ray/Evening/ra-e-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Ray/Evening/ra-e-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Ray/Evening/ra-e-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Ray/Evening/ra-e-4.wav')],
                
    'ri': [ DayGreeting('audio/sfx/Main Menu Greetings/Rika/Evening/r-e-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Rika/Evening/r-e-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Rika/Evening/r-e-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Rika/Evening/r-e-4.wav')],
                
    's': [ DayGreeting('audio/sfx/Main Menu Greetings/Seven/Evening/s-e-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Seven/Evening/s-e-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Seven/Evening/s-e-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Seven/Evening/s-e-4.wav')],
                
    'u': [ DayGreeting('audio/sfx/Main Menu Greetings/Unknown/Evening/u-e-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Unknown/Evening/u-e-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Unknown/Evening/u-e-3.wav')],
                
    'v': [ DayGreeting('audio/sfx/Main Menu Greetings/V/Evening/v-e-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/V/Evening/v-e-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/V/Evening/v-e-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/V/Evening/v-e-4.wav')],
                
    'y': [ DayGreeting('audio/sfx/Main Menu Greetings/Yoosung/Evening/y-e-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Yoosung/Evening/y-e-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Yoosung/Evening/y-e-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Yoosung/Evening/y-e-4.wav')],
                
    'z': [ DayGreeting('audio/sfx/Main Menu Greetings/Zen/Evening/z-e-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Zen/Evening/z-e-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Zen/Evening/z-e-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Zen/Evening/z-e-4.wav')] }                    

define night_greeting = {
    'ja': [ DayGreeting('audio/sfx/Main Menu Greetings/Jaehee/Night/ja-n-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jaehee/Night/ja-n-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jaehee/Night/ja-n-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jaehee/Night/ja-n-4.wav')],
                
    'ju': [ DayGreeting('audio/sfx/Main Menu Greetings/Jumin/Night/ju-n-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jumin/Night/ju-n-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jumin/Night/ju-n-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jumin/Night/ju-n-4.wav')],
                
    'sa': [ DayGreeting('audio/sfx/Main Menu Greetings/Ray/Night/ra-n-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Ray/Night/ra-n-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Ray/Night/ra-n-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Ray/Night/ra-n-4.wav')],
                
    'ri': [ DayGreeting('audio/sfx/Main Menu Greetings/Rika/Night/r-n-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Rika/Night/r-n-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Rika/Night/r-n-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Rika/Night/r-n-4.wav')],
                
    's': [ DayGreeting('audio/sfx/Main Menu Greetings/Seven/Night/s-n-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Seven/Night/s-n-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Seven/Night/s-n-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Seven/Night/s-n-4.wav')],
                
    'u': [ DayGreeting('audio/sfx/Main Menu Greetings/Unknown/Night/u-n-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Unknown/Night/u-n-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Unknown/Night/u-n-3.wav')],
                
    'v': [ DayGreeting('audio/sfx/Main Menu Greetings/V/Night/v-n-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/V/Night/v-n-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/V/Night/v-n-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/V/Night/v-n-4.wav')],
                
    'y': [ DayGreeting('audio/sfx/Main Menu Greetings/Yoosung/Night/y-n-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Yoosung/Night/y-n-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Yoosung/Night/y-n-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Yoosung/Night/y-n-4.wav')],
                
    'z': [ DayGreeting('audio/sfx/Main Menu Greetings/Zen/Night/z-n-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Zen/Night/z-n-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Zen/Night/z-n-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Zen/Night/z-n-4.wav')] }
                                
define late_night_greeting = {
    'ja': [ DayGreeting('audio/sfx/Main Menu Greetings/Jaehee/Morning/ja-m-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jaehee/Late Night/ja-ln-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jaehee/Late Night/ja-ln-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jaehee/Late Night/ja-ln-4.wav')],
                
    'ju': [ DayGreeting('audio/sfx/Main Menu Greetings/Jumin/Late Night/ju-ln-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jumin/Late Night/ju-ln-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jumin/Late Night/ju-ln-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Jumin/Late Night/ju-ln-4.wav')],
                
    'sa': [ DayGreeting('audio/sfx/Main Menu Greetings/Ray/Late Night/ra-ln-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Ray/Late Night/ra-ln-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Ray/Late Night/ra-ln-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Ray/Late Night/ra-ln-4.wav')],
                
    'ri': [ DayGreeting('audio/sfx/Main Menu Greetings/Rika/Late Night/r-ln-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Rika/Late Night/r-ln-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Rika/Late Night/r-ln-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Rika/Late Night/r-ln-4.wav')],
                
    's': [ DayGreeting('audio/sfx/Main Menu Greetings/Seven/Late Night/s-ln-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Seven/Late Night/s-ln-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Seven/Late Night/s-ln-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Seven/Late Night/s-ln-4.wav')],
                
    'u': [ DayGreeting('audio/sfx/Main Menu Greetings/Unknown/Late Night/u-ln-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Unknown/Late Night/u-ln-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Unknown/Late Night/u-ln-3.wav')],
                
    'v': [ DayGreeting('audio/sfx/Main Menu Greetings/V/Late Night/v-ln-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/V/Late Night/v-ln-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/V/Late Night/v-ln-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/V/Late Night/v-ln-4.wav')],
                
    'y': [ DayGreeting('audio/sfx/Main Menu Greetings/Yoosung/Late Night/y-ln-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Yoosung/Late Night/y-ln-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Yoosung/Late Night/y-ln-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Yoosung/Late Night/y-ln-4.wav')],
                
    'z': [ DayGreeting('audio/sfx/Main Menu Greetings/Zen/Late Night/z-ln-1.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Zen/Late Night/z-ln-2.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Zen/Late Night/z-ln-3.wav'),
                DayGreeting('audio/sfx/Main Menu Greetings/Zen/Late Night/z-ln-4.wav')] }     