# ######################################################
# This file contains many of the primary menu screens
# used throughout the game. It's organized as follows:
#   python definitions:
#       class NameInput(InputValue)
#       def chat_greet(hour, greet_char)
#       def set_pronouns()
#   variable definitions
#   screen main_menu()
#       screen route_select_screen()
#   screen save/load
#       screen file_slots(title)
#   screen menu_header(title, return_action, envelope)
#   screen chat_home(reshow)
#       screen chara_profile(who)   
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
        hour = int(time.strftime('%H', time.localtime()))

        greet_text_english = "Welcome to my Mystic Messenger Generator!"
        # If translations were included, the text would be set like this
        # greet_text_english=morning_greeting[greet_char][the_greeting].english
        # greet_text_korean = morning_greeting[greet_char][the_greeting].korean
        
        if hour >= 6 and hour < 12:  # morning
            greet_text_english = "Good morning! " + greet_text_english
            
            num_greetings = len(morning_greeting[greet_char])
            the_greeting = renpy.random.randint(1, num_greetings) - 1
            renpy.play(morning_greeting[greet_char][the_greeting].sound_file, 
                channel="voice_sfx")
            
        elif hour >=12 and hour < 18:    # afternoon
            greet_text_english = "Good afternoon! " + greet_text_english
            
            num_greetings = len(afternoon_greeting[greet_char])
            the_greeting = renpy.random.randint(1, num_greetings) - 1
            renpy.play(afternoon_greeting[greet_char][the_greeting].sound_file, 
                channel="voice_sfx")
            
        elif hour >= 18 and hour < 22:  # evening
            greet_text_english = "Good evening! " + greet_text_english
            
            num_greetings = len(evening_greeting[greet_char])
            the_greeting = renpy.random.randint(1, num_greetings) - 1
            renpy.play(evening_greeting[greet_char][the_greeting].sound_file, 
                channel="voice_sfx")
            
        elif hour >= 22 or hour < 2: # night
            greet_text_english = "It's getting late! " + greet_text_english
            
            num_greetings = len(night_greeting[greet_char])
            the_greeting = renpy.random.randint(1, num_greetings) - 1
            renpy.play(night_greeting[greet_char][the_greeting].sound_file, 
                channel="voice_sfx")
            
        else:   # late night/early morning
            greet_text_english = "You're up late! " + greet_text_english
            
            num_greetings = len(late_night_greeting[greet_char])
            the_greeting = renpy.random.randint(1, num_greetings) - 1
            renpy.play(late_night_greeting[greet_char][
                            the_greeting].sound_file, channel="voice_sfx")
        
        
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

    def set_name_pfp():
        """Ensure the player's name and profile picture are set correctly."""

        global name, persistent
        name = persistent.name
        # if m.prof_pic != persistent.MC_pic and isImg(persistent.MC_pic):
        #     m.prof_pic = persistent.MC_pic
        # else:
        #     m.prof_pic = 'Profile Pics/MC/MC-1.png'
        # if m.name != persistent.name:
        #     m.name = persistent.name
        renpy.retain_after_load()
        return
      
            

## Variable to help determine when there should be Honey Buddha
## Chips available
default hbc_bag = RandomBag([ False, False, False, 
                              False, False, True, True ])


## Greeting Text
## (Eventually these will be stored in the Day_Greet object to be
## pulled alongside the sound file)
default greet_text_korean = "제 프로그램으로 환영합니다!"
default greet_text_english = "Welcome to my Mystic Messenger Generator!"

## This lets the program randomly pick a greet
## character to display for greetings       
default greet_list = [x.file_id for x in all_characters if (x != r and x != m)]
default greet_char = greet_list[0]


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
            text greet_text_korean style "greet_text" size 25
            text greet_text_english style "greet_text"

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
        fixed:   
            xysize (720, 1170)
            yalign 1.0
            xalign 0.5
            # New code after here
            vbox:
                style 'route_select_vbox'
                button:
                    style 'route_select_button'
                    action Start()
                    text "Start Game" style 'menu_text_small' align (0.5, 0.5)
                
