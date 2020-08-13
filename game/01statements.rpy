python early hide:

    ########################################
    ## ENTER AND EXIT CHATROOM CDS
    ########################################

    def parse_enter_exit(l):
        who = l.simple_expression()
        if not who:
            renpy.error("chatroom enter/exit requires a character.")
        return dict(who=who)

    def execute_enter_chat(p):
        if p["who"] is not None:
            who = eval(p["who"])
        else:
            renpy.error("enter chatroom requires a ChatCharacter")
        
        if who is None or not isinstance(who, ChatCharacter):
            print("WARNING: variable %s provided to enter chatroom is not recognized as a ChatCharacter." % p["who"])
            renpy.show_screen('script_error',
                message="Variable %s provided to enter chatroom is not recognized as a ChatCharacter.",
                link="Useful-Chatroom-Functions#how-to-make-a-character-enterexit-the-chatroom",
                link_text="How to make a character enter/exit the chatroom")
            return
        
        enter_string = who.name + " has entered the chatroom."
        if (not store.observing and not store.persistent.testing_mode
                and not store.vn_choice
                and renpy.get_screen('phone_overlay')):
            # Add this as a replay entry
            enter_entry = ("enter", who)
            store.current_chatroom.replay_log.append(enter_entry)
        
        addchat(store.special_msg, enter_string, store.pv)
        if who.name not in store.in_chat:
            store.in_chat.append(who.name)

        if not store.observing:
            store.current_chatroom.add_participant(who)
        
        # Refresh the screen
        renpy.restart_interaction()
        return

    def execute_exit_chat(p):
        if p["who"] is not None:
            who = eval(p["who"])
        else:
            renpy.error("exit chatroom requires a ChatCharacter")
        
        if who is None or not isinstance(who, ChatCharacter):
            print("WARNING: variable %s provided to exit chatroom is not recognized as a ChatCharacter." % p["who"])
            renpy.show_screen('script_error',
                message="Variable %s provided to exit chatroom is not recognized as a ChatCharacter.",
                link="Useful-Chatroom-Functions#how-to-make-a-character-enterexit-the-chatroom",
                link_text="How to make a character enter/exit the chatroom")
            return
        
        exit_string = who.name + " has left the chatroom."
        if (not store.observing and not store.persistent.testing_mode
                and not store.vn_choice
                and renpy.get_screen('phone_overlay')):
            # Add this as a replay entry
            exit_entry = ("exit", who)
            store.current_chatroom.replay_log.append(exit_entry)
        
        addchat(store.special_msg, exit_string, store.pv)
        if who.name in store.in_chat:
            store.in_chat.remove(who.name)
        
        # Refresh the screen
        renpy.restart_interaction()
        return

    def lint_enter_exit(l):
        who = p["who"]
        eval_who = None
        try:
            eval_who = eval(p["who"])
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
    def parse_message_args(what, ffont, bold, xbold, big, img, spec_bubble):
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
        if big:
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

    def parse_sub_block(l, messages=[]):
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
                    line = parse_msg_stmt(l, check_time=True)
                    messages.append(line)       
                except:
                    try:
                        # If that didn't work, assume it's a python conditional
                        messages.append(l.delimited_python(':'))
                    except:
                        print_file("Couldn't get the delimited python")
                    try:
                        ll = l.subblock_lexer()
                        messages = parse_sub_block(ll, messages)
                        messages.append('end')
                        continue                        
                    except:
                        print_file("Couldn't parse the subblock")
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

        # Parse the statements in the subblock and store it
        messages = [ ]
        ll = l.subblock_lexer()
        # This function recursively calls itself to check all sub-blocks
        messages = parse_sub_block(ll, messages)       
        
        return dict(who=who,
                    day=day,
                    messages=messages)
    
    def predict_backlog_stmt(p):
        return [ ]

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
        for d in p['messages']:
            if isinstance(d, dict):
                if not condition:
                    continue
                try:
                    who = eval(d["who"])       
                    what = eval(d["what"])
                    ffont = d["ffont"]            
                    bold = d["bold"]
                    xbold = d["xbold"]        
                    big = d["big"]
                    img = d["img"]        
                    timestamp = d['timestamp']
                except:
                    print("WARNING: The arguments for dialogue %s could not "
                        + "be evaluated." % p['what'])
                    renpy.show_screen('script_error',
                            message=("The arguments for dialogue %s could not " 
                                + "be evaluated." % p['what']))
                    return

                # Get the correct dialogue and img
                dialogue, img, spec_bubble = parse_message_args(                
                    what, ffont, bold, xbold, big, img, False)
                # Create the 'when' timestamp
                if timestamp:
                    when = upTime(day, timestamp)
                else:
                    when = upTime(day)
                sender.text_backlog(who, dialogue, when, img)      
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
                        + "for line with dialogue %s" % p['what'])
                    renpy.show_screen('script_error',
                        message="Could not evaluate conditional statement "
                            + "for line with dialogue %s" % p['what'])
                    return                  
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
                    what = eval(d["what"])
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

    
    def parse_msg_stmt(l, check_time=False):

        who = l.simple_expression()
        # This is also used to parse backlogs; if it begins with if/elif/else
        # then we were trying to evaluate a python string so it should raise
        # an error and stop parsing
        if who in ['elif', 'if', 'else']:
            raise AttributeError
        what = l.simple_expression()

        if not who or not what:
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


    def execute_msg_stmt(p):
        try:
            who = eval(p["who"])       
            what = eval(p["what"])        
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
        # or a text message
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
                    store.current_chatroom.replay_log.append(ReplayEntry(
                            who, dialogue, new_pv, img, bounce, spec_bubble))
                
            # Now add this dialogue to the chatlog
            addchat(who, dialogue, pauseVal=pv, img=img, bounce=bounce,
                specBubble=spec_bubble)
        
        return

    def lint_msg_stmt(p):        
        try:
            who = eval(p["who"])       
            what = eval(p["what"])        
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
        return [ ]
    
    def warp_msg_stmt(p):
        return True
    

    renpy.register_statement('msg',
        parse=parse_msg_stmt,
        execute=execute_msg_stmt,
        predict=predict_msg_stmt,
        lint=lint_msg_stmt,
        warp=warp_msg_stmt)
    
    renpy.register_statement('add backlog',
        parse=parse_backlog_stmt,
        execute=execute_backlog_stmt,
        predict=predict_backlog_stmt,
        lint=lint_backlog_stmt,
        warp=warp_msg_stmt,
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
                        # store.chatroom_hp += 1
                        if bad:
                            store.chatroom_hp['bad'].append(who)
                        else:
                            store.chatroom_hp['good'].append(who)
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
        return [ ]
    
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
                store.chatroom_hp['break'].append(who)
            store.persistent.HP -= 1

            if store.persistent.animated_icons:
                renpy.show_screen('heart_break_screen', character=who)
            else:
                msg = who.name + " -1"
                renpy.show_screen(allocate_notification_screen(True), msg)
        return

    renpy.register_statement('break heart',
        parse=parse_break_heart,
        execute=execute_break_heart,
        predict=predict_award_heart,
        lint=lint_award_heart,
        warp=warp_award_heart)

    # This duplicates the above statement, just switches the words to account
    # for possible error checking.
    renpy.register_statement('heart break',
        parse=parse_break_heart,
        execute=execute_break_heart,
        predict=predict_award_heart,
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
                store.current_chatroom.replay_log.append(music_entry)
        
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

