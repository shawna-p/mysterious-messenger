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
        mm_mr.add(
            name=mr_name,
            path=key,
            artist="Flaming Heart",
        )



screen music_room(mr):
    tag menu
    default current_track = None

    use menu_header("Music Room", Return()):
        vbox:
            for track in mr.get_tracklist(all_tracks=True):
                textbutton track.name:
                    action mr.Play(track.path)