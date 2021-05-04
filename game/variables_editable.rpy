init python:

    def set_pronouns():
        """Set the player's pronouns and pronoun variables."""

        global they, them, their, theirs, themself, they_re
        global They, Them, Their, Theirs, Themself, They_re
        global is_are, has_have, s_verb, do_does
        if persistent.pronoun == "she/her":
            they = "she"
            them = "her"
            their = "her"
            theirs = "hers"
            themself = "herself"
            they_re = "she's"
            is_are = "is"
            has_have = "has"
            do_does = "does"
            s_verb = "s"
        elif persistent.pronoun == "he/him":
            they = "he"
            them = "him"
            their = "his"
            theirs = "his"
            themself = "himself"
            they_re = "he's"
            is_are = "is"
            has_have = "has"
            do_does = "does"
            s_verb = "s"
        elif persistent.pronoun == "they/them":
            they = "they"
            them = "them"
            their = "their"
            theirs = "theirs"
            themself = "themself"
            they_re = "they're"
            is_are = "are"
            has_have = "have"
            do_does = "do"
            s_verb = ""
        # Set the capitalized versions
        They_re = string.capwords(they_re)
        They = string.capwords(they)
        Them = string.capwords(them)
        Their = string.capwords(their)
        Theirs = string.capwords(theirs)
        Themself = string.capwords(themself)
        # Save all variables
        renpy.retain_after_load()

init offset = -1

########################################
## PRONOUN VARIABLES
########################################
# Extra variables since the player can choose their pronouns.
# Feel free to add more so script writing is easier.
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
default do_does = "do"
default s_verb = ""

########################################
## SETUP DEFAULTS
########################################

default persistent.pronoun = "they/them"
default persistent.gender = "nonbinary"
define gender_options = ["nonbinary", "female", "male"]

default persistent.MC_pic = 'Profile Pics/MC/MC-1.webp'
default persistent.name = "Rainbow"
default persistent.chat_name = "Rainbow"

default persistent.HP = 0
default persistent.HG = 100

########################################
## HISTORY VARIABLES
########################################
# Define extra history items here, such as route prologues. The first string
# is the name of the button, and the second is the label it's found at.
define extra_history_items = [
    ("Tutorial Prologue", "start")
    ]

########################################
## GREETING IMAGES
########################################
# These image are approximately 121x107 up to 143x127
image greet ja = "Menu Screens/Main Menu/ja_greeting.webp"
image greet ju = "Menu Screens/Main Menu/ju_greeting.webp"
image greet sa = "Menu Screens/Main Menu/sa_greeting.webp"
image greet r = 'greet sa'
image greet ri = "Menu Screens/Main Menu/ri_greeting.webp"
image greet s = "Menu Screens/Main Menu/s_greeting.webp"
image greet u = "Menu Screens/Main Menu/u_greeting.webp"
image greet v = "Menu Screens/Main Menu/v_greeting.webp"
image greet va = "Menu Screens/Main Menu/va_greeting.webp"
image greet y = "Menu Screens/Main Menu/y_greeting.webp"
image greet z = "Menu Screens/Main Menu/z_greeting.webp"

# Add a character here if they do not have main menu greeting messages
default no_greet_chars = [r, m, va]

########################################
## BONUS PROFILE PICTURES
########################################

