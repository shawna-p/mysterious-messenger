################################################################################
## Initialization
################################################################################

## The init offset statement causes the initialization statements in this file
## to run before init statements in any other file.
init offset = -2

## Calling gui.init resets the styles to sensible default values, and sets the
## width and height of the game.
init python:
    gui.init(750, 1334)



################################################################################
## GUI Configuration Variables
################################################################################


## Colors ######################################################################
##
## The colors of text in the interface.

## An accent color used throughout the interface to label and highlight text.
define gui.accent_color = '#ffffff' # a purplish colour '#cc0066'

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

## The font used for in-game text.
define gui.text_font = "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"

## The font used for character names.
define gui.name_text_font = "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"

## The font used for out-of-game text.
define gui.interface_text_font = "DejaVuSans.ttf"

## The size of normal dialogue text.
define gui.text_size = 33

## The size of character names.
define gui.name_text_size = 28

## The size of text in the game's user interface.
define gui.interface_text_size = 30

## The size of labels in the game's user interface.
define gui.label_text_size = 30

## The size of text on the notify screen.
define gui.notify_text_size = 25

## The size of the game's title.
define gui.title_text_size = 60



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

## Main and Game Menus #########################################################

## The images used for the main and game menus.
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## Dialogue ####################################################################
##
## These variables control how dialogue is displayed on the screen one line at a
## time.

## The height of the textbox containing dialogue.
define gui.textbox_height = 320

## The placement of the textbox vertically on the screen. 0.0 is the top, 0.5 is
## center, and 1.0 is the bottom.
define gui.textbox_yalign = 0.94


## The placement of the speaking character's name, relative to the textbox.
## These can be a whole number of pixels from the left or top, or 0.5 to center.
define gui.name_xpos = 130
define gui.name_ypos = 6

## The horizontal alignment of the character's name. This can be 0.0 for left-
## aligned, 0.5 for centered, and 1.0 for right-aligned.
define gui.name_xalign = 0.5

## The width, height, and borders of the box containing the character's name, or
## None to automatically size it.
define gui.namebox_width = None
define gui.namebox_height = None

## The borders of the box containing the character's name, in left, top, right,
## bottom order.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## If True, the background of the namebox will be tiled, if False, the
## background of the namebox will be scaled.
define gui.namebox_tile = False


## The placement of dialogue relative to the textbox. These can be a whole
## number of pixels relative to the left or top side of the textbox, or 0.5 to
## center.
define gui.dialogue_xpos = 20
define gui.dialogue_ypos = 75

## The maximum width of dialogue text, in pixels.
define gui.dialogue_width = 700

## The horizontal alignment of the dialogue text. This can be 0.0 for left-
## aligned, 0.5 for centered, and 1.0 for right-aligned.
define gui.dialogue_text_xalign = 0.0


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

define gui.check_button_borders = Borders(50,4,4,4)#(16, 4, 4, 4)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(9, 4, 9, 4)

define gui.quick_button_borders = Borders(9, 4, 9, 0)
define gui.quick_button_text_size = 12
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## You can also add your own customizations, by adding properly-named variables.
## For example, you can uncomment the following line to set the width of a
## navigation button.

# define gui.navigation_button_width = 250


## Choice Buttons ##############################################################
##
## Choice buttons are used in the in-game menus.

define gui.choice_button_width = 740
define gui.choice_button_height = 221
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(40, 30, 40, 30)
define gui.choice_button_text_font = "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.0
define gui.choice_button_text_idle_color = "#000000"
define gui.choice_button_text_hover_color = "#000000"


## File Slot Buttons ###########################################################
##
## A file slot button is a special kind of button. It contains a thumbnail
## image, and text describing the contents of the save slot. A save slot uses
## image files in gui/button, like the other kinds of buttons.

## The save slot button.
define gui.slot_button_width = 715
define gui.slot_button_height = 142
define gui.slot_button_borders = Borders(15,10,15,10)
define gui.slot_button_text_size = 12
define gui.slot_button_text_xalign = 0.0
define gui.slot_button_text_idle_color = gui.idle_small_color

## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 122
define config.thumbnail_height = 122

## The number of columns and rows in the grid of save slots.
define gui.file_slot_cols = 1
define gui.file_slot_rows = 50


## Positioning and Spacing #####################################################
##
## These variables control the positioning and spacing of various user interface
## elements.

## The position of the left side of the navigation buttons, relative to the left
## side of the screen.
define gui.navigation_xpos = 34

## The vertical position of the skip indicator.
define gui.skip_ypos = 9

## The vertical position of the notify screen.
define gui.notify_ypos = 38

## The spacing between menu choices.
define gui.choice_spacing = 5

## Buttons in the navigation section of the main and game menus.
define gui.navigation_spacing = 4

