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
            self.enter(simulate=True)
            #renpy.run(self.Enable())

        def enter(self, simulate=False):
            print("Pressed enter")
            if not simulate:
                renpy.run(self.Disable())
            else:
                renpy.run(self.Enable())
            raise renpy.IgnoreEvent()

default chat_dialogue = ""
default the_entry = ChatEntry(s, "None", upTime())
default chat_dialogue_input = InputDialogue('chat_dialogue')

screen chatroom_creator():
    tag menu

    use starry_night()
    use menu_header("Chat Creator", Show('main_menu', Dissolve(0.5))):
        use messenger_screen()
        textbutton "Add to chatlog":
            action [chat_dialogue_input.Disable(),#Function(chat_dialogue_input.enter),
                Function(print, 'chat_dialogue is', chat_dialogue,
                    'inputdialogue is', chat_dialogue_input.s, 'ugh',
                    chat_dialogue_input.get_text()),
                Function(addchat, random.choice(character_list),
                chat_dialogue, 0)]
        use dialogue_input()


screen dialogue_input():
    button:
        xysize (730, 200)
        background 'input_popup_bkgr'
        padding (12, 10)
        xalign 0.5 yalign 0.4
        input value chat_dialogue_input
        #if not chat_dialogue_input.editable:
        action chat_dialogue_input.Enable()