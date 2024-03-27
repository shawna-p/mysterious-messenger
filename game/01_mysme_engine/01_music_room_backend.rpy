################################################################################
##
## Extended Music Room for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com)
##
################################################################################
## This file contains code for a music room in Ren'Py. It is designed
## as a wrapper to the built-in music room system, so many of the methods and
## functions used there will also work with this music room.
##
## If you use this code in your projects, credit me as Feniks @ feniksdev.com
##
## If you'd like to see how to use this tool, check the other file,
## music_room.rpy! This is just the backend; you don't need to understand
## everything in this file.
##
## Leave a comment on the tool page on itch.io or an issue on the GitHub
## if you run into any issues.
################################################################################
python early:

    class AudioBar(renpy.display.behavior.Bar):
        """
        A special kind of bar which allows the user to adjust the position
        of the audio being played on release. It is automatically set up to
        use the right value and can be styled like any other bar. You can
        provide a "room" property to the bar, which should be a MusicRoom
        object (such as the ExtendedMusicRoom included in these files). If so,
        it will automatically work with the playlist and looping features of
        the room. Otherwise, you can provide a "channel" property, which should
        be a string. The music will be played on that channel when restarted.
        """

        def __init__(self, **kwargs):
            self.musicroom = kwargs.get('room', None)
            if self.musicroom:
                kwargs['channel'] = self.musicroom.channel
            kwargs['value'] = AudioAdjustmentValue(kwargs.get('channel', 'music'),
                kwargs.get('update_interval', 0.1))
            super(AudioBar, self).__init__(**kwargs)
            self.channel = kwargs.get('channel', 'music')
            self.released_fn = adjust_music_released
            self.released = self.pass_value_released

        def pass_value_released(self):
            return self.released_fn(self.adjustment.value,
                self.musicroom or self.channel)

    ## Create a special music bar screen language statement which uses the
    ## AudioBar class.
    renpy.register_sl_displayable("music_bar", AudioBar, "bar", 0, replaces=True,
        pass_context=True
        ).add_property("hovered"
        ).add_property("unhovered"
        ).add_property("channel"
        ).add_property("room"
        ).add_property("update_interval"
        ).add_property_group("bar")

init python:

    def adjust_music_released(value, musicroom):
        """
        Plays a track starting at the position provided by value, in seconds,
        on the provided channel. musicroom should either be a MusicRoom
        object or the name of a channel. If it is the former, it will work
        with the looping and playlist features of the room. Otherwise, it will
        just play the track on the channel.
        """
        next_songs = None

        try:
            channel = musicroom.channel
            loop = musicroom.loop or musicroom.single_track
            fadeout = musicroom.fadeout
            fadein = musicroom.fadein
        except:
            channel = musicroom
            loop = renpy.music.get_loop(channel)
            fadeout = 0.0
            fadein = 0.0
            if loop:
                next_songs = list(loop)
                next_songs.pop(0)
                loop = True

        track = renpy.music.get_playing(channel)
        if not track:
            return

        # Strip out any existing <> information
        track = strip_playback(track)

        duration = renpy.music.get_duration(channel)
        if not duration:
            return

        new_t = max(value, 0)
        new_t = min(new_t, duration)

        file = "<from {} loop 0.0>{}".format(new_t, track)

        try:
            musicroom.play(file)
        except Exception as e:
            print("EXCEPTION", e)
            renpy.music.play(file, channel=channel, loop=loop,
                fadeout=fadeout, fadein=fadein)
            if next_songs:
                renpy.music.queue(next_songs, channel=channel, clear_queue=True,
                    loop=loop)

    class AudioAdjustmentValue(AudioPositionValue):
        """
        An AudioPositionValue bar value that gives a bit of extra
        leeway on not jumping the position to 0. It has an adjustable value
        which can be changed on release using the AudioBar class.
        """
        def __init__(self, *args, **kwargs):
            super(AudioAdjustmentValue, self).__init__(*args, **kwargs)
            self.last_nonzero_pos = 0
            self.last_duration = 1.0
            self.last_zero = 0

        def get_pos_duration(self):
            """
            Return the position and duration of the currently playing track.
            If no track is detected, and some information is saved, it will
            keep showing the saved information for a short while to avoid
            jumping the bar to 0.
            """
            pos = renpy.music.get_pos(self.channel) or self.last_nonzero_pos
            duration = renpy.music.get_duration(self.channel) or self.last_duration

            if pos > self.update_interval:
                self.last_nonzero_pos = pos
                self.last_duration = duration
                self.last_zero = 0
            else:
                self.last_zero += 1

            if self.last_zero > 10:
                return pos, duration
            else:
                return self.last_nonzero_pos, self.last_duration

        def get_adjustment(self):
            """
            Get the current value of the adjustment for this bar, based on
            the position and duration of the currently playing song.
            """
            pos, duration = self.get_pos_duration()
            self.adjustment = ui.adjustment(value=pos, range=duration,
                adjustable=True)
            return self.adjustment

