#####################################
# Answer Button
#####################################

screen answer_button(act=None):
    zorder 4
    tag chat_footer
    add 'pause_square' ysize config.screen_height-113-165 yalign 0.0 yoffset 165

    add "pause_ui" xalign 1.0 xoffset -25 yoffset 190
    add "answer_ui" yalign 1.0

    imagebutton:
        yalign 1.0
        focus_mask None
        idle 'transparent_answer'
        activate_sound "audio/sfx/UI/answer_screen.mp3"
        if not act:
            action [Show('pause_button'), Return()]
        else:
            action act
        keysym "K_SPACE"

    if not choosing:
        use fast_slow_buttons()

#####################################
# Continue Button
#####################################
## This button appears when transitioning from
## a chatroom directly into a VN
screen continue_button():
    zorder 4
    tag chat_footer
    if persistent.custom_footers:
        add 'custom_darklight_continue_button' yalign 1.0
    else:
        add 'darklight_continue_button' yalign 1.0
    imagebutton:
        yalign 1.0
        focus_mask None
        idle 'transparent_answer'
        action Return()
        keysym "K_SPACE"

#####################################
# Pause/Play footers
#####################################

# This is the screen that shows the pause button
# (but the chat is still playing)
screen pause_button():
    zorder 4
    tag chat_footer

    if (on_screen_choices > 0 and persistent.use_timed_menus
            and not _in_replay):
        viewport:
            # Use this viewport to "consume" the mouse input so the player
            # can't click to mess up the timed answer timing.
            draggable True
            align (0.5, 1.0)
            xysize (config.screen_width, 113)
            frame:
                align (0.5, 1.0)
                background "#282828"
                xysize (config.screen_width, 113)
                text "Choose a reply":
                    color "#fff" text_align 0.5 align (0.5, 0.5)
    else:
        imagebutton:
            yalign 1.0
            focus_mask True
            idle 'phone_pause'
            if (not choosing and not block_interrupts and
                    not (timed_menu_dict and persistent.use_timed_menus
                        and not _in_replay)
                    and not renpy.get_screen('answer_choice')):
                action ShowMenu('play_button_pause_chat')
                keysym "K_SPACE"

        if not choosing:
            use fast_slow_buttons()


label play_after_link(jump_link=None):
    $ chat_stopped = False
    show screen pause_button
    if jump_link:
        $ jlink = jump_link
        $ renpy.pop_call()
        jump expression jlink
    return

## True if the chat is stopped (typically due to waiting for a link
## to be pressed).
default chat_stopped = False

screen play_button_pause_chat():
    zorder 4
    use messenger_screen(no_anim_list=chatlog[-bubbles_to_keep:])
    use phone_overlay(is_menu_pause=True)
    if persistent.custom_footers:
        add 'custom_pausebutton' xalign 1.0 xoffset -25 yoffset 190
    else:
        add "pausebutton" xalign 1.0 xoffset -25 yoffset 190
    add "pause_square" ysize config.screen_height-113-165 yalign 0.0 yoffset 165
    imagebutton:
        xanchor 0.0
        xpos 0
        yalign 1.0
        focus_mask True
        idle 'phone_play'
        keysym "K_SPACE"
        action Return()

# This screen is visible when the chat is paused;
# shows the play button
screen stop_chat_screen(wait_for_interact=False):
    zorder 4
    tag chat_footer

    default wait_text = str(wait_for_interact) if wait_for_interact else "Click the link to proceed"

    viewport:
        # Use this viewport to "consume" the mouse input so the player
        # can't click to proceed without going through a link.
        draggable True
        align (0.5, 1.0)
        xysize (config.screen_width, 113)
        if persistent.link_wait_pause:
            add 'phone_pause' align (0.5, 1.0)
        else:
            frame:
                align (0.5, 1.0)
                background "#282828"
                xysize (config.screen_width, 113)
                text wait_text:
                    color "#fff" text_align 0.5 align (0.5, 0.5)