style route_select_vbox:
    xysize (700, 750)
    align (0.5, 0.5)
    spacing 30

style route_select_button:
    is right_menu_button
    xysize (700, 320)
  
## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##

screen save():

    tag save_load
    modal True

    use menu_header("Save", Hide('save', Dissolve(0.5))):
        use file_slots(_("Save"))

screen load():

    tag save_load
    modal True
    
    use menu_header("Load", Hide('load', Dissolve(0.5))):
        use file_slots(_("Load"))

screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), 
                        auto=_("Automatic saves"), quick=_("Quick saves"))
        
    default the_day = "1st"
    
    python:      
        # Retrieve the name and day of the most recently completed
        # chatroom for the save file name  
        if (most_recent_chat is None 
                and chat_archive
                and chat_archive[0].archive_list):
            most_recent_chat = chat_archive[0].archive_list[0]
        elif most_recent_chat is None:
            most_recent_chat = ChatHistory('Example Chatroom', 
                                            'example_chat', '00:01')
        for day in chat_archive:
            if most_recent_chat in day.archive_list:
                the_day = day.day
                        
    
    fixed:
        # This ensures the input will get the enter event before any of the
        # buttons do.
        order_reverse True

        # Contains the save slots.
        vpgrid id 'save_load_vp':
            style_prefix "save_load"
            cols gui.file_slot_cols
            rows gui.file_slot_rows
            draggable True
            mousewheel True
            scrollbars "vertical" 
            
            # This adds the 'backup' save slot to the top when loading
            if title == "Load" and FileLoadable(mm_auto):
                $ save_title = (most_recent_chat.save_img + '|' 
                                + the_day + '|' + most_recent_chat.title)
                if '|' in FileSaveName(mm_auto):
                    $ rt, dn, cn = FileSaveName(mm_auto).split('|')
                else:                    
                    $ rt, dn, cn = save_title.split('|')
            
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
                            text "Today: [dn] DAY" yalign 1.0

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

            ## This displays all the regular save slots
            for i in range(gui.file_slot_cols * gui.file_slot_rows):

                $ slot = i + 1
                
                
                $ save_title = (most_recent_chat.save_img + '|' 
                                + the_day + '|' + most_recent_chat.title)
                if '|' in FileSaveName(slot):
                    $ rt, dn, cn = FileSaveName(slot).split('|')
                else:                    
                    $ rt, dn, cn = save_title.split('|')
                    
                $ file_time = FileTime(slot, empty="00:00")[-5:]
                $ file_hour = file_time[:2]
                $ file_min = file_time[-2:]
                $ next_day_name = False
                
                python:
                    # Compare file times to now
                    # E.g. if the game was saved at 20:30, if now is 20:29
                    # or earlier, it should load the next day
                    if int(file_hour) > int(datetime.now().strftime('%H')):
                        # Hour of save is greater; proceed to next day
                        # Gets the name of the next day for loading purposes
                        for index, archive in enumerate(chat_archive):
                            if dn == archive.day:
                                if index+1 < len(chat_archive):
                                    next_day_name = chat_archive[index+1].day
                                    break
                    elif int(file_hour) == int(datetime.now().strftime('%H')):
                        # Check minutes
                        if int(file_min) > int(datetime.now().strftime('%M')):
                            # Minutes of save are greater; proceed to
                            # next day. Gets the name of the next day
                            # for loading purposes
                            for index, archive in enumerate(chat_archive):
                                if dn == archive.day:
                                    if index+1 < len(chat_archive):
                                        next_day_name = (chat_archive[index+1].
                                                                            day)
                                        break
                    else:
                        next_day_name = False
                
                    
                if next_day_name:
                    $ long_msg = ("There is a difference between the save"
                                  + " time and the present time. It may cause"
                                  + " missed conversations or phone calls"
                                  + " during the time gap. Would you like to"
                                  + " continue?\n\nSave Time: " + dn 
                                  + " DAY " + file_time + "\n\nLoad Time: " 
                                  + next_day_name + " DAY " 
                                  + datetime.now().strftime('%H') + ":" 
                                  + datetime.now().strftime('%M'))
                else:
                    $ long_msg = ("There is a difference between the save"
                                  + " time and the present time. It may cause"
                                  + " missed conversations or phone calls"
                                  + " during the time gap. Would you like to"
                                  + " continue?\n\nSave Time: " + dn + " DAY " 
                                  + file_time + "\n\nLoad Time: " + dn 
                                  + " DAY " + datetime.now().strftime('%H') 
                                  + ":" + datetime.now().strftime('%M'))
               

                button:
                    if title == "Save":
                        action [SetVariable('save_name', save_title), 
                                FileAction(slot),
                                renpy.restart_interaction]
                    else: # title == "Load"
                        if (next_day_name and FileLoadable(slot) 
                                and persistent.real_time):
                            action [Show("confirm", message=long_msg, 
                                yes_action=[
                                SetField(persistent, 'just_loaded', True),
                                SetField(persistent, 'on_route', True), 
                                SetField(persistent, 'load_instr', '+1 day'), 
                                FileLoad(slot)], 
                                no_action=Hide('confirm'))]
                        elif FileLoadable(slot) and persistent.real_time:
                            action [Show("confirm", message=long_msg, 
                                yes_action=[
                                SetField(persistent, 'just_loaded', True),
                                SetField(persistent, 'on_route', True), 
                                SetField(persistent, 'load_instr', 'Same day'),
                                FileLoad(slot)], 
                                no_action=Hide('confirm'))]
                        elif not persistent.real_time and FileLoadable(slot):
                            action [SetField(persistent, 'on_route', True), 
                                    SetField(persistent, 'just_loaded', True),
                                    FileAction(slot)]

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
                                text "Today: [dn] DAY" yalign 1.0
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
        timer 60 action Function(next_chatroom) repeat True
        on 'show' action Function(next_chatroom)
        on 'replace' action Function(next_chatroom)
        
    if (not renpy.get_screen('text_message_screen') 
            and not main_menu 
            and not starter_story 
            and num_undelivered()):
        timer 0.5 action If(not randint(0,3), deliver_next, []) repeat True

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
                        action Show('confirm', message="There are no in-game "
                            + "purchases in this application. However, if "
                            + "you'd like to support its development, you can ",
                            #+ "{a=https://ko-fi.com/somniarre}check out my Ko-Fi here.{/a}",
                            yes_action=Hide('confirm'), show_link=True)
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
                                Show('preferences')]
                    else:
                        action Show("preferences")  
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
                    elif text_person and text_person.real_time_text:
                        action Show("confirm", 
                                    message=("Do you really want to leave this"
                                    + " text message? You won't be able to"
                                    + " continue this conversation."), 
                                    yes_action=[Hide('confirm'), 
                                    Jump('leave_inst_text')], 
                                    no_action=Hide('confirm'))    
                    else:
                        action return_action

         
    if title == "Save" or title == "Load":
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

