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
            elif s:
                entry_update = add_creation_entry(return_entry=True,
                    is_edit=True)
                store.chatlog[store.edit_msg_index].what = entry_update.what

            if s:
                self.enter(simulate=True)

        def enter(self, simulate=False):
            if not simulate:
                if not self.edit_action:
                    renpy.run([Function(add_creation_entry),
                        Function(self.set_text, ''),
                        SetVariable('redo_list', [ ])])
                else:
                    # This is an edit to an existing entry
                    renpy.run([
                        Function(self.set_text, ''),
                        Function(record_chatlog),
                        Hide('dialogue_edit_popup')
                    ])
            else:
                renpy.run(self.Enable())
            raise renpy.IgnoreEvent()

    def undo_chatlog():
        """
        Replace the chatlog with the most recent "undo" entry.
        """
        store.redo_list.append(chatlog)
        store.chatlog = store.undo_list.pop()


    def record_chatlog():
        """
        Add the current chatlog to the undo list.
        """
        new_log = [ ]
        for entry in store.chatlog:
            new_log.append(copy(entry))
        # Keep this in an intermediate variable; otherwise undo would
        # just pop the copy of the chatlog.
        store.undo_list.append(store.chatlog_copy)
        store.chatlog_copy = new_log
        if len(store.undo_list) > 5:
            # Keep the size down to 5 entries
            item = store.undo_list.pop(0)
            del item

        return

    def redo_chatlog():
        """
        Replace the chatlog with the most recent "undone" chatlog entry.
        """
        store.undo_list.append(chatlog)
        store.chatlog = store.redo_list.pop()

        return

    def add_creation_entry(return_entry=False, is_edit=False):
        """
        Adds an entry to the chatlog after parsing out which styles it should
        have. May also return the created entry or replace an existing
        entry if it's an edit.
        """
        global entry_styles, edit_styles
        if is_edit:
            styles_dict = edit_styles
            entry = store.chatlog[store.edit_msg_index]
            dialogue = store.edit_dialogue
        else:
            styles_dict = entry_styles
            # Make a copy of the entry
            entry = copy(store.the_entry)
            dialogue = entry.what

        # Add fonts and bubbles and stuff
        if styles_dict['font'] == gui.curly_font:
            the_size = styles_dict['size'] + 5
        else:
            the_size = styles_dict['size']
        if the_size != 0:
            if the_size > 0:
                dialogue = "{size=+" + str(the_size) + "}" + dialogue
            else:
                dialogue = "{size=-" + str(abs(the_size)) + "}" + dialogue
            dialogue += "{/size}"
        # Check for underline
        if styles_dict['underline']:
            dialogue = "{u}" + dialogue + "{/u}"
        if styles_dict['italics']:
            dialogue = "{i}" + dialogue + "{/i}"

        # Check for bold fonts
        newfont = styles_dict['font']
        if styles_dict['bold']:
            if styles_dict['font'] == gui.sans_serif_1:
                newfont = gui.sans_serif_1xb
            elif styles_dict['font'] == gui.sans_serif_2:
                newfont = gui.sans_serif_2xb
            elif styles_dict['font'] == gui.serif_1:
                newfont = gui.serif_1xb
            elif styles_dict['font'] == gui.serif_2:
                newfont = gui.serif_2xb
            else:
                # Just put bold tags around it
                dialogue = "{b}" + dialogue + "{/b}"

        dialogue = "{font=" + newfont + "}" + dialogue
        dialogue += "{/font}"
        entry.what = dialogue
        if return_entry:
            return entry
        if store.insert_msg_index == -1:
            store.chatlog.append(entry)
            store.yadj.value = store.yadjValue
        else:
            store.chatlog.insert(store.insert_msg_index, entry)
            store.insert_msg_index += 1
        record_chatlog()
        return

    def get_styles_from_entry(msg, return_dict=False):
        """
        Retrieve the appropriate styles from the 'what' part of a ChatEntry
        and store it in a dictionary format so it can be edited.
        """
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

        if return_dict:
            return dict(edit_styles), dialogue

        dialogue = renpy.filter_text_tags(msg.what, allow="image")
        store.edit_dialogue = dialogue
        store.edit_msg = msg

    def create_enter_exit(who, enter=True):
        """
        Add an enter/exit chatroom entry.
        """
        the_str = ""
        if enter:
            replay_type = 'enter'
            the_str = who.name + " has entered the chatroom."
        else:
            replay_type = 'exit'
            the_str = who.name + " has left the chatroom."

        if store.insert_msg_index == -1:
            chatlog.append(ChatEntry(store.special_msg, the_str, upTime(),
                for_replay=(replay_type, who)))
        else:
            chatlog.insert(store.insert_msg_index,
                ChatEntry(store.special_msg, the_str, upTime(),
                    for_replay=(replay_type, who)))
            store.insert_msg_index += 1
        record_chatlog()
        return

    def add_emote(emote, edit=False):
        """
        Add the given emoji to the chatlog.
        """
        if emote is None:
            return
        the_str = "{image=" + emote + "}"
        if not edit:
            if store.insert_msg_index == -1:
                store.chatlog.append(ChatEntry(store.the_entry.who,
                    the_str, upTime(), img=True))
            else:
                store.chatlog.insert(store.insert_msg_index,
                    ChatEntry(store.the_entry.who,
                        the_str, upTime(), img=True))
                store.insert_msg_index += 1
        else:
            the_msg = store.chatlog[store.edit_msg_index]
            new_entry = ChatEntry(the_msg.who, the_str, the_msg.thetime,
                the_msg.img, the_msg.bounce, the_msg.specBubble)
            store.chatlog.insert(store.edit_msg_index, new_entry)
            chatlog.remove(the_msg)
            store.edit_msg_index = -1
        record_chatlog()
        return

    def update_edit_text():
        """
        Update the text of an entry which is currently being edited.
        """
        if store.edit_msg_index is not None and store.chatlog:
            try:
                editmsg = store.chatlog[store.edit_msg_index]
            except IndexError:
                return
            newmsg = add_creation_entry(True, True)
            editmsg.what = newmsg.what
            store.chatlog.insert(store.edit_msg_index, editmsg)
            store.chatlog.remove(editmsg)
        return

    def add_bubble(bubble_info, is_edit=False):
        """
        Add a special bubble to this entry. May also replace an existing
        entry with an updated one that includes the bubble.
        """
        if is_edit:
            entry = store.chatlog.pop(store.edit_msg_index)
        else:
            entry = add_creation_entry(True, is_edit)

        entry.img = False
        entry.bounce = False
        entry.specBubble = None
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

        if is_edit:
            # Replace the edit entry with this new one
            store.chatlog.insert(store.edit_msg_index,
                ChatEntry(entry.who, entry.what, entry.thetime,
                    entry.img, entry.bounce, entry.specBubble))
        else:
            if store.insert_msg_index == -1:
                store.chatlog.append(entry)
                store.yadj.value = store.yadjValue
            else:
                store.chatlog.insert(store.insert_msg_index, entry)
                store.insert_msg_index += 1

        # Reset the bubble dict
        store.bubble_info = {
            'size' : None,
            'bounce' : False,
            'bubble' : None
        }
        store.edit_bubble_info = {
            'size' : None,
            'bounce' : False,
            'bubble' : None
        }

        record_chatlog()

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
        """
        Update the speaker of a message already in the chatlog.
        """
        the_msg = store.chatlog[ind]
        if chara == store.m:
            # Remove special bubbles
            new_specBubble = None
            new_bounce = False
        else:
            new_specBubble = the_msg.specBubble
            new_bounce = the_msg.bounce
        new_entry = ChatEntry(chara, the_msg.what, the_msg.thetime,
            the_msg.img, new_bounce, new_specBubble)
        store.chatlog.insert(ind, new_entry)
        chatlog.remove(the_msg)
        record_chatlog()
        return

    def update_chat_entry():
        """
        Replace a chat entry to update its information.
        """
        new_entry = add_creation_entry(True, True)
        the_msg = store.chatlog[store.edit_msg_index]
        store.chatlog.insert(store.edit_msg_index, new_entry)
        store.chatlog.remove(the_msg)
        return

    def play_chatlog():
        """
        Convert the chatlog into a replay log to play through
        the replay system.
        """

        store.current_timeline_item = ChatRoom("Creation",
            'replay_chat_creator', '00:00', participants=store.cc_participants)

        #bg_entry = ('background', store.current_background)
        #store.current_timeline_item.replay_log.append(bg_entry)
        if cc_cracked_overlay:
            crack_entry = ("overlay", "screen_crack")
            store.current_timeline_item.replay_log.append(crack_entry)

        store.saved_chatlog = store.chatlog
        store.saved_background = (store.current_background, store.cc_cracked_overlay)

        for entry in store.chatlog:
            if entry.for_replay:
                store.current_timeline_item.replay_log.append(entry.for_replay)
            elif entry.who == store.filler:
                pass # Don't want to bother with filler
            else:
                store.current_timeline_item.replay_log.append(
                    ReplayEntry(who=entry.who, what=entry.what, pauseVal=None,
                        img=entry.img, bounce=entry.bounce,
                        specBubble=entry.specBubble)
                )

    def chatroom_to_code():
        """
        Convert the current chatlog into program-compatible code.
        """

        try:
            # Put together the path where the file is
            out_gamedir = renpy.config.gamedir
            filepath = os.path.join( out_gamedir, "generated")
            ret, file_name = convert_chatlog()
            filepath = os.path.join( filepath, file_name + ".rpy")
            # Open the file and print to it
            f = open(filepath, "a")
            print(ret, file=f)
            f.close()
        except Exception as e:
            # Tell the user print to file didn't work
            print("Print to file did not work:", e)
            renpy.notify("WARNING: Print to file didn't work:" + e)
            return
        renpy.notify("Code saved at game/generated/" + file_name + ".rpy")
        return


    def add_replay_direction(text, entry, at_beginning=False, reverse=False):
        """
        Adds an instruction for the replay, such as setting the music.
        """

        if reverse and entry[1] == 'regular':
            entry = ('hack', 'reverse')
            text += " (reversed)"
        elif reverse and entry[1] == 'red':
            entry = ('hack', "red_reverse")
            text += " (reversed)"
        elif reverse and entry[1] == "red_static":
            entry = ('hack', 'red_static_reverse')
            text += " (reversed)"

        if not at_beginning:
            if store.insert_msg_index == -1:
                store.chatlog.append(
                    ChatEntry(store.special_msg, text, upTime(),
                        for_replay=entry)
                )
            else:
                store.chatlog.insert(store.insert_msg_index,
                    ChatEntry(store.special_msg, text, upTime(),
                            for_replay=entry)
                )
                store.insert_msg_index += 1
        else:
            store.chatlog.insert(0,
                ChatEntry(store.special_msg, text, upTime(),
                    for_replay=entry)
            )
        record_chatlog()
        return


