# ######################################################
# This file contains many of the primary menu screens
# used throughout the game. It's organized as follows:
#   python definitions:
#       class NameInput(InputValue)
#       def has_alpha(mystring)
#       def has_valid_chars(mystring)
#       def chat_greet()
#       def set_name_pfp()
#   screen main_menu()
#       screen route_select_screen()
#   screen save/load
#       screen file_slots(title)
#   screen menu_header(title, return_action, envelope)
#   screen chat_home(reshow)
#       screen links()
#       screen developer_settings()
#       screen chara_profile(who)
#       screen pick_chara_pfp(who)
#   def is_unlocked_pfp(img, condition, pfp_list=None)
# ######################################################


init python:

    import time

    class NameInput(InputValue):
        """Retrieve the player's name from input."""

        def __init__(self):
            self.the_name = "Rainbow"

        def get_text(self):
            global persistent
            return persistent.name

        def set_text(self, s):
            s = s.strip()
            self.the_name = s
            global name, persistent
            # Ensure the given name is valid
            if (len(s) < 2
                    or not has_alpha(s)
                    or not has_valid_chars(s)):
                # renpy.show_screen('notify',
                #     message=("Names must be between 2 and 20 characters long"
                #     + " and can only contain alphabet characters, dashes,"
                #     + " spaces, and apostrophes."))
                pass
            else:
                persistent.name = self.the_name
                renpy.save_persistent()
                name = persistent.name
                renpy.retain_after_load()

        def enter(self):
            global name, persistent
            if (len(self.the_name) < 2
                    or not has_alpha(self.the_name)
                    or not has_valid_chars(self.the_name)):
                renpy.show_screen('notify',
                    message=("Names must be between 2 and 20 characters long"
                    + " and can only contain alphabet characters, dashes,"
                    + " spaces, and apostrophes."))
            else:
                persistent.name = self.the_name
                renpy.save_persistent()
                name = persistent.name
                renpy.retain_after_load()
                renpy.hide_screen('input_popup')
            # renpy.run(self.Disable())
            # raise renpy.IgnoreEvent()

    def has_alpha(mystring):
        """Check if the given string has at least one alphabet character."""
        for c in "aeiouyAEIOUYbcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ":
            if c in mystring:
                return True
        return False

    def has_valid_chars(mystring):
        """
        Check if the given string includes only valid alphabet characters.
        Also includes spaces, dashes, and apostrophes.
        """

        for c in mystring:
            if c not in " -'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                return False
        return True

    def chat_greet():
        """
        Pick a greeting depending on the time of day and play it.
        Makes use of a DayGreeting class to find sound clips and
        corresponding translations.
        """
        global greet_text_english, greet_text_korean
        global greet_char, greet_list
        greet_char = renpy.random.choice(greet_list)

        # Test that this character is indeed in the greetings lists
        while greet_list:
            try:
                morning_greeting[greet_char]
                afternoon_greeting[greet_char]
                evening_greeting[greet_char]
                night_greeting[greet_char]
                late_night_greeting[greet_char]
                break
            except KeyError:
                # This means the character doesn't have a greeting available
                print("WARNING: Character", greet_char,
                    "does not have greetings, but is included in greet_list.")
                renpy.show_screen('notify',
                    "WARNING: Character " + greet_char + " does not have "
                    + "greetings, but is included in greet_list.")
                greet_list.remove(greet_char)
                greet_char = renpy.random.choice(greet_list)


        hour = int(time.strftime('%H', time.localtime()))

        if hour >= 6 and hour < 12:  # morning
            num_greetings = len(morning_greeting[greet_char])
            the_greeting = renpy.random.randint(1, num_greetings) - 1

            greet_text_english = ("Good morning! "
                + morning_greeting[greet_char][the_greeting].english)
            greet_text_korean = morning_greeting[greet_char][the_greeting].korean
            renpy.play(morning_greeting[greet_char][the_greeting].sound_file,
                channel="voice_sfx")

        elif hour >=12 and hour < 18:    # afternoon
            num_greetings = len(afternoon_greeting[greet_char])
            the_greeting = renpy.random.randint(1, num_greetings) - 1

            greet_text_english = ("Good afternoon! "
                + afternoon_greeting[greet_char][the_greeting].english)
            greet_text_korean = afternoon_greeting[greet_char][the_greeting].korean
            renpy.play(afternoon_greeting[greet_char][the_greeting].sound_file,
                channel="voice_sfx")

        elif hour >= 18 and hour < 22:  # evening
            num_greetings = len(evening_greeting[greet_char])
            the_greeting = renpy.random.randint(1, num_greetings) - 1

            greet_text_english = ("Good evening! "
                + evening_greeting[greet_char][the_greeting].english)
            greet_text_korean = evening_greeting[greet_char][the_greeting].korean
            renpy.play(evening_greeting[greet_char][the_greeting].sound_file,
                channel="voice_sfx")

        elif hour >= 22 or hour < 2: # night
            num_greetings = len(night_greeting[greet_char])
            the_greeting = renpy.random.randint(1, num_greetings) - 1

            greet_text_english = ("It's getting late! "
                + night_greeting[greet_char][the_greeting].english)
            greet_text_korean = night_greeting[greet_char][the_greeting].korean
            renpy.play(night_greeting[greet_char][the_greeting].sound_file,
                channel="voice_sfx")

        else:   # late night/early morning
            num_greetings = len(late_night_greeting[greet_char])
            the_greeting = renpy.random.randint(1, num_greetings) - 1

            greet_text_english = ("You're up late! "
                + late_night_greeting[greet_char][the_greeting].english)
            greet_text_korean = late_night_greeting[greet_char][the_greeting].korean
            renpy.play(late_night_greeting[greet_char][
                            the_greeting].sound_file, channel="voice_sfx")



    def set_name_pfp():
        """Ensure the player's name and profile picture are set correctly."""

        global name, persistent
        name = persistent.name
        # if m.prof_pic != persistent.MC_pic and isImg(persistent.MC_pic):
        #     m.prof_pic = persistent.MC_pic
        # else:
        #     m.prof_pic = 'Profile Pics/MC/MC-1.webp'
        # if m.name != persistent.name:
        #     m.name = persistent.name
        renpy.retain_after_load()
        return



## Variable to help determine when there should be Honey Buddha
## Chips available
default hbc_bag = RandomBag([ False, False, False,
                              False, False, True, True ])


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
## Also shows a greeting from a random character
##

