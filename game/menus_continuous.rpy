init python:

    class ChoiceInfo(renpy.store.object):
        """
        A class which organizes information on a choice for a continuous menu.

        Attributes:
        -----------
        begin : int
            Index of the parent block where the choice begins.
        end : int
            Index of the parent block where the choice ends.
        choice_id : string
            Unique identifier for this particular choice.
        wait_time : float
            The time this choice will remain on-screen for after it is first
            shown.
        final_node : renpy.ast.Node
            The final node to execute for this choice.
        end_with_menu : bool
            True if this choice ends when the menu ends.
        choice_dict : dict
            A dictionary from the parsed choice CDS. Contains information on
            the label and block for this choice, among other things.
        """

        def __init__(self, begin, end, choice_id=None):
            """
            Construct a ChoiceInfo object.

            Parameters:
            -----------
            begin : int
                Index of the parent block where the choice begins.
            end : int
                Index of the parent block where the choice ends.
            choice_id : string
                Unique identifier for this particular choice.
            """

            self.begin = begin
            self.end = end
            self.choice_id = choice_id
            self.wait_time = 0.0
            self.final_node = None
            self.end_with_menu = False
            self.choice_dict = {}

        def construct_action(self, nodes):
            """Construct the block this choice should execute."""

            block = self.choice_dict['block'].block

            if self.end_with_menu:
                block.append(self.final_node)
            else:
                block.extend(nodes[self.end-1:])

            for a, b in zip(block, block[1:]):
                a.chain(b)
            return block

            # Otherwise, the final action is the end of the menu. The choice
            # action is simply to jump to the appropriate block
            return block


        def __str__(self):
            """Print out a readable string representing this object."""

            return ("<ChoiceInfo> object\n   begin: " + str(self.begin)
                + "\n   end: " + str(self.end) + "\n   choice_id: "
                + str(self.choice_id) + "\n   wait_time: " + str(self.wait_time)
                + "\n   final_node: " + str(self.final_node))



    def execute_continuous_menu_action(item, say_nothing=False):
        """
        Mark the selected choice as chosen and proceed to the choice
        block to execute its action.
        """
        print_file("Made a choice:", item.caption)
        store.c_menu_dict['item'] = item

        ## Mark this as chosen
        item.value.chosen[(item.value.location, item.value.label)] = True

        if (not say_nothing
                and store.c_menu_dict.get('narration', None) is not None):
            store.c_menu_dict['items'].remove(item)
            store.c_menu_dict['available_choices'].remove(item)

        if say_nothing:
            store.dialogue_picked = ""
            store.dialogue_paraphrase = store.paraphrase_choices
            store.dialogue_pv = 0
            renpy.jump(item.jump_to_label)
        else:
            # renpy.game.context().current = None
            renpy.jump('finish_c_menu')


    def allocate_choice_box(choice_id):
        """Allocate an available choice screen."""

        possible_screens = ['c_choice_2', 'c_choice_1', 'c_choice_3',
                            'c_choice_4']

        ## Make sure the least-recently allocated screens end up first in
        ## the list
        allocate_list = [ x for x in possible_screens
                        if x not in store.recently_hidden_choice_screens ]
        allocate_list.extend(store.recently_hidden_choice_screens)
        result = allocate_screen(allocate_list)

        store.c_menu_dict['showing_choices'][choice_id] = result

        return result

    def adjust_xoffset(trans, x):
        """Adjust the xoffset of trans to x."""

        if trans.xoffset == x:
            return 0.1

        ## The desired xoffset may not divide nicely into the slide speed;
        ## if we're off by a few pixels, just snap to position.
        if ((trans.xoffset + store.choice_slide_speed) > x
                and trans.xoffset < x):
            trans.xoffset = x
            return 0.1
        elif ((trans.xoffset - store.choice_slide_speed) < x
                and trans.xoffset > x):
            trans.xoffset = x
            return 0.1

        if trans.xoffset < x:
            trans.xoffset += store.choice_slide_speed
        else:
            trans.xoffset -= store.choice_slide_speed
        return 0

    def choice_move_left(trans, st, at):
        """The transform function for the left choice."""

        if c_menu_dict.get('max_choices', 3) < 3:
            choice_offsets = store.choice_offsets_2
        else:
            choice_offsets = store.choice_offsets_3

        ## Center this choice if it's the only choice on-screen
        if store.on_screen_choices == 1:
            return adjust_xoffset(trans, choice_offsets[2])

        ## Move this choice to the mid-left position if there are two choices
        if store.on_screen_choices == 2:
            return adjust_xoffset(trans, choice_offsets[1])

        ## Move this choice to the fully left position if there are 3 choices
        if store.on_screen_choices == 3:
            return adjust_xoffset(trans, choice_offsets[0])
        return 0.1

    def choice_move_center(trans, st, at):
        """The transform function for the center choice."""

        if c_menu_dict.get('max_choices', 3) < 3:
            choice_offsets = store.choice_offsets_2
        else:
            choice_offsets = store.choice_offsets_3

        ## Center this choice if it's the only choice on-screen
        if store.on_screen_choices in [1, 3]:
            return adjust_xoffset(trans, choice_offsets[2])

        ## This choice moves left or right depending on which other screen
        ## is showing
        if renpy.get_screen('c_choice_1') or renpy.get_screen('c_choice_4'):
            return adjust_xoffset(trans, choice_offsets[3])

        elif renpy.get_screen('c_choice_3'):
            return adjust_xoffset(trans, choice_offsets[1])
        return 0.1

    def choice_move_substitute(trans, st, at):
        """The transform function for the choice which can replace any box."""

        if c_menu_dict.get('max_choices', 3) < 3:
            choice_offsets = store.choice_offsets_2
        else:
            choice_offsets = store.choice_offsets_3

        ## Center this choice if it's the only choice on-screen
        if store.on_screen_choices == 1:
            return adjust_xoffset(trans, choice_offsets[2])

        ## This choice moves left or right depending on which other screen
        ## is showing
        if store.on_screen_choices == 2:
            if renpy.get_screen('c_choice_1'):
                return adjust_xoffset(trans, choice_offsets[3])

            if renpy.get_screen('c_choice_3') or renpy.get_screen('c_choice_2'):
                return adjust_xoffset(trans, choice_offsets[1])

        ## Otherwise, there are three on-screen choices.
        ## Need to account for all possible combinations of two screens
        if renpy.get_screen('c_choice_1') and renpy.get_screen('c_choice_2'):
            ## This screen acts like the right choice
            return adjust_xoffset(trans, choice_offsets[4])

        if renpy.get_screen('c_choice_1') and renpy.get_screen('c_choice_3'):
            ## Act like the middle choice
            return adjust_xoffset(trans, choice_offsets[2])

        if renpy.get_screen('c_choice_2') and renpy.get_screen('c_choice_3'):
            ## Act like the left choice
            return adjust_xoffset(trans, choice_offsets[0])

        return 0.1

    def choice_move_right(trans, st, at):
        """The transform function for the right choice."""

        if c_menu_dict.get('max_choices', 3) < 3:
            choice_offsets = store.choice_offsets_2
        else:
            choice_offsets = store.choice_offsets_3

        ## Center this choice if it's the only choice on-screen
        if store.on_screen_choices == 1:
            return adjust_xoffset(trans, choice_offsets[2])

        ## Move this choice to the mid-right position if there are two choices
        if store.on_screen_choices == 2:
            return adjust_xoffset(trans, choice_offsets[3])


        ## Move this choice to the fully left position if there are 3 choices
        if store.on_screen_choices == 3:
            return adjust_xoffset(trans, choice_offsets[4])

        return 0.1

