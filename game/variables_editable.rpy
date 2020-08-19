init python:

    def set_pronouns():
        """Set the player's pronouns and pronoun variables."""

        global they, them, their, theirs, themself, they_re
        global They, Them, Their, Theirs, Themself, They_re
        global is_are, has_have, s_verb
        if persistent.pronoun == "female":
            they = "she"
            them = "her"
            their = "her"
            theirs = "hers"
            themself = "herself"
            they_re = "she's"
            They_re = "She's"
            They = "She"
            Them = "Her"
            Their = "Her"
            Theirs = "Hers"
            Themself = "Herself"   
            is_are = "is"
            has_have = "has"
            s_verb = "s"
        elif persistent.pronoun == "male":
            they = "he"
            them = "him"
            their = "his"
            theirs = "his"
            themself = "himself"
            they_re = "he's"
            They_re = "He's"
            They = "He"
            Them = "Him"
            Their = "His"
            Theirs = "His"
            Themself = "Himself"
            is_are = "is"
            has_have = "has"
            s_verb = "s"
        elif persistent.pronoun == "non binary":
            they = "they"
            them = "them"
            their = "their"
            theirs = "theirs"
            themself = "themself"
            they_re = "they're"
            They_re = "They're"
            They = "They"
            Them = "Them"
            Their = "Their"
            Theirs = "Theirs"
            Themself = "Themself"
            is_are = "are"
            has_have = "have"
            s_verb = ""
        renpy.retain_after_load()

########################################
## PRONOUN VARIABLES
########################################
# Extra variables since the player can choose their pronouns
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

########################################
## GREETING IMAGES
########################################
# These image are approximately 121x107 up to 143x127
image greet ja = "Menu Screens/Main Menu/ja_greeting.png"
image greet ju = "Menu Screens/Main Menu/ju_greeting.png"
image greet sa = "Menu Screens/Main Menu/sa_greeting.png"
image greet r = 'greet sa'
image greet ri = "Menu Screens/Main Menu/ri_greeting.png"
image greet s = "Menu Screens/Main Menu/s_greeting.png"
image greet u = "Menu Screens/Main Menu/u_greeting.png"
image greet v = "Menu Screens/Main Menu/v_greeting.png"
image greet y = "Menu Screens/Main Menu/y_greeting.png"
image greet z = "Menu Screens/Main Menu/z_greeting.png"

########################################
## BONUS PROFILE PICTURES
########################################

# These variables use `register_pfp` to make a big list of the profile pictures
# the user can unlock for each character.
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
define y_unlockable_pfps = combine_lists(
    register_pfp(folder="Profile Pics/Yoosung/", filter_out='-b.'),
    register_pfp(folder="CGs/y_album/", filter_keep='-thumb.')
)
define z_unlockable_pfps = combine_lists(
    register_pfp(folder="Profile Pics/Zen/", filter_out='-b.'),
    register_pfp(folder="CGs/z_album/", filter_keep='-thumb.')
)

########################################
## SPACESHIP THOUGHT IMAGES
########################################
# These image are rounded and 651x374
image ja_spacethought = "Menu Screens/Spaceship/ja_spacethought.png"
image ju_spacethought = "Menu Screens/Spaceship/ju_spacethought.png"
image r_spacethought = "Menu Screens/Spaceship/r_spacethought.png"
image ri_spacethought = "Menu Screens/Spaceship/ri_spacethought.png"
image s_spacethought = "Menu Screens/Spaceship/s_spacethought.png"
image sa_spacethought = "Menu Screens/Spaceship/sa_spacethought.png"
image v_spacethought = "Menu Screens/Spaceship/v_spacethought.png"
image y_spacethought = "Menu Screens/Spaceship/y_spacethought.png"
image z_spacethought = "Menu Screens/Spaceship/z_spacethought.png"

########################################
## DAY SELECT IMAGES
########################################
# These images are rectangular (with rounded corners) and 263x367
image day_common1 = 'Menu Screens/Day Select/day_common1.png'
image day_common2 = 'Menu Screens/Day Select/day_common2.png'
image day_ja = 'Menu Screens/Day Select/day_ja.png'
image day_ju = 'Menu Screens/Day Select/day_ju.png'
image day_r = 'Menu Screens/Day Select/day_r.png'
image day_s = 'Menu Screens/Day Select/day_s.png'
image day_v = 'Menu Screens/Day Select/day_v.png'
image day_y = 'Menu Screens/Day Select/day_y.png'
image day_z = 'Menu Screens/Day Select/day_z.png'


