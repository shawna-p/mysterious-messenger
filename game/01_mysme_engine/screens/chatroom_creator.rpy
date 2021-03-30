init python:
    class InputDialogue(InputValue):
        """InputValue that lets the user type dialogue to the program."""
        def __init__(self, var, default="Insert Text Here",
                edit_action=False):
            self.var = var
            self.s = default
            self.edit_action = edit_action
            if not hasattr(store, var):
                setattr(store, var, default)

        def get_text(self):
            return getattr(store, self.var) or self.s

        def set_text(self, s):
            setattr(store, self.var, s)
            self.s = s

            if not self.edit_action:
                store.the_entry.what = s
            if s:
                self.enter(simulate=True)

        def enter(self, simulate=False):
            if not simulate:
                if not self.edit_action:
                    renpy.run([Function(add_creation_entry),
                        Function(self.set_text, ''),
                        SetVariable('last_added', [ ])])
                else:
                    # This is an edit to an existing entry
                    renpy.run([
                        Function(self.set_text, ''),
                    ])
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

    def add_creation_entry(return_entry=False):
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
        if return_entry:
            return entry
        store.chatlog.append(entry)
        return

    def get_styles_from_entry(msg):
        global edit_styles
        edit_styles = {
            'font' : gui.sans_serif_1,
            'specBubble' : None,
            'img' : False,
            'size' : 0,
            'bold' : False,
            'italics' : False,
            'underline' : False
        }
        # Fetch the dialogue styles from an entry
        dialogue = msg.what
        if "{i}" in dialogue:
            edit_styles['italics'] = True
        if "{u}" in dialogue:
            edit_styles['underline'] = True
        if "{font" in msg.what:
            # isolate out the font
            ffont = msg.what.split('{font=')[1]
            str_font = ffont.split('}')[0]
            # Check for bold/xbold
            if str_font in [gui.serif_1b, gui.serif_1xb]:
                str_font = gui.serif_1
                edit_styles['bold'] = True
            elif str_font in [gui.serif_2b, gui.serif_2xb]:
                str_font = gui.serif_2
                edit_styles['bold'] = True
            elif str_font in [gui.sans_serif_1b, gui.sans_serif_1xb]:
                str_font = gui.sans_serif_1
                edit_styles['bold'] = True
            elif str_font in [gui.sans_serif_2b, gui.sans_serif_2xb]:
                str_font = gui.sans_serif_2
                edit_styles['bold'] = True

            edit_styles['font'] = str_font
            print("font is", str_font)
        if "{b}" in msg.what:
            edit_styles['bold'] = True
        if "{size" in msg.what:
            # Fetch the size
            ssize = msg.what.split("{size=")[1]
            str_size = ssize.split("}")[0]
            if str_size[0] == "+":
                str_size = str_size[1:]
            int_size = int(str_size)
            edit_styles['size'] = int_size





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

    def add_bubble(bubble_info):

        entry = add_creation_entry(True)
        # Determine if the bubble had its size set
        if bubble_info['size'] not in ['Large', None]:
            # Adjust the size
            bub_start, bub_end = bubble_info['bubble'].split('_l.')
            if bubble_info['size'] == "Small":
                bub = bub_start + '_s.' + bub_end
            else:
                bub = bub_start + '_m.' + bub_end
        elif bubble_info['bubble'] is not None:
            bub = bubble_info['bubble']
        else:
            bub = None

        if bub:
            # Get just the "s_cloud_m" bit
            full_bub = bub.split('/')[-1].split('.')[0]
            bub_who = full_bub.split('_')[0]
            bub_end = full_bub.split('_')[1:]
            bub_end = ('_').join(bub_end)
            if bub_who == store.the_entry.who.file_id:
                # This belongs to the speaker
                entry.specBubble = bub_end
            else:
                entry.specBubble = full_bub

        if bubble_info['bounce']:
            entry.bounce = True

        store.chatlog.append(entry)

        # Reset the bubble dict
        store.bubble_info = {
            'size' : None,
            'bounce' : False,
            'bubble' : None
        }

        return

    def find_bubble_sizes(bubble):
        """Find the sizes this bubble comes in."""

        if 'glow' in bubble:
            return None
        sizes = [ 'Large' ]
        try:
            bub_start, bub_end = bubble.split('_l.')
            if renpy.loadable(bub_start + '_m.' + bub_end):
                sizes.append('Medium')
            if renpy.loadable(bub_start + '_s.' + bub_end):
                sizes.append('Small')
        except:
            return None
        return sizes

    def update_speaker(ind, chara):
        the_msg = store.chatlog[ind]
        new_entry = ChatEntry(chara, the_msg.what, the_msg.thetime,
            the_msg.img, the_msg.bounce, the_msg.specBubble)
        store.chatlog.insert(ind, new_entry)
        chatlog.remove(the_msg)
        return