screen main_menu():

    tag menu

    if persistent.first_boot:
        on 'show' action [SetField(persistent, 'first_boot', False),
                            Show('route_select_screen')]
        on 'replace' action [SetField(persistent, 'first_boot', False),
                            Show('route_select_screen')]
    else:
        # Greet the player, and play the title music if not already
        on 'show' action If(renpy.music.get_playing(channel='music')
                            != mystic_chat,
                            [Queue('music', mystic_chat),
                            Function(chat_greet)],
                            Function(chat_greet))
        on 'replace' action If(renpy.music.get_playing(channel='music')
                            != mystic_chat,
                            [Queue('music', mystic_chat),
                            Function(chat_greet)],
                            Function(chat_greet))

    # This adds the 'starry night' background with a few animated stars
    # It is defined in 'screens_starry_night.rpy'
    use starry_night()

    # Welcome to Rika's Fundraising Association message
    add "rfa_greet" yalign 0.02 xalign 0.25


    # Box that adds the characters' greeting messages
    frame:
        xysize(670,140)
        yalign 0.105
        xalign 0.5
        background Transform("greeting_panel", alpha=0.7)
        has hbox
        frame:
            xysize(143,127)
            add 'greet ' + greet_char align (0.5, 0.5)
        frame:
            xysize(500,120)
            background "greeting_bubble" padding (35, 5, 10, 5)
            has vbox
            text "[greet_text_korean]" style "greet_text" size 25
            text "[greet_text_english]" style "greet_text"

    # The main menu buttons. Note that some currently don't take
    # you to the screen you'd want as those features have yet to
    # be added (or are irrelevant)
    frame:
        xysize(655, 625)
        xalign 0.5
        yalign 0.61
        has vbox
        spacing 15
        hbox:
            spacing 15
            # Original Story
            # Top left
            button:
                xysize(430,400)
                style_prefix 'left_menu'
                if persistent.on_route:
                    # This is the auto save that gets loaded every
                    # time you load the game
                    action [SetField(persistent, 'load_instr', 'Auto'),
                            SetField(persistent, 'just_loaded', True),
                            FileLoad(mm_auto)]
                else:
                    # Note: this screen only has a placeholder
                    # but can easily be customized (see below)
                    action Show('route_select_screen')

                vbox:
                    add "menu_original_story" xpos 20
                    text "Original\nStory"

            vbox:
                spacing 15
                # Save and Load
                # Top Right
                button:
                    xysize(205, 195)
                    style_prefix 'right_menu'
                    action [Hide('load'), Show("load")]
                    vbox:
                        add "menu_save_load" xpos 25
                        text "Save & Load"

                # After Ending
                # Mid Right
                button:
                    xysize(205, 195)
                    style_prefix 'right_menu'
                    action [Hide('preferences'), Show('preferences')]
                    vbox:
                        add "menu_after_ending" align (0.5, 0.5)
                        text "Settings"
        hbox:
            spacing 15
            # History
            # Bottom Left
            button:
                xysize(430,195)
                style_prefix 'left_menu'
                action Show('select_history', Dissolve(0.5))
                vbox:
                    add "menu_history" align (0.5, 0.5)
                    text "History"


            # DLC
            # Bottom Right
            button:
                xysize (205,195)
                style_prefix 'right_menu'
                action Show('developer_settings')
                vbox:
                    add "menu_dlc" align (0.5, 0.5)
                    text "Developer"

style greet_text is text:
    color "#ffffff"
    size 27
    text_align 0.0
    slow_cps 20
    font curlicue_font

style left_menu_button:
    focus_mask True
    padding (10, 10)
    background 'left_corner_menu'
    hover_foreground 'left_corner_menu_hover'
    activate_sound 'audio/sfx/UI/select_4.mp3'

style left_menu_vbox:
    is default
    spacing 8
    align (0.5, 0.5)

style left_menu_text:
    is menu_text_big


style right_menu_button:
    is left_menu_button
    background 'right_corner_menu'
    hover_foreground 'right_corner_menu_hover'

style right_menu_vbox is left_menu_vbox

style right_menu_text:
    is menu_text_small

style menu_top_left_frame:
    maximum(450,420)
    padding (10, 10)
    xfill True
    yfill True

style menu_right_frame:
    maximum(225, 210)
    xfill True
    yfill True
    padding (10, 10)

style menu_bottom_left_frame:
    maximum(450,210)
    padding (10, 10)
    xfill True
    yfill True

style menu_text_big is text:
    color "#ffffff"
    size 45
    text_align 0.5
    xalign 0.5

style menu_text_small is text:
    color "#ffffff"
    size 30
    text_align 0.5
    xalign 0.5


## A short screen where the player selects which route they would
## like to start on. Can be customized to lead the player to a route
## to select, but as of now simply starts the game
screen route_select_screen():
    tag menu
    use menu_header("Mode Select", Show('main_menu', Dissolve(0.5))):
        frame:
            xysize (720, 1170)
            yalign 1.0
            xalign 0.5
            if persistent.custom_route_select:
                use custom_route_select_screen
            else:
                vbox:
                    style_prefix 'route_select'
                    button:
                        ysize 210
                        add 'Menu Screens/Main Menu/route_select_tutorial.webp':
                            align (0.08, 0.5)
                        action Start()
                        frame:
                            text "Tutorial Day"
                    # Casual/Jaehee's route is only available to a player who
                    # has completed Tutorial Day
                    button:
                        add 'Menu Screens/Main Menu/route_select_casual.webp':
                            align (0.08, 0.5)
                        frame:
                            if completed_branches(tutorial_route) == 0:
                                hbox:
                                    align (0.4, 0.5)
                                    add 'plot_lock' align (0.5, 0.5)
                                    text "Casual Story"
                            else:
                                text "Casual Story"
                        if completed_branches(tutorial_route) > 0:
                            action Start('example_casual_start')
                        else:
                            action CConfirm("This route is locked until you've played through Tutorial Day at least once.")
                            hover_foreground None

style route_select_frame:
    background 'Menu Screens/Main Menu/route_select.webp'
    xysize (235, 157)
    align (0.9, 0.5)
    padding (20, 15, 30, 15)

style route_select_text:
    align (0.5, 0.5)
    color "#fff"
    layout "subtitle"
    text_align 0.5
    size 36

style route_select_vbox:
    xsize 700
    align (0.5, 0.5)
    spacing 30

style route_select_button:
    is right_menu_button
    ymaximum 320
    xsize 700
    padding (15, 20)
    align (0.5, 0.5)

## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##

screen save():

    tag save_load
    modal True

    default current_page = 0
    default num_pages = 5
    default slots_per_column = 7
    default begin_page = 0

    use menu_header("Save", Hide('save', Dissolve(0.5))):
        use file_slots(_("Save"), current_page, num_pages, slots_per_column,
            begin_page)

