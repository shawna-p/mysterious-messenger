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
        @property
        def x_int(self):
            return int(self.x*config.screen_width)
        @property
        def y_int(self):
            return int(self.y*config.screen_height)

        def dist(self, x, y):
            """Return the distance from this finger to the given coordinates."""

            dx = self.x - x
            dy = self.y - y

            return (dx**2 + dy**2)**0.5

        def finger_info(self):
            return "Finger: ({}, {})".format(self.x_int, self.y_int)

    class MultiTouch(renpy.Displayable):

        square_dimensions = 314

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.text = ""
            self.zoom = 1.0
            self.rotate = 0

            self.fingers = [ ]

        def render(self, width, height, st, at):

            r = renpy.Render(width, height)

            square_width = int(self.square_dimensions*self.zoom)
            square_size = int((square_width**2+square_width**2)**0.5)

            square_pos = (config.screen_width//2-square_size//2,
                        config.screen_height//2-square_size//2)
            square = Transform("Profile Pics/Zen/zen-10-b.webp",
                xysize=(square_width, square_width),
                rotate=self.rotate,
                #anchor=(0.5, 0.5),
                pos=square_pos)

            # ren = renpy.render(Transform("#f0f8",
            #     xysize=(square_width, square_width),
            #     rotate=self.rotate,
            #     anchor=(0.5, 0.5)), width, height, st, at)
            # r.blit(ren, (config.screen_width//2-square_size//2,
            #             config.screen_height//2-square_size//2))

            text = Text(self.text, style='multitouch_text')

            fix = Fixed(
                square, text,
                xysize=(config.screen_width, config.screen_height),
            )

            ren = renpy.render(fix, width, height, st, at)
            r.blit(ren, (0, 0))

            renpy.redraw(self, 0)

            return r

        def normalize_pos(self, x, y):
            return (int(x*config.screen_width), int(y*config.screen_height))

        def register_finger(self, x, y):
            self.fingers.append(Finger(x, y))

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

        def remove_finger(self, x, y):
            finger = self.find_finger(x, y)
            if not finger:
                return
            self.fingers.remove(finger)

        def event(self, ev, x, y, st):

            if ev.type == pygame.FINGERMOTION:
                self.text = "Finger motion"
                self.update_finger(ev.x, ev.y)
            elif ev.type == pygame.FINGERDOWN:
                self.text = "Finger down"
                self.register_finger(ev.x, ev.y)
            elif ev.type == pygame.FINGERUP:
                self.text = "Finger up"
                self.remove_finger(ev.x, ev.y)
            elif ev.type == pygame.MULTIGESTURE:
                self.text = "Multigesture"

                self.rotate += int(ev.dTheta*360)
                self.zoom += ev.dDist*15
            elif renpy.map_event(ev, "viewport_wheelup"):
                if store.wheel_zoom:
                    self.zoom += 0.25
                else:
                    self.rotate += 10
            elif renpy.map_event(ev, "viewport_wheeldown"):
                if store.wheel_zoom:
                    self.zoom -= 0.25
                else:
                    self.rotate -= 10
            else:
                self.text = "Not recognized"

            self.zoom = min(max(0.25, self.zoom), 4.0)
            # self.rotate %= 360

            if self.fingers:
                self.text = '\n'.join([x.finger_info for x in self.fingers])
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

default multi_touch = MultiTouch()
default wheel_zoom = True
screen multitouch_test():

    modal True

    use starry_night()

    add multi_touch

    vbox:
        align (1.0, 1.0) spacing 20
        textbutton "Wheel Zoom" action ToggleVariable('wheel_zoom')
        textbutton "Return" action Hide('multitouch_test')
