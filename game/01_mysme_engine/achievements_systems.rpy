init python:

    class Achievement():
        """
        A class with information on in-game achievements which can be extended
        to use with other systems (e.g. Steam achievements).
        """
        all_achievements = [ ]
        def __init__(self, name, id=None, description=None, unlocked_image=None,
                locked_image=None, stat_max=None, stat_modulo=0):

            self.name = name
            # Try to sanitize the name for an id, if possible
            self.id = id or name.lower().replace(' ', '_').replace("'", '')

            self.description = description
            self.unlocked_image = unlocked_image or Null()
            self.locked_image = locked_image or "locked_achievement"

            self.stat_max = stat_max
            self.stat_modulo = stat_modulo

            # Add to list of all achievements
            self.all_achievements.append(self)