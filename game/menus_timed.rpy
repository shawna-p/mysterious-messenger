init python:

    def execute_timed_menu_action(item, jump_to_end=False):
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
        item.value.chosen[(item.value.location, item.value.label)] = True

        if jump_to_end:
            # This means (Say nothing) was chosen, so the MC shouldn't
            # post any messages.
            store.dialogue_picked = ""
            store.dialogue_paraphrase = store.paraphrase_choices
            store.dialogue_pv = 0
            # Jump to the end of the menu; no choice dialogue to execute.
            end_label = store.timed_menu_dict['end_label']
            store.timed_menu_dict = {}
            renpy.jump(end_label)
        else:
            renpy.jump('finish_timed_menu')

        return

    class TimedMenuValue(AnimatedValue):
        """
        A class which inherits from the AnimatedValue bar, but stops
        animating when certain conditions are met. Used for timed menus.
        """

        def __init__(self, value=0.0, range=1.0, delay=1.0, old_value=None):
            if old_value == None:
                old_value = value

            self.value = value
            self.range = range
            self.delay = delay
            self.old_value = old_value
            self.start_time = None
            self.restart_time = 0.0
            self.pause_time = 0.0
            self.pausing = True

            self.adjustment = None

        def periodic(self, st):

            if self.start_time is None:
                self.start_time = st
                print_file("Start time is", self.start_time)

            if self.value == self.old_value:
                return

            # if (st % 1.0 >= 0.0 and st % 1.0 <= 0.01):
            #     print_file("pausing_timed_menu is", store.pausing_timed_menu,
            #         "and t_menu_is_pausing is", store.t_menu_is_pausing)

            restart_time = 0.0
            # Halt timer
            if store.pausing_timed_menu and not store.t_menu_is_pausing:
                store.t_menu_is_pausing = True
                store.t_menu_pause_time = st
                print_file("Pausing at time", st)

            # Resume timer
            if not store.pausing_timed_menu and store.t_menu_is_pausing:
                store.t_menu_is_pausing = False
                restart_time = st - store.t_menu_pause_time
                store.t_menu_resume_time = st
                store.t_menu_offset += restart_time


            # Holding on the pause/confirm screen
            if store.pausing_timed_menu:
                restart_time = st - store.t_menu_pause_time + store.t_menu_offset

            if restart_time == 0.0:
                restart_time = store.t_menu_offset

            fraction = (st - self.start_time - restart_time) / self.delay
            fraction = min(1.0, fraction)

            value = self.old_value + fraction * (self.value - self.old_value)

            self.adjustment.change(value)

            if fraction != 1.0:
                return 0



## A duplicate of the messenger_screen screen that includes an animation
## to smooth out the transition into timed menu answers showing.
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

## Two animations to move the messages up and down the screen when
## the choices appear/disappear.
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

## The length of extra time to wait while the answers are on-screen before
## the menu expires.
default end_menu_buffer = 3.0
## Variables to handle the pausing and un-pausing of timed menus via clicking
## the back button.
default pausing_timed_menu = False
default t_menu_pause_time = 0.0
default t_menu_is_pausing = False
default t_menu_resume_time = 0.0
default t_menu_offset = 0.0

## A label which handles animating the messages up the screen to make room
## for choices, if there are available choices and timed menus are set.
## Otherwise it ensures the dialogue for the menu plays out if it is not
## set to be skipped.
label execute_timed_menu():
    if not timed_menu_dict:
        $ print_file("ERROR: Something went wrong with timed menus")
        return

    python:
        pausing_timed_menu = False
        t_menu_pause_time = 0.0
        t_menu_is_pausing = False
        t_menu_resume_time = 0.0
        t_menu_offset = 0.0

    ## First things first: if the player is skipping, they do not receive the
    ## opportunity to answer at all.
    if renpy.is_skipping():
        $ timed_menu_dict['no_choices'] = True
        jump execute_timed_menu_narration

    ## Separate out the vars
    python:
        wait_time = timed_menu_dict['wait_time']
        end_label = timed_menu_dict['end_label']
        narration = timed_menu_dict['narration']
        items = timed_menu_dict['items']
        screen_kwargs = timed_menu_dict['menu_kwargs']
        para = screen_kwargs.get('paraphrased', None)

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
        extra_time = end_menu_buffer * persistent.timed_menu_pv

        if _in_replay:
            # If we're in replay, then the player only gets to see answers if
            # they previously chose an answer
            has_chosen = False
            for item in items:
                if item.chosen:
                    has_chosen = True
                    break
            if not has_chosen:
                # Special case where the menu isn't shown
                timed_menu_dict['no_choices'] = True
                renpy.jump('execute_timed_menu_narration')

    if not persistent.use_timed_menus:
        jump execute_timed_menu_narration

    # If the program got here, it is time to animate the messages
    # sliding up the screen.
    hide screen messenger_screen
    $ no_anim_list = chatlog[-20:-1]
    show screen timed_menu_messages(no_anim_list)
    show screen timed_choice(items, para)
    show screen answer_countdown(end_label, wait_time+extra_time,
        use_timer=False)
        #custom_action=[ Hide('answer_countdown'), Show('pause_button') ])

    # Execute the narration
    jump execute_timed_menu_narration