default is_main_menu_replay = False
default in_chat_creator = False
# Save the chatlog before a replay to restore it
default saved_chatlog = [ ]
## Label which begins the chatroom creator! It operates a bit
## like a game within a game.
label start_chatroom_creator():
    if len(renpy.get_return_stack()) > 0:
        $ renpy.pop_call()
    # Set this up so we know we're in the chatroom creator
    $ in_chat_creator = True
    $ renpy.retain_after_load()
    # Prompt the player for a chatroom name
    call get_input('save_name', prompt='Enter a title for this chatroom',
        default='Chat 1', length=25, accept_blank=False,
        show_answer=False, can_close=False)
    $ renpy.retain_after_load()
    jump main_chatroom_creator

label main_chatroom_creator():
    $ renpy.retain_after_load()
    call screen chatroom_creator
    $ renpy.retain_after_load()
    if is_main_menu_replay:
        call screen save_and_exit()
        call screen signature_screen(True)
        jump chatroom_creator_setup
    jump main_chatroom_creator


## Clean up the screens before returning to the chatroom creator
label chatroom_creator_setup():
    $ reset_story_vars()
    $ chatlog = saved_chatlog
    $ current_background, cc_cracked_overlay = saved_background
    $ is_main_menu_replay = False
    $ store.chatlog = store.saved_chatlog
    $ renpy.retain_after_load()
    jump main_chatroom_creator