## A label which handles displaying the dialogue for a continuous menu
## as well as the choices that will show up
label execute_continuous_menu():
    if not c_menu_dict:
        $ print_file("ERROR: Something went wrong with continuous menus")
        return

    $ narration = c_menu_dict['narration']
    # while narration:
    $ node = narration.pop(0)
    $ node.execute()

    return

## Plays the continuous menu as if it were a regular menu without a timer.
label play_continuous_menu_no_timer():
    call answer
    python:
        print_file("in play_continuous_menu_no_timer")
        items = c_menu_dict['available_choices'][:]
        items.append(c_menu_dict['autoanswer'])
        screen_kwargs = c_menu_dict['menu_kwargs']
        para = screen_kwargs.get('paraphrased', None)
        if c_menu_dict.get('erase_menu', False):
            print_file("Erased menu")
            c_menu_dict = {}
    call screen choice(items=items, paraphrased=para)
    return


label finish_c_menu:
    ## Get rid of the backup; check if paraphrased dialogue should be sent
    $ chatbackup = None
    $ no_anim_list = chatlog[-20:]
    if (not dialogue_paraphrase and dialogue_picked != ""):
        # The choice was not paraphrased and should be posted
        $ say_choice_caption(dialogue_picked, dialogue_paraphrase, dialogue_pv)

    $ chatbackup = None

    if persistent.use_timed_menus:
        # Hide all the choice screens
        hide screen c_choice_1
        hide screen c_choice_2
        hide screen c_choice_3
        hide screen timed_menu_messages
        # Show the original messenger screen; it should animate back down into
        # position
        show screen messenger_screen(no_anim_list=no_anim_list, animate_down=True)

    $ item = c_menu_dict['item']
    ## If this isn't at the end of the menu, re-show any remaining
    ## choices. Reset the number that are on-screen.
    $ on_screen_choices = 0
    ## Reset the showing choices dictionary
    $ c_menu_dict['showing_choices'] = dict()
    # $ c_menu_dict = {}
    # This executes the statements bundled after the choice
    $ renpy.ast.next_node(item.block[0])
    return

