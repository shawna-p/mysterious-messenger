#************************************
# Heart Icons
#************************************
init python:

    TAG_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    def get_random_screen_tag(k=4, text_msg=False):
        """Generate a random k-letter word out of alphabet letters."""

        while True:
            # Used to retain compatibility between Ren'Py 7.4+ and 8.0+
            if renpy.version_only.startswith("7"):
                # Shuffle the list and pop k items from the front
                alphabet = list(store.TAG_ALPHABET)
                random.shuffle(alphabet)
                tag = ''.join(alphabet[:k])
            else:
                # Sample k letters from the alphabet. Repeats allowed.
                tag = ''.join(random.choices(list(store.TAG_ALPHABET), k=k))

            if text_msg and tag not in store.text_screen_tags:
                break
            elif not text_msg and tag not in store.screen_tags:
                break

        # Add the tag to a set so we can be sure to hide it
        if text_msg:
            store.text_screen_tags.add(tag)
        else:
            store.screen_tags.add(tag)
        return tag

    def heart_icon(character):
        """
        Dynamically recolour the heart icon to the colour associated with
        this character.
        """
        try:
            return Transform("Heart Point/Unknown Heart Point.webp",
                matrixcolor=ColorizeMatrix("#000", character.heart_color))
        except:
            return "Heart Point/Unknown Heart Point.webp"

# A set of tags which have been used for currently showing tags
default screen_tags = set()
default text_screen_tags = set()
default showing_text_screens = dict()

# Display the heart icon on-screen
screen heart_icon_screen(character, hide_screen='heart_icon_screen'):
    zorder 20

    fixed at heart:
        yfit True
        xfit True
        add heart_icon(character)

    timer 0.62 action [Hide(hide_screen)]

# Additional screens for allocation
screen hicon2(character):
    zorder 20
    use heart_icon_screen(character, 'hicon2')

screen hicon3(character):
    zorder 20
    use heart_icon_screen(character, 'hicon3')

# List of the most recently shown heart screens
default recently_shown_heart = [ ]

## This screen is used to display text notifications
## as an alternative to animated icons
screen stackable_notifications(message, hide_screen='stackable_notifications'):
    zorder 100
    button at stack_notify_appear:
        style 'notify_frame'
        xalign 1.0 yalign 0.92
        text "[message!tq]" style 'notify_text'
        action Hide(hide_screen)
    timer 5.25 action Hide(hide_screen)

transform stack_notify_appear:
    yoffset 0
    on show:
        alpha 0 yoffset 30
        linear .25 alpha 1.0 yoffset 0
        linear 5 yoffset -250
    on hide:
        linear .5 alpha 0.0 yoffset -310

image heart_break_anim:
    "Heart Point/heartbreak_0.webp"
    0.12
    "Heart Point/heartbreak_1.webp"
    0.12
    "Heart Point/heartbreak_2.webp"
    0.12
    "Heart Point/heartbreak_3.webp"
    0.12
    "Heart Point/heartbreak_4.webp"
    0.12
    Null()


# Display the heartbreak on-screen
screen heart_break_screen(character, hide_screen='heart_break_screen'):
    zorder 20

    fixed:
        align (0.5, 0.5) xfit True yfit True
        at transform:
            zoom 2.0
        add 'heart_break_anim':
            matrixcolor ColorizeMatrix("#000", character.heart_color)

    timer 0.6 action [Hide(hide_screen)]

image hg_1 = "Heart Point/hourglass_1.webp"
image hg_2 = "Heart Point/hourglass_2.webp"

## Screen that displays the hourglass animation when the player
## receives an hourglass
screen hourglass_animation(hide_screen='hourglass_animation'):

    zorder 20

    add 'hg_1' at hourglass_anim(0.0) align (0.5, 0.5)
    add 'hg_2' at hourglass_anim_2(firstbouncein
            + firstbounceout + secbouncein, 0.7):
        align (0.5, 0.5)

    timer arbitrary_delay+smallzoom+0.3+zoomouttime:
        action Hide(hide_screen)

## Additional screens for allocation
screen hg_icon2():
    zorder 20
    use hourglass_animation('hg_icon2')

screen hg_icon3():
    zorder 20
    use hourglass_animation('hg_icon3')

transform hourglass_anim(delay=0.0):
    zoom 1.0
    parallel:
        # Bounce 1
        easein firstbouncein zoom 2.6
        easeout firstbounceout zoom 1.0
        # Bounce 2
        easein secbouncein zoom 2.1
        easeout smallzoom zoom 1.15
        # Grow larger
        easein bigzoom zoom 5.75
    parallel:
        # And fade out
        linear firstbouncein + firstbounceout + secbouncein + smallzoom
        linear fadeinout alpha 0.0

transform hourglass_anim_2(delay=0.0, proportion=1.0):
    alpha 0.0 zoom proportion*2.1#1.83
    linear delay
    parallel:
        # Image gets smaller
        easeout smallzoom zoom 1.15*proportion#1.0
    parallel:
        # Image becomes visible
        linear arbitrary_delay
        linear 0.3 alpha 1.0
    parallel:
        # Image becomes larger
        easeout smallzoom
        easein bigzoom zoom proportion*5.75#5.0
    parallel:
        # Image becomes transparent
        linear arbitrary_delay+smallzoom
        linear zoomouttime-0.3 alpha 0.0