screen load():

    tag save_load
    modal True

    default current_page = 0
    default num_pages = 5
    default slots_per_column = 7
    default begin_page = 0

    use menu_header("Load", Hide('load', Dissolve(0.5))):
        use file_slots(_("Load"), current_page, num_pages, slots_per_column,
            begin_page)

screen file_slots(title, current_page=0, num_pages=5, slots_per_column=7,
        begin_page=0):

    python:
        # Retrieve the name and day of the most recently completed
        # chatroom for the save file name
        if (most_recent_item is None
                and story_archive
                and story_archive[0].archive_list):
            most_recent_item = story_archive[0].archive_list[0]
        elif most_recent_item is None:
            most_recent_item = ChatRoom('Example Chatroom',
                                            'example_chat', '00:01')

        # Determine the beginning/end values
        if current_page == 0:
            begin_range = 0
            end_range = slots_per_column - 1
        else:
            begin_range = (current_page*slots_per_column)-1
            end_range = (current_page*slots_per_column)+slots_per_column-1

        end_page = begin_page + num_pages


    fixed:
        # This ensures the input will get the enter event before any of the
        # buttons do.
        order_reverse True

        # Contains the save slots.
        vpgrid id 'save_load_vp':
            style_prefix "save_load"
            cols gui.file_slot_cols
            rows slots_per_column

            # This adds the 'backup' save slot to the top when loading
            if title == "Load" and FileLoadable(mm_auto) and current_page == 0:
                if '|' in FileSaveName(mm_auto):
                    $ info = FileSaveName(mm_auto).split('|')
                    $ rt = info[0]
                    $ dn = info[1]
                    $ cn = info[2]
                    if len(info) > 3:
                        $ dn2 = info[3]
                    else:
                        $ dn2 = dn
                    if len(info) > 4:
                        $ day_suffix = info[4]
                    else:
                        $ day_suffix = " DAY"
                else:
                    $ rt, dn, cn, dn2 = 'auto', '1st', 'Example Chatroom', '2nd'
                    $ day_suffix = " DAY"

                button:
                    background 'save_auto_idle'
                    hover_background 'save_auto_hover'
                    action If(persistent.real_time,
                                [SetField(persistent, 'on_route', True),
                                SetField(persistent, 'load_instr', 'Auto'),
                                SetField(persistent, 'just_loaded', True),
                                FileAction(mm_auto),
                                renpy.restart_interaction],

                                [SetField(persistent, 'on_route', True),
                                SetField(persistent, 'just_loaded', True),
                                FileAction(mm_auto),
                                renpy.restart_interaction])
                    hbox:
                        fixed:
                            add 'save_auto' align (0.5, 0.5)
                        frame:
                            style_prefix 'save_desc'

                            has vbox
                            fixed:
                                text ("This is a backup file that"
                                        + " is auto-generated")
                            text "Today: [dn]" + day_suffix yalign 1.0

                        frame:
                            style_prefix 'save_stamp'
                            has vbox
                            fixed:
                                text FileTime(mm_auto,
                                    format=_("{#file_time}%m/%d %H:%M"),
                                    empty=_("empty slot"))
                            fixed:
                                null
                                # Can't delete this file
            elif current_page == 0:
                yoffset 71

            ## This displays all the regular save slots
            #for i in range(gui.file_slot_cols * gui.file_slot_rows):
            for i in range(begin_range, end_range):

                python:
                    slot = i + 1
                    if '|' in FileSaveName(slot):
                        info = FileSaveName(slot).split('|')
                        rt = info[0]
                        dn = info[1]
                        cn = info[2]
                        if len(info) > 3:
                            dn2 = info[3]
                        else:
                            dn2 = dn
                        if len(info) > 4:
                            day_suffix = info[4]
                        else:
                            day_suffix = " DAY"
                    else:
                        rt, dn, cn, dn2 = 'auto', '1st', 'Example', '2nd'
                        day_suffix = " DAY"

                    file_time = FileTime(slot, empty="00:00")[-5:]


                button:
                    if title == "Save":
                        action [SetVariable('save_name', get_save_title()),
                                FileAction(slot),
                                renpy.restart_interaction]
                    else: # title == "Load"
                        action [Function(load_action, the_day=dn, next_day=dn2,
                                file_time=FileTime(slot, empty="00:00"),
                                slot=slot)]

                    hbox:
                        fixed:
                            # Adds the correct save image to the left
                            if FileLoadable(slot):
                                add 'save_' + rt align (0.5, 0.5)
                            else:
                                add 'save_empty' align (0.5, 0.5)

                        frame:
                            style_prefix 'save_desc'
                            has vbox
                            # Displays the most recent chatroom title + day
                            if FileLoadable(slot):
                                fixed:
                                    text "[cn]"
                                text "Today: [dn]" + day_suffix yalign 1.0
                            else:
                                fixed:
                                    text "Empty Slot"
                                text "Tap an empty slot to save" yalign 1.0

                        frame:
                            style_prefix 'save_stamp'
                            has vbox
                            # Displays the time the save was created
                            # and the delete button
                            fixed:
                                text FileTime(slot,
                                        format=_("{#file_time}%m/%d %H:%M"),
                                        empty=_("empty slot"))
                            fixed:
                                imagebutton:
                                    hover Transform('save_trash',zoom=1.05)
                                    idle 'save_trash'
                                    xalign 1.0
                                    action FileDelete(slot)

                    key "save_delete" action FileDelete(slot)

        hbox:
            style_prefix 'email_hub'
            spacing 18
            if begin_page >= 5:
                imagebutton:
                    idle Transform("email_next", xzoom=-1, zoom=1.5)
                    align (0.5, 0.5)
                    action [SetScreenVariable('begin_page', begin_page-5)]
                    activate_sound 'audio/sfx/UI/email_next_arrow.mp3'

            for index in range(begin_page, end_page):
                $ zoomval = 0.7
                textbutton _(str(index+1)):
                    xysize (int(130*zoomval), int(149*zoomval))
                    background Transform('white_hex', zoom=zoomval)
                    hover_background Transform('white_hex_hover', zoom=zoomval)
                    selected_background Transform('blue_hex', zoom=zoomval)
                    text_size 38
                    text_align (0.5, 0.5)
                    action [SetScreenVariable('current_page', index)]
            # Currently there are 10 pages.
            if begin_page < 5:
                imagebutton:
                    idle Transform("email_next", zoom=1.5)
                    align (0.5, 0.5)
                    action [SetScreenVariable('begin_page', begin_page+5)]
                    activate_sound 'audio/sfx/UI/email_next_arrow.mp3'