default cc_participants = [ ]
default edit_dialogue = ""
default edit_dialogue_input = InputDialogue('edit_dialogue', edit_action=True)
default edit_msg = None
default edit_msg_index = -1
default insert_msg_index = -1
default edit_mode = True
default chat_dialogue = ""
default emoji_speaker = s
default bubble_user = s
default bubble_info = {
    'size' : None,
    'bounce' : False,
    'bubble' : None
}
default edit_bubble_info = {
    'size' : None,
    'bounce' : False,
    'bubble' : None
}
default the_entry = ChatEntry(s, "None", upTime())
default chat_dialogue_input = InputDialogue('chat_dialogue')
default undo_list = [ ]
default redo_list = [ ]
default chatlog_copy = [ ]
default saved_background = "morning"
define creator_messenger_ysize = 640
# Styles which are applied to a fresh entry
default entry_styles = {
    'font' : gui.sans_serif_1,
    'specBubble' : None,
    'img' : False,
    'size' : 0,
    'bold' : False,
    'italics' : False,
    'underline' : False
}
# Styles which are applied to an edited entry
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
            action SetScreenVariable('active_tab', 'Other')

screen chatroom_creator():

    default active_tab = "Dialogue"
    default show_fonts = False

    tag menu
    use starry_night()
    add Transform('bg ' + current_background,
            crop=(0, 315, 750, creator_messenger_ysize)):
        yoffset 150
    if cc_cracked_overlay:
        add Transform('screen_crack',
                crop=(0, 315, 750, creator_messenger_ysize)):
            yoffset 150
    use menu_header("Chat Creator", MainMenu(),
            hide_bkgr=True):
        use messenger_screen()
        use chat_creator_tabs(active_tab)
        if active_tab == "Dialogue":
            use dialogue_tab(show_fonts)
        elif active_tab == "Effects":
            use effects_tab()
        elif active_tab == "Other":
            use other_cc_tab()

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
    default styles_dict = entry_styles if not compact_ver else edit_styles
    hbox:
        button:
            style_prefix 'font_options'
            xysize (320, 47)
            add "#000"
            action If(compact_ver, Show('pick_speaker', msg_ind=edit_msg_index),
                Show('pick_speaker'))
            hbox:
                xoffset 6
                text "Speaker:"
                if compact_ver:
                    text chatlog[edit_msg_index].who.name size 27
                else:
                    text the_entry.who.name size 27
        if not compact_ver:
            use add_enter_exit_msg()
    # if compact_ver:
    #     hbox:
    #         use add_enter_exit_msg()
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
            action [ToggleDict(styles_dict, 'bold'),
                If(compact_ver, Function(update_edit_text))]

        button:
            add "#000"
            text "I" italic True
            action [ToggleDict(styles_dict, 'italics'),
                If(compact_ver, Function(update_edit_text))]
        button:
            add "#000"
            action [ToggleDict(styles_dict, 'underline'),
                If(compact_ver, Function(update_edit_text))]
            vbox:
                text "U" underline True
                add Solid("#fff") size (30, 1) xalign 0.5
        button:
            xsize 67
            insensitive_foreground "#5555"
            add "#000"
            add 'text_size_decrease'
            sensitive styles_dict['size'] >= -5 # allow two size decreases
            selected styles_dict['size'] < 0
            action [SetDict(styles_dict, 'size', styles_dict['size']-5),
                If(compact_ver, Function(update_edit_text))]
        button:
            xsize 67
            insensitive_foreground "#ccc5"
            add "#000"
            add 'text_size_increase'
            sensitive styles_dict['size'] < 50
            selected styles_dict['size'] > 0
            action [SetDict(styles_dict, 'size', styles_dict['size']+5),
                If(compact_ver, Function(update_edit_text))]
        button:
            xsize 67
            add "#000"
            add 'text_size_reset'
            sensitive styles_dict['size'] != 0
            action [SetDict(styles_dict, 'size', 0),
                If(compact_ver, Function(update_edit_text))]
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
                action [SetDict(styles_dict, 'font', gui.sans_serif_1),
                    If(compact_ver, Function(update_edit_text))]
            button:
                add "#000"
                text "Font 2" font gui.sans_serif_2
                action [SetDict(styles_dict, 'font', gui.sans_serif_2),
                    If(compact_ver, Function(update_edit_text))]
            button:
                add "#000"
                text "Font 3" font gui.serif_1
                action [SetDict(styles_dict, 'font', gui.serif_1),
                    If(compact_ver, Function(update_edit_text))]
            button:
                add "#000"
                text "Font 4" font gui.serif_2
                action [SetDict(styles_dict, 'font', gui.serif_2),
                    If(compact_ver, Function(update_edit_text))]
            button:
                add "#000"
                text "Font 5" font gui.curly_font size 29+5
                action [SetDict(styles_dict, 'font', gui.curly_font),
                    If(compact_ver, Function(update_edit_text))]
            button:
                add "#000"
                text "Font 6" font gui.blocky_font
                action [SetDict(styles_dict, 'font', gui.blocky_font),
                    If(compact_ver, Function(update_edit_text))]


    use dialogue_input(compact_ver)
    hbox:
        spacing 40 xalign 0.5
        if compact_ver:
            xsize 680
        if not compact_ver:
            textbutton "Clear Chat":
                selected False
                action CConfirm("Are you sure you want to clear the chat?",
                    [AddToSet(undo_list, chatlog),
                    SetVariable('chatlog', [ ])])
            textbutton "Undo":
                sensitive undo_list
                action Function(undo_chatlog)
            textbutton "Redo":
                sensitive redo_list
                action Function(redo_chatlog)
            textbutton "Add to Chat":
                action [chat_dialogue_input.Disable(),
                    Function(add_creation_entry),
                    Function(chat_dialogue_input.set_text, ''),
                    SetVariable('redo_list', [ ])]
        else:
            textbutton "Update":
                xalign 0.5
                action [edit_dialogue_input.Disable(),
                    Function(update_chat_entry),
                    Function(record_chatlog),
                    Function(edit_dialogue_input.set_text, ''),
                    SetVariable('edit_msg_index', -1),
                    Hide('dialogue_edit_popup')]

