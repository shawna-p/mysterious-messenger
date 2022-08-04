########################################################
## This is the text message hub, where the player can
## view any of their ongoing text conversations
########################################################
screen text_message_hub():

    tag menu
    on 'replace' action [AutoSave()]
    on 'show' action [AutoSave()]

    use menu_header('Text Message', Show('chat_home', Dissolve(0.5))):

        viewport:
            xsize 725
            ysize config.screen_height-184
            draggable True
            mousewheel True
            side_spacing 5
            scrollbars "vertical"

            xalign 0.5
            yalign 0.95

            vbox:
                xalign 0.5
                spacing 10
                for i in all_characters:
                    # First display unread messages
                    if i.text_msg.msg_list and not i.text_msg.read:
                        use text_hub_display(i)
                for i in all_characters:
                    # Next display read messages
                    if i.text_msg.msg_list and i.text_msg.read:
                        use text_hub_display(i)

## Displays an individual message preview.
screen text_hub_display(i):

    python:
        text_log = i.text_msg.msg_list
        text_read = i.text_msg.read
        text_label = i.text_msg.reply_label
        text_notified = i.text_msg.notified

        if len(text_log) > 0:
            last_text = text_log[-1]
            text_time = last_text.thetime
        else:
            last_text = False
            text_time = False


    button:
        style_prefix 'text_msg'
        selected last_text and text_read
        # If there's a label, jump to it, otherwise
        # just show the messages.
        action If((text_label and i.real_time_text),

                    [Function(text_message_begin, text_person=i),
                    Jump('play_text_message')],

                    [Function(text_message_begin, text_person=i),
                    Show('text_message_screen', sender=i, animate=False)])

        hbox:
            fixed:
                add last_text.who.get_pfp(127) align(0.5, 0.5)

            frame:
                style_prefix 'text_preview'
                has vbox
                text last_text.who.name
                text text_popup_preview(last_text, 16)

            frame:
                style_prefix 'text_timestamp'
                has vbox
                if last_text and not text_read:
                    spacing 30
                else:
                    spacing 10
                text text_time.get_text_msg_time()
                hbox:
                    if last_text and text_read:
                        add 'read_text_envelope'
                    else:
                        add 'new_text'
                        add 'new_text_envelope'

style text_msg_button:
    selected_background 'message_idle_bkgr'
    selected_hover_background 'message_hover_bkgr'
    background 'unread_message_idle_bkgr'
    hover_background 'unread_message_hover_bkgr'
    activate_sound 'audio/sfx/UI/email_next_arrow.mp3'
    ysize 150
    xsize 705

style text_msg_hbox:
    align (0.5, 0.5)
    spacing 10

style text_msg_fixed:
    xysize (135, 135)
    align (0.0, 0.5)

style text_preview_frame:
    xysize(380,135)
    yalign 0.5

style text_preview_vbox:
    align (0.0, 0.5)
    spacing 40

style text_preview_text is save_slot_text

style text_timestamp_frame:
    xysize (150, 135)

style text_timestamp_vbox:
    align (0.5, 0.5)

style text_timestamp_text is save_stamp_text

style text_timestamp_hbox:
    spacing 10
    xalign 1.0



init python:
    def allocate_text_popup():
        """Allocate a screen for the text message popup."""

        return allocate_screen(["text_msg_popup", "text_pop_2", "text_pop_3"])

    def MMGoToText(c, popup_tag):
        """Action which occurs when Go To is pressed on a text popup."""
        return If(gamestate is None,
            If ((c.real_time_text and c.text_msg.reply_label),
                [Function(text_message_begin, text_person=c),
                    Function(hide_all_popups),
                    Hide('save_load'),
                    Hide('menu'),
                    Hide('chat_footer'),
                    Hide('phone_overlay'),
                    Hide('settings_screen'),
                    Function(reset_text_popup, popup_tag),
                    Hide(popup_tag),
                    Jump('play_text_message')],

                [Function(text_message_begin, text_person=c),
                    Function(hide_all_popups),
                    Hide('save_load'),
                    Hide('menu'),
                    Hide('chat_footer'),
                    Hide('phone_overlay'),
                    Hide('settings_screen'),
                    Function(reset_text_popup, popup_tag),
                    Hide(popup_tag),
                    Show('text_message_screen', sender=c,
                        animate=False)]))

    def get_text_popup_zorder(tag):
        """Ensure each text popup has its own zorder."""
        for i in range(10):
            scr = store.showing_text_screens.get(i, None)
            if scr is not None:
                if not renpy.get_screen(scr):
                    # No longer showing this screen anyway
                    reset_text_popup(scr)
                    scr = None

            # Hopefully we don't have more than 10 popups at once
            if scr is None:
                # We can show at this zorder
                store.showing_text_screens[i] = tag
                store.showing_text_screens[tag] = i
                print("returning text message zorder of", 100-i)
                return 100-i
        return 100

    def reset_text_popup(tag):
        """Reset information saved on the text popup."""

        print("resetting text popup for", tag)
        i = store.showing_text_screens.pop(tag, None)
        store.showing_text_screens.pop(i, None)


