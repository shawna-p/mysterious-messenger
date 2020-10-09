## This code is heavily modified from trooper6's clock code
## found on the Lemma Soft forums at 
## https://lemmasoft.renai.us/forums/viewtopic.php?t=21978
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
        width : int
            Width of the clock.
        height : int
            Height of the clock.
        minutes : int
            Current time's minutes.
        seconds : int
            Current time's seconds.
        military : bool
            True if the time should be displayed in military format. If False,
            displays in 12-hour format.
        am_pm : string
            Equal to "AM" or "PM" depending on the time of day.
        """

        def __init__(self, my_size=185, military=False, **kwargs):
            """
            Create a Clock displayable object.

            Parameters:
            -----------
            my_size : int
                Width of the clock. The height is calculated based off of this.
            military : bool
                True if the time should be displayed in military format.
                If False, displays in 12-hour format.
            """
            super(Clock, self).__init__(**kwargs)

            # Determine how big the clock should be
            self.width = my_size
            self.height = (my_size*25)/100 # *32

            # Keep track of the minutes and seconds, and whether
            # the hours should be displayed military or with AM/PM
            self.minutes = 0
            self.seconds = 0
            self.military = military
            self.am_pm = "AM"

        def render(self, width, height, st, at):
            """Render the Clock object in real-time."""

            # Make sure the minutes variable is
            # always in sync with the seconds variable
            if self.minutes != self.seconds//60:
                self.minutes = self.seconds//60
            # Calculate how many seconds have passed today
            if self.seconds >= 86400:
                self.seconds -= 86400

            # Figure out how tall the font can be in order to fit within
            # the size defined for the box
            font_height = self.height # 44
            div = Text(":", style="digi_clock", size=font_height, yalign=0.5)
            the_time = list(Text("{0:02d}".format(item), style="digi_clock", 
                size=font_height)
                for item in self.get_time())
            font_xsize = (self.width) // 4 # -10, -65

            
            am_pm_txt = Text(str(self.am_pm), style='digi_clock', 
                            size=font_height)

            # Display everything in an hbox
            if not self.military:
                digi_text = HBox(Fixed(the_time[0], xsize=font_xsize+3), 
                    Fixed(div, xsize=10, yalign=0.5, xalign=0.5), 
                    Fixed(the_time[1], xsize=font_xsize),
                    Null(width=self.width//20),
                    Fixed(am_pm_txt, xsize=font_xsize),
                    xalign=0.5)
            else:
                digi_text = HBox(Fixed(the_time[0], xsize=font_xsize+3), 
                    Fixed(div, xsize=10, yalign=0.5, xalign=0.5), 
                    Fixed(the_time[1], xsize=font_xsize),
                    xalign=0.5)

            # Put everything into one Fixed box
            digi = Fixed(digi_text, xysize=(self.width, self.height))
            digi_render = renpy.render(digi, width, height, st, at)

            # Create a render for the Fixed box
            render = renpy.Render(self.width, self.height)

            # Blit (draw) the child's render to the render
            render.blit(digi_render, (0,0))

            self.realclock()

            # Make sure the object redraws itself after it makes changes
            renpy.redraw(self, 0)

            return render

        def realclock(self):
            """Run the clock based on the real-world time."""

            t = datetime.today()
            self.am_pm = time.strftime('%p', time.localtime())
            self.seconds = (3600 * t.hour) + (60 * t.minute) + t.second

        def get_time(self):
            """
            Return the current hours, minutes, and seconds of the clock
            and ensure the AM/PM is set properly.
            """

            h, m = divmod(self.minutes, 60)
            h = int(h)
            m = int(m)
            s = self.seconds%60
            s = int(s)

            self.am_pm = time.strftime('%p', time.localtime())

            if self.military:
                if h > 23:
                    h = h%24
            else:
                if h is 0:
                    h = 12
                elif h > 12:
                    h = h % 12
            return h, m, s

