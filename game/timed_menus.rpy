init python:

    def timed_menu_null(st, at):
        """
        A DynamicDisplayable function which animates the timed menus
        in and out.
        """

        anim_len = 4
        anim_speed = 1.0#1.0 / 30 # 60 FPS
        max_height = 220

        d = store.timed_menu_anim_dict

        if not d:
            return Null(height=0), None

        start_time = d.get('anim_start', None)
        state = d.get('anim_state', None)
        #print("\n   INITIAL: start", start_time, "state", state, "anim_speed", anim_speed)

        ## Possible states:
        ## 1) About to be shown. anim_start is None and anim_state is show
        ## 2) Growing. Should be animating larger. anim_start is a number,
        ##      anim_state is grow
        ## 3) Visible. anim_start is None and anim_state is visible
        ## 4) Shrinking. anim_start is a number and anim_state is shrink
        ## 5) Hidden. anim_start is None and anim_state is None

        # if state == 'show':
        #     d['anim_start'] = st
        #     d['anim_state'] = 'grow'
        #     return Null(height=10), 0.1
        # if state == 'grow':
        #     diff = st - start_time
        #     if diff <= 2:
        #         return Null(height=50), 0.1
        #     elif diff <= 3:
        #         return Null(height=100), 0.1
        #     elif diff <= 4:
        #         return Null(height=150), 0.1
        #     elif diff <= 5:
        #         return Null(height=200), 0.1
        #     return Null(height=220), 0.1


        # ## Try this again
        # if state == 'show':
        #     return At(Null(height=max_height), shrink_away), 0.5
        # elif state == 'shrink':
        #     return At(Null(height=max_height), wait_fade), 0.5
        # else:
        #     return Null(height=max_height), 0.1

        if state == 'show':
            print("1. start:", start_time, "state:", state)
            d['anim_start'] = st
            d['anim_state'] = 'grow'
            return Null(height=10), anim_speed

        if start_time is not None and state == 'grow':
            print("2. start:", start_time, "state:", state)

            diff = st - start_time
            if diff >= anim_len:
                d['anim_state'] = 'visible'
            else:
                return Null(height=int(max_height * (diff/anim_len))), anim_speed

        if state == 'visible':
            print("3. start:", start_time, "state:", state)

            d['anim_start'] = None
            return Null(height=max_height), anim_speed

        if state == 'shrink':
            print("4. start:", start_time, "state:", state)

            d['anim_start'] = st
            d['anim_state'] = 'shrinking'
            return Null(height=max_height), anim_speed

        if start_time is not None and state == 'shrinking':
            print("5. start:", start_time, "state:", state)

            diff = st - start_time
            if diff >= anim_len:
                d['anim_state'] = 'hidden'
            else:
                return Null(height=(max_height - int(max_height * (diff/anim_len)))), anim_speed

        if state == 'hidden':
            d['anim_start'] = None
            return Null(height=10), anim_speed

        return Null(height=10), anim_speed




    def execute_timed_menu_action(item):
        """
        Add the selected choice to the menu set if applicable and ensure
        it is marked as chosen, then proceed to the choice block.
        """
        # Hide the animation
        timed_menu_anim_dict['anim_state'] = 'shrink'
        renpy.hide_screen('timed_choice')
        renpy.hide_screen('answer_countdown')

        ## Add the chosen answer to the menu set
        set = store.timed_menu_dict['menu_set']

        if set is not None and item.caption is not None:
            try:
                set.append(item.caption)
            except AttributeError:
                set.add(item.caption)

        ## Mark this as chosen
        item.action.chosen[(item.action.location, item.action.label)] = True

        ## Reset the menu
        store.timed_menu_dict = {}
        ## Set the next node as the block of items resulting from the choice
        renpy.ast.next_node(item.subparse.block[0])
        return

screen timed_m_test():
    add "#000d"
    hbox:
        align (0.5, 0.5)
        textbutton "show":
            action SetDict(timed_menu_anim_dict, 'anim_state', 'show')
        vbox:
            add '#0ff' size (200, 150)
            add 'timed_menu_anim'
            add "#0ff" size (200, 150)
        textbutton "shrink":
            action SetDict(timed_menu_anim_dict, 'anim_state', 'shrink')



## A label which handles displaying the dialogue behind a menu and what happens
## if the player does not make a choice
label execute_timed_menu():
    if not timed_menu_dict:
        $ print_file("ERROR: Something went wrong with timed menus")
        return

    ## First things first: if the player is skipping, the menu is omitted
    if renpy.is_skipping():
        $ end_label = timed_menu_dict['end_label']
        $ timed_menu_dict = {}
        jump expression end_label

    ## Separate out the vars
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

        # The length of time the player has to read the final message
        # before the timer runs out
        end_menu_buffer = 3.0 * pv

        # Show the animation
        timed_menu_anim_dict['anim_state'] = 'show'

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
        $ who = msg['who']
        $ who(what=msg['what'], pauseVal=msg['pauseVal'], img=msg['img'],
            bounce=msg['bounce'], specBubble=msg['specBubble'])

    # If the dialogue is exhausted, the player has missed the time window to
    # reply. There is a small buffer for them to finish reading the last
    # message and then everything is reset.
    $ messenger_pause(end_menu_buffer)
    $ timed_menu_dict = {}
    hide screen timed_choice
    # Hide the animation
    $ timed_menu_anim_dict['anim_state'] = 'shrink'
    pause 0.5
    jump expression end_label

## Dictionary which holds information needed to display timed menus
default timed_menu_dict = { }
## Dictionary which holds information needed to display the animation
## to/from a timed menu
default timed_menu_anim_dict = { }
image timed_menu_anim = DynamicDisplayable(timed_menu_null)

## Screen that borrows from the choice screen, but customized for
## timed menus.
screen timed_choice(items, paraphrase=None):
    zorder 150

    if persistent.custom_footers and not renpy.is_skipping():
        default the_anim = choice_anim
    else:
        default the_anim = null_anim

    frame:
        at shrink_away()
        yalign 1.0
        top_padding 20
        xsize 750
        ysize 220
        yoffset -113-20
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
                    action [SetVariable('dialogue_picked', i.caption),
                        Function(set_paraphrase, screen_pref=paraphrase,
                            item_pref=(i.kwargs.get('paraphrase',
                            None))),
                        Function(execute_timed_menu_action, item=i)]
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