init python:

    def execute_continuous_menu_action(item, jump_to_end=False):
        """
        Mark the selected choice as chosen and proceed to the choice
        block to execute its action.
        """

        return execute_timed_menu_action(item, jump_to_end)

    def allocate_choice_box(choice_id):
        result = allocate_screen(['c_choice_2', 'c_choice_1', 'c_choice_3'])
        if store.c_menu_dict.get('showing_choices', None):
            store.c_menu_dict['showing_choices'][choice_id] = result
        else:
            store.c_menu_dict['showing_choices'] = {}
            store.c_menu_dict['showing_choices'][choice_id] = result
        return result

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

## Dictionary which holds information needed to display continuous menus
default c_menu_dict = { }


## The screen which displays a single choice for a continuous menu.
screen c_choice_1(i, x=-250, hide_screen='c_choice_1'):
    zorder 150

    # Could check if the c_menu_dict['items'] only has two items
    # for two-item styling
    fixed:
        #at continue_appear_disappear(i.wait, persistent.timed_menu_pv)
        at shrink_away()
        if persistent.custom_footers:
            style_prefix 'new_three'
        else:
            style_prefix 'old_three'
        xalign 0.5
        xoffset x
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

screen c_choice_2(i):
    zorder 150
    use c_choice_1(i, x=-0, hide_screen='c_choice_2')

screen c_choice_3(i):
    zorder 150
    use c_choice_1(i, x=250, hide_screen='c_choice_3')

transform continue_appear_disappear(end_delay, mod):
    on show:
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
        easein 0.25*mod alpha 0.6 zoom 1.1
        easeout 0.25*mod alpha 1.0 zoom 1.0
        repeat
    on hide:
        # pause (end_delay*mod) - max((end_delay*mod) - (3.0*mod), 0.1) - mod
        parallel:
            ease 0.625*mod alpha 0.0
        parallel:
            ease 0.625*mod xzoom 0.01