init python:

    def get_save_title():
        """Get the save title based on today's information."""

        global most_recent_item

        if most_recent_item and most_recent_item.parent:
            save_title_item = most_recent_item.parent
        else:
            save_title_item = most_recent_item
        # Find today
        today = "1st"
        tomorrow = "2nd"
        day_suffix = " DAY"
        for day_num, day in enumerate(store.story_archive):
            if save_title_item in day.archive_list:
                today = day.day
                try:
                    if day.exclude_suffix:
                        day_suffix = ""
                except AttributeError:
                    pass
                if day_num+1 < len(store.story_archive):
                    tomorrow = store.story_archive[day_num+1].day
                else:
                    tomorrow = today
                break

        the_title = (save_title_item.save_img + "|" + today + "|"
                + save_title_item.title + "|" + tomorrow)
        if day_suffix:
            the_title += "|" + day_suffix
        return the_title



    def load_action(the_day, next_day, file_time, slot):

        file_time = file_time[-5:]
        file_hour = file_time[:2]
        file_min = file_time[-2:]
        current_time = upTime()
        current_hour = current_time.military_hour
        current_min = current_time.minute

        load_next_day = False

        # Compare file times to now
        # E.g. if the game was saved at 20:30, if now is 20:29
        # or earlier, it should load the next day
        if (is_time_later(current_hour, current_min, file_hour, file_min)):
            load_next_day = True
            if the_day == next_day:
                next_day = "NEXT"
            load_msg = ("There is a difference between the save time and "
                + "the present time. It may cause missed conversations or "
                + "phone calls during the time gap. Would you like to "
                + "continue?\n\nSave Time: " + the_day + " DAY "
                + file_time + "\n\nLoad Time: " + next_day + " DAY "
                + current_hour + ":" + current_min)
        else:
            load_msg = ("There is a difference between the save time and "
                + "the present time. It may cause missed conversations or "
                + "phone calls during the time gap. Would you like to "
                + "continue?\n\nSave Time: " + the_day + " DAY "
                + file_time + "\n\nLoad Time: " + the_day + " DAY "
                + current_hour + ":" + current_min)

        if store.persistent.real_time:
            if load_next_day:
                load_var = '+1 day'
                print_file("LOAD INSTR: Advance day +1")
            else:
                print_file("LOAD INSTR: Same day")
                load_var = 'Same day'
            renpy.show_screen('confirm', message=load_msg,
                yes_action=[SetField(persistent, 'just_loaded', True),
                    SetField(persistent, 'on_route', True),
                    SetField(persistent, 'load_instr', load_var),
                    FileLoad(slot)],
                no_action=Hide('confirm'))
            return

        # Otherwise, it's not in real-time mode
        store.persistent.on_route = True
        store.persistent.just_loaded = True
        renpy.run(FileLoad(slot))

    class AutoSave(FileSave):
        """
        Custom action which will automatically save the game to the Auto
        save file slot and update the save name accordingly.
        """

        def __init__(self, name="mm_auto_save", confirm=False, newest=True,
                page=None, cycle=False, slot=False):

            super(AutoSave, self).__init__(name, confirm, newest,
                page, cycle, slot)

        def __call__(self):
            store.save_name = get_save_title()
            super(AutoSave, self).__call__()
            renpy.retain_after_load()




style save_load_vpgrid:
    is slot_vpgrid
    yalign 1.0

style save_load_side:
    spacing 12
    align (1.0, 1.0)

style save_load_button:
    is slot_button

style save_load_fixed:
    align (0.5, 0.5)
    xysize(120, 120)

style save_desc_frame:
    is slot_frame
    xysize (400, 120)
    yalign 0.0

style save_desc_vbox:
    is slot_vbox
    spacing 8

style save_desc_fixed:
    is slot_fixed
    ysize 75

style save_desc_text:
    is save_slot_text
    yalign 0.0

style save_stamp_frame:
    is slot_frame
    xysize (155,120)

style save_stamp_vbox:
    is slot_vbox
    spacing 30

style save_stamp_fixed:
    is slot_fixed
    xsize 155
    yfit True

style save_stamp_text:
    size 25
    color "#fff"
    text_align 1.0
    xalign 1.0

style save_slot_text:
    color "fff"
    text_align 0.0

style vscroll_bar:
    base_bar Frame('gui/scrollbar/vertical_hover_bar.png',0,0)
    xsize 110
    thumb 'gui/scrollbar/vertical_hover_thumb.png'

########################################################
## Just the header that often shows up over menu items;
## put in a separate screen for less repeating code
########################################################

default my_menu_clock = Clock()

