init python:

    def execute_timed_menu_action(item):
        """
        Add the selected choice to the menu set if applicable and ensure
        it is marked as chosen, then proceed to the choice block.
        """

        print_file("Made a choice:", item.caption)
        store.timed_menu_dict['item'] = item

        ## Add the chosen answer to the menu set
        set = store.timed_menu_dict['menu_set']

        if set is not None and item.caption is not None:
            try:
                set.append(item.caption)
            except AttributeError:
                set.add(item.caption)

        ## Mark this as chosen
        item.action.chosen[(item.action.location, item.action.label)] = True

        renpy.jump('finish_timed_menu')

        # Hide the animation
        renpy.hide_screen('timed_choice')
        renpy.hide_screen('answer_countdown')
        renpy.hide_screen('timed_menu_messages')
        no_anim_list = store.chatlog[-20:]
        renpy.show_screen('messenger_screen', no_anim_list=no_anim_list)
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
        ## Get rid of the backup
        store.chatbackup = None
        if (not store.dialogue_paraphrase and store.dialogue_picked != ""):
            say_choice_caption(store.dialogue_picked,
                store.dialogue_paraphrase, store.dialogue_pv)
        store.chatbackup = None
        ## Set the next node as the block of items resulting from the choice
        renpy.ast.next_node(item.subparse.block[0])
        return

## A duplicate of the messenger_screen screen that includes an animation
## to smooth out the transition into timed menu answers showing
screen timed_menu_messages(no_anim_list=None):
    tag menu
    zorder 1
    python:
        yadj.value = yadjValue
        finalchat = None
        if len(chatlog) > 0:
            finalchat = chatlog[-1]
        if (no_anim_list and len(chatlog) > 20
                and chatlog[-20] not in no_anim_list):
            no_anim_list = None

    frame at slide_up_down(-220):
        align (0.5, 1.0)
        yoffset -114
        xfill True
        ysize 1080
        viewport:
            yadjustment yadj
            draggable True
            mousewheel True
            ysize 1080
            xfill True
            has vbox
            spacing 10
            xfill True
            for i index id(i) in chatlog[-bubbles_to_keep:]:
                fixed:
                    yfit True
                    xfill True
                    if i.who.name in ['msg', 'filler']:
                        use special_msg(i)
                    elif i.who == answer:
                        pass
                    # This trick means that the program displays
                    # an invisible bubble behind the visible one
                    # so the animation doesn't "slide" in
                    elif i == finalchat:
                        use chat_animation(i, True)
                    if (i.who.name not in ['msg', 'filler', 'answer']
                            and (no_anim_list is None
                                or i not in no_anim_list)):
                        use chat_animation(i)
                    elif (i.who.name not in ['msg', 'filler', 'answer']
                            and i in no_anim_list):
                        use chat_animation(i, no_anim=True)
                null height 10

transform slide_up_down(y=-220):
    yoffset 0
    pause 0.1
    ease 0.5 yoffset y
    on hide:
        yoffset y
        ease 0.5 yoffset 0

transform slide_down(y=-220):
    yoffset y
    ease 0.5 yoffset 0

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

        if _in_replay:
            # If we're in replay, then the player only gets to see answers if
            # they previously chose an answer
            has_chosen = False
            for item in items:
                if item.chosen:
                    has_chosen = True
                    break
            if not has_chosen:
                # Special case where we don't show the menu
                renpy.jump('no_timed_menu_choices')


    hide screen messenger_screen
    $ no_anim_list = chatlog[-20:-1]
    show screen timed_menu_messages(no_anim_list)
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
    hide screen timed_menu_messages
    pause 0.5
    $ no_anim_list = chatlog[-20:]
    show screen messenger_screen(no_anim_list)
    jump expression end_label