# Buttons that speed up or slow down the chat speed
screen fast_slow_buttons():
    # Fast button
    imagebutton:
        xalign 0.985
        yalign 1.0 yoffset -12
        focus_mask None
        idle "fast_slow_button"
        keysym "K_RIGHT"
        action [Function(fast_pv),
                Hide('speed_num'),
                Show("speed_num")]

    # Slow button
    imagebutton:
        xalign 0.015
        yalign 1.0 yoffset -12
        focus_mask None
        idle "fast_slow_button"
        keysym "K_LEFT"
        action [Function(slow_pv),
                Hide('speed_num'),
                Show("speed_num")]


#####################################
# Chat Header Overlay
#####################################

# Displays a list of the characters in the chatroom
image in_chat_display = DynamicDisplayable(in_chat_fn)
# The clock that gets displayed in chatrooms
define myClock = Clock(30)

init python:
    def in_chat_fn(st, at):
        """Display the names of the characters in the chatroom."""

        list_of_char = ''
        for index, chara in enumerate(store.in_chat):
            list_of_char += chara
            if index+1 < len(store.in_chat):
                list_of_char += ', '

        return Text(list_of_char, style='in_chat_list_style'), None

    def battery_charge_icon(st, at):
        """Display the charging or fully charged battery icons."""

        # 0 = no idea what the status is, or -1
        # 1 = running on battery, not plugged in
        # 2 = plugged in, no battery available
        # 3 = plugged in, charging
        # 4 = plugged in, battery fully charged
        battery = renpy.display.behavior.pygame.power.get_power_info()
        if battery.state == 3 or (battery.state == 4 and battery.percent <= 97):
            return Transform('battery_charged', alpha=0.75), 0.1
        elif battery.state == 4 and battery.percent > 97:
            return Transform('battery_charging', alpha=0.75), 0.1
        else:
            return Transform('transparent', size=(18,26)), None

    def battery_level_bar(st, at):
        """Return the battery level image to use based on remaining power."""

        battery = renpy.display.behavior.pygame.power.get_power_info()
        if battery.percent > 50:
            img1 = "battery_high"
        elif battery.percent < 20:
            img1 = 'battery_low'
        else:
            img1 = 'battery_med'

        return Fixed(img1, Fixed('charging_icon',
            size=(18,26), xalign=0.5, yalign=0.4)), 0.5

    def battery_empty_bar(st, at):
        """
        Return a compound image of the battery empty image plus the
        correct charging/charged image to make up a full battery icon.
        """

        battery = renpy.display.behavior.pygame.power.get_power_info()
        return Fixed("battery_empty_img",
                Fixed('charging_icon',
                size=(18,26), xalign=0.5, yalign=0.4)), 0.5

image battery_remaining = DynamicDisplayable(battery_level_bar)
image battery_empty = DynamicDisplayable(battery_empty_bar)
image charging_icon = DynamicDisplayable(battery_charge_icon)

style battery_bar:
    is empty
    bar_vertical True
    bottom_bar 'battery_remaining'
    top_bar 'battery_empty'
    xsize 18
    ysize 26
    align (.5, .5)

# The style that is used when the program cannot detect battery level
style battery_bar_undetected:
    is battery_bar
    bottom_bar "battery_high"