screen menu_header(title, return_action=NullAction,
                    envelope=False, hide_bkgr=False):

    python:
        # Ensures the background music is playing
        if title != "In Call":
            if (renpy.music.get_playing(channel='music') != mystic_chat
                    and not hacked_effect):
                renpy.music.queue(mystic_chat, loop=True)
            elif (hacked_effect and renpy.music.get_playing(channel='music')
                    == mystic_chat):
                renpy.music.play(mystic_chat_hacked, loop=True)
            elif (hacked_effect
                    and renpy.music.get_playing(channel='music')
                        != mystic_chat_hacked):
                renpy.music.queue(mystic_chat_hacked, loop=True)

    if not hide_bkgr:
        use starry_night()


    # If the game loaded and isn't showing the chat hub, jump there
    if persistent.just_loaded and renpy.get_screen('chat_home') is None:
        on 'show' action [SetField(persistent, 'just_loaded', False),
                            Show('chat_home')]
        on 'replace' action [SetField(persistent, 'just_loaded', False),
                            Show('chat_home')]
    # # If the game is running on real-time, check once a minute
    # # if it's time for the next chatroom
    if persistent.real_time and not main_menu and not starter_story:
        timer 60 action Function(check_and_unlock_story) repeat True
        on 'show' action Function(check_and_unlock_story)
        on 'replace' action Function(check_and_unlock_story)

    if (not renpy.get_screen('text_message_screen')
            and not main_menu
            and not starter_story
            and num_undelivered()):
        #timer 0.5 action If(not randint(0,3), Function(deliver_next), []) repeat True
        timer 1.5 action Function(deliver_next, randomize=True) repeat True

    hbox:
        style_prefix "hg_hp"
        add my_menu_clock xalign 0.0 yalign 0.0 xpos -5

        fixed:
            if not persistent.first_boot:
                hbox:
                    style_prefix 'header_hg'
                    frame:
                        has hbox
                        xalign 1.0
                        add 'header_hg' yalign 1.0
                        frame:
                            style_prefix 'hg_hp_display'
                            text str(persistent.HG)
                    imagebutton:
                        idle "header_plus"
                        hover "header_plus_hover"
                        action CConfirm(("There are no in-game "
                            + "purchases in this application. However, if "
                            + "you'd like to support its development, you can "),
                            #+ "{a=https://ko-fi.com/somniarre}check out my Ko-Fi here.{/a}",
                            show_link=True)
                        #if not renpy.get_screen("choice"):
                        #    action NullAction
                    frame:
                        has hbox
                        xalign 1.0
                        add "header_heart" yalign 1.0
                        frame:
                            style_prefix 'hg_hp_display'
                            text str(persistent.HP)

        # Settings gear
        if not persistent.first_boot and title != "Settings":
            imagebutton:
                xysize (72, 72)
                idle "settings_gear"
                hover "settings_gear_rotate"
                focus_mask None
                # Eventually I'd like to get the settings button
                # working during phone calls, but there are too
                # many bugs so it's commented out
                # if renpy.get_screen("in_call") and not renpy.get_screen("choice"):
                #     action [Preference("auto-forward", "disable"), Show("preferences")]
                if (not renpy.get_screen("choice")
                        and not renpy.get_screen("in_call")
                        and not text_person):
                    if renpy.get_screen('settings_screen'):
                        action [Hide('preferences'),
                                Hide('profile_pic'),
                                Hide('other_settings'),
                                ShowMenu('preferences')]
                    else:
                        action ShowMenu("preferences")
                else:
                    action Function(print, "Settings won't work because: choice? ",
                        renpy.get_screen("choice"), " in_call? ", renpy.get_screen("in_call"),
                        " text person? ", text_person)
        else:
            null width 72

    # Header
    if title != "Original Story" and title != "In Call":
        frame:
            ysize 80
            yalign 0.058
            add "menu_header"

        if not envelope:
            text title:
                color "#ffffff"
                size 40
                xalign 0.5 yalign 0.072
                text_align 0.5
        else:
            hbox:
                xalign 0.5
                yalign 0.072
                spacing 15
                add 'header_envelope' xalign 0.5 yalign 0.5
                text title color "#ffffff" size 40 text_align 0.5



    if not persistent.first_boot:
        if title != "Original Story" and title != "In Call":
            # Back button
            imagebutton:
                xalign 0.013
                yalign 0.068
                idle "menu_back"
                focus_mask None
                hover Transform("menu_back", zoom=1.1)
                activate_sound 'audio/sfx/UI/back_button.mp3'
                if not renpy.get_screen("choice"):
                    if persistent.first_boot or not persistent.on_route:
                        action [SetField(persistent, 'first_boot', False),
                                return_action]
                    elif (envelope and (not text_person
                            or not text_person.real_time_text)):
                        action Show('text_message_hub', Dissolve(0.5))
                    # If the player is texting in real time, leaving
                    # text messages works differently
                    elif (text_person and text_person.real_time_text
                            and renpy.get_screen('text_message_screen')
                            and len(renpy.get_return_stack()) > 0):
                        action CConfirm(("Do you really want to leave this"
                                    + " text message? You won't be able to"
                                    + " continue this conversation."),
                                    [Jump('leave_inst_text')])
                    else:
                        action If(_menu and not main_menu,
                            Return(), return_action)


    if title == "Save" or title == "Load" or title == "Mode Select":
        transclude
    else:
        frame:
            if title != "Original Story" and title != "In Call":
                xysize (750, 1180)
            else:
                xysize (750, 1180+80)
            yalign 1.0
            has vbox
            align (0.5, 0.0)
            spacing 10
            transclude

style hg_hp_hbox:
    spacing -52
    yalign 0.01

style hg_hp_fixed:
    xysize(600, 80)

style header_hg_hbox:
    xalign 0.5

style header_hg_frame:
    background 'header_tray'
    padding (20,0,0,5)
    xysize (205,51)

style hg_hp_display_frame:
    xysize(205-75, 42)

style hg_heart_points:
    color "#ffffff"
    font gui.sans_serif_1
    size 39
    text_align 1.0

style hg_hp_display_text:
    is hg_heart_points
    text_align 1.0
    xalign 1.0

########################################################
## The 'homepage' from which you interact with the game
## after the main menu
########################################################

default chips_available = False
default spaceship_xalign = 0.04
default reset_spaceship_pos = False

image github = "Menu Screens/Chat Hub/github.webp"
image discord = "Menu Screens/Chat Hub/discord.webp"
image kofi = "Menu Screens/Chat Hub/ko-fi.webp"
## Icon made by Freepik from www.flaticon.com
image developer_settings = "Menu Screens/Chat Hub/global-settings-freepik-red.webp"
## Icon made by Creaticca Creative Agency from www.flaticon.com
image link_hex = "Menu Screens/Chat Hub/link-creaticca-creative-agency.webp"
## Icon made by Pixel perfect from www.flaticon.com
image exit_hex = "Menu Screens/Chat Hub/exit-pixel-perfect.webp"


image new_profile_update = Frame("Menu Screens/Chat Hub/main_profile_new_update.webp", 0, 0)
image no_profile_update = Frame("Menu Screens/Chat Hub/main_profile_normal.webp", 0, 0)

