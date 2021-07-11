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
        line += entry.who.file_id
        # Add the opening quotes
        line += ' "'

        # Get a dictionary of the styles for this dialogue
        style_dict, dialogue = get_styles_from_entry(entry, True)
        # Is size 10 and font not curly?
        if style_dict['size'] == 10 and style_dict['font'] != gui.curly_font:
            style_dict['big'] = True
        elif style_dict['font'] == gui.curly_font and style_dict['size'] == 20:
            style_dict['big'] = True
        else:
            style_dict['big'] = False

        # Otherwise, if it's not big, we'll need to be more specific
        # with the size arguments
        if style_dict['big']:
            dialogue = renpy.filter_text_tags(entry.what,
                deny=['size', 'font'])
        else:
            dialogue = renpy.filter_text_tags(entry.what,
                deny=['font'])

        if style_dict['font'] == gui.curly_font and style_dict['size'] in (5, 6):
            style_dict['size'] = 0
            dialogue = renpy.filter_text_tags(dialogue, deny='size')

        # Check if we need to filter out {b} tags
        if style_dict['bold'] and style_dict['font'] not in [gui.blocky_font,
                gui.curly_font]:
            # Can filter out {b}
            dialogue = renpy.filter_text_tags(dialogue, deny=['b'])
        else:
            style_dict['bold'] = False

        # Add the dialogue
        line += dialogue
        # End quote
        line += ' "'
        # Add font
        if style_dict['font'] == gui.serif_1 and style_dict['bold']:
            line += ' ser1xb'
        elif style_dict['font'] == gui.serif_1:
            line += ' ser1'

        elif style_dict['font'] == gui.serif_2 and style_dict['bold']:
            line += ' ser2xb'
        elif style_dict['font'] == gui.serif_2:
            line += ' ser2'

        elif style_dict['font'] == gui.sans_serif_1 and style_dict['bold']:
            line += ' sser1xb'
        elif style_dict['font'] == gui.sans_serif_1:
            line += ' sser1'

        elif style_dict['font'] == gui.sans_serif_2 and style_dict['bold']:
            line += ' sser2xb'
        elif style_dict['font'] == gui.sans_serif_2:
            line += ' sser2'

        elif style_dict['font'] == gui.blocky_font:
            line += ' blocky'
        elif style_dict['font'] == gui.curly_font:
            line += ' curly'

        # Add 'big'
        if style_dict['big']:
            line += ' big'


        # add special bubble
        if entry.specBubble:
            line += ' ' + entry.specBubble
        if style_dict['img']:
            line += ' img'

        if not entry.specBubble and entry.bounce:
            line += ' glow'



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