## This screen shows the header/footer above the chat
screen phone_overlay(is_menu_pause=False):
    zorder 2
    add 'phone_ui'

    ## Python because we want this to update as the screen updates
    $ battery = renpy.display.behavior.pygame.power.get_power_info()

    fixed:
        xysize(150,80)
        pos (105, 105)
        yanchor 0.5
        if starter_story:
            xoffset -85
        imagebutton:
            align (0.5, 0.5)
            auto 'maxSpeed_%s'
            focus_mask True
            selected renpy.is_skipping()
            if not choosing and not renpy.get_screen('no_modal_confirm'):
                action Skip()
    if starter_story or persistent.testing_mode or persistent.unlock_all_story:
        fixed:
            xysize (150, 80)
            pos (config.screen_width-15, 105) xanchor 1.0 yanchor 0.5
            imagebutton:
                align (0.5, 0.5)
                focus_mask True
                if starter_story:
                    idle 'skip_intro_idle'
                    hover 'skip_intro_hover'
                    if not renpy.get_screen('no_modal_confirm'):
                        action [If(renpy.call_stack_depth() > 0,
                                Function(renpy.pop_call), NullAction()),
                            SetField(persistent, 'first_boot', False),
                            SetField(persistent, 'on_route', True),
                            SetVariable('gamestate', VNMODE),
                            Function(purge_temp_texts),
                            If(is_menu_pause,
                                Function(renpy.jump_out_of_context,
                                    label='chat_end'),
                                Jump('chat_end'))]
                else:
                    idle 'skip_to_end_idle'
                    hover 'skip_to_end_hover'
                    if not renpy.get_screen('no_modal_confirm'):
                        if not is_menu_pause:
                            action If(renpy.call_stack_depth() > 1,
                                [Function(renpy.pop_call), Jump('just_return')],
                                [Jump('just_return')])
                        else:
                            action If(renpy.call_stack_depth() > 1,
                                [Function(renpy.pop_call),
                                    Function(renpy.jump_out_of_context,
                                        label='just_return')],
                                [Function(renpy.jump_out_of_context,
                                        label='just_return')])

    frame:
        ypos 105 yalign 0.5
        if starter_story:
            xalign 0.5
        else:
            xalign 0.62
        xysize (350, 100)
        add 'in_chat_display'

    # 0 = no idea what status is, or -1
    # 1 = running on battery, not plugged in
    # 2 = plugged in, no battery available
    # 3 = plugged in, charging
    # 4 = plugged in, battery fully charged
    hbox:
        align (1.0, 0.0)
        spacing 15
        fixed:
            xysize (20, 48)
            # Use the actual battery information
            if battery.state >= 1 and battery.state != 2:
                bar:
                    value StaticValue(value=float(battery.percent)/100.0,
                        range=1.0)
                    style 'battery_bar'
            # No battery information available; use 75%
            else:
                bar:
                    value StaticValue(value=float(75)/100.0,
                        range=1.0)
                    style 'battery_bar_undetected'
        add myClock yalign 1.0 xoffset -5 yoffset -3

    if not starter_story:
        fixed:
            xysize (50,50)
            yanchor 0.5
            pos (25, 105)
            imagebutton:
                align (0.5, 0.5)
                idle 'back_arrow_btn'
                hover Transform('back_arrow_btn', zoom=1.2)
                keysym "K_BACKSPACE"
                # The program should not allow the back button to be pressed
                # again while the non-modal confirm screen is showing.
                if renpy.get_screen('no_modal_confirm'):
                    action None
                # Back button during a history replay ends it
                elif _in_replay:
                    action EndReplay(False)
                # Back button during the chat creator jumps back to it
                elif (is_main_menu_replay):
                    action If(is_menu_pause,
                        Function(renpy.jump_out_of_context,
                            label='chatroom_creator_setup'),
                        Jump('chatroom_creator_setup'))
                # Back button when the chat is expired jumps out of it
                elif (observing or current_timeline_item.currently_expired):
                    action If(is_menu_pause,
                        Function(renpy.jump_out_of_context,
                            label='exit_item_early'),
                        Jump('exit_item_early'))
                elif on_screen_choices > 0:
                    # Continuous menus must continue on or their animation
                    # timing will de-sync.
                    action Show('no_modal_confirm', message=("Do you really "
                        + "want to exit this chatroom? Please note that you "
                        + "cannot participate once you leave. If you want to "
                        + "enter this chatroom again, you will need to buy it "
                        + "back."), yes_action=[Hide('no_modal_confirm'),
                                If(is_menu_pause,
                                    Function(renpy.jump_out_of_context,
                                        label='exit_item_early'),
                                    Jump('exit_item_early'))],
                            no_action=[Hide('no_modal_confirm')])
                # Otherwise, the player is trying to exit the chat while
                # it's still "active"
                else:
                    action CConfirm(("Do you really want to "
                        + "exit this chatroom? Please note that you cannot "
                        + "participate once you leave. If you want to enter "
                        + "this chatroom again, you will need to buy it back."),
                                    [If(is_menu_pause,
                                        Function(renpy.jump_out_of_context,
                                            label='exit_item_early'),
                                        Jump('exit_item_early'))])


