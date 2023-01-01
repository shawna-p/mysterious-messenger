init python:

    class Achievement():
        """
        A class with information on in-game achievements which can be extended
        to use with other systems (e.g. Steam achievements).

        Attributes:
        -----------
        name : string
            The human-readable name of this achievement. May have spaces,
            apostrophes, dashes, etc.
        id : string
            The code-friendly name of this achievement (which can be used for
            things like Steam backend). May not include spaces, single or
            double quotes, or dashes. If not provided, name will be sanitized
            for this purpose.
        description : string
            A longer description for this achievement. Optional.
        unlocked_image : Displayable
            A displayable to use when this achievement is unlocked.
        locked_image : Displayable
            A displayable to use when this achievement is locked. If not
            provided, requires an image named "locked_achievement" is declared.
        stat_max : int
            If provided, an integer corresponding to the maximum progress of
            an achievement, if the achievement can be partially completed
            (e.g. your game has 24 chapters and you want this to tick up
            after every chapter, thus, stat_max is 24). The achievement is
            unlocked when it reaches this value.
        stat_progress : int
            The current progress for the stat.
        stat_modulo : int
            The formula (stat_progress % stat_modulo) is applied whenever
            achievement progress is updated. If the result is 0, the
            progress is shown to the user. By default this is 0 so all updates
            to stat_progress are shown. Useful if, for the supposed 24-chapter
            game progress stat, you only wanted to show updates every time the
            player got through a quarter of the chapters. In this case,
            stat_modulo would be 6 (24//4).
        hidden : bool
            True if this achievement's description and name should be hidden
            from the player.
        timestamp : Datetime
        """
        all_achievements = [ ]
        def __init__(self, name, id=None, description=None, unlocked_image=None,
                locked_image=None, stat_max=None, stat_modulo=0, hidden=False):

            self._name = name
            # Try to sanitize the name for an id, if possible
            self.id = id or name.lower().replace(' ', '_').replace("'", '').replace('-', '_')

            self._description = description
            self.unlocked_image = unlocked_image or Null()
            self.locked_image = locked_image or "locked_achievement"

            self.stat_max = stat_max
            self.stat_modulo = stat_modulo
            self.stat_progress = 0

            self.hidden = hidden
            if persistent.achievement_timestamp is not None:
                self._timestamp = persistent.achievement_timestamp.get(self.id, None)

            # Add to list of all achievements
            self.all_achievements.append(self)

            # Register with backends
            achievement.register(self.id, stat_max=stat_max, stat_modulo=stat_modulo)

        @property
        def timestamp(self):
            if self.has():
                return "Unlocked {}".format(
                    datetime.fromtimestamp(
                        self._timestamp).strftime("%b %d, %Y @ %I:%M %p")
                )
            else:
                return ""

        @property
        def idle_img(self):
            if self.has():
                return self.unlocked_image
            else:
                return self.locked_image

        @property
        def name(self):
            if self.hidden and not self.has():
                return "???"
            else:
                return self._name

        @property
        def description(self):
            if self.hidden and not self.has():
                return "???"
            else:
                return self._description

        ## Wrappers for various achievement functionality
        def clear(self):
            return achievement.clear(self.id)
        def get_progress(self):
            return achievement.get_progress(self.id)
        def grant(self):
            has_achievement = self.has()
            x = achievement.grant(self.id)
            if not has_achievement:
                # First time this was granted
                self.achievement_popup()
                # Save the timestamp
                self._timestamp = time.time()
                store.persistent.achievement_timestamp[self.id] = self._timestamp
            return x
        def has(self):
            return achievement.has(self.id)
        def progress(self, complete):
            has_achievement = self.has()
            x = achievement.progress(self.id, complete)
            if not has_achievement and self.has():
                # First time this was granted
                self.achievement_popup()
            return x

        def achievement_popup(self):
            """
            A function which shows an achievement screen to the user
            to indicate they were granted an achievement.
            """

            if not self.has():
                # Don't have this achievement
                return

            # Otherwise, show the achievement screen
            # TODO: onlayer?
            store.onscreen_achievements += 1
            renpy.show_screen('achievement_popup', a=self,
                _tag=get_random_screen_tag(6, return_after_tag=True))

        def Toggle(self):
            """
            A developer action to easily toggle the achieved status
            of a particular achievement.
            """
            return [SelectedIf(self.has()),
                If(self.has(),
                    Function(self.clear),
                    Function(self.grant))]

    ## Declare achievements here. The order you declare them in is the order
    ## they will appear on the Achievements page.
    test_achievement = Achievement("A Test", "a_test", "A test achievement!",
        "CGs/ju_album/cg-1-thumb.webp")
    hidden_achievement = Achievement("Hidden", "hidden", "You got the hidden achievement!",
        "CGs/ju_album/cg-1-thumb.webp", hidden=True)
    third_achievement = Achievement("A longer achievement name",
        description="I want this to be long enough to possibly expand this bubble",
        unlocked_image="CGs/ju_album/cg-1-thumb.webp"
        )


default persistent.achievement_timestamp = dict()
default onscreen_achievements = 0

image blue_ui_bg = Frame("Menu Screens/Day Select/daychat01_2.webp", 20, 15, 20, 15)