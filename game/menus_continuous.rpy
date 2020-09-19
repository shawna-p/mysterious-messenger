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
            self.choice_dict = {}

        def construct_action(self, nodes):
            """Construct the block this choice should execute."""

            block = self.choice_dict['block'].block

            # If final is a node, then this choice has an explicit `end choice`
            # CDS. The choice will execute, then jump to the end of the CDS.
            if isinstance(self.final_node, renpy.ast.Node):
                block.extend(nodes[self.end:])
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



    def execute_continuous_menu_action(item, jump_to_end=False):
        """
        Mark the selected choice as chosen and proceed to the choice
        block to execute its action.
        """
        print_file("Made a choice:", item.caption)
        store.c_menu_dict['item'] = item

        ## Mark this as chosen
        item.value.chosen[(item.value.location, item.value.label)] = True

        if jump_to_end:
            end_label = store.c_menu_dict['end_label']
            store.c_menu_dict = {}
            renpy.jump(end_label)
        else:
            renpy.jump('finish_c_menu')


    def allocate_choice_box(choice_id):
        """Allocate an available choice screen."""

        possible_screens = ['c_choice_2', 'c_choice_1', 'c_choice_3']

        ## Make sure the least-recently allocated screens end up first in
        ## the list
        allocate_list = [ x for x in possible_screens
                        if x not in store.recently_hidden_choice_screens ]
        allocate_list.extend(store.recently_hidden_choice_screens)
        result = allocate_screen(allocate_list)

        if store.c_menu_dict.get('showing_choices', None):
            store.c_menu_dict['showing_choices'][choice_id] = result
        else:
            store.c_menu_dict['showing_choices'] = {}
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
        if renpy.get_screen('c_choice_1'):
            return adjust_xoffset(trans, choice_offsets[3])

        elif renpy.get_screen('c_choice_3'):
            return adjust_xoffset(trans, choice_offsets[1])
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
    while narration:
        $ node = narration.pop(0)
        $ node.execute()

    return

label finish_c_menu:
    ## Get rid of the backup; check if paraphrased dialogue should be sent
    $ chatbackup = None
    $ no_anim_list = chatlog[-20:]
    if (not dialogue_paraphrase and dialogue_picked != ""):
        # The choice was not paraphrased and should be posted
        $ say_choice_caption(dialogue_picked, dialogue_paraphrase, dialogue_pv)

    $ chatbackup = None

    ## Check if this choice has an `end choice` node and continue from there
    ## if applicable


    ## Otherwise, this is the end of the menu
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
    $ c_menu_dict = {}
    # This executes the statements bundled after the choice
    $ renpy.ast.next_node(item.block[0])
    return

## Dictionary which holds information needed to display continuous menus
default c_menu_dict = { }
## Number of choices currently on-screen
default on_screen_choices = 0
## Size of the choices that are on-screen (approx 750 // on_screen_choices)
default choice_box_size = 740
## Speed at which the animation for the choice boxes plays out
define choice_slide_speed = 4
## Offsets for the on-screen choices
define choice_offsets_2 = (-185, -185, 0, 185, 185)
define choice_offsets_3 = (-255, -132, 0, 132, 255)
## Holds the most recently hidden choice screens to avoid pop-in
default recently_hidden_choice_screens = []

## The screen which displays a single choice for a continuous menu.
screen c_choice_1(i, hide_screen='c_choice_1', first_choice=False):
    zorder 150

    python:
        if hide_screen == 'c_choice_1':
            fn = choice_move_left
        elif hide_screen == 'c_choice_2':
            fn = choice_move_center
        else:
            fn = choice_move_right

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
                    Function(set_paraphrase, screen_pref=None,
                        item_pref=(i.kwargs.get('paraphrased', None))),
                        i.action]

        add 'header_hg':
            align (0.5, 0.98)
            at choice_disappear_hourglass(i.wait, persistent.timed_menu_pv)

        timer (i.wait*persistent.timed_menu_pv):
            action Hide(hide_screen)

screen c_choice_2(i, first_choice=False):
    zorder 150
    use c_choice_1(i, hide_screen='c_choice_2', first_choice=first_choice)

screen c_choice_3(i, first_choice=False):
    zorder 150
    use c_choice_1(i, hide_screen='c_choice_3', first_choice=first_choice)

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

