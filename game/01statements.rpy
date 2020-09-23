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

        if is_text_msg and ffont in store.font_dict:
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

    def parse_sub_block(l, messages=[], check_time=False, is_text_msg=False):
        """
        Parse l for messages or conditional python statements. If a sub-block
        is discovered, this function recursively calls itself to parse the
        whole statement.

        Parameters:
        -----------
        l : Lexer
            The lexer that is parsing the block.
        messages : list of dict, string
            Contains dictionaries corresponding to messages as well as strings
            corresponding to conditional statements. 'end' indicates the end
            of a conditional statement's block.
        """

        while l.advance():
            with l.catch_error():
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
                except:
                    try:
                        # If that didn't work, assume it's a python conditional
                        messages.append(l.delimited_python(':'))
                    except:
                        print("Couldn't get the delimited python")
                    try:
                        ll = l.subblock_lexer()
                        messages = parse_sub_block(ll, messages, check_time)
                        messages.append('end')
                        continue
                    except:
                        print("Couldn't parse the subblock")
        return messages

    def parse_backlog_stmt(l):
        # First, we need the person whose text message backlog this is
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

        # Now we know whose backlog to add this to.
        condition = True
        condition_outcomes = []
        backlog = []
        what = "First message"
        for d in p['messages']:
            if isinstance(d, dict):
                if not condition:
                    continue
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
                    print("WARNING: The arguments for dialogue %s could not "
                        + "be evaluated." % d['what'])
                    renpy.show_screen('script_error',
                            message=("The arguments for dialogue %s could not "
                                + "be evaluated." % d['what']))
                    return

                # Get the correct dialogue and img
                dialogue, img, spec_bubble = parse_message_args(
                    what, ffont, bold, xbold, big, img, False)
                # Create the 'when' timestamp
                if timestamp:
                    when = upTime(day, timestamp)
                else:
                    when = upTime(day)
                backlog.append((ChatEntry(who, dialogue, when, img), timestamp))
                # sender.text_backlog(who, dialogue, when, img)
            elif d[:5] == 'pause':
                if not condition:
                    continue
                else:
                    backlog.append(d.split('|'))
            elif d == 'end':
                condition = True
            else:
                # This is a conditional; Evaluate it
                try:
                    # This is an 'if' statement
                    if 'if ' in d:
                        condition_outcomes = []
                        condition = d[3:]
                        condition = eval(condition)
                        condition_outcomes.append(condition)
                    # This is an 'elif' statement
                    elif len(d) > 0:
                        if len(condition_outcomes) == 0:
                            condition = False
                            continue
                        if True in condition_outcomes:
                            condition = False
                            continue
                        condition = eval(d)
                        condition_outcomes.append(condition)
                    # This is an 'else' statement
                    else:
                        if len(condition_outcomes) == 0:
                            condition = False
                            continue
                        if True in condition_outcomes:
                            condition = False
                        else:
                            condition = True
                except:
                    print("WARNING: Could not evaluate conditional statement "
                        + "for line with dialogue %s" % what)
                    renpy.show_screen('script_error',
                        message="Could not evaluate conditional statement "
                            + "for line with dialogue %s" % what)
                    return
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
        # then we were trying to evaluate a python string so it should raise
        # an error and stop parsing
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
            if l.keyword('big'):
                big = True
                continue

            item = l.simple_expression()
            if item in bubble_list:
                spec_bubble = item
                bounce = True
                continue

            if item in font_list:
                ffont = item
                continue

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
                    timestamp=timestamp)


    def execute_msg_stmt(p, return_dict=False):
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

        # Correct 'what' into dialogue with the right text tags
        dialogue, img, spec_bubble = parse_message_args(what, ffont, bold,
                                                xbold, big, img, spec_bubble)

        # What to do with this dialogue depends on if it's for a chatroom
        # or a text message, or for another CDS
        if return_dict:
            return dict(who=who,
                        what=dialogue,
                        pauseVal=pv,
                        img=img,
                        bounce=bounce,
                        specBubble=spec_bubble)

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
        # Get the non-message arguments of this day
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
            # Determine how many days ago this item was
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
                when = upTime(day=day_diff,
                    thetime=check_item.get_trigger_time())
                print_file("2. we've got a timestamp that looks like", when.get_text_msg_time())
            else:
                # Need to generate a random delivery time
                begin = check_item.get_trigger_time()
                end, day_diff2 = closest_item_time(check_item)
                # If we got `next_item`, then it goes *after* this chat
                if delivery_time == 'next_item':
                    begin = end
                    end, day_diff3 = closest_item_time(begin)
                    begin = begin.get_trigger_time()
                    day_diff2 += day_diff3
                end = end.get_trigger_time()
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

        message_queue = []

        # Now we know whose text messages to add this to.
        condition = True
        condition_outcomes = []
        for d in p['messages']:
            if isinstance(d, dict):
                if not condition:
                    continue
                try:
                    who = eval(d["who"])
                    what = d["what"]
                    ffont = d["ffont"]
                    bold = d["bold"]
                    xbold = d["xbold"]
                    big = d["big"]
                    img = d["img"]
                except:
                    print("WARNING: The arguments for dialogue %s could not "
                        + "be evaluated." % d['what'])
                    renpy.show_screen('script_error',
                            message=("The arguments for dialogue %s could not "
                                + "be evaluated." % d['what']))
                    return

                # Get the correct dialogue and img
                dialogue, img, spec_bubble = parse_message_args(
                    what, ffont, bold, xbold, big, img, False, is_text_msg=True)

                # Add messages to send to a list first
                message_queue.append(ChatEntry(who, dialogue, deepcopy(when), img))
                sender.text_msg.notified = False
                if img and "{image" not in dialogue:
                    # Add the CG to the unlock list
                    cg_helper(what, who, instant_unlock=False)

            elif d[:5] == 'pause':
                if not condition or not generate_timestamps:
                    continue
                else:
                    message_queue.append(d)
            elif d[:5] == 'label':
                if not condition:
                    continue
                try:
                    arg, val = d.split('|')
                except:
                    print("ERROR: could not split text message argument")
                    continue
                if arg == 'label':
                    # It's the label to jump to to reply
                    sender.text_label = val
            elif d == 'end':
                condition = True
            else:
                # This is a conditional; Evaluate it
                try:
                    # This is an 'if' statement
                    if 'if ' in d:
                        condition_outcomes = []
                        condition = d[3:]
                        condition = eval(condition)
                        condition_outcomes.append(condition)
                    # This is an 'elif' statement
                    elif len(d) > 0:
                        if len(condition_outcomes) == 0:
                            condition = False
                            continue
                        if True in condition_outcomes:
                            condition = False
                            continue
                        condition = eval(d)
                        condition_outcomes.append(condition)
                    # This is an 'else' statement
                    else:
                        if len(condition_outcomes) == 0:
                            condition = False
                            continue
                        if True in condition_outcomes:
                            condition = False
                        else:
                            condition = True
                except:
                    print("WARNING: Could not evaluate conditional statement "
                        + "for line with dialogue %s" % d['what'])
                    renpy.show_screen('script_error',
                        message="Could not evaluate conditional statement "
                            + "for line with dialogue %s" % d['what'])
                    return

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

        if not isinstance(guest, Guest):
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
        if not store.observing or store.persistent.testing_mode:
            try:
                guest.sent_time = upTime()
                # Add them to the front of the email inbox
                store.email_list.insert(0, Email(guest, guest.start_msg, guest.label1))
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

        if not isinstance(eval_guest, Guest):
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
        Determines if we should play this statement while warping.
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
        Determines if we should play this statement while warping.
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
    ########################################
    ## TIMED MENU CDS
    ########################################
    ## Definitions that simplify declaring a timed menu
    ## This is a helper to parse choice blocks
    def parse_choice_block(l):

        choice_block = l.renpy_block(empty=True)

        return choice_block

    ## A helper to parse menu arguments. Modified slightly from the engine
    ## code at renpy/parser.py
    def c_parse_arguments(l, include_wait=True):
        """
        Parse a list of arguments, if one is present.
        """

        arguments = [ ]
        extrakw = None
        extrapos = None
        wait = None

        if not l.match(r'\('):
            return dict(args=arguments,
                        kwargs=extrakw,
                        pos=extrapos,
                        wait=wait)

        while True:

            if l.match('\)'):
                break

            if l.match(r'\*\*'):

                if extrakw is not None:
                    l.error('a call may have only one ** argument')

                extrakw = l.delimited_python("),")

            elif l.match(r'\*'):
                if extrapos is not None:
                    l.error('a call may have only one * argument')

                extrapos = l.delimited_python("),")

            else:

                state = l.checkpoint()

                name = l.name()
                if not (name and l.match(r'=')):
                    l.revert(state)
                    name = None

                l.skip_whitespace()
                if include_wait and name == 'wait':
                    # This is a wait argument
                    wait = l.delimited_python("),")
                else:
                    arguments.append((name, l.delimited_python("),")))

            if l.match(r'\)'):
                break

            l.require(r',')

        return dict(args=arguments,
                    kwargs=extrakw,
                    pos=extrapos,
                    wait=wait)

    def parse_regular_dialogue(l):
        """Parse a line of 'regular' dialogue as used by __call__"""

        who = l.simple_expression()
        if who == 'msg':
            renpy.error("msg CDS received instead of regular dialogue.")
        what = l.string()

        if not who or not what:
            renpy.error("msg requires a speaker and some dialogue")
        print("got who/what", who, what)

        # Parse the arguments
        arg_dict = c_parse_arguments(l, False)

        # If there are no arguments, raise an error to process this as
        # a msg CDS
        print("The argument dict for regular dialogue:")
        print(arg_dict['args'], "kwargs", arg_dict['kwargs'],
            "pos", arg_dict['pos'])
        if (not arg_dict['args'] and not arg_dict['kwargs']
                and not arg_dict['pos']):
            renpy.error("dialogue may not be regular")

        arg_info = renpy.ast.ArgumentInfo(arg_dict['args'],
                    arg_dict['pos'], arg_dict['kwargs'])

        return dict(who=who,
                    what=what,
                    arg_info=arg_info)

    def execute_regular_dialogue(p):
        """Turn a parsed line of regular dialogue into a proper dictionary."""

        try:
            who = eval(p['who'])
            what = p['what']
        except:
            renpy.error("Could not parse arguments of msg CDS")
            return

        args, kwargs = p['arg_info'].evaluate()

        pv = None
        img = False
        bounce = False
        spec_bubble = None

        # If there are any arguments, they get priority
        for i, arg in enumerate(args):
            if i == 0:
                pv = arg
            elif i == 1:
                img = arg
            elif i == 2:
                bounce = arg
            elif i == 3:
                spec_bubble = arg

        # Now the keywords
        if kwargs.get('pauseVal', None):
            pv = kwargs['pauseVal']
        if kwargs.get('img', False):
            img = kwargs['img']
        if kwargs.get('bounce', False):
            bounce = kwargs['bounce']
        if kwargs.get('specBubble', None):
            spec_bubble = kwargs['specBubble']

        # Turn this into an easily digestible dictionary
        return dict(who=who,
                    what=what,
                    pauseVal=pv,
                    img=img,
                    bounce=bounce,
                    specBubble=spec_bubble)


    ## A helper function to parse the choices of the menu. Modified from
    ## renpy/parser.py
    def parse_menu_options(stmtl, has_wait_time=False):
        l = stmtl.subblock_lexer()

        has_choice = False
        after_caption = False

        set = None

        pre_menu_block = []

        # Tuples of (label, condition, block)
        items = [ ]
        item_arguments = [ ]

        while l.advance():

            # The menu can have a set to exclude previously chosen items
            if l.keyword('set'):
                set = l.require(l.simple_expression)
                l.expect_eol()
                l.expect_noblock('timed menu set')
                continue

            # Try to parse for caption lines
            if not after_caption:
                state = l.checkpoint()

                # Try to parse it as the __call__ statement uses
                try:
                    if after_caption:
                        l.error("Cannot have a caption in the middle of a timed menu.")
                    caption = parse_regular_dialogue(l)
                    l.expect_eol()
                    l.expect_noblock('timed menu caption')
                    pre_menu_block.append(caption)
                    # Move on to the next line
                    continue
                except Exception as e:
                    print("WARNING: couldn't parse possible caption for timed menu")
                    print("Error was:", e)
                    l.revert(state)

                # Next try to parse it as a `msg` CDS
                try:
                    if after_caption:
                        l.error("Cannot have a caption in the middle of a timed menu.")
                    caption = parse_msg_stmt(l, msg_prefix=True)
                    l.expect_eol()
                    l.expect_noblock('timed menu caption')
                    pre_menu_block.append(caption)
                    # Move on to the next line
                    continue
                except Exception as e:
                    print("WARNING: couldn't parse possible caption for timed menu")
                    print("Error was:", e)
                    l.revert(state)


            # Otherwise, this item should be a choice
            has_choice = True
            after_caption = True
            condition = "True"

            label = l.string()

            if l.eol():

                if l.subblock:
                    l.error("Line is followed by a block, despite not being a "
                        + "menu choice. Did you forget a colon at the end of "
                        + "the line?")

                l.error("Timed menus need a speaker to say dialogue.")

            item_arguments.append(c_parse_arguments(l, include_wait=False))

            # Check for conditional statements
            if l.keyword('if'):
                condition = l.require(l.python_expression)

            l.require(':')
            l.expect_eol()
            l.expect_block('timed choice menuitem')

            block = parse_choice_block(l.subblock_lexer())

            items.append((label, condition, block))

        if not has_choice:
            stmtl.error("Menu does not contain any choices.")

        if has_wait_time and pre_menu_block:
            stmtl.error("Cannot specify a wait time and have a menu caption.")

        if not has_wait_time and not pre_menu_block:
            stmtl.error("If no wait time is specified, must provide a menu caption.")

        # Ideally we should end up with:
        # pre_menu_block : a block of msg-equivalent statements that are
        #       supposed to execute while the menu is displaying.
        # items : A list of (label, condition, block) that are the choices
        #       for this menu
        # set : The set to be used for this menu
        # item_arguments : A list of arguments corresponding to each choice item

        # Return these as a dictionary
        return dict(pre_menu_block=pre_menu_block,
                    items=items,
                    item_arguments=item_arguments,
                    menu_set=set)


    def parse_timed_menu(l):
        l.expect_block('timed menu statement')
        # Declare a given label as a global label
        label = l.label_name(declare=True)

        arguments_dict = c_parse_arguments(l)

        # IF we get an argument e.g. `timed menu (wait=5)` then this menu
        # is supposed to wait 5 seconds and will NOT have dialogue shown while
        # the menu is active
        if arguments_dict and arguments_dict['wait'] is not None:
            has_wait_time = True
        else:
            has_wait_time = False

        # It needs a colon and a newline
        l.require(':')
        l.expect_eol()

        choices_dict = parse_menu_options(l, has_wait_time)

        # Update the choices dictionary with the menu arguments
        choices_dict.update(arguments_dict)
        choices_dict['label'] = label

        return choices_dict

    def lint_timed_menu(p):
        return

    def execute_timed_menu(p):

        # Try to evaluate arguments passed to the menu
        arg_info = renpy.ast.ArgumentInfo(p['args'], p['pos'], p['kwargs'])
        args, kwargs = arg_info.evaluate()

        choices = [ ]
        narration = [ ]
        item_arguments = [ ]

        for i, (label, condition, block) in enumerate(p['items']):
            if renpy.config.say_menu_text_filter:
                label = renpy.config.say_menu_text_filter(label)

            choices.append((label, condition, i))

            # Add the arguments, or an empty tuple and dictionary if there
            # are none
            pargs = p['item_arguments']
            if pargs and pargs[i] is not None:
                arg_info = renpy.ast.ArgumentInfo(pargs[i]['args'],
                    pargs[i]['pos'], pargs[i]['kwargs'])
                item_arguments.append(arg_info.evaluate())
            else:
                item_arguments.append((tuple(), dict()))


        ## Dissect pre_menu_block into something displayable
        for msg in p['pre_menu_block']:
            if msg.get('arg_info', None):
                # It was written like regular dialogue
                print("parsing msg as regular dialogue.", msg)
                narration.append(execute_regular_dialogue(msg))
            else:
                print("parsing msg as CDS.", msg)
                narration.append(execute_msg_stmt(msg, return_dict=True))


        # Figure out how long to show this menu on-screen for. This is either
        # the `wait` argument or the length of time it will take to post all
        # the chat messages
        wait_time = 0
        if p['wait'] is not None:
            try:
                wait_time = eval(p['wait'])
            except:
                print("WARNING: Could not evaluate the length of time to show",
                    "the timed menu for.")
                wait_time = 8
        else:
            # Try to evaluate the messages in the pre-menu block
            try:
                for msg in narration:
                    msg_time = calculate_type_time(msg['what'])
                    if msg['pauseVal'] is not None:
                        msg_time *= msg['pauseVal']
                    wait_time += msg_time
            except:
                print("WARNING: Could not evaluate the 'what' part of all the",
                    "menu captions to calculate a time.")
                wait_time = 8

        # Now adjust the wait_time for the pv
        wait_time *= store.persistent.timed_menu_pv


        ## Look for keywords relating to how long these choices stay on-screen
        for a, kw in item_arguments:
            # Convert other arguments to more readable ones
            if kw.get('appear_after', None):
                kw['appear_before'] = kw['appear_after'] + 1
            if kw.get('disappear_after', None):
                kw['disappear_before'] = kw['disapper_after'] + 1

            if kw.get('appear_before', None):
                # There is a message during which this item should appear
                if kw['appear_before'] <= 1:
                    print("WARNING: A choice cannot appear before the timed menu.")
                    renpy.show_screen('script_error',
                        message=("A choice cannot appear before the timed menu."))
                else:
                    # Calculate the time this message should appear at. If the
                    # user wants it to appear before the 4th message, it should
                    # appear after the 3rd.
                    arg_appear = 0
                    for msg in narration[:(kw.get('appear_before', -1)-1)]:
                        msg_time = calculate_type_time(msg['what'])
                        if msg['pauseVal'] is not None:
                            msg_time *= msg['pauseVal']
                        arg_appear += msg_time
                    kw['appear_time'] = arg_appear

            if kw.get('disappear_before', None):
                # There is a message before which this message should disappear
                if (kw['disappear_before'] <= kw.get('appear_before', 1)):
                    print("WARNING: A timed menu choice cannot disappear",
                        "before it is shown.")
                    renpy.show_screen('script_error',
                        message=("A timed menu choice cannot disappear before"
                            + " it has been shown."))
                else:
                    arg_disappear = 0
                    for msg in narration[:kw.get('disappear_before', -1)]:
                        msg_time = calculate_type_time(msg['what'])
                        if msg['pauseVal'] is not None:
                            msg_time *= msg['pauseVal']
                        arg_disappear += msg_time
                    kw['disappear_time'] = arg_disappear
                    print_file("Got a disappear time of", kw['disappear_time'])


        ## OKAY time to parse the arguments for the set and conditions
        ## It looks like each item in regular choices is a tuple of
        ## (caption, ChoiceReturn) -> It's a MenuEntry tuple
        ## After it's picked it gets a third entry which is False (?)
        # `choice` is passed choices, set, args, kwargs, item_arguments
        # It calls these items,  set_expr, args, kwargs, item_arguments
        args = args or tuple()
        kwargs = kwargs or dict()

        # Filter out items already in the set
        if p['menu_set']:
            set = renpy.python.py_eval(p['menu_set'])

            new_items = [ ]
            new_item_arguments = [ ]

            for i, ia in zip(choices, item_arguments):
                if i[0] not in set:
                    new_items.append(i)
                    new_item_arguments.append(ia)

            items = new_items
            item_arguments = new_item_arguments
        else:
            items = choices
            set = None

        # Filter the list of items to only include ones for which the
        # condition is true.

        location=renpy.game.context().current

        new_items = [ ]

        for (label, condition, value), (item_args, item_kwargs) in zip(items, item_arguments):
            condition = renpy.python.py_eval(condition)

            if (not renpy.config.menu_include_disabled) and (not condition):
                continue

            if value is not None:
                new_items.append((label, renpy.ui.ChoiceReturn(label,
                        value, location, sensitive=condition, args=item_args,
                        kwargs=item_kwargs)))
            else:
                new_items.append((label, None))

        # Check to see if there's at least one choice in set of items:
        choices = [ value for label, value in new_items if value is not None ]

        # If not, bail out.
        if not choices:
            # Should just finish/go to post-execute label
            return None

        choices = new_items

        # Time to construct some choices
        # Currently choices is a list of (label, ChoiceReturn) tuples
        # Time to turn it into MenuEntries
        item_actions = [ ]
        for (label, value) in choices:
            if not label:
                value = None
            if isinstance(value, renpy.ui.ChoiceReturn):
                new_val = value
                chosen = value.get_chosen()
                item_args = value.args
                item_kwargs = value.kwargs
            elif value is not None:
                new_val = renpy.ui.ChoiceReturn(label, value, location)
                chosen = new_val.get_chosen()
                item_args = ()
                item_kwargs = { }
            else:
                new_val = None
                chosen = False
                item_args = ()
                item_kwargs = { }

            if renpy.config.choice_screen_chosen:
                me = renpy.exports.MenuEntry((label, new_val, chosen))
            else:
                me = renpy.exports.MenuEntry((label, new_val))

            me.value = new_val
            me.caption = label
            me.chosen = chosen
            me.args = item_args
            me.kwargs = item_kwargs
            if new_val:
                me.subparse = p['items'][new_val.value][2]
                me.action = Function(execute_timed_menu_action, item=me)
            else:
                me.subparse = None
                me.action = None

            item_actions.append(me)

        # Create a "dummy action" that can be used for autoanswer timed menu
        label = "(Say nothing)"
        value = renpy.ui.ChoiceReturn(label, item_actions[-1].value.value + 1,
            location, sensitive=True, args=tuple(), kwargs=dict())
        me = renpy.exports.MenuEntry((label, value))
        me.value = value
        me.caption = label
        me.chosen = value.get_chosen()
        me.args = tuple()
        me.kwargs = dict()
        me.subparse = False
        me.action = Function(execute_timed_menu_action, item=me,
                            jump_to_end=True)


        ## Now to pass this somewhere as a comprehensible object:
        menu_dict = dict(items=item_actions,
                        menu_args=args,
                        menu_kwargs=kwargs,
                        menu_set=set,
                        wait_time=wait_time,
                        narration=narration,
                        end_label=post_timed_menu(p),
                        autoanswer=me)
        store.timed_menu_dict = menu_dict
        renpy.jump('execute_timed_menu')



        return

    def predict_timed_menu(p):
        return [ ]

    def label_timed_menu(p):
        return p['label']

    def post_timed_menu(p):
        # Name of the label which points to the end of the menu
        # If we were given a name for this menu, use that
        if p['label']:
            return p['label'] + "_end_for_internal_use"
        # Otherwise, make up a label name based on the dialogue of the
        # first choice (or the second, as needed)
        try:
            name = []
            for j in range(len(p['items'])):
                lim = min(len(p['items'][j][0]), 6)
                name.extend([c for c in p['items'][j][0][1:lim] if c.isalpha()])
            lbl = ''.join(name)
            lbl += "_end_for_internal_use"
        except:
            print("ERROR: Couldn't figure out a name for the post_label")
            return 'this_didnt_work'
        return lbl


    renpy.register_statement('timed menu',
                            parse=parse_timed_menu,
                            lint=lint_timed_menu,
                            execute=execute_timed_menu,
                            predict=predict_timed_menu,
                            label=label_timed_menu,
                            #translation_strings=translate_timed_menu,
                            force_begin_rollback=True,
                            post_label=post_timed_menu,
                            block=True
                            )

    ########################################
    ## CONTINUOUS MENU CDS
    ########################################
    ## Definitions that simplify declaring a continuous menu
    def parse_continuous_menu(l):
        # This menu just expects a colon and a block, which is parsed
        # as Ren'Py script. It may also receive arguments or a label name.
        l.expect_block('continuous menu statement')
        # Declare a given label as a global label
        label = l.label_name(declare=True)

        arguments_dict = c_parse_arguments(l, include_wait=False)

        l.require(':')
        l.expect_eol()

        block = l.subblock_lexer().renpy_block()
        # Location is used to create a unique end label.
        loc = l.get_location()

        arguments_dict.update(dict(block=block,
                    loc=loc,
                    label=label))
        return arguments_dict

    def lint_continuous_menu(p):
        return

    def convert_node_to_time(node):
        """Return how long a node should be on-screen for."""

        if isinstance(node, renpy.ast.Say):
            # May have been passed a pauseVal argument. If so, need to factor
            # that in.
            mult = 1.0
            if node.arguments:
                args, kwargs = node.arguments.evaluate()
                if kwargs.get('pauseVal', -1) >= 0:
                    mult = kwargs['pauseVal']
            t = calculate_type_time(node.what)
            t *= mult
            print_file("Node's dialogue is", node.what, t)
            return t
        if isinstance(node, renpy.ast.UserStatement):
            if node.parsed[0] == ('msg',):
                # This is a msg CDS
                np = node.parsed[1]
                # Factor in the pauseVal, if present.
                mult = 1.0
                if np['pv'] != "None":
                    mult = eval(np['pv'])
                t = calculate_type_time(np['what'])
                t *= mult
                print_file("Node's msg dialogue is", np['what'], t)
                return t

            elif (node.parsed[0] in [('enter', 'chatroom',),
                    ('exit', 'chatroom',)]):
                # This is a message like "XYZ has entered the chatroom."
                return store.enter_exit_modifier
            else:
                return 0.0

        if isinstance(node, renpy.ast.Translate):
            # A Translate block typically contains a Say statement inside
            # its block. Extract the time from that.
            print_file("Translate block contains", node.block)
            return convert_node_to_time(node.block)

        if isinstance(node, renpy.ast.Call):
            # Maintained for backwards compatibility. Allows users to still
            # use `call enter(ja)` instead of `enter chatroom ja`.
            if node.label not in ['exit', 'enter']:
                return 0.0
            return store.enter_exit_modifier

        elif isinstance(node, renpy.ast.If):
            ## This is a tricky case; need to evaluate if there are
            ## any statements in this If node that should be evaluated.
            for condition, block in node.entries:
                if renpy.python.py_eval(condition):
                    return convert_node_to_time(block)
            return 0.0

        # For an unknown reason, testing isinstance(node, list) does not always
        # return True even if the item in question is ostensibly a list. The
        # try/catch block checks if it can be accessed as a list and sets a
        # flag if this is the case.
        is_list = True
        try:
            x = node[0]
        except:
            is_list = False

        if isinstance(node, list) or is_list:
            result = 0.0
            for n in node:
                result += convert_node_to_time(n)
            return result

        # This node is not recognized as containing dialogue; return zero.
        return 0.0


    def execute_continuous_menu(p):

        # Try to evaluate arguments passed to the menu
        arg_info = renpy.ast.ArgumentInfo(p['args'], p['pos'], p['kwargs'])
        margs, mkwargs = arg_info.evaluate()

        choice_id_lookup = {}
        choice_begin_lookup = {}
        # List of ChoiceInfo objects
        choices = [ ]

        after_menu_node = renpy.game.context().next_node

        ## STEP ONE
        ## Parse all the nodes in the SubParse block. In particular, look for
        ## choice and end choice CDSs to construct ChoiceInfo objects.
        try:
            for i, node in enumerate(p['block'].block):

                if isinstance(node, renpy.ast.UserStatement):
                    # Get the parsed dictionary for the node
                    np = node.parsed[1]
                    if node.parsed[0] == ('choice',):
                        ## Got a choice
                        choice_id_lookup[np['choice_id']] = i
                        dialogue_nodes.append(None)
                        choice_begin_lookup[i] = np['choice_id']

                    elif node.parsed[0] == ('end', 'choice',):
                        ## Mark the end of the choice
                        ## Fetch the id
                        b_num = choice_id_lookup.get(np['choice_id'], None)
                        if b_num is None:
                            renpy.error("Need an identifier for choice statements.")
                        # Add i+1 as the end index because the statement after
                        # this one will be the PostUserStatement node
                        choices.append(ChoiceInfo(b_num, i+1, np['choice_id']))
                        dialogue_nodes.append(None)

        except:
            print_file("WARNING: Couldn't parse the choices.")

        # If a choice doesn't have a pair, assume it ends at the end
        # of the menu as a whole.
        beginning_ids = [b.begin for b in choices ]
        no_end_ids = [b for b in choice_id_lookup.values() if b not in beginning_ids]
        for i in no_end_ids:
            choices.append(ChoiceInfo(i, -1, choice_begin_lookup[i]))

        ## STEP TWO
        ## Convert all dialogue nodes into a time, which is how long it takes
        ## to post that dialogue.
        node_times = [ ]
        for node in p['block'].block:
            node_times.append(convert_node_to_time(node))

        # Now figure out how long each choice remains on-screen for.
        # Add this information to the ChoiceInfo object.
        for c in choices:
            dialogue_time = 0
            # Look through the nodes in this section
            final = p['block'].block[c.end]
            if c.end == -1:
                c.end = len(node_times)-1
                final = after_menu_node
                c.end_with_menu = True
            for t in node_times[c.begin:c.end+1]:
                dialogue_time += t

            c.wait_time = dialogue_time
            c.final_node = final
            ## Add the choice's parsed dictionary
            c.choice_dict = p['block'].block[c.begin].parsed[1]


        print_file("This is the ammended choice pairs list:")
        for c in choices:
            print_file(c)


        ## STEP THREE
        ## Filter out choices whose conditions are not True.
        new_items = [ ]
        location = renpy.game.context().current

        for c in choices:

            condition = renpy.python.py_eval(c.choice_dict['condition'])

            if (not renpy.config.menu_include_disabled) and (not condition):
                continue

            # Get the choice arguments
            item_args = c.choice_dict['args']
            arg_info = renpy.ast.ArgumentInfo(item_args['args'],
                        item_args['pos'], item_args['kwargs'])
            args, kwargs = arg_info.evaluate()
            label = c.choice_dict['label']

            new_items.append((label, renpy.ui.ChoiceReturn(label, c.begin,
                location, sensitive=condition, args=args, kwargs=kwargs), c))

        if len(new_items) == 0:
            # There are no choices to show the player; should just
            # execute the dialogue nodes
            return None

        ## STEP 4
        ## Calculate the maximum number of choices that are on-screen at
        ## any given time. Should have a list of tuples that have begin/end
        ## node information.
        max_choices = 1
        for l, r, c in new_items:
            print_file("Looking at choice (", c.begin, ",", c.end, ")")
            current_choices = 0
            if i == len(new_items) - 1:
                break

            if c.end == -1:
                final = len(p['block'].block) - 1
            else:
                final = c.end

            for l2, r2, c2 in new_items:
                print_file("Checking if", c2.begin, "in range", c.begin, "-", final)
                if c2.begin in range(c.begin, final):
                    current_choices += 1

                if current_choices >= 3:
                    break

            # TODO: Maybe throw an error if more than 3 choices are on-screen
            if current_choices >= 3:
                max_choices = 3
                break


        ## STEP 5
        ## Construct the MenuEntry objects that will be used to display
        ## these choices on-screen.
        item_actions = [ ]
        choice_id_dict = { }
        for (label, value, info) in new_items:
            chosen = value.get_chosen()
            item_args = value.args
            item_kwargs = value.kwargs

            me = renpy.exports.MenuEntry((label, value, chosen))

            me.value = value
            me.caption = label
            me.chosen = chosen
            me.args = item_args
            me.kwargs = item_kwargs
            me.info = info
            me.wait = info.wait_time
            me.choice_id = info.choice_id
            me.block = info.construct_action(p['block'].block)
            me.action = Function(execute_continuous_menu_action, item=me)
            choice_id_dict[me.choice_id] = me
            item_actions.append(me)

        store.c_menu_dict = dict(items=item_actions,
                                end_label=post_continuous_menu(p),
                                narration=p['block'].block,
                                choice_id_dict=choice_id_dict,
                                max_choices=max_choices,
                                showing_choices=dict(),
                                node_times=node_times,
                                available_choices=[],
                                autoanswer=None,
                                menu_args=margs,
                                menu_kwargs=mkwargs)

        renpy.jump('execute_continuous_menu')

        return

    def label_continuous_menu(p):
        return p['label']

    def post_continuous_menu(p):
        """Return a label which leads to the end of the menu."""

        name = [c for c in p['loc'][0][0:-4] if c.isalpha()]
        lbl = ''.join(name)
        return 'end_for_internal_use_' + lbl + '_' + str(p['loc'][1])

    def post_execute_c_menu(p):
        """This executes after the continuous menu is complete."""

        print_file("executing after c menu")
        if store.persistent.use_timed_menus:
            renpy.hide_screen("c_choice_1")
            renpy.hide_screen("c_choice_2")
            renpy.hide_screen("c_choice_3")
            renpy.hide_screen("c_choice_4")
            renpy.hide_screen("timed_menu_messages")
            no_anim_list = store.chatlog[-20:-1]
            renpy.show_screen('messenger_screen', no_anim_list=no_anim_list,
                    animate_down=True)
            store.c_menu_dict = {}
            store.on_screen_choices = 0
            store.last_shown_choice_index = None
            return

        print_file("c_menu_dict is", store.c_menu_dict)
        if store.c_menu_dict.get('narration', None) is None:
            store.c_menu_dict = {}
            store.on_screen_choices = 0
            store.last_shown_choice_index = None
            return

        ## Need to look through all choices for those which end at the
        ## same time as the menu.
        for i in store.c_menu_dict['items']:
            store.c_menu_dict['available_choices'] = []
            if i.info.end_with_menu:
                if not store.persistent.use_timed_menus:
                    ## Add this choice to the available choices
                    store.c_menu_dict['available_choices'].append(i)

        ## Show any remaining choices to the user, along with an option
        ## to remain silent.
        if len(store.c_menu_dict.get('available_choices', [])) < 1:
            ## The player has already chosen any answers that would end
            ## at the end of the menu; nothing to show, so return.
            return

        # Create a "dummy action" that can be used for autoanswer timed menu
        label = "(Say nothing)"
        location = renpy.game.context().current
        value = renpy.ui.ChoiceReturn(label, 1, location, sensitive=True,
                                    args=tuple(), kwargs=dict())
        me = renpy.exports.MenuEntry((label, value))
        me.value = value
        me.caption = label
        me.chosen = value.get_chosen()
        me.args = tuple()
        me.kwargs = dict()
        me.jump_to_label = post_continuous_menu(p)
        me.action = Function(execute_continuous_menu_action, item=me,
                            say_nothing=True)
        store.c_menu_dict['autoanswer'] = me
        # The menu dictionary should be erased after this set of choices
        # is shown so the game can continue with the rest of the chatroom.
        store.c_menu_dict['erase_menu'] = True
        renpy.jump('play_continuous_menu_no_timer')
        return

    renpy.register_statement('continuous menu',
                            parse=parse_continuous_menu,
                            lint=lint_continuous_menu,
                            execute=execute_continuous_menu,
                            label=label_continuous_menu,
                            force_begin_rollback=True,
                            post_label=post_continuous_menu,
                            post_execute=post_execute_c_menu,
                            block=True
                            )

    ## CHOICE CDS
    ## A CDS used in tandem with the continuous menu CDS to create
    ## continuous menus.
    def parse_choice_stmt(l):
        choice_id = l.simple_expression()
        if choice_id is None:
            renpy.error("Choice statement requires an identifier")

        # Get caption
        label = l.string()
        # Check for arguments
        args = c_parse_arguments(l, include_wait=False)
        # Check for conditional statements
        condition = 'True'
        if l.keyword('if'):
            condition = l.require(l.python_expression)

        l.require(':')
        l.expect_eol()
        l.expect_block('continuous menu choice')

        block = parse_choice_block(l.subblock_lexer())

        loc = l.get_location()

        return dict(choice_id=choice_id,
                    label=label,
                    condition=condition,
                    args=args,
                    loc=loc,
                    block=block)

    def execute_choice_stmt(p, recalculate_time=False, begin=-1):

        ## Only show this choice if the condition is True
        condition = renpy.python.py_eval(p['condition'])
        if (not renpy.config.menu_include_disabled) and (not condition):
            return

        # Retrieve the MenuEntry item associated with this choice.
        item = store.c_menu_dict['choice_id_dict'][p['choice_id']]

        if not store.persistent.use_timed_menus:
            ## If timed menus are turned off, don't show a choice screen
            ## until one or more choices are about to expire. Add this choice
            ## to the list of choices that are currently available.
            store.c_menu_dict['available_choices'].append(item)
            return

        # Indicates this choice should have a different animation when entering.
        first_choice = False

        ## Might need to recalculate how long this choice is on-screen for.
        ## Generally used if the player made a choice that led them to an
        ## end choice statement and the menu continues on.
        if recalculate_time:
            ## Get the parent node times
            node_times = store.c_menu_dict['node_times']
            new_choice_end = item.info.end + 1
            wait = 0
            for node in node_times[begin:new_choice_end]:
                wait += node

            # If wait is 0, this choice shouldn't be on-screen. This may occur
            # if the only nodes after the end choice are python statements
            # or other non-dialogue nodes.
            if wait <= 0:
                return

            new_info = item.info
            new_info.wait_time = wait
            new_info.begin = begin
            ## Construct a new MenuEntry for this node with the new wait info
            me = renpy.exports.MenuEntry((item.caption, item.value, item.chosen))

            me.value = item.value
            me.caption = item.caption
            me.chosen = item.chosen
            me.args = item.args
            me.kwargs = item.kwargs
            me.info = new_info
            me.wait = wait
            me.choice_id = item.choice_id
            me.block = item.block
            me.action = Function(execute_continuous_menu_action, item=me)
            ## Replace the choice in the id dictionary with this new version.
            store.c_menu_dict['choice_id_dict'][me.choice_id] = me
            ## Remove the original item from the menu items and add the
            ## new version.
            store.c_menu_dict['items'].remove(item)
            item = me
            store.c_menu_dict['items'].append(item)

        # Show the messenger screen animating up to reveal the choices
        if store.on_screen_choices <= 0:
            first_choice = True
            renpy.hide_screen("messenger_screen")
            no_anim_list = store.chatlog[-20:-1]
            renpy.show_screen("timed_menu_messages", no_anim_list=no_anim_list)

        # Test if this item is being shown at the "same" time as another choice,
        # which is the first choice. Therefore they should both receive the
        # same entrance animation.
        if store.last_shown_choice_index is None:
            first_choice = True
            store.last_shown_choice_index = (item.info.begin, True)
        elif ((store.last_shown_choice_index[0] + 2 == item.info.begin
                    or store.last_shown_choice_index[0] + 1 == item.info.begin
                    or store.last_shown_choice_index[0] == item.info.begin)
                and store.last_shown_choice_index[1]):
            first_choice = True
            store.last_shown_choice_index = (item.info.begin, True)
        else:
            store.last_shown_choice_index = (item.info.begin, first_choice)

        ## Allocate a choice box to display the choice in
        renpy.show_screen(allocate_choice_box(p['choice_id']), i=item,
                        first_choice=first_choice)
        ## The number of choices that are on-screen increases.
        store.on_screen_choices += 1
        return

    def post_choice_stmt(p):
        """Return a label to jump to for the end of this choice statement."""

        lim = min(len(p['label']), 6)
        name = [c for c in p['label'][1:lim] if c.isalpha()]
        lbl = ''.join(name)
        return "choice_" + p['choice_id'] + "_" + lbl + '_' + str(p['loc'][1])

    renpy.register_statement('choice',
                            parse=parse_choice_stmt,
                            execute=execute_choice_stmt,
                            post_label=post_choice_stmt,
                            block=True)
    ## END CHOICE CDS
    ## A CDS used alongside the choice CDS inside the continuous menu CDS to
    ## create a continuous menu.
    def parse_end_choice(l):
        # End choice only gets an identifier; no block.
        choice_id = l.simple_expression()
        if choice_id is None:
            renpy.error("choice end requires an identifier")
        loc = l.get_location()
        return dict(choice_id=choice_id,
                    loc=loc)

    def execute_end_choice(p):

        if (not store.persistent.use_timed_menus
                and not store.c_menu_dict.get('item', None)):
            ## Show this choice to the user, along with an option to remain
            ## silent.
            item = store.c_menu_dict['choice_id_dict'][p['choice_id']]
            # Create a "dummy action" that can be used for autoanswer timed menu
            label = "(Say nothing)"
            location = renpy.game.context().current
            value = renpy.ui.ChoiceReturn(label, 1,
                location, sensitive=True, args=tuple(), kwargs=dict())
            me = renpy.exports.MenuEntry((label, value))
            me.value = value
            me.caption = label
            me.chosen = value.get_chosen()
            me.args = tuple()
            me.kwargs = dict()
            me.jump_to_label = post_end_choice(p)
            me.action = Function(execute_continuous_menu_action, item=me,
                                say_nothing=True)
            store.c_menu_dict['autoanswer'] = me
            print_file("Calling execute_end_choice with", p['choice_id'])
            renpy.jump('play_continuous_menu_no_timer')

        ## Find the screen this choice is showing on and hide it.
        which_screen = store.c_menu_dict['showing_choices'].get(
            p['choice_id'], None)
        if which_screen:
            store.on_screen_choices -= 1
            # Add this screen to the recently_hidden_choice_screens list so
            # the program does not immediately choose it to display a new
            # choice, causing abrupt animations.
            if which_screen in store.recently_hidden_choice_screens:
                store.recently_hidden_choice_screens.remove(which_screen)
            store.recently_hidden_choice_screens.append(which_screen)

        ## If there are no choices left on-screen, slide the messages back
        ## down into place.
        if (store.on_screen_choices <= 0
                and renpy.get_screen('timed_menu_messages')):
            renpy.hide_screen("timed_menu_messages")
            no_anim_list = store.chatlog[-20:]
            renpy.show_screen('messenger_screen', no_anim_list=no_anim_list)

        return

    def post_end_choice(p):
        return 'end_for_internal_use_' + p['choice_id'] + '_' + str(p['loc'][1])

    def post_execute_end_choice(p):
        print("Calling post_execute_end_choice with", p['choice_id'])
        ## Grab the ending index of this choice
        choice_id_dict = store.c_menu_dict['choice_id_dict']
        item = choice_id_dict[p['choice_id']]
        end = item.info.end
        ## Add one so it starts *after* the PostUserStatement
        end += 1

        ## Remove this item from the menu items list
        if item in store.c_menu_dict['items']:
            store.c_menu_dict['items'].remove(item)
        if item in store.c_menu_dict['available_choices']:
            store.c_menu_dict['available_choices'].remove(item)

        ## This choice is no longer showing
        store.c_menu_dict['showing_choices'][p['choice_id']] = None

        ## Remove this choice from the dictionary as it's already been chosen
        ## or its time has passed
        choice_id_dict[p['choice_id']] = None

        if (store.c_menu_dict.get('item', None)
                or not store.persistent.use_timed_menus):
            ## If this isn't at the end of the menu, re-show any remaining
            ## choices. Reset the number that are on-screen.
            store.on_screen_choices = 0
            ## Reset the showing choices dictionary
            store.c_menu_dict['showing_choices'] = dict()

            ## Need to look through all choices for those who begin *before*
            ## end, and end *after* end.
            for i in store.c_menu_dict['items']:
                print_file("Looking at", i.info.choice_id, ":", i.info.begin,
                    ",", i.info.end)
                print_file("end is", end)
                store.c_menu_dict['available_choices'] = []
                if i.info.begin < end and i.info.end > end:
                    if not store.persistent.use_timed_menus:
                        ## Add this choice to the available choices
                        print_file("Added", i.info.choice_id, "to available choices.")
                        store.c_menu_dict['available_choices'].append(i)
                    ## Show this choice when the menu resumes
                    else:
                        execute_choice_stmt(i.info.choice_dict,
                            recalculate_time=True, begin=end)

        store.c_menu_dict['item'] = None
        return


    renpy.register_statement('end choice',
                            parse=parse_end_choice,
                            execute=execute_end_choice,
                            post_label=post_end_choice,
                            post_execute=post_execute_end_choice,
                            )

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

