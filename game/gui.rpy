################################################################################
## Initialization
################################################################################

## The init offset statement causes the initialization statements in this file
## to run before init statements in any other file.
init offset = -20

## Calling gui.init resets the styles to sensible default values, and sets the
## width and height of the game.
init python:

    ## EDITABLE
    # Turn this off if you don't want screen scaling
    allow_ui_scaling = True

    # The width/height of your original game UI
    original_width = 750
    original_height = 1334

    # The original dimensions (ratio) of your original UI
    original_width_ratio = 9
    original_height_ratio = 16

    # Whether the UI can get wider (keeping its original height)
    ui_allow_wider = False
    # Whether the UI can get taller (keeping its original width)
    ui_allow_taller = True
    ## END OF EDITABLE

    # Don't allow regular players to mess with the screen dimensions
    if not config.developer:
        persistent.virt_screen_width = None
        persistent.virt_screen_height = None

    # Are we doing this wider, or taller? e.g. 9/16=0.5625
    original_ratio = float(original_width_ratio) / float(original_height_ratio)

    # Developer options to manually change the dimensions for testing
    if (persistent.virt_screen_height
            and persistent.virt_screen_width
            and (persistent.virt_screen_height != original_height_ratio
                or persistent.virt_screen_width != original_width_ratio)):

        if persistent.virt_screen_width:
            mult0 = float(persistent.virt_screen_width)
        else:
            mult0 = float(original_width_ratio)

        if persistent.virt_screen_height:
            mult1 = float(persistent.virt_screen_height)
        else:
            mult1 = float(original_height_ratio)

        if (mult0 / mult1) < original_ratio:
            # Taller
            gui.init(original_width, int(float(original_width)/mult0*mult1))
        else:
            # Wider
            gui.init(int(float(original_height)/mult1*mult0), original_height)

    elif (persistent.virt_screen_height == original_height_ratio
                and persistent.virt_screen_width == original_width_ratio):
        # Same dimensions as original UI
        gui.init(original_width, original_height)

    elif allow_ui_scaling:
        # Get different screen resolutions

        inf = renpy.display.get_info()
        # actual screen width
        ww = inf.current_w
        # actual screen height
        hh = inf.current_h
        if renpy.android:
            try:
                # Fetch the width/height from Java
                ww = PythonSDLActivity.getScreenWidth()
                ww = max(ww, inf.current_w)
                hh = PythonSDLActivity.getScreenHeight()
                hh = min(hh, inf.current_h)
                # Shave a few pixels off the screen height to account for the top
                # bar and/or navigation bar
                hh -= 120
            except Exception as e:
                # This functionality wasn't implemented for Android
                pass


        # height if it was the original ratio for the game width
        vh = float(ww) / float(original_width_ratio) * float(original_height_ratio)
        # The screen is within the original ratio
        if hh-10 <= vh <= hh+10:
            gui.init(original_width, original_height)
        else:
            # What the height should be instead of the original ratio
            new_h = (float(hh) / float(ww)) * float(original_width)
            new_h = int(new_h)
            # What the width should be instead of the original ratio
            new_w = (float(ww) / float(hh) * float(original_height))
            new_w = int(new_w)
            if new_h < original_height:
                # Wider
                if ui_allow_wider:
                    gui.init(new_w, original_height)
                else:
                    gui.init(original_width, original_height)
            else:
                # Taller
                if ui_allow_taller:
                    gui.init(original_width, new_h)
                else:
                    gui.init(original_width, original_height)
    else:
        gui.init(original_width, original_height)




################################################################################
## GUI Configuration Variables
################################################################################


## Colors ######################################################################
##
## The colors of text in the interface.

## An accent color used throughout the interface to label and highlight text.
define gui.accent_color = '#ffffff'

## The color used for a text button when it is neither selected nor hovered.
define gui.idle_color = '#ababab' #888

## The small color is used for small text, which needs to be brighter/darker to
## achieve the same effect.
define gui.idle_small_color = '#aaaaaa'

## The color that is used for buttons and bars that are hovered.
define gui.hover_color = '#3e8478'

## The color used for a text button when it is selected but not focused. A
## button is selected if it is the current screen or preference value.
define gui.selected_color = '#ffffff'

## The color used for a text button when it cannot be selected.
define gui.insensitive_color = '#8888887f'

## Colors used for the portions of bars that are not filled in. These are not
## used directly, but are used when re-generating bar image files.
define gui.muted_color = '#510028'
define gui.hover_muted_color = '#7a003d'

## The colors used for dialogue and menu choice text.
define gui.text_color = '#000000'
define gui.interface_text_color = '#ffffff'


## Fonts and Font Sizes ########################################################

