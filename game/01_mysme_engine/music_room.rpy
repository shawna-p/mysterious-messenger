init 3 python:

    mm_mr = ExtendedMusicRoom(channel='music', fadeout=0.0, fadein=0.0,
        loop=True, single_track=False, shuffle=False, stop_action=None,
        alphabetical=True)

    # mm_mr.default_art = "gui/music_room/cover_art.webp"
    for key in music_dictionary.keys():
        import re as regex
        pattern = regex.compile("audio\/music\/\d?\d? ?(.*)\.\w+")
        match = pattern.match(key)
        if match:
            mr_name = match.group(1)
        else:
            mr_name = key
        if mr_name == "Mystic_Messenger_Opening_Instrumental_Version":
            mr_name = "Mystic Messenger Opening (Instrumental Ver.)"
        elif mr_name == "Geniusly Hacked Bedop":
            mr_name = "Geniusly Hacked Bebop"
        mm_mr.add(
            name=mr_name,
            path=key,
            artist="Flaming Heart",
        )

define myconfig.UNLOCK_TRACKS_FOR_DEVELOPMENT = True

################################################################################
## IMAGES & DEFINITIONS
################################################################################
## These colours are used by the colorize_button transform in the screens below
## to colorize the default music controls. You can change these if you want to
## use the provided images, or simply supply your own and remove the lines
## `at colorize_button` from the screen below.
define MUSIC_ROOM_IDLE_COLOR = "#fff"
define MUSIC_ROOM_HOVER_COLOR = "#b3f3ee"
define MUSIC_ROOM_SELECTED_IDLE_COLOR = "#fff"
define MUSIC_ROOM_SELECTED_HOVER_COLOR = "#b3f3ee"
define MUSIC_ROOM_INSENSITIVE_COLOR = "#888"

## Here are the default buttons used for the music controls below. You can
## update these or replace them.
image play_button = "gui/music_room/play.webp"
image pause_button = "gui/music_room/pause.webp"
image next_button = "gui/music_room/next.webp"
image prev_button = Transform("gui/music_room/next.webp", xzoom=-1.0)
image repeat_all_button = "gui/music_room/repeat all.webp"
## Note that this image is just a foreground on top of the repeat_all button!
image repeat_one_button = "gui/music_room/repeat 1.webp"
image shuffle_button = "gui/music_room/shuffle.webp"
image back_10_button = "gui/music_room/back_10.webp"
image forward_10_button = "gui/music_room/forward_10.webp"

## The "audio level" bars. These are optional to show next to the currently
## playing song. There are four bars that randomly change height.
define AUDIO_BAR_HEIGHT = 30
define AUDIO_BAR_WIDTH = 8
image audio_bar = Transform(MUSIC_ROOM_HOVER_COLOR,
    xysize=(AUDIO_BAR_WIDTH, AUDIO_BAR_HEIGHT))
transform audio_bar_move():
    yzoom renpy.random.random() ## Start at a random height
    block:
        ## Choose a random height to be
        choice:
            ease 0.2 yzoom 1.0
        choice:
            ease 0.2 yzoom 0.2
        choice:
            ease 0.2 yzoom 0.8
        choice:
            ease 0.2 yzoom 0.0
        choice:
            ease 0.2 yzoom 0.5
        repeat
## The final audio bars image, with four bars that randomly change height.
image audio_bars = HBox(
    At('audio_bar', audio_bar_move),
    At('audio_bar', audio_bar_move),
    At('audio_bar', audio_bar_move),
    At('audio_bar', audio_bar_move),
    yalign=1.0, ysize=AUDIO_BAR_HEIGHT,
)

################################################################################
## TRANSFORMS
################################################################################
## A transform that makes it easier to apply colours to the various buttons.
## The default images are black, so it uses ColorizeMatrix to colorize them.
## The colours are defined at the top of the file.
transform colorize_button(idle=MUSIC_ROOM_IDLE_COLOR,
        hover=MUSIC_ROOM_HOVER_COLOR,
        selected_idle=MUSIC_ROOM_SELECTED_IDLE_COLOR,
        selected_hover=MUSIC_ROOM_SELECTED_HOVER_COLOR,
        insensitive=MUSIC_ROOM_INSENSITIVE_COLOR):
    matrixcolor ColorizeMatrix(insensitive, "#fff")
    on idle:
        matrixcolor ColorizeMatrix(idle, "#fff")
    on hover:
        matrixcolor ColorizeMatrix(hover, "#fff")
    on insensitive:
        matrixcolor ColorizeMatrix(insensitive, "#fff")
    on selected_idle:
        matrixcolor ColorizeMatrix(selected_idle, "#fff")
    on selected_hover:
        matrixcolor ColorizeMatrix(selected_hover, "#fff")