#************************************
# Countdown Screen
#************************************

# This is a screen to test out timed responses
# Default countdown time is 5 seconds
screen answer_countdown(themenu, count_time=5, use_timer=True):
    zorder 151
    if use_timer:
        timer count_time:
            repeat False
            action If(persistent.use_timed_menus,

                [ Hide('answer_countdown'),
                Hide('continue_answer_button'),
                Show('pause_button'),
                SetVariable("timed_choose", False) ],

                [ Hide('answer_countdown'),
                Hide('continue_answer_button'),
                Show('pause_button'),
                SetVariable('choosing', True),
                SetVariable('timed_choose', True),
                Jump(themenu) ]
                )

    bar value TimedMenuValue(0, count_time, count_time, count_time):
        at alpha_dissolve
        style 'answer_bar'


#************************************
# Continue Answer
#************************************

default timed_choose = False
default reply_instant = False
default using_timed_menus = False

init python:

    def timed_answer_modifier(count_time):
        """Return count_time modified to account for the current pv."""

        modifier = 1.00
        if renpy.is_skipping():
            # Max Speed active
            modifier = 0.0
        else:
            modifier = 0.1875 * (((store.persistent.pv - 0.2) /
                                store.chat_speed_increment) - 4)
        return count_time + (count_time * modifier)

## A helper label which will pause the chat for the given
## number of seconds in count_time, multiplied by a modifier
## depending on how fast the chat speed is
label timed_pause(count_time):
    if not _in_replay:
        # Timed answers don't show up in replays, so don't pause
        pause timed_answer_modifier(count_time)
    return

## Timed answers to speed up/slow down based on how fast
## the player has the chat speed set to. Default is 0.8,
## increased/decreased by 0.15 (aka increased/decreased by
## 18.75% each time).
## So if the chat is at 3x normal speed, the time to answer
## the menu is decreased by 3x.
label continue_answer(themenu, count_time=5):
    # Timed menus don't show up for players who are skipping
    # through entire conversations or who are replaying an existing
    # chatroom. Not allowing 'observing' players to choose an
    # answer avoids the problem of players who didn't initially
    # choose an answer being unable to continue
    if not renpy.is_skipping() and not observing:
        $ using_timed_menus = True
        show screen answer_countdown(themenu, timed_answer_modifier(count_time))
        hide screen viewCG
        $ pre_choosing = True
        show screen continue_answer_button(themenu)
        pause 0.01
    else:
        $ timed_choose = False
    return

screen continue_answer_button(themenu):
    zorder 4
    tag chat_footer
    if persistent.custom_footers:
        add "custom_answerbutton" yalign 1.0
    else:
        add "answerbutton" yalign 1.0

    imagebutton:
        yalign 1.0
        focus_mask None
        idle "transparent_answer"
        activate_sound "audio/sfx/UI/answer_screen.mp3"
        keysym "K_SPACE"
        action [SetVariable("choosing", True),
                SetVariable('timed_choose', True),
                Hide('answer_countdown'),
                Hide('continue_answer_button'),
                Show('pause_button'),
                Jump(themenu)]

    # If the player starts skipping in the middle of the menu,
    # they either forfeit the ability to pick an answer or
    # the program auto-selects the answer button for them
    if renpy.is_skipping() and not observing:
        timer 0.01:
            action [
                Hide('answer_countdown'),
                Hide('continue_answer_button'),
                Show('pause_button'),
                If(persistent.use_timed_menus,
                    [SetVariable('choosing', True),
                    SetVariable('timed_choose', True),
                    Jump(themenu)],

                    SetVariable('timed_choose', False))
            ]

style answer_bar:
    bar_invert True
    thumb 'gui/slider/horizontal_idle_thumb.png'
    left_bar Frame('gui/slider/left_horizontal_bar.png',4,4)
    right_bar Frame('gui/slider/right_horizontal_bar.png',4,4)
    left_gutter 18
    right_gutter 18
    thumb_offset 18
    ypos 1210
