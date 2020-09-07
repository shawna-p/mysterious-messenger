init python:

    def execute_timed_menu_action(item, items):
        print_file("The player chose", item.caption)
        #end_label = store.timed_menu_dict['end_label']
        #store.timed_menu_dict = {}
        renpy.hide_screen('timed_choice')
        renpy.hide_screen('answer_countdown')
        #renpy.jump(end_label)
        #return

        # Reset the timed_menu_dict at the end
        rv = item.caption
        set = store.timed_menu_dict['menu_set']
        ## Note for adding chosen item to the set:
        ## rv is just the return value of the menu it seems
        if set is not None and rv is not None:
            if set is not None and rv is not None:
                try:
                    set.append(rv)
                except AttributeError:
                    set.add(rv)

        ## Do my own `chosen` marking?
        # return (self.location, self.label) in self.chosen
        # Mark this as chosen
        item.action.chosen[(item.action.location, item.action.label)] = True

        store.timed_menu_dict = {}
        print_file("What are all the values of things?")
        print_file("   action:", item.action)
        print_file("   chosen:", item.chosen)
        print_file("   caption:", item.caption)
        print_file("   args:", item.args)
        print_file("   kwargs:", item.kwargs)
        print_file("   action.value:", item.action.value)
        print_file("   subparse:", item.subparse)
        renpy.ast.next_node(item.subparse.block[0])
        #renpy.ast.next_node(item.action)




label execute_timed_menu():
    if not timed_menu_dict:
        $ print_file("Something went wrong with timed menus")
        return

    ## All right, now we need to sort out some stuff. Separate out the vars
    python:
        wait_time = timed_menu_dict['wait_time']
        end_label = timed_menu_dict['end_label']
        narration = timed_menu_dict['narration']
        items = timed_menu_dict['items']
        screen_kwargs = timed_menu_dict['menu_kwargs']
        if screen_kwargs.get('paraphrase', None):
            para = True
        else:
            para = False

        # Shuffle the menu options
        if shuffle and shuffle != "last":
            renpy.random.shuffle(items)
        elif shuffle == "last":
            last = items.pop()
            renpy.random.shuffle(items)
            items.append(last)
        shuffle = True
        end_menu_buffer = 2.0 * pv

    show screen timed_choice(items, para)
    show screen answer_countdown(end_label, wait_time+(end_menu_buffer),
        custom_action=If(persistent.autoanswer_timed_menus,

                # Need to somehow keep the answers on-screen and pause
                [ Hide('answer_countdown'),
                Hide('timed_choice'),
                Show('pause_button'),
                SetVariable('choosing', True),
                SetVariable('timed_choose', True) ],

                [ Hide('answer_countdown'),
                Hide('timed_choice'),
                Show('pause_button') ]))


    # Now show the narration behind the choices
    while narration:
        $ msg = narration.pop(0)
        # Hopefully this makes it use the __call__ method?
        $ who = msg['who']
        $ who(what=msg['what'], pauseVal=msg['pauseVal'], img=msg['img'],
            bounce=msg['bounce'], specBubble=msg['specBubble'])

    # If we got here, then the menu is over
    # Give it a small buffer
    $ messenger_pause(end_menu_buffer)
    $ timed_menu_dict = {}
    hide screen timed_choice
    pause 0.5
    jump expression end_label




default timed_menu_dict = { }

screen timed_choice(items, paraphrase=None):
    zorder 150

    if persistent.custom_footers and not renpy.is_skipping():
        default the_anim = choice_anim
    else:
        default the_anim = null_anim

    frame:
        at shrink_away()
        #background "#2828280a"
        yalign 1.0
        top_padding 20
        xsize 750
        ysize 220
        yoffset -113-20
        # For now, just show the choices on top of stuff
        hbox:
            style_prefix 'phone_vn_choice'
            xalign 0.5
            spacing 20
            for num, i in enumerate(items):
                $ fnum = float(num*0.2)
                textbutton i.caption at the_anim(fnum):
                    xmaximum 300
                    text_xmaximum 250
                    if persistent.dialogue_outlines:
                        text_outlines [ (absolute(2), "#000",
                            absolute(0), absolute(0)) ]
                    if (persistent.past_choices and not observing
                            and i.chosen):
                        foreground 'seen_choice_check_circle'
                        background 'call_choice_check'
                        hover_background 'call_choice_check_hover'
                    action Function(execute_timed_menu_action, item=i, items=items)
                    #[i.action]
                        # SetVariable('dialogue_picked', i.caption),
                        # Function(set_paraphrase, screen_pref=paraphrase,
                        #     item_pref=(i.kwargs.get('paraphrase',
                        #     None)),
                        #     save_choices=True)]
        #add "answerbutton"
    frame:
        at wait_fade()
        align (0.5, 1.0)
        background "#282828"
        xysize (750, 113)
        text "Choose a reply" color "#fff" text_align 0.5 align (0.5, 0.5)

transform shrink_away():
    yzoom 0.0
    ease 0.5 yzoom 1.0
    on hide:
        yzoom 1.0
        ease 0.5 yzoom 0.0


transform wait_fade():
    alpha 0.0
    linear 0.5 alpha 1.0
    alpha 1.0
    on hide:
        linear 0.5 alpha 0.0