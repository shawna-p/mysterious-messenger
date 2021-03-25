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
            print("updating var to", s)
            setattr(store, self.var, s)
            self.s = s

            store.the_entry.what = s
            if s:
                self.enter(simulate=True)
            #renpy.run(self.Enable())

        def enter(self, simulate=False):
            print("Pressed enter")
            if not simulate:
                renpy.run(self.Disable())
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


default chat_dialogue = ""
default the_entry = ChatEntry(s, "None", upTime())
default chat_dialogue_input = InputDialogue('chat_dialogue')
default last_added = [ ]
define creator_messenger_ysize = 640

screen chatroom_creator():
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
        use dialogue_input()
        hbox:
            spacing 40 xalign 0.5
            textbutton "Clear Chat":
                action [SetVariable('last_added', chatlog),
                    SetVariable('chatlog', [ ])]
            textbutton "Undo":
                sensitive chatlog or (last_added and not chatlog)
                action Function(pop_chatlog)
            textbutton "Redo":
                sensitive last_added
                action Function(redo_chatlog)
            textbutton "Add to chatlog":
                action [chat_dialogue_input.Disable(),
                    #Function(addchat, random.choice(character_list), chat_dialogue, 0),
                    #SetField(the_entry, 'what', chat_dialogue),
                    AddToSet(chatlog, copy(the_entry)),
                    #SetVariable('chat_dialogue', ''),
                    Function(chat_dialogue_input.set_text, ''),
                    SetVariable('last_added', [ ])]



screen dialogue_input():
    button:
        xysize (730, 200)
        background 'input_popup_bkgr'
        padding (12, 10)
        xalign 0.5 yalign 0.4
        input value chat_dialogue_input
        action chat_dialogue_input.Enable()