# These variables use `register_pfp` to make a big list of the profile pictures
# the user can unlock for each character. There are various filter functions
# to add many pictures at once.
define ja_unlockable_pfps = combine_lists(
    register_pfp(folder="Profile Pics/Jaehee/", filter_out='-b.'),
    register_pfp(folder="CGs/ja_album/", filter_keep='-thumb.')
)
define ju_unlockable_pfps = combine_lists(
    register_pfp(folder="Profile Pics/Jumin/", filter_out='-b.'),
    register_pfp(folder="CGs/ju_album/", filter_keep='-thumb.')
)
define sa_unlockable_pfps = [] # Saeran uses Ray's pictures
define r_unlockable_pfps = combine_lists(
    register_pfp(folder="Profile Pics/Saeran/", filter_out='-b.'),
    register_pfp(folder="Profile Pics/Ray/", filter_out='-b.'),
    register_pfp(folder="CGs/r_album/", filter_keep='-thumb.')
)
define ri_unlockable_pfps = combine_lists(
    register_pfp(folder="Profile Pics/Rika/", filter_out='-b.')
)
define s_unlockable_pfps = combine_lists(
    register_pfp(folder="Profile Pics/Seven/", filter_out='-b.'),
    register_pfp(folder="CGs/s_album/", filter_keep='-thumb.')
)
define u_unlockable_pfps = []
define v_unlockable_pfps = combine_lists(
    register_pfp(folder="Profile Pics/V/", filter_out='-b.'),
    register_pfp(folder="CGs/v_album/", filter_keep='-thumb.')
)
define va_unlockable_pfps = combine_lists(
    register_pfp(folder="Profile Pics/Vanderwood/", filter_out='-b.')
)
define y_unlockable_pfps = combine_lists(
    register_pfp(folder="Profile Pics/Yoosung/", filter_out='-b.'),
    register_pfp(folder="CGs/y_album/", filter_keep='-thumb.')
)
define z_unlockable_pfps = combine_lists(
    register_pfp(folder="Profile Pics/Zen/", filter_out='-b.'),
    register_pfp(folder="CGs/z_album/", filter_keep='-thumb.')
)

# List of images the player has unlocked and can use as a profile picture.
# Automatically includes everything in the Drop Your Profile Picture Here
# folder, and you can add more items to be unlocked by default if desired.
default persistent.mc_unlocked_pfps = set()

# Number of heart points it costs to unlock a profile picture for an NPC.
define pfp_cost = 5

# A function that will be called when the player changes their
# profile picture. The function should take four arguments: 1) the
# time that has passed since the picture was last changed, 2) the profile
# picture before this one 3) the current profile pic, and 4) the ChatCharacter
# associated with the profile picture (or None if it's a default picture).
# If it returns a string, the program will call that string as a label
# (e.g. for text messages).
default mc_pfp_callback = bonus_pfp_dialogue


init -1 python:
    def bonus_pfp_dialogue(time_diff, prev_pic, current_pic, who):
        """
        An example callback function for when the player changes their
        profile picture.
        """

        # time_diff is a timedelta object wrapped in a MyTimeDelta class to
        # make accessing fields easier. Its most useful fields are `days`,
        # `minutes`, `hours`, and `seconds`. Each field is rounded DOWN to the
        # nearest value e.g. if 2 minutes have passed, seconds = 120,
        # minutes = 2, and hours and days = 0.
        if time_diff.seconds < 10:
            return
        # Otherwise, figure out what to do based on the other properties
        if (who == store.r and "CGs/r_album/cg-1" in current_pic):
            # This is Ray's flower image
            return 'ray_pfp_callback_1'
        # You can also return a list of labels, in which case the first unplayed
        # label in the list will be called. This is so you can have different
        # events occur the first time a condition is met vs the second time etc
        # You can see another example of a callback function in
        # tutorial_0_introduction.rpy

label ray_pfp_callback_1:
    compose text r real_time:
        r "Oh, haha."
        r "I just realized you changed your profile picture."
        label ray_pfp_callback_1_menu_1
    return

label ray_pfp_callback_1_menu_1:

    menu:
        "Yeah! I really like it.":
            m "Yeah! I really like it." (pauseVal=0)
            r "Oh ^^"
            award heart r
            r "Well, I'm glad you can use it, then."
            r "{image=ray_smile}" (img=True)
        "I thought it'd be funny.":
            r "Ah. I see."
            r "Well, I hope you're enjoying yourself."
    return

########################################
## PHONE HANG UP CALLBACK
########################################
# This function is executed with one parameter, the phone call that
# the player hung up during. Use this to modify dialogue if the player
# hangs up in the middle of a call.
default phone_hangup_callback = hang_up_callback_fn

