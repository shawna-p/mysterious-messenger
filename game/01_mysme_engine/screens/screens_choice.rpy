## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

init python:
    def say_choice_caption(dialogue, paraphrased, p=0):
        """
        Have the main character say the caption that was given
        to the most recently chosen choice.
        """

        if paraphrased:
            store.dialogue_picked = ""
            store.dialogue_paraphrase = store.paraphrase_choices
            store.dialogue_pv = 0
            return

        # Temporarily ditch image attributes
        temp_side_attr = renpy.store._side_image_attributes
        temp_temp_attr = renpy.game.context().temporary_attributes
        temp_attr = renpy.game.context().say_attributes

        renpy.store._side_image_attributes = None
        renpy.game.context().say_attributes = None
        renpy.game.context().temporary_attributes = None

        store.main_character(dialogue, pauseVal=p, from_paraphrase=True)

        # Restore the image attributes
        renpy.store._side_image_attributes = temp_side_attr
        renpy.game.context().say_attributes = temp_attr
        renpy.game.context().temporary_attributes = temp_temp_attr

        store.dialogue_picked = ""
        store.dialogue_paraphrase = store.paraphrase_choices
        store.dialogue_pv = 0
        return

    def set_paraphrase(screen_pref, item_pref, save_choices=False):
        """Determine whether this choice caption was paraphrased or not."""

        # First, this item gets saved to the timelineitem's choices,
        # if applicable
        if save_choices and (gamestate != PHONE
                or isinstance(store.current_call, TimelineItem)):
            store.current_timeline_item.add_to_choices(store.dialogue_picked)
        elif save_choices and gamestate == PHONE:
            # This is a regular phone call
            store.current_call.add_to_choices(store.dialogue_picked)

        if item_pref is not None:
            # The item set its own preference
            store.dialogue_paraphrase = item_pref
        elif screen_pref is not None:
            # Otherwise, use the screen's preference
            store.dialogue_paraphrase = screen_pref
        else:
            # All else fails, use the default preference
            store.dialogue_paraphrase = store.paraphrase_choices

        # Now do some calculations to see if it's possible to manually
        # determine what store.paraphrase_choices should be.
        if store.paraphrase_choices is None:
            # If the menu set a preference, global is probably the opposite
            # of the menu
            if screen_pref is not None:
                store.paraphrase_choices = not screen_pref
            # Otherwise if the item set a preference, global is probably
            # the opposite of the choice
            elif item_pref is not None:
                store.paraphrase_choices = not item_pref

        return

    def menu_args_callback(*args, **kwargs):

        # Check if we're in a chatroom
        if gamestate == CHAT and not store.answer_shown:
            kwargs['screen'] = "answer_choice"
        if (store.text_person and store.text_person.real_time_text
                and not (gamestate in (PHONE, VNMODE)
                    or store.email_reply or store.answer_shown)):
            kwargs['screen'] = 'answer_choice_text'
        store.answer_shown = True
        store.pre_choosing = True
        # Some code that might be used if I figure out how to get
        # rid of the `extend ''` stuff.
        # Check if it's a phone call or Story Mode
        # if (not (store.text_msg_reply
        #             or store.email_reply)
        #         and (store.in_phone_call
        #             or store.vn_choice)):
        #     renpy.ast.statement_name("menu-with-caption")
        #     # Get the dialogue
        #     # what = store._last_say_what
        #     # who = store._last_say_who
        #     #_window_show = True
        #     #extend('', interact=False)
        #     #_window_auto = True
        #     who = store._last_say_who
        #     who = renpy.eval_who(who)
        #     if who is None:
        #         who = narrator
        #     elif isinstance(who, basestring):
        #         who = Character(who, kind=name_only)
        #     who(store._last_say_what + "{fast}", interact=False)
        #     store._history_list.pop()

        return args, kwargs

    # This lets the program shuffle menu options
    renpy_menu = menu
    def menu(items):
        # Copy the items list
        items = list(items)
        global shuffle
        if shuffle and shuffle not in ["last", "default"]:
            renpy.random.shuffle(items)
        elif shuffle == "last":
            last = items.pop()
            renpy.random.shuffle(items)
            items.append(last)
        elif shuffle == "default":
            # Don't shuffle or modify these answers
            shuffle = True
            return renpy_menu(items)
        shuffle = True

        # If observing, check which items have already been seen
        new_items = []
        if store.observing and not store._in_replay and store.current_choices:
            # Restrict choices to what's been selected this playthrough
            the_choice = store.current_choices.pop(0)
            new_items = [ i for i in items if i[0] == the_choice ]
        if store.observing and not new_items:
            new_items = [ i for i in items if i[1].get_chosen() ]
        if new_items:
            items = new_items
        return renpy_menu(items)

default answer_shown = False
define config.menu_arguments_callback = menu_args_callback

default dialogue_picked = ""
default dialogue_paraphrase = True
default dialogue_pv = 0

## These two screens will automatically show the answer button before
## showing the choice screen
screen answer_choice(items, paraphrased=None):
    zorder 5

    use answer_button([Hide('answer_choice'), Show('pause_button'),
        ShowTransient('choice', items=items, paraphrased=paraphrased)])

screen answer_choice_text(items, paraphrased=None):
    zorder 5

    use text_answer([Hide('answer_choice_text'), Show('text_pause_button'),
        ShowTransient('choice', items=items, paraphrased=paraphrased)])