define gui.curly_font = gui.preference('curly_font', "fonts/Sandoll Misaeng (Curly Font).ttf")
define gui.serif_1 = gui.preference('serif_1', "fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf")
define gui.serif_1b = gui.preference('serif_1b', "fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Bold.ttf")
define gui.serif_1xb = gui.preference('serif_1xb', "fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-ExtraBold.ttf")
define gui.serif_2 = gui.preference('serif_2', "fonts/Seoul Hangang (Serif font 2)/SeoulHangangM.ttf")
define gui.serif_2b = gui.preference('serif_2b', "fonts/Seoul Hangang (Serif font 2)/SeoulHangangB.ttf")
define gui.serif_2xb = gui.preference('serif_2xb', "fonts/Seoul Hangang (Serif font 2)/SeoulHangangEB.ttf")
define gui.sans_serif_1 = gui.preference('sans_serif_1', "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf")
define gui.sans_serif_1b = gui.preference('sans_serif_1b', "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Bold.ttf")
define gui.sans_serif_1xb = gui.preference('sans_serif_1xb', "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-ExtraBold.ttf")
define gui.sans_serif_2 = gui.preference('sans_serif_2', "fonts/SeoulNamsan (Sans Serif Font 2)/SeoulNamsanM.ttf")
define gui.sans_serif_2b = gui.preference('sans_serif_2b', "fonts/SeoulNamsan (Sans Serif Font 2)/SeoulNamsanB.ttf")
define gui.sans_serif_2xb = gui.preference('sans_serif_2xb', "fonts/SeoulNamsan (Sans Serif Font 2)/SeoulNamsanEB.ttf")
define gui.blocky_font = gui.preference('blocky_font', "fonts/BM-HANNA (Bold Font).ttf")
define gui.curlicue_font = gui.preference('curlicue_font', "fonts/NanumBarunpenR.ttf")

init python:
    ## Ensures that when bold is used for the fonts, it uses the bolded font
    ## rather than artificially applying weight.
    config.font_replacement_map[gui.serif_1, True, False] = (gui.serif_1xb, False, False)
    config.font_replacement_map[gui.serif_1, True, True] = (gui.serif_1xb, False, True)
    config.font_replacement_map[gui.serif_2, True, False] = (gui.serif_2xb, False, False)
    config.font_replacement_map[gui.serif_2, True, True] = (gui.serif_2xb, False, True)
    config.font_replacement_map[gui.sans_serif_1, True, False] = (gui.sans_serif_1xb, False, False)
    config.font_replacement_map[gui.sans_serif_1, True, True] = (gui.sans_serif_1xb, False, True)
    config.font_replacement_map[gui.sans_serif_2, True, False] = (gui.sans_serif_2xb, False, False)
    config.font_replacement_map[gui.sans_serif_2, True, True] = (gui.sans_serif_2xb, False, True)

## The font used for in-game text.
define gui.text_font = gui.sans_serif_1

## The font used for out-of-game text.
define gui.interface_text_font = gui.sans_serif_1

## The size of normal dialogue text.
define gui.text_size = 33

## The size of text in the game's user interface.
define gui.interface_text_size = 30

## The size of labels in the game's user interface.
define gui.label_text_size = 30

## Buttons #####################################################################
##
## These variables, along with the image files in gui/button, control aspects of
## how buttons are displayed.

## The width and height of a button, in pixels. If None, Ren'Py computes a size.
define gui.button_width = None
define gui.button_height = None

## The borders on each side of the button, in left, top, right, bottom order.
define gui.button_borders = Borders(4, 4, 4, 4)

## If True, the background image will be tiled. If False, the background image
## will be linearly scaled.
define gui.button_tile = False

## The font used by the button.
define gui.button_text_font = gui.interface_text_font

## The size of the text used by the button.
define gui.button_text_size = gui.interface_text_size

## The color of button text in various states.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## The horizontal alignment of the button text. (0.0 is left, 0.5 is center, 1.0
## is right).
define gui.button_text_xalign = 0.0


## These variables override settings for different kinds of buttons. Please see
## the gui documentation for the kinds of buttons available, and what each is
## used for.
##
## These customizations are used by the default interface:

define gui.radio_button_borders = Borders(40, 4, 4, 4)

define gui.check_button_borders = Borders(50,4,4,4)

define gui.page_button_borders = Borders(9, 4, 9, 4)

define gui.quick_button_borders = Borders(9, 4, 9, 0)
define gui.quick_button_text_size = 12
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## Bars, Scrollbars, and Sliders ###############################################
##
## These control the look and size of bars, scrollbars, and sliders.
##
## The default GUI only uses sliders and vertical scrollbars. All of the other
## bars are only used in creator-written screens.

## True if bar images should be tiled. False if they should be linearly scaled.
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Horizontal borders.
define gui.bar_borders = Borders(4, 4, 4, 4)
define gui.scrollbar_borders = Borders(4, 4, 4, 4)
define gui.slider_borders = Borders(4, 4, 4, 4)

## Vertical borders.
define gui.vbar_borders = Borders(4, 4, 4, 4)
define gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define gui.vslider_borders = Borders(4, 4, 4, 4)

## What to do with unscrollable scrollbars in the gui. "hide" hides them, while
## None shows them.
define gui.unscrollable = "hide"


## Localization ################################################################

## This controls where a line break is permitted. The default is suitable
## for most languages. A list of available values can be found at https://
## www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"


