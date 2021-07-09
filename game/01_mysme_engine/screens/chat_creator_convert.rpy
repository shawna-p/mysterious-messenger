init python:

    def convert_chatlog():
        """
        Function which converts an existing chatlog into program code
        that can be added to a rpy file and edited.
        """

        code = ""

        for entry in store.chatlog:
            ## Is it a replay entry?
            if entry.for_replay:
                # There's a replay entry
                # Do stuff
                pass
            else:
                if entry.who == store.special_msg:
                    # An enter/exit entry
                    # Get who it is and what it is
                    pass
                else:
                    # Turn this into a msg statement
                    code += get_dialogue_from_entry(entry)

    def get_dialogue_from_entry(entry):
        """
        A helper function which returns a code line with the appropriate
        arguments equivalent to an entry in the chatlog.
        """

        line = "msg "
        # get the character's variable/name
        line += entry.file_id
        # Add the opening quotes
        line += " \""

        # Get a dictionary of the styles for this dialogue
        style_dict, dialogue = get_styles_from_entry(entry, True)
        # Add the dialogue
        line += dialogue
        # End quote
        line += "\""
        # Add font
        #????????
        # add special bubble
        if style_dict['specBubble']:
            line += ' ' + style_dict['specBubble']
        if style_dict['img']:
            line += ' img'




        # edit_styles = {
        #     'font' : gui.sans_serif_1,
        #     'specBubble' : None,
        #     'img' : False,
        #     'size' : 0,
        #     'bold' : False,
        #     'italics' : False,
        #     'underline' : False
        # }
        return line