init python:

    def hang_up_callback_fn(phonecall):
        """
        A function which is called when the player hangs up an ongoing
        phone call with a character. It is given one parameter: the call
        that the player was in the middle of. By default, that call is
        removed from the list of available calls afterwards.

        Parameters:
        -----------
        phonecall : PhoneCall
            The call the player hung up the phone during. PhoneCall objects
            have the following useful parameters:
                caller : ChatCharacter
                    The person the player was on the phone with.
                phone_label : string
                    The label that leads to the phone call.
                call_status : string
                    The status of the phone call. One of "incoming", "outgoing",
                    "missed", or "voicemail".
                voicemail : bool
                    True if this phone call is a voicemail message rather than
                    a proper conversation.
        """

        if phonecall.voicemail:
            # It doesn't matter if the player hung up in the middle
            # a voicemail
            return

        if phonecall.phone_label == 'test_call':
            # The special test phone call always available on Tutorial Day.
            # More typically your check will look like "day1_chat1_outgoing_z"
            # Anyway, since the player hung up on Ray, he's going to try
            # to call them back.
            create_incoming_call("ray_test_call_callback", who=r)

        # This ends the function; it doesn't need to return any values
        return

label ray_test_call_callback():
    r "[name]... is your phone not working?"
    r "All of a sudden the call dropped."
    r "I can come over and take a look if you're having trouble. I wouldn't want you to have a broken app."
    menu:
        extend ''
        "I didn't mean to hang up! Sorry about that.":
            r "Oh, it's okay! Please don't worry about it."
        "Omg I didn't think you'd know I hung up.":
            r "Oh... haha. Well that's just one of the things you can do with this app, I guess."
            r "I hope it doesn't freak you out or anything. It's not like I'm monitoring you."
    r "I don't even remember what I was talking about... I guess it wasn't very important."
    r "I hope you like this app! Please let me know if you run into any issues."
    r "Bye for now~"
    return


########################################
## SPACESHIP THOUGHT IMAGES
########################################
# These image are rounded and 651x374
image ja_spacethought = "Menu Screens/Spaceship/ja_spacethought.webp"
image ju_spacethought = "Menu Screens/Spaceship/ju_spacethought.webp"
image r_spacethought = "Menu Screens/Spaceship/r_spacethought.webp"
image ri_spacethought = "Menu Screens/Spaceship/ri_spacethought.webp"
image s_spacethought = "Menu Screens/Spaceship/s_spacethought.webp"
image sa_spacethought = "Menu Screens/Spaceship/sa_spacethought.webp"
image v_spacethought = "Menu Screens/Spaceship/v_spacethought.webp"
image y_spacethought = "Menu Screens/Spaceship/y_spacethought.webp"
image z_spacethought = "Menu Screens/Spaceship/z_spacethought.webp"

########################################
## DAY SELECT IMAGES
########################################
# These images are rectangular (with rounded corners) and 263x367
image day_common1 = 'Menu Screens/Day Select/day_common1.webp'
image day_common2 = 'Menu Screens/Day Select/day_common2.webp'
image day_ja = 'Menu Screens/Day Select/day_ja.webp'
image day_ju = 'Menu Screens/Day Select/day_ju.webp'
image day_r = 'Menu Screens/Day Select/day_r.webp'
image day_s = 'Menu Screens/Day Select/day_s.webp'
image day_v = 'Menu Screens/Day Select/day_v.webp'
image day_y = 'Menu Screens/Day Select/day_y.webp'
image day_z = 'Menu Screens/Day Select/day_z.webp'


########################################
## SAVE & LOAD IMAGES
########################################
# These images are square and 109x109
image save_auto = "Menu Screens/Main Menu/msgsl_icon_m.webp"
image save_another = "Menu Screens/Main Menu/msgsl_image_another.webp"
image save_april = "Menu Screens/Main Menu/msgsl_image_april.webp"
image save_casual = "Menu Screens/Main Menu/msgsl_image_casual.webp"
image save_deep = "Menu Screens/Main Menu/msgsl_image_deep.webp"
image save_jaehee = "Menu Screens/Main Menu/msgsl_image_jaehee.webp"
image save_jumin = "Menu Screens/Main Menu/msgsl_image_jumin.webp"
image save_ray = "Menu Screens/Main Menu/msgsl_image_ray.webp"
image save_empty = "Menu Screens/Main Menu/msgsl_image_save.webp"
image save_seven = "Menu Screens/Main Menu/msgsl_image_seven.webp"
image save_v = "Menu Screens/Main Menu/msgsl_image_v.webp"
image save_xmas = "Menu Screens/Main Menu/msgsl_image_xmas.webp"
image save_yoosung = "Menu Screens/Main Menu/msgsl_image_yoosung.webp"
image save_zen = "Menu Screens/Main Menu/msgsl_image_zen.webp"