## This label executes the timed menu narration.
label execute_timed_menu_narration():
    # Don't play the narration if set to skip it
    $ menu_skip_empty = timed_menu_dict['menu_kwargs'].get('skip_empty', None)
    if (timed_menu_dict.get('no_choices', None)
            and ((menu_skip_empty is None and not show_empty_menus)
                or (menu_skip_empty))):
        $ end_label = timed_menu_dict['end_label']
        $ timed_menu_dict = {}
        jump expression end_label

    # The narration nodes are all chained to execute in sequence, so it's
    # only necessary to execute the first one.
    $ narration = timed_menu_dict['narration']
    $ msg = narration.pop(0)
    $ msg.execute()
    return

## The program jumps here at the end of a timed menu when the player has not
## yet made a choice. Depending on the settings, it may either hide the menu
## or show the regular choice screen to the player.
label end_of_timed_menu():
    # If the dialogue is exhausted, the player has missed the time window to
    # reply. There is a small buffer for them to finish reading the last
    # message and then everything is reset.
    if (persistent.use_timed_menus
            and not timed_menu_dict.get('no_choices', False)):
        $ messenger_pause(end_menu_buffer * persistent.timed_menu_pv)
        hide screen timed_choice
        hide screen answer_countdown
        show screen pause_button
        hide screen timed_menu_messages
        # Show the original messenger screen; it should
        # animate back down into position
        show screen messenger_screen(no_anim_list=chatlog[-20:],
            animate_down=True)

    # Otherwise, if the player has timed menus turned off, it is time to show
    # them the choice screen
    if (not persistent.use_timed_menus
            and not timed_menu_dict.get('item', None)):
        call answer
        python:
            items = timed_menu_dict['items']
            items.append(timed_menu_dict['autoanswer'])
            screen_kwargs = timed_menu_dict['menu_kwargs']
            para = screen_kwargs.get('paraphrased', None)
        call screen choice(items=items, paraphrased=para)
        return

    $ end_label = timed_menu_dict.get('end_label', None)
    if end_label is None:
        return
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

    if persistent.use_timed_menus:
        # Hide all the choice screens
        hide screen timed_choice
        hide screen answer_countdown
        show screen pause_button
        hide screen timed_menu_messages
        # Show the original messenger screen; it should
        # animate back down into position
        show screen messenger_screen(no_anim_list=no_anim_list,
            animate_down=True)

    $ item = timed_menu_dict['item']
    $ timed_menu_dict = {}
    # This executes the statements bundled after the choice
    $ renpy.ast.next_node(item.subparse.block[0])
    return


## Dictionary which holds information needed to display timed menus
default timed_menu_dict = { }

## Screen that borrows from the choice screen, but customized for
## timed menus. The choices are arranged horizontally instead of vertically,
## and there is only room for a maximum of three choices at once.
screen timed_choice(items, paraphrased=None):
    zorder 150

    if persistent.custom_footers and not renpy.is_skipping():
        default the_anim = choice_anim
    else:
        default the_anim = null_anim
    default item_len = len(items) > 2

    frame:
        # The choices are squashed vertically when appearing and disappearing
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
                textbutton i.caption:
                    at the_anim(fnum)
                    # Check if the caption is long; reduce font size
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
                            i.action]

    viewport:
        # Use this viewport to "consume" the mouse input so the player
        # can't click to mess up the timed answer timing.
        at wait_fade()
        draggable True
        align (0.5, 1.0)
        xysize (750, 113)
        frame:
            align (0.5, 1.0)
            background "#282828"
            xysize (750, 113)
            text "Choose a reply":
                color "#fff" text_align 0.5 align (0.5, 0.5)

## This very long section defining styles allows style prefixes to take
## care of how to display the choices based on how many choices there are
## and whether the player is using the new or old-style UI.
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