## A simple transform to easily resize buttons. Used by some layouts.
transform zoom_button(z):
    zoom z

style music_room_pos:
    color "#fff" xalign 0.5 adjust_spacing False yalign 0.5
style music_room_duration:
    color "#fff" xalign 0.5 adjust_spacing False yalign 0.5


screen music_room(mr):
    tag menu
    default current_track = mr.get_current_song()

    use menu_header("Music Room", Return()):
        fixed:
            style_prefix 'music_room'
            xfill True yfill True
            frame:
                style_prefix 'track_list'
                viewport:
                    scrollbars "vertical" mousewheel True draggable True
                    has vbox
                    label _("Track List") style "music_room_title" xalign 0.5
                    for num, song in enumerate(mr.get_tracklist(all_tracks=True)):
                        button:
                            action mr.Play(song.path)
                            has hbox
                            fixed:
                                if song is current_track:
                                    ## If the song is currently playing, add a
                                    ## bit of flair with some audio bars.
                                    add Transform('audio_bars', ysize=30,
                                        xalign=0.5, yzoom=-1.0, yalign=0.55)
                                else:
                                    ## The track number
                                    text str(num+1) align (0.5, 0.55)
                            vbox:
                                spacing 4
                                ## Track info
                                label song.name
                                text song.artist
            vbox:
                spacing 15 yalign 1.0

                fixed:
                    xalign 0.5 yfit True
                    if current_track:
                        label current_track.name text_color "#fff" xalign 0.5:
                            text_text_align 0.5 style 'music_room_title'
                            text_layout "subtitle"

                null height 80

                hbox:
                    xalign 0.5 spacing 60
                    ################## Shuffle button ##################
                    imagebutton:
                        idle "shuffle_button"
                        at colorize_button(MUSIC_ROOM_INSENSITIVE_COLOR,
                            MUSIC_ROOM_IDLE_COLOR), zoom_button(0.9)
                        action mr.ToggleShuffle()
                    ############ Previous, play/pause, next buttons ############
                    imagebutton:
                        idle "prev_button"
                        at colorize_button(), zoom_button(0.65)
                        action mr.Previous()
                    imagebutton:
                        at colorize_button(), zoom_button(0.5)
                        idle "pause_button" hover "pause_button"
                        selected_idle "play_button" selected_hover "play_button"
                        action mr.PlayAction()
                    imagebutton:
                        idle "next_button"
                        at colorize_button(), zoom_button(0.65)
                        action mr.Next()
                    ################## Repeat all, repeat one buttons ##################
                    imagebutton:
                        at colorize_button(idle=MUSIC_ROOM_INSENSITIVE_COLOR,
                            hover=MUSIC_ROOM_IDLE_COLOR), zoom_button(0.9)
                        idle "repeat_all_button"
                        if mr.single_track:
                            foreground "repeat_one_button"
                        action mr.CycleLoop()

                ################## Music Bar ##################
                hbox:
                    spacing 8 ysize 22 xalign 0.5
                    fixed:
                        yfit True xsize 100
                        add mr.get_pos(style="music_room_pos")
                    music_bar room mr xsize config.screen_width-250
                    fixed:
                        yfit True xsize 100
                        add mr.get_duration(style="music_room_duration")

                null height 30

style music_room_image_button:
    align (0.5, 0.5)

style track_list_frame:
    background "#213738bd"
    yalign 0.0 xalign 0.0
    padding (25, 25) xfill True ysize 600+50
style track_list_viewport:
    xfill True ysize 600
style track_list_side:
    spacing 20
style track_list_vbox:
    spacing 0
style track_list_button:
    right_padding 45
    background Transform("#b3f3ee", ysize=2, yalign=1.0)
    hover_foreground "#fff1"
    ypadding 15 xfill True
style track_list_hbox:
    xalign 0.0 spacing 18
style track_list_fixed:
    xsize 45 ysize 45 yalign 0.5
style track_list_text:
    color "#bfbfb9"
    insensitive_color "#666"
style track_list_label:
    background None padding (2, 0)
style track_list_label_text:
    color "#f7f7ed" hover_color "#b3f3ee" selected_color "#5ef4d3"
    insensitive_color "#666"
style music_room_title:
    background None xalign 0.5 bottom_padding 15
style music_room_title_text:
    font gui.name_text_font
    size 40 color "#b3f3ee" xalign 0.5