########################################
## PHONE CONTACT IMAGES
########################################
# These images are 188x188 and round
image sa_contact = 'Phone Calls/call_contact_saeran.webp'
image s_contact = 'Phone Calls/call_contact_707.webp'
image empty_contact = 'Phone Calls/call_contact_empty.webp'
image ja_contact = 'Phone Calls/call_contact_jaehee.webp'
image ju_contact = 'Phone Calls/call_contact_jumin.webp'
image r_contact = 'Phone Calls/call_contact_ray.webp'
image v_contact = 'Phone Calls/call_contact_v.webp'
image va_contact = "Phone Calls/call_contact_vanderwood.webp"
image y_contact = 'Phone Calls/call_contact_yoosung.webp'
image z_contact = 'Phone Calls/call_contact_zen.webp'
image ri_contact = 'Phone Calls/call_contact_rika.webp'

########################################
## STORY MODE/VN IMAGES
########################################
# These images are rectangular and typically 555x126 (with the exception
# of the party icon)
image vn_other = 'Menu Screens/Day Select/vn_other.webp'
image vn_ja = 'Menu Screens/Day Select/vn_ja.webp'
image vn_ju = 'Menu Screens/Day Select/vn_ju.webp'
image vn_r = 'Menu Screens/Day Select/vn_r.webp'
image vn_ri = 'Menu Screens/Day Select/vn_ri.webp'
image vn_sa = 'Menu Screens/Day Select/vn_sa.webp'
image vn_s = 'Menu Screens/Day Select/vn_s.webp'
image vn_v = 'Menu Screens/Day Select/vn_v.webp'
image vn_y = 'Menu Screens/Day Select/vn_y.webp'
image vn_z = 'Menu Screens/Day Select/vn_z.webp'
image vn_party = 'Menu Screens/Day Select/vn_party.webp'
image vn_party_inactive = 'Menu Screens/Day Select/vn_party_inactive.webp'

########################################
## PARTY RANKING
########################################
# It seems 15+ guests is A grade and 6- guests is D grade.
# This program has its own arbitrary grade calculations instead.
# Feel free to replace the numbers with more suitable ones.
image party_grade = ConditionSwitch(
    "guest_countup >= 20", "Email/a_grade.webp",
    "guest_countup >= 10", "Email/b_grade.webp",
    "guest_countup >= 5", "Email/c_grade.webp",
    "guest_countup >= 2", "Email/d_grade.webp",
    True, "Email/f_grade.webp",
)

########################################
## CUSTOM MESSENGER ITEMS
########################################
# If you'd like to use custom fonts with the msg CDS, you must add them
# to these lists.
define all_fonts_list = ['sser1', 'sser2', 'ser1', 'ser2', 'curly','blocky']
# Fonts which can be bold/extra bold
define bold_xbold_fonts_list = ['sser1', 'sser2', 'ser1', 'ser2']
# And if you want them to be used in text messages, you must add them to
# this dictionary along with a path to its .ttf file.
define font_dict = { 'curly' : gui.curly_font, 'ser1' : gui.serif_1,
            'ser1b' : gui.serif_1b, 'ser1xb' : gui.serif_1xb,
            'ser2' : gui.serif_2, 'ser2b' : gui.serif_2b,
            'ser2xb' : gui.serif_2xb, 'sser1' : gui.sans_serif_1,
            'sser1b' : gui.sans_serif_1b, 'sser1xb' : gui.sans_serif_1xb,
            'sser2' : gui.sans_serif_2, 'sser2b' : gui.sans_serif_2b,
            'sser2xb' : gui.sans_serif_2xb, 'blocky' : gui.blocky_font
            # A valid entry could also look like:
            # 'cursive' : 'fonts/somecursivefont.ttf'
        }