define firstbouncein = 0.23 # 1.0
define firstbounceout = 0.23 # 0.8
define secbouncein = 0.2 # 0.5
define smallzoom = 0.32 # 0.7
define bigzoom = 1.2 # 2.0
define arbitrary_delay = 0.1 # 0.3
define zoomouttime = 0.8 # 1.6
define fadeinout = 0.6

#####################################
# Chat Speed Modifiers
#####################################

init python:

    def speed_num_fn(st, at):
        """Display the SPEED number in-chat."""

        speednum = "!!"
        # Minimum pv is 0.1, maximum is ~1.4
        # 5 = 0.8
        # So it goes 1.4, 1.25, 1.1, 0.95, 0.8, 0.65, 0.5, 0.35, 0.2
        speednum = str(int((round(9.0 - ((store.persistent.pv - 0.2)
                                                    / 0.15), 1))))

        speedtxt = Text("SPEED", style='speednum_style', size=30)
        numtxt = Text(speednum, style='speednum_style', align=(.5,.5))
        return VBox(speedtxt, numtxt), 0.05

# The number that shows up when adjusting the chatroom speed
style speednum_style is text:
    xalign 0.97
    yalign 0.22
    color "#ffffff"
    font gui.sans_serif_1b
    size 45
    text_align 0.5

image speed_num_img = DynamicDisplayable(speed_num_fn)

screen speed_num():

    zorder 200

    add 'speed_num_img' align(0.98, 0.2)

    timer 0.4 action Hide('speed_num', Dissolve(0.4))

#####################################
# Hack scrolls, banners, enter/exit
#####################################

#************************************
# Hack Scrolls
#************************************
# Displays the scrolled hacking effect

screen hack_screen(hack, flicker_anim=True, bg="black"):
    zorder 10
    modal True
    add bg
    imagebutton:
        if flicker_anim:
            at flicker()
        xysize (config.screen_width, config.screen_height)
        idle hack
        if observing and not _in_replay:
            action Hide('hack_screen')

    timer 3.0 action Hide('hack_screen')

label hack(reverse=False):
    if (not observing and not persistent.testing_mode
            and gamestate == CHAT):
        if reverse:
            $ hack_entry = ("hack", "reverse")
        else:
            $ hack_entry = ("hack", "regular")
        $ current_timeline_item.replay_log.append(hack_entry)
    if persistent.hacking_effects:
        if reverse:
            show screen hack_screen('hack scroll reverse')
        else:
            show screen hack_screen('hack scroll')
        with Pause(3.0)
        hide screen hack_screen
    return

label redhack(reverse=False):
    if (not observing and not persistent.testing_mode
            and gamestate == CHAT):
        if reverse:
            $ hack_entry = ("hack", "red_reverse")
        else:
            $ hack_entry = ("hack", "red")
        $ current_timeline_item.replay_log.append(hack_entry)
    if persistent.hacking_effects:
        if reverse:
            show screen hack_screen('redhack scroll reverse')
        else:
            show screen hack_screen('redhack scroll')
        with Pause(3.0)
        hide screen hack_screen
    return

label red_static(reverse=False):
    if (not observing and not persistent.testing_mode
            and gamestate == CHAT):
        if reverse:
            $ hack_entry = ("hack", "red_static_reverse")
        else:
            $ hack_entry = ("hack", "red_static")
        $ current_timeline_item.replay_log.append(hack_entry)
    if persistent.hacking_effects:
        if reverse:
            show screen hack_screen("red_static_reverse", False,
            'red_static_background')
        else:
            show screen hack_screen('red_static_scroll', False,
                'red_static_background')
        with Pause(3.0)
        hide screen hack_screen
    return

# Shows the "cracked" phone screen overlay
label screen_crack_overlay():
    if (not observing and not persistent.testing_mode
            and gamestate == CHAT):
        $ entry = ("overlay", "screen_crack")
        $ current_timeline_item.replay_log.append(entry)
    $ renpy.show_screen('screen_crack_overlay_bg')
    return

screen screen_crack_overlay_bg():
    zorder 0
    add 'screen_crack'

#************************************
# Banners
#************************************

# These are the special "banners" that crawl across the screen
# Call them using "call banner('well')" etc

label banner(banner):
    if (not observing and not persistent.testing_mode and gamestate == CHAT):
        $ banner_entry = ("banner", banner)
        $ current_timeline_item.replay_log.append(banner_entry)
    if persistent.banners:
        hide screen banner_screen
        show screen banner_screen(banner)
    return

screen banner_screen(banner):
    zorder 10
    fixed:
        xysize (config.screen_width, 230)
        align (.5, .5)
        add 'banner ' + banner align (0.5, 1.0)

    timer 0.72 action Hide('banner_screen')

#************************************
# Other
#************************************

# The "secure chat" animation
label secure_anim():
    if (not observing and not persistent.testing_mode):
        $ entry = ("anim", "secure_anim")
        $ current_timeline_item.replay_log.append(entry)
    show screen secure_anim_screen()
    with Pause(1.25)
    hide screen secure_anim_screen
    return

screen secure_anim_screen():
    zorder 10
    modal True
    add 'black'
    imagebutton:
        align (0.5, 0.5)
        idle 'secure_chat_intro'
        if observing and not _in_replay:
            action Hide('secure_anim_screen')

    timer 1.25 action Hide('secure_anim_screen')