style font_options_button:
    background "#fff"
    selected_background "#5beec8"
    insensitive_foreground "#0003"
    xysize (47, 47)
    padding (2, 2)

style font_options_text:
    align (0.5, 0.5)
    color "#fff"
    insensitive_color "#bbb"

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
default cc_cracked_overlay = False

screen other_cc_tab():
    null height 30
    hbox:
        spacing 50
        align (0.5, 0.0)
        textbutton "Select Background":
            style_prefix 'other_settings_end'
            action Show('select_background')
        textbutton "Add Music":
            style_prefix 'other_settings_end'
            action Show("select_music")
    null height 20
    hbox:
        spacing 12
        xalign 0.5
        textbutton "Add Participants":
            style_prefix 'other_settings_end'
            action Show("select_participants")
        textbutton "Play Chat":
            style_prefix 'other_settings_end'
            action [Function(play_chatlog),
                Call('rewatch_chatroom_main_menu')]
        textbutton "Generate Code":
            style_prefix 'other_settings_end'
            action [Function(chatroom_to_code)]
    null height 35
    hbox:
        spacing 20
        xalign 0.5
        xysize (161*2, 70)
        # Save / Load
        imagebutton:
            style_prefix None
            xysize (161, 70)
            align (.5, .5)
            idle Transform("save_btn", align=(0.5, 0.5))
            hover Transform("save_btn", zoom=1.1)
            action Show("save", Dissolve(0.5))
        button:
            style_prefix 'tone_selection'
            vbox:
                align (0.5, 0.5)
                text "Rename Chat" style 'ringtone_change'
                text "[save_name]":
                    style 'ringtone_description'
            action Show('input_template', None,
                'save_name', prompt='Enter a chatroom title',
                default=save_name, length=25,
                allow=allowed_username_chars, accept_blank=False,
                can_close=False)
        imagebutton:
            style_prefix None
            xysize (161, 70)
            align (.5, .5)
            idle Transform("load_btn", align=(0.5, 0.5))
            hover Transform("load_btn", zoom=1.1)
            action Show("load", Dissolve(0.5))