init python:
    def choice_action(i, paraphrased):
        """
        Return the action for this choice based on the current state of
        the game and various variables.
        """

        usual_action = [
            SetVariable('dialogue_picked', i.caption),
            Function(set_paraphrase,
                screen_pref=paraphrased,
                item_pref=i.kwargs.get('paraphrased', None),
                save_choices=gamestate in (PHONE, VNMODE)),
            i.action
        ]

        if gamestate == TEXTMSG:
            usual_action.insert(0,
                If(not text_person or not text_person.real_time_text,
                    Show('text_message_screen', sender=text_person)))
            return usual_action

        elif gamestate in (PHONE, VNMODE):
            return usual_action

        elif email_reply:
            return i.action

        else:
            if using_timed_menus:
                ret = [SetVariable('reply_instant', True),
                    SetVariable('using_timed_menus', False),
                    Hide('answer_countdown'),
                    # This ensures the messenger scrolls
                    # to the bottom
                    Hide('messenger_screen'),
                    Show('messenger_screen')]
                ret.extend(usual_action)
                return ret
            else:
                return usual_action


screen choice(items, paraphrased=None):
    zorder 150
    modal True

    default the_anim = choice_anim if persistent.custom_footers and not renpy.is_skipping() else null_anim
    default outline_color = "#0000" if not persistent.dialogue_outlines else "#fff" if (gamestate == CHAT and not persistent.custom_footers) else "#000"

    add "choice_darken"

    # For text messages
    if gamestate == TEXTMSG:
        if not text_person or not text_person.real_time_text:
            use text_message_screen(text_person)
            add "choice_darken"
        vbox:
            style_prefix 'text_msg_choice'
            for num, i in enumerate(items):
                textbutton i.caption at the_anim(float(num*0.2)):
                    text_outlines [(2, outline_color)]
                    if (persistent.past_choices and i.chosen):
                        foreground 'seen_choice_check'
                    action choice_action(i, paraphrased)

    # For Story Mode and phone calls
    elif gamestate in (PHONE, VNMODE):
        vbox:
            style_prefix 'phone_vn_choice'
            for num, i in enumerate(items):
                textbutton i.caption at the_anim(float(num*0.2)):
                    text_outlines [(2, outline_color)]
                    if (persistent.past_choices and not observing
                            and i.chosen):
                        foreground 'seen_choice_check_circle'
                        background 'call_choice_check'
                        hover_background 'call_choice_check_hover'
                    action choice_action(i, paraphrased)

    # For emails
    elif email_reply:
        use email_hub
        use open_email(current_email)
        add "choice_darken"
        vbox:
            style_prefix 'email_choice'
            for num, i in enumerate(items):
                textbutton i.caption at the_anim(float(num*0.2)):
                    action choice_action(i, paraphrased)

    # For everything else (e.g. chatrooms)
    else:
        vbox:
            if persistent.custom_footers:
                style_prefix 'phone_vn_choice'
            else:
                style_prefix 'choice'
            for num, i in enumerate(items):
                button at the_anim(float(num*0.2)):
                    if (persistent.past_choices and not observing
                            and i.chosen):
                        if persistent.custom_footers:
                            foreground 'seen_choice_check_circle'
                            background 'call_choice_check'
                            hover_background 'call_choice_check_hover'
                        else:
                            foreground 'seen_choice_check'

                    text i.caption:
                        if persistent.custom_footers:
                            style 'phone_vn_choice_button_text'
                        else:
                            style 'choice_button_text'
                        outlines [(2, outline_color)]
                    action choice_action(i, paraphrased)

image phone_icon_bg = Fixed(
    'call_choice_check',
    Transform('Phone Calls/call_button_answer.webp', align=(0.0, 0.5)),
    fit_first=True,
)
image seen_choice_check = Image('Menu Screens/Main Menu/main02_tick.webp',
                            align=(0.99, 0.97))
image seen_choice_check_circle = Image('Menu Screens/Main Menu/main02_tick_2.webp',
                            align=(0.985, 0.955))

## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True

## Choice Buttons ##############################################################
##
## Choice buttons are used in the in-game menus.

style choice_vbox:
    xalign 0.5
    yalign 0.5
    spacing 5

style choice_button is default:
    background Frame("gui/button/choice[_prefix]_background.png", 40, 30, 40, 30)
    xsize 740 ysize 221
    padding (40, 30)
    activate_sound "audio/sfx/UI/answer_select.mp3"

style choice_button_text is default:
    idle_color "#000"
    hover_color "#000"
    font gui.serif_1
    text_align 0.0 xalign 0.0
    size gui.text_size

style text_msg_choice_vbox:
    is choice_vbox

style text_msg_choice_button:
    is choice_button
    background 'text_answer_idle'
    hover_background 'text_answer_hover'

style text_msg_choice_button_text:
    is choice_button_text
    idle_color '#fff'
    hover_color '#fff'

style phone_vn_choice_vbox:
    is choice_vbox
    spacing 20

style phone_vn_choice_button:
    is choice_button
    xysize (740, 180)
    background 'call_choice'
    hover_background 'call_choice_hover'
    padding(45,45)
    align (0.5, 0.5)

style phone_vn_choice_button_text:
    is choice_button_text
    align (0.5, 0.5)
    idle_color '#f9f9f9'
    hover_color '#fff'
    text_align 0.5

style email_choice_vbox:
    is choice_vbox

style email_choice_button:
    is choice_button
    background 'text_answer_idle'
    hover_background 'text_answer_hover'

style email_choice_button_text:
    is choice_button_text
    idle_color '#fff'
    hover_color '#fff'
    xalign 0.5
    yalign 0.5
    text_align 0.5

