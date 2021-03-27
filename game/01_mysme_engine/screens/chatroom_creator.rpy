init python:
    class InputDialogue(InputValue):
        """InputValue that lets the user type dialogue to the program."""
        def __init__(self, var, default="Insert Text Here"):
            self.var = var
            self.s = default
            if not hasattr(store, var):
                setattr(store, var, default)

        def get_text(self):
            return getattr(store, self.var) or self.s

        def set_text(self, s):
            setattr(store, self.var, s)
            self.s = s

            store.the_entry.what = s
            if s:
                self.enter(simulate=True)

        def enter(self, simulate=False):
            if not simulate:
                renpy.run([Function(add_creation_entry),
                    Function(chat_dialogue_input.set_text, ''),
                    SetVariable('last_added', [ ])])
            else:
                renpy.run(self.Enable())
            raise renpy.IgnoreEvent()

    def pop_chatlog():
        if store.chatlog:
            store.last_added.append(store.chatlog.pop())
            # Cut down on how many entries we remember
            store.last_added = store.last_added[-20:]
        else:
            # They want to undo clearing the chatlog
            store.chatlog = store.last_added
            store.last_added = [ ]
        return

    def redo_chatlog():
        if store.last_added:
            store.chatlog.append(store.last_added.pop())
        return

    def add_creation_entry():
        global entry_styles
        # Make a copy of the entry
        entry = copy(store.the_entry)
        # Add fonts and bubbles and stuff
        dialogue = entry.what
        if entry_styles['font'] == gui.curly_font:
            entry_styles['size'] += 5
        if entry_styles['size'] != 0:
            if entry_styles['size'] > 0:
                dialogue = "{size=+" + str(entry_styles['size']) + "}" + dialogue
            else:
                dialogue = "{size=-" + str(abs(entry_styles['size'])) + "}" + dialogue
            dialogue += "{/size}"
        # Check for underline
        if entry_styles['underline']:
            dialogue = "{u}" + dialogue + "{/u}"
        if entry_styles['italics']:
            dialogue = "{i}" + dialogue + "{/i}"

        # Check for bold fonts
        newfont = entry_styles['font']
        if entry_styles['bold']:
            if entry_styles['font'] == gui.sans_serif_1:
                newfont = gui.sans_serif_1xb
            elif entry_styles['font'] == gui.sans_serif_2:
                newfont = gui.sans_serif_2xb
            elif entry_styles['font'] == gui.serif_1:
                newfont = gui.serif_1xb
            elif entry_styles['font'] == gui.serif_2:
                newfont = gui.serif_2xb
            else:
                # Just put bold tags around it
                dialogue = "{b}" + dialogue + "{/b}"

        dialogue = "{font=" + newfont + "}" + dialogue
        dialogue += "{/font}"
        entry.what = dialogue
        store.chatlog.append(entry)
        return

    def create_enter_exit(who, enter=True):
        the_str = ""
        if enter:
            the_str = who.name + " has entered the chatroom."
        else:
            the_str = who.name + " has left the chatroom."

        chatlog.append(ChatEntry(store.special_msg, the_str, upTime()))
        return

    def add_emote(emote):

        if emote is None:
            return
        the_str = "{image=" + emote + "}"
        chatlog.append(ChatEntry(store.the_entry.who,
            the_str, upTime(), img=True))
        return

default chat_dialogue = ""
default emoji_speaker = s
default the_entry = ChatEntry(s, "None", upTime())
default chat_dialogue_input = InputDialogue('chat_dialogue')
default last_added = [ ]
define creator_messenger_ysize = 640
default entry_styles = {
    'font' : gui.sans_serif_1,
    'specBubble' : None,
    'img' : False,
    'size' : 0,
    'bold' : False,
    'italics' : False,
    'underline' : False
}

screen chat_creator_tabs(active_tab):
    hbox:
        style_prefix "settings_tabs"
        xalign 0.5
        # Dialogue / Effects / Other
        textbutton _('Dialogue'):
            sensitive active_tab != "Dialogue"
            action SetScreenVariable('active_tab', 'Dialogue')

        textbutton _('Effects'):
            sensitive active_tab != "Effects"
            action SetScreenVariable('active_tab', 'Effects')

        textbutton _('Other'):
            sensitive active_tab != "Other"
            action NullAction()