default edit_dialogue = ""
default edit_dialogue_input = InputDialogue('edit_dialogue')
default edit_mode = True
default chat_dialogue = ""
default emoji_speaker = s
default bubble_user = s
default bubble_info = {
    'size' : None,
    'bounce' : False,
    'bubble' : None
}
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
default edit_styles = {
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

    default active_tab = "Dialogue"
    default show_fonts = False

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
            use dialogue_tab(show_fonts)
        elif active_tab == "Effects":
            use effects_tab()

screen add_enter_exit_msg():
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

screen dialogue_tab(show_fonts, compact_ver=False):

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
        if not compact_ver:
            use add_enter_exit_msg()
    if compact_ver:
        hbox:
            use add_enter_exit_msg()
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


    use dialogue_input(compact_ver)
    hbox:
        spacing 40 xalign 0.5
        if not compact_ver:
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

screen effects_tab():
    hbox:
        textbutton "Add Emote":
            style_prefix "other_settings_end"
            action Show('select_emote')
        textbutton "Special Bubbles":
            style_prefix "other_settings_end"
            action Show('select_bubble')

screen select_emote():

    zorder 100
    modal True

    default selected_emote = None

    frame:
        maximum(680, 1000)
        background 'input_popup_bkgr'
        xalign 0.5
        yalign 0.6
        imagebutton:
            align (1.0, 0.0)
            idle 'input_close'
            hover 'input_close_hover'
            action Hide('select_emote')
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.6
            null height 10
            hbox:
                button:
                    style_prefix 'font_options'
                    xysize (320, 47)
                    add "#000"
                    action Show('pick_speaker', active_tab="Emoji",
                        pos=(220, 280), anchor=(0.5, 0.0))
                    hbox:
                        xoffset 6
                        text "Emotes:"
                        text emoji_speaker.name size 27
                button:
                    style_prefix 'font_options'
                    xysize (320, 47)
                    add "#000"
                    action Show('pick_speaker', pos=(535, 280),
                        anchor=(0.5, 0.0))
                    hbox:
                        xoffset 6
                        text "Speaker:"
                        text the_entry.who.name size 27
            frame:
                xysize (630,760)
                xalign 0.5
                background 'input_square' padding(40,40)
                vpgrid:
                    mousewheel True
                    xysize (590,740)
                    align (0.5, 0.5)
                    cols 3
                    for emote in emoji_speaker.emote_list:
                        button:
                            xysize (int(310*0.63),int(310*0.63))
                            hover_background '#e0e0e0'
                            selected_background '#a8a8a8'
                            add Transform(emote, zoom=0.63) align (0.5, 0.5)
                            action ToggleScreenVariable('selected_emote',
                                emote)


            textbutton _('Confirm'):
                text_style 'mode_select'
                xalign 0.5
                xsize 240
                ysize 80
                background 'menu_select_btn' padding(20,20)
                hover_background 'menu_select_btn_hover'
                action [Function(add_emote, selected_emote),
                    Hide('select_emote')]

screen select_bubble():

    zorder 100
    modal True

    frame:
        maximum(680, 1000)
        background 'input_popup_bkgr'
        xalign 0.5
        yalign 0.6
        imagebutton:
            align (1.0, 0.0)
            idle 'input_close'
            hover 'input_close_hover'
            action Hide('select_bubble')
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.6
            null height 10
            button:
                style_prefix 'font_options'
                xysize (320, 47)
                xalign 0.5
                add "#000"
                action Show('pick_speaker', active_tab="Bubble",
                    pos=(370, 300), anchor=(0.5, 0.0))
                hbox:
                    xoffset 6
                    text "Bubbles:"
                    text bubble_user.name size 27

            frame:
                xysize (630,760)
                xalign 0.5
                background 'menu_popup_bkgrd' padding (20,20)
                vpgrid:
                    mousewheel True
                    xysize (590,720)
                    align (0.5, 0.5)
                    cols 2
                    # Add the regular bubble image
                    if bubble_user is the_entry.who:
                        button:
                            xysize (580//2, 220)
                            hover_background '#e0e0e0'
                            selected_background '#a8a8a8'
                            selected not bubble_info['bounce']
                            action [SetDict(bubble_info, 'size', None),
                                SetDict(bubble_info, 'bubble', None),
                                SetDict(bubble_info, 'bounce', False)]
                            frame:
                                background bubble_user.reg_bubble_img
                                align (0.5, 0.5)
                                style 'reg_bubble'
                                add Null(height=100, width=150)
                        # The glowing bubble image
                        if bubble_user is not m:
                            button:
                                xysize (580//2, 220)
                                hover_background '#e0e0e0'
                                selected_background '#a8a8a8'
                                selected (bubble_info['bounce']
                                    and bubble_info['bubble'] is None)
                                action [SetDict(bubble_info, 'size', None),
                                    SetDict(bubble_info, 'bubble', None),
                                    SetDict(bubble_info, 'bounce', True)]
                                frame:
                                    background bubble_user.glow_bubble_img
                                    align (0.5, 0.5)
                                    style 'glow_bubble'
                                    add Null(height=100, width=150)

                    $ bub_list = bubble_user.get_bubbles()
                    for bub in bub_list:
                        button:
                            xysize (580//2, 220)
                            hover_background '#e0e0e0'
                            selected_background '#a8a8a8'
                            selected (bubble_info['bubble'] == bub)
                            if "glow" not in bub:
                                action [Show('pick_bubble_size',
                                    bubble_sizes=find_bubble_sizes(bub)),
                                    SetDict(bubble_info, 'bubble', bub),
                                    SetDict(bubble_info, 'bounce', True)]
                                add Transform(bub, zoom=0.46) align (0.5, 0.5)
                            else:
                                action [SetDict(bubble_info, 'size', None),
                                    SetDict(bubble_info, 'bubble', bub),
                                    SetDict(bubble_info, 'bounce', True)]
                                frame:
                                    background Frame(bub, 25, 25)
                                    align (0.5, 0.5)
                                    style 'glow_bubble'
                                    add Null(height=100, width=150)
                    # for emote in emoji_speaker.emote_list:
                    #     button:
                    #         xysize (int(310*0.63),int(310*0.63))
                    #         hover_background '#e0e0e0'
                    #         selected_background '#a8a8a8'
                    #         add Transform(emote, zoom=0.63) align (0.5, 0.5)
                    #         action ToggleScreenVariable('selected_bubble',
                    #             bubble)


            textbutton _('Confirm'):
                text_style 'mode_select'
                xalign 0.5
                xsize 240
                ysize 80
                background 'menu_select_btn' padding(20,20)
                hover_background 'menu_select_btn_hover'
                action [chat_dialogue_input.Disable(),
                    Function(add_bubble, bubble_info),
                    Function(chat_dialogue_input.set_text, ''),
                    SetVariable('last_added', [ ]),
                    Hide('select_bubble')]




screen dialogue_input(compact_ver=False):
    default box_size = (730, 180) if not compact_ver else (600, 220)
    default styles_dict = entry_styles if not compact_ver else edit_styles
    default size_bonus = 5 if styles_dict['font'] == gui.curly_font else 0
    default the_input = chat_dialogue_input if not compact_ver else edit_dialogue_input
    $ focus_coord = renpy.focus_coordinates()
    $ is_focused = (focus_coord[2] == box_size[0] and focus_coord[3] == box_size[1])
    $ text_input_yadj.value = yadjValue

    button:
        xysize box_size
        background 'input_square'
        if not is_focused:
            foreground "#0003"
        padding (14, 10)
        xalign 0.5 yalign 0.4
        viewport:
            yadjustment text_input_yadj
            xysize (730-28, 180-20)
            mousewheel True
            input value the_input:
                copypaste True
                color "#000"
                line_spacing 1
                if is_focused:
                    caret 'text_caret'
                else:
                    caret Null()
                if styles_dict['bold']:
                    if styles_dict['font'] == gui.sans_serif_1:
                        font gui.sans_serif_1xb
                    elif styles_dict['font'] == gui.sans_serif_2:
                        font gui.sans_serif_2xb
                    elif styles_dict['font'] == gui.serif_1:
                        font gui.serif_1xb
                    elif styles_dict['font'] == gui.serif_2:
                        font gui.serif_2xb
                    else:
                        bold True
                        font styles_dict['font']
                else:
                    font styles_dict['font']
                align (0.0, 0.5)
                xmaximum 690
                italic styles_dict['italics']
                underline styles_dict['underline']
                size gui.text_size + styles_dict['size'] + size_bonus
        action the_input.Enable()

screen pick_speaker(active_tab="Dialogue", pos=(320, 890), anchor=(0.0, 0.5),
        msg_ind=None):

    zorder 101
    python:
        if active_tab == "Emoji":
            all_chara = [chara for chara in all_characters if chara.emote_list]
        else:
            all_chara = all_characters

    button:
        xysize (config.screen_width, config.screen_height)
        background None
        action Hide('pick_speaker')
    frame:
        background "#000"
        padding (2, 2)
        anchor anchor
        pos pos
        has fixed:
            fit_first True
        vbox:
            for chara in all_chara:
                textbutton chara.name:
                    if chara.bubble_color:
                        background chara.bubble_color
                    else:
                        background "#fff"
                    # Add size_group for the buttons
                    xminimum 200
                    text_idle_color "#000"
                    if msg_ind:
                        action [Function(update_speaker, msg_ind, chara),
                            Hide('pick_speaker'), Hide('edit_msg_menu')]
                    elif active_tab == "Dialogue":
                        action [SetField(the_entry, 'who', chara),
                            SetVariable('bubble_user', chara),
                            Hide('pick_speaker')]
                    elif active_tab == "Emoji":
                        action [SetVariable('emoji_speaker', chara),
                            SetField(the_entry, 'who', chara),
                            Hide('pick_speaker')]
                    elif active_tab == "Bubble":
                        action [SetVariable('bubble_user', chara),
                            Hide('pick_speaker')]


screen pick_bubble_size(bubble_sizes):
    default pos = renpy.get_mouse_pos()
    zorder 101
    button:
        xysize (config.screen_width, config.screen_height)
        background None
        action Hide('pick_bubble_size')
    frame:
        at yzoom_in()
        background "#000"
        xysize (150, 150)
        pos pos
        if (pos[0] + 150) > config.screen_width:
            anchor (1.0, 0.5)
        else:
            anchor (0.0, 0.5)
        has vbox
        for sz in bubble_sizes:
            textbutton sz:
                xsize 150
                text_color "#fff"
                action [SetDict(bubble_info, 'size', sz),
                    Hide('pick_bubble_size')]

screen edit_msg_menu(msg, ind):
    default pos = renpy.get_mouse_pos()
    default too_wide = (pos[0] + 300) > config.screen_width
    default speaker_pos = (pos[0], pos[1]+(175//2)) if not too_wide else (pos[0]-300, pos[1]+(175//2))
    zorder 50
    button:
        xysize (config.screen_width, config.screen_height)
        background None
        action Hide('edit_msg_menu')
    frame:
        at yzoom_in()
        background "#000"
        xysize (300, 175)
        pos pos
        if too_wide:
            anchor (1.0, 0.5)
        else:
            anchor (0.0, 0.5)
        has vbox
        textbutton "Remove message":
            text_color "#fff"
            action CConfirm(("Are you sure you want to delete the message \""
                + msg.what + "\"?"), [RemoveFromSet(chatlog, msg),
                Hide('edit_msg_menu')])
        textbutton "Edit text":
            text_color "#fff"
            action [Hide('edit_msg_menu'), Show('dialogue_edit_popup')]
        text "Change bubble" color "#fff"
        textbutton "Change speaker":
            text_color "#fff"
            action Show('pick_speaker', msg_ind=ind, pos=speaker_pos,
                anchor=(0.0, 0.0))

screen dialogue_edit_popup():
    modal True

    default show_fonts = False

    frame:
        maximum(680, 600)
        background 'input_popup_bkgr'
        xpadding 20
        xalign 0.5
        yalign 0.6
        imagebutton:
            align (1.0, 0.0) xoffset 20
            idle 'input_close'
            hover 'input_close_hover'
            action Hide('dialogue_edit_popup')
        vbox:
            spacing 10
            null height 60
            use dialogue_tab(show_fonts, compact_ver=True)


transform yzoom_in():
    yzoom 0.0
    easein 0.2 yzoom 1.0
    on hide:
        easeout 0.2 yzoom 0.0

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