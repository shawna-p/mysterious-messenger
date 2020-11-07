python early hide:

    ########################################
    ## ENTER AND EXIT CHATROOM CDS
    ########################################

    def parse_enter_exit(l):
        who = l.simple_expression()
        if not who:
            renpy.error("chatroom enter/exit requires a character.")
        return who

    def execute_enter_chat(d_who):
        if d_who is not None:
            who = eval(d_who)
        else:
            renpy.error("enter chatroom requires a ChatCharacter")

        if who is None or not isinstance(who, ChatCharacter):
            print("WARNING: variable %s provided to enter chatroom is not recognized as a ChatCharacter." % d_who)
            renpy.show_screen('script_error',
                message="Variable %s provided to enter chatroom is not recognized as a ChatCharacter.",
                link="Useful-Chatroom-Functions#how-to-make-a-character-enterexit-the-chatroom",
                link_text="How to make a character enter/exit the chatroom")
            return

        if (not store.dialogue_paraphrase and store.dialogue_picked != ""):
            say_choice_caption(store.dialogue_picked,
                store.dialogue_paraphrase, store.dialogue_pv)

        enter_string = who.name + " has entered the chatroom."
        if (not store.observing and not store.persistent.testing_mode
                and not store.vn_choice
                and renpy.get_screen('phone_overlay')):
            # Add this as a replay entry
            enter_entry = ("enter", who)
            store.current_timeline_item.replay_log.append(enter_entry)

        addchat(store.special_msg, enter_string, store.enter_exit_modifier)
        if who.name not in store.in_chat:
            store.in_chat.append(who.name)

        if not store.observing:
            store.current_timeline_item.add_participant(who)

        # Refresh the screen
        renpy.restart_interaction()
        return

    def execute_exit_chat(d_who):
        if d_who is not None:
            who = eval(d_who)
        else:
            renpy.error("exit chatroom requires a ChatCharacter")

        if who is None or not isinstance(who, ChatCharacter):
            print("WARNING: variable %s provided to exit chatroom is not recognized as a ChatCharacter." % d_who)
            renpy.show_screen('script_error',
                message="Variable %s provided to exit chatroom is not recognized as a ChatCharacter.",
                link="Useful-Chatroom-Functions#how-to-make-a-character-enterexit-the-chatroom",
                link_text="How to make a character enter/exit the chatroom")
            return

        if (not store.dialogue_paraphrase and store.dialogue_picked != ""):
            say_choice_caption(store.dialogue_picked,
                store.dialogue_paraphrase, store.dialogue_pv)

        exit_string = who.name + " has left the chatroom."
        if (not store.observing and not store.persistent.testing_mode
                and not store.vn_choice
                and renpy.get_screen('phone_overlay')):
            # Add this as a replay entry
            exit_entry = ("exit", who)
            store.current_timeline_item.replay_log.append(exit_entry)

        addchat(store.special_msg, exit_string, store.enter_exit_modifier)
        if who.name in store.in_chat:
            store.in_chat.remove(who.name)

        # Refresh the screen
        renpy.restart_interaction()
        return

    def lint_enter_exit(who):
        eval_who = None
        try:
            eval_who = eval(who)
        except:
            renpy.error("enter and exit functions require a ChatCharacter")

        if eval_who is None:
            renpy.error("The person entering or exiting the chatroom to cannot be None.")

        if not isinstance(eval_who, ChatCharacter):
            renpy.error("%s is not recognized as a ChatCharacter object for entering or exiting chatrooms." % p["who"])
        return

    def predict_enter_exit(p):
        return [ ]
    def warp_enter_exit(p):
        return True

    renpy.register_statement('enter chatroom',
        parse=parse_enter_exit,
        execute=execute_enter_chat,
        predict=predict_enter_exit,
        lint=lint_enter_exit,
        warp=warp_enter_exit)

    renpy.register_statement('exit chatroom',
        parse=parse_enter_exit,
        execute=execute_exit_chat,
        predict=predict_enter_exit,
        lint=lint_enter_exit,
        warp=warp_enter_exit)

    ########################################
    ## MSG AND BACKLOG CDS
    ########################################
    def parse_message_args(what, ffont, bold, xbold, big, img, spec_bubble,
            is_text_msg=False):
        """
        Parse the arguments for a message and add them to the dialogue if
        applicable. Also check for errors in ffont and spec_bubble.

        Parameters:
        -----------
        what : string
            The dialogue being sent.
        ffont : string
            The font that should be used.
        bold: bool
            True if this text is bold.
        xbold : bool
            True if this text is extra bold.
        big : bool
            True if the size of this text should be increased.
        img : bool
            True if this message contains an image.
        spec_bubble : string
            Contains the name of the special bubble.

        Returns:
        --------
        tuple of dialogue, img, spec_bubble
            After evaluating `what` and the arguments, returns `dialogue` which
            contains the correct text tags for font and size, as well as img
            and spec_bubble, as they may have been corrected.
        """

        # Ensure the font is known
        if not ffont in store.all_fonts_list:
            print("WARNING: The font %s for dialogue \"" + what + "\" could "
                + "not be evaluated." % ffont)
            renpy.show_screen('script_error',
                    message=("The font %s for dialogue \"" + what + "\" could "
                        + "not be evaluated." % ffont))
            # Use the default font instead
            ffont = 'sser1'

        # Ensure the special bubble is known
        if spec_bubble and not spec_bubble in store.all_bubbles_list:
            print("WARNING: The special bubble %s for dialogue \"" + what
                + "\" could not be evaluated." % spec_bubble)
            renpy.show_screen('script_error',
                    message=("The special bubble %s for dialogue \"" + what
                        + "\" could not be evaluated." % spec_bubble))
            # Don't use a special bubble
            spec_bubble = None

        # Construct the actual "what" statement
        dialogue = what
        # First, the size
        if big and (not is_text_msg or ffont != 'curly'):
            dialogue = "{size=+10}" + dialogue + "{/size}"

        # Next, construct the font
        d_font = ffont
        extra_item = False
        if bold and ffont in store.bold_xbold_fonts_list:
            d_font = d_font + 'b'
        elif xbold and ffont in store.bold_xbold_fonts_list:
            d_font = d_font + 'xb'
        elif (bold or xbold):
            extra_item = 'b'

        if ((is_text_msg and ffont in store.font_dict)
                or ffont not in ['sser1', 'sser2', 'ser1', 'ser2', 'curly',
                'blocky']):
            # Can construct this for text messages
            if ffont == 'curly' and big:
                dialogue = "{size=+20}" + dialogue + "{/size}"
            elif ffont == 'curly':
                dialogue = "{size=+6}" + dialogue + "{/size}"
            if ffont != 'sser1':
                dialogue = ("{font=" + store.font_dict[d_font] + "}"
                    + dialogue + "{/font}")
        else:
            # Add the font around the dialogue, unless it's the default
            if d_font != 'sser1':
                dialogue = "{=" + d_font + "}" + dialogue + "{/=" + d_font + "}"

        if extra_item:
            dialogue = ("{" + extra_item + "}" + dialogue + "{/"
                + extra_item + "}")

        # There is a special bubble; check if need to correct it
        if (spec_bubble and spec_bubble[:7] == "round"
                and (who.file_id == 'r' or who.file_id == 'z')):
            # Correct this to the new 'flower' variant if applicable
            spec_bubble = "flower_" + spec_bubble[-1:]

        if what in store.emoji_lookup:
            # Automatically set img to True
            img = True

        return dialogue, img, spec_bubble

    def parse_sub_block(l, messages=None, check_time=False, is_text_msg=False):
        """
        Parse l for messages or conditional python statements. If a sub-block
        is discovered, this function recursively calls itself to parse the
        whole statement.

        Parameters:
        -----------
        l : Lexer
            The lexer that is parsing the block.
        messages : list of dict, string, list
            Contains dictionaries corresponding to messages as well as strings
            corresponding to statements like the pause and label statements.
            May contain a list of (condition, block) tuples corresponding to
            a conditional statement.
        check_time : bool
            True if the program should check for a `time` keyword after the
            message body, indicating when the message should be sent.
        is_text_msg : bool
            Indicates the program should check for `pause` arguments and use
            those to calculate timestamps for the text messages.
        """

        if messages is None:
            messages = []

        while l.advance():
            with l.catch_error():
                state = l.checkpoint()
                try:
                    if is_text_msg and l.keyword('pause'):
                        p_time = l.rest()
                        messages.append('pause' + '|' + p_time)
                    elif is_text_msg and l.keyword('label'):
                        label_name = l.rest()
                        messages.append('label' + '|' + label_name)
                    else:
                        line = parse_msg_stmt(l, check_time=check_time)
                        messages.append(line)
                    continue
                except:
                    l.revert(state)

                try:
                    # If that didn't work, assume it's a python conditional
                    messages.append(parse_msg_conditional(l,
                        check_time, is_text_msg))
                except:
                    l.error("Couldn't parse message conditional.")

        return messages

    def parse_msg_conditional(l, check_time=False, is_text_msg=False):
        """
        Parse l as a conditional statement intended for a message.
        """

        if not l.keyword('if'):
            renpy.error("Unrecognized statement inside text message block.")
        entries = [ ]
        condition = l.require(l.python_expression)
        l.require(':')
        l.expect_eol()
        l.expect_block('if statement')

        block = parse_sub_block(l.subblock_lexer(), check_time=check_time,
            is_text_msg=is_text_msg)
        entries.append((condition, block))

        l.advance()

        while l.keyword('elif'):
            condition = l.require(l.python_expression)
            l.require(':')
            l.expect_eol()
            l.expect_block('elif clause')

            block = parse_sub_block(l.subblock_lexer(), check_time=check_time,
                is_text_msg=is_text_msg)
            entries.append((condition, block))
            l.advance()

        if l.keyword('else'):
            l.require(':')
            l.expect_eol()
            l.expect_block('elif clause')

            block = parse_sub_block(l.subblock_lexer(), check_time=check_time,
                is_text_msg=is_text_msg)
            entries.append(('True', block))
            l.advance()

        return entries


    def resolve_conditionals(items):
        """
        Turn a list of (condition, block) tuples into a list with the
        appropriate dialogue based on which condition evaluates to True.
        """

        if not isinstance(items, list):
            return [ ]

        the_block = [ ]

        for condition, block in items:
            try:
                condition = renpy.python.py_eval(condition)
            except:
                print("WARNING: something went wrong when evaluating the condition",
                    condition)
                condition = None
            if not condition:
                continue
            else:
                the_block = block
                break

        messages = [ ]
        for msg in the_block:
            if isinstance(msg, list):
                messages.extend(resolve_conditionals(msg))
            else:
                messages.append(msg)
        return messages



    def parse_backlog_stmt(l):
        # First, find need the person whose text message backlog this is
        who = l.simple_expression()
        # For whatever reason negative numbers get stored with "who", so
        # separate it
        if ' ' in who:
            actual_who = who.split(' ')[0]
            day = who.split(' ')[1]
            who = actual_who
        else:
            # See if there is a number for how many days in the past
            day = l.integer()
            if day is None:
                day = '0'
        l.require(':')
        l.expect_eol()

        # Parse the statements in the subblock and store them
        messages = [ ]
        ll = l.subblock_lexer()
        # This function recursively calls itself to check all sub-blocks
        messages = parse_sub_block(ll, messages, check_time=True,
            is_text_msg=True)

        return dict(who=who,
                    day=day,
                    messages=messages)

    def predict_backlog_stmt(p):
        messages = p['messages']
        images = []
        for msg_dict in messages:
            try:
                images.extend(predict_msg_stmt(msg_dict))
            except:
                print("ERROR: Could not predict images for backlog statement.")
        return images

    def execute_backlog_stmt(p):
        # Get the 'who' and 'day' of this backlog
        try:
            sender = eval(p['who'])
            day = eval(p['day'])
        except:
            renpy.error("Could not parse arguments of backlog CDS.")

        # Double-check 'sender' is a ChatCharacter
        if not isinstance(sender, ChatCharacter):
            print("WARNING: The ChatCharacter %s for dialogue \"" + what
                + "\" could not be evaluated." % p['who'])
            renpy.show_screen('script_error',
                    message=("The ChatCharacter %s for dialogue " + what
                        + " could not be evaluated." % p['who']),
                    link="Adding-a-New-Character-to-Chatrooms",
                    link_text="Adding a New Character to Chatrooms")
            return

        # Time to go through the messages and determine if there are any
        # conditionals to be resolved.
        messages = [ ]
        for msg in p['messages']:
            if isinstance(msg, list):
                # This is a conditional
                messages.extend(resolve_conditionals(msg))
            else:
                messages.append(msg)
        backlog = []
        what = "First message"
        for d in messages:
            if isinstance(d, dict):
                try:
                    d2 = execute_msg_stmt(d, return_dict=True)
                    timestamp = d['timestamp']
                    who = d2['who']
                    dialogue = d2['dialogue']
                    img = d2['img']
                except:
                    print("WARNING: The arguments for dialogue %s could not "
                        + "be evaluated." % d['what'])
                    renpy.show_screen('script_error',
                            message=("The arguments for dialogue %s could not "
                                + "be evaluated." % d['what']))
                    return

                # Create the 'when' timestamp
                if timestamp:
                    when = upTime(day, timestamp)
                else:
                    when = upTime(day)
                backlog.append((ChatEntry(who, dialogue, when, img), timestamp))
            elif d[:5] == 'pause':
                backlog.append(d.split('|'))
            else:
                print("WARNING: Could not recognize text message:", d)

        if len(backlog) == 0:
            return
        # Adjust timestamps for typing time
        total_sec = 0
        start_time = None
        for msg, timestamp in backlog:
            # Everything should be a tuple
            if isinstance(msg, ChatEntry):
                if start_time is None and not timestamp:
                    print("WARNING: Did not get an initial timestamp for %s's"
                        + " text message backlog." % sender.name)
                    renpy.show_screen('script_error',
                            message=("Did not get an initial timestamp for %s's"
                                + " text message backlog." % sender.name))
                    start_time = '00:00'
                elif start_time is None:
                    start_time = timestamp

                if not timestamp:
                    # Adjust this time stamp
                    when = upTime(day, start_time)
                    when.adjust_time(timedelta(seconds=total_sec))
                    msg.thetime = when
                else:
                    start_time = timestamp
                    total_sec = 0
                typeTime = calculate_type_time(msg.what)
                total_sec += typeTime
                sender.text_msg.msg_list.append(msg)
                print_file("Added message", msg.what, "time", msg.thetime.stopwatch_time,
                    "to", sender.name + "'s text backlog")

            elif msg == 'pause':
                try:
                    pause_time = eval(timestamp)
                    total_sec += pause_time
                except:
                    print("ERROR: couldn't evaluate text message pause argument")

        sender.text_msg.read = True
        return

    def lint_backlog_stmt(p):
        try:
            sender = eval(p['who'])
        except:
            renpy.error("ChatCharacter not defined in backlog statement.")

        try:
            day = eval(p['day'])
        except:
            renpy.error("Could not determine day in backlog statement.")

        if not isinstance(sender, ChatCharacter):
            renpy.error("Sender of backlog is not recognized as a ChatCharacter.")

        for d in p['messages']:
            if isinstance(d, dict):
                try:
                    who = eval(d["who"])
                    what = d["what"]
                    ffont = d["ffont"]
                    bold = d["bold"]
                    xbold = d["xbold"]
                    big = d["big"]
                    img = d["img"]
                    timestamp = d['timestamp']
                except:
                    renpy.error("Could not parse arguments of backlog CDS")

                # Check text tags
                tte = renpy.check_text_tags(what)
                if tte:
                    renpy.error(tte)
            elif d != 'end':
                # It's a condition
                try:
                    if 'if ' in d:
                        condition = d[3:]
                        condition = eval(condition)
                    elif len(d) > 0:
                        condition = eval(d)
                except:
                    renpy.error("Could not evaluate condition for backlog.")
        return

    def translate_backlog_stmt(p):
        # TODO: Remove this
        return [ ]
        messages = p['messages']

        translation = [ ]
        for msg in messages:
            translation.extend(translate_msg_stmt(msg))
        return translation

    def parse_msg_stmt(l, check_time=False, msg_prefix=False):

        who = l.simple_expression()
        # This is also used to parse backlogs; if it begins with if/elif/else
        # then the program was trying to evaluate a python string so it
        # should raise an error and stop parsing.
        if who in ['elif', 'if', 'else']:
            raise AttributeError
        elif msg_prefix and who == 'msg':
            who = l.simple_expression()
        what = l.string()

        if not who or not what:
            print("Who/What not registering. Who:", who, "what", what)
            renpy.error("msg requires a speaker and some dialogue")

        ffont = 'sser1'
        pv = "None"
        bold = False
        xbold = False
        big = False
        img = False
        bounce = False
        spec_bubble = None
        timestamp = False
        arg_dict = dict()

        bubble_list = ['cloud_l', 'cloud_m', 'cloud_s', 'round_l', 'round_m',
                'round_s', 'sigh_l', 'sigh_m', 'sigh_s', 'spike_l', 'spike_m',
                'spike_s', 'square_l', 'square_m', 'square_s', 'square2_l',
                'square2_m', 'square2_s', 'round2_l', 'round2_m', 'round2_s',
                'flower_l', 'flower_m', 'flower_s', 'glow2']

        font_list = ['sser1', 'sser2', 'ser1', 'ser2', 'curly','blocky']

        while True:

            if l.eol():
                break

            # If you preface the argument with `font`, you can use custom
            # fonts
            if l.keyword('font'):
                ffont = l.simple_expression()
                if ffont is None:
                    renpy.error('expected font for msg argument')
                continue
            # Similarly, prefacing a bubble argument with `bubble` allows you
            # to use custom bubbles
            if l.keyword('bubble'):
                spec_bubble = l.simple_expression()
                if spec_bubble is None:
                    renpy.error('expected special bubble for msg argument')
                bounce = True
                continue
            if l.keyword('pv'):
                pv = l.simple_expression()
                if pv is None:
                    renpy.error('expected simple expression for pv value')
                continue

            if check_time:
                if l.keyword('time'):
                    # Timestamp needs to be of the format ##:##
                    timestamp = l.match("\d\d:\d\d")
                if timestamp is None:
                    renpy.error('expected timestamp for time argument')
                continue
            if l.keyword('bold'):
                bold = True
                xbold = False
                continue
            if l.keyword('xbold'):
                xbold = True
                bold = False
                continue
            if l.keyword('img'):
                img = True
                bounce = False
                continue
            if l.keyword('bounce'):
                bounce = True
                continue
            if l.keyword('glow'):
                bounce = True
                continue
            if l.keyword('big'):
                big = True
                continue

            state = l.checkpoint()

            item = l.simple_expression()
            if item in bubble_list:
                spec_bubble = item
                bounce = True
                continue

            if item in font_list:
                ffont = item
                continue

            l.revert(state)

            arg_dict = c_parse_arguments(l)

            renpy.error("couldn't recognize msg argument")

        return dict(who=who,
                    what=what,
                    pv=pv,
                    ffont=ffont,
                    bold=bold,
                    xbold=xbold,
                    big=big,
                    img=img,
                    bounce=bounce,
                    spec_bubble=spec_bubble,
                    timestamp=timestamp,
                    arg_dict=arg_dict)


    def execute_msg_stmt(p, return_dict=False, is_text_msg=False):
        try:
            who = eval(p["who"])
            what = p["what"]
            pv = eval(p["pv"])
            ffont = p["ffont"]
            bold = p["bold"]
            xbold = p["xbold"]
            big = p["big"]
            img = p["img"]
            bounce = p["bounce"]
            spec_bubble = p["spec_bubble"]
            arg_dict = p['arg_dict']
        except:
            print_file("msg CDS failed. Results:", p['who'], p['what'], p['pv'])
            renpy.error("Could not parse arguments of msg CDS")
            return

        # Double-check 'who' is a ChatCharacter
        if not isinstance(who, ChatCharacter):
            print("WARNING: The ChatCharacter %s for dialogue \"" + what
                + "\" could not be evaluated." % p['who'])
            renpy.show_screen('script_error',
                    message=("The ChatCharacter %s for dialogue " + what
                        + " could not be evaluated." % p['who']),
                    link="Adding-a-New-Character-to-Chatrooms",
                    link_text="Adding a New Character to Chatrooms")
            return

        # Retrieve the arguments, if applicable
        if arg_dict:
            arg_info = renpy.ast.ArgumentInfo(arg_dict['args'], arg_dict['pos'],
                arg_dict['kwargs'])
            args, kwargs = arg_info.evaluate()
            args = args or tuple()
            kwargs = kwargs or dict()
            print_file("\nBefore parsing arguments, values were:")
            print_file("    img:", img, "\n    bounce:", bounce)
            print_file("    specBubble:", spec_bubble, "\n    pv:", pv)

            # Check for img
            img = kwargs.get('img', img)
            # Check for bounce
            bounce = kwargs.get('bounce', bounce)
            # Check for specBubble
            spec_bubble = kwargs.get('specBubble', spec_bubble)
            # Check for pv
            pv = kwargs.get('pauseVal', pv)

        # Correct 'what' into dialogue with the right text tags
        dialogue, img, spec_bubble = parse_message_args(what, ffont, bold,
            xbold, big, img, spec_bubble, is_text_msg=is_text_msg)

        # print_file("\nAfter parsing arguments, values are:")
        # print_file("    img:", img, "\n    bounce:", bounce)
        # print_file("    specBubble:", spec_bubble, "\n    pv:", pv)
        # print_file("    dialogue:", dialogue)

        # What to do with this dialogue depends on if it's for a chatroom
        # or a text message, or for another CDS
        if return_dict:
            return dict(who=who,
                        what=dialogue,
                        pauseVal=pv,
                        img=img,
                        bounce=bounce,
                        specBubble=spec_bubble)

        # Check if the player just got out of a menu and there's dialogue
        # for the main character.
        if (who != store.main_character and not store.dialogue_paraphrase
                and store.dialogue_picked != ""):
            say_choice_caption(store.dialogue_picked,
                store.dialogue_paraphrase, store.dialogue_pv)

        if (who == store.main_character
                and not kwargs.get('from_paraphrase', None)):
            # This didn't come from `say_choice_caption`, but the MC is
            # speaking. Is this the same dialogue that was going to be
            # posted?
            # print("what =", what, "dialogue_picked =", store.dialogue_picked)
            if what == store.dialogue_picked:
                # Clear the stored no-paraphrase items
                store.dialogue_picked = ""
                store.dialogue_paraphrase = store.paraphrase_choices
                store.dialogue_pv = 0
                # If paraphrase_choices is None, set it to True
                if store.paraphrase_choices is None:
                    store.paraphrase_choices = True

        if store.text_person is not None:
            # If the player is on the text message screen, then show the
            # message in real-time
            if store.text_person.real_time_text and store.text_msg_reply:
                addtext_realtime(who, dialogue, pauseVal=pv, img=img)
            # If they're not on the text message screen, this is "backlog"
            # to a text conversation
            elif store.text_person.real_time_text:
                if not who.right_msgr:
                    store.text_person.text_msg.notified = False
                if img and "{image" not in what:
                    cg_helper(what, who, False)
                store.text_person.text_msg.msg_list.append(ChatEntry(
                    who, dialogue, upTime(), img))
            # Otherwise, this is a regular text conversation and is added
            # all at once
            else:
                addtext(who, dialogue, img)
        # This is for a chatroom
        else:
            # Add an entry to the replay_log if the player is not observing
            # this chat
            if not store.observing:
                new_pv = pv
                # For replays, MC shouldn't reply instantly
                if who.right_msgr and new_pv == 0:
                    new_pv = None
                    store.current_timeline_item.replay_log.append(ReplayEntry(
                            who, dialogue, new_pv, img, bounce, spec_bubble))

            # Now add this dialogue to the chatlog
            addchat(who, dialogue, pauseVal=pv, img=img, bounce=bounce,
                specBubble=spec_bubble)

        return

    def lint_msg_stmt(p):
        try:
            who = eval(p["who"])
            what = p["what"]
            pv = eval(p["pv"])
            ffont = p["ffont"]
            bold = p["bold"]
            xbold = p["xbold"]
            big = p["big"]
            img = p["img"]
            bounce = p["bounce"]
            spec_bubble = p["spec_bubble"]
        except:
            renpy.error("Could not parse arguments of msg CDS")

        # Double-check 'who' is a ChatCharacter
        if not isinstance(who, ChatCharacter):
            renpy.error("The ChatCharacter %s for dialogue \"" + what
                + "\" could not be evaluated." % p['who'])
        return

    def predict_msg_stmt(p):
        # Predict possible images used
        try:
            what = p['what']
        except:
            renpy.error("Could not evaluate what argument of custom say")
            return [ ]
        if p['img'] and "{image" in what:
            # Get the image that will be used
            img = what.split('=')[2].strip()[:-1]
            return [ img ]
        elif p['img']:
            if what[:3] != 'cg ':
                img = 'cg ' + what
            else:
                img = what
            return [ img ]
        return [ ]

    def warp_msg_stmt(p):
        return True

    def translate_msg_stmt(p):
        return [ ]
        # Get the 'what'
        try:
            what = p['what']
        except:
            return [ ]

        if "{image" not in what:
            return [ what ]
        return [ ]

    renpy.register_statement('msg',
        parse=parse_msg_stmt,
        execute=execute_msg_stmt,
        translation_strings=translate_msg_stmt,
        predict=predict_msg_stmt,
        lint=lint_msg_stmt,
        warp=warp_msg_stmt)

    renpy.register_statement('add backlog',
        parse=parse_backlog_stmt,
        execute=execute_backlog_stmt,
        predict=predict_backlog_stmt,
        translation_strings=translate_backlog_stmt,
        lint=lint_backlog_stmt,
        warp=warp_msg_stmt,
        block=True)

    ########################################
    ## COMPOSE TEXT MESSAGE CDS
    ########################################
    def parse_compose_text(l):
        # What compose text CDSs look like:
        # compose text who <real_time> <deliver_at [00:00, random]>:
        # compose text s real_time deliver_at 09:30:
        # compose text z deliver_at random:
        # compose text y deliver_at next_item:

        # First, require the variable of the person whose text message
        # conversation this belongs to
        who = l.simple_expression()

        real_time = False
        delivery_time = False

        # Next, there are some optional arguments
        while True:

            if l.eol():
                renpy.error("Reached end of line without a colon")
                break

            if l.keyword('real_time'):
                real_time = True
                continue

            if l.keyword('deliver_at'):
                delivery_time = l.match("\d\d:\d\d")
                if delivery_time is not None:
                    continue
                # Try matching it to the word `random`
                delivery_time = l.match('random')
                if delivery_time is not None:
                    continue
                # Try matching it to the word `next_item`
                delivery_time = l.match('next_item')
                if delivery_time is not None:
                    continue
                renpy.error("Could not parse argument for deliver_at")

            if l.match(":") and not l.match("\d\d:\d\d"):
                l.expect_eol()
                break

            renpy.error("couldn't recognize compose text argument")

        # Parse the statements in the subblock and store them
        messages = [ ]
        ll = l.subblock_lexer()
        # This function recursively calls itself to check all sub-blocks
        messages = parse_sub_block(ll, messages, is_text_msg=True)

        return dict(who=who,
                    real_time=real_time,
                    delivery_time=delivery_time,
                    messages=messages)

    def execute_compose_text(p):
        # Get the non-message arguments
        try:
            sender = eval(p['who'])
            real_time = p['real_time']
            delivery_time = p['delivery_time']
            messages = p['messages']
        except:
            renpy.error("Could not parse arguments of compose text CDS.")

        # Double-check 'sender' is a ChatCharacter
        if not isinstance(sender, ChatCharacter):
            print("WARNING: The ChatCharacter %s for dialogue \"" + what
                + "\" could not be evaluated." % p['who'])
            renpy.show_screen('script_error',
                    message=("The ChatCharacter %s for dialogue " + what
                        + " could not be evaluated." % p['who']),
                    link="Adding-a-New-Character-to-Chatrooms",
                    link_text="Adding a New Character to Chatrooms")
            return

        sender.set_real_time_text(real_time)
        sender.text_msg.read = False
        store.textbackup = 'Reset'
        store.text_person = sender

        send_now = True
        generate_timestamps = False

        # Create the 'when' timestamp. Several cases to consider:
        # CASE 1:
        # This is either being expired from check_and_unlock_story in real-time,
        # or it's the current timeline item. The text message can have the
        # real time stamp.
        print_file("Delivery_time is", delivery_time)
        if store.persistent.real_time:
            # Determine how many days ago the expiring item or current item was
            if store.expiring_item:
                check_item = store.expiring_item
                day_index = get_item_day(store.expiring_item)
                day_diff = store.days_to_expire - day_index - 1
            else:
                check_item = store.current_timeline_item
                day_index = store.today_day_num
                day_diff = 0
            print_file("For the timestamp: check_item", check_item.item_label,
                "day_index", day_index, "day_diff", day_diff, "days_to_expire",
                store.days_to_expire)
            # Create the timestamp
            if (delivery_time and delivery_time != 'random'
                    and delivery_time != 'next_item'):
                when = upTime(day=day_diff, thetime=delivery_time)
                print_file("1. we've got a timestamp that looks like", when.get_text_msg_time())
            elif not delivery_time:
                when = upTime(day=day_diff, thetime=check_item.trigger_time)
                print_file("2. we've got a timestamp that looks like", when.get_text_msg_time())
            else:
                # Need to generate a random delivery time
                begin = check_item.trigger_time
                end, day_diff2 = closest_item_time(check_item)
                # If delivery time is `next_item`, then it goes *after*
                # this item.
                if delivery_time == 'next_item':
                    begin = end
                    end, day_diff3 = closest_item_time(begin)
                    begin = begin.trigger_time
                    day_diff2 += day_diff3
                end = end.trigger_time
                print_file("begin is", begin, "and day_diff is", day_diff)
                # day_diff2 is the difference between the checked item
                # and its closest item
                print_file("end is", end, "and day_diff2 is", day_diff2)
                random_time, final_day_diff = get_random_time(
                    begin=begin, end=end, day_diff=day_diff2
                )
                # final_day_diff is the difference between the checked
                # item and the new generated random time
                # Set day_diff equal to the difference between the
                # current day and the day of the random time
                day_diff = (store.days_to_expire - day_index
                    - 1 + final_day_diff)
                # Now make the time stamp
                when = upTime(day=day_diff, thetime=random_time)
            # It's possible the program generated a timestamp in the
            # future, and this message shouldn't be sent now
            send_now = when.has_occurred()
            generate_timestamps = True
            print_file('send_now is', send_now, "and we've got a timestamp that looks like",
                when.get_text_msg_time())
        # CASE 2:
        # Program is running sequentially OR player has bought
        # the next 24 hours in advance
        # After_ items are delivered after the player has played
        # that item
        elif ((store.persistent.real_time and not store.expiring_item)
                or not store.persistent.real_time):
            # There is no point manufacturing timestamps, as all items
            # are simply delivered after the item is played
            when = upTime()

        # CASE 3:
        # The player backed out of this item and expired it. Now its
        # after_ items are delivered immediately
        else:
            when = upTime()

        message_queue = [ ]
        messages = [ ]

        # Time to go through the messages and determine if there are any
        # conditionals to be resolved.
        for msg in p['messages']:
            if isinstance(msg, list):
                # This is a conditional
                messages.extend(resolve_conditionals(msg))
            else:
                messages.append(msg)

        # Now go through and turn this into an understandable dictionary
        for d in messages:
            if isinstance(d, dict):
                try:
                    d2 = execute_msg_stmt(d, return_dict=True, is_text_msg=True)
                    what = d['what']
                    who = d2['who']
                    dialogue = d2['what']
                    img = d2['img']
                except:
                    print("WARNING: The arguments for dialogue %s could not "
                        + "be evaluated." % d['what'])
                    renpy.show_screen('script_error',
                            message=("The arguments for dialogue %s could not "
                                + "be evaluated." % d['what']))
                    return


                # Add messages to send to a list first
                message_queue.append(ChatEntry(who, dialogue, deepcopy(when), img))
                sender.text_msg.notified = False
                if img and "{image" not in dialogue:
                    # Add the CG to the unlock list
                    cg_helper(what, who, instant_unlock=False)

            elif d[:5] == 'pause':
                if not generate_timestamps:
                    continue
                else:
                    message_queue.append(d)

            elif d[:5] == 'label':
                try:
                    arg, val = d.split('|')
                except:
                    print("ERROR: could not split text message argument.")
                    continue
                if arg == 'label':
                    # It's the label to jump to for the reply
                    sender.text_label = val

            else:
                print("WARNING: Could not recognize text message:", d)

        # Now go through and adjust the timestamps of each message if needed
        if generate_timestamps:
            new_queue = []
            total_sec = 0
            while len(message_queue) > 0:
                if send_now:
                    msg = message_queue.pop()
                else:
                    msg = message_queue.pop(0)

                if not isinstance(msg, ChatEntry):
                    try:
                        arg, val = msg.split('|')
                    except:
                        print("ERROR: could not split text message argument")
                        continue
                    # It's a pause argument
                    if arg == 'pause':
                        try:
                            pause_time = eval(val)
                            if send_now:
                                total_sec -= pause_time
                            else:
                                total_sec += pause_time
                        except:
                            print("ERROR: couldn't evaluate text message pause argument")
                        print_file("Adjusted total_sec by", pause_time)
                    continue

                msg.thetime.adjust_time(timedelta(seconds=total_sec))
                typeTime = calculate_type_time(msg.what)
                if send_now:
                    total_sec -= typeTime
                    new_queue.insert(0, msg)
                else:
                    total_sec += typeTime
                    new_queue.append(msg)
                print_file("Added message", msg.what, "time", msg.thetime.stopwatch_time)
            message_queue = new_queue

        # Add these messages to the sender's msg_queue
        sender.text_msg.msg_queue.extend(message_queue)
        print_file("Extended " + sender.file_id + "'s msg_queue")
        store.text_person = None
        return


    def lint_compose_text(p):
        return

    renpy.register_statement('compose text',
        parse=parse_compose_text,
        execute=execute_compose_text,
        predict=predict_backlog_stmt,
        #translation_strings=translate_backlog_stmt,
        lint=lint_compose_text,
        warp=lambda : True,
        block=True)

    ########################################
    ## AWARD/BREAK HEART CDS
    ########################################
    ## Creator-defined statements for awarding and rescinding heart points
    def parse_award_heart(l):

        who = l.simple_expression()
        if not who:
            renpy.error("award heart requires a person to award the heart to.")

        bad = False

        while True:
            if l.eol():
                break
            if l.keyword('bad'):
                bad = True
                continue

            renpy.error("Could not parse statement.")

        return dict(who=who, bad=bad)

    def execute_award_heart(p):

        if p["who"] is not None:
            who = eval(p["who"])
        else:
            renpy.error("award heart requires a ChatCharacter the heart belongs to")

        if who is None or not isinstance(who, ChatCharacter):
            print("WARNING: variable %s provided to award heart is not recognized as a ChatCharacter." % p["who"])
            renpy.show_screen('script_error',
                message="Variable %s provided to award heart is not recognized as a ChatCharacter.",
                link="Useful-Chatroom-Functions#how-to-show-a-heart-icon",
                link_text="How to show a heart icon")
            return


        bad = p["bad"]

        # This ensures pending dialogue is posted before awarding a heart.
        # Fixes some issues with text message heart points.
        if (not store.dialogue_paraphrase and store.dialogue_picked != ""):
            say_choice_caption(store.dialogue_picked,
                store.dialogue_paraphrase, store.dialogue_pv)

        # This is during a chatroom or a real-time text conversation
        if store.text_person is None or store.text_person.real_time_text:
            try:
                if not store.observing:
                    who.increase_heart(bad)
                    if store.text_person is None:
                        # store.collected_hp += 1
                        if bad:
                            store.collected_hp['bad'].append(who)
                        else:
                            store.collected_hp['good'].append(who)
                    store.persistent.HP += 1

                    if store.persistent.animated_icons:
                        renpy.show_screen(allocate_heart_screen(), character=who)
                    else:
                        msg = who.name + " +1"
                        renpy.show_screen(allocate_notification_screen(True), msg)
            except:
                print("WARNING: Heart could not be awarded for %s." % p["who"])
                renpy.show_screen('script_error',
                    message="Heart could not be awarded for " + p["who"],
                    link="Useful-Chatroom-Functions#how-to-show-a-heart-icon",
                    link_text="How to show a heart icon")
                return
        # This is during a regular text message
        else:
            add_heart(store.text_person, who, bad)
        return


    def predict_award_heart(p):
        if not persistent.animated_icons:
            return [ ]
        if p["who"] is not None:
            try:
                who = eval(p["who"])
            except:
                return [ ]
        return [ heart_icon(who) ]

    def warp_award_heart(p):
        return True

    def lint_award_heart(p):

        who = p["who"]
        eval_who = None
        try:
            eval_who = eval(p["who"])
        except:
            renpy.error("heart functions require a ChatCharacter the heart belongs to")

        if eval_who is None:
            renpy.error("The person the heart belongs to cannot be None.")

        if not isinstance(eval_who, ChatCharacter):
            renpy.error("%s is not recognized as a ChatCharacter object for the heart icon." % p["who"])

        return

    renpy.register_statement('award heart',
        parse=parse_award_heart,
        execute=execute_award_heart,
        predict=predict_award_heart,
        lint=lint_award_heart,
        warp=warp_award_heart)

    def parse_break_heart(l):
        who = l.simple_expression()
        return dict(who=who)

    def execute_break_heart(p):
        if p["who"] is not None:
            who = eval(p["who"])
        else:
            renpy.error("break heart requires a ChatCharacter the heart belongs to")

        if who is None or not isinstance(who, ChatCharacter):
            print("WARNING: variable %s provided to break heart is not recognized as a ChatCharacter." % p["who"])
            renpy.show_screen('script_error',
                message="Variable %s provided to break heart is not recognized as a ChatCharacter.",
                link="Useful-Chatroom-Functions#how-to-show-a-heart-icon",
                link_text="How to show a heart icon")
            return

        if not store.observing:
            who.decrease_heart()

            if store.text_person is None:
                store.collected_hp['break'].append(who)
            store.persistent.HP -= 1

            if store.persistent.animated_icons:
                renpy.show_screen('heart_break_screen', character=who)
            else:
                msg = who.name + " -1"
                renpy.show_screen(allocate_notification_screen(True), msg)
        return

    def predict_break_heart(p):
        if not persistent.animated_icons:
            return [ ]
        if p["who"] is not None:
            try:
                who = eval(p["who"])
            except:
                return [ ]
        return [ heart_break_img("Heart Point/heartbreak_0.webp", who),
                heart_break_img("Heart Point/heartbreak_1.webp", who),
                heart_break_img("Heart Point/heartbreak_2.webp", who),
                heart_break_img("Heart Point/heartbreak_3.webp", who),
                heart_break_img("Heart Point/heartbreak_4.webp", who) ]

    renpy.register_statement('break heart',
        parse=parse_break_heart,
        execute=execute_break_heart,
        predict=predict_break_heart,
        lint=lint_award_heart,
        warp=warp_award_heart)

    # This duplicates the above statement, just switches the words to account
    # for possible error checking.
    renpy.register_statement('heart break',
        parse=parse_break_heart,
        execute=execute_break_heart,
        predict=predict_break_heart,
        lint=lint_award_heart,
        warp=warp_award_heart)

    ########################################
    ## INVITE GUEST CDS
    ########################################
    # Definitions that allow you to write `invite guest` in Ren'Py script
    def parse_invite_guest(l):
        guest = l.simple_expression()
        if not guest:
            renpy.error("invite requires a guest to invite")

        return dict(guest=guest)

    def execute_invite_guest(p):

        if p["guest"] is not None:
            guest = eval(p["guest"])
        else:
            renpy.error("invite requires a guest to invite.")

        if not (isinstance(guest, Guestv2) or isinstance(guest, Guestv3)):
            print("WARNING: Invited guest is not recognized as a Guest object.")
            renpy.show_screen('script_error',
                message="Invited guest %s is not recognized as a Guest object." % p["guest"],
                link="Inviting-a-Guest", link_text="Inviting a Guest")
            return
        elif guest is None:
            print("WARNING: Invited guest cannot be None.")
            renpy.show_screen('script_error', message="Invited guest cannot be None.",
                link="Inviting-a-Guest", link_text="Inviting a Guest")
            return


        # So you can't re-invite a guest while replaying a chatroom
        if (not store.observing) or store.persistent.testing_mode:
            try:
                # Add them to the front of the email inbox
                if isinstance(guest, Guestv2):
                    e = Email(guest, guest.start_msg, guest.label1)
                else:
                    e = Emailv3(guest)
                store.email_list.insert(0, e)
                # The player has encountered the guest so the guestbook can be
                # updated
                if not store.persistent.guestbook[guest.name]:
                    store.persistent.guestbook[guest.name] = "seen"
            except:
                print("WARNING: Guest %s could not be invited." % p["guest"])
                renpy.show_screen('script_error',
                    message="Guest %s could not be invited." % p["guest"],
                    link="Inviting-a-Guest", link_text="Inviting a Guest")

        return

    def predict_invite_guest(p):
        return [ ]

    def lint_invite_guest(p):

        guest = p["guest"]
        eval_guest = None

        try:
            eval_guest = eval(p["guest"])
        except:
            renpy.error("invite requires a guest to invite.")

        if eval_guest is None:
            renpy.error("Invited guest cannot be None.")

        if not (isinstance(eval_guest, Guestv2)
                or isinstance(eval_guest, Guestv3)):
            renpy.error("Invited guest %s is not recognized as a Guest object." % p["guest"])

        return

    def warp_invite_guest(p):
        return True

    renpy.register_statement('invite',
        parse=parse_invite_guest,
        execute=execute_invite_guest,
        predict=predict_invite_guest,
        lint=lint_invite_guest,
        warp=warp_invite_guest)

    ########################################
    ## CLEAR CHAT CDS
    ########################################
    # Definitions that allow you to clear the chatlog in a chatroom.
    def parse_clear_chat(l):
        reset_participants = False
        if l.keyword('participants'):
            reset_participants = True
        return reset_participants

    def execute_clear_chat(reset_participants):
        store.chatlog = []
        addchat(filler, "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", 0)
        if reset_participants:
            store.in_chat = []
            if not store.observing:
                current_timeline_item.reset_participants()
            for person in current_timeline_item.original_participants:
                if person.name not in store.in_chat:
                    store.in_chat.append(person.name)
        return

    renpy.register_statement('clear chat',
        parse=parse_clear_chat,
        execute=execute_clear_chat,
        warp=lambda : True)
    ########################################
    ## PLAY MUSIC/SOUND REPLACEMENT CDS
    ########################################
    # These statements replace Ren'Py's default `play music` and `play sound`
    # implementations so they are compatible with audio captions.
    def warp_audio(p):
        """
        Determines if the program should play this statement while warping.
        """

        if p.get("channel", None) is not None:
            channel = eval(p["channel"])
        else:
            channel = "music"

        return renpy.music.is_music(channel)

    def parse_play_music(l):

        file = l.simple_expression()
        if not file:
            renpy.error("play requires a file")

        fadeout = "None"
        fadein = "0"
        channel = None
        loop = None
        if_changed = False
        captions = True

        while True:

            if l.eol():
                break

            if l.keyword('fadeout'):
                fadeout = l.simple_expression()
                if fadeout is None:
                    renpy.error('expected simple expression')

                continue

            if l.keyword('fadein'):
                fadein = l.simple_expression()
                if fadein is None:
                    renpy.error('expected simple expression')

                continue

            if l.keyword('channel'):
                channel = l.simple_expression()
                if channel is None:
                    renpy.error('expected simple expression')

                continue

            if l.keyword('loop'):
                loop = True
                continue

            if l.keyword('noloop'):
                loop = False
                continue

            if l.keyword('if_changed'):
                if_changed = True
                continue

            if l.keyword('nocaption'):
                captions = False
                continue

            renpy.error('could not parse statement.')

        return dict(file=file,
                    fadeout=fadeout,
                    fadein=fadein,
                    channel=channel,
                    loop=loop,
                    if_changed=if_changed,
                    captions=captions)


    def execute_play_c_music(p):

        if p["channel"] is not None:
            channel = eval(p["channel"])
        else:
            channel = "music"

        captions = p["captions"]

        if captions:
            try:
                notification =  ("♪ " +
                        store.music_dictionary[getattr(store, p["file"])]
                        + " ♪")
                if store.persistent.audio_captions:
                    renpy.show_screen('notify', notification)
            except (KeyError, AttributeError) as e:
                renpy.show_screen('script_error',
                    message="No Audio Caption defined for %s" % p["file"],
                    link="Adding-Music-and-SFX", link_text="Adding Music and SFX")
                print("WARNING: No Audio Caption defined for " + p["file"])

            if (not store.observing and not store.persistent.testing_mode
                    and not store.vn_choice):
                # Add this music to the replay_log
                try:
                    music_entry = ("play music", getattr(store, p["file"]))
                except AttributeError:
                    music_entry = ("play music", p["file"])
                store.current_timeline_item.replay_log.append(music_entry)

        renpy.music.play(_audio_eval(p["file"]),
                         fadeout=eval(p["fadeout"]),
                         fadein=eval(p["fadein"]),
                         channel=channel,
                         loop=p.get("loop", None),
                         if_changed=p.get("if_changed", False))

    def predict_play_music(p):
        return [ ]

    def lint_play_music(p, channel="music"):

        file = _try_eval(p["file"], 'filename')

        if p["channel"] is not None:
            channel = _try_eval(p["channel"], 'channel')

        if not isinstance(file, list):
            file = [ file ]

        for fn in file:
            if isinstance(fn, basestring):
                try:
                    if not renpy.music.playable(fn, channel):
                        renpy.error("%r is not loadable" % fn)
                except:
                    pass

    renpy.register_statement('play music',
        parse=parse_play_music,
        execute=execute_play_c_music,
        predict=predict_play_music,
        lint=lint_play_music,
        warp=warp_audio)

    def warp_sound(p):
        """
        Determines if the program should play this statement while warping.
        """

        if p.get("channel", None) is not None:
            channel = eval(p["channel"])
        else:
            channel = "sound"

        return renpy.music.is_music(channel)

    def lint_play_sound(p, lint_play_music=lint_play_music):
        return lint_play_music(p, channel="sound")

    def execute_play_c_sound(p):

        if p["channel"] is not None:
            channel = eval(p["channel"])
        else:
            channel = "sound"

        fadeout = eval(p["fadeout"]) or 0
        captions = p["captions"]

        loop = p.get("loop", False)

        if loop is None:
            loop = config.default_sound_loop

        if captions:
            try:
                notification = ("SFX: " +
                        store.sfx_dictionary[getattr(store, p["file"])])
                if store.persistent.audio_captions:
                    renpy.show_screen('notify', notification)
            except (KeyError, AttributeError) as e:
                renpy.show_screen('script_error',
                    message="No Audio Caption defined for %s" % p["file"],
                    link="Adding-Music-and-SFX", link_text="Adding Music and SFX")
                print("WARNING: No Audio Caption defined for " + p["file"])


        renpy.sound.play(_audio_eval(p["file"]),
                         fadeout=fadeout,
                         fadein=eval(p["fadein"]),
                         loop=loop,
                         channel=channel)


    renpy.register_statement('play sound',
                              parse=parse_play_music,
                              execute=execute_play_c_sound,
                              lint=lint_play_sound,
                              warp=warp_sound)




# Thoughts on how continuous menus might work
# s "Big trouble..."
# continuous menu:
#     y "What trouble?"
#     s "It's..."
#     always post:
#         s "So, I check the health reports of all the members..."
#     "Yoosung... what do we do now?":
#         y "Why?"
#         y "Did something happen?"
#         s "Gah... I was just about to say."
#     "What's big trouble?":
#         y "Yeah. What is it?"
#     "Seven's just messing around lol":
#         y "Right? lolol"
#         s "Not joking."
#         s "I'm dead serious."

#     y "Okay... Ur not saying that I can't dringak coffxee, r u?"
#     y "*drink coffee?"
#     always post:
#         s "U can never ever!!! drink coffee."
#         s "If u do, ur hands will start shaking and u'll faint eventually."
#         y "Nah"
#         y "I don't have that kind of allergy."
#         y "No way~"
#     "Ya. U'll be in trouble if u drink coffee.":
#         s "Ya..."
#         s "Seeing ur typos above, it seems like ur symptoms are showing already."

# s "..."
# s "I'm sorry."
# s "U've already lost trust in me."
# s "so u r not listening."
# y "?"