image github = "Menu Screens/Chat Hub/github.png"
image discord = "Menu Screens/Chat Hub/discord.png"
image kofi = "Menu Screens/Chat Hub/ko-fi.png"
## Icon made by Freepik from www.flaticon.com
image developer_settings = "Menu Screens/Chat Hub/global-settings-freepik-red.png"
## Icon made by Creaticca Creative Agency from www.flaticon.com
image link_hex = "Menu Screens/Chat Hub/link-creaticca-creative-agency.png"
## Icon made by Pixel perfect from www.flaticon.com
image exit_hex = "Menu Screens/Chat Hub/exit-pixel-perfect.png"


image new_profile_update = Frame("Menu Screens/Chat Hub/main_profile_new_update.png", 0, 0)
image no_profile_update = Frame("Menu Screens/Chat Hub/main_profile_normal.png", 0, 0)

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
                Hide('chip_end'), renpy.retain_after_load,
                FileSave(mm_auto, confirm=False)]) 
 
    on 'replace':
        action If(renpy.get_screen('chip_tap') 
                    or renpy.get_screen('chip_cloud') 
                    or renpy.get_screen('chip_end'),
                SetField(persistent, 'just_loaded', False),
                [SetField(persistent, 'just_loaded', False), 
                Hide('chip_end'), renpy.retain_after_load, 
                FileSave(mm_auto, confirm=False)]) 

    use menu_header("Original Story"):
        # Note that only characters in the list 'character_list' will
        # show up here as profile pictures
        python:
            if len(character_list) > 6:
                pfp_size = 95
            elif len(character_list) > 5:
                pfp_size = 105
            else:
                pfp_size = 115
            num_col = (741-8-16-pfp_size) // pfp_size
            num_row = -(-(len(character_list)-1) // num_col)
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
                for x in range(num_col*num_row - len(character_list) + 1):
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
                if len(character_list) > 10:
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
                if len(character_list) > 10:
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
                if len(character_list) > 10:
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
                    action [Function(next_chatroom), 
                            Function(deliver_all_texts), 
                            Show('chat_select')]
                else:
                    action [Function(deliver_all_texts), Show('chat_select')]
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
                    action [Show('photo_album', Dissolve(0.5))]
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
                    # add "discord" xalign 0.5 yalign 0.42
                    # text "DISCORD" 

                # Exit to main menu ("Link")     
                button:
                    selected None
                    action [Function(renpy.full_restart)]
                    add 'exit_hex' align (0.6, 0.38)
                    text "MAIN MENU" size 18
                    # add "github" xalign 0.5 yalign 0.3
                    # text "GITHUB"

                    
                    
            ## Spaceship    
            add "dot_line" xalign 0.5 yalign .97
                
            $ spaceship_xalign = spaceship_get_xalign(True)
                
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
                
                if reshow:
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
                    xalign 0.04#spaceship_xalign
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
                xysize(650,280)
                background "menu_settings_panel"
                text "Variables for testing":
                    style "settings_style" xpos 45 ypos -3

                vbox:
                    spacing 6
                    style_prefix "check"
                    null height 30
                    textbutton _("Testing Mode"):
                        action If(not main_menu,
                            [ToggleField(persistent, "testing_mode"),
                            Function(next_chatroom)],
                            ToggleField(persistent, "testing_mode"))
                    textbutton _("Real-Time Mode"):
                        action ToggleField(persistent, "real_time")
                    textbutton _("Hacked Effect"):
                        action ToggleVariable('hacked_effect')
            textbutton _('Fix Persistent'):
                style "other_settings_end_button"
                text_style 'other_settings_end_button_text'
                ysize 80
                yalign 1.0
                if not main_menu:
                    action Show('confirm', message=("Resetting "
                        + "your persistent variables may cause "
                        + "information to be lost. You will "
                        + "need to start a new game after resetting "
                        + "your persistent variables.\nContinue?"),
                        yes_action=[Function(reset_old_persistent),
                            Jump('restart_game')],
                        no_action=Hide('confirm'))
                else:
                    action Show('confirm', message=("Resetting your persistent"
                        + " variables may cause information to be lost. You "
                        + "will need to start a new game after resetting your "
                        + "persistent variables.\nContinue?"),
                        yes_action=[Function(reset_old_persistent), 
                                    Hide('confirm')],
                        no_action=Hide('confirm'))


     
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
            
            fixed:
                xfit True yfit True
                xalign 0.1 yalign 0.62
                add who.get_pfp(314)
                add 'profile_outline'    
            fixed:
                xysize (350,75)
                xalign 0.96
                yalign 0.645
                text who.name style "profile_header_text"
            fixed:  
                xysize (700, 260)
                yalign 0.95
                text who.status style "profile_status"
    
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
        
