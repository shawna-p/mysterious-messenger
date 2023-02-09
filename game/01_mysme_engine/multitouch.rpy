init python in myconfig:
    viewport_inertia_amplitude = 30.0#20.0
    viewport_inertia_time_constant = 0.325

init python:
    import pygame

    # https://www.pygame.org/docs/ref/event.html
    # https://github.com/renpy/pygame_sdl2/blob/master/src/pygame_sdl2/event.pyx#L259

    config.pygame_events.extend([
        pygame.FINGERMOTION,
        pygame.FINGERDOWN,
        pygame.FINGERUP,
        pygame.MULTIGESTURE,
    ])

    class Finger():
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.touchdown_x = x
            self.touchdown_y = y
            self.last_three_speeds = [ ]

        def dist(self, x, y):
            """Return the distance from this finger to the given coordinates."""

            dx = self.x - x
            dy = self.y - y

            return (dx**2 + dy**2)**0.5

        def add_speed(self, speed):
            self.last_three_speeds.append(speed)
            if len(self.last_three_speeds) > 3:
                self.last_three_speeds.pop(0)

        @property
        def last_speed(self):
            if self.last_three_speeds:
                ## Return the average of all three
                all_xspeeds = [x[0] for x in self.last_three_speeds]
                all_yspeeds = [x[1] for x in self.last_three_speeds]
                final_x = sum(all_xspeeds) / float(len(self.last_three_speeds))
                final_y = sum(all_yspeeds) / float(len(self.last_three_speeds))
                return (final_x, final_y)
            return (0.0, 0.0)

        @property
        def finger_info(self):
            return "Finger: ({}, {})".format(self.x, self.y)

    class MyAdjustment(renpy.display.behavior.Adjustment):
        # renpy.display.behavior.Adjustment

        # The amplitude of the inertia.
        animation_amplitude = None # type: float|None

        # The target value of the inertia.
        animation_target = None # type: float|None

        # The time the inertia started
        animation_start = None # type: float|None

        # The time constant of the inertia.
        animation_delay = None # type: float|None

        # The warper applied to the animation.
        animation_warper = None # type (float) -> float|None


        def __init__(self, *args, **kwargs):
            super(MyAdjustment, self).__init__(*args, **kwargs)
            self.range_limits = (0, 1)

        def round_value(self, value, release):
            # Prevent deadlock border points

            if value <= self.range_limits[0]:
                return type(self._value)(self.range_limits[0])
            elif value >= self.range_limits[1]:
                return self.range_limits[1]

            # if value <= 0:
            #     return type(self._value)(0)
            # elif value >= self._range:
            #     return self._range

            if self.force_step is False:
                return value

            if (not release) and self.force_step == "release":
                return value

            return type(self._value)(self.step * round(float(value) / self.step))

        def change(self, value, end_animation=True):

            if end_animation:
                self.end_animation()

            if value < self.range_limits[0]:
                value = self.range_limits[0]
            if value > self.range_limits[1]: # type: ignore
                value = self.range_limits[1]

            # if value < 0:
            #     value = 0
            # if value > self._range: # type: ignore
            #     value = self._range

            if value != self._value:
                self._value = value
                for d in renpy.display.behavior.adj_registered.setdefault(self, [ ]):
                    renpy.display.render.redraw(d, 0)
                if self.changed:
                    return self.changed(value)

            return None

        def inertia_warper(self, done):
            return 1.0 - math.exp(-done * 6)

        def animate(self, amplitude, delay, warper):
            if not amplitude or not self._range:
                self.end_animation(True)
            else:
                self.animation_amplitude = amplitude
                # self.animation_target = self.round_value(self._value + amplitude,
                #     release=True)
                self.animation_target = self._value + amplitude

                self.animation_delay = delay
                self.animation_start = None
                self.animation_warper = warper
                self.update()

        def inertia(self, amplitude, time_constant, st):
            self.animate(amplitude, time_constant * 6.0, self.inertia_warper)
            self.periodic(st)

        def end_animation(self, always=False, instantly=False):
            if always or self.animation_target is not None:
                value = self.animation_target

                self.animation_amplitude = None
                self.animation_target = None
                self.animation_start = None
                self.animation_delay = None
                self.animation_warper = None

                if not instantly:
                    self.change(value, end_animation=False)

        def periodic(self, st):

            if self.animation_target is None:
                return

            if self.animation_start is None:
                self.animation_start = st

            done = (st - self.animation_start) / self.animation_delay
            done = self.animation_warper(done)

            value = self.animation_target - self.animation_amplitude * (1.0 - done)

            self.change(value, end_animation=False)

            # Did we hit a wall?
            if value <= self.range_limits[0] or value >= self.range_limits[1]:
                self.end_animation(instantly=True)
                print("Hit a wall", value, self.range, self.range_limits)
                return None
            elif st > self.animation_start + self.animation_delay: # type: ignore
                self.end_animation(instantly=True)
                print("Hit a wall", value, self.range, self.range_limits)
                return None
            else:
                return 0

    class MultiTouch(renpy.Displayable):

        def __init__(self, img, width, height, zoom_min=0.25, zoom_max=4.0,
                rotate_degrees=360, start_zoom=1.0, *args, **kwargs):
            super(MultiTouch, self).__init__(*args, **kwargs)
            self.img = img
            self.width = width
            self.height = height
            self.text = ""
            self.zoom = start_zoom
            self.rotate = 0

            self.xpos = config.screen_width//2
            self.ypos = config.screen_height//2

            self.anchor = (config.screen_width//2, config.screen_height//2)

            self.zoom_max = zoom_max
            self.zoom_min = zoom_min

            min_width_ratio = config.screen_width / float(width)
            min_height_ratio = config.screen_height / float(height)
            max_ratio = max(min_width_ratio, min_height_ratio)
            min_ratio = min(min_width_ratio, min_height_ratio)
            ## Screen is entirely covered by the image
            self.fill_screen_zoom_level = max(max_ratio, self.zoom_min)
            ## Screen contains the image, but may have top/bottom
            ## "black bars"/empty space in one dimension
            self.fit_screen_zoom_level = max(min_ratio, self.zoom_min)

            self.rotate_degrees = rotate_degrees

            self.touch_screen_mode = renpy.variant("touch")
            self.wheel_zoom = True

            self.drag_finger = None
            self.drag_offset = (0, 0)

            self.drag_position_time = None
            self.drag_speed = (0.0, 0.0)
            self.drag_position = (0, 0)

            self.stationary_drag_counter = 0

            self.xadjustment = MyAdjustment(1, 0)
            self.yadjustment = MyAdjustment(1, 0)

            self.padding = self.get_padding()

            self.update_adjustment_limits()

            self.fingers = [ ]

            self.original_values = (start_zoom, self.xpos, self.ypos, self.anchor)

        def reset_values(self):
            """Reset all values for this object."""

            self.zoom, self.xpos, self.ypos, self.anchor = self.original_values
            self.rotate = 0
            self.drag_finger = None
            self.drag_offset = (0, 0)

            self.drag_position_time = None
            self.drag_speed = (0.0, 0.0)
            self.drag_position = (0, 0)

            self.stationary_drag_counter = 0

            self.xadjustment = MyAdjustment(1, 0)
            self.yadjustment = MyAdjustment(1, 0)

            self.padding = self.get_padding()

            self.update_adjustment_limits()

            self.fingers = [ ]

        def per_interact(self):
            self.xadjustment.register(self)
            self.yadjustment.register(self)

        def clamp_zoom(self):
            self.zoom = min(max(self.zoom, self.zoom_min), self.zoom_max)

        def clamp_rotate(self):

            self.rotate %= 360
            self.rotate = min(max(self.rotate, -self.rotate_degrees), self.rotate_degrees)

        def redraw_adjustments(self, st):
            redraw = self.xadjustment.periodic(st)

            padding = self.padding

            if redraw is not None:
                renpy.redraw(self, redraw)
                self.xpos = int(padding//2 - self.xadjustment.value)

            redraw = self.yadjustment.periodic(st)
            if redraw is not None:
                renpy.redraw(self, redraw)
                self.ypos = int(padding//2 - self.yadjustment.value)

        def render(self, width, height, st, at):
            r = renpy.Render(width, height)

            dimensions = self.get_dimensions()

            self.redraw_adjustments(st)

            xpos, ypos = self.xpos, self.ypos

            the_img = Transform(self.img,
                xysize=dimensions,
                rotate=int(self.rotate),
                anchor=(0.5, 0.5),
                pos=(xpos, ypos))

            text = Text(self.text, style='multitouch_text')

            fix = Fixed(
                the_img, text,
                xysize=(config.screen_width, config.screen_height),
            )

            ren = renpy.render(fix, width, height, st, at)
            r.blit(ren, (0, 0))

            renpy.redraw(self, 0)

            return r

        def update_adjustments(self):
            """
            Update the x/yadjustments after updating the xypos.
            """

            ## Range: the whole width of the padded displayable
            range = self.padding

            self.xadjustment.range = range
            self.yadjustment.range = range

            ## Value: where the top-left of the screen is relative to the
            ## top-left of the displayable
            left_corner = self.left_corner

            ## Say the left corner is (-400, -300)
            ## The anchor is (10, 50)

            self.xadjustment.change(abs(left_corner[0]), end_animation=False)
            self.yadjustment.change(abs(left_corner[1]), end_animation=False)

        @property
        def left_corner(self):
            """Return the coordinates of the padded top-left corner of the image."""
            # Currently, the xpos/ypos are indicating the center of the image
            padding = self.padding
            return (self.xpos - padding//2, self.ypos - padding//2)

        def normalize_pos(self, x, y):
            return (int(x*config.screen_width), int(y*config.screen_height))

        def register_finger(self, x, y):
            finger = Finger(x, y)
            self.fingers.append(finger)
            return finger

        def find_finger(self, x, y):
            """
            Find the finger with the smallest distance between its current
            position and x, y
            """
            if not self.fingers:
                return None
            dist = [
                (f.dist(x, y), f) for f in self.fingers
            ]
            dist.sort(key=lambda x : x[0])
            return dist[0][1]

        def update_finger(self, x, y):
            """Find which finger just moved and update it."""
            if len(self.fingers) == 1:
                # Only one finger *to* move
                self.fingers[0].x = x
                self.fingers[0].x = y
                return self.fingers[0]
            finger = self.find_finger(x, y)
            if not finger:
                return
            finger.x = x
            finger.y = y
            return finger

        def remove_finger(self, x, y):
            finger = self.find_finger(x, y)
            if not finger:
                return
            self.fingers.remove(finger)
            return finger

        def touch_down_event(self, ev):
            if self.touch_screen_mode:
                return ev.type == pygame.FINGERDOWN
            else:
                return renpy.map_event(ev, "viewport_drag_start")

        def touch_up_event(self, ev):
            if self.touch_screen_mode:
                return ev.type == pygame.FINGERUP
            else:
                return renpy.map_event(ev, "viewport_drag_end")

        def calculate_drag_offset(self, x, y):

            padding = self.padding
            dx = x - self.xpos# - int(padding//2 - self.xadjustment.value)
            dy = y - self.ypos# - int(padding//2 - self.yadjustment.value)
            self.drag_offset = (dx, dy)

        def get_dimensions(self):
            return (int(self.width*self.zoom), int(self.height*self.zoom))

        def get_padding(self, dimensions=None):
            if dimensions is None:
                dimensions = self.get_dimensions()
            return int((dimensions[0]**2+dimensions[1]**2)**0.5)

        def clamp_pos(self):

            return

        def adjust_pos_for_zoom(self, start_zoom):
            """
            Adjust the position of the image such that it appears to be
            zooming in from the anchor point.
            """

            if start_zoom == self.zoom:
                # No change
                return
            ## First, where is the anchor point relative to the actual
            ## center anchor of the image?
            dx =  self.xpos - self.anchor[0]
            dy =  self.ypos - self.anchor[1]

            x_dist_from_zoom1 = dx / start_zoom
            y_dist_from_zoom1 = dy / start_zoom

            ## Okay, we're trying to keep that particular pixel in place while
            ## the image gets bigger. How much bigger/smaller has it gotten?

            ## So let's say we zoomed in from 0.75 zoom to 1.2 zoom.
            ## If the image was 100x100, it went from 75x75 to 120x120
            ## If our anchor point was at 25x25 on the original image, now
            ## it should be at 40x40 on the new size
            ## 25 / 0.75 * 1.2 = 40 (new_dx)
            ## Relative to the top-left corner of the unpadded image, in order
            ## to keep the 25x25 anchor point at the same place on the screen,
            ## it has to move -15, -15

            ## Goal: where does the original anchor point end up, after zooming?
            ## How about step 1 is just to have the anchor point follow the zoomed image

            ## First task: find where the anchor pixel position is on the new size
            new_dx = x_dist_from_zoom1*self.zoom
            new_dy = y_dist_from_zoom1*self.zoom

            # new_xanchor = int(self.xpos - new_dx)
            # new_yanchor = int(self.ypos - new_dy)

            new_xanchor = self.xpos - new_dx
            new_yanchor = self.ypos - new_dy

            # These are some wild guesses but let's say that all worked out,
            # now we gotta adjust the position to put that back at the
            # original anchor location
            xpos_adj = self.anchor[0] - new_xanchor
            ypos_adj = self.anchor[1] - new_yanchor

            self.xpos += int(xpos_adj)
            self.ypos += int(ypos_adj)

        def update_adjustment_limits(self):
            """
            Adjust the limits as to how far the xadjustment can *actually* go.
            """

            ## Clamp
            ## For the xpos: the minimum it can be will put the right edge
            ## against the right side of the screen
            ## So, how far is that?
            dimensions = self.get_dimensions()
            padding = self.get_padding(dimensions)

            xpadding = (padding - dimensions[0])//2
            ypadding = (padding - dimensions[1])//2

            xmin = xpadding
            xmax = (padding - xpadding - config.screen_width)

            ymin = ypadding
            ymax = padding - ypadding - config.screen_height

            self.xadjustment.range_limits = (xmin, xmax)
            self.yadjustment.range_limits = (ymin, ymax)

        def update_anchor(self):
            """
            Set the anchor as the middle between the two currently touching
            fingers.
            """
            if len(self.fingers) != 2:
                return

            finger1 = self.fingers[0]
            finger2 = self.fingers[1]

            x_midpoint = (finger1.x+finger2.x)//2
            y_midpoint = (finger1.y+finger2.y)//2

            self.anchor = (x_midpoint, y_midpoint)

        def update_image_pos(self, x, y):
            """
            The player has dragged their finger to point (x, y), and the
            drag itself is supposed to come along with it.
            """

            self.xpos = int(x - self.drag_offset[0])
            self.ypos = int(y - self.drag_offset[1])

            return

        def event(self, ev, event_x, event_y, st):
            self.text = ""

            if ev.type in (pygame.FINGERDOWN, pygame.FINGERMOTION, pygame.FINGERUP):
                x, y = self.normalize_pos(ev.x, ev.y)
            else:
                x = event_x
                y = event_y

            xadj_x = int(x - self.padding//2)
            yadj_y = int(y - self.padding//2)

            start_zoom = self.zoom

            if self.drag_finger is not None:
                # Dragging
                old_xvalue = self.xadjustment.value
                old_yvalue = self.yadjustment.value

                oldx, oldy = self.drag_position # type: ignore
                dx = xadj_x - oldx
                dy = yadj_y - oldy

                dt = st - self.drag_position_time
                if dt > 0:
                    old_xspeed, old_yspeed = self.drag_speed
                    new_xspeed = -dx / dt / 60
                    new_yspeed = -dy / dt / 60

                    done = min(1.0, dt / (1 / 60))

                    new_xspeed = old_xspeed + done * (new_xspeed - old_xspeed)
                    new_yspeed = old_yspeed + done * (new_yspeed - old_yspeed)

                    self.drag_speed = (new_xspeed, new_yspeed)

                    debug_log(f"Old speed: ({old_xspeed:.2f}, {old_yspeed:.2f})\nNew speed ({new_xspeed:.2f}, {new_yspeed:.2f})")

                    if ((0.05 > new_xspeed > -0.05)
                                and (0.05 > new_yspeed > -0.05)):
                        ## Check if we're just slowing down overall
                        if ((0.09 > old_xspeed > -0.09)
                                and (0.09 > old_yspeed > -0.09)):
                            debug_log("Slowing down")
                        else:
                            self.stationary_drag_counter += 1
                            debug_log("Increasing stationary counter:", self.stationary_drag_counter, color="blue")
                            if self.stationary_drag_counter < 4 and dt < 0.1:
                                # Don't update it yet
                                # But do correct the speed direction
                                debug_log(f"Reusing old speed ({old_xspeed:.2f}, {old_yspeed:.2f})")
                                if ((new_xspeed > 0 and old_xspeed < 0)
                                        or (new_xspeed < 0 and old_xspeed > 0)):
                                    adjusted_xspeed = old_xspeed * -1.0
                                else:
                                    adjusted_xspeed = old_xspeed

                                if ((new_yspeed > 0 and old_yspeed < 0)
                                        or (new_yspeed < 0 and old_yspeed > 0)):
                                    adjusted_yspeed = old_yspeed * -1.0
                                else:
                                    adjusted_yspeed = old_yspeed

                                #debug_log(f"Adjusted old speed is ({adjusted_xspeed:.2f}, {adjusted_yspeed:.2f}) vs ({new_xspeed:.2f}, {new_yspeed:.2f})")
                                #self.drag_speed = (adjusted_xspeed, adjusted_yspeed)
                                debug_log(f"Popping last speed {self.drag_finger.last_speed}")
                                self.drag_speed = self.drag_finger.last_speed
                    else:
                        self.stationary_drag_counter = 0
                        self.drag_finger.add_speed(self.drag_speed)

            if self.touch_down_event(ev):
                finger = self.register_finger(x, y)

                if self.drag_finger is None and len(self.fingers) == 1:
                    debug_log(f"Drag DOWN at ({x}, {y})", color="green")
                    # Inertia
                    self.drag_position = (xadj_x, yadj_y)
                    self.drag_position_time = st
                    self.drag_speed = (0.0, 0.0)

                    self.xadjustment.end_animation(instantly=True)
                    self.yadjustment.end_animation(instantly=True)

                    # Normal
                    self.calculate_drag_offset(x, y)
                    self.update_image_pos(x, y)
                    self.drag_finger = finger

                elif self.drag_finger and len(self.fingers) > 1:
                    debug_log(f"Finger DOWN at ({x}, {y})", color="green")
                    # More than one finger; turn off dragging
                    # self.update_image_pos(self.drag_finger.x, self.drag_finger.y)
                    self.drag_offset = (0, 0)
                    self.drag_finger = None

                    self.xadjustment.end_animation(instantly=True)
                    self.yadjustment.end_animation(instantly=True)

            elif self.touch_up_event(ev):
                finger = self.remove_finger(x, y)

                if finger and self.drag_finger is finger:
                    debug_log(f"Drag UP at ({x}, {y})\nStarted at ({finger.touchdown_x}, {finger.touchdown_y})", color="red")
                    self.drag_finger = None
                    self.drag_offset = (0, 0)

                    ## Inertia
                    xspeed, yspeed = self.drag_speed

                    if xspeed and myconfig.viewport_inertia_amplitude:
                        self.xadjustment.inertia(
                            myconfig.viewport_inertia_amplitude * xspeed,
                                myconfig.viewport_inertia_time_constant, st)
                    else:
                        xvalue = self.xadjustment.round_value(old_xvalue, release=True)
                        self.xadjustment.change(xvalue)

                    if yspeed and myconfig.viewport_inertia_amplitude:
                        self.yadjustment.inertia(
                            myconfig.viewport_inertia_amplitude * yspeed,
                                myconfig.viewport_inertia_time_constant, st)
                    else:
                        yvalue = self.yadjustment.round_value(old_yvalue, release=True)
                        self.yadjustment.change(yvalue)

                    self.drag_position = None
                    self.drag_position_time = None
                else:
                    if finger is None:
                        debug_log(f"Finger UP at ({x}, {y}) but couldn't actually find it in self.fingers", color="red")
                    else:
                        debug_log(f"Finger UP at ({x}, {y})\nStarted at ({finger.touchdown_x}, {finger.touchdown_y})", color="red")

            elif ev.type in (pygame.FINGERMOTION, pygame.MOUSEMOTION):
                finger = self.update_finger(x, y)
                if finger is not None and finger is self.drag_finger:
                    # They are dragging the image around
                    self.update_image_pos(x, y)

                    ## Inertia
                    new_xvalue = self.xadjustment.round_value(old_xvalue - dx,
                        release=False)
                    if old_xvalue == new_xvalue:
                        newx = oldx
                    else:
                        self.xadjustment.change(new_xvalue)
                        newx = xadj_x

                    new_yvalue = self.yadjustment.round_value(old_yvalue - dy,
                        release=False)
                    if old_yvalue == new_yvalue:
                        newy = oldy
                    else:
                        self.yadjustment.change(new_yvalue)
                        newy = yadj_y

                    self.drag_position = (newx, newy) # W0201
                    self.drag_position_time = st

            elif (ev.type == pygame.MULTIGESTURE
                    and len(self.fingers) > 1):

                self.rotate += ev.dTheta*360/8
                self.zoom += ev.dDist*4   # *15

                self.xadjustment.end_animation(instantly=True)
                self.yadjustment.end_animation(instantly=True)

                ## Set the anchor as the middle between their two fingers
                self.update_anchor()

            elif renpy.map_event(ev, "viewport_wheelup"):

                # Set the anchor to wherever they're hovering
                self.anchor = (x, y)

                self.xadjustment.end_animation(instantly=True)
                self.yadjustment.end_animation(instantly=True)

                if self.wheel_zoom:
                    self.zoom += 0.05 #0.25
                else:
                    self.rotate += 10

            elif renpy.map_event(ev, "viewport_wheeldown"):
                # Set the anchor to wherever they're hovering
                self.anchor = (x, y)

                self.xadjustment.end_animation(instantly=True)
                self.yadjustment.end_animation(instantly=True)

                if self.wheel_zoom:
                    self.zoom -= 0.25
                else:
                    self.rotate -= 10

            if ( (ev.type == pygame.MULTIGESTURE
                        and len(self.fingers) > 1)
                    or renpy.map_event(ev, "viewport_wheelup")
                    or renpy.map_event(ev, "viewport_wheeldown")
            ):

                self.clamp_rotate()
                self.clamp_zoom()
                self.padding = self.get_padding()
                self.update_adjustment_limits()
                self.adjust_pos_for_zoom(start_zoom)

            self.clamp_pos()
            self.update_adjustments()

            if self.fingers:
                self.text += '\n'.join([x.finger_info for x in self.fingers])
            else:
                self.text = "No fingers recognized"

            self.text += "\nPos: ({}, {})".format(self.xpos, self.ypos)
            self.text += "\nAnchor: {}".format(self.anchor)
            self.text += "\nxadjustment: {}/{}".format(self.xadjustment.value, self.xadjustment.range)
            self.text += "\nyadjustment: {}/{}".format(self.yadjustment.value, self.yadjustment.range)
            self.text += "\ndrag_speed: ({:.2f}, {:.2f})".format(self.drag_speed[0], self.drag_speed[1])


    class ZoomGalleryDisplayable(MultiTouch):
        """
        A class which allows zooming in on full-screen gallery images.
        """
        def __init__(self, img, width, height, zoom_max=4.0, use_container=False,
            *args, **kwargs):

            ## Calculate zoom_min. It should always fill the screen in one
            ## dimension
            min_width_ratio = config.screen_width / float(width)
            min_height_ratio = config.screen_height / float(height)
            min_ratio = min(min_width_ratio, min_height_ratio)

            super(ZoomGalleryDisplayable, self).__init__(img, width, height, min_ratio,
                zoom_max, rotate_degrees=0, start_zoom=min_ratio, *args, **kwargs)

        def clamp_pos(self):

            ## Clamp
            ## For the xpos: the minimum it can be will put the right edge
            ## against the right side of the screen
            ## So, how far is that?
            dimensions = self.get_dimensions()
            padding = self.padding

            xpadding = (padding - dimensions[0])//2
            ypadding = (padding - dimensions[1])//2

            has_black_bars = ((self.fill_screen_zoom_level > self.fit_screen_zoom_level)
                and (self.zoom < self.fill_screen_zoom_level))

            ## Are we zoomed out enough that we're going to start getting
            ## black bars? Is that possible?
            if has_black_bars and dimensions[0] <= config.screen_width:
                    self.xpos = config.screen_width//2
            else:
                ## When the image is against the right side, the left side will
                ## be at -(padding-screen_width) + xpadding
                xmin = (padding-xpadding-config.screen_width)*-1 + padding//2
                self.xpos = max(self.xpos, xmin)
                ## When the image is against the left side, the right side will
                ## be at -xpadding
                self.xpos = min(self.xpos, -xpadding+padding//2)

            if has_black_bars and dimensions[1] <= config.screen_height:
                self.ypos = config.screen_height//2
            else:
                ymin = (padding-ypadding-config.screen_height)*-1 + padding//2
                self.ypos = max(self.ypos, ymin)
                self.ypos = min(self.ypos, -ypadding+padding//2)

    class ZoomGalleryImage():
        """
        A class to facilitate declaring images to be used in a ZoomGallery.
        """
        def __init__(self, name, image, width=None, height=None,
                locked_image=None, condition="True"):

            self.name = name
            self.image = renpy.easy.displayable(image)
            self.width = width
            self.height = height
            self.locked_image = locked_image
            self.condition = condition

        @property
        def unlocked(self):
            try:
                return eval(self.condition)
            except Exception as e:
                return True

    class ZoomGallery(MultiTouch):
        """
        A class which holds a list of gallery images to be able to swipe
        through and view.
        """

        def __init__(self, *images, screen=None,
                image_size=None, locked_image=None,
                show_locked=False, loop_gallery=True, **kwargs):
            """
            images : ZoomGalleryImage[]
                ZoomGalleryImage objects corresponding to images to be added
                to this gallery.
            image_size : (int, int)
                If given, this is the width and height of all images in this
                gallery, or at least all images for which a more specific
                width and height is not given.
            locked_image : Displayable
                A displayable which is shown when the player has not
                unlocked this image in the gallery.
            show_locked : bool
                True if this gallery should show locked images when swiping
                through. If False, it will skip them.
            loop_gallery : bool
                True if this gallery should loop around to the first image
                if it reaches the last one.
            """
            super(ZoomGallery, self).__init__(Null(), config.screen_width,
                config.screen_height, **kwargs)
            if locked_image is not None and image_size is None:
                raise Exception("For a ZoomGallery, you must provide an image_size if you provide a locked_img. image_size must be the size of the locked_img")

            self.image_size = image_size
            self.locked_image = locked_image
            self.screen = screen
            if screen is None:
                raise Exception("ZoomGallery must be given the name of a screen to use for the gallery.")

            for image in images:
                if image.width is None:
                    image.width = image_size[0]
                    image.height = image_size[1]
                if image.locked_image is None:
                    image.locked_image = locked_image

            # Now create ZoomGalleryImage objects out of all of them
            self.gallery_images = [ ]
            self.gallery_displayables = [ ]
            self.image_lookup = dict()
            self.displayable_lookup = dict()

            for img in images:
                gi = ZoomGalleryDisplayable(img.image, img.width, img.height)
                self.image_lookup[img.name] = img
                self.displayable_lookup[img.name] = gi
                self.gallery_displayables.append(gi)
                self.gallery_images.append(img)

            self.previous_image = None
            self.current_image = self.gallery_images[0]
            if len(self.gallery_images) > 1:
                self.next_image = self.gallery_images[1]
            else:
                self.next_image = None

            self.unlocked_displayables = self.gallery_displayables.copy()
            self.loop_gallery = loop_gallery
            self.show_locked = show_locked

            self.viewing_child = False

            self.padding = self.get_padding()
            self.xpos = -10
            self.original_values = (self.original_values[0], self.xpos, self.original_values[2], self.original_values[3])

        def is_viewable(self, name):
            """
            Return True if this image is viewable in the gallery.
            """
            # First find it
            img = self.image_lookup.get(name, None)
            if img is None:
                return False
            return img.unlocked

        def set_up_gallery(self, from_image=None):
            """
            Set up the gallery to begin from a particular image, or from
            the first unlocked image if available.
            """

            if not self.show_locked:
                ## First, filter all the images for conditions.
                self.unlocked_images = [
                    x for x in self.gallery_images if x.unlocked
                ]
                ## Otherwise it's just a copy of regular images

            self.unlocked_displayables = [
                self.displayable_lookup[x.name] for x in self.unlocked_images
            ]

            ## Reset all the values in these gallery images
            for img in self.unlocked_displayables:
                img.reset_values()

            ## Is there a start image?
            if from_image is not None:
                from_image = self.displayable_lookup.get(from_image, None)
                try:
                    start_index = self.unlocked_displayables.index(from_image)
                except ValueError:
                    start_index = 0
                self.current_image = self.unlocked_displayables[start_index]
            else:
                start_index = 0
                self.current_image = self.unlocked_displayables[0]

            ## Set up next and previous images
            if len(self.unlocked_displayables) == 1:
                self.previous_image = None
                self.next_image = None
            else:
                if self.loop_gallery:
                    self.previous_image = self.unlocked_displayables[start_index-1]
                    self.next_image = self.unlocked_displayables[(start_index+1)%len(self.unlocked_displayables)]
                else:
                    prev_index = max(0, start_index-1)
                    next_index = min(len(self.unlocked_displayables)-1, start_index+1)
                    if prev_index == start_index:
                        self.previous_image = None
                    else:
                        self.previous_image = self.unlocked_displayables[prev_index]
                    if next_index == start_index:
                        self.next_image = None
                    else:
                        self.next_image = self.unlocked_displayables[next_index]

        def visit(self):
            return [x.image for x in self.unlocked_images]

        def update_adjustment_limits(self):
            """
            Adjust the limits as to how far the xadjustment can *actually* go.
            """

            ## Clamp
            ## For the xpos: the minimum it can be will put the right edge
            ## against the right side of the screen
            ## So, how far is that?
            dimensions = self.get_dimensions()
            padding = self.get_padding(dimensions)

            xpadding = (padding - dimensions[0])//2
            ypadding = (padding - dimensions[1])//2

            xmin = xpadding
            xmax = (padding - xpadding - config.screen_width)

            ymin = ypadding
            ymax = padding - ypadding - config.screen_height

            self.xadjustment.range_limits = (0, 1500+750)
            self.yadjustment.range_limits = (7, 7)

        def redraw_adjustments(self, st):
            redraw = self.xadjustment.periodic(st)

            padding = self.padding

            if redraw is not None:
                renpy.redraw(self, redraw)
                self.xpos = int(padding//2 - self.xadjustment.value)

        def render(self, width, height, st, at):
            r = renpy.Render(width, height)

            self.redraw_adjustments(st)

            text = ""
            child = self.current_image
            fix = Fixed(
                Transform(child, pos=(self.xpos+config.screen_width//2+10, self.ypos), anchor=(0.5, 0.5)),
                Window(Text(self.text, style="multitouch_text", color="#d4e2f3"),
                    background="#0008", style="frame", yalign=1.0),
                xysize=(config.screen_width, config.screen_height),
            )

            if self.viewing_child:
                ren = renpy.render(child, width, height, st, at)
            else:
                ren = renpy.render(fix, width, height, st, at)
            r.blit(ren, (0, 0))
            # Note to self: you can make another render and then r.blit(that_render)

            renpy.redraw(self, 0)

            return r

        def clamp_pos(self):
            ## Just keep the ypos in the center
            self.ypos = config.screen_height//2

        def event(self, ev, event_x, event_y, st):

            ## All we're doing is checking if they're swiping the image away
            child = self.current_image

            # Too zoomed in
            if ((child.zoom > child.fit_screen_zoom_level)
                # Or trying to zoom
                or len(child.fingers) > 1
                or ev.type == pygame.MULTIGESTURE
                or renpy.map_event(ev, "viewport_wheelup")
                or renpy.map_event(ev, "viewport_wheeldown")
            ):
                self.viewing_child = True
                return self.current_image.event(ev, event_x, event_y, st)

            if self.viewing_child:
                self.viewing_child = False
                # Reset positioning
                self.reset_values()

            self.text = ""

            # Otherwise, yes, they can drag it. The parent will take over the
            # touch events.
            if ev.type in (pygame.FINGERDOWN, pygame.FINGERMOTION, pygame.FINGERUP):
                x, y = self.normalize_pos(ev.x, ev.y)
            else:
                x = event_x
                y = event_y

            xadj_x = int(x - self.padding//2)
            yadj_y = int(y - self.padding//2)

            start_zoom = self.zoom

            if self.drag_finger is not None:
                # Dragging
                old_xvalue = self.xadjustment.value
                old_yvalue = self.yadjustment.value

                oldx, oldy = self.drag_position # type: ignore
                dx = xadj_x - oldx
                dy = yadj_y - oldy

                dt = st - self.drag_position_time
                if dt > 0:
                    old_xspeed, old_yspeed = self.drag_speed
                    new_xspeed = -dx / dt / 60

                    done = min(1.0, dt / (1 / 60))

                    new_xspeed = old_xspeed + done * (new_xspeed - old_xspeed)
                    new_yspeed = 0.0

                    self.drag_speed = (new_xspeed, new_yspeed)

                    debug_log(f"Old speed: ({old_xspeed:.2f})\nNew speed ({new_xspeed:.2f})")

                    if (0.05 > new_xspeed > -0.05):
                        ## Check if we're just slowing down overall
                        if (0.09 > old_xspeed > -0.09):
                            debug_log("Slowing down")
                        else:
                            self.stationary_drag_counter += 1
                            debug_log("Increasing stationary counter:", self.stationary_drag_counter, color="blue")
                            if self.stationary_drag_counter < 4 and dt < 0.1:
                                # Don't update it yet
                                # But do correct the speed direction
                                debug_log(f"Reusing old speed ({old_xspeed:.2f})")
                                if ((new_xspeed > 0 and old_xspeed < 0)
                                        or (new_xspeed < 0 and old_xspeed > 0)):
                                    adjusted_xspeed = old_xspeed * -1.0
                                else:
                                    adjusted_xspeed = old_xspeed
                                adjusted_yspeed = 0.0

                                #debug_log(f"Adjusted old speed is ({adjusted_xspeed:.2f}, {adjusted_yspeed:.2f}) vs ({new_xspeed:.2f}, {new_yspeed:.2f})")
                                self.drag_speed = (adjusted_xspeed, adjusted_yspeed)
                                debug_log(f"Popping last speed {self.drag_finger.last_speed}")
                                self.drag_speed = self.drag_finger.last_speed
                    else:
                        self.stationary_drag_counter = 0
                        self.drag_finger.add_speed(self.drag_speed)

            if self.touch_down_event(ev):
                finger = self.register_finger(x, y)

                if self.drag_finger is None and len(self.fingers) == 1:
                    debug_log(f"Drag DOWN at ({x}, {y})", color="green")
                    # Inertia
                    self.drag_position = (xadj_x, yadj_y)
                    self.drag_position_time = st
                    self.drag_speed = (0.0, 0.0)

                    self.xadjustment.end_animation(instantly=True)
                    self.yadjustment.end_animation(instantly=True)

                    # Normal
                    self.calculate_drag_offset(x, y)
                    self.update_image_pos(x, y)
                    self.drag_finger = finger

                elif self.drag_finger and len(self.fingers) > 1:
                    debug_log(f"Finger DOWN at ({x}, {y})", color="green")
                    # More than one finger; turn off dragging
                    # self.update_image_pos(self.drag_finger.x, self.drag_finger.y)
                    self.drag_offset = (0, 0)
                    self.drag_finger = None

                    self.xadjustment.end_animation(instantly=True)
                    self.yadjustment.end_animation(instantly=True)

            elif self.touch_up_event(ev):
                finger = self.remove_finger(x, y)

                if finger and self.drag_finger is finger:
                    debug_log(f"Drag UP at ({x}, {y})\nStarted at ({finger.touchdown_x}, {finger.touchdown_y})", color="red")
                    self.drag_finger = None
                    self.drag_offset = (0, 0)

                    ## Inertia
                    xspeed, yspeed = self.drag_speed

                    if xspeed and myconfig.viewport_inertia_amplitude:
                        self.xadjustment.inertia(
                            myconfig.viewport_inertia_amplitude * xspeed,
                                myconfig.viewport_inertia_time_constant, st)
                    else:
                        xvalue = self.xadjustment.round_value(old_xvalue, release=True)
                        self.xadjustment.change(xvalue)

                    self.drag_position = None
                    self.drag_position_time = None
                else:
                    if finger is None:
                        debug_log(f"Finger UP at ({x}, {y}) but couldn't actually find it in self.fingers", color="red")
                    else:
                        debug_log(f"Finger UP at ({x}, {y})\nStarted at ({finger.touchdown_x}, {finger.touchdown_y})", color="red")

            elif ev.type in (pygame.FINGERMOTION, pygame.MOUSEMOTION):
                finger = self.update_finger(x, y)
                if finger is not None and finger is self.drag_finger:
                    # They are dragging the image around
                    self.update_image_pos(x, y)

                    ## Inertia
                    new_xvalue = self.xadjustment.round_value(old_xvalue - dx,
                        release=False)
                    if old_xvalue == new_xvalue:
                        newx = oldx
                    else:
                        self.xadjustment.change(new_xvalue)
                        newx = xadj_x

                    newy = self.yadjustment.value

                    self.drag_position = (newx, newy) # W0201
                    self.drag_position_time = st


            self.clamp_pos()
            self.update_adjustments()

            if self.fingers:
                self.text += '\n'.join([x.finger_info for x in self.fingers])
            else:
                self.text = "No fingers recognized"

            self.text += "\nPos: ({}, {})".format(self.xpos, self.ypos)
            self.text += "\nAnchor: {}".format(self.anchor)
            self.text += "\nxadjustment: {}/{}".format(self.xadjustment.value, self.xadjustment.range)
            self.text += "\nyadjustment: {}/{}".format(self.yadjustment.value, self.yadjustment.range)
            self.text += "\ndrag_speed: ({:.2f}, {:.2f})".format(self.drag_speed[0], self.drag_speed[1])

            # raise renpy.IgnoreEvent()



    def debug_log(*args, color=None):
        ret = ' '.join([str(arg) for arg in args])
        ret += "\n"
        if color is not None:
            if color == "red":
                color = "#860c0c"
            elif color == "blue":
                color = "#121277"
            elif color == "green":
                color = "#0a630a"
            else:
                color = "#000"
            ret = "{{b}}{{color={}}}{}{{/color}}{{/b}}".format(color, ret)

        debug_record.append(ret)
        if len(debug_record) > 100:
            debug_record.pop(0)

    class ViewGallery(Action):
        def __init__(self, gallery, image_name=None):
            self.gallery = gallery
            self.image_name = image_name
        def get_sensitive(self):
            if self.image_name is None:
                return True
            else:
                return self.gallery.is_viewable(self.image_name)
        def __call__(self):
            self.gallery.set_up_gallery(self.image_name)
            renpy.run(Show(self.gallery.screen))

default debug_record = [ ]

style multitouch_text:
    color "#fff"
    size 35
    outlines [ (1, "#000", 0, 0)]

default multi_touch = MultiTouch("Profile Pics/Zen/zen-10-b.webp", 314, 314)
#default cg_zoom = ZoomGalleryImage("CGs/ju_album/cg-1.webp", 750, 1334)
default cg_zoom = ZoomGalleryDisplayable("jellyfish.jpg", 1920, 2880)
default cg_zoom2 = ZoomGalleryDisplayable("flowers.jpg", 1920, 2560)
default cg_zoom3 = ZoomGalleryDisplayable("vase.jpg", 1920, 2560)
default cg_zoom4 = ZoomGalleryDisplayable("city.jpg", 1920, 1200)

default zoom_gallery = ZoomGallery(
    ZoomGalleryImage("jellyfish", "jellyfish.jpg", 1920, 2880),
    ZoomGalleryImage("flowers", "flowers.jpg", 1920, 2560, condition="flowers_unlocked"),
    ZoomGalleryImage("vase", "vase.jpg", 1920, 2560),
    ZoomGalleryImage("city", "city.jpg", 1920, 1200),
    screen="use_zoom_gallery"
)
default flowers_unlocked = False

screen multitouch_test():
    modal True

    use starry_night()

    vbox:
        align (0.5, 0.5)
        spacing 100
        hbox:
            align (0.5, 0.5)
            spacing 40
            textbutton "Jellyfish" action ViewGallery(zoom_gallery, "jellyfish")
            textbutton "Flowers" action ViewGallery(zoom_gallery, "flowers")
            textbutton "Vase" action ViewGallery(zoom_gallery, "vase")
            textbutton "City" action ViewGallery(zoom_gallery, "city")
        hbox:
            align (0.5, 0.5)
            spacing 40
            textbutton "Unlock flowers" action ToggleVariable("flowers_unlocked")


    frame:
        align (1.0, 1.0)
        modal True
        has vbox
        textbutton "Return" action Hide()

screen use_zoom_gallery():

    modal True

    default show_log = False

    add "#f0f3"

    add zoom_gallery

    if show_log:
        dismiss action ToggleScreenVariable("show_log")
        frame:
            xysize (720, 1000)
            background "#fff"
            viewport:
                draggable True
                yinitial 1.0
                scrollbars "vertical"
                mousewheel True
                has vbox
                xpos 25
                for entry in debug_record:
                    text entry size 20
                null height 25

    frame:
        align (1.0, 1.0)
        modal True
        has vbox
        textbutton "Show Debug" action ToggleScreenVariable("show_log")
        textbutton "Return" action Hide()

screen multitouch_test_working():

    default show_log = False

    modal True

    use starry_night()

    add cg_zoom

    if show_log:
        dismiss action ToggleScreenVariable("show_log")
        frame:
            xysize (720, 1000)
            background "#fff"
            viewport:
                draggable True
                yinitial 1.0
                scrollbars "vertical"
                mousewheel True
                has vbox
                xpos 25
                for entry in debug_record:
                    text entry size 20
                null height 25

    frame:
        align (1.0, 1.0)
        modal True
        has vbox
        spacing 20
        textbutton "Touch version" action ToggleField(cg_zoom, 'touch_screen_mode')
        if not cg_zoom.touch_screen_mode:
            textbutton "Wheel Zoom" action ToggleField(cg_zoom, 'wheel_zoom')
        textbutton "Show Debug" action ToggleScreenVariable("show_log")
        textbutton "Return" action Hide('multitouch_test')

screen original_touch_test():
    add multi_touch

    vbox:
        align (1.0, 1.0) spacing 20
        textbutton "Touch version" action ToggleField(multi_touch, 'touch_screen_mode')
        if not multi_touch.touch_screen_mode:
            textbutton "Wheel Zoom" action ToggleField(multi_touch, 'wheel_zoom')
        textbutton "Return" action Hide('multitouch_test')
