python early hide:
    ########################################
    ## TIMED MENU CDS
    ########################################
    ## Definitions that simplify declaring a timed menu
    ## This is a helper to parse choice blocks
    def parse_choice_block(l):

        choice_block = l.renpy_block(empty=True)

        return choice_block

    def construct_menu(stmtl, has_wait_time=False):
        """
        A helper function which separates out the choices and narration
        and collects relevant arguments/conditions etc.
        """

        l = stmtl.subblock_lexer()

        has_choice = False
        after_caption = False

        set = None

        pre_menu_block = [ ]

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

            # Try to parse this as a choice
            state = l.checkpoint()

            condition = 'True'

            try:
                label = l.string()
                if not label:
                    raise

                if l.eol():
                    if l.subblock:
                        # No colon indicating a block
                        l.error("Line is followed by a block, despite not "
                            + "being a menu choice. Did you forget a colon at "
                            + "the end of the line?")
                    l.error("Timed menus require a speaker to say dialogue.")

                item_arguments.append(c_parse_arguments(l, include_wait=False))

                # Check for conditional statements
                if l.keyword('if'):
                    condition = l.require(l.python_expression)

                l.require(':')
                l.expect_eol()
                l.expect_block('timed choice menuitem')

                block = parse_choice_block(l.subblock_lexer())

                items.append((label, condition, block))

                has_choice = True

                continue
            except:
                l.revert(state)

            # This wasn't a menu choice; grab it as a Ren'Py line
            try:
                pre_menu_block.append(l.renpy_statement())
            except:
                l.error("Could not parse the given timed menu narration.")

        if not has_choice:
            stmtl.error("Timed menu does not contain any choices.")

        if has_wait_time and pre_menu_block:
            stmtl.error("Cannot specify a timed menu wait time and have a menu caption.")

        if not has_wait_time and not pre_menu_block:
            stmtl.error("If no wait time is specified, must provide a timed menu caption.")

        return dict(pre_menu_block=pre_menu_block,
                    items=items,
                    item_arguments=item_arguments,
                    menu_set=set)

    def subparse_to_nodes(sp):
        """
        Convert a list of SubParse objects and lists of SubParse objects
        into one list of nodes.
        """

        nodes = [ ]
        if isinstance(sp, renpy.parser.SubParse):
            nodes.extend(sp.block)
        is_list = True
        try:
            x = sp[0]
        except:
            is_list = False

        if isinstance(sp, list) or is_list:
            for node in sp:
                nodes.extend(subparse_to_nodes(node))

        return nodes

    def parse_timed_menu(l):
        l.expect_block('timed menu statement')
        # Declare a given label as a global label
        label = l.label_name(declare=True)

        arguments_dict = c_parse_arguments(l)

        # If the program gets an argument e.g. `timed menu (wait=5)` then this
        # menu is supposed to wait 5 seconds and will NOT have dialogue shown
        # while the menu is active.
        if arguments_dict and arguments_dict['wait'] is not None:
            has_wait_time = True
        else:
            has_wait_time = False

        # It needs a colon and a newline
        l.require(':')
        l.expect_eol()

        # Now parse the menu for narration and choices
        # choices_dict = parse_menu_options(l, has_wait_time)
        choices_dict = construct_menu(l, has_wait_time)

        # Update the choices dictionary with the menu arguments
        choices_dict.update(arguments_dict)
        choices_dict['label'] = label

        return choices_dict

    def execute_timed_menu(p):

        # Try to evaluate arguments passed to the menu
        arg_info = renpy.ast.ArgumentInfo(p['args'], p['pos'], p['kwargs'])
        args, kwargs = arg_info.evaluate()
        args = args or tuple()
        kwargs = kwargs or dict()

        choices = [ ]
        narration = [ ]
        item_arguments = [ ]

        # Fetch the next node
        after_menu_node = renpy.game.context().next_node

        if p['wait'] is None:
            # Construct one giant block out of all the items in pre_menu_block
            narration = subparse_to_nodes(p['pre_menu_block'])

            # Link all the narration nodes together
            renpy.ast.chain_block(narration, after_menu_node)

            # Calculate how long it will take to play the narration
            wait_time = convert_node_to_time(narration)
        else:
            try:
                wait_time = eval(p['wait'])
            except:
                print("WARNING: Could not evaluate the length of time to show",
                    "the timed menu for.")
                wait_time = 8
            # Don't need a buffer for explicitly given wait times
            wait_time -= store.end_menu_buffer

        # Adjust the wait time for the timed menu pv
        wait_time *= store.persistent.timed_menu_pv

        # Create the choices
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

        # Time to parse the arguments for the set and conditions.
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

        menu_dict = dict(items=[],
                        menu_args=args,
                        menu_kwargs=kwargs,
                        menu_set=set,
                        wait_time=wait_time,
                        narration=narration,
                        end_label=post_timed_menu(p))

        # Filter the list of items to only include ones for which the condition
        # is True.

        location = renpy.game.context().current

        new_items = [ ]


        for (label, condition, value), (item_args,
                item_kwargs) in zip(items, item_arguments):

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


        if not choices:
            # There are no choices which can be shown to the player. Should
            # the narration be shown?
            if kwargs.get('show_empty', None):
                # This menu should be shown regardless
                store.timed_menu_dict = menu_dict
                renpy.jump('execute_timed_menu')
            elif kwargs.get('show_empty', None) is not None:
                # This menu should not be shown; skip
                return
            elif store.show_empty_menus:
                # Show this menu
                store.timed_menu_dict = menu_dict
                renpy.jump('execute_timed_menu')
            else:
                # Don't show the menu
                return
            # Should just finish/go to post-execute label
            return None

        choices = new_items

        # Time to construct some choices and turn them into MenuEntry objects.
        # Currently choices is a list of (label, ChoiceReturn) tuples
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
        menu_dict.update(dict(items=item_actions,
                        autoanswer=me))

        store.timed_menu_dict = menu_dict
        renpy.jump('execute_timed_menu')

    def lint_timed_menu(p):
        return

    def predict_timed_menu(p):
        return [ ]

    def label_timed_menu(p):
        return p['label']

    def post_timed_menu(p):
        # Name of the label which points to the end of the menu
        # If a label for this menu was given, use that.
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

    def post_execute_timed_menu(p):
        ## This function plays after the timed menu has been executed
        if store.timed_menu_dict and not store.timed_menu_dict.get('item', None):
            renpy.jump('end_of_timed_menu')
        return

    renpy.register_statement('timed menu',
                            parse=parse_timed_menu,
                            lint=lint_timed_menu,
                            execute=execute_timed_menu,
                            predict=predict_timed_menu,
                            label=label_timed_menu,
                            #translation_strings=translate_timed_menu,
                            force_begin_rollback=True,
                            post_label=post_timed_menu,
                            post_execute=post_execute_timed_menu,
                            block=True
                            )
    ########################################
    ## CONTINUOUS MENU CDS
    ########################################
    ## Definitions that simplify declaring a continuous menu
    def parse_continuous_menu(l):
        # This menu just expects a colon and a block, which is parsed as
        # Ren'Py script. It may also receive arguments or a label name.
        l.expect_block('continuous menu statement')
        # Check if there is a label
        label = l.label_name(declare=True)

        # Get any arguments
        arguments_info = renpy.parser.parse_arguments(l)

        # Require a colon and newline
        l.require(':')
        l.expect_eol()

        # Fetch the block
        block = l.subblock_lexer().renpy_block()

        # Fetch location to create unique labels
        loc = l.get_location()

        return dict(loc=loc,
                    block=block,
                    label=label,
                    arg_info=arguments_info)

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

        # Ensure the program is not interrupted while doing these calculations
        store.block_interrupts = True
        # Evaluate the menu arguments
        if p['arg_info']:
            margs, mkwargs = p['arg_info'].evaluate()
        else:
            margs = tuple()
            mkwargs = dict()

        # Establish the node after the menu
        after_menu_node = renpy.game.context().next_node
        next_dialogue = after_menu_node.next
        # Make sure it's the node after the narration
        p['block'].block[-1].next = after_menu_node

        # Ensure the nodes in this block are linked
        renpy.ast.chain_block(p['block'].block, after_menu_node)

        # Create a lookup dictionary for getting an id from an index
        choice_id_from_index = {}
        # Create a lookup dictionary for getting a beginning index from an id
        choice_begin_from_id = {}
        # List of ChoiceInfo objects
        choices = [ ]

        ## STEP ONE
        ## Look through all the nodes in the SubParse block and extract the
        ## needed information. In particular, look for `choice` and `end choice`
        ## CDSs to construct ChoiceInfo objects.
        try:
            for i, node in enumerate(p['block'].block):
                if isinstance(node, renpy.ast.UserStatement):
                    # Get the node's parsed dictionary
                    np = node.parsed[1]
                    if node.parsed[0] == ('choice',):
                        # Got a choice. Add the ID and index to the appropriate
                        # dictionaries.
                        choice_id_from_index[i] = np['choice_id']
                        choice_begin_from_id[np['choice_id']] = i
                    elif node.parsed[0] == ('end', 'choice',):
                        # Mark the end of a choice. Create a ChoiceInfo
                        # object for the begin/end pair.
                        begin = choice_begin_from_id.get(np['choice_id'], None)
                        if begin is None:
                            renpy.error("end choice statement does not "
                                + "have a beginning choice pair.")
                        # Add the begin, end, and id to a ChoiceInfo object.
                        choices.append(ChoiceInfo(begin, i+1, np['choice_id']))
        except Exception as e:
            print("WARNING: Could not parse choices for the",
                "continuous menu. Error:", e)


        # If a choice doesn't have a pair, it ends when the menu does.
        beginning_indices = [b.begin for b in choices]
        no_end = [b for b in get_dict_keys(choice_id_from_index)
            if b not in beginning_indices]

        for i in no_end:
            choices.append(ChoiceInfo(i, -1, choice_id_from_index[i]))

        ## STEP TWO
        ## Convert all dialogue nodes into a time, which is how long it will
        ## take to post that dialogue.
        node_times = [ ]
        for node in p['block'].block:
            node_times.append(convert_node_to_time(node))

        # Now figure out how long each choice stays on-screen for.
        # Add this information to the ChoiceInfo object.
        for c in choices:
            dialogue_time = 0
            # Look through the nodes from when the choices is shown to
            # when it ends.
            final = p['block'].block[c.end]
            if c.end == -1:
                c.end = len(node_times)-1
                c.end_with_menu = True
                final = after_menu_node
            for t in node_times[c.begin:c.end+1]:
                dialogue_time += t

            c.wait_time = dialogue_time
            c.final_node = final
            ## Add the choice's parsed dictionary
            c.choice_dict = p['block'].block[c.begin].parsed[1]
            c.after_c_menu_end = next_dialogue


        ## STEP THREE
        ## Filter out choices whose conditions are not True.
        new_items = [ ]
        location = renpy.game.context().current

        for c in choices:

            condition = renpy.python.py_eval(c.choice_dict['condition'])

            if (not renpy.config.menu_include_disabled) and (not condition):
                continue

            # Get the choice arguments
            if c.choice_dict['arg_info']:
                args, kwargs = c.choice_dict['arg_info'].evaluate()
            else:
                args = tuple()
                kwargs = dict()
            label = c.choice_dict['label']

            new_items.append((label, renpy.ui.ChoiceReturn(label, c.begin,
                location, sensitive=condition, args=args, kwargs=kwargs), c))

        if len(new_items) == 0:
            # There are no choices to show the player; should just
            # execute the dialogue nodes if show_empty_menus is True.
            store.block_interrupts = False
            if store.show_empty_menus:
                p['block'].block[0].execute()
            return None

        ## STEP 4
        ## Calculate the maximum number of choices that are on-screen at
        ## any given time. Should have a list of tuples that have begin/end
        ## node information.
        max_choices = 1
        simple_choices = [ c for l, r, c in new_items ]
        for i, c in enumerate(simple_choices):
            # Don't bother checking for this if the individual choice
            # screens won't be shown.
            if not store.persistent.use_timed_menus or store._in_replay:
                max_choices = 3
                break

            current_choices = 0
            in_range = [ ]
            if i == len(new_items) - 1:
                break

            if c.end == -1:
                final = len(p['block'].block) - 1
            else:
                final = c.end

            for c2 in simple_choices:
                print_file("Checking if", c2.begin, "in range of", c)
                if c2.begin in range(c.begin, final):
                    # Only actually add to this if it's also in the range of
                    # other in-range choices
                    if (c.begin == c2.begin and c.end == c2.end):
                        current_choices += 1
                    elif len(in_range) == 0:
                        in_range.append((c2.begin, c2.end))
                        current_choices += 1
                    else:
                        for b, e in in_range:
                            if c2.begin in range(b, e+1):
                                print_file(c2.begin, "is also in range of", b, ",", e)
                                in_range.append((c2.begin, c2.end))
                                current_choices += 1
                                break

                    print_file("It is. Current_choices is", current_choices)

                if current_choices >= 3:
                    break

            if current_choices >= 3:
                max_choices = 3
                break
            max_choices = max(max_choices, current_choices)

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
            me.action = Function(execute_continuous_menu_action, item=me)
            choice_id_dict[me.choice_id] = me
            item_actions.append(me)

        # Fill the continuous menu dictionary with the appropriate values
        store.c_menu_dict = dict(items=item_actions,
                                end_label=c_menu_post_label(p),
                                narration=p['block'].block,
                                choice_id_dict=choice_id_dict,
                                max_choices=max_choices,
                                showing_choices=dict(),
                                node_times=node_times,
                                available_choices=[],
                                autoanswer=None,
                                menu_args=margs,
                                menu_kwargs=mkwargs)
                                #after_node=after_node)

        store.block_interrupts = False
        # renpy.jump('execute_continuous_menu')
        p['block'].block[0].execute()
        return

    def label_continuous_menu(p):
        return p['label']

    def c_menu_post_label(p):
        if p['label']:
            return "end_for_internal_use_" + p['label']
        name = [c for c in p['loc'][0][0:-4] if c.isalpha()]
        lbl = ''.join(name)
        return 'end_for_internal_use_' + lbl + '_' + str(p['loc'][1])

    def post_execute_c_menu(p):
        print_file("Executing post_execute_c_menu")
        # This executes when the menu is over.
        # If there are choices on-screen, hide everything
        if store.on_screen_choices > 0:
            # Hide the choice screens
            hide_all_c_choices()
            renpy.hide_screen("timed_menu_messages")
            no_anim_list = store.chatlog[-20:-1]
            renpy.show_screen('messenger_screen', no_anim_list=no_anim_list,
                    animate_down=True)
            reset_c_menu_vars()
            # Continue executing code after the menu
            print_file("Hiding all the on-screen choices and returning")
            return

        # If the dictionary is empty, reset variables
        if not store.c_menu_dict:
            reset_c_menu_vars()
            print_file("c_menu_dict was empty")
            return

        if store.persistent.use_timed_menus and not store._in_replay:
            # The menu is over
            store.c_menu_dict = { }
            reset_c_menu_vars()
            return

        print_file("c_menu_dict contains:")
        for key, val in store.c_menu_dict.items():
            if key == 'narration':
                continue
            print_file("   ", key, ":", val)
        # Otherwise, this was likely at the end of a non-timed menu
        # either in replay or because timed menus are turned off.
        # Need to show choices that end at the same time as the menu.
        store.c_menu_dict['available_choices'] = [ ]
        for i in store.c_menu_dict.get('items', []):
            if i.info.end_with_menu:
                if (not store.persistent.use_timed_menus) or store._in_replay:
                    # Add this choice to available choices
                    store.c_menu_dict['available_choices'].append(i)

        # If there are no available choices, the menu is over.
        if len(store.c_menu_dict.get('available_choices', [ ])) < 1:
            # The player has already chosen any answers that would end
            # at the same time as the menu; nothing to show, so return.
            reset_c_menu_vars()
            # Continue executing code after the menu
            print_file("There were no available choices so the menu is over")
            return

        # Show any remaining choices to the user, along with an option
        # to remain silent.
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
        me.next_node = store.c_menu_dict['narration'][-1].next.next
        me.jump_to_label = None #post_continuous_menu(p)
        me.action = Function(execute_continuous_menu_action, item=me,
                            say_nothing=True)
        store.c_menu_dict['autoanswer'] = me
        # The menu dictionary should be erased after this set of choices
        # is shown so the game can continue with the rest of the chatroom.
        store.c_menu_dict['erase_menu'] = True
        store.block_interrupts = False
        print_file("Added a say nothing to the final menu option")
        renpy.jump('play_continuous_menu_no_timer')
        return

    renpy.register_statement('continuous menu',
                            parse=parse_continuous_menu,
                            lint=lint_continuous_menu,
                            execute=execute_continuous_menu,
                            label=label_continuous_menu,
                            force_begin_rollback=True,
                            post_label=c_menu_post_label,
                            post_execute=post_execute_c_menu,
                            block=True
                            )

    ## CHOICE CDS
    ## A CDS used in tandem with the continuous menu CDS to create
    ## continuous menus.
    def parse_choice_stmt(l):
        # First, a choice has an ID so it can have a
        # corresponding `end choice` CDS.
        choice_id = l.simple_expression()
        if choice_id is None:
            renpy.error("Choice statement requires a unique identifier.")

        # Get the caption
        label = l.string()
        # Check for arguments
        args = renpy.parser.parse_arguments(l)
        # Check for an `if` conditional
        condition = 'True'
        if l.keyword('if'):
            condition = l.require(l.python_expression)

        # Require a colon and a newline
        l.require(':')
        l.expect_eol()
        l.expect_block('continuous menu choice')

        # Get the choice block
        block = l.subblock_lexer().renpy_block(empty=True)

        loc = l.get_location()

        return dict(choice_id=choice_id,
                    label=label,
                    condition=condition,
                    arg_info=args,
                    loc=loc,
                    block=block)

    def lint_choice_stmt(p):
        return

    def execute_choice_stmt(p, recalculate_time=False, begin=-1):

        # If there is no continuous menu, do nothing. The menu is over.
        if not store.c_menu_dict:
            return

        # Only show this choice if the condition is True.
        condition = renpy.python.py_eval(p['condition'])
        if (not renpy.config.menu_include_disabled) and (not condition):
            return

        store.block_interrupts = True

        # Retrieve the MenuEntry item associated with this choice.
        item = store.c_menu_dict['choice_id_dict'][p['choice_id']]

        # If timed menus are turned off, choices aren't shown until one or
        # more are about to expire. Add this choice to the list of choices
        # that are currently available.
        if not store.persistent.use_timed_menus or store._in_replay:
            store.c_menu_dict['available_choices'].append(item)
            store.block_interrupts = False
            return

        # Indicate if this choice should animate in from the bottom of
        # the screen.
        first_choice = False

        # Might need to recalculate how long this choice is on-screen for,
        # if it is displayed again after a different choice was made.
        if recalculate_time:
            # Get the list of times for narration
            node_times = store.c_menu_dict['node_times']
            new_choice_end = item.info.end + 1
            wait = 0
            for node in node_times[begin:new_choice_end]:
                wait += node

            # If wait is 0, this choice shouldn't be on-screen. This may occur
            # if the only nodes after the end choice are python statements or
            # other non-dialogue nodes.
            if wait <= 0:
                store.block_interrupts = False
                return

            # Construct a new MenuEntry for this node with the new wait info.
            new_info = item.info
            new_info.wait_time = wait
            new_info.begin = begin
            me = renpy.exports.MenuEntry((item.caption, item.value, item.chosen))

            me.value = item.value
            me.caption = item.caption
            me.chosen = item.chosen
            me.args = item.args
            me.kwargs = item.kwargs
            me.info = new_info
            me.wait = wait
            me.choice_id = item.choice_id
            me.action = Function(execute_continuous_menu_action, item=me)
            ## Replace the choice in the id dictionary with this new version.
            store.c_menu_dict['choice_id_dict'][me.choice_id] = me
            ## Remove the original item from the menu items and add the
            ## new version.
            store.c_menu_dict['items'].remove(item)
            item = me
            store.c_menu_dict['items'].append(item)

        # Time to show this choice. If it's the first choice, show the messenger
        # screen animating up to reveal the choices.
        if store.on_screen_choices <= 0:
            first_choice = True
            renpy.hide_screen("messenger_screen")
            no_anim_list = store.chatlog[-20:-1]
            renpy.show_screen('timed_menu_messages', no_anim_list=no_anim_list)

        # Test if this item is being shown at the "same" time as another choice,
        # which is the first choice, meaning it should receive the same
        # entrance animation.
        if store.last_shown_choice_index is None:
            first_choice = True
            store.last_shown_choice_index = (item.info.begin, True)
        elif ((store.last_shown_choice_index[0] + 1 == item.info.begin
                    or store.last_shown_choice_index[0] == item.info.begin)
                and store.last_shown_choice_index[1]):
            first_choice = True
            store.last_shown_choice_index = (item.info.begin, True)
        else:
            store.last_shown_choice_index = (item.info.begin, first_choice)

        # Allocate a choice box to display the choice in
        renpy.show_screen(allocate_choice_box(p['choice_id']), i=item,
                        first_choice=first_choice)
        ## The number of choices that are on-screen increases.
        store.on_screen_choices += 1
        store.block_interrupts = False
        return

    renpy.register_statement('choice',
                            parse=parse_choice_stmt,
                            lint=lint_choice_stmt,
                            execute=execute_choice_stmt,
                            block=True)

    ## END CHOICE CDS
    ## A CDS used alongside the choice CDS inside the continuous menu CDS to
    ## create a continuous menu.
    def parse_end_choice(l):
        # End choice only gets an identifier; no block
        choice_id = l.simple_expression()
        if choice_id is None:
            renpy.error("Choice end requires an identifier")
        # Get the location for a unique label ID
        loc = l.get_location()
        return dict(choice_id=choice_id, loc=loc)

    def lint_end_choice(p):
        return

    def execute_end_choice(p):

        if not store.c_menu_dict:
            return

        store.block_interrupts = True

        # If timed menus are off, create a choice to remain silent.
        if store._in_replay or (not store.persistent.use_timed_menus
                and not store.c_menu_dict.get('item', None)):

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
            me.jump_to_label = None #end_choice_label(p)
            print_file("The node after end choice", p['choice_id'], "is",
                renpy.game.context().next_node.next)
            me.next_node = renpy.game.context().next_node
            me.action = Function(execute_continuous_menu_action, item=me,
                                say_nothing=True)
            store.c_menu_dict['autoanswer'] = me
            store.block_interrupts = False
            renpy.jump('play_continuous_menu_no_timer')

        # Otherwise, this choice should no longer be shown. Find the screen
        # it's on and hide it.
        which_screen = store.c_menu_dict['showing_choices'].get(
            p['choice_id'], None)

        if which_screen is None:
            store.block_interrupts = False
            return

        store.on_screen_choices -= 1
        if which_screen in store.recently_hidden_choice_screens:
            # Add this screen to the recently_hidden_choice_screens list so
            # the program does not immediately choose it to display a new
            # choice, causing abrupt animations.
            store.recently_hidden_choice_screens.remove(which_screen)

        store.recently_hidden_choice_screens.append(which_screen)

        ## If there are no choices left on-screen, slide the messages back
        ## down into place.
        if (store.on_screen_choices <= 0
                and renpy.get_screen('timed_menu_messages')):
            renpy.hide_screen("timed_menu_messages")
            no_anim_list = store.chatlog[-20:]
            store.c_menu_dict['showing_choices'] = dict()
            renpy.show_screen('messenger_screen', no_anim_list=no_anim_list)

        store.block_interrupts = False

        return

    def end_choice_label(p):
        return 'end_for_internal_use_' + p['choice_id'] + '_' + str(p['loc'][1])

    def post_execute_end_choice(p):

        if not store.c_menu_dict:
            return

        # Grab the ending index of this choice
        choice_id_dict = store.c_menu_dict['choice_id_dict']
        item = choice_id_dict[p['choice_id']]

        if item is None:
            return

        store.block_interrupts = True

        end = item.info.end
        # Add one so it starts after the PostUserStatement
        end += 1

        # Remove this item from the menu items list
        if item in store.c_menu_dict['items']:
            store.c_menu_dict['items'].remove(item)
        # This choice is no longer available because it has already been
        # chosen or has expired.
        if item in store.c_menu_dict['available_choices']:
            store.c_menu_dict['available_choices'].remove(item)
        # This choice is no longer showing.
        store.c_menu_dict['showing_choices'][p['choice_id']] = None

        # Remove this choice from the dictionary as it's already been chosen.
        choice_id_dict[p['choice_id']] = None

        # If this isn't the end of the menu, re-show any remaining
        # choices. Reset the number that are on-screen.
        if (store.c_menu_dict.get('item', None)
                or not store.persistent.use_timed_menus
                or store._in_replay):
            store.on_screen_choices = 0
            # Reset the showing choices dictionary
            store.c_menu_dict['showing_choices'] = dict()

            # Look through all the remaining choices to find ones that began
            # *before* end and end *after* end
            for i in store.c_menu_dict['items']:
                store.c_menu_dict['available_choices'] = [ ]

                if i.info.begin < end and i.info.end > end:
                    if not store.persistent.use_timed_menus or store._in_replay:
                        ## Add this choice to the available choices
                        store.c_menu_dict['available_choices'].append(i)
                    ## Show this choice when the menu resumes
                    else:
                        execute_choice_stmt(i.info.choice_dict,
                            recalculate_time=True, begin=end)

        # Clear the chosen item from the menu dictionary.
        store.c_menu_dict['item'] = None
        store.block_interrupts = False

        return

    renpy.register_statement('end choice',
                            parse=parse_end_choice,
                            lint=lint_end_choice,
                            execute=execute_end_choice,
                            post_label=end_choice_label,
                            post_execute=post_execute_end_choice,
                            )