########################################
## SAVE & LOAD IMAGES
########################################
# These images are square and 109x109
image save_auto = "Menu Screens/Main Menu/msgsl_icon_m.png"
image save_another = "Menu Screens/Main Menu/msgsl_image_another.png"
image save_april = "Menu Screens/Main Menu/msgsl_image_april.png"
image save_casual = "Menu Screens/Main Menu/msgsl_image_casual.png"
image save_deep = "Menu Screens/Main Menu/msgsl_image_deep.png"
image save_jaehee = "Menu Screens/Main Menu/msgsl_image_jaehee.png"
image save_jumin = "Menu Screens/Main Menu/msgsl_image_jumin.png"
image save_ray = "Menu Screens/Main Menu/msgsl_image_ray.png"
image save_empty = "Menu Screens/Main Menu/msgsl_image_save.png"
image save_seven = "Menu Screens/Main Menu/msgsl_image_seven.png"
image save_v = "Menu Screens/Main Menu/msgsl_image_v.png"
image save_xmas = "Menu Screens/Main Menu/msgsl_image_xmas.png"
image save_yoosung = "Menu Screens/Main Menu/msgsl_image_yoosung.png"
image save_zen = "Menu Screens/Main Menu/msgsl_image_zen.png"

########################################
## PHONE CONTACT IMAGES
########################################
# These images are 188x188 and round
image sa_contact = 'Phone Calls/call_contact_saeran.png'
image s_contact = 'Phone Calls/call_contact_707.png'
image empty_contact = 'Phone Calls/call_contact_empty.png'
image ja_contact = 'Phone Calls/call_contact_jaehee.png'
image ju_contact = 'Phone Calls/call_contact_jumin.png'
image r_contact = 'Phone Calls/call_contact_ray.png'
image v_contact = 'Phone Calls/call_contact_v.png'
image y_contact = 'Phone Calls/call_contact_yoosung.png'
image z_contact = 'Phone Calls/call_contact_zen.png'
image ri_contact = 'Phone Calls/call_contact_rika.png'

########################################
## STORY MODE/VN IMAGES
########################################
# These images are rectangular and typically 555x126 (with the exception
# of the party icon)
image vn_other = 'Menu Screens/Day Select/vn_other.png'
image vn_ja = 'Menu Screens/Day Select/vn_ja.png'
image vn_ju = 'Menu Screens/Day Select/vn_ju.png'
image vn_r = 'Menu Screens/Day Select/vn_r.png'
image vn_ri = 'Menu Screens/Day Select/vn_ri.png'
image vn_sa = 'Menu Screens/Day Select/vn_sa.png'
image vn_s = 'Menu Screens/Day Select/vn_s.png'
image vn_v = 'Menu Screens/Day Select/vn_v.png'
image vn_y = 'Menu Screens/Day Select/vn_y.png'
image vn_z = 'Menu Screens/Day Select/vn_z.png'
image vn_party = 'Menu Screens/Day Select/vn_party.png'
image vn_party_inactive = 'Menu Screens/Day Select/vn_party_inactive.png'

########################################
## CUSTOM MESSENGER ITEMS
########################################
# If you'd like to use custom fonts with the chat CDS, you must add them
# to these lists.
define all_fonts_list = ['sser1', 'sser2', 'ser1', 'ser2', 'curly','blocky']
define bold_xbold_fonts_list = ['sser1', 'sser2', 'ser1', 'ser2']
# And if you want them to be used in text messages, you must add them to
# this dictionary along with a path to its .ttf file
define font_dict = { 'curly' : gui.curly_font, 'ser1' : gui.serif_1,
            'ser1b' : gui.serif_1b, 'ser1xb' : gui.serif_1xb, 
            'ser2' : gui.serif_2, 'ser2b' : gui.serif_2b,
            'ser2xb' : gui.serif_2xb, 'sser1' : gui.sans_serif_1, 
            'sser1b' : gui.sans_serif_1b, 'sser1xb' : gui.sans_serif_1xb, 
            'sser2' : gui.sans_serif_2, 'sser2b' : gui.sans_serif_2b,
            'sser2xb' : gui.sans_serif_2xb, 'blocky' : gui.blocky_font}
# Similarly, if you have any custom bubbles defined, add them here.
define all_bubbles_list = ['cloud_l', 'cloud_m', 'cloud_s', 'round_l',
    'round_m', 'round_s', 'sigh_l', 'sigh_m', 'sigh_s', 'spike_l', 'spike_m',
    'spike_s', 'square_l', 'square_m', 'square_s', 'square2_l', 'square2_m',
    'square2_s', 'round2_l', 'round2_m', 'round2_s', 'flower_l', 'flower_m',
    'flower_s', 'glow2']
# All possible backgrounds are defined here. If they are a static image,
# they should be defined as `image bg morning` and the list contains 'morning'.
define all_static_backgrounds = ['morning', 'noon', 'evening', 'hack',
                'redhack', 'night', 'earlyMorn', 'redcrack']
# If there is an animated version, it goes here. They should be defined as
# `screen animated_evening` and the list contains 'evening'.
# Animated backgrounds should have a `zorder` of 0 and be tagged `animated_bg`.
define all_animated_backgrounds = ['morning', 'noon', 'evening', 'night', 
                'earlyMorn']
# This should be the same string as seen in all_static_backgrounds and
# all_animated_backgrounds. Any backgrounds in here will display chatroom
# nicknames in black. Otherwise, they are displayed in white.
define black_text_bgs = ['morning', 'noon', 'evening']



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
        #     return "Bubble/Special/r_" + msg.specBubble + ".png"        

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
            of two ints for the x and y pos of this bubble.
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

