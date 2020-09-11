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

    python:
        len_var = len(items) > 2

    frame:
        at shrink_away()
        if persistent.custom_footers:
            yoffset -113-15
        else:
            yoffset -113-25
        hbox:
            if persistent.custom_footers:
                style_prefix 'phone_vn_choice'
                if len_var:
                    spacing 5
                else:
                    spacing 20
            else:
                style_prefix 'choice'
                if len_var:
                    spacing 2
                else:
                    spacing 20
            xalign 0.5
            for num, i in enumerate(items):
                $ fnum = float(num*0.2)
                textbutton i.caption at the_anim(fnum):
                    text_text_align 0.5
                    text_align (0.5, 0.5)
                    if len_var:
                        text_size 28
                        xmaximum (750 // 3) - 4
                        text_xmaximum (750 // 3) - 4 - 40
                    else:
                        xmaximum (750 // 2) - 20
                        text_xmaximum (750 // 2) - 20 - 40
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

    frame:
        at wait_fade()
        align (0.5, 1.0)
        background "#282828"
        xysize (750, 113)
        text "Choose a reply" color "#fff" text_align 0.5 align (0.5, 0.5)

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
    is new_three_button_text
    size 33
    xmaximum (750 // 2) - 20 - 50

style old_two_button:
    is choice_button
    xmaximum (750 // 2) - 20

style old_two_button_text:
    is old_three_button_text
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