screen effects_tab():
    null height 30
    hbox:
        spacing 50
        align (0.5, 0.0)
        textbutton "Add Emote":
            style_prefix "other_settings_end"
            action Show('select_emote')
        textbutton "Special Bubbles":
            style_prefix "other_settings_end"
            action Show('select_bubble')
    null height 20
    hbox:
        spacing 50
        align (0.5, 1.0)
        textbutton "Add Shake":
            style_prefix 'other_settings_end'
            action Function(add_replay_direction,
                text="Effect: Screen shake",
                entry=("shake", current_background))
        textbutton "Add Animations":
            style_prefix 'other_settings_end'
            action Show('select_anim')

screen select_anim():
    zorder 100
    modal True

    default anim_msg = ""
    default anim_entry = None
    default anim_reverse = False

    frame:
        maximum(680, 1000)
        background 'input_popup_bkgr'
        xalign 0.5
        yalign 0.6
        imagebutton:
            align (1.0, 0.0)
            idle 'input_close'
            hover 'input_close_hover'
            action Hide('select_anim')
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.6
            null height 10
            frame:
                xysize (630,760)
                xalign 0.5
                background 'input_square' padding(40,40)
                vpgrid:
                    mousewheel True
                    xysize (590,740)
                    align (0.5, 0.5)
                    cols 2
                    spacing 10
                    imagebutton:
                        idle 'hack scroll'
                        hover_foreground "#fff5"
                        selected_foreground "#fff3"
                        at hack_transform()
                        action [SetScreenVariable('anim_msg',
                                "Effect: Green hack scroll"),
                            SetScreenVariable('anim_entry',
                                ('hack', 'regular'))]
                    imagebutton:
                        idle 'redhack scroll'
                        hover_foreground "#fff5"
                        selected_foreground "#fff3"
                        at hack_transform()
                        action [SetScreenVariable('anim_msg',
                                "Effect: Red hack scroll"),
                            SetScreenVariable('anim_entry',
                                ('hack', 'red'))]
                    imagebutton:
                        idle Transform('red_static_background',
                            crop=(0, 200, 750, 1000))
                        hover_foreground "#fff5"
                        selected_foreground "#fff3"
                        at transform:
                            zoom 0.3
                        action [SetScreenVariable('anim_msg',
                                "Effect: Red static scroll"),
                            SetScreenVariable('anim_entry',
                                ('hack', 'red_static'))]
                    imagebutton:
                        idle Transform('secure_chat_intro',
                            crop=(80, 200, 750, 1000))
                        hover_foreground "#fff5"
                        selected_foreground "#fff3"
                        at transform:
                            zoom 0.3
                        action [SetScreenVariable('anim_msg',
                                "Animation: Secure Chat"),
                            SetScreenVariable('anim_entry',
                                ('anim', 'secure_anim'))]


            if anim_entry and anim_entry[0] == 'hack':
                textbutton "Reverse Animation":
                    style_prefix 'check'
                    action ToggleScreenVariable('anim_reverse')


            textbutton _('Confirm'):
                text_style 'mode_select'
                style 'cc_confirm_style'
                action [Hide('select_anim'),
                    Function(add_replay_direction,
                        anim_msg, anim_entry, reverse=anim_reverse)]