########################################################
## This screen displays the popups that notify
## the user when there is a new text message
########################################################
screen text_msg_popup(c, last_msg=False, hide_screen='text_msg_popup',
        popup_tag=None, offset=(0, 0)):

    #modal True
    zorder 100

    default send_next = not last_msg

    if not last_msg:
        if len(c.text_msg.msg_list) > 0:
            $ last_msg = c.text_msg.msg_list[-1]

    frame:
        style_prefix 'text_popup'
        offset offset
        imagebutton:
            align (1.0, 0.22)
            auto 'input_close_%s'
            if not randint(0,3) and send_next:
                action [Hide(hide_screen),
                        Function(reset_text_popup, popup_tag),
                        Function(deliver_next)]
            else:
                action [Hide(hide_screen),
                        Function(reset_text_popup, popup_tag)]

        hbox:
            add 'new_text_envelope'
            text 'NEW'

        vbox:
            hbox:
                style 'text_popup_hbox2'
                add c.get_pfp(110)

                vbox:
                    style_prefix None
                    style 'text_popup_vbox2'
                    text "From: " + c.name color '#fff'

                    frame:
                        style_prefix 'text_popup_preview'
                        text text_popup_preview(last_msg)

            if (gamestate is None):
                textbutton _('Go to') action MMGoToText(c, popup_tag)
            else:
                null height 70
    timer 13.25:
        action If(randint(0,1) and send_next,
            [Hide(hide_screen, Dissolve(0.25)),
                Function(reset_text_popup, popup_tag),
                Function(deliver_next)],
            [Hide(hide_screen, Dissolve(0.25)),
                Function(reset_text_popup, popup_tag)])

    frame:
        align (1.0, 1.0)
        text "popup tag: [popup_tag] offset: [offset]" color "#fff"

style text_popup_frame:
    xysize (621,373)
    background 'text_popup_bkgr'
    xalign 0.5
    yalign 0.4

style text_popup_imagebutton:
    align (1.0, 0.22)

style text_popup_hbox:
    yalign 0.05
    xalign 0.03
    spacing 15

style text_popup_text:
    color '#73f1cf'
    yalign 1.0
    font gui.sans_serif_1b

style text_popup_vbox:
    xalign 0.3
    yalign 0.85
    spacing 20

style text_popup_hbox2:
    spacing 20

style text_popup_vbox2:
    spacing 10

style text_popup_preview_frame:
    xysize(420,130)
    padding (10,10)
    background 'text_popup_msg'

style text_popup_preview_text:
    size 30
    xalign 0.5 yalign 0.5
    text_align 0.5

style text_popup_button:
    xalign 0.5
    xsize 220
    ysize 70
    background 'menu_select_btn'
    padding(20,20)
    hover_foreground 'menu_select_btn_hover'

style text_popup_button_text:
    is mode_select
    size 28

## Additional screens to allow the program to display multiple popups
screen text_pop_2(c, last_msg=False):
    zorder 99
    use text_msg_popup(c, last_msg, 'text_pop_2')
screen text_pop_3(c, last_msg=False):
    zorder 98
    use text_msg_popup(c, last_msg, 'text_pop_3')
########################################################
## Includes the 'answer' button at the bottom
########################################################
screen text_message_footer(c):

    python:
        text_log = c.text_msg.msg_list
        text_read = c.text_msg.read
        text_label = c.text_msg.reply_label
        if len(text_log) > 0:
            last_msg = text_log[-1]
        else:
            last_msg = False

    vbox:
        xalign 0.5
        yalign 1.0
        yoffset -30
        frame:
            ymaximum 40
            background 'text_msg_line'
        button:
            xsize 468
            ysize 95
            xalign 0.5
            if text_log and text_label and not last_msg.who.right_msgr:
                background 'text_answer_active'
                hover_background 'text_answer_animation'
                if not renpy.get_screen("choice"):
                    action [Jump('play_text_message')]
                    activate_sound "audio/sfx/UI/answer_screen.mp3"
                add 'text_answer_text' xalign 0.5 yalign 0.5
            else:
                background None

## Displays the date separator between two messages that
## have a time difference of one day or more
screen text_date_separator(text_time):

    hbox:
        style_prefix 'date_separator'
        frame:
            background 'text_msg_line'
        text text_time.text_separator_time
        frame:
            background 'text_msg_line'