## A label used during a replay when the player has never chosen an answer
## in a timed menu
label no_timed_menu_choices():
    # No new screens to show; just execute the narration and jump to
    # the end
    $ narration = timed_menu_dict['narration']
    while narration:
        $ msg = narration.pop(0)
        $ who = msg['who']
        $ who(what=msg['what'], pauseVal=msg['pauseVal'], img=msg['img'],
            bounce=msg['bounce'], specBubble=msg['specBubble'])
    $ end_label = timed_menu_dict['end_label']
    $ timed_menu_dict = {}
    jump expression end_label


## A label triggered after the player makes a choice in a timed menu.
label finish_timed_menu():
    ## Get rid of the backup; check if paraphrased dialogue should be sent
    $ chatbackup = None
    $ no_anim_list = chatlog[-20:]
    if (not dialogue_paraphrase and dialogue_picked != ""):
        # The choice was not paraphrased and should be posted
        $ say_choice_caption(dialogue_picked, dialogue_paraphrase, dialogue_pv)

    $ chatbackup = None

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


## Dictionary which holds information needed to display timed menus
default timed_menu_dict = { }

## Screen that borrows from the choice screen, but customized for
## timed menus.
screen timed_choice(items, paraphrased=None):
    zorder 150

    if persistent.custom_footers and not renpy.is_skipping():
        default the_anim = choice_anim
    else:
        default the_anim = null_anim
    default item_len = len(items) > 2

    frame:
        at shrink_away()
        if persistent.custom_footers and item_len:
            style_prefix 'new_three'
        elif persistent.custom_footers:
            style_prefix 'new_two'
        elif not persistent.custom_footers and item_len:
            style_prefix 'old_three'
        else:
            style_prefix 'old_two'
        hbox:
            for num, i in enumerate(items):
                $ fnum = float(num*0.2)
                fixed:
                    fit_first True
                    ## This choice both appears and disappears
                    if (i.kwargs.get('appear_time', None)
                            and i.kwargs.get('disappear_time', None)):
                        at choice_appear_disappear(
                            begin_delay=i.kwargs['appear_time'],
                            end_delay=(i.kwargs['disappear_time']
                                - i.kwargs['appear_time']),
                            mod=pv)
                    ## This choice only appears
                    elif i.kwargs.get('appear_time', None):
                        at choice_appear(i.kwargs['appear_time'], pv)
                    ## This choice only disappears
                    elif i.kwargs.get('disappear_time', None):
                        at choice_disappear(i.kwargs['disappear_time'], pv)
                    ## This choice is simply on-screen
                    else:
                        at the_anim(fnum)

                    textbutton i.caption:
                        # Check if the caption is pretty long
                        if (len(i.caption) > 60
                                or (len(items) > 2 and len(i.caption) > 42)):
                            text_size 25
                        elif len(i.caption) > 42:
                            text_size 28
                        if (persistent.dialogue_outlines
                                and persistent.custom_footers):
                            text_outlines [ (2, "#000",
                                absolute(0), absolute(0)) ]
                        elif (persistent.dialogue_outlines
                                and not persistent.custom_footers):
                            text_outlines [ (2, "#fff",
                                absolute(0), absolute(0)) ]


                        if (persistent.past_choices and not observing
                                and i.chosen):
                            if persistent.custom_footers:
                                foreground 'seen_choice_check_circle'
                                background 'call_choice_check'
                                hover_background 'call_choice_check_hover'
                            else:
                                foreground 'seen_choice_check'

                        action [SetVariable('dialogue_picked', i.caption),
                            Function(set_paraphrase, screen_pref=paraphrased,
                                item_pref=(i.kwargs.get('paraphrased',
                                None))),
                            Function(execute_timed_menu_action, item=i)]


                    if i.kwargs.get('disappear_time', None):
                        add 'header_hg' align (0.5, 0.98):
                            if i.kwargs.get('appear_time', None):
                                at choice_disappear_hourglass(
                                    pause_time=(i.kwargs['disappear_time']),
                                    mod=pv)
                            else:
                                at choice_disappear_hourglass(
                                    i.kwargs['disappear_time'], pv)

    frame:
        at wait_fade()
        align (0.5, 1.0)
        background "#282828"
        xysize (750, 113)
        text "Choose a reply" color "#fff" text_align 0.5 align (0.5, 0.5)

