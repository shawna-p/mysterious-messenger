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

            self.xpos = config.screen_width//2
            self.ypos = config.screen_height//2

            self.anchor = (config.screen_width//2, config.screen_height//2)

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

            dimensions = self.get_dimensions()

            the_img = Transform(self.img,
                xysize=dimensions,
                rotate=int(self.rotate),
                anchor=(0.5, 0.5),
                pos=(self.xpos, self.ypos))

            anchor = Transform("#f008", xysize=(7, 7), anchor=(0.5, 0.5), pos=(int(self.anchor[0]), int(self.anchor[1])))

            text = Text(self.text, style='multitouch_text')

            fix = Fixed(
                the_img, text, anchor,
                xysize=(config.screen_width, config.screen_height),
            )

            ren = renpy.render(fix, width, height, st, at)
            r.blit(ren, (0, 0))

            renpy.redraw(self, 0)

            return r

        @property
        def left_corner(self):
            """Return the coordinates of the padded top-left corner of the image."""
            # Currently, the xpos/ypos are indicating the center of the image
            padding = self.get_padding()
            return (self.xpos - padding//2, self.ypos - padding//2)

        def get_xypadding(self):

            dimensions = self.get_dimensions()
            padding = self.get_padding(dimensions)
            xpadding = (padding - dimensions[0])//2
            ypadding = (padding - dimensions[1])//2
            return (xpadding, ypadding)

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

        def update_image_pos(self, x=None, y=None):
            """
            The player has dragged their finger to point (x, y), and the
            drag itself is supposed to come along with it.
            """

            if x is not None and y is not None:

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

            start_zoom = self.zoom

            if self.touch_down_event(ev):
                finger = self.register_finger(x, y)
                if self.drag_finger is None and len(self.fingers) == 1:
                    self.calculate_drag_offset(x, y)
                    self.update_image_pos(x, y)
                    self.drag_finger = finger
                elif self.drag_finger and len(self.fingers) > 1:
                    # More than one finger; turn off dragging
                    # self.update_image_pos(self.drag_finger.x, self.drag_finger.y)
                    self.drag_offset = (0, 0)
                    self.drag_finger = None

            elif self.touch_up_event(ev):
                finger = self.remove_finger(x, y)
                if finger and self.drag_finger is finger:
                    self.drag_finger = None
                    self.drag_offset = (0, 0)
                if finger and len(self.fingers) == 1:
                    new_drag_finger = self.fingers[0]
                    self.calculate_drag_offset(new_drag_finger.x, new_drag_finger.y)
                    self.update_image_pos(new_drag_finger.x, new_drag_finger.y)
                    self.drag_finger = new_drag_finger

            elif not self.touch_screen_mode and renpy.map_event(ev, 'mouseup_3'):
                # Right mouse click; set the anchor
                self.anchor = (x, y)

            elif ev.type in (pygame.FINGERMOTION, pygame.MOUSEMOTION):
                finger = self.update_finger(x, y)
                if finger is not None and finger is self.drag_finger:
                    # They are dragging the image around
                    self.update_image_pos(x, y)

            elif ev.type == pygame.MULTIGESTURE:
                self.rotate += ev.dTheta*360/8
                self.zoom += ev.dDist*15

                ## Set the anchor as the middle between their two fingers
                self.update_anchor()

            elif renpy.map_event(ev, "viewport_wheelup"):
                if self.wheel_zoom:
                    self.zoom += 0.05 #0.25
                else:
                    self.rotate += 10

            elif renpy.map_event(ev, "viewport_wheeldown"):
                if self.wheel_zoom:
                    self.zoom -= 0.25
                else:
                    self.rotate -= 10

            self.clamp_rotate()
            self.clamp_zoom()
            self.adjust_pos_for_zoom(start_zoom)
            self.clamp_pos()


            if self.fingers:
                self.text += '\n'.join([x.finger_info for x in self.fingers])
            else:
                self.text = "No fingers recognized"

            self.text += "\nPos: ({}, {})".format(self.xpos, self.ypos)
            self.text += "\nAnchor: {}".format(self.anchor)



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

    class GalleryZoom(MultiTouch):
        """
        A class which allows zooming in on full-screen gallery images.
        """
        def __init__(self, img, width, height, zoom_max=4.0, *args, **kwargs):
            ## Calculate zoom_min. It should always fill the screen in one
            ## dimension
            min_width_ratio = config.screen_width / float(width)
            min_height_ratio = config.screen_height / float(height)
            min_ratio = max(min_width_ratio, min_height_ratio)

            super(GalleryZoom, self).__init__(img, width, height, min_ratio,
                zoom_max, rotate_degrees=0, *args, **kwargs)

        def clamp_pos(self):

            ## Clamp
            ## For the xpos: the minimum it can be will put the right edge
            ## against the right side of the screen
            ## So, how far is that?
            dimensions = self.get_dimensions()
            padding = self.get_padding(dimensions)

            xpadding = (padding - dimensions[0])//2
            ypadding = (padding - dimensions[1])//2

            ## When the image is against the right side, the left side will
            ## be at -(padding-screen_width) + xpadding
            xmin = (padding-xpadding-config.screen_width)*-1 + padding//2
            self.xpos = max(self.xpos, xmin)
            ## When the image is against the left side, the right side will
            ## be at -xpadding
            self.xpos = min(self.xpos, -xpadding+padding//2)

            ymin = (padding-ypadding-config.screen_height)*-1 + padding//2
            self.ypos = max(self.ypos, ymin)
            self.ypos = min(self.ypos, -ypadding+padding//2)


style multitouch_text:
    color "#fff"
    size 35
    outlines [ (1, "#000", 0, 0)]

default multi_touch = MultiTouch("Profile Pics/Zen/zen-10-b.webp", 314, 314)
default cg_zoom = GalleryZoom("CGs/ju_album/cg-1.webp", 750, 1334)
screen multitouch_test():

    modal True

    use starry_night()

    add cg_zoom

    vbox:
        align (1.0, 1.0) spacing 20
        textbutton "Touch version" action ToggleField(cg_zoom, 'touch_screen_mode')
        if not cg_zoom.touch_screen_mode:
            textbutton "Wheel Zoom" action ToggleField(cg_zoom, 'wheel_zoom')
        textbutton "Return" action Hide('multitouch_test')

screen original_touch_test():
    add multi_touch

    vbox:
        align (1.0, 1.0) spacing 20
        textbutton "Touch version" action ToggleField(multi_touch, 'touch_screen_mode')
        if not multi_touch.touch_screen_mode:
            textbutton "Wheel Zoom" action ToggleField(multi_touch, 'wheel_zoom')
        textbutton "Return" action Hide('multitouch_test')