# Similarly, if you have any custom bubbles defined, add them here.
define all_bubbles_list = ['cloud_l', 'cloud_m', 'cloud_s', 'round_l',
    'round_m', 'round_s', 'sigh_l', 'sigh_m', 'sigh_s', 'spike_l', 'spike_m',
    'spike_s', 'square_l', 'square_m', 'square_s', 'square2_l', 'square2_m',
    'square2_s', 'round2_l', 'round2_m', 'round2_s', 'flower_l', 'flower_m',
    'flower_s', 'glow2', 'glow3', 'square3_s', 'square3_m', 'square3_l',
    'cloud2_s', 'cloud2_m', 'cloud2_l', 'spike2_l', 'spike2_m']

# A list of bubbles which will occasionally award a bonus hourglass when used
# in a chatroom.
define hourglass_bubbles = ['cloud_l', 'round_l', 'square_l', 'flower_l',
                'square2_l', 'round2_l', 'square3_l', 'cloud2_l']

# All possible backgrounds are defined here. If they are a static image,
# they should be defined as `image bg morning` and the list contains 'morning'.
define all_static_backgrounds = ['morning', 'noon', 'evening', 'hack',
                'redhack', 'night', 'earlyMorn', 'redcrack', 'secure',
                'rainy_day', 'snowy_day', 'morning_snow']
# If there is an animated version, it goes here. They should be defined as
# `screen animated_evening` and the list contains 'evening'.
# Animated backgrounds should have a `zorder` of 0 and be tagged `animated_bg`.
define all_animated_backgrounds = ['morning', 'noon', 'evening', 'night',
                'earlyMorn', 'rainy_day', 'snowy_day', 'morning_snow']
# This should be the same string as seen in all_static_backgrounds and
# all_animated_backgrounds. Any backgrounds in here will display chatroom
# nicknames in black. Otherwise, they are displayed in white.
define black_text_bgs = ['morning', 'noon', 'evening', 'snowy_day', 'morning_snow']



init python:

    def custom_bubble_bg(msg):
        """
        A special function which is used for a ChatEntry's `bubble_bg` property.
        It allows you to read from and modify the ChatEntry object in case
        you want to use a special bubble background.

        Parameters:
        -----------
        msg : ChatEntry
            A ChatEntry object containing the information on this particular
            message.

        Returns:
        --------
        string or False
            If this function returns False, the program will use the default
            background for this message. Otherwise, this should return a string
            or a Displayable such as a Frame() that will be used as the
            background for this bubble.
        """

        ## An example might look like the following:
        # if (msg.specBubble and msg.who.file_id == 'u'):
        #     ## This allows Unknown to use Ray's special bubbles
        #     return "Bubble/Special/r_" + msg.specBubble + ".webp"

        return False

    def custom_bubble_offset(msg):
        """
        A special function which is used for a ChatEntry's `spec_bubble_offset`
        property. It allows you to read from and modify the ChatEntry object
        in case you want to use a special style.

        Parameters:
        -----------
        msg : ChatEntry
            A ChatEntry object containing the information on this particular
            message.

        Returns:
        --------
        tuple(int, int) or False
            If this function returns False, the program will use the default
            styling for this message. Otherwise, this should return a tuple
            of (x, y) integers for the x and y pos of this bubble.
        """

        ## An example might look like the following:
        # if msg.specBubble == 'my_special_bubble':
        #     return (120, 30)

        return False

    def custom_bubble_style(msg):
        """
        A special function which is used for a ChatEntry's `bubble_style`
        property. It allows you to read from and modify the ChatEntry object
        in case you want to return a special style.

        Parameters:
        -----------
        msg : ChatEntry
            A ChatEntry object containing the information on this particular
            message.

        Returns:
        --------
        string or False
            If this function returns False, the program will use the default
            styling for this message. Otherwise, this should return a string
            with the name of the style to use.
        """

        ## An example might look like the following:
        # if msg.specBubble == 'my_special_bubble':
        #     return 'my_special_style'
        ## See below for a definition of this possible style

        return False