## Controls the amount of spacing between preferences.
define gui.pref_spacing = 9

## Controls the amount of spacing between preference buttons.
define gui.pref_button_spacing = 0

## The spacing between file page buttons.
define gui.page_spacing = 0

## The spacing between file slots.
define gui.slot_spacing = 5

## The position of the main menu text.
define gui.main_menu_text_xalign = 1.0


## Frames ######################################################################
##
## These variables control the look of frames that can contain user interface
## components when an overlay or window is not present.

## Generic frames.
define gui.frame_borders = Borders(4, 4, 4, 4)

## The frame that is used as part of the confirm screen.
define gui.confirm_frame_borders = Borders(34, 34, 34, 34)

## The frame that is used as part of the skip screen.
define gui.skip_frame_borders = Borders(14, 5, 43, 5)

## The frame that is used as part of the notify screen.
define gui.notify_frame_borders = Borders(14, 5, 34, 5)

## Should frame backgrounds be tiled?
define gui.frame_tile = False


## Bars, Scrollbars, and Sliders ###############################################
##
## These control the look and size of bars, scrollbars, and sliders.
##
## The default GUI only uses sliders and vertical scrollbars. All of the other
## bars are only used in creator-written screens.

## The height of horizontal bars, scrollbars, and sliders. The width of vertical
## bars, scrollbars, and sliders.
define gui.bar_size = 22
define gui.scrollbar_size = 11
define gui.slider_size = 22

## True if bar images should be tiled. False if they should be linearly scaled.
define gui.bar_tile = False
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


## History #####################################################################
##
## The history screen displays dialogue that the player has already dismissed.

## The number of blocks of dialogue history Ren'Py will keep.
define config.history_length = 250

## The height of a history screen entry, or None to make the height variable at
## the cost of performance.
define gui.history_height = 119

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.history_name_xpos = 160
define gui.history_name_ypos = 0
define gui.history_name_width = 165
define gui.history_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.history_text_xpos = 170
define gui.history_text_ypos = 2
define gui.history_text_width = 560
define gui.history_text_xalign = 0.0


## NVL-Mode ####################################################################
##
## The NVL-mode screen displays the dialogue spoken by NVL-mode characters.

## The borders of the background of the NVL-mode background window.
define gui.nvl_borders = Borders(0, 20, 0, 20)

## The maximum number of NVL-mode entries Ren'Py will display. When more entries
## than this are to be show, the oldest entry will be removed.
define gui.nvl_list_length = 20

## The height of an NVL-mode entry. Set this to None to have the entries
## dynamically adjust height.
define gui.nvl_height = None

## The spacing between NVL-mode entries when gui.nvl_height is None, and between
## NVL-mode entries and an NVL-mode menu.
define gui.nvl_spacing = 20

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.nvl_name_xpos = 70
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 127
define gui.nvl_name_xalign = 0.5

#define gui.nvl_name_xpos = 700
#define gui.nvl_name_ypos = -10
#define gui.nvl_name_width = 127
#define gui.nvl_name_xalign = 0.5


## The position, width, and alignment of the dialogue text.
define gui.nvl_text_xpos = 130
define gui.nvl_text_ypos = 7
define gui.nvl_text_width = 500
define gui.nvl_text_xalign = 0.0


## The position, width, and alignment of nvl_thought text (the text said by the
## nvl_narrator character.)
#define gui.nvl_thought_xpos = 203
#define gui.nvl_thought_ypos = 0
#define gui.nvl_thought_width = 500
#define gui.nvl_thought_xalign = 0.0

define gui.nvl_thought_xpos = 550
define gui.nvl_thought_ypos = 7
define gui.nvl_thought_width = 750
define gui.nvl_thought_xalign = 0.5

## The position of nvl menu_buttons.
define gui.nvl_button_xpos = 380
define gui.nvl_button_xalign = 0.0
define gui.nvl_button_ypos = 200


## Chat Spacing ###############################################################
##
## Controls the spacing and look of dialogue said by characters in the messenger

## The borders of the background of the phone background window.
## This window is currently set to be transparent
define gui.phone_borders = Borders(0, 0, 0, 0)

## The height of an chat entry. Set this to None to have the entries
## dynamically adjust height.
define gui.phone_height = None

## The spacing between chat entries when gui.phone_height is None
define gui.phone_spacing = 0

## These are additional modifiers for the text specifically,
## separate from the speech bubbles each character has
define gui.phone_text_line_spacing = 10
define gui.phone_text_xalign = 0.0
define gui.phone_text_ypos2 = 6

## Some extra variables
define gui.phone_text_xsize_long = 377
define gui.long_line_min_width = 377
define gui.longer_than = 420

###############################################################################
##
## All the Special Bubble stats
##
###############################################################################