transform hack_transform(end=0.35):
    zoom 0.3
    crop_relative True
    crop (0.0, 0.0, 1.0, end)

init python:
    def get_readable_music():
        """Return a human-readable music list, sorted."""
        the_list = store.music_dictionary.keys()
        new_list = [ ]
        for item in the_list:
            new_item = item.split('audio/music/')[-1]
            new_item = '.'.join(new_item.split('.')[:-1])
            # Remove any digits at the start of the name
            new_item = regex.sub("^[0-9]+ ", "", new_item)
            new_list.append((new_item, item))
        new_list = sorted(new_list, key=lambda x: x[0])
        return new_list

init 10:
    define readable_music = get_readable_music()

screen select_music():
    zorder 100
    modal True

    default temp_music = None
    default temp_path = None
    default at_beginning = False

    frame:
        maximum(680, 1000)
        background 'input_popup_bkgr'
        xalign 0.5
        yalign 0.6
        imagebutton:
            align (1.0, 0.0)
            idle 'input_close'
            hover 'input_close_hover'
            action Hide('select_music')
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.6
            null height 10
            frame:
                xysize (630,760)
                xalign 0.5
                background 'input_square' padding(40,40)
                vpgrid:
                    mousewheel True
                    xysize (590,740)
                    align (0.5, 0.5)
                    cols 1
                    spacing 10
                    for song, path in readable_music:
                        textbutton song:
                            yalign 0.5 xysize (590, 80)
                            selected_background "#ccc"
                            sensitive True selected temp_music == song
                            action [SetScreenVariable('temp_music', song),
                                SetScreenVariable('temp_path', path),
                                Play('music', path)]

            textbutton "Add to the beginning of the chat":
                style_prefix 'check'
                action ToggleScreenVariable('at_beginning')


            textbutton _('Confirm'):
                text_style 'mode_select'
                style 'cc_confirm_style'
                action [Function(add_replay_direction,
                        'Play Music: ' + str(temp_music),
                        ('play music', temp_path),
                        at_beginning),
                    Hide('select_music')]#Play('music', mystic_chat),

screen select_background():
    zorder 100
    modal True

    default temp_bg = current_background
    default at_beginning = False

    frame:
        maximum(680, 1000)
        background 'input_popup_bkgr'
        xalign 0.5
        yalign 0.6
        imagebutton:
            align (1.0, 0.0)
            idle 'input_close'
            hover 'input_close_hover'
            action Hide('select_background')
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.6
            null height 10
            frame:
                xysize (630,760)
                xalign 0.5
                background 'input_square' padding(40,40)
                vpgrid:
                    mousewheel True
                    xysize (590,740)
                    align (0.5, 0.5)
                    cols 3
                    spacing 10
                    for ccbg in all_static_backgrounds:
                        python:
                            try:
                                ccbg2 = renpy.get_registered_image('bg ' + ccbg).child
                                try:
                                    ccbg2 = ccbg2.child
                                except:
                                    pass
                            except:
                                ccbg2 = 'bg ' + ccbg

                        button:
                            xysize (187, 333)
                            selected_foreground "#fff3"
                            add ccbg2:
                                size (187, 333)
                            action SetScreenVariable('temp_bg', ccbg)
            textbutton "Use cracked overlay":
                style_prefix 'check'
                action ToggleVariable('cc_cracked_overlay')

            textbutton "Add to the beginning of the chat":
                style_prefix 'check'
                action ToggleScreenVariable('at_beginning')


            textbutton _('Confirm'):
                text_style 'mode_select'
                style 'cc_confirm_style'
                action [Function(add_replay_direction, 'Background: ' + temp_bg,
                    ('background', temp_bg), at_beginning=at_beginning),
                    ## Cracked background?
                    SetVariable('current_background', temp_bg),
                    If(temp_bg in black_text_bgs,
                        SetVariable('nickColour', black),
                        SetVariable('nickColour', white)),
                    Hide('select_background')]

