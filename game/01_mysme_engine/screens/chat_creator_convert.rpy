init python:

    def convert_chatlog():
        """
        Function which converts an existing chatlog into program code
        that can be added to a rpy file and edited.
        """

        code = "label "
        label_name = ('_').join(store.save_name.split(' '))
        # Sanitize the label name (no non-alphanumeric characters)
        #import re, string
        pattern = regex.compile('[\W]+', regex.UNICODE)
        label_name = pattern.sub('', label_name).lower()
        if '0' <= label_name <= '9':
            # label starts with a number; prepend some text
            label_name = 'chat_' + label_name

        code += label_name + "():\n"

        # Check if we need to update any profile pictures
        for chara in store.all_characters:
            if (chara is not store.m and chara.bonus_pfp):
                # It was changed
                if not isinstance(chara.bonus_pfp, basestring):
                    # Can't easily print out Transforms etc
                    code += "    # Note: You may want to update " + chara.name
                    code += "'s profile picture (couldn't not update automatically)\n"
                    continue
                code += "    $ " + chara.file_id + ".prof_pic = \""
                code += chara.bonus_pfp + "\"\n"

        for entry in store.chatlog:
            ## Is it a replay entry?
            if entry.for_replay:
                # There's a replay entry
                code += "    " + parse_replay_entry(entry)
            else:
                if entry.who == store.special_msg:
                    # An enter/exit entry
                    pass
                else:
                    # Turn this into a msg statement
                    code += "    " + get_dialogue_from_entry(entry)
            code += "\n"
        code += "    return"

        code += "\n\n## You can use this label for things like text messages"
        code += "\n## (or get rid of it if you don't need it)"
        code += "\nlabel after_" + label_name + "():\n"
        code += "\n    return"
        code += "\n\n## Similarly, this is the label for the expired version"
        code += "\n## of this chatroom."
        code += "\nlabel " + label_name + "_expired():\n"
        code += "\n    return"
        return code, label_name

    def parse_replay_entry(entry):
        """
        Parse the information in a replay entry to turn it into a line
        of code.
        """

        first = entry.for_replay[0]
        second = entry.for_replay[1]

        if first == "anim":
            # It's the secure screen animation
            return "show secure anim"
        elif first == "overlay":
            return "show screen_crack"
        elif first == "hack":
            if second == "regular":
                return "show hack effect"
            elif second == "reverse":
                return "show hack effect reverse"
            elif second == "red":
                return "show redhack effect"
            elif second == "red_reverse":
                return "show redhack effect reverse"
            elif second == "red_static":
                return "show red static effect"
            elif second == "red_static_reverse":
                return "show red static effect reverse"

        elif first == "play music":
            # We want this to look pretty, so use the
            # "pretty format" dictionary
            return "play music " + music_dictionary_prettify.get(second, second)

        elif first == 'shake':
            return 'show shake'

        elif first == 'enter':
            return 'enter chatroom ' + second.file_id

        elif first == 'exit':
            return 'exit chatroom ' + second.file_id

        elif first == 'background':
            return 'scene ' + second

        elif first == 'banner':
            return 'show banner ' + second

        return '# Could not parse entry: ' + first + ' ' + second


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
        line += '"'
        if entry.img:
            # That's it
            return line
        # Add font
        if style_dict['font'] == gui.serif_1:
            line += ' ser1'

        elif style_dict['font'] == gui.serif_2:
            line += ' ser2'

        elif style_dict['font'] == gui.sans_serif_1:
            # Only add this (the default font) if there's a modifier
            if style_dict['bold']:
                line += ' sser1'

        elif style_dict['font'] == gui.sans_serif_2:
            line += ' sser2'

        elif style_dict['font'] == gui.blocky_font:
            line += ' blocky'
        elif style_dict['font'] == gui.curly_font:
            line += ' curly'

        if style_dict['bold']:
            line += ' xbold'

        # Add 'big'
        if style_dict['big']:
            line += ' big'


        # add special bubble
        if entry.specBubble:
            # Is it a known bubble?
            if entry.specBubble in all_bubbles_list:
                line += ' ' + entry.specBubble
            else:
                line += ' bubble ' + entry.specBubble
        if style_dict['img']:
            line += ' img'

        if not entry.specBubble and entry.bounce:
            line += ' glow'

        return line

init offset = 5
define music_dictionary_prettify = {
    mystic_chat : "mystic_chat",
    mystic_chat2 : "mystic_chat2",
    mysterious_clues : "mysterious_clues",
    urban_night_cityscape : "urban_night_cityscape",
    urban_night_cityscape_v2 : "urban_night_cityscape_v2",
    narcissistic_jazz : "narcissistic_jazz",
    lonely_but_passionate_way : "lonely_but_passionate_way",
    geniusly_hacked_bebop : "geniusly_hacked_bebop",
    same_old_fresh_air : "same_old_fresh_air",
    silly_smile_again : "silly_smile_again",
    lonesome_practicalism : "lonesome_practicalism",
    lonesome_practicalism_v2 : "lonesome_practicalism_v2",
    i_miss_happy_rika : "i_miss_happy_rika",
    dark_secret : "dark_secret",
    life_with_masks : "life_with_masks",
    my_half_is_unknown : "my_half_is_unknown",
    endless_struggle_guitar : "endless_struggle_guitar",
    endless_struggle_harp : "endless_struggle_harp",
    endless_struggle : "endless_struggle",
    four_seasons_piano : "four_seasons_piano",
    i_am_the_strongest_harp : "i_am_the_strongest_harp",
    i_am_the_strongest_piano : "i_am_the_strongest_piano",
    i_am_the_strongest : "i_am_the_strongest",
    i_draw_piano : "i_draw_piano",
    i_draw : "i_draw",
    light_and_daffodils_piano1 : "light_and_daffodils_piano1",
    light_and_daffodils_piano2 : "light_and_daffodils_piano2",
    mint_eye_piano : "mint_eye_piano",
    mint_eye : "mint_eye",
    mysterious_clues_v2 : "mysterious_clues_v2",
    mystic_chat_hacked : "mystic_chat_hacked",
    suns_love_piano : "suns_love_piano",
    suns_love : "suns_love",
    the_compass_piano1 : "the_compass_piano1",
    the_compass_piano2 : "the_compass_piano2",
    xmas_life_with_masks : "xmas_life_with_masks",
    xmas_lonesome_practicalism : "xmas_lonesome_practicalism",
    xmas_narcissistic_jazz : "xmas_narcissistic_jazz",
    xmas_same_old_fresh_air : "xmas_same_old_fresh_air",
    xmas_urban_night_cityscape : "xmas_urban_night_cityscape",
    april_mystic_chat : "april_mystic_chat",
    april_mysterious_clues : "april_mysterious_clues",
    april_dark_secret : "april_dark_secret"
}
init offset = 0