init -50 python:

    class MusicInfo():
        """
        A class with information on a track which can be played in the music
        room.

        Attributes:
        -----------
        name : string
            The name of the track.
        path : string
            The file path to the track.
        artist : string
            The artist of the track.
        art : Displayable
            The art to display for the track.
        description : string
            An optional description of the track (can be used for extra
            information, when the track plays in-game, the length of the
            track to display in the track list, etc.).
        unlock_condition : string
            The condition to unlock the track. This is a string that can be
            evaluated to a boolean. If it evaluates to True, the track is
            unlocked. If it evaluates to False, the track is locked. By default,
            a track is unlocked if it has been seen in-game.
        """
        ALL_MUSIC_FILES = [ ]
        PATH_TO_INFO = dict()
        def __init__(self, name, path, artist=None, art=None, description=None,
                    unlock_condition=None):
            self.name = name
            self.path = path
            self.artist = artist
            self.art = art
            self.description = description

            if unlock_condition is None:
                self.unlock_condition = "renpy.seen_audio('{}')".format(path)
            else:
                self.unlock_condition = unlock_condition

            MusicInfo.ALL_MUSIC_FILES.append(self)
            MusicInfo.PATH_TO_INFO[path] = self

        @property
        def locked(self):
            try:
                return not eval(self.unlock_condition)
            except:
                return True

        def __str__(self):
            return "<MusicInfo: {} : {} : {}>".format(self.name, self.path,
                "locked" if self.locked else "unlocked")


    def strip_playback(filename):
        """
        Strip out any existing <> playback information from a filename.
        """
        if filename and filename.startswith("<"):
            return '>'.join(filename.split(">")[1:])
        else:
            return filename


    @renpy.pure
    class CustomMusicRoomPlay(Action, FieldEquality):
        """
        The action returned by MusicRoom.Play when called with a file.
        It's the same as __MusicRoomPlay in the engine, but with a more
        forgiving `get_selected` method to account for partial playback.
        """
        identity_fields = [ "mr" ]
        equality_fields = [ "filename" ]

        def __init__(self, mr, filename):
            self.mr = mr
            self.filename = filename
            self.selected = self.get_selected()

        def __call__(self):

            renpy.restart_interaction()
            playing = renpy.music.get_playing(self.mr.channel)
            playing = strip_playback(playing) if playing else None

            if playing == self.filename:
                if renpy.music.get_pause(self.mr.channel):
                    renpy.music.set_pause(False, self.mr.channel)
                    return
            self.mr.play(self.filename, 0)

        def get_sensitive(self):
            return self.mr.is_unlocked(self.filename)

        def get_selected(self):
            song = renpy.music.get_playing(self.mr.channel)
            if song:
                song = strip_playback(song)
            return song == self.filename

        def periodic(self, st):
            if self.selected != self.get_selected():
                self.selected = self.get_selected()
                renpy.restart_interaction()

            self.mr.periodic(st)

            return .1


    class ExtendedMusicRoom(MusicRoom):
        """
        A class which extends the built-in music room to allow for greater
        compatibility with partial playback.

        ExtendedMusicRoom-specific Attributes:
        --------------------------------------
        alphabetical : bool
            If True, the music room will be sorted alphabetically. If False,
            the music room will be sorted by the order in which the tracks
            were added to the music room. Defaults to False.
        default_art : Displayable
            A displayable to use as the default art for tracks, unless a
            more specific art is given.
        saved_pos : string
            The last saved position of the currently playing track. Saved to
            avoid flickers in display due to a pause between starting a track
            again using partial playback.
        saved_duration : string
            The last saved duration of the currently playing track. Saved to
            avoid flickers in display due to a pause between starting a track
            again using partial playback.
        last_zero : int
            The number of times the position of the currently playing track
            has been None. Used to avoid flickers in display due to a pause
            between starting a track again using partial playback.
        last_song : string
            Obsolete, retained for compatibility.
        old_shuffle : bool
            The value of shuffle, not taking into account the current value
            of single_track. Used to remember the shuffle value when single
            track is toggled on.
        music_dictionary : dict
            A dictionary of path : MusicInfo objects for all tracks in the
            music room.
        """
        ## The grace period for the position of the currently playing track
        ## to not be reset to 0. Mostly prevents the bar from jumping to zero
        ## when we're starting partial playback in a new position.
        ZERO_THRESHOLD = 10
        def __init__(self, *args, **kwargs):
            """
            ExtendedMusicRoom-specific Arguments:
            -------------------------------------
            alphabetical : bool
                If True, the music room will be sorted alphabetically. If False,
                the music room will be sorted by the order in which the tracks
                were added to the music room. Defaults to False.
            default_art : Displayable
                A displayable to use as the default art for tracks, unless a
                more specific art is given.
            """
            self.alphabetical = kwargs.pop("alphabetical", False)
            stop_action = kwargs.pop("stop_action", None)
            if stop_action and not isinstance(stop_action, list):
                stop_action = [ stop_action ]
            else:
                stop_action = [ ]
            stop_action.append(SetScreenVariable("current_track", None))
            kwargs['stop_action'] = stop_action
            if kwargs['single_track']:
                kwargs['loop'] = True
            super(ExtendedMusicRoom, self).__init__(*args, **kwargs)
            self.default_art = kwargs.pop('default_art', Null())
            self.saved_pos = "--:--"
            self.saved_duration = "--:--"
            self.last_zero = 0
            self.last_song = None
            self.old_shuffle = self.shuffle
            self.music_dictionary = dict()

        def add(self, name, path, artist=None, art=None, description=None,
                    unlock_condition=None):
            """
            Create a MusicInfo object which adds music to this music room.
            See the MusicInfo class for information on these fields.
            """
            track = MusicInfo(name, path, artist, art or self.default_art,
                description, unlock_condition)

            super(ExtendedMusicRoom, self).add(track.path,
                always_unlocked=track.unlock_condition=="True",
                action=SetScreenVariable('current_track', track))

            self.music_dictionary[track.path] = track

            if self.alphabetical:
                self.playlist.sort(key=lambda x: self.music_dictionary[x].name)

        def is_unlocked(self, filename):
            """
            Returns True if the filename has been unlocked (or is always
            unlocked), and False if it is still locked.
            """
            track = self.music_dictionary.get(filename)

            if filename in self.always_unlocked:
                return True

            ## Allow for all songs in developer mode with the correct
            ## config value. Otherwise, use only unlocked songs.
            if config.developer and myconfig.UNLOCK_TRACKS_FOR_DEVELOPMENT:
                return True

            return (not track.locked)

        def periodic(self, st):
            """
            A function which is called periodically. Used to ensure actions
            are called when the music room changes songs to update the
            song information and possibly reshuffle the queue.
            """

            if st == self.st:
                return
            elif st < self.st:
                self.last_playing = None

            self.st = st

            current_playing = renpy.music.get_playing(self.channel)
            if current_playing is None:
                current_playing = ""
            else:
                current_playing = strip_playback(current_playing)

            if self.last_playing != current_playing:
                action = self.action.get(current_playing, None)
                renpy.run_action(action)
                self.last_playing = current_playing

        def pos_dd(self, st, at, style="music_room_pos"):
            """
            A DynamicDisplayable function for the position of the currently
            playing track.
            """
            x = renpy.music.get_pos(channel=self.channel)
            if x is None:
                txt = "--:--"
                self.last_zero += 1
            else:
                ## Format it in 00:00 style
                txt = "{:02}:{:02}".format(int(x/60), int(x%60))
                self.saved_pos = txt
                self.last_zero = 0

            ## Use the saved value if it's been temporarily at zero.
            if self.last_zero < self.ZERO_THRESHOLD:
                txt = self.saved_pos
            ## Make sure this is updated at least every second
            return Text(txt, style=style), 0.2

        def duration_dd(self, st, at, style="music_room_duration"):
            """
            A DynamicDisplayable function for the duration of the currently
            playing track.
            """
            x = renpy.music.get_duration(channel=self.channel)
            if not x:
                txt = "--:--"
            else:
                ## format it in 00:00 style
                txt = "{:02}:{:02}".format(int(x/60), int(x%60))
                self.saved_duration = txt
            if self.last_zero < self.ZERO_THRESHOLD:
                txt = self.saved_duration
            ## This only needs to be updated when the song changes instead
            ## of every second.
            return Text(txt, style=style), None

        def get_pos(self, style="music_room_text"):
            """
            Returns the position of the currently playing track, in seconds.
            """
            return DynamicDisplayable(self.pos_dd, style=style)

        def get_duration(self, style="music_room_text"):
            """
            Returns the duration of the currently playing track, in seconds.
            """
            return DynamicDisplayable(self.duration_dd, style=style)

        def queue_empty_callback(self):
            if not self.loop:
                return
            if self.single_track:
                self.play(None, 0, queue=True, clear_queue=False)
            elif self.shuffle:
                self.shuffled = None
                ## Shuffle the playlist again to queue up in a new order.
                self.play(None, 0, queue=True, clear_queue=False)
            else:
                self.play(None, 1, queue=True)

        def play(self, filename=None, offset=0, queue=False, strip=False,
                clear_queue=True):
            """
            Starts the music room playing. The file we start playing with is
            selected in two steps.

            If `filename` is an unlocked file, we start by playing it.
            Otherwise, we start by playing the currently playing file, and if
            that doesn't exist or isn't unlocked, we start with the first file.

            We then apply `offset`. If `offset` is positive, we advance that
            many files, otherwise we go back that many files.

            If `queue` is true, the music is queued. Otherwise, it is played
            immediately.

            strip ensures that the song which is set up to be played
            does not have partial playback information.

            Clear queue makes sure we can set up a new queue when it's empty.
            """

            playlist = self.unlocked_playlist(filename)

            if not playlist:
                return

            renpy.music.set_queue_empty_callback(self.queue_empty_callback,
                channel=self.channel)

            if filename is None:
                filename = renpy.music.get_playing(channel=self.channel)
            ## Strip out any existing <> information. This ensures the
            ## music room can find songs played via partial playback.
            if filename:
                find_filename = strip_playback(filename)
            else:
                find_filename = None

            try:
                idx = playlist.index(find_filename)
                has_filename = True
            except ValueError:
                has_filename = False
                idx = 0

            idx = (idx + offset) % len(playlist)

            if self.single_track:
                playlist = [ playlist[idx] ]
            elif self.loop and not self.shuffle:
                playlist = playlist[idx:] + playlist[:idx]
            else:
                playlist = playlist[idx:]

            if (has_filename and playlist and playlist[0] == find_filename
                    and not queue and not strip):
                # Play the partial playback version of the song.
                playlist.pop(0)
                playlist.insert(0, filename)

            if queue:
                renpy.music.queue(playlist, channel=self.channel, loop=False,
                    clear_queue=clear_queue)
            else:
                renpy.music.play(playlist, channel=self.channel,
                    fadeout=self.fadeout, fadein=self.fadein, loop=False)
            renpy.restart_interaction()

        def next(self):
            """
            Play the next file in the playlist.
            """

            filename = renpy.music.get_playing(channel=self.channel)
            if filename is None:
                return self.play(None, 0)
            else:
                ## Turn off single track playback and toggle regular looping
                if self.single_track:
                    self.single_track = False
                    self.loop = True
                    ## Reset shuffle if necessary
                    self.shuffle = self.old_shuffle
                return self.play(None, 1)

        def previous(self):
            """
            Plays the previous file in the playlist.
            """
            pos = renpy.music.get_pos(channel=self.channel)
            if pos > 2 or self.single_track:
                ## This starts the current song over again if it's been
                ## playing for more than 2 seconds.
                return self.play(None, 0, strip=True)
            else:
                ## Turn off single track playback and toggle regular looping.
                if self.single_track:
                    self.single_track = False
                    ## Reset shuffle if necessary
                    self.shuffle = self.old_shuffle
                    self.loop = True
                return self.play(None, -1)

        def get_tracklist(self, all_tracks=False):
            """
            Get the unlocked tracks from this track list, or all tracks if
            all_tracks is True. Returns MusicInfo objects instead of
            filenames.
            """
            return [self.music_dictionary.get(x) for x in self.playlist
                if all_tracks or self.is_unlocked(x)]

        def get_current_song(self):
            """
            Returns the MusicInfo object for the currently playing song.
            """
            filename = renpy.music.get_playing(channel=self.channel)
            if filename is None:
                return None
            else:
                return self.music_dictionary.get(strip_playback(filename))

        def unlocked_playlist(self, filename=None):
            """
            Returns a list of filenames in the playlist that have been
            unlocked.
            """

            if self.shuffle:
                ## Create the shuffle order if it doesn't yet exist, or if
                ## we're starting to shuffle from a new track.
                if self.shuffled is None or (filename
                        and self.shuffled[0] != filename):
                    self.shuffled = list(self.playlist)
                    random.shuffle(self.shuffled)

                    if filename in self.shuffled:
                        self.shuffled.remove(filename)
                        self.shuffled.insert(0, filename)

                playlist = self.shuffled

            else:
                self.shuffled = None
                playlist = self.playlist

            return [ i for i in playlist if self.is_unlocked(i) ]

        def Play(self, filename=None):
            """
            :doc: music_room method

            This action causes the music room to start playing. If `filename`
            is given, that file begins playing. Otherwise, the currently playing
            file starts over (if it's unlocked), or the first file starts
            playing.

            If `filename` is given, buttons with this action will be insensitive
            while `filename` is locked, and will be selected when `filename`
            is playing.
            """

            if filename is None:
                return self.play

            if filename not in self.filenames:
                raise Exception("{0!r} is not a filename registered with this music room.".format(filename))

            return CustomMusicRoomPlay(self, filename)

        def PlayAction(self):
            """
            A convenience action to determine which action should be taken
            when the Play/Pause button is pressed for the music room.
            """
            if not (renpy.music.is_playing(channel=self.channel)):
                if self.shuffle:
                    return [SelectedIf(True), self.RandomPlay()]
                else:
                    return [SelectedIf(True), self.Play()]
            else:
                return [SelectedIf(renpy.music.get_pause(channel=self.channel)),
                    self.TogglePause()]

        def CycleLoop(self):
            """
            A convenience action to cycle through the 3 loop options:
                no loop, loop, and repeat one.
            """
            if not self.loop:
                ## Not looping; turn on loop.
                return [SelectedIf(False), self.SetLoop(True)]
            elif not self.single_track:
                ## Looping; toggle repeat one
                return [SelectedIf(True), self.SetSingleTrack(True)]
            else:
                ## Repeat one; turn off loop.
                return [SelectedIf(True), self.SetSingleTrack(False),
                    self.SetLoop(False)]

        def AdjustTrackPos(self, seconds):
            """
            A function that jumps `seconds` seconds on the currently playing
            track.
            """
            return AdjustTrackPos(seconds, self)

        def SetSingleTrack(self, value):
            """
            This action sets the value of the single_track property.
            """
            if value:
                act = [SelectedIf(self.single_track)]
            else:
                act = [SelectedIf(not self.single_track)]

            ## Have to remember the old value of shuffle if we're toggling
            ## single track on.
            if value:
                act.append(SetField(self, "old_shuffle", self.shuffle))
                act.append(SetField(self, "shuffle", False))
            else:
                act.append(SetField(self, "shuffle", self.old_shuffle))
            act.append(SetField(self, "single_track", value))
            act.append(self.queue_if_playing)
            return act

        def SetShuffle(self, value):
            """
            This action sets the value of the shuffle property.
            """
            if value:
                act = [SelectedIf(self.old_shuffle)]
            else:
                act = [SelectedIf(not self.old_shuffle)]

            if self.single_track:
                ## Can't *really* toggle shuffle if single track is on,
                ## but we can prep it to be the right value later
                act.append(SetField(self, "old_shuffle", value))
                ## Turn off shuffle if it's not already off
                act.append(SetField(self, "shuffle", False))
            else:
                ## Otherwise, set both to the new value
                act.append(SetField(self, "shuffle", value))
                act.append(SetField(self, "old_shuffle", value))
            ## And queue the music if it's playing
            act.append(self.queue_if_playing)
            return act

        def ToggleShuffle(self):
            """
            This action toggles the value of the shuffle property.
            """
            if self.old_shuffle:
                act = self.SetShuffle(False)
            else:
                act = self.SetShuffle(True)
            act.pop(0)
            act.insert(0, SelectedIf(self.old_shuffle))
            return act


    def adjust_track_pos(seconds, musicroom):
        """
        A function that jumps `seconds` seconds on the currently playing track.
        If musicroom is a Music Room, it will use the appropriate channel and
        loop information. Otherwise, it should be a channel name like "music".
        """
        try:
            channel = musicroom.channel
        except:
            channel = musicroom

        track = renpy.music.get_playing(channel)
        if not track:
            return

        # Strip out any existing <> information
        track = strip_playback(track)

        duration = renpy.music.get_duration(channel)
        if not duration:
            return

        t = renpy.music.get_pos(channel)
        if not t:
            return

        new_t = max(t+seconds, 0)
        new_t = min(new_t, duration)

        adjust_music_released(new_t, musicroom)


    class AdjustTrackPos(Action):
        """
        A custom action which uses partial playback to start playback at the
        provided seconds argument. musicroom should be a Music Room object or
        the channel name the music is being played on.
        """
        def __init__(self, seconds, musicroom):
            self.seconds = seconds
            self.musicroom = musicroom
            try:
                self.channel = musicroom.channel
            except:
                self.channel = musicroom
        def get_sensitive(self):
            return (renpy.music.is_playing(channel=self.channel)
                and not preferences.get_mute(self.channel)
                and preferences.get_volume(self.channel))
        def __call__(self):
            adjust_track_pos(self.seconds, self.musicroom)
            renpy.restart_interaction()


init -100 python in myconfig:
    _constant = True

    ## True if all tracks in the music room should be automatically unlocked
    ## during development. In a release build, tracks will automatically
    ## enforce the unlock condition regardless of the value of this variable,
    ## which only affects development.
    UNLOCK_TRACKS_FOR_DEVELOPMENT = True