screen chat_home(reshow=False):

    tag menu
    modal True

    # Every time you go back to this screen, the game will auto-save
    on 'show':
        action If(renpy.get_screen('chip_tap')
                    or renpy.get_screen('chip_cloud')
                    or renpy.get_screen('chip_end'),
                SetField(persistent, 'just_loaded', False),
                [SetField(persistent, 'just_loaded', False),
                SetVariable('text_person', None),
                Hide('chip_end'), renpy.retain_after_load,
                AutoSave()])

    on 'replace':
        action If(renpy.get_screen('chip_tap')
                    or renpy.get_screen('chip_cloud')
                    or renpy.get_screen('chip_end'),
                SetField(persistent, 'just_loaded', False),
                [SetField(persistent, 'just_loaded', False),
                SetVariable('text_person', None),
                Hide('chip_end'), renpy.retain_after_load,
                AutoSave()])

    use menu_header("Original Story"):
        # Note that only characters in the list 'character_list' will
        # show up here as profile pictures
        python:
            if m in character_list:
                sub_num = 1
            else:
                sub_num = 0
            char_list_len = len(character_list) - sub_num + 1
            if char_list_len > 6:
                pfp_size = 95
            elif char_list_len > 5:
                pfp_size = 105
            else:
                pfp_size = 115
            num_col = (741-8-16-pfp_size) // pfp_size
            num_row = -(-(len(character_list)-sub_num) // num_col)
            extra_space = (741-8-8-pfp_size) - (num_col * pfp_size)


        frame:
            xysize(741, 206)
            xalign 0.5
            yalign 0.08
            xoffset 8
            grid num_col num_row:
                xysize (pfp_size, pfp_size)
                spacing extra_space // num_col

                for person in character_list:
                    if person != m:
                        imagebutton:
                            xysize (pfp_size,pfp_size)
                            xalign 0.0
                            idle Transform(person.homepage_pic,
                                    size=(pfp_size, pfp_size))
                            background Transform('no_profile_update',
                                    size=(pfp_size,pfp_size))
                            selected_background Transform('new_profile_update',
                                    size=(pfp_size, pfp_size))
                            selected not person.seen_updates
                            action [SetField(person, 'seen_updates', True),
                                Show('chara_profile', who=person)]
                            activate_sound 'audio/sfx/UI/profile_screen_select.mp3'
                for x in range(num_col*num_row - len(character_list) + sub_num):
                    null

            imagebutton:
                xysize (pfp_size,pfp_size)
                hover Transform("profile_pic_select_square",
                        size=(pfp_size,pfp_size))
                idle m.get_pfp(pfp_size)
                background m.get_pfp(pfp_size)
                action Show('profile_pic')
                xalign 1.0
                xoffset -8
                yalign 0.0

        frame:
            xysize (750, 1170)
            yoffset -140
            # Text Messages
            button:
                style_prefix 'small_menu_circle'
                xalign 0.62
                if char_list_len > 10:
                    yalign 0.2
                else:
                    yalign 0.1
                selected new_message_count() > 0
                action Show('text_message_hub', Dissolve(0.5))
                if new_message_count() > 0:
                    add 'blue_maincircle' xalign 0.5 yalign 0.5
                    frame:
                        text str(new_message_count())
                else:
                    add "gray_maincircle" xalign 0.5 yalign 0.5
                add "msg_mainicon" xalign 0.5 yalign 0.5
                text "MESSAGE" style 'hex_text' yalign 0.85


            # Calls
            button:
                style_prefix 'small_menu_circle'
                xalign 0.91
                if char_list_len > 10:
                    yalign 0.4
                else:
                    yalign 0.3
                selected unseen_calls > 0
                action [SetVariable('unseen_calls', 0), Show('phone_calls')]
                if unseen_calls > 0:
                    add "blue_maincircle" xalign 0.5 yalign 0.5
                    frame:
                        text str(unseen_calls)
                else:
                    add "gray_maincircle" xalign 0.5 yalign 0.5

                add "call_mainicon" xalign 0.5 yalign 0.5
                text "CALL" style 'hex_text' yalign 0.85

            # Emails
            button:
                style_prefix 'small_menu_circle'
                xalign 0.342
                if char_list_len > 10:
                    yalign 0.4
                else:
                    yalign 0.3
                selected unread_emails() > 0
                action Show('email_hub', Dissolve(0.5))
                if unread_emails() > 0:
                    add "blue_maincircle" xalign 0.5 yalign 0.5
                    frame:
                        text str(unread_emails())
                else:
                    add "gray_maincircle" xalign 0.5 yalign 0.5
                add "email_mainicon" xalign 0.5 yalign 0.5
                text "EMAIL" style 'hex_text' yalign 0.85

            # Main Chatroom
            button:
                style 'big_menu_circle'
                if persistent.real_time:
                    action [Function(check_and_unlock_story),
                            Function(deliver_all_texts),
                            If(not story_archive
                                or not story_archive[0].archive_list,
                                Show('script_error', message="There is no content for this route"),
                            Show('day_select'))]
                else:
                    action [Function(deliver_all_texts), If(not story_archive
                                or not story_archive[0].archive_list,
                                Show('script_error', message="There is no content for this route"),
                            Show('day_select'))]
                add "rfa_chatcircle" yalign 0.5 xalign 0.5
                add "blue_chatcircle" xalign 0.5 yalign 0.5
                add "chat_icon" xalign 0.5 yalign 0.5
                text "CHATROOM" style 'hex_text' size 34


            # Links/etc on the left side of the screen
            vbox:
                style_prefix 'hex'
                # Album
                button:
                    if new_cg > 0:
                        add 'new_text' align (1.0, 0.1) xoffset 15
                    selected new_cg > 0
                    action [Function(check_for_CGs, all_albums=all_albums),
                            Show('photo_album', Dissolve(0.5))]
                    add "album_icon" xalign 0.5 yalign 0.35
                    text "ALBUM"

                # Guest
                button:
                    selected None
                    action Show('guestbook')
                    add "guest_icon" xalign 0.5 yalign 0.3
                    text "GUEST"

                # Developer Settings ("Shop")
                button:
                    background "red_hex"
                    hover_background "red_hex_hover"
                    selected None
                    action Show('developer_settings')
                    add "developer_settings" xalign 0.55 yalign 0.35
                    text "DEVELOPER" size 18

                # Link ("Notice")
                button:
                    selected None
                    action Show('links')
                    add 'link_hex' align (0.5, 0.35)
                    text "LINKS"

                # Exit to main menu ("Link")
                button:
                    selected None
                    action [Function(renpy.full_restart)]
                    add 'exit_hex' align (0.6, 0.38)
                    text "MAIN MENU" size 18

            ## Spaceship
            add "dot_line" xalign 0.5 yalign .97

            if chips_available:

                if not reshow:
                    fixed at chip_anim:
                        xysize(90,70)
                        xalign 0.93
                        yalign 0.942
                        add "space_chip_explode"

                    add "space_chip_active" xalign 0.92 yalign 0.98

                    fixed at spaceship_chips(1.0):
                        xysize (100,110)
                        xalign 0.96
                        yalign 1.0
                        add "space_flame" xalign 0.5 yalign 1.0
                        add "spaceship" xalign 0.5 yalign 0.0
                        imagebutton:
                            idle "space_transparent_btn"
                            focus_mask None
                            activate_sound 'audio/sfx/UI/select_6.mp3'
                            action Show('chip_tap')

                else:
                    fixed at chip_anim(0):
                        xysize(90,70)
                        xalign 0.93
                        yalign 0.942
                        add "space_chip_explode"

                    add "space_chip_active2" xalign 0.92 yalign 0.98

                    fixed at spaceship_chips:
                        xysize (100,110)
                        xalign 0.96
                        yalign 1.0
                        add "space_flame" xalign 0.5 yalign 1.0
                        add "spaceship" xalign 0.5 yalign 0.0
                        imagebutton:
                            idle "space_transparent_btn"
                            focus_mask None
                            activate_sound 'audio/sfx/UI/select_6.mp3'
                            action Show('chip_tap')

            else:
                add "space_chip_inactive" xalign 0.92 yalign 0.98

                fixed at spaceship_flight:
                    xysize (100,110)
                    xalign 0.04
                    yalign 1.0
                    add "space_flame" xalign 0.5 yalign 1.0
                    add "spaceship" xalign 0.5 yalign 0.0
                    imagebutton:
                            idle "space_transparent_btn"
                            focus_mask None
                            activate_sound 'audio/sfx/UI/select_6.mp3'
                            action Show('spaceship_thoughts', Dissolve(0.5))


style small_menu_circle_button:
    xysize(168,168)
    selected_background "blue_mainbtn"
    selected_hover_background "blue_mainbtn_hover"
    background "gray_mainbtn"
    hover_background "gray_mainbtn_hover"
    activate_sound 'audio/sfx/UI/select_phone_text.mp3'

style small_menu_circle_frame:
    xysize(45,45)
    xalign 1.0
    yalign 0.0
    background 'new_text_count'

style small_menu_circle_text:
    is text_num

style big_menu_circle:
    xysize(305,305)
    xalign 0.65
    yalign 0.722
    background "gray_chatbtn"
    hover_background "gray_chatbtn_hover"
    activate_sound "audio/sfx/UI/chatroom_select.mp3"

style hex_vbox:
    spacing 20
    xysize(140, 830)
    xalign 0.03
    yalign 0.5

style hex_button:
    xysize(130,149)
    selected_background "blue_hex"
    selected_hover_background "blue_hex_hover"
    background "white_hex"
    hover_background "white_hex_hover"

style hex_text:
    is text
    xalign 0.5
    yalign 0.8
    text_align 0.5
    color "#fff"
    size 20
    font gui.sans_serif_1xb
    kerning -1

##########################################################
## Link screens to additional content
##########################################################
screen links():
    tag menu
    use menu_header("Links", Show('chat_home', Dissolve(0.5))):
        frame:
            style_prefix 'link_menu'
            vbox:
                text "Follow Program Updates"
                grid 2 1:
                    button:
                        vbox:
                            style_prefix 'link_btn'
                            fixed:
                                add 'discord'
                            text 'Discord'
                        action OpenURL('https://discord.gg/BPbPcpk')
                    button:
                        vbox:
                            style_prefix 'link_btn'
                            fixed:
                                add 'github'
                            text "GitHub"
                        action OpenURL('https://github.com/shawna-p/mysterious-messenger')
                null height 5
                button:
                    add 'kofi'
                    action OpenURL('https://ko-fi.com/somniarre')

                null height 20
                text "Additional Credits"
                vbox:
                    style_prefix 'credits'
                    text "Developer settings icon made by Freepik"
                    text "Link icon made by Creaticca Creative Agency"
                    text "Exit to Main Menu icon made by Pixel perfect"
                    text "Zodiac symbols made by Freepik"
                    text "All creators can be found at {a=https://www.flaticon.com/}www.flaticon.com{/a},\nicons used under the Freepik License"

style credits_text:
    is text
    color "#fff"
    xalign 0.5
    text_align 0.5
    size 25

style credits_vbox:
    is link_menu_vbox

style link_menu_frame:
    xysize (720, 1170)
    yalign 1.0
    xalign 0.5
    background "#000a"

style link_menu_vbox:
    xsize 750
    xalign 0.5
    spacing 20
    yalign 0.2

style link_menu_text:
    size 42
    color "#fff"
    xalign 0.5

style link_menu_grid:
    xalign 0.5
    spacing 50

style link_menu_button:
    xalign 0.5

style link_btn_vbox:
    is default
    ysize 150

style link_btn_text:
    is default
    color "#fff"
    xalign 0.5
    text_align 0.5

style link_btn_fixed:
    xysize (146,143)


##########################################################
## Additional developer settings for creating new content
##########################################################

screen developer_settings():
    modal True
    add "#000a"

    frame:
        xysize (675, 600)
        background Transform('menu_settings_panel_light', alpha=0.95)
        align (0.5, 0.5)

    frame:
        xysize (675, 600)
        background 'menu_settings_panel_bright'
        align (0.5, 0.5)
        bottom_padding 20

        imagebutton:
            align (1.0, 0.0)
            xoffset 3 yoffset -3
            idle 'input_close'
            hover 'input_close_hover'
            action Hide('developer_settings')

        text "Developer Settings" style "settings_style" xpos 55 ypos 5

        vbox:
            style_prefix "other_settings"
            yalign 0.5
            null height 30

            frame:
                xsize 650
                background "menu_settings_panel"
                has vbox
                spacing 6
                first_spacing 15
                text "Variables for testing":
                    style "settings_style" xpos 45 ypos -3
                style_prefix "check"
                textbutton _("Testing Mode"):
                    action ToggleField(persistent, "testing_mode")
                textbutton _("Unlock all story"):
                    action If(not main_menu,
                        [ToggleField(persistent, "unlock_all_story"),
                        Function(check_and_unlock_story)],
                        ToggleField(persistent, "unlock_all_story"))
                textbutton _("Real-Time Mode"):
                    action ToggleField(persistent, "real_time")
                textbutton _("Hacked Effect"):
                    action ToggleVariable('hacked_effect')
                textbutton _("Receive Hourglasses in Chatrooms"):
                    action ToggleField(persistent, 'receive_hg')
                textbutton _("Use custom route select screen"):
                    action ToggleField(persistent, 'custom_route_select')
                textbutton _("Prefer local documentation"):
                    action ToggleField(persistent, 'open_docs_locally')

            hbox:
                align (0.5, 0.5)
                spacing 40
                textbutton _('Fix Persistent'):
                    style "other_settings_end_button"
                    text_style 'other_settings_end_button_text'
                    ysize 80
                    xsize 285
                    yalign 1.0
                    if not main_menu:
                        action CConfirm(("Resetting "
                            + "your persistent variables may cause "
                            + "information to be lost. You will "
                            + "need to start a new game after resetting "
                            + "your persistent variables.\nContinue?"),
                            [Function(reset_old_persistent),
                                Jump('restart_game')])
                    else:
                        action CConfirm(("Resetting your persistent"
                            + " variables may cause information to be lost. You "
                            + "will need to start a new game after resetting your "
                            + "persistent variables.\nContinue?"),
                            [Function(reset_old_persistent)])

                textbutton _('Documentation'):
                    style "other_settings_end_button"
                    text_style 'other_settings_end_button_text'
                    ysize 80
                    xsize 285
                    yalign 1.0
                    action OpenMysMeDocumentation()

default persistent.open_docs_locally = False

init python:

    import os.path

    MM_WEB_DOC_URL = "https://mysterious-messenger.readthedocs.io/en/latest/"

    # Get the game dir without "/game"
    mm_folder_dir = os.path.dirname(config.gamedir)
    MM_DOC_PATH = os.path.join(mm_folder_dir, "docs\\_build\\html\\")


    def OpenMysMeDocumentation(link=False):
        """
        A custom action which opens the Mysterious Messenger documentation.
        """

        if not link:
            link = "index.html"

        web_link = MM_WEB_DOC_URL + link
        doc_link = os.path.join(MM_DOC_PATH, link)

        if store.persistent.open_docs_locally:
            if "#" in link:
                truncated_link = link.split('#')[0]
                existing_link = os.path.join(MM_DOC_PATH, truncated_link)
            else:
                existing_link = doc_link

            if os.path.exists(existing_link):
                doc_link = "file:///" + doc_link
            else:
                doc_link = None

            if doc_link is not None:
                return OpenURL(doc_link)
        return OpenURL(web_link)



########################################################
## The Profile Screen for each of the characters
########################################################

screen chara_profile(who):

    tag settings_screen
    modal True

    use menu_header("Profile", Hide('chara_profile', Dissolve(0.5))):
        frame:
            xysize (750, 1170)

            add who.cover_pic yoffset -10

            button:
                xalign 0.1 yalign 0.62
                add who.get_pfp(314)
                background 'profile_outline'
                hover_foreground Fixed(Transform('#fff3', size=(328, 324)),
                                Transform('menu_pencil', align=(0.95, 0.05)))
                padding (7, 5)
                action Show('pick_chara_pfp', who=who)
            fixed:
                xysize (350,75)
                xalign 0.96
                yalign 0.645
                text who.name style "profile_header_text"
            fixed:
                xysize (700, 260)
                yalign 0.95
                text who.status style "profile_status"

init python:
    def get_pfp_list(who):
        """Get the appropriate profile picture list for who, if it exists."""
        try:
            if who == store.sa:
                who = store.r
            pfp_list = getattr(store, who.file_id + '_unlockable_pfps')
        except:
            print("ERROR: Could not find unlockable_pfps variable")
            pfp_list = []
        return pfp_list

## Screen that lets you choose a profile picture for a character
screen pick_chara_pfp(who):
    modal True

    default pfp_list = get_pfp_list(who)
    default num_rows = -(-(len(pfp_list)+1) // 4)

    add "#000a"
    frame:
        style_prefix 'pick_pfp'
        imagebutton:
            idle 'input_close'
            hover 'input_close_hover'
            action [Hide('pick_chara_pfp')]

        text "Choose " + who.name + "'s profile picture"

        vpgrid:
            rows num_rows
            cols 4
            draggable True
            mousewheel True
            scrollbars "vertical"
            button:
                background 'menu_ringtone_box'
                text "Revert to default" style 'pick_pfp_text2'
                hover_foreground "menu_ringtone_box"
                action SetField(who, 'bonus_pfp', False)
            for img, condition in pfp_list:
                button:
                    if is_unlocked_pfp(img, condition):
                        background Transform(img, size=(140, 140))
                        hover_foreground "#fff3"
                        action SetField(who, 'bonus_pfp', img)
                    elif is_unlocked_pfp(img, condition) is None:
                        background Transform(img, size=(140,140))
                        action CConfirm(("Would you like to unlock this "
                            + "profile picture for [pfp_cost] hearts?"),
                            If(persistent.spendable_hearts.get(
                                who.file_id, 0) >= pfp_cost,
                            [SetDict(persistent.spendable_hearts, who.file_id,
                                persistent.spendable_hearts.get(who.file_id,
                                0)-pfp_cost),
                            AddToSet(persistent.bought_prof_pics, img)],
                            CConfirm("You do not have enough heart points with "
                                + who.name + " to purchase this picture.")))
                        add "#0005" size (140, 140)
                        add 'plot_lock' align (0.5, 0.5)
                        add 'header_heart' align (0.95, 0.95)
                    else:
                        background Transform('img_locked', size=(140, 140))
                        action CConfirm(("You have not yet "
                            + "unlocked this profile picture."))

    frame:
        background "space_black_box"
        padding (12, 5)
        align (.5, 0.97)
        has hbox
        spacing 5
        align (0.5, 0.5)
        add who.greet_img(0.8) align (0.5, 0.5)
        text str(persistent.spendable_hearts.get(who.file_id, 0)):
            style "point_indicator"
            align (0.5, 0.5)
        add 'header_heart':
            align (0.5, 0.52)

style pick_pfp_frame:
    xysize(675,1000)
    background Fixed("menu_settings_panel_bright", "menu_settings_panel_bright")
    align (0.5, 0.5)

style pick_pfp_image_button:
    align (1.0, 0.0)
    xoffset 3 yoffset -3

style pick_pfp_text:
    is settings_style
    xpos 25 ypos 3

style pick_pfp_vpgrid:
    xysize (650, 925)
    xoffset 15
    spacing 20

style pick_pfp_side:
    xalign 1.0
    yalign 0.8
    spacing 15

style pick_pfp_button:
    xysize (140, 140)
    padding (0,0)

style pick_pfp_text2:
    text_align 0.5
    align (0.5, 0.5)

init python:
    def is_unlocked_pfp(img, condition, pfp_list=None):
        """
        Return True if this image should be unlocked as a selectable
        bonus profile picture.
        """

        if store.persistent.testing_mode:
            return True

        if condition != 'seen':
            # Evaluate the condition
            try:
                return eval(condition)
            except:
                print("ERROR: Could not evaluate unlock condition on image.")
                return False

        # Otherwise, need to check if this image has been seen
        if pfp_list is None:
            pfp_list = store.persistent.unlocked_prof_pics
        if img in pfp_list:
            if pfp_list != store.persistent.bought_prof_pics:
                return (is_unlocked_pfp(img, condition,
                        store.persistent.bought_prof_pics))
            return True
        if img[:7] == 'images/' and img[7:] in pfp_list:
            if pfp_list != store.persistent.bought_prof_pics:
                return (is_unlocked_pfp(img, condition,
                        store.persistent.bought_prof_pics))
            return True
        # Could also check if it's been registered under a different name
        no_ext = img.split('.')[0]
        if (no_ext + '.png' in pfp_list or no_ext[7:] + '.png' in pfp_list):
            if pfp_list != store.persistent.bought_prof_pics:
                return (is_unlocked_pfp(img, condition,
                        store.persistent.bought_prof_pics))
            return True
        if (no_ext + '.jpg' in pfp_list or no_ext[7:] + '.jpg' in pfp_list):
            if pfp_list != store.persistent.bought_prof_pics:
                return (is_unlocked_pfp(img, condition,
                        store.persistent.bought_prof_pics))
            return True
        if pfp_list == store.persistent.bought_prof_pics:
            return None
        return False


style profile_header_text:
    align (0.5, 0.5)
    text_align 0.5
    color "#fff"
    font gui.sans_serif_1
    size 55

style profile_status:
    text_align 0.5
    align (0.5, 0.5)
    color "#fff"
    font gui.serif_1
    size 40
    xmaximum 600