screen chatroom_creator():

    default active_tab = "Effects"

    tag menu
    use starry_night()
    add Transform('bg ' + current_background,
            crop=(0, 315, 750, creator_messenger_ysize)):
        yoffset 150
    use menu_header("Chat Creator", Show('main_menu', Dissolve(0.5)),
            hide_bkgr=True):
        use messenger_screen()
        use chat_creator_tabs(active_tab)
        if active_tab == "Dialogue":
            use dialogue_tab()
        elif active_tab == "Effects":
            use effects_tab()

screen dialogue_tab():
    default show_fonts = False

        hbox:
            button:
                style_prefix 'font_options'
                xysize (320, 47)
                add "#000"
                action Show('pick_speaker')
                hbox:
                    xoffset 6
                    text "Speaker:"
                    text the_entry.who.name size 27
            button:
                style_prefix 'font_options'
                xysize (210, 47)
                add "#000"
                text "Add Enter Msg" size 27
                action Function(create_enter_exit, the_entry.who, True)
            button:
                style_prefix 'font_options'
                xysize (210, 47)
                add "#000"
                text "Add Exit Msg" size 27
                action Function(create_enter_exit, the_entry.who, False)

        # button:
        #     xysize (280, 85)
        #     hbox:
        #         align (0.5, 0.5)
        #         spacing 8
        #         add Transform('album_icon', zoom=0.85) align (0.5, 0.5)
        #         text "Change background" color "#fff" size 30

        hbox:
            style_prefix 'font_options'
            # Font styles and stuff
            button:
                add "#000"
                text "B" font gui.sans_serif_1xb
                action ToggleDict(entry_styles, 'bold')
            button:
                add "#000"
                text "I" italic True
                action ToggleDict(entry_styles, 'italics')
            button:
                add "#000"
                action ToggleDict(entry_styles, 'underline')
                vbox:
                    text "U" underline True
                    add Solid("#fff") size (30, 1) xalign 0.5
            button:
                xsize 67
                add "#000"
                add 'text_size_decrease'
                sensitive entry_styles['size'] > 10
                action SetDict(entry_styles, 'size', entry_styles['size']-5)
            button:
                xsize 67
                add "#000"
                add 'text_size_increase'
                sensitive entry_styles['size'] < 50
                action SetDict(entry_styles, 'size', entry_styles['size']+5)
            button:
                xsize 67
                add "#000"
                add 'text_size_reset'
                action SetDict(entry_styles, 'size', 0)
            button:
                xsize 105
                xpadding 5
                add "#000"
                text "Fonts" size 29
                action ToggleScreenVariable('show_fonts', True)
        showif show_fonts:
            hbox:
                style_prefix 'font_options2'
                at slide_in_out()
                button:
                    add "#000"
                    text "Font 1" font gui.sans_serif_1
                    action SetDict(entry_styles, 'font', gui.sans_serif_1)
                button:
                    add "#000"
                    text "Font 2" font gui.sans_serif_2
                    action SetDict(entry_styles, 'font', gui.sans_serif_2)
                button:
                    add "#000"
                    text "Font 3" font gui.serif_1
                    action SetDict(entry_styles, 'font', gui.serif_1)
                button:
                    add "#000"
                    text "Font 4" font gui.serif_2
                    action SetDict(entry_styles, 'font', gui.serif_2)
                button:
                    add "#000"
                    text "Font 5" font gui.curly_font size 29+5
                    action SetDict(entry_styles, 'font', gui.curly_font)
                button:
                    add "#000"
                    text "Font 6" font gui.blocky_font
                    action SetDict(entry_styles, 'font', gui.blocky_font)


        use dialogue_input()
        hbox:
            spacing 40 xalign 0.5
            textbutton "Clear Chat":
                selected False
                action [SetVariable('last_added', chatlog),
                    SetVariable('chatlog', [ ])]
            textbutton "Undo":
                sensitive chatlog or (last_added and not chatlog)
                action Function(pop_chatlog)
            textbutton "Redo":
                sensitive last_added
                action Function(redo_chatlog)
            textbutton "Add to Chat":
                action [chat_dialogue_input.Disable(),
                    Function(add_creation_entry),
                    Function(chat_dialogue_input.set_text, ''),
                    SetVariable('last_added', [ ])]