## Dictionary which holds information needed to display continuous menus
default c_menu_dict = { }
## Number of choices currently on-screen
default on_screen_choices = 0
## Speed at which the animation for the choice boxes plays out
define choice_slide_speed = 4
## Offsets for the on-screen choices
define choice_offsets_2 = (-185, -185, 0, 185, 185)
define choice_offsets_3 = (-255, -132, 0, 132, 255)
## Holds the most recently hidden choice screens to avoid pop-in
default recently_hidden_choice_screens = []
default last_shown_choice_index = None

## The screen which displays a single choice for a continuous menu.
screen c_choice_1(i, hide_screen='c_choice_1', first_choice=False,
                    fn=choice_move_left):
    zorder 150

    # Could check if the c_menu_dict['items'] only has two items
    # for two-item styling
    fixed:
        if first_choice:
            at continue_appear_disappear_first(i.wait,
                persistent.timed_menu_pv, fn)
        else:
            at continue_appear_disappear(i.wait, persistent.timed_menu_pv, fn)

        if persistent.custom_footers:
            if c_menu_dict.get('max_choices', 3) < 3:
                style_prefix 'new_two'
            else:
                style_prefix 'new_three'
        else:
            if c_menu_dict.get('max_choices', 3) < 3:
                style_prefix 'old_two'
            else:
                style_prefix 'old_three'
        xalign 0.5
        yalign 1.0
        yoffset -113-20
        fit_first True
        textbutton i.caption:
            ## Check if the caption is long; reduce font size
            if len(i.caption) > 60:
                text_size 23
            elif len(i.caption) > 42:
                text_size 25

            ## Add dialogue outlines
            if (persistent.dialogue_outlines
                    and persistent.custom_footers):
                text_outlines [ (2, "#000",
                    absolute(0), absolute(0)) ]
            elif (persistent.dialogue_outlines
                    and not persistent.custom_footers):
                text_outlines [ (2, "#fff",
                    absolute(0), absolute(0)) ]

            ## Add 'seen' choice styling
            if (persistent.past_choices and not observing
                    and i.chosen):
                if persistent.custom_footers:
                    foreground 'seen_choice_check_circle'
                    background 'call_choice_check'
                    hover_background 'call_choice_check_hover'
                else:
                    foreground 'seen_choice_check'

            action [SetVariable('dialogue_picked', i.caption),
                    Function(set_paraphrase,
                        screen_pref=store.c_menu_dict['menu_kwargs'].get(
                            'paraphrased', None),
                        item_pref=(i.kwargs.get('paraphrased', None))),
                        i.action]

        add 'header_hg':
            align (0.5, 0.98)
            at choice_disappear_hourglass(i.wait, persistent.timed_menu_pv)

        timer (i.wait*persistent.timed_menu_pv):
            action Hide(hide_screen)

screen c_choice_2(i, first_choice=False):
    zorder 150
    use c_choice_1(i, hide_screen='c_choice_2', first_choice=first_choice,
        fn=choice_move_center)

screen c_choice_3(i, first_choice=False):
    zorder 150
    use c_choice_1(i, hide_screen='c_choice_3', first_choice=first_choice,
        fn=choice_move_right)

screen c_choice_4(i, first_choice=False):
    zorder 150
    use c_choice_1(i, hide_screen='c_choice_4', first_choice=first_choice,
        fn=choice_move_substitute)

transform continue_appear_disappear(end_delay, mod, fn):
    on show:
        parallel:
            xzoom 0.01 alpha 0.0
            parallel:
                pause 0.125*mod
                ease 0.5*mod alpha 1.0
            parallel:
                ease 0.625*mod xzoom 1.0

            xzoom 1.0 alpha 1.0 zoom 1.0
            pause max((end_delay*mod) - (2.0*mod) - mod, 0.1)
            # Indicate it's about to expire
            block:
                easein 0.25*mod alpha 0.7 zoom 1.1
                easeout 0.25*mod alpha 1.0 zoom 1.0
                repeat 2
        parallel:
            function fn

    on hide:
        parallel:
            ease 0.625*mod alpha 0.0
        parallel:
            ease 0.625*mod xzoom 0.01

transform continue_appear_disappear_first(end_delay, mod, fn):
    on show:
        parallel:
            yzoom 0.0 alpha 0.0
            parallel:
                pause 0.125*mod
                ease 0.5*mod alpha 1.0
            parallel:
                ease 0.625*mod yzoom 1.0

            xzoom 1.0 alpha 1.0 zoom 1.0
            pause max((end_delay*mod) - (2.0*mod) - mod, 0.1)
            # Indicate it's about to expire
            block:
                easein 0.25*mod alpha 0.7 zoom 1.1
                easeout 0.25*mod alpha 1.0 zoom 1.0
                repeat 2
        parallel:
            function fn

    on hide:
        parallel:
            ease 0.625*mod alpha 0.0
        parallel:
            ease 0.625*mod xzoom 0.01

