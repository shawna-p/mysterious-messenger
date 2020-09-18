init python:

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
        result = allocate_screen(['c_choice_2', 'c_choice_1', 'c_choice_3'])
        if store.c_menu_dict.get('showing_choices', None):
            store.c_menu_dict['showing_choices'][choice_id] = result
        else:
            store.c_menu_dict['showing_choices'] = {}
            store.c_menu_dict['showing_choices'][choice_id] = result
        return result

    def choice_move_left(trans, st, at):
        """The transform function for the left choice."""

        ## Center this choice if it's the only choice on-screen
        if store.on_screen_choices == 1 and trans.xoffset != 0:
            if trans.xoffset < 0:
                trans.xoffset += store.choice_slide_speed
            else:
                trans.xoffset -= store.choice_slide_speed
            return 0

        ## Move this choice to the mid-left position if there are two choices
        if store.on_screen_choices == 2 and trans.xoffset != -132:
            if trans.xoffset < -132:
                trans.xoffset += store.choice_slide_speed
            else:
                trans.xoffset -= store.choice_slide_speed
            return 0

        ## Move this choice to the fully left position if there are 3 choices
        if store.on_screen_choices == 3 and trans.xoffset != -255:
            if trans.xoffset < -255:
                trans.xoffset += store.choice_slide_speed
            else:
                trans.xoffset -= store.choice_slide_speed
            return 0
        return 0.1

    def choice_move_center(trans, st, at):
        """The transform function for the center choice."""

        ## Center this choice if it's the only choice on-screen
        if store.on_screen_choices in [1, 3] and trans.xoffset != 0:
            if trans.xoffset < 0:
                trans.xoffset += store.choice_slide_speed
            else:
                trans.xoffset -= store.choice_slide_speed
            return 0

        ## This choice moves left or right depending on which other screen
        ## is showing
        if renpy.get_screen('c_choice_1') and trans.xoffset != 132:
            if trans.xoffset < 132:
                trans.xoffset += store.choice_slide_speed
            else:
                trans.xoffset -= store.choice_slide_speed
            return 0

        elif renpy.get_screen('c_choice_3') and trans.xoffset != -132:
            if trans.xoffset < -132:
                trans.xoffset += store.choice_slide_speed
            else:
                trans.xoffset -= store.choice_slide_speed
            return 0
        return 0.1

    def choice_move_right(trans, st, at):
        """The transform function for the right choice."""

        ## Center this choice if it's the only choice on-screen
        if store.on_screen_choices == 1 and trans.xoffset != 0:
            if trans.xoffset < 0:
                trans.xoffset += store.choice_slide_speed
            else:
                trans.xoffset -= store.choice_slide_speed
            return 0

        ## Move this choice to the mid-right position if there are two choices
        if store.on_screen_choices == 2 and trans.xoffset != 132:
            if trans.xoffset < 132:
                trans.xoffset += store.choice_slide_speed
            else:
                trans.xoffset -= store.choice_slide_speed
            return 0

        ## Move this choice to the fully left position if there are 3 choices
        if store.on_screen_choices == 3 and trans.xoffset != 255:
            if trans.xoffset < 255:
                trans.xoffset += store.choice_slide_speed
            else:
                trans.xoffset -= store.choice_slide_speed
            return 0
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
    if not persistent.autoanswer_timed_menus:
        # Hide all the choice screens
        hide screen timed_choice
        hide screen answer_countdown
        hide screen timed_menu_messages
        # Show the original messenger screen; it should animate back down into
        # position
        show screen messenger_screen(no_anim_list=no_anim_list, animate_down=True)

    $ item = timed_menu_dict['item']
    $ timed_menu_dict = {}
    # This executes the statements bundled after the choice
    $ renpy.ast.next_node(item.subparse.block[0])
    return

## Dictionary which holds information needed to display continuous menus
default c_menu_dict = { }
## Number of choices currently on-screen
default on_screen_choices = 0
## Size of the choices that are on-screen (approx 750 // on_screen_choices)
default choice_box_size = 740
## Speed at which the animation for the choice boxes plays out
define choice_slide_speed = 3

## The screen which displays a single choice for a continuous menu.
screen c_choice_1(i, hide_screen='c_choice_1', first_choice=False):
    zorder 150

    # Could check if the c_menu_dict['items'] only has two items
    # for two-item styling
    fixed:
        if hide_screen == 'c_choice_1':
            at continue_appear_disappear(i.wait, persistent.timed_menu_pv,
                                        choice_move_left)
        elif hide_screen == 'c_choice_2':
            at continue_appear_disappear(i.wait, persistent.timed_menu_pv,
                                        choice_move_center)
        elif hide_screen == 'c_choice_3':
            at continue_appear_disappear(i.wait, persistent.timed_menu_pv,
                                        choice_move_right)

        if persistent.custom_footers:
            style_prefix 'new_three'
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
        # parallel:
        #     function fn

    on hide:
        # pause (end_delay*mod) - max((end_delay*mod) - (3.0*mod), 0.1) - mod
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
        # parallel:
        #     function fn

    on hide:
        # pause (end_delay*mod) - max((end_delay*mod) - (3.0*mod), 0.1) - mod
        parallel:
            ease 0.625*mod alpha 0.0
        parallel:
            ease 0.625*mod xzoom 0.01

