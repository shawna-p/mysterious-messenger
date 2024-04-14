init -6 python:
    from datetime import datetime, date, timedelta
    from copy import copy, deepcopy


    class CConfirm(Show):
        """A special Action for showing confirmation prompts to the player."""

        def __init__(self, msg, yes=None, *args, **kwargs):
            if yes is None:
                yes = Hide('confirm')
                no = None
            else:
                no = Hide('confirm')
                if isinstance(yes, list):
                    yes.insert(0, Hide('confirm'))
                elif yes != Hide('confirm'):
                    yes = [Hide('confirm'), yes]
            super(CConfirm, self).__init__('confirm', None, *args, message=msg,
                yes_action=yes, no_action=no, **kwargs)


    class Start(Action, DictEquality):
        """
        Causes Ren'Py to jump out of the menu context to the named
        label. The main use of this is to start a new game from the
        main menu. Common uses are:

        * Start() - Start at the start label.
        * Start("foo") - Start at the "foo" label.

        This is copied from common/00_action_menu.rpy
        """

        def __init__(self, label="start"):
            self.label = label

        def __call__(self):
            # Save the intended start label and jump to the
            # pre-defined introduction label
            store.starter_story = self.label
            renpy.jump_out_of_context("begin_intro_mstmg")


    class ShowCG(ShowMenu):
        """A special Action for displaying a CG to the player."""

        def __init__(self, img, *args, **kwargs):
            if not isinstance(img, Album) and not isinstance(img, GalleryImage):
                img = cg_helper(img)
            super(ShowCG, self).__init__('viewCG_fullsize', *args,
                fullsizeCG=img, **kwargs)


    class JumpVN(Call):
        """
        A special Action for jumping to a Story Mode (VN) in the
        middle of a chatroom.
        """

        def __init__(self, label, *args, **kwargs):
            """
            Initializes a JumpVN action.

            label : string
                The label to jump to for this VN.
            """

            super(JumpVN, self).__init__('vn_during_chat', *args, vn_label=label,
                from_link=True, **kwargs)


    class LinkJump(Call):
        """
        A special Action for jumping to a label or menu when clicking on a link,
        bypassing the answer button at the bottom of the screen.
        """

        def __init__(self, label=None, is_menu=False):
            self.label = label
            self.is_menu = is_menu

        def __call__(self):
            if self.is_menu:
                store.answer_shown = True
            store.choosing = False
            store.chatbackup = None
            if self.label is None:
                # No need to jump anywhere; this is right
                # after the link
                if store.chat_stopped:
                    store.chat_stopped = False
                    renpy.call('play_after_link')
                return
            if not renpy.has_label(self.label):
                ScriptError("Could not find label \"", self.label, "\".")
            else:
                if store.chat_stopped:
                    store.chat_stopped = False
                    renpy.call('play_after_link', jump_link=self.label)
                else:
                    renpy.jump(self.label)


    class ContinueChat(Call):
        """A special action which continues the chat when called."""

        def __init__(self, *args, **kwargs):
            super(ContinueChat, self).__init__('play_after_link')

        def __call__(self):
            store.choosing = False
            store.chat_stopped = False
            # If observing?
            super(ContinueChat, self).__call__()


    def IfChatStopped(true_list, false_list=None):
        """
        A function that acts like an action. Has two parameters, what action
        to do if chat_stopped is True and what to do if it's False.
        """

        return (true_list, false_list)


    from collections import namedtuple
    GameTone = namedtuple('GameTone', ['title', 'file'])

    class ToneCategory(object):
        """
        A class to better organize the categories of the various
        phone/text/email tones found in the game.

        Attributes:
        -----------
        category : string
            The name of the category.
        folder : string
            The folder name and/or prefix that should be added to the start
            of each tone in this category.
        ext : string
            The file extension for each tone in this category e.g. "wav"
        tones : GameTone
            A list of GameTone tuples containing the title and file of a tone.
        condition : string
            A string that evaluates to a condition which determines whether a
            tone should be shown to the player or not.
        """

        def __init__(self, category, folder, ext, *args, **kwargs):
            """
            Create a ToneCategory object to hold the information on a category
            of tones.

            Parameters:
            -----------
            category : string
                The name of the category
            folder : string
                The folder name and/or prefix that should be added to the start
                of each tone in this category.
            ext : string
                The file extension for each tone in this category e.g. "wav"
            args
                Expected to be a list of title, field pairs (both strings) that
                will be added to the tone dictionary.
            kwargs
                May contain the keyword argument "condition", which should
                evaluate to a Python condition that determines whether this
                category should be shown to the player.
            """

            self.category = category
            if len(ext) > 0 and ext[0] != ".":
                ext = "." + ext
            self.folder = folder
            self.ext = ext
            self.tones = [ ]
            self.condition = kwargs.get('condition', 'True')

            for i in range(0, len(args), 2):
                try:
                    # args should come in (title, file) pairs
                    title = args[i]
                    file = args[i+1]
                    self.add_tone(title, file)
                except IndexError:
                    ScriptError("Given tone", args[i], "does not have a",
                        "corresponding file path.",
                        header="Miscellaneous",
                        subheader="Adding New Ringtones, Text Tones, & Email Tones")
                    return

        def add_tone(self, title, file):
            """Add this tone to the category."""

            if isinstance(title, ChatCharacter):
                title = title.name
            file = self.folder + file + self.ext

            self.tones.append(GameTone(title, file))

        def eval_condition(self):
            """
            Evaluate the condition on this category to determine if it
            should be available.
            """

            try:
                return renpy.python.py_eval(self.condition)
            except:
                # Notify the user if the condition could not be evaluated.
                ScriptError("Could not evaluate condition", self.condition,
                    "for a tone category",
                    header="Miscellaneous",
                    subheader="Adding New Ringtones, Text Tones, & Email Tones")
                return True


    class MyTime(object):
        """
        A class that fetches the current time/date information and stores
        it in easy-to-access fields.

        Attributes:
        -----------
        short_weekday : string
            Shortened name of the day of the week e.g. Mon
        weekday : string
            Full name of the day of the week e.g. Monday
        short_month : string
            Shortened name of the month e.g. Aug
        month : string
            Full name of the day of the month e.g. August
        month_num : string
            Number (1-12) of the month e.g. "8"
        year : string
            Year for the date e.g. "2018"
        day : string
            Day number for the date e.g. "21"
        twelve_hour : string
            Hour in twelve-hour format e.g. "10"
        military_hour : string
            Hour in military format e.g. "22"
        minute : string
            Minute for the time e.g. "32"
        second : string
            Second for the time e.g. "10"
        am_pm : string
            Equal to "PM" or "AM" depending on the time.
        """

        def __init__(self, day=None, thehour=None, themin=None):
            """
            Create a MyTime object to store date and time information.

            Parameters:
            -----------
            day : int
                A number of days (<0 in the past, >0 in the future) to use
                for this object.
            thehour : string
                The hour, in military time, for this timestamp e.g. "23"
            themin : string
                The minutes for this timestamp e.g. "42".
            """

            self.datetime = datetime.now()

            day_diff = 0
            hour_diff = 0
            min_diff = 0

            # Do some calculations for the date, if it's in the past or future
            if day is not None:
                day_diff = day * 60 * 60 * 24
            if thehour is not None:
                hour_diff = int(thehour) - int(self.datetime.strftime('%H'))
                hour_diff = hour_diff * 60 * 60
            if themin is not None:
                min_diff = int(themin) - int(self.datetime.strftime('%M'))
                min_diff = min_diff * 60

            unix_seconds = time.time()
            new_timestamp = unix_seconds + day_diff + hour_diff + min_diff

            self.datetime = datetime.fromtimestamp(new_timestamp)

        @property
        def short_weekday(self):
            try:
                return self.datetime.strftime('%a')
            except:
                return self.__dict__['short_weekday']
        @property
        def weekday(self):
            try:
                return self.datetime.strftime('%A')
            except:
                return self.__dict__['weekday']
        @property
        def short_month(self):
            try:
                return self.datetime.strftime('%b')
            except:
                return self.__dict__['short_month']
        @property
        def month(self):
            try:
                return self.datetime.strftime('%B')
            except:
                return self.__dict__['month']
        @property
        def month_num(self):
            try:
                return self.datetime.strftime('%m')
            except:
                return self.__dict__['month_num']
        @property
        def year(self):
            try:
                return self.datetime.strftime('%Y')
            except:
                return self.__dict__['year']
        @property
        def day(self):
            try:
                return self.datetime.strftime('%d')
            except:
                return self.__dict__['day']
        @property
        def twelve_hour(self):
            try:
                return self.datetime.strftime('%I')
            except:
                return self.__dict__['twelve_hour']
        @property
        def military_hour(self):
            try:
                return self.datetime.strftime('%H')
            except:
                return self.__dict__['military_hour']
        @property
        def minute(self):
            try:
                return self.datetime.strftime('%M')
            except:
                return self.__dict__['minute']
        @property
        def second(self):
            try:
                return self.datetime.strftime('%S')
            except:
                return self.__dict__['second']
        @property
        def am_pm(self):
            try:
                return self.datetime.strftime('%p')
            except:
                return self.__dict__['am_pm']

        def get_phone_time(self):
            """Return the time formatted as displayed for phone calls."""

            # Returns a time like 10:15 PM, 25/10
            return (self.twelve_hour + ":" + self.minute
                + " " + self.am_pm + ", " + self.day + "/"
                + self.month_num)

        def get_twelve_hour(self):
            """Return the time formatted as 10:45 AM"""

            return self.twelve_hour + ':' + self.minute + ' ' + self.am_pm

        def get_text_msg_time(self):
            """Return the time formatted for text messages."""

            # Returns a time like 15/08/2020 11:58 PM
            return (self.day + '/' + self.month_num
                        + '/' + self.year + ' '
                        + self.twelve_hour + ':'
                        + self.minute + self.am_pm)

        @property
        def text_separator_time(self):
            """Return the time formatted for the text message date separator."""

            # Returns a time like 2020.08.15 Saturday
            return (self.year + '.' + self.month_num + '.' + self.day
                + ' ' + self.weekday)

        def has_occurred(self):
            """
            Return True if this time has already passed compared to
            the current date and time.
            """

            try:
                if self.datetime <= datetime.now():
                    return True
                return False
            except:
                print_file("Could not compare datetime objects")

            cur_time = upTime()
            # Check the year
            if int(self.year) < int(cur_time.year):
                return True
            elif int(self.year) > int(cur_time.year):
                return False
            # Check the month
            if int(self.month_num) < int(cur_time.month_num):
                return True
            elif int(self.month_num) > int(cur_time.month_num):
                return False
            # Check the day
            if int(self.day) < int(cur_time.day):
                return True
            elif int(self.day) > int(cur_time.day):
                return False
            # Check the hour
            if int(self.military_hour) < int(cur_time.military_hour):
                return True
            elif int(self.military_hour) > int(cur_time.military_hour):
                return False
            # Check the minutes
            if int(self.minute) <= int(cur_time.minute):
                return True
            else:
                return False

        def adjust_time(self, td):
            """Adjust the datetime according to timedelta td."""
            try:
                self.datetime += td
            except:
                print("ERROR: Couldn't adjust datetime.")
                renpy.show_screen('messenger_error')

        def time_diff_minimum(self, other_time, day=None, hour=None,
                minute=None):
            """
            Return True if the other_time is at least the given time later
            than this time.
            """

            try:
                td = self.datetime - other_time.datetime
                mtd = MyTimeDelta(td)
                if day and mtd.days >= day:
                    return True
                if hour and mtd.hours >= hour:
                    return True
                if minute and mtd.minutes >= minute:
                    return True
                return False
            except AttributeError:
                if day and int(self.day) + day <= int(other_time.day):
                    return True
                # Not going to do any more complex calculations
                print_file("WARNING: Can't properly compare time differences.")
                return False

        @property
        def stopwatch_time(self):
            """Return a timestamp including seconds."""
            # Returns a time like 21:04:52
            return self.military_hour + ":" + self.minute + ":" + self.second

        def __eq__(self, other):
            """Check for equality between two MyTime objects."""
            try:
                return self.datetime == other.datetime
            except:
                return (self.military_hour == other.military_hour
                    and self.minute == other.minute
                    and self.second == other.second)

        def __ne__(self, other):
            return not self.__eq__(other)


    def upTime(day=None, thetime=None):
        """
        Return a MyTime object with the current time, or a time based
        on the given arguments.

        Parameters:
        -----------
        day : None or int
            The number of days in the past (<0) or in the future (>0) this
            timestamp should be created for.
        thetime : string
            A string in the format "00:00" that represents the time this
            timestamp should represent.

        Returns:
        --------
        MyTime
            If day=None, returns a MyTime object representing the current
            date with either the specified time or the given time.
            If thetime=None, the time in the MyTime object will reflect the
            current time.
        """

        if day is not None and thetime is None:
            return MyTime(day)
        elif thetime is not None:
            # Get the hour and minute
            thehour = thetime[:2]
            themin = thetime[-2:]
            return MyTime(day, thehour, themin)
        else:
            return MyTime()


    class MyTimeDelta(store.object):
        """
        A class with properties to make it easy to parse a timedelta object.
        It represents the length of time between two datetime objects.

        Attributes:
        -----------
        days : int
            Number of days represented in this object.
        hours : int
            Number of hours represented in this object.
        minutes : int
            Number of minutes represented in this object.
        seconds : int
            Number of seconds represented in this object.
        td : timedelta
            The timedelta object this class is wrapping.
        """

        def __init__(self, td=None):
            """
            Create a MyTimeDelta object for easier access of fields.

            Parameters:
            -----------
            td : timedelta
                The timedelta object this object is wrapping.
            """

            self.td = td

            if td is None:
                # This item should be infinity
                self.seconds = float('inf')
                self.minutes = float('inf')
                self.hours = float('inf')
                self.days = float('inf')
                return

            # Determine total number of seconds
            self.seconds = int(td.total_seconds())
            # Calculate the other fields
            self.minutes = self.seconds // 60
            self.hours = self.minutes // 60
            self.days = self.hours // 24


    def new_route_setup(route, chatroom_label=None, participants=None):
        """Set up variables for a new route."""

        global story_archive, current_timeline_item, starter_story

        if (isinstance(route, store.Route) or isinstance(route, Route)):
            # Got a Route object; use the default route
            try:
                route = route.default_branch
            except AttributeError:
                ScriptError("Given Route object does not have a ",
                    "default_branch field.",
                    link="route-setup", link_text="Setting up a Route")

        if (len(route) > 0
                and (isinstance(route[0], RouteDay)
                    or isinstance(route[0], store.RouteDay))):
            story_archive = route
        else:
            story_archive = route[1:]

        if participants is None:
            participants = []
        if not isinstance(participants, list):
            # Check if this is a valid participant
            if not isinstance(participants, ChatCharacter):
                ScriptError("Given participants list for new_route_setup",
                    "is not recognized as a ChatCharacter or list of",
                    "ChatCharacters.",
                    header="route-setup", subheader="Chatrooms",
                    link_text="Adding a Chatroom")
                participants = [ ]
            else:
                participants = [participants]
        define_variables(False)
        try:
            if chatroom_label is None and isinstance(store.mlabel, basestring):
                chatroom_label = store.mlabel
            else:
                chatroom_label = 'starter_chat'
        except:
            chatroom_label = 'starter_chat'
        current_timeline_item = ChatRoom('Introduction', chatroom_label,
                                        '00:00', participants)
        # This sets a specific variable that lets you have phone calls/
        # VNs for a starter chat/opening
        starter_story = True
        renpy.retain_after_load()
        # Load it as though it is a chatroom
        begin_timeline_item(generic_chatroom)
        return

    def hide_all_popups():
        """Hide all popup screens in-game."""

        for i in range(10):
            # Hopefully we don't have more than 10 popups at once
            scr = store.showing_text_screens.get(i, None)
            if scr is not None:
                renpy.hide_screen(scr)
        text_screen_tags = set()
        showing_text_screens = dict()

        for tag in store.screen_tags:
            renpy.hide_screen(tag)
        store.screen_tags = set()
        return

    def btn_hover_img(s):
        """A displayable prefix function to make button hover images."""

        return Fixed(s, Transform(s, alpha=0.5))

    def center_bg_img(s):
        """
        A displayable prefix function to display backgrounds and
        their shake counterparts.
        """

        return Fixed(Transform(s,
            align=(0.5, 1.0), yoffset=-113,
            ysize=config.screen_height-113-165,
            xsize=config.screen_width, fit="cover"),
            xysize=(config.screen_width, config.screen_height)
        )

    def center_full_img(s):
        """
        A displayable prefix function to display backgrounds and
        their shake counterparts.
        """

        return Fixed(Transform(s,
            align=(0.5, 1.0),
            ysize=config.screen_height-113-165,
            xsize=config.screen_width, fit="cover"),
            xysize=(config.screen_width, config.screen_height)
        )

    def center_crop_bg_img(s):
        """
        A displayable prefix function which crops and centers a background
        image to display as 'shake'.
        """

        s = Transform(s, crop=(0, (1334-1125)//2, 750, 1125))

        return Fixed(
            Transform(s, align=(0.5, 1.0), yoffset=-113,
            ysize=config.screen_height-113-165, xsize=config.screen_width,
            fit="cover"),
            xysize=(config.screen_width, config.screen_height)
        )

    def big_tag(tag, argument, contents):
        """
        A custom text tag designed to work similarly to the msg CDS "big"
        argument.
        """

        return [
                (renpy.TEXT_TAG, u"size=+10"),
            ] + contents + [
                (renpy.TEXT_TAG, u"/size"),
            ]

    def resize_center_bg(img):
        return Transform(img,
            align=(0.5, 1.0),
            xsize=config.screen_width,
            ysize=config.screen_height,
            fit="cover"
        )

    config.custom_text_tags["big"] = big_tag

    ## Displayable prefix definitions
    config.displayable_prefix["btn_hover"] = btn_hover_img
    config.displayable_prefix["center_bg"] = center_bg_img
    config.displayable_prefix["center_full"] = center_full_img
    config.displayable_prefix["center_crop_bg"] = center_crop_bg_img
    config.displayable_prefix["resize"] = resize_center_bg


    def get_text_width(the_text, the_style='default', size=None):
        """Return the width of text with a certain style applied."""
        if size is None:
            return int(Text(the_text, style=the_style).size()[0])
        else:
            return int(Text(the_text, style=the_style, size=size).size()[0])

    def get_char_from_file_id(file_id):
        """
        Return the ChatCharacter associated with the given file_id, or None
        if no ChatCharacter could be found.
        """

        try:
            char = getattr(store, file_id)
            return char
        except AttributeError:
            for char in store.all_characters:
                if char.file_id == file_id:
                    return char
            for char in store.phone_only_characters:
                if char.file_id == file_id:
                    return char
        return None

    def print_file(*args, **kwargs):
        """Print statements to a file or to the console for debugging."""

        DEBUG = None
        if DEBUG is None:
            return

        if not DEBUG:
            print(*args, **kwargs)
            return
        # Otherwise, print this to a file for debugging
        try:
            with open(os.path.join(renpy.config.basedir,
                    "game_output.txt"), 'a') as f:
                print(*args, file=f, **kwargs)
        except:
            print("Print to file did not work:", args)

    def get_img_from_file():
        """
        (Windows only) Display a file picker to the player to get an
        image for use in-game.
        """

        import subprocess, os

        try:
            if not can_pick_image():
                return None
            # Look for exe in the game dir
            out_gamedir = renpy.config.gamedir[:-5]
            filepath = os.path.join( out_gamedir, "file_picker.exe")
            thevar = subprocess.check_output([filepath])
            thevar.strip()
            if ".webp" in thevar:
                thevar = thevar.split('.webp')[0] + '.webp'
            elif ".png" in thevar:
                thevar = thevar.split('.png')[0] + '.png'
            elif ".jpg" in thevar:
                thevar = thevar.split('.jpg')[0] + '.jpg'
            else:
                thevar = None
        except:
            return None
        # Make sure Ren'Py can load the image
        if thevar and renpy.loadable(thevar):
            return thevar
        return None

    def set_pfp_from_file():
        """
        (Windows only) Set the player's profile picture from a file.
        """

        the_img = get_img_from_file()
        if the_img is None:
            # Can't use this as a profile picture
            renpy.run(CConfirm("This image cannot be used as a profile picture."))
            return
        # Otherwise, we're good to go
        store.m.prof_pic = the_img
        return

    def can_pick_image():
        """Return True if a file-picker is available."""
        from platform import system
        # Can only use file picker on Windows
        sys = system().lower()
        if "windows" not in sys and "win" not in sys:
            return False
        # Does the file picker exist?
        out_gamedir = renpy.config.gamedir[:-5]
        filepath = os.path.join( out_gamedir, "file_picker.exe")
        if not os.path.exists(filepath):
            return False

        return True

    def ScriptError(*args, **kwargs):
        """
        Print an error message and display a pop-up to the user informing
        them of an error in their script. Can also link to an appropriate
        page in the documentation.

        Parameters:
        -----------
        args : strings
            A list of strings which will be printed out as part of the
            error message.
        kwargs - link : string
            A string used as part of the link to lead to an appropriate
            page in the documentation.
        kwargs - link_text : string
            The text the link should be attached to.
        """

        # First, convert all arguments to strings
        str_args = [ ]
        for arg in args:
            try:
                str_args.append(str(arg))
            except:
                print_file("ERROR: Couldn't convert arg to a string.")

        # Construct the args into a sentence, being mindful of quotes
        sentence = ""
        open_quote = False
        new_quote = False
        for arg in str_args:
            if arg and arg[-1] == '"' and not open_quote:
                open_quote = True
                new_quote = True
            if arg and arg[0] == '"' and not new_quote:
                open_quote = False
            sentence += arg
            if not open_quote and arg != str_args[-1]:
                sentence += " "
            new_quote = False

        # Print the message to the console
        print("WARNING:", sentence)

        link = kwargs.get('link', False)
        header = kwargs.get('header', False)
        sub_header = kwargs.get('sub_header', '') or kwargs.get('subheader', '')
        link_text = kwargs.get('link_text', False)
        if header or sub_header and not link_text:
            if sub_header:
                link_text = sub_header
            elif header:
                link_text = header
        if header:
            header = header.replace(' ', '-')
            header = header.lower()
            header += ".html"
        if sub_header:
            sub_header = sub_header.replace(' ', '-')
            sub_header = sub_header.lower()
            sub_header = "#" + sub_header
        if header:
            link = header + sub_header

        # Now show the error message screen
        renpy.show_screen('script_error', message=sentence, link=link,
            link_text=link_text)

    def combine_lists(*args):
        """
        Combine args into one giant list and return it. Removes duplicates.
        """

        result = []
        for arg in args:
            if isinstance(arg, list):
                for pic in arg:
                    if pic not in result:
                        result.append(pic)
            else:
                if arg not in result:
                    result.append(arg)
        return result

    def handle_missing_image(img):
        """Give a generic image to use when an image cannot be found."""

        # First try to see if the image has an equivalent .webp version
        try:
            if '.webp' not in img:
                new_img = img.split('.')[0] + '.webp'
                if renpy.loadable(new_img):
                    return Image(new_img)
                return None
            # Replace the old VN window backgrounds
            if "VN Mode/Chat Bubbles/vnmode_" in img:
                #prefix = "VN Mode/Chat Bubbles/vnmode_"
                if "0." in img or "ju." in img:
                    return colorize_vn_window("#648EFC")
                elif "1." in img or "z." in img:
                    return colorize_vn_window("#929292")
                elif "2." in img or "s." in img:
                    return colorize_vn_window("#F54848")
                elif "3." in img or "y." in img:
                    return colorize_vn_window("#75C480")
                elif "4." in img or "ja." in img:
                    return colorize_vn_window("#C8954D")
                elif "5." in img or "v." in img:
                    return colorize_vn_window("#7ED4C7")
                elif "7." in img or "ri." in img:
                    return colorize_vn_window("#A774CC")
                elif "8." in img or "sa." in img:
                    return colorize_vn_window("#FC9796")
                else:
                    return colorize_vn_window("#b7b7b7")
        except:
            pass
        # Otherwise, assume the image couldn't be found.
        return None

    def handle_missing_label(lbl):
        """
        Determine how Ren'Py should proceed if it cannot find the given label.
        """

        if lbl in ['main_menu', '_library_main_menu']:
            return None
        if lbl[0] == "_":
            return None
        ScriptError("Could not find the label", lbl)

        if lbl == store.current_timeline_item.item_label:
            # Couldn't find this item's correct label; use `just_return` as a
            # replacement since it just returns
            return 'just_return'
        if lbl == store.current_timeline_item.expired_label:
            # Try jumping to the regular, non-expired label
            return store.current_timeline_item.item_label
        # Otherwise, it might be more of an internal issue
        return None

    # This lets the program shuffle menu options
    renpy_menu = menu
    def menu(items):
        # Copy the items list
        items = list(items)
        global shuffle
        if shuffle and shuffle not in ["last", "default"]:
            renpy.random.shuffle(items)
        elif shuffle == "last":
            last = items.pop()
            renpy.random.shuffle(items)
            items.append(last)
        elif shuffle == "default":
            # Don't shuffle or modify these answers
            shuffle = True
            return renpy_menu(items)
        shuffle = True

        # If observing, check which items have already been seen
        new_items = []
        if store.observing and not store._in_replay and store.current_choices:
            # Restrict choices to what's been selected this playthrough
            the_choice = store.current_choices.pop(0)
            new_items = [ i for i in items if i[0] == the_choice ]
        if store.observing and not new_items:
            new_items = [ i for i in items if i[1].get_chosen() ]
        if new_items:
            items = new_items
        return renpy_menu(items)

    # Don't let the player rollback the game by scrolling.
    try:
        config.keymap['rollback'].remove('mousedown_4')
    except ValueError:
        pass
    try:
        config.keymap['rollback'].remove('K_PAGEUP')
    except ValueError:
        pass
    try:
        config.keymap['rollback'].remove('repeat_K_PAGEUP')
    except ValueError:
        pass
    # Allow right clicks for alternate button actions.
    try:
        config.keymap['game_menu'].remove('mouseup_3')
    except ValueError:
        pass

    def custom_show(name, at_list=None, layer='master', what=None,
            zorder=0, tag=None, behind=None, **kwargs):
        """
        A custom statement which replaces the default `show` statement in order
        to work with chatrooms.

        Parameters:
        -----------
        name : string
            The name of the image to show.
        at_list : transforms[]
            A list of transforms that are applied to the image. The equivalent
            of the `at` property.
        layer : string
            Gives the name of the layer on which the image will be shown. The
            equivalent of the `onlayer` property. If None, uses the default
            layer associated with the tag.
        what : Displayable or None
            A displayable that will be shown in lieu of looking on the image.
            (The equivalent of the `show expression` statement). When a `what`
            parameter is given, `name` can be used to associate a tag with
            the image.
        zorder : int
            The equivalent of the `zorder` property. If None, the zorder is
            preserved if it exists, and is otherwise set to 0.
        tag : string
            Specifies the image tag of the shown image. The equivalent of the
            `as` property.
        behind : string[]
            A list of image tags that this image is shown behind. The equivalent
            of the `behind` property.

        Result:
        -------
            Displays the image on the screen according to the given parameters.
        """

        # This helps paraphrasing to work with Story Mode
        if (not store.dialogue_paraphrase and store.dialogue_picked != ""):
            say_choice_caption(store.dialogue_picked,
                store.dialogue_paraphrase, store.dialogue_pv)

        # Chatroom-specific statements
        if gamestate == CHAT and not at_list:
            # The scrolling hack effect should be shown
            if ('hack' in name and 'effect' in name):
                renpy.call('hack', reverse=('reverse' in name))
                return
            elif ((('redhack' in name) or ('red' in name and 'hack' in name))
                    and 'effect' in name):
                renpy.call('redhack', reverse=('reverse' in name))
                return
            # The scrolling red static effect
            elif ("red" in name and "static" in name and "effect" in name):
                renpy.call('red_static', reverse=('reverse' in name))
                return
            ## Banners
            elif ('lightning' in name and 'banner' in name):
                renpy.call('banner', banner='lightning')
                return
            elif ('well' in name and 'banner' in name):
                renpy.call('banner', banner='well')
                return
            elif ('annoy' in name and 'banner' in name):
                renpy.call('banner', banner='annoy')
                return
            elif ('heart' in name and 'banner' in name):
                renpy.call('banner', banner='heart')
                return
            ## The shake effect
            elif ( name == ('shake',)):
                renpy.call('shake')
                return
            ## The secure chat animation
            elif ('secure' in name and 'anim' in name):
                renpy.call('secure_anim')
                return
            ## The screen crack overlay
            elif ('screen_crack' in name):
                renpy.call('screen_crack_overlay')
                return
            ## Chatroom backgrounds
            elif (not ('bg' in name and 'black' in name)):
                # The messenger screen is showing, therefore this statement is
                # likely being used in conjunction with `scene` to display a
                # chatroom background
                if isinstance(name, tuple) and name[0] == 'bg':
                    set_chatroom_background(name[1])
                elif isinstance(name, tuple):
                    set_chatroom_background(name[0])
                else:
                    set_chatroom_background(name)
                return

        elif gamestate == VNMODE and 'bg' in name:
            at_list.insert(0, scale_vn_bg)
        elif gamestate == VNMODE and name == ('shake',):
            if persistent.screenshake:
                #renpy.show_layer_at(shake, 'master')
                renpy.with_statement(hpunch)
                return

        at_list = at_list or []
        behind = behind or []

        renpy.exports.show(name, at_list, layer, what, zorder, tag, behind, **kwargs)

    def custom_hide(name, layer=None):
        """
        A custom statement which replaces the default `hide` statement for
        compatibility with other program features such as menu paraphrasing.

        Parameters:
        -----------
        name : string
            The name of the image to hide. Only the image tag is used, and any
            image with the tag is hidden (the precise name does not matter).
        layer : string
            The layer on which this function operates. If None, uses the
            default layer associated with the tag.

        Result:
        -------
            Executes a say statement for the main character if applicable and
            hides the given image.
        """

        # This helps paraphrasing to work with Story Mode
        if (not store.dialogue_paraphrase and store.dialogue_picked != ""):
            say_choice_caption(store.dialogue_picked,
                store.dialogue_paraphrase, store.dialogue_pv)

        renpy.hide(name, layer)

    import requests
    LATEST_UPDATE_URL = "https://api.github.com/repos/shawna-p/mysterious-messenger/releases/latest"
    RELEASES_UPDATE_URL = "https://api.github.com/repos/shawna-p/mysterious-messenger/releases"
    CHECK_INTERVAL_TIME = 3600*6 # How long to wait before checking for updates

    def check_version(test=False, force=False):
        """
        Check for updates to Mysterious Messenger.

        Parameters:
        -----------
        test : bool
            True for testing; bypasses checks for update time and whether the
            current version is already up-to-date.
        force : bool
            True if the user is forcing an update check from the update menu.
        """

        if renpy.variant("mobile") or not config.developer:
            # Don't check for updates on mobile or if not developing
            return
        # When's the last time the program checked for an update? If it's
        # too recent, stop.
        if store.persistent.last_update_check is None:
            pass
        elif force:
            pass
        elif time.time() < store.persistent.last_update_check + CHECK_INTERVAL_TIME:
            # Too soon; don't check
            print_file("We already checked for updates not long ago")
            if not test:
                return

        store.persistent.last_update_check = time.time()

        try:
            # Parse for relevant information
            if not store.persistent.check_for_prerelease :
                rel = return_version_info(stable=True)
            else:
                rel = return_version_info(stable=False)
            if rel is None:
                return
            version_tag = rel['tag_name']
            is_prerelease = rel['prerelease']
            publish_time = rel['published_at']
            download_link = rel['zipball_url']
            ver_name = rel['name']
        except Exception as e:
            print("ERROR while checking for updates:", e)
            print("Could not connect to the internet to check for updates")
            if force:
                renpy.show_screen("confirm", message=("Could not check for "
                    + "updates. Make sure you're connected to the internet "
                    + "before trying again."),
                    yes_action=Hide('confirm'))
            return

        try:
            # Compare version tag with current version
            version_tag = version_tag[1:] # Strip the starting 'v'
            if is_prerelease:
                version_tag = version_tag[:-5] # Strip the -beta suffix
            if version_tag == store.config.version:
                # Program is up-to-date; reset available update and return
                store.persistent.available_update = [ ]
                if force:
                    renpy.show_screen("confirm", message=("Your program is "
                        + "already up-to-date."),
                    yes_action=Hide('confirm'))
                if not test:
                    return
            # Otherwise, notify the user that they can update to this
            # newer version.
            pretty_time = publish_time[:10]
            prerelease_yn = "Yes" if is_prerelease else "No"
        except Exception as e:
            print("ERROR getting update:", e)

        store.persistent.available_update = [ ver_name, version_tag,
            pretty_time, prerelease_yn, download_link ]
        renpy.show_screen('program_updates', store.persistent.available_update)

    def return_version_info(stable=False):
        """
        Return information for the stable version of Mysterious Messenger,
        after retrieving information from the GitHub API.
        """

        response = requests.get(RELEASES_UPDATE_URL)
        releases = response.json()
        for rel in releases:
            # Check if this release matches the current version; if so,
            # there are no newer updates
            ver_tag = rel['tag_name']
            if ver_tag:
                ver_tag = ver_tag[1:] # Strip the starting 'v'
                if rel['prerelease']:
                    ver_tag = ver_tag[:-5] # Strip the -beta suffix
                if ver_tag == store.config.version:
                    return rel
            # Don't look at prereleases if we only want full releases
            if stable and rel['prerelease']:
                continue
            if ver_tag not in store.persistent.ignored_versions:
                return rel
        return None

    def reorient_game():
        """
        A function which is called when the game can't reorient itself
        on a load.
        """

        print("WARNING: Failed to recover when loading game.")

        return 'reload_game_restart'

    def align_to_pos(x, y, xsize, ysize):

        anchorx = x*float(xsize)
        anchory = y*float(ysize)

        return (int(anchorx//2), int(anchory//2))

    def align_new_dimensions(y):
        return y*1334.0/float(config.screen_height)

    def get_dict_keys(d):
        # Get the keys from a dictionary. Used to retain compatibility
        # between Ren'Py 7.4+ and 8.0+
        if renpy.version_only.startswith("7"):
            return d.keys()
        else:
            return list(d.keys())

    # Some colour names, mostly for testing
    WHITE = "#FFF"
    BLACK = "#000"
    SILVER = "#c0c0c0"
    GRAY = "#808080"
    RED = "#F00"
    MAROON = "#800000"
    YELLOW = "#FF0"
    OLIVE = "#808000"
    LIME = "#0F0"
    GREEN = "#008000"
    AQUA = "#0FF"
    TEAL = "#008080"
    BLUE = "#00F"
    NAVY = "#000080"
    FUCHSIA = "#F0F"
    PURPLE = "#800080"

# Track the last time the program checked for updates
default persistent.last_update_check = None
# True if the program should automatically check for updates
default persistent.check_for_updates = True
# True if the program should include prerelease updates
default persistent.check_for_prerelease = False
# List of ignored versions for updates
default persistent.ignored_versions = [ ]
# Information on the next available update
default persistent.available_update = [ ]

# These definitions allow the program to get the first pass at show/hide/scene
# statements, to be compatible with chatrooms and paraphrasing.
define config.show = custom_show
define config.hide = custom_hide

## A label the program can jump to in the event it cannot find a
## regular label to jump to
label just_return():
    return

# This tells the program to randomly shuffle the order
# of responses
default shuffle = True

init offset = 4
## Generic variables that are used for some program calls and setup.
default generic_chatroom = ChatRoom('Chatroom', 'generic_chatroom', '00:00')
default generic_storymode = StoryMode('Story Mode', 'generic_storymode', '00:00')
default generic_storycall = StoryCall('Story Call', 'generic_storycall', '00:00', None)
default generic_timeline_items = [generic_chatroom, generic_storycall, generic_storymode]
init offset = 0

## A label that's called when a load failed and Ren'Py can't recover
define config.load_failed_label = reorient_game

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
# continue expiring chatrooms
default days_to_expire = 1
# Keeps a record of the current time to compare
# with load times so it knows when to make days
# available
default current_game_day = date.today()
# Lets the program know how to advance days when loading
default persistent.load_instr = False
# True if the player is beginning a new game
default starter_story = False
# When expiring items, this is equal to the item being expired
default expiring_item = None

# Story Mode preferences
default preferences.afm_time = 15
default preferences.skip_unseen = True
default preferences.skip_after_choices = True

# The automatic save file used by the program
define mm_auto = "mm_auto_save"
# "Unlocks" some developer options for testing
default persistent.testing_mode = False
# Used with testing mode; allows you to skip over a story item.
default skip_story_item = False
# Used for testing; ensures all story items are available immediately.
default persistent.unlock_all_story = False


#************************************
# Chatroom Backgrounds
#************************************
image bg morning = "center_bg:Phone UI/bg-morning.webp"
image bg evening = "center_bg:Phone UI/bg-evening.webp"
image bg night = "center_bg:Phone UI/bg-night.webp"
image bg earlyMorn = "center_bg:Phone UI/bg-earlyMorn.webp"
image bg noon = "center_bg:Phone UI/bg-noon.webp"
image bg rainy_day = "center_bg:Phone UI/bg-rainy-day.webp"
image bg snowy_day = "center_full:Phone UI/bg-snowy-day.webp"
image bg morning_snow = "center_full:Phone UI/bg-morning-snow.webp"

image bg hack = "center_crop_bg:Phone UI/bg-hack.webp"
image bg redhack = "center_crop_bg:Phone UI/bg-redhack.webp"
image bg redcrack = "center_crop_bg:Phone UI/bg-redhack-crack.webp"
image bg secure = "center_bg:Phone UI/bg_secure.webp"
image black = "#000000"


## The "secure chatroom" animation
image secure_lock = "Phone UI/chat_lock_secure.webp"
image secure_lock_glow = "Phone UI/chat_lock_glow.webp"

transform lock_spin():
    rotate 0
    ease 1.2 rotate -360

image secure_chat_intro = Fixed(
    # The background
    Transform('Phone UI/bg_secure.webp', zoom=1.19, align=(0.5, 0.5)),
    # The lock
    Fixed(Transform('secure_lock', align=(0.5, 0.5)),
        # The circle animation
        At(Fixed(Transform('secure_lock_glow', align=(0.0, 0.5)),
            xysize=(545, 545), align=(0.5, 0.5)
        ), lock_spin),
        align=(0.5, 0.5), xysize=(545, 545)
    ),
    xysize=(892, 1334), align=(0.5, 0.5)
)

# A starry night background with some static stars;
# used in menu screens
image bg starry_night = "Menu Screens/Main Menu/bg-starry-night.webp"
image hack_long = "Phone UI/Hack-Long.webp"
image red_hack_long = "Phone UI/Hack-Red-Long.webp"
image transparent_img = '#0000'

# ********************************
# Short forms/Startup Variables
# ********************************
# What state the game is in
default gamestate = None
define CHAT = 1
# Replaces in_phone_call TODO: Set this during incoming/outgoing calls too
define PHONE = 2
# Replaces text_msg_reply
define TEXTMSG = 3
# Replaces vn_choice
define VNMODE = 4
# Replaces email_reply
define EMAIL = 5

# Displays all the messages in a chatroom
default chatlog = []
# A list of the characters currently in the chatroom
default in_chat = []
# Holds the current timeline item the player is going through.
default current_timeline_item = ChatRoom('title', 'chatroom_label', '00:00')
# Item that should be used when saving the game or used for plot branches.
default most_recent_item = None
default name = 'Rainbow'
default chat_name = 'Rainbow'
default hacked_effect = False
# True if the player can receive hourglasses in chatrooms
default persistent.receive_hg = True

# Checks if the player is on a route or not
default persistent.on_route = False
# Checks if it's the first time you've started the game
default persistent.first_boot = True
# Determines if the program should run in real-time or not
default persistent.real_time = False
# Check if the program needs to manually load the chat home screen
default persistent.just_loaded = False

# Set to True if you're viewing a previously-seen chatroom/call/etc
default observing = False

# Detects if you're choosing an option from a menu
# If so, the program uses this variable to disable most buttons
default choosing = False

# Detects if the answer screen should be showing. Useful if you
# view a CG when you should be answering a prompt
default pre_choosing = False

# This keeps track of the sorts of heart points earned over a timeline item
# so it can reset them if the player backs out of it.
default collected_hp = {'good': [], 'bad': [], 'break': []}
# Total number of hg (hourglasses) earned per timeline item
default collected_hg = 0

# Keeps track of the ending the game should show the player
default ending = None

# These are primarily used when setting the nickname colour
# via $ nickColour = black or $ nickColour = white
define white = "#ffffff"
define black = "#000000"

image new_sign = "Bubble/main01_new.webp"

define _preferences.show_empty_window = False


##******************************
## Image Definitions - Menu
##******************************
image greeting_bubble = Frame("Menu Screens/Main Menu/greeting_bubble.webp", 40, 10, 10, 10)
image greeting_panel = Frame("Menu Screens/Main Menu/greeting_panel.webp", 20, 20)

image rfa_greet:
    Text("{k=-1}>>>>>>>{/k}  Welcome to Rika's Fundraising Association",
                color="#ffffff", size=30, slow=True,
                font=curlicue_font, slow_cps=8, bold=True)
    10.0
    "transparent"
    0.2
    repeat

# Background Menu Squares
image right_corner_menu = Frame("Menu Screens/Main Menu/right_corner_menu.webp", 45, 45)
image right_corner_menu_hover = Transform('right_corner_menu', alpha=0.5)
image left_corner_menu = Frame("Menu Screens/Main Menu/left_corner_menu.webp", 45, 45)
image left_corner_menu_hover = Transform('left_corner_menu', alpha=0.5)

# Menu Icons
image menu_after_ending = "Menu Screens/Main Menu/after_ending.webp"
image menu_dlc = "Menu Screens/Main Menu/dlc.webp"
image menu_history = "Menu Screens/Main Menu/history.webp"
image menu_save_load = "Menu Screens/Main Menu/save_load.webp"
image menu_original_story = "Menu Screens/Main Menu/original_story.webp"

# Settings panel
image menu_settings_panel = Frame("Menu Screens/Main Menu/settings_sound_panel.webp",60,200,60,120)
image menu_settings_panel_bright = Frame("Menu Screens/Main Menu/settings_sound_panel_bright.webp",60,200,60,120)
image menu_settings_panel_light = Frame("Menu Screens/Main Menu/settings_sound_panel_light.webp",60,200,60,120)
image menu_sound_sfx = "Menu Screens/Main Menu/settings_sound_sfx.webp"
image menu_other_box = Frame("Menu Screens/Main Menu/settings_sound_sfx.webp", 10, 10)
image menu_ringtone_box = Frame("Menu Screens/Main Menu/daychat01_3.webp", 35, 35)

# Settings tabs
image menu_tab_inactive = Frame("Menu Screens/Main Menu/settings_tab_inactive.webp",10,10)
image menu_tab_inactive_hover2 = Frame("Menu Screens/Main Menu/settings_tab_inactive_hover2.webp",10,10)
image menu_tab_active = Frame("Menu Screens/Main Menu/settings_tab_active.webp",25,25)
image menu_tab_inactive_hover = Frame("Menu Screens/Main Menu/settings_tab_inactive_hover.webp",10,10)

# Header Images
image header_plus = "Menu Screens/Main Menu/header_plus.webp"
image header_plus_hover = "Menu Screens/Main Menu/header_plus_hover.webp"
image header_tray = "Menu Screens/Main Menu/header_tray.webp"
image header_hg = "Menu Screens/Main Menu/header_hg.webp"
image header_heart = "Menu Screens/Main Menu/header_heart.webp"

# Profile Page
image menu_header = Frame("Menu Screens/Main Menu/menu_header.webp", 0, 50)
image menu_back = "Menu Screens/Main Menu/menu_back_btn.webp"
image save_btn = "Menu Screens/Main Menu/menu_save_btn.webp"
image load_btn = "Menu Screens/Main Menu/menu_load_btn.webp"
image name_line = "Menu Screens/Main Menu/menu_underline.webp"
image menu_edit = "Menu Screens/Main Menu/menu_pencil_long.webp"
image menu_pencil = "Menu Screens/Main Menu/menu_pencil.webp"

image radio_on = "Menu Screens/Main Menu/menu_radio_on.webp"
image radio_off = "Menu Screens/Main Menu/menu_radio_off.webp"

image settings_gear = "Menu Screens/Main Menu/menu_settings_gear.webp"

# Save/Load
image save_auto_idle = Frame("Menu Screens/Main Menu/save_auto_idle.webp", 20, 20)
image save_auto_hover = Frame("btn_hover:save_auto_idle", 20, 20)


# Just for fun, this is the animation when you hover over the settings
# button. It makes the gear look like it's turning.
image settings_gear_rotate:
    "Menu Screens/Main Menu/menu_settings_gear.webp"
    xpos -10
    ypos -10
    block:
        rotate 0
        linear 1.0 rotate 45
        repeat

# Other Settings
image menu_select_btn = Frame("Menu Screens/Main Menu/menu_select_button.webp",60, 80, 130, 60)
image menu_select_btn_hover = Transform('menu_select_btn', alpha=0.5)
image menu_select_btn_inactive = Frame("Menu Screens/Main Menu/menu_select_button_inactive.webp",60,60)
image menu_select_btn_clear = Frame("Menu Screens/Main Menu/menu_select_button_clear.webp",60, 80, 130, 60)


## ********************************
## Chat Home Screen
## ********************************
image gray_chatbtn = "Menu Screens/Chat Hub/main01_chatbtn.webp"
image gray_chatbtn_hover = "btn_hover:gray_chatbtn"
image rfa_chatcircle:
    "Menu Screens/Chat Hub/main01_chatcircle.webp"
    block:
        rotate 0
        alignaround(.5, .5)
        linear 13.0 rotate -360
        repeat
image blue_chatcircle:
    "Menu Screens/Chat Hub/main01_chatcircle_big.webp"
    block:
        rotate 60
        alignaround(.5, .5)
        linear 4 rotate 420
        repeat

image chat_icon = "Menu Screens/Chat Hub/main01_chaticon.webp"
image gray_mainbtn = "Menu Screens/Chat Hub/main01_mainbtn.webp"
image gray_mainbtn_hover = "btn_hover:gray_mainbtn"
image blue_mainbtn = "Menu Screens/Chat Hub/main01_mainbtn_lit.webp"
image blue_mainbtn_hover = 'btn_hover:blue_mainbtn'
image gray_maincircle:
    "Menu Screens/Chat Hub/main01_maincircle.webp"
    block:
        rotate -120
        alignaround(.5, .5)
        linear 4 rotate -480
        repeat
image blue_maincircle:
    "Menu Screens/Chat Hub/main01_maincircle_lit.webp"
    block:
        rotate 180
        alignaround(.5, .5)
        linear 4 rotate 540
        repeat
image call_mainicon = "Menu Screens/Chat Hub/main01_mainicon_call.webp"
image email_mainicon = "Menu Screens/Chat Hub/main01_mainicon_email.webp"
image msg_mainicon = "Menu Screens/Chat Hub/main01_mainicon_message.webp"

image profile_pic_select_square = Transform("Menu Screens/Chat Hub/profile_pic_select_square.webp", xysize=(95, 95))

image white_hex = "Menu Screens/Chat Hub/main01_subbtn.webp"
image blue_hex = "Menu Screens/Chat Hub/main01_subbtn_lit.webp"
image red_hex = "Menu Screens/Chat Hub/main01_subbtn_shop.webp"
image white_hex_hover = 'btn_hover:white_hex'
image blue_hex_hover = 'btn_hover:blue_hex'
image red_hex_hover = 'btn_hover:red_hex'

image album_icon = "Menu Screens/Chat Hub/main01_subicon_album.webp"
image guest_icon = "Menu Screens/Chat Hub/main01_subicon_guest.webp"

image loading_circle_stationary = "Menu Screens/Main Menu/loading_circle.webp"

## ********************************
## Profile Picture Screen
## ********************************
image profile_outline = Frame('#fff', 5, 5)
image profile_cover_photo = "Cover Photos/profile_cover_photo.webp"

image input_close_idle = "Menu Screens/Main Menu/main02_close_button.webp"
image input_close_hover = "Menu Screens/Main Menu/main02_close_button_hover.webp"
image input_square = Frame("Menu Screens/Main Menu/main02_text_input.webp",40,40)
image input_popup_bkgr = Frame("Menu Screens/Main Menu/menu_popup_bkgrd.webp",70,70)
image input_popup_bkgr_hover = Frame("Menu Screens/Main Menu/menu_popup_bkgrd_hover.webp",70,70)


## ********************************
## Text Message Screen
## ********************************
image new_text_envelope = 'Text Messages/main03_email_unread.webp'
image read_text_envelope = 'Text Messages/main03_email_read.webp'
image new_text = 'Text Messages/new_text.webp'
image header_envelope = 'Text Messages/header_envelope.webp'

image message_idle_bkgr = Frame('Text Messages/message_idle_background.webp',20,20,20,20)
image message_hover_bkgr = 'btn_hover:message_idle_bkgr'
image unread_message_idle_bkgr = Frame('Text Messages/message_idle_background_unread.webp',20,20,20,20)
image unread_message_hover_bkgr = 'btn_hover:unread_message_idle_bkgr'

image text_msg_line = Frame('Text Messages/msgsl_line.webp', 40,2)
image text_answer_active = 'Text Messages/msgsl_button_answer_active.webp'
image text_answer_inactive = 'Text Messages/msgsl_button_answer_inactive.webp'
image text_answer_text = 'Text Messages/msgsl_text_answer.webp'
image text_answer_animation:
    'Text Messages/answer_animation/1.webp'
    0.1
    'Text Messages/answer_animation/2.webp'
    0.1
    'Text Messages/answer_animation/3.webp'
    0.1
    'Text Messages/answer_animation/4.webp'
    0.1
    'Text Messages/answer_animation/5.webp'
    0.1
    'Text Messages/answer_animation/6.webp'
    0.1
    'Text Messages/answer_animation/7.webp'
    0.1
    'Text Messages/answer_animation/8.webp'
    0.1
    'Text Messages/answer_animation/9.webp'
    0.1
    'Text Messages/answer_animation/10.webp'
    0.1
    'Text Messages/answer_animation/11.webp'
    0.1
    'Text Messages/answer_animation/12.webp'
    0.1
    'Text Messages/answer_animation/13.webp'
    0.1
    'Text Messages/answer_animation/14.webp'
    0.1
    'Text Messages/answer_animation/15.webp'
    0.1
    'Text Messages/answer_animation/16.webp'
    0.1
    'Text Messages/answer_animation/17.webp'
    0.1
    repeat

image text_pause_button = 'Text Messages/msgsl_text_pause.webp'
image text_play_button = 'Text Messages/msgsl_text_play.webp'

image text_popup_bkgr = "Text Messages/msgsl_popup_edge.webp"
image text_popup_msg = Frame("Text Messages/msgsl_popup_text_bg.webp", 0,0)
image text_answer_idle = Frame("Text Messages/chat-bg02_2.webp", 100, 100)
image text_answer_hover = Frame("Text Messages/chat-bg02_3.webp", 100, 100)
image new_text_count = "Text Messages/new_msg_count.webp"

image mc_text_msg_bubble = Frame("Text Messages/msgsl_text_player.webp", 60,60,60,10)
image npc_text_msg_bubble = Frame("Text Messages/msgsl_text_npc.webp", 60,60,60,10)


## ********************************
## Chat Select Screen
## ********************************
image day_selected = Frame('Menu Screens/Day Select/daychat01_day_mint.webp', 50, 50)
image day_selected_hover = Frame('Menu Screens/Day Select/daychat01_day_mint_hover.webp', 50, 50)
image day_inactive = Frame('Menu Screens/Day Select/daychat01_day_inactive.webp', 50, 50)
image day_active = Frame('Menu Screens/Day Select/daychat01_day_active.webp', 50, 50)
image day_active_hover = Frame('Menu Screens/Day Select/daychat01_day_active_hover.webp', 50, 50)
image day_reg_hacked = 'Menu Screens/Day Select/chatlist_hacking.webp'
image day_reg_hacked_long = 'Menu Screens/Day Select/chatlist_hacking_long.webp'

image chat_hack_thin = 'Menu Screens/Day Select/chat_hacking_thin.webp'
image chat_hack_thick = 'Menu Screens/Day Select/chat_hacking_thick.webp'
image chat_hack_filled = 'Menu Screens/Day Select/chat_hacking_filled.webp'

image hacked_white_squares:

    block:
        choice:
            Transform('chat_hack_thin', yzoom=0.3, alpha=0.4, yoffset=800)
            pause 0.02
            Transform('chat_hack_thin', yzoom=0.3, alpha=0.0, yoffset=800)
            pause 0.02
        choice:
            Transform('chat_hack_thin', yzoom=0.3, alpha=0.4, yoffset=800)
            pause 0.02
            Transform('chat_hack_thin', yzoom=0.3, alpha=0.0, yoffset=800)
            pause 0.02
        choice:
            Transform('chat_hack_thin', yzoom=0.01, alpha=0.45, yoffset=720)
            pause 0.02
            Transform('chat_hack_thin', yzoom=1.0, alpha=0.95, yalign=0.6)
            pause 0.02
    block:
        choice:
            Transform('chat_hack_filled', yzoom=0.45, alpha=0.9, yalign=1.0)
            pause 0.02
            Transform('chat_hack_filled', yzoom=0.45, alpha=0.0, yalign=1.0)
            pause 0.03
        choice:
            Transform('chat_hack_thin', yzoom=1.0, alpha=0.95, yalign=0.6)
            pause 0.02
            Transform('chat_hack_filled', yzoom=0.3, alpha=0.8, yalign=1.0)
            pause 0.02
        choice:
            Transform('chat_hack_thick', yzoom=0.3, alpha=0.98, yalign=0.5)
            pause 0.02
            Transform('chat_hack_thick', yzoom=0.3, alpha=0.0, yalign=0.5)
            pause 0.04
    block:
        choice:
            Transform('chat_hack_thin', yzoom=1.0, alpha=0.95, yalign=0.6)
            pause 0.02
            Transform('chat_hack_filled', yzoom=0.4, alpha=0.8, yalign=0.85)
            pause 0.02
        choice:
            Transform('chat_hack_thin', yzoom=1.0, alpha=0.95, yalign=0.6)
            pause 0.02
            Transform('chat_hack_filled', yzoom=0.45, alpha=0.9, yalign=1.0)
            pause 0.02
        choice:
            Transform('chat_hack_filled', yzoom=0.45, alpha=0.0, yalign=1.0)
            pause 0.05
            Transform('chat_hack_thick', yzoom=0.3, alpha=0.98, yalign=0.5)
            pause 0.02
    block:
        choice:
            Transform('chat_hack_filled', yzoom=0.45, alpha=0.0, yalign=1.0)
            pause 0.1
            Transform('chat_hack_filled', yzoom=0.45, alpha=0.9, yalign=1.0)
            pause 0.02
        choice:
            Transform('chat_hack_thick', yzoom=0.3, alpha=0.98, yalign=0.5)
            pause 0.02
            Transform('chat_hack_thick', yzoom=0.1, alpha=0.7, yalign=0.6)
            pause 0.02
        choice:
            Transform('chat_hack_filled', yzoom=0.45, alpha=0.0, yalign=1.0)
            pause 0.05
            Transform('chat_hack_filled', yzoom=0.4, alpha=0.5, yalign=0.85)
            pause 0.02
    block:
        choice:
            Transform('chat_hack_filled', yzoom=0.45, alpha=0.0, yalign=1.0)
            pause 0.1
            Transform('chat_hack_filled', yzoom=0.45, alpha=0.9, yalign=1.0)
            pause 0.02
        choice:
            Transform('chat_hack_thick', yzoom=0.3, alpha=0.98, yalign=0.5)
            pause 0.02
            Transform('chat_hack_thick', yzoom=0.1, alpha=0.7, yalign=0.6)
            pause 0.02
        choice:
            Transform('chat_hack_filled', yzoom=0.45, alpha=0.0, yalign=1.0)
            pause 0.05
            Transform('chat_hack_filled', yzoom=0.4, alpha=0.5, yalign=0.85)
            pause 0.02
    block:
        choice:
            Transform('chat_hack_thin', yzoom=1.0, alpha=0.95, yalign=0.6)
            pause 0.02
            Transform('chat_hack_filled', yzoom=0.4, alpha=0.8, yalign=0.85)
            pause 0.02
        choice:
            Transform('chat_hack_thin', yzoom=1.0, alpha=0.95, yalign=0.6)
            pause 0.02
            Transform('chat_hack_filled', yzoom=0.45, alpha=0.9, yalign=1.0)
            pause 0.02
        choice:
            Transform('chat_hack_filled', yzoom=0.45, alpha=0.0, yalign=1.0)
            pause 0.05
            Transform('chat_hack_thick', yzoom=0.3, alpha=0.98, yalign=0.5)
            pause 0.02
    block:
        choice:
            Transform('chat_hack_thin', yzoom=0.3, alpha=0.4, yoffset=800)
            pause 0.02
            Transform('chat_hack_thin', yzoom=0.3, alpha=0.0, yoffset=800)
            pause 0.02
        choice:
            Transform('chat_hack_thin', yzoom=0.3, alpha=0.4, yoffset=800)
            pause 0.02
            Transform('chat_hack_thin', yzoom=0.3, alpha=0.0, yoffset=800)
            pause 0.02
        choice:
            Transform('chat_hack_thin', yzoom=0.01, alpha=0.45, yoffset=720)
            pause 0.02
            Transform('chat_hack_thin', yzoom=1.0, alpha=0.95, yalign=0.6)
            pause 0.02
    Transform('chat_hack_filled', yzoom=0.4, alpha=0.0, yalign=0.85)

image day_today:
    'Menu Screens/Day Select/daychat_today.webp'
    block:
        easein 0.5 yoffset -20
        easeout 0.5 yoffset 0
        repeat
image final_day = 'Menu Screens/Day Select/daychat_finalday.webp'
image day_percent = Frame('Menu Screens/Day Select/daychat_percent.webp', 15, 15)
image day_percent_bg = Frame('Menu Screens/Day Select/daychat_percent_bg.webp', 15, 15)
image day_percent_border = Frame('Menu Screens/Day Select/daychat_percent_border.webp', 15, 15)
image day_hlink = 'Menu Screens/Day Select/daychat_hlink.webp'
image plot_lock = 'Menu Screens/Day Select/plot_lock.webp'
image expired_chat = 'Menu Screens/Day Select/daychat_hg.webp'

image day_vlink = Tile('Menu Screens/Day Select/daychat_vlink.webp')
image vn_inactive = 'Menu Screens/Day Select/vn_inactive.webp'
image vn_selected = 'Menu Screens/Day Select/daychat01_vn_mint.webp'
image vn_active = 'Menu Screens/Day Select/vn_active.webp'
image vn_selected_hover = 'Menu Screens/Day Select/daychat01_vn_mint_hover.webp'
image vn_active_hover = 'Menu Screens/Day Select/vn_active_hover.webp'
image vn_inactive_hover = 'vn_inactive'
image vn_marker = 'Menu Screens/Day Select/daychat01_vn_marker.webp'
image vn_time_bg = 'Menu Screens/Day Select/daychat01_chat_timebg.webp'

image solo_vn_active = "Menu Screens/Day Select/solo_vn_active.webp"
image solo_vn_inactive = "Menu Screens/Day Select/solo_vn_inactive.webp"
image solo_vn_selected = "Menu Screens/Day Select/solo_vn_mint.webp"
image solo_vn_hover = "Menu Screens/Day Select/solo_vn_hover.webp"

image chat_active = Frame('Menu Screens/Day Select/daychat01_chat_active.webp',190, 70, 40, 50)
image chat_inactive = Frame('Menu Screens/Day Select/daychat01_chat_inactive.webp',190, 70, 40, 50)
image chat_continue = Frame('Menu Screens/Day Select/daychat01_chat_continue.webp',190, 70, 40, 20)
image chat_selected = Frame('Menu Screens/Day Select/daychat01_chat_mint.webp',190, 70, 40, 50)
image chat_timeline_hover = Frame('Menu Screens/Day Select/daychat01_chat_hover.webp', 190, 70, 40, 50)
image chat_secure_box = Frame('Menu Screens/Day Select/chatbox_secure_underlay.webp', 190, 70, 40, 50)
image chat_colorhack_box = Frame('Menu Screens/Day Select/chatbox_hacker_underlay.webp', 190, 70, 40, 50)

image story_call_active = Frame('Menu Screens/Day Select/story_call_active.webp', 290, 56, 40, 50)
image story_call_inactive = Frame('Menu Screens/Day Select/story_call_inactive.webp', 290, 56, 40, 50)
image story_call_selected = Frame('Menu Screens/Day Select/story_call_mint.webp', 290, 56, 40, 50)
image story_call_hover = Frame('Menu Screens/Day Select/story_call_hover.webp', 290, 56, 40, 50)
image story_call_history = 'Menu Screens/Day Select/story_call_history.webp'

## ********************************
## Phone Call Screen
## ********************************
image call_back = 'Phone Calls/call.webp'

image call_signal_sl:
    Transform('Phone Calls/call_ani_0.webp', xzoom=-1)
    block:
        alpha 0.0
        1.0
        alpha 0.8
        3.0
        repeat
image call_signal_ml:
    Transform('Phone Calls/call_ani_1.webp', xzoom=-1)
    block:
        alpha 0.0
        2.0
        alpha 0.8
        2.0
        repeat
image call_signal_ll:
    Transform('Phone Calls/call_ani_2.webp', xzoom=-1)
    block:
        alpha 0.0
        3.0
        alpha 0.8
        1.0
        repeat
image call_signal_sr:
    'Phone Calls/call_ani_0.webp'
    block:
        alpha 0.0
        1.0
        alpha 0.8
        3.0
        repeat
image call_signal_mr:
    'Phone Calls/call_ani_1.webp'
    block:
        alpha 0.0
        2.0
        alpha 0.8
        2.0
        repeat
image call_signal_lr:
    'Phone Calls/call_ani_2.webp'
    block:
        alpha 0.0
        3.0
        alpha 0.8
        1.0
        repeat

image call_overlay = Frame('Phone Calls/call_back_screen.webp', 0, 0)
image call_answer = 'Phone Calls/call_button_answer.webp'
image call_hang_up = 'Phone Calls/call_button_hang_up.webp'
image call_pause = 'Phone Calls/call_button_pause.webp'
image call_play = 'Phone Calls/call_button_play.webp'
image call_replay_active = 'Phone Calls/call_button_replay_active.webp'
image call_replay_inactive = 'Phone Calls/call_button_replay_inactive.webp'
image call_connect_triangle = 'Phone Calls/call_connect_waiting.webp'

image contact_icon = 'Phone Calls/call_icon_contacts.webp'
image call_headphones = 'Phone Calls/call_icon_earphone_en.webp'
image call_history_icon = 'Phone Calls/call_icon_history.webp'
image call_incoming = 'Phone Calls/call_icon_incoming.webp'
image call_missed = 'Phone Calls/call_icon_missed.webp'
image call_outgoing = 'Phone Calls/call_icon_outgoing.webp'
image call_voicemail = 'Phone Calls/call_icon_voicemail.webp'

image call_choice = Frame('Phone Calls/call_select_button.webp', 70, 70)
image call_choice_hover = Frame('Phone Calls/call_select_button_hover.webp', 90, 90)

image call_choice_check = Frame('Phone Calls/call_select_button_check.webp', 70, 70)
image call_choice_check_hover = Frame('Phone Calls/call_select_button_hover_check.webp', 90, 90)

## ********************************
## Email Screen
## ********************************
image email_completed_3 = "Email/main03_email_completed_01.webp"
image email_completed_2 = "Email/main03_completed_02.webp"
image email_completed_1 = "Email/main03_completed_03.webp"
image email_failed = "Email/main03_email_failed.webp"
image email_timeout = "Email/main03_email_timeout.webp"
image email_good = "Email/main03_email_good.webp"
image email_bad = "Email/main03_email_bad.webp"
image email_inactive = "Email/main03_email_inactive.webp"
image email_panel = "Email/main03_email_panel.webp"
image email_read = "Email/main03_email_read.webp"
image email_replied = "Email/main03_email_replied.webp"
image email_unread = "Email/main03_email_unread.webp"
image email_next = "Email/main03_email_next_button.webp"
image email_mint = "Email/main03_email_mint.webp"
image white_transparent = Frame("Email/white_transparent.webp", 0, 0)
image email_open_transparent = Frame("Email/email_open_transparent.webp", 0, 0)
image left_corner_menu_dark = Frame("Email/left_corner_menu_dark.webp", 45, 45)

## *******************************
## Tutorial Images
## *******************************
image tut_arrow:
    'Menu Screens/Tutorial/tut_arrow.webp'
    block:
        easein 0.5 xoffset 20
        easeout 0.5 xoffset 0
        repeat
image tut_arrow_vert:
    'Menu Screens/Tutorial/tut_arrow.webp'
    block:
        easein 0.5 yoffset 20
        easeout 0.5 yoffset 0
        repeat
image tut_dev_options = "Menu Screens/Tutorial/tut_dev_options.webp"
image tut_hacking = "Menu Screens/Tutorial/tut_hacking.webp"
image tut_other_pfp1 = "Menu Screens/Tutorial/tut_other_pfp1.webp"
image tut_other_pfp2 = "Menu Screens/Tutorial/tut_other_pfp2.webp"
image tut_other_pfp3 = "Menu Screens/Tutorial/tut_other_pfp3.webp"
image tut_player_pfp = "Menu Screens/Tutorial/tut_player_pfp.webp"
image tut_player_pfp2 = "Menu Screens/Tutorial/tut_player_pfp2.webp"
image tut_real_time = "Menu Screens/Tutorial/tut_real_time.webp"
image tut_skip_to_end = "Menu Screens/Tutorial/tut_skip_to_end.webp"
image tut_prefs = "Menu Screens/Tutorial/tut_prefs.webp"