style date_separator_hbox:
    spacing 10
    xalign 0.5
    ysize 80
    xsize 740
style date_separator_frame:
    ymaximum 40
    xmaximum 240
    yalign 0.5
style date_separator_text:
    size 25
    color '#fff'
    yalign 0.5


init python:
    def award_text_hp(who):
        """Award the player a heart point with who during a text message."""

        who.text_msg.heart_person.increase_heart(who.text_msg.bad_heart)
        if persistent.animated_icons:
            renpy.show_screen('heart_icon_screen',
                character=who.text_msg.heart_person)
        else:
            msg = who.text_msg.heart_person.name + " +1"
            popup_tag = get_random_screen_tag()
            renpy.show_screen('stackable_notifications', message=msg,
                hide_screen=popup_tag, _tag=popup_tag)
        who.text_msg.heart_person = None
        who.text_msg.bad_heart = False
        who.text_msg.heart = False
        store.persistent.HP += 1


########################################################
## This is the screen that actually displays the
## message, though it mostly borrows from the chatroom
## display screen
########################################################
screen text_message_screen(sender, animate=True):

    tag menu

    # If this text message is supposed to trigger a heart icon,
    # display the correctly-coloured heart, award
    # a heart point, and increase the appropriate totals.
    if (not sender.real_time_text
            and sender.text_msg.heart
            and not sender.text_msg.msg_list[-1].who.right_msgr):
        on 'show':
            action [Function(award_text_hp, who=sender)]
        on 'replace':
            action [Function(award_text_hp, who=sender)]

    default prev_msg = None

    use menu_header(sender.name, [SetVariable('CG_who', None),
                                Show('text_message_hub', Dissolve(0.5))], True,
                                hide_bkgr=(_menu and not main_menu) or animate)

    python:
        if not _menu or main_menu:
            yadj.value = yadjValue
        textlog = sender.text_msg.msg_list

    viewport:
        yinitial 1.0
        yadjustment yadj
        draggable True
        mousewheel True
        ysize config.screen_height-311
        yalign 1.0
        yoffset -144

        has vbox
        spacing 20

        for i index id(i) in textlog[-bubbles_to_keep:]:
            # Show the date separator if applicable
            if (len(textlog) > 0 and (prev_msg is not None)
                    and i.thetime.time_diff_minimum(prev_msg.thetime, day=1)):
                use text_date_separator(i.thetime)
            if (len(textlog) > 0 and textlog[0] == i):
                use text_date_separator(i.thetime)
            if (len(textlog) > bubbles_to_keep
                    and textlog[-bubbles_to_keep] == i):
                use text_date_separator(i.thetime)
            fixed:
                yfit True
                xfit True
                if i == textlog[-1]:
                    use text_animation(i, False, True)
                use text_animation(i, (sender.real_time_text
                    and i == textlog[-1] and animate
                    and (not _menu or main_menu)))
            $ prev_msg = i
        null height 5
    if not sender.real_time_text:
        use text_message_footer(sender)
    else:
        frame:
            xalign 0.5
            ymaximum 40
            yalign 1.0 yoffset -125
            background 'text_msg_line'



screen text_animation(i, animate=False, anti=False):
    python:
        transformVar = incoming_message

        if anti:
            transformVar = invisible
        else:
            transformVar = incoming_message

        if not animate and not anti:
            transformVar = null_anim


    if i.who != 'answer' and i.who != 'pause':
        # Add the dialogue
        hbox:
            spacing 5
            if i.who.right_msgr:
                xalign 1.0
                box_reverse True
            xmaximum config.screen_width
            style i.reg_text_style
            null width 18
            frame:
                style i.pfp_style + '_text'
                if not anti and i.who.prof_pic:
                    add i.who.get_pfp(110)

            frame at transformVar:
                # Check if it's an image
                if i.img and not "{image" in i.what:
                    style i.text_img_style
                    imagebutton:
                        focus_mask True
                        idle smallCG(cg_helper(i.what))
                        if not choosing:
                            action [ShowCG(i.what)]

                else:
                    style i.text_bubble_style
                    yalign 0.0
                    if i.dialogue_width > gui.longer_than:
                        text i.text_msg_what:
                            style "bubble_text_long"
                            min_width gui.long_line_min_width
                            color '#fff'
                            font i.text_msg_font
                    else:
                        if not i.img:
                            yoffset 35
                        text i.text_msg_what:
                            style "bubble_text"
                            color '#fff'
                            font i.text_msg_font

            if i != filler and not anti:
                text i.thetime.get_twelve_hour():
                    color '#fff'
                    yalign 1.0
                    size 23
                    if i.img and not "{image" in i.what:
                        xoffset 10





