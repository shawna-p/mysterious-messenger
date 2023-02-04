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

        def dist(self, x, y):
            """Return the distance from this finger to the given coordinates."""

            dx = self.x - x
            dy = self.y - y

            return (dx**2 + dy**2)**0.5

        @property
        def finger_info(self):
            return "Finger: ({}, {})".format(self.x, self.y)

    class MultiTouch(renpy.Displayable):

        def __init__(self, img, width, height, zoom_min=0.25, zoom_max=4.0,
                rotate_degrees=360, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.img = img
            self.width = width
            self.height = height
            self.text = ""
            self.zoom = 1.0
            self.rotate = 0
            self.xpos = 0
            self.ypos = 0

            self.zoom_max = zoom_max
            self.zoom_min = zoom_min
            self.rotate_degrees = rotate_degrees

            self.touch_screen_mode = renpy.variant("touch")
            self.wheel_zoom = True

            self.drag_finger = None
            self.drag_offset = (0, 0)

            self.fingers = [ ]

        def clamp_zoom(self):
            self.zoom = min(max(self.zoom, self.zoom_min), self.zoom_max)

        def clamp_rotate(self):

            self.rotate %= 360
            self.rotate = min(max(self.rotate, -self.rotate_degrees), self.rotate_degrees)

        def render(self, width, height, st, at):

            r = renpy.Render(width, height)

            dimensions = self.update_image_pos()

            the_img = Transform(self.img,
                xysize=dimensions,
                rotate=int(self.rotate),
                pos=(self.xpos, self.ypos))

            text = Text(self.text, style='multitouch_text')

            fix = Fixed(
                the_img, text,
                xysize=(config.screen_width, config.screen_height),
            )

            ren = renpy.render(fix, width, height, st, at)
            r.blit(ren, (0, 0))

            renpy.redraw(self, 0)

            return r

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

        def start_drag(self, x, y, finger):
            finger_touch_pos = (x, y)

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

            dx = x - self.xpos
            dy = y - self.ypos
            self.drag_offset = (dx, dy)

        def get_dimensions(self):
            return (int(self.width*self.zoom), int(self.height*self.zoom))

        def update_image_pos(self, x=None, y=None):
            """
            The player has dragged their finger to point (x, y), and the
            drag itself is supposed to come along with it.
            """

            dimensions = self.get_dimensions()
            padded_size = int((dimensions[0]**2+dimensions[1]**2)**0.5)

            if self.drag_finger is None:

                self.xpos = config.screen_width//2-padded_size//2
                self.ypos = config.screen_height//2-padded_size//2

            elif x is not None and y is not None:

                self.xpos = int(x - self.drag_offset[0])
                self.ypos = int(y - self.drag_offset[1])

            return dimensions

        def event(self, ev, event_x, event_y, st):
            self.text = ""

            if ev.type in (pygame.FINGERDOWN, pygame.FINGERMOTION, pygame.FINGERUP):
                x, y = self.normalize_pos(ev.x, ev.y)
            else:
                x = event_x
                y = event_y

            if self.touch_down_event(ev):
                finger = self.register_finger(x, y)
                if self.drag_finger is None and len(self.fingers) == 1:
                    self.calculate_drag_offset(x, y)
                    self.drag_finger = finger
                elif len(self.fingers) > 1:
                    # More than one finger; no dragging
                    self.drag_offset = (0, 0)
                    self.drag_finger = None

            elif self.touch_up_event(ev):
                finger = self.remove_finger(x, y)
                if finger and self.drag_finger == finger:
                    self.drag_finger = None
                    self.drag_offset = (0, 0)

            elif ev.type in (pygame.FINGERMOTION, pygame.MOUSEMOTION):
                finger = self.update_finger(x, y)
                if finger is not None and finger is self.drag_finger:
                    # They are dragging the image around
                    self.update_image_pos(x, y)

            elif ev.type == pygame.MULTIGESTURE:
                self.rotate += ev.dTheta*360/8
                self.zoom += ev.dDist*15

            elif renpy.map_event(ev, "viewport_wheelup"):
                if self.wheel_zoom:
                    self.zoom += 0.25
                else:
                    self.rotate += 10

            elif renpy.map_event(ev, "viewport_wheeldown"):
                if self.wheel_zoom:
                    self.zoom -= 0.25
                else:
                    self.rotate -= 10

            self.clamp_rotate()
            self.clamp_zoom()

            if self.fingers:
                self.text += '\n'.join([x.finger_info for x in self.fingers])
            else:
                self.text = "No fingers recognized"

            ## Results:
            ## FINGER MOVEMENT:
            ## touchId = 131151
            ## fingerId = numbers from 186-193, goes up while moving?
            ## x = float between 0 and 1
            ## y = float between 0 and 1
            ##
            ## MULTIGESTURE:
            ## touchId = 131151
            ## dTheta = Very tiny negative number ~0.002
            ## dDist = Veery tiny number 0.0005
            ## x/y = float between 0 and 1
            ## numFingers = 2

style multitouch_text:
    color "#fff"
    size 35

default multi_touch = MultiTouch("Profile Pics/Zen/zen-10-b.webp", 314, 314)
screen multitouch_test():

    modal True

    use starry_night()

    add multi_touch

    vbox:
        align (1.0, 1.0) spacing 20
        textbutton "Touch version" action ToggleField(multi_touch, 'touch_screen_mode')
        if not multi_touch.touch_screen_mode:
            textbutton "Wheel Zoom" action ToggleField(multi_touch, 'wheel_zoom')
        textbutton "Return" action Hide('multitouch_test')
