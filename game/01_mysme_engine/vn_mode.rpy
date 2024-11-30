#************************************
# Visual Novel Mode
#************************************

init -10 python:

    class MyADVCharacter(renpy.character.ADVCharacter):
        """
        A class which inherits from the default Ren'Py implementation
        of an ADV character in order to get first pass at its functions.
        """

        def __call__(self, what, interact=True, _call_done=True,
                multiple=None, from_paraphrase=None, **kwargs):
            """
            Overrides the default implementation of an ADV character's
            __call__ function in order to work with paraphrasing.
            """

            if (self != store.main_character.vn_char
                    and not store.dialogue_paraphrase
                    and store.dialogue_picked != ""
                    and not from_paraphrase):

                say_choice_caption(store.dialogue_picked,
                    store.dialogue_paraphrase, store.dialogue_pv)

            if (self.screen != 'phone_say'
                    and self.window_args.get('color', None)):
                # Colorize the window background
                wbg = colorize_vn_window(self.window_args.get('color', "#fff"))
                self.window_args['background'] = Transform(wbg,
                    alpha=store.persistent.vn_window_alpha)
            elif (self.screen != 'phone_say'
                    and self.window_args.get('background', None)):
                wbg = self.window_args['background']
                if isinstance(wbg, renpy.display.transform.Transform):
                    wbg = wbg.child
                self.window_args['background'] = Transform(wbg,
                    alpha=store.persistent.vn_window_alpha)

            return super(MyADVCharacter, self).__call__(what, interact,
                _call_done, multiple, **kwargs)

    def colorize_vn_window(c):
        """Colorizes the generic VN window background with colour c."""

        return Transform('VN Mode/Chat Bubbles/white_vn.webp',
            matrixcolor=ColorizeMatrix('#000', c))

    # Essentially copied from renpy.store.adv; a default ADV character
    # to work with the new MyADVCharacter class.
    my_adv = MyADVCharacter(
                None,
                who_prefix='',
                who_suffix='',
                what_prefix='',
                what_suffix='',

                show_function=renpy.show_display_say,
                predict_function=renpy.predict_show_display_say,

                condition=None,
                dynamic=False,
                image=None,

                interact=True,
                slow=True,
                slow_abortable=True,
                afm=True,
                ctc=None,
                ctc_pause=None,
                ctc_timedpause=None,
                ctc_position="nestled",
                all_at_once=False,
                with_none=None,
                callback=None,
                type='say',
                advance=True,
                retain=False,

                who_style='say_label',
                what_style='say_dialogue',
                window_style='say_window',
                screen='say',
                mode='say',
                voice_tag=None,

                kind=False)

    def Character(name=renpy.character.NotSet, kind=None, **properties):
        """
        This overwrites the default Character definition in order to
        intercept its arguments to function with the paraphrase system.
        """

        if kind is None:
            kind = my_adv

        if kind == renpy.store.adv:
            kind = my_adv

        return type(kind)(name, kind=kind, **properties)


#####################################
## VN Setup
#####################################

## Call to begin a VN section. Largely unnecessary except during the intro.
label vn_begin(nvl=False):
    $ begin_timeline_item(generic_storymode, is_vn=nvl)
    return

## Call to end a VN section. Largely unnecessary except during the intro.
label vn_end():
    if starter_story and not renpy.get_return_stack():
        jump end_prologue
    return

# Lets the program know it's in Story Mode
default vn_choice = False

#####################################
## This screen shows the clock
#####################################

screen vn_overlay():

    add my_menu_clock xanchor 0.0 yanchor 0.0 xpos 5


################################################
## This is the custom history screen for VN Mode
## https://www.renpy.org/doc/html/history.html
################################################

## History #####################################################################
##
## The history screen displays dialogue that the player has already dismissed.

screen history():

    tag menu

    # Avoid predicting this screen, as it can be very large.
    predict False

    # Allow the user to darken the VN window for better contrast
    add Transform('#000', alpha=max(((persistent.vn_window_dark
                        + persistent.vn_window_alpha) / 2.0), 0.7))

    # Close button
    button:
        style_prefix 'history_close'
        action Hide('history')
        keysym ["rollback", "game_menu"]
        text "Close" style "CG_close_button_text":
            if persistent.dialogue_outlines:
                outlines [ (2, "#000") ]
                font gui.sans_serif_1xb

    viewport:
        yinitial 1.0
        scrollbars "vertical"
        mousewheel True
        draggable True
        side_yfill True
        style_prefix "history"

        vbox:
            null height 5
            for h in _history_list:

                fixed:
                    yfit True

                    if h.who:

                        label h.who + ':':
                            style "history_name"
                            if persistent.dialogue_outlines:
                                text_outlines [ (2, "#000") ]
                                text_font gui.sans_serif_1xb

                            # Take the color of the who text from the
                            # Character, if set.
                            if "color" in h.who_args:
                                text_color h.who_args["color"]

                    $ what = renpy.filter_text_tags(h.what,
                                    allow=gui.history_allow_tags)
                    text what:
                        if persistent.dialogue_outlines:
                            outlines [ (2, "#000") ]

            if not _history_list:
                label _("The dialogue history is empty."):
                    if persistent.dialogue_outlines:
                        text_outlines [ (2, "#000") ]
            null height 10


## This determines what tags are allowed to be displayed on the history screen.
define gui.history_allow_tags = set(['b', 'i', 'u', 's', 'font', 'color', 'size'])

## The number of blocks of dialogue history Ren'Py will keep.
define config.history_length = 250

style history_viewport:
    ysize config.screen_height-100
    yalign 1.0

style history_vbox:
    spacing 20

## The position, width, and alignment of the label giving the name of the
## speaking character.
style history_name:
    is gui_label
    xpos 160
    xanchor 1.0
    ypos 0
    xsize 165

style history_name_text:
    is gui_label_text
    min_width 165
    text_align 1.0

## The position, width, and alignment of the dialogue text.
style history_text:
    is gui_text
    xpos 170
    ypos 2
    xanchor 0.0
    xsize 560
    min_width 560
    text_align 0.0
    layout "tex"

## Used for the "dialogue history is empty" message
style history_label:
    is gui_label
    xfill True

style history_label_text:
    is gui_label_text
    xalign 0.5

style history_close_button:
    background "#00000066"
    xalign 0.5 yalign 0.0
    xysize (config.screen_width, 99)
style history_close_text:
    is CG_close_button_text
    yalign 0.5 xpos 20
