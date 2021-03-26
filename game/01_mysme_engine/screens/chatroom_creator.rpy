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

        dialogue = "{font=" + entry_styles['font'] + "}" + dialogue
        dialogue += "{/font}"
        entry.what = dialogue
        store.chatlog.append(entry)
        return

default chat_dialogue = ""
default the_entry = ChatEntry(s, "None", upTime())
default chat_dialogue_input = InputDialogue('chat_dialogue')
default last_added = [ ]
define creator_messenger_ysize = 640
default entry_styles = {
    'font' : gui.sans_serif_1,
    'specBubble' : None,
    'img' : False,
    'size' : 0
}

screen chatroom_creator():

    default show_fonts = False

    tag menu
    use starry_night()
    add Transform('bg ' + current_background,
            crop=(0, 315, 750, creator_messenger_ysize)):
        yoffset 150
    use menu_header("Chat Creator", Show('main_menu', Dissolve(0.5)),
            hide_bkgr=True):
        use messenger_screen()
        hbox:
            box_wrap True
            spacing 15
            xalign 0.5
            xmaximum 740
            style_prefix 'check'
            for chara in all_characters:
                textbutton chara.name:
                    left_padding 35
                    action SetField(the_entry, 'who', chara)
        hbox:
            spacing 5
            # Font styles and stuff
            button:
                background "#fff"
                xysize (47, 47)
                padding (2, 2)
                add "#000"
                text "B" style 'sser1xb' align (0.5, 0.5) color "#fff"
            button:
                background "#fff"
                xysize (47, 47)
                padding (2, 2)
                add "#000"
                text "I" italic True align (0.5, 0.5) color "#fff"
            button:
                background "#fff"
                xysize (47, 47)
                padding (2, 2)
                add "#000"
                vbox:
                    spacing -3
                    align (0.5, 0.5)
                    text "U" underline True color "#fff" xalign 0.5
                    add Solid("#fff") size (30, 1) xalign 0.5
            button:
                background "#fff"
                xysize (47+20, 47)
                padding (2, 2)
                add "#000"
                add 'text_size_decrease'
                action SetDict(entry_styles, 'size', entry_styles['size']-5)
            button:
                background "#fff"
                xysize (47+20, 47)
                padding (2, 2)
                add "#000"
                add 'text_size_increase'
                action SetDict(entry_styles, 'size', entry_styles['size']+5)
            button:
                background "#fff"
                xysize (47+20, 47)
                padding (2, 2)
                add "#000"
                add 'text_size_reset'
                action SetDict(entry_styles, 'size', 0)
            button:
                background "#fff"
                xysize (105, 47)
                padding (5, 2)
                add "#000"
                text "Fonts" color "#fff" size 29 align (0.5, 0.5)
                action ToggleScreenVariable('show_fonts', True)
        showif show_fonts:
            hbox:
                at slide_in_out()
                spacing 5
                button:
                    background "#fff"
                    xysize (105, 47)
                    padding (5, 2)
                    add "#000"
                    text "Font 1" style 'sser1' color "#fff" size 29 align (0.5, 0.5)
                    action SetDict(entry_styles, 'font', gui.sans_serif_1)
                button:
                    background "#fff"
                    xysize (105, 47)
                    padding (5, 2)
                    add "#000"
                    text "Font 2" style 'sser2' color "#fff" size 29 align (0.5, 0.5)
                    action SetDict(entry_styles, 'font', gui.sans_serif_2)
                button:
                    background "#fff"
                    xysize (105, 47)
                    padding (5, 2)
                    add "#000"
                    text "Font 3" style 'ser1' color "#fff" size 29 align (0.5, 0.5)
                    action SetDict(entry_styles, 'font', gui.serif_1)
                button:
                    background "#fff"
                    xysize (105, 47)
                    padding (5, 2)
                    add "#000"
                    text "Font 4" style 'ser2' color "#fff" size 29 align (0.5, 0.5)
                    action SetDict(entry_styles, 'font', gui.serif_2)
                button:
                    background "#fff"
                    xysize (105, 47)
                    padding (5, 2)
                    add "#000"
                    text "Font 5" style 'curly' color "#fff" size 29 align (0.5, 0.5)
                    action SetDict(entry_styles, 'font', gui.curly_font)
                button:
                    background "#fff"
                    xysize (105, 47)
                    padding (5, 2)
                    add "#000"
                    text "Font 6" style 'blocky' color "#fff" size 29 align (0.5, 0.5)
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
                if is_focused:
                    caret 'text_caret'
                else:
                    caret Null()
                font entry_styles['font']
                align (0.0, 0.5)
                xmaximum 690
                size gui.text_size + entry_styles['size']
        action chat_dialogue_input.Enable()

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