screen select_participants():
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
            action Hide('select_participants')
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.6
            null height 10
            frame:
                xysize (630,760)
                xalign 0.5
                background "#000a"
                padding(40,40)
                vpgrid:
                    mousewheel True
                    xysize (590,740)
                    align (0.5, 0.5)
                    cols 1
                    spacing 10
                    for who in all_characters:
                        if who.name:
                            textbutton who.name:
                                style_prefix 'check'
                                action ToggleSetMembership(cc_participants,
                                    who)

            textbutton _('Confirm'):
                text_style 'mode_select'
                style 'cc_confirm_style'
                action [Hide('select_participants')]

screen select_emote(edit=False):

    zorder 100
    modal True

    default selected_emote = None

    frame:
        style_prefix 'emote_select'
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
                style 'cc_confirm_style'
                text_style 'mode_select'
                action [Function(add_emote, selected_emote, edit=edit),
                    If(not edit and insert_msg_index == -1,
                        SetField(yadj, 'value', yadjValue)),
                    Hide('select_emote')]

style cc_confirm_style:
    xalign 0.5
    xsize 240
    ysize 80
    background 'menu_select_btn'
    hover_background 'menu_select_btn_hover'
    padding (20, 20)


screen select_bubble(editing=False):

    if editing:
        default bubble_dict = bubble_info
        default bubble_who = chatlog[edit_msg_index].who
    else:
        default bubble_dict = edit_bubble_info
        default bubble_who = the_entry.who

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
                    if bubble_user is bubble_who:
                        button:
                            xysize (580//2, 220)
                            hover_background '#e0e0e0'
                            selected_background '#a8a8a8'
                            selected not bubble_dict['bounce']
                            action [SetDict(bubble_dict, 'size', None),
                                SetDict(bubble_dict, 'bubble', None),
                                SetDict(bubble_dict, 'bounce', False)]
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
                                selected (bubble_dict['bounce']
                                    and bubble_dict['bubble'] is None)
                                action [SetDict(bubble_dict, 'size', None),
                                    SetDict(bubble_dict, 'bubble', None),
                                    SetDict(bubble_dict, 'bounce', True)]
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
                            selected (bubble_dict['bubble'] == bub)
                            if "glow" not in bub:
                                action [Show('pick_bubble_size',
                                    bubble_sizes=find_bubble_sizes(bub),
                                    editing=True),
                                    SetDict(bubble_dict, 'bubble', bub),
                                    SetDict(bubble_dict, 'bounce', True)]
                                add Transform(bub, zoom=0.46) align (0.5, 0.5)
                            else:
                                action [SetDict(bubble_dict, 'size', None),
                                    SetDict(bubble_dict, 'bubble', bub),
                                    SetDict(bubble_dict, 'bounce', True)]
                                frame:
                                    background Frame(bub, 25, 25)
                                    align (0.5, 0.5)
                                    style 'glow_bubble'
                                    add Null(height=100, width=150)

            textbutton _('Confirm'):
                text_style 'mode_select'
                style 'cc_confirm_style'
                action If(not editing,
                    [chat_dialogue_input.Disable(),
                    Function(add_bubble, bubble_dict),
                    Function(chat_dialogue_input.set_text, ''),
                    SetVariable('redo_list', [ ]),
                    Hide('select_bubble')],
                    [Function(add_bubble, bubble_dict, is_edit=True),
                    Hide('select_bubble')])





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
        if compact_ver:
            xalign 0.0
        else:
            xalign 0.5
        yalign 0.4
        viewport:
            yadjustment text_input_yadj
            xysize (730-28, 180-20)
            mousewheel True
            input value the_input:
                allow allowed_username_chars
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
                    if msg_ind is not None and active_tab == "Edit":
                        action [Function(update_speaker, msg_ind, chara),
                            SetVariable('edit_msg_index', -1),
                            Hide('pick_speaker'), Hide('edit_msg_menu')]
                    elif msg_ind is not None:
                        action [Function(update_speaker, msg_ind, chara),
                            Hide('pick_speaker')]
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


screen pick_bubble_size(bubble_sizes, editing=False):
    default pos = renpy.get_mouse_pos()
    if editing:
        default bubble_dict = bubble_info
    else:
        default bubble_dict = edit_bubble_info

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
                action [SetDict(bubble_dict, 'size', sz),
                    Hide('pick_bubble_size')]

screen edit_msg_menu(msg, ind):
    default pos = renpy.get_mouse_pos()
    default too_wide = (pos[0] + 300) > config.screen_width
    default speaker_pos = (pos[0], pos[1]+(175//2)) if not too_wide else (pos[0]-300, pos[1]+(175//2))
    default filter_what = renpy.filter_text_tags(msg.what, allow=['b', 'image'])
    default edit_item = "text" if not msg.img else "emoji"
    zorder 50
    button:
        xysize (config.screen_width, config.screen_height)
        background None
        action [SetVariable('edit_msg_index', -1), Hide('edit_msg_menu')]
    frame:
        at yzoom_in()
        background "#000"
        xsize 300
        #ymaximum 250
        pos pos
        if too_wide:
            anchor (1.0, 0.5)
        else:
            anchor (0.0, 0.5)
        has vbox
        textbutton "Remove message":
            text_color "#fff"
            action CConfirm(("Are you sure you want to delete the message \""
                + filter_what + "\"?"), [RemoveFromSet(chatlog, msg),
                Hide('edit_msg_menu'),
                SetVariable('edit_msg_index', -1)])
        textbutton "Insert message before":
            text_color "#fff"
            action [SetVariable('insert_msg_index', ind),
                Hide('edit_msg_menu')]
        if msg.who != special_msg:
            textbutton "Edit " + edit_item:
                text_color "#fff"
                action If(msg.img,
                    [Hide('edit_msg_menu'),
                    Show('select_emote', edit=True)],
                    [Function(get_styles_from_entry, msg),
                    Hide('edit_msg_menu'),
                    Show('dialogue_edit_popup')])
            if msg.who != m:
                textbutton "Change bubble":
                    text_color "#fff"
                    action [Hide('edit_msg_menu'),
                        Show('select_bubble', editing=True)]

            textbutton "Change speaker":
                text_color "#fff"
                action Show('pick_speaker', active_tab="Edit",
                    msg_ind=ind, pos=speaker_pos, anchor=(0.0, 0.0))

            textbutton "Change profile picture":
                text_color "#fff"
                action [Hide('edit_msg_menu'),
                    If(msg.who == m,
                        Show('pick_mc_pfp'),
                        Show('pick_chara_pfp', who=msg.who))]

screen dialogue_edit_popup():
    modal True

    default show_fonts = False

    frame:
        maximum(680, 600)
        background 'input_popup_bkgr'
        xpadding 20
        xalign 0.5
        yalign 0.85
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



screen chatroom_file_slots(title, current_page=0, num_pages=5, slots_per_column=7,
        begin_page=0):

    on 'show' action FilePage(2)
    on 'replace' action FilePage(2)

    default rows = 7
    default page = 2

    python:
        # Determine the beginning/end values
        begin_range = (current_page*slots_per_column)-1
        end_range = (current_page*slots_per_column)+slots_per_column-1

        end_page = begin_page + num_pages

    fixed:
        xysize (750, 1170)
        yalign 1.0
        ## This ensures the input will get the enter event before any of the
        ## buttons do.
        order_reverse True

        ## The grid of file slots.
        grid 1 rows:
            style_prefix "slot"

            xalign 0.5
            yalign 0.0

            spacing gui.slot_spacing

            for i in range(begin_range, end_range):

                $ slot = i + 1

                button:
                    if title == "Load":
                        action FileLoad(slot, page=page)
                    else:
                        action FileSave(slot, page=page)

                    has hbox
                    xalign 0.0

                    if FileLoadable(slot, page=page):
                        add 'save_auto' align (0.5, 0.5)
                    else:
                        add 'save_empty' align (0.5, 0.5)

                    frame:
                        style_prefix 'save_desc'
                        has vbox
                        # Displays the most recent chatroom title + day
                        if FileLoadable(slot, page=page):
                            fixed:
                                text "Chatroom Creator"
                            text "Title: " + FileSaveName(slot, page=page):
                                yalign 1.0 layout "nobreak"
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
                                    empty=_("empty slot"),
                                    page=page)

                        imagebutton:
                            hover Transform('save_trash',zoom=1.05)
                            idle 'save_trash'
                            xalign 1.0
                            action FileDelete(slot, page=page)

                    key "save_delete" action FileDelete(slot, page=page)

        ## Buttons to access other pages.
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



screen choose_chat_creator():

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        vbox:
            label _("What would you like to do?"):
                style "confirm_prompt"
                xalign 0.5

            vbox:
                textbutton _("Create New Chat"):
                    xsize 300
                    action Start('start_chatroom_creator')
                textbutton _("Load Chat"):
                    xsize 300
                    action [Hide('choose_chat_creator'),
                        Show('load_chat')]
                textbutton _("Cancel"):
                    xsize 300
                    action Hide('choose_chat_creator')

    ## Right-click and escape answer "no".
    key "game_menu" action Hide('choose_chat_creator')

screen load_chat():
    tag save_load
    modal True

    default current_page = 0
    default num_pages = 5
    default slots_per_column = 7
    default begin_page = 0

    use menu_header("Chat Creator Load", Hide('load_chat', Dissolve(0.5)))
    use chatroom_file_slots(_("Load"), current_page, num_pages,
        slots_per_column, begin_page)