## An example of a style that could be used for custom_bubble_style
# style my_special_style:
#     padding (20, 40, 20, 30)


########################################
## SPACESHIP/CHIP BAG VARIABLES
########################################
# Chip thoughts are organized in a tuple with three items:
# The description, approximate number of hearts, and number of hourglasses
default chip_prize_list = RandomBag( [
    ('A clump of cat hair.', 30, 0),
    ("Jumin's old toothbrush.", 20, 0),
    ("Some Honey Buddha Chip crumbs.", 24, 0),
    ("Jaehee's spare pair of glasses.", 65, 0),
    ("Yoosung's left sock.", 33, 0),
    ("Your middle school photo album!", 19, 0),
    ("Toothpaste that tastes like Honey Buddha Chips", 69, 0),
    ("A completion certificate for mid-level dating.", 100, 0),
    ("It's a present for you.", 67, 0),
    ("A very normal industrial product.", 86, 0),
    ("This Honey Boss Chip began in 1987 England...", 34, 0),
    ("Disco lights! Let's dance!", 69, 0),
    ("Yoosung's blessed hair strands. Blow on it and make a wish!", 443, 4),
    ("A chip bag full of chip dust", 10, 0),
    ("There's mold on these...", 19, 0)
    # Feel free to add more things
    ] )


# This is what a list of thoughts for the spaceship will look like
default space_thoughts = RandomBag( [
    SpaceThought(ja, "I should have broken these shoes in better before wearing them to work today."),
    SpaceThought(ju, "I wonder how Elizabeth the 3rd is doing at home."),
    SpaceThought(s, "Maybe I should Noogle how to get chip crumbs out of my keyboard..."),
    SpaceThought(y, "Yes! Chocolate milk is on sale!"),
    SpaceThought(z, "Maybe I should learn how to braid my hair..."),
    SpaceThought(r, "I can't believe I accidentally used one of the other Believer's shampoo. My hair smells like lemons."),
    SpaceThought(ri, "Hmm... the soup tastes different today."),
    SpaceThought(sa, "So... sleepy..."),
    SpaceThought(v, "The weather is so very lovely today. Maybe I'll go for a walk.")
    ] )

########################################
## MISCELLANEOUS VARIABLES
########################################
# If True, choices in a menu are treated as "paraphrased" -- that is,
# it is your responsibility to write out exactly what you want the MC to
# say after a choice. If False, the program will automatically make the MC
# say the choice dialogue.
# If None, the program tries to dynamically figure out what the value
# should be based on the first menu of choices it comes across.
default paraphrase_choices = None
# If True, when a timed menu or continuous menu has no available choices
# (e.g. none of the conditions on the choices are met), the narration will
# still be shown to the player. If False, the program will skip to the end
# of the menu.
define show_empty_menus = True
# This tells the program whether or not it should use the "old" method of
# defining guests, where the user must manually declare reply labels. It is
# automatically set to True for old save files before v3.0 and False otherwise.
init offset = -1
default use_2_2_guest = False
init offset = 0

# Add tips here to appear on the loading screen
default loading_tips = [
    "Please make sure the game is not quit or interrupted during save or load.",
    "Tap the Links button in the hub screen to go to the Mysterious Messenger Discord.",
    "Want to contribute to the program? Submit a pull request to the Mysterious Messenger GitHub!",
    "There are many accessibility options in the Settings menu.",
    "Found a bug? Report it on the Mysterious Messenger GitHub.",
    "Like the program? Consider donating to my Ko-Fi in Links.",
    "Is there a feature you want to see? Let me know in the Mysterious Messenger Discord.",
    "Did you know? You can turn on Audio Captions from the Settings menu.",
    "You can toggle animated backgrounds on or off from the Settings menu.",
    "Testing Mode in the Developer menu makes it easy to test routes.",
    "Sometimes characters might send you a message when you change your profile picture."
]

