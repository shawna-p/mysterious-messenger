init -2:
    style digi_clock:
        is default
        font 'fonts/SamsungSans-Light.ttf'
        color "#fff"
        yalign 0.5

init -1 python:
    class Clock(renpy.Displayable):
        """
        Class that creates a displayable clock that updates in real-time.

        Attributes:
        -----------
        size : int
            The font size of the resulting clock text.
        military : bool
            True if this clock should display in military time, False otherwise.
        hour : int
            The current hour.
        minute : int
            The current minute.
        second : int
            The current second.
        am_pm : string
            "AM" or "PM" based on the current time.
        """
        def __init__(self, size=40, military=False, **kwargs):
            super().__init__(**kwargs)
            self.size = size
            self.military = military

            self.hour = 0
            self.minute = 0
            self.second = 0
            self.am_pm = "AM"

        def update_time(self):
            """Update the current time based on the datetime module."""
            t = datetime.today()

            self.hour = t.hour
            self.minute = t.minute
            self.second = t.second
            self.am_pm = "AM" if t.hour < 12 else "PM"

            if not self.military and self.hour > 12:
                self.hour -= 12

        def render(self, width, height, st, at):
            """Render the clock to the screen."""

            # First, update the time
            self.update_time()

            # How big do these numbers need to be?
            num_size = Text("88", style='digi_clock', size=self.size).size()
            # Convert to integers
            num_size = (int(num_size[0]), int(num_size[1]))

            time_list = [ ]
            time_list.append(Fixed(
                Text("{:02d}".format(self.hour),
                    style="digi_clock", size=self.size, xalign=1.0),
                xysize=num_size))
            time_list.append(Text(":", style='digi_clock', size=self.size, align=(0.5, 0.5)))
            time_list.append(Fixed(
                Text("{:02d}".format(self.minute),
                    style="digi_clock", size=self.size, xalign=1.0),
                xysize=num_size))

            if not self.military:
                time_list.append(Text("{}".format(self.am_pm), style="digi_clock", size=self.size))

            time_hbox = HBox(*time_list)
            # Render it virtually. This doesn't display it to the screen, but
            # calculates the width and height (which we need).
            hbox_render = renpy.render(time_hbox, width, height, st, at)
            new_width = hbox_render.width
            new_height = hbox_render.height

            #digi_render = renpy.render(time_hbox, width, height, st, at)

            # Create a render for the Fixed box
            render = renpy.Render(new_width, new_height)

            # Blit (draw) the child's render to the render
            render.blit(hbox_render, (0,0))

            # Make sure the object redraws itself after it makes changes
            renpy.redraw(self, 0)

            return render