## SPIKE
## Small Spike Bubble
define gui.spike_s_padding = (45, 50, 95, 50)
define gui.spike_s_offset = (140, 38)

## Small Spike Bubble v2
define gui.spike_s2_padding = (25, 20, 25, 15)
define gui.spike_s2_offset = (170, 38)

## Medium Spike Bubble
define gui.spike_m_padding = (50, 50, 50, 50)
define gui.spike_m_offset = (130, 38)

## Large Spike Bubble
define gui.spike_l_padding = (40, 60, 60, 65)
define gui.spike_l_offset = (140, 25)

## CLOUD
## Small Cloud Bubble
define gui.cloud_s_padding = (30, 20, 30, 20)
define gui.cloud_s_offset = (145, 32)

## Medium Cloud Bubble
define gui.cloud_m_padding = (45, 40, 45, 40)
define gui.cloud_m_offset = (135, 25)

## Large Cloud Bubble
define gui.cloud_l_padding = (65, 40, 70, 80)
define gui.cloud_l_offset = (115, 20)

## Large Cloud Bubble v2
define gui.cloud_l2_padding = (115, 50, 70, 40)
define gui.cloud_l2_offset = (90, 20)

## SPECIAL 1 (Round)
## Small Special 1 Bubble
define gui.round_s_padding = (40, 30, 40, 20)
define gui.round_s_offset = (140, 32)

## Medium Special 1 Bubble
define gui.round_m_padding = (55, 50, 55, 50)
define gui.round_m_offset = (130,25)

## Large Special 1 Bubble
define gui.round_l_padding = (70, 50, 70, 50)
define gui.round_l_offset = (110,0)

## SPECIAL 2 (Square)
## Small Special 2 Bubble
define gui.square_s_padding = (40, 30, 50, 25)
define gui.square_s_offset = (135, 27)

## Medium Special 2 Bubble
define gui.square_m_padding = (50, 50, 65, 35)
define gui.square_m_offset = (135, 35)

## Large Special 2 Bubble
define gui.square_l_padding = (80, 60, 90, 50)
define gui.square_l_offset = (120,35)

## SPECIAL 3 (Flower)
## Small Special 3 Bubble
define gui.flower_s_padding = (35, 50, 40, 20)
define gui.flower_s_offset = (130, 17)

## Medium Special 3 Bubble
define gui.flower_m_padding = (45, 80, 60, 35)
define gui.flower_m_offset = (120,25)

## Large Special 3 Bubble
define gui.flower_l_padding = (55, 90, 65, 50)
define gui.flower_l_offset = (110,0)

## SIGH
## Small Sigh Bubble
define gui.sigh_s_padding = (20, 30, 25, 50)
define gui.sigh_s_offset = (140, 38)

## Medium Sigh Bubble 
define gui.sigh_m_padding = (30, 40, 40, 80)
define gui.sigh_m_offset = (130, 38)

## Large Sigh Bubble
define gui.sigh_l_padding = (45, 60, 45, 110)
define gui.sigh_l_offset = (125, 38)


## Localization ################################################################

## This controls where a line break is permitted. The default is suitable
## for most languages. A list of available values can be found at https://
## www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"


################################################################################
## Mobile devices
################################################################################

init python:

    ## This increases the size of the quick buttons to make them easier to touch
    ## on tablets and phones.
    if renpy.variant("touch"):

        gui.quick_button_borders = Borders(34, 12, 34, 0)

    ## This changes the size and spacing of various GUI elements to ensure they
    ## are easily visible on phones.
    if renpy.variant("small"):

        ## Font sizes.
        #gui.text_size = 26
        #gui.name_text_size = 31
        #gui.notify_text_size = 22
        #gui.interface_text_size = 26
        #gui.button_text_size = 26
        #gui.label_text_size = 29

        ## Adjust the location of the textbox.
        #gui.textbox_height = 203
        #gui.name_xpos = 68
        #gui.text_xpos = 76
        #gui.text_width = 929

        ## Change the size and spacing of various things.
        #gui.slider_size = 31

        #gui.choice_button_width = 1047

        #gui.navigation_spacing = 17
        #gui.pref_button_spacing = 9

        gui.history_height = 161
        gui.history_text_width = 583

        gui.quick_button_text_size = 17

        ## File button layout.
        #gui.file_slot_cols = 2
        #gui.file_slot_rows = 2

        ## NVL-mode.
        #gui.nvl_height = 144

        #gui.nvl_name_width = 258
        #gui.nvl_name_xpos = 275

        #gui.nvl_text_width = 773
        #gui.nvl_text_xpos = 292
        #gui.nvl_text_ypos = 5

        #gui.nvl_thought_width = 1047
        #gui.nvl_thought_xpos = 17

        #gui.nvl_button_width = 1047
        #gui.nvl_button_xpos = 17



