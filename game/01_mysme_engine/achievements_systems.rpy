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
        """
        all_achievements = [ ]
        def __init__(self, name, id=None, description=None, unlocked_image=None,
                locked_image=None, stat_max=None, stat_modulo=0):

            self.name = name
            # Try to sanitize the name for an id, if possible
            self.id = id or name.lower().replace(' ', '_').replace("'", '').replace('-', '_')

            self.description = description
            self.unlocked_image = unlocked_image or Null()
            self.locked_image = locked_image or "locked_achievement"

            self.stat_max = stat_max
            self.stat_modulo = stat_modulo
            self.stat_progress = 0

            # Add to list of all achievements
            self.all_achievements.append(self)

            # Register with backends
            achievement.register(self.id, stat_max, stat_modulo)

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