transform choice_disappear_hourglass(pause_time=0.0, mod=0.8):
    alpha 0.0 rotate 0
    pause max((pause_time*mod) - (2.0*mod) - mod, 0.1)
    block:
        rotate 0
        easein 0.25*mod alpha 0.6 zoom 1.1
        easeout 0.25*mod alpha 1.0 zoom 1.0
        pause 0.5
        ease 1.0 rotate 180
        repeat


transform choice_disappear(pause_time=0.0, mod=0.8):
    xzoom 1.0 alpha 1.0 zoom 1.0
    pause max((pause_time*mod) - (2.0*mod) - mod, 0.1)
    # Indicate it's about to expire
    block:
        easein 0.25*mod alpha 0.6 zoom 1.1
        easeout 0.25*mod alpha 1.0 zoom 1.0
        repeat 2
    pause (pause_time*mod) - max((pause_time*mod) - (3.0*mod), 0.1) - mod
    parallel:
        ease 0.625*mod alpha 0.0
    parallel:
        ease 0.625*mod xzoom 0.01

transform choice_appear(pause_time=0.0, mod=0.8):
    xzoom 0.01 alpha 0.0
    pause max(pause_time*mod, 0.1)
    parallel:
        pause 0.125*mod
        ease 0.5*mod alpha 1.0
    parallel:
        ease 0.625*mod xzoom 1.0

    on hover:
        ease 0.5 yoffset 5
        ease 0.5 yoffset -5
        repeat
    on idle:
        linear 0.3 yoffset 0

transform choice_appear_disappear(begin_delay=0.0, end_delay=1.0, mod=0.8):
    xzoom 0.01 alpha 0.0
    pause max(begin_delay*mod, 0.1)
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
        repeat 2
    pause (end_delay*mod) - max((end_delay*mod) - (3.0*mod), 0.1) - mod
    parallel:
        ease 0.625*mod alpha 0.0
    parallel:
        ease 0.625*mod xzoom 0.01



style choice_common_frame:
    yalign 1.0
    top_padding 20
    xsize 750
    ysize 220

style choice_common_hbox:
    xalign 0.5
    spacing 20

style new_choice_frame:
    is choice_common_frame
    yoffset -113 - 20

style old_choice_frame:
    is choice_common_frame
    yoffset -113 - 25

style new_three_frame:
    is new_choice_frame

style old_three_frame:
    is old_choice_frame

style new_three_hbox:
    is choice_common_hbox
    spacing 5

style old_three_hbox:
    is choice_common_hbox
    spacing 2

style new_two_hbox:
    is choice_common_hbox

style old_two_hbox:
    is choice_common_hbox

style new_two_frame:
    is new_choice_frame

style old_two_frame:
    is old_choice_frame

style new_three_button:
    is phone_vn_choice_button
    xmaximum (750 // 3) - 10

style new_three_button_text:
    is phone_vn_choice_button_text
    text_align 0.5
    size 28
    align (0.5, 0.5)
    xmaximum (750 // 3) - 10 - 50

style old_three_button:
    is choice_button
    xmaximum (750 // 3) - 4

style old_three_button_text:
    is choice_button_text
    text_align 0.5
    size 28
    align (0.5, 0.5)
    xmaximum (750 // 3) - 4 - 40

style new_two_button:
    is phone_vn_choice_button
    xmaximum (750 // 2) - 20

style new_two_button_text:
    is new_three_text
    size 33
    xmaximum (750 // 2) - 20 - 50

style old_two_button:
    is choice_button
    xmaximum (750 // 2) - 20

style old_two_button_text:
    is old_three_text
    size 33
    xmaximum (750 // 2) - 20 - 40



transform shrink_away():
    yzoom 0.0
    pause 0.2
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