init python:

    mm_mr = ExtendedMusicRoom(channel='music', fadeout=0.0, fadein=0.0,
        loop=True, single_track=False, shuffle=False, stop_action=None,
        alphabetical=True)

    # mm_mr.default_art = "gui/music_room/cover_art.webp"



screen music_room():
    tag menu

    use menu_header("Music Room", Return()):
        text "To be created..."