style font_options_button:
    background "#fff"
    xysize (47, 47)
    padding (2, 2)

style font_options_text:
    align (0.5, 0.5)
    color "#fff"

style font_options_hbox:
    spacing 5

style font_options_vbox:
    spacing -3
    align (0.5, 0.5)

style font_options2_button:
    is font_options_button
    xysize (105, 47)
    padding (5, 2)


style font_options2_text:
    is font_options_text
    size 29
style font_options2_hbox is font_options_hbox
style font_options2_vbox is font_options_vbox


transform slide_in_out():
    on show, appear:
        yzoom 0.0
        easein 0.35 yzoom 1.0
    on hide:
        yzoom 1.0
        easein 0.35 yzoom 0.0

default text_input_yadj = ui.adjustment()

screen dialogue_input():
    $ focus_coord = renpy.focus_coordinates()
    $ is_focused = focus_coord[2] == 730.0 and focus_coord[3] == 180.0
    $ text_input_yadj.value = yadjValue
    $ size_bonus = 5 if entry_styles['font'] == gui.curly_font else 0
    button:
        xysize (730, 180)
        background 'input_square'
        if not is_focused:
            foreground "#0003"
        padding (14, 10)
        xalign 0.5 yalign 0.4
        viewport:
            yadjustment text_input_yadj
            xysize (730-28, 180-20)
            mousewheel True
            input value chat_dialogue_input:
                copypaste True
                color "#000"
                line_spacing 1
                if is_focused:
                    caret 'text_caret'
                else:
                    caret Null()
                if entry_styles['bold']:
                    if entry_styles['font'] == gui.sans_serif_1:
                        font gui.sans_serif_1xb
                    elif entry_styles['font'] == gui.sans_serif_2:
                        font gui.sans_serif_2xb
                    elif entry_styles['font'] == gui.serif_1:
                        font gui.serif_1xb
                    elif entry_styles['font'] == gui.serif_2:
                        font gui.serif_2xb
                    else:
                        bold True
                        font entry_styles['font']
                else:
                    font entry_styles['font']
                align (0.0, 0.5)
                xmaximum 690
                italic entry_styles['italics']
                underline entry_styles['underline']
                size gui.text_size + entry_styles['size'] + size_bonus
        action chat_dialogue_input.Enable()

screen pick_speaker():
    button:
        xysize (config.screen_width, config.screen_height)
        background None
        action Hide('pick_speaker')
    frame:
        background "#000"
        padding (2, 2)
        anchor (0.0, 0.5)
        pos (340, 890)
        has fixed:
            fit_first True
        vbox:
            for chara in all_characters:
                textbutton chara.name:
                    if chara.bubble_color:
                        background chara.bubble_color
                    else:
                        background "#fff"
                    # Add size_group for the buttons
                    xminimum 200
                    text_idle_color "#000"
                    action [SetField(the_entry, 'who', chara),
                        Hide('pick_speaker')]

image text_caret:
    Solid("#000", xmaximum=2)
    0.5
    Solid("#0000", xmaximum=2)
    0.5
    repeat

image text_size_increase = Composite(
    (47+20, 47),
    (5+5, 18), Text("T", color="#fff", font=gui.serif_1xb, size=14),
    (12+4, 4), Text("T", color="#fff", font=gui.serif_1xb, size=30),
    (30+5, 8), Text("+", color="#fff", font=gui.serif_1xb, size=30)
)
image text_size_decrease = Composite(
    (47+20, 47),
    (5+5, 18), Text("T", color="#fff", font=gui.serif_1xb, size=14),
    (12+4, 4), Text("T", color="#fff", font=gui.serif_1xb, size=30),
    (30+5, 8), Text("-", color="#fff", font=gui.serif_1xb, size=30)
)

image text_size_reset = Composite(
    (47+20, 47),
    (5+5, 18), Text("T", color="#fff", font=gui.serif_1xb, size=14),
    (12+4, 4), Text("T", color="#fff", font=gui.serif_1xb, size=30),
    (30+3, 12), 'Menu Screens/Main Menu/update_arrow.png'
)