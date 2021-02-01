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

        return im.MatrixColor('VN Mode/Chat Bubbles/white_vn.webp',
            im.matrix.colorize('#000', c))

    # Essentially copied from renpy.store.adv; a default ADV character
    # to work with the new MyADVCharacter class.
    my_adv = MyADVCharacter(None,
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

    hbox:
        add my_menu_clock xalign 0.0 yalign 0.0 xpos 5


################################################
## This is the custom history screen
## for VN Mode
## https://www.renpy.org/doc/html/history.html
################################################

screen history():

    tag menu

    # Avoid predicting this screen, as it can be very large.
    predict False

    # Allow the user to darken the VN window for better contrast
    add Transform('#000', alpha=max(((persistent.vn_window_dark
                        + persistent.vn_window_alpha) / 2.0), 0.7))

    # Close button
    button:
        xalign 1.0
        yalign 0.0
        focus_mask True
        add "close_button"
        action Hide('history')#Return()
        text "Close" style "CG_close":
            if persistent.dialogue_outlines:
                outlines [ (2, "#000",
                            absolute(0), absolute(0)) ]
                font gui.sans_serif_1xb


    viewport:
        yinitial 1.0
        scrollbars "vertical"
        mousewheel True
        draggable True
        side_yfill True

        ysize 1235
        yalign 1.0

        vbox:
            style_prefix "history"
            spacing 20
            null height 5
            for h in _history_list:

                fixed:
                    yfit True

                    if h.who:

                        label h.who + ':':
                            style "history_name"
                            if persistent.dialogue_outlines:
                                text_outlines [ (absolute(2), "#000",
                                            absolute(0), absolute(0)) ]
                                text_font gui.sans_serif_1xb

                            # Take the color of the who text from the
                            # Character, if set.
                            if "color" in h.who_args:
                                text_color h.who_args["color"]

                    $ what = renpy.filter_text_tags(h.what,
                                    allow=gui.history_allow_tags)
                    text what:
                        if persistent.dialogue_outlines:
                            outlines [ (absolute(2), "#000", 0, 0) ]

            if not _history_list:
                label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.
define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5
