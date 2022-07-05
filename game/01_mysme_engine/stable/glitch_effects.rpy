## This code has been modified from effects.rpy
## from the Ren'Py game Doki Doki Literature Club

init python:

    import random

    ## Screen cap the current screen; used by multiple functions
    def screenshot_srf():
        srf = renpy.display.draw.screenshot(None)#, False)
        s_w, s_h = renpy.get_physical_size()
        if srf.get_width != s_w: srf = renpy.display.scale.smoothscale(srf,
                                                                (s_w, s_h))
        return srf

    ## Invert the colors of the current screen.
    def invert():
        srf = screenshot_srf()
        inv = (renpy.Render(srf.get_width(),
                srf.get_height()).canvas().get_surface())
        inv.fill((255,255,255,255))
        inv.blit(srf, (0,0), None, 2)
        return inv

    ## This defines a displayable for the inverted screen
    class Invert(renpy.Displayable):
        def __init__(self, delay=0.0, screenshot_delay=0.0):
            super(Invert, self).__init__()
            self.width, self.height = renpy.get_physical_size()
            self.height = int(self.width * 16 // 9)
            self.srf = invert()
            self.delay = delay

        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)
            if st >= self.delay:
                render.blit(self.srf, (0, 0))
            return render

## Define the invert screen for renpy
screen invert(w_timer=False):
    add Invert() size (config.screen_width, config.screen_height)
    if w_timer:
        timer w_timer action Hide("invert")

## tear(number=10, offtimeMult=1, ontimeMult=1,
##      offsetMin=0, offsetMax=50, srf=None)
## This screen is called using a statement like
## `show screen tear(20, 0.1, 0.1, 0, 40)`
## Cut the screen up into some number of pieces and
## make them offset from each other at random.

## Define some python stuff
init python:

    class BasicScreenshot(renpy.Displayable):
        """
        A class which takes a screenshot of the current screen and
        returns it as a render.

        Attributes:
        -----------
        screenshot : Surface or Displayable
            A screenshot of the currently displaying screen.
        width : int
            The width of the screenshot.
        height : int
            The height of the screenshot.
        pieces : TearPiece[]
            A list of TearPiece objects representing tears in this screenshot.
            Optional.
        """

        def __init__(self, img=None, width=None, height=None,
                create_tears=False, *args, **kwargs):
            super(BasicScreenshot, self).__init__()

            if img is None:
                # Take a screenshot
                self.screenshot = renpy.display.draw.screenshot(None)
                s_w, s_h = renpy.get_physical_size()
                self.width = int(s_w)
                self.height = int(s_h)
                self.has_screenshot = True
            else:
                self.screenshot = renpy.easy.displayable(img)
                self.width = width or config.screen_width
                self.height = height or config.screen_height
                self.has_screenshot = False

            if create_tears:
                self.create_tears(*args, **kwargs)
            else:
                self.pieces = [ ]

        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)
            if self.has_screenshot:
                render.blit(self.screenshot, (0, 0))
            else:
                r = renpy.render(self.screenshot, self.width, self.height, st, at)
                render.blit(r, (0, 0))
            return render

        def create_tears(self, num_pieces=10, xoffset_min=-10, xoffset_max=10,
                idle_len_multiplier=1.0, move_len_multiplier=1.0):
            """
            Parameters:
            -----------
            num_pieces : int
                The number of pieces the screen should be torn into.
            xoffset_min : int
                The leftmost offset an offset piece can have.
            xoffset_max : int
                The rightmost offset an offset piece can have.
            idle_len_multiplier : float
                A multiplier for the length of time the image stays in its "idle"
                state, where the piece is not offset from its original position.
            move_len_multiplier : float
                A multiplier for the length of time the image is moving around
                the screen offset from its original position for.
            """

            self.pieces = []
            tear_points = [0, self.height]

            for i in range(num_pieces):
                tear_points.append(random.randint(10, self.height - 10))
            tear_points.sort()
            for i in range(num_pieces+1):
                self.pieces.append(TearPiece(tear_points[i], tear_points[i+1],
                                idle_len_multiplier, move_len_multiplier,
                                xoffset_min, xoffset_max))

        def update_pieces(self, st):
            """Update the position of all tear pieces."""
            for piece in self.pieces:
                piece.update(st)

        def get_composite(self):
            """
            Return a composite image of this screenshot along with
            all its tear pieces.
            """
            comp = [ (self.width, self.height) ]
            for piece in self.pieces:
                comp.extend(piece.get_piece(self))
            return Composite(*comp)

    def create_torn_screen(st, at, screenshot):
        screenshot.update_pieces(st)
        return screenshot.get_composite(), 0.0

    ## This class defines the little blinking pieces of the screen tear effect
    class TearPiece():
        """
        A class which defines the coordinates of a torn image.
        """
        def __init__(self, start_y, end_y, idle_len_multiplier,
                    move_len_multiplier, xoffset_min, xoffset_max):
            self.start_y = start_y
            self.end_y = end_y
            self.idle_time = (random.random() * 0.2 + 0.2) * idle_len_multiplier
            self.move_time = (random.random() * 0.2 + 0.2) * move_len_multiplier
            self.offset = 0
            self.xoffset_min = xoffset_min
            self.xoffset_max = xoffset_max

        def update(self, st):
            """Update the offset of this piece."""
            st = st % (self.idle_time + self.move_time)
            if st > self.idle_time and self.offset == 0:
                self.offset = random.randint(self.xoffset_min, self.xoffset_max)
            elif st <= self.idle_time and self.offset != 0:
                self.offset = 0

        def get_piece(self, img):
            the_crop = Crop(
                (0, max(0, self.start_y - 1),
                config.screen_width, max(0, self.end_y - self.start_y)),
                img)

            the_pos = (self.offset, self.start_y)
            return [the_pos, the_crop]

    ## This class defines a renpy displayable made up of `number`
    ## of screen tear sections, that bounce back and forth, based
    ## on ontimeMult & offtimeMult and each piece is randomly offset
    ## by an amount between offsetMin & offsetMax
    class Tear(renpy.Displayable):
        def __init__(self, number, offtimeMult, ontimeMult,
                        offsetMin, offsetMax, srf=None):
            super(Tear, self).__init__()
            self.width, self.height = renpy.get_physical_size()
            self.width = int(self.width)
            self.height = int(self.height)
            print_file("1")
            # Force screen to 9:16 ratio
            if float(self.width) / float(self.height) > 9.0/16.0:
                self.width = int(self.height * 9 // 16)
            else:
                self.height = int(self.width * 16 // 9)
            print_file("2")
            self.number = number
            # Use a special image if specified, or tear
            # current screen by default
            if not srf: self.srf = screenshot_srf()
            else: self.srf = srf
            print_file("3")

            # Rip the screen into `number` pieces
            self.pieces = []
            tearpoints = [0, self.height]
            print_file("4")
            for i in range(number):
                tearpoints.append(random.randint(10, self.height - 10))
            print_file("5")
            tearpoints.sort()
            for i in range(number+1):
                self.pieces.append(TearPiece(tearpoints[i],
                                    tearpoints[i+1], offtimeMult,
                                    ontimeMult, offsetMin, offsetMax))
            print_file("6")

        ## Render the displayable
        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)
            print_file("7")
            render.blit(self.srf, (0,0))
            print_file("8")
            # Render each piece
            for piece in self.pieces:
                print_file("9")
                piece.update(st)
                subsrf = (self.srf.subsurface((0,
                            max(0, piece.start_y - 1),
                            self.width,
                            max(0, piece.end_y - piece.start_y))))
                            #.pygame_surface()
                render.blit(subsrf, (piece.offset, piece.start_y))
            print_file("10")
            renpy.redraw(self, 10)
            print_file("11")
            return render

## Define the screen for Ren'Py; by default, tear the screen into 10 pieces
screen tear(number=10, offtimeMult=1, ontimeMult=1, offsetMin=0,
                            offsetMax=50, w_timer=False, srf=None):
    zorder 150 #Screen tear appears above pretty much everything

    add Tear(number, offtimeMult, ontimeMult, offsetMin,
                                offsetMax, srf) size (config.screen_width,config.screen_height)
    if w_timer:
        timer w_timer action Hide('tear')

screen tear2(num_pieces=10, xoffset_min=-10, xoffset_max=10,
            idle_len_multiplier=1.0, move_len_multiplier=1.0,
            img=None, width=None, height=None, w_timer=False):
    zorder 150

    default screen_sh = BasicScreenshot(img, width, height, create_tears=True,
            num_pieces=num_pieces, xoffset_min=xoffset_min,
            xoffset_max=xoffset_max, idle_len_multiplier=idle_len_multiplier,
            move_len_multiplier=move_len_multiplier)

    add DynamicDisplayable(create_torn_screen, screenshot=screen_sh):
        xysize (width or config.screen_width, height or config.screen_height)
        align (0.5, 0.5)

    if w_timer:
        timer w_timer action Hide('tear2')

## This screen provides additional "hacking" white lines
## across the screen
screen white_squares(w_timer=False):
    zorder 151
    add 'hacked_white_squares'
    if w_timer:
        timer w_timer action Hide('white_squares')


########## rectstatic
# These are three displayables (m_rectstatic, m_rectstatic2, m_rectstatic3)
# and one displayable effect RectStatic() that make a bunch of little
# boxes on the screen that blink on and off.

# Little black squares
image m_rectstatic:
    RectStatic(Solid("#000"), 32, False, False).sm
    # RectStatic(Crop((0,0,renpy.random.randint(20, 60),
    #                     renpy.random.randint(20, 40)), 'hack_long'), 32).sm
    pos (0, 0)
    size (32,32)
# Little squares with a part of the logo
image m_rectstatic2:
    RectStatic(Transform(Crop((0,0,32,32),
                        "chat_selected", size=(32,32))), 2).sm
    size (32, 32)
# Little squares with a part of the menu
image m_rectstatic3:
    RectStatic(Transform(Crop((0,0,64,64),
                        "day_selected", size=(32, 32))), 2).sm
    size (32, 32)

init python:
    import math
    ## This effect takes a displayable, a number of rectangles
    ## to show concurrently, and a size for the rectangles, then
    ## makes them randomly show up on the screen
    ## RectStatic(Solid("#000"), 32, 32, 32) would make 32 32x32 black squares
    ## That show up randomly on the screen
    class RectStatic(object):
        def __init__(self, theDisplayable, numRects=12, rectWidth = False,
                        rectHeight = False):
            self.sm = SpriteManager(update=self.update)
            self.rects = [ ]
            self.timers = [ ]
            self.displayable = theDisplayable
            self.numRects = numRects
            if not rectWidth:
                self.rectWidth = renpy.random.randint(4, 60)
                self.is_random = True
            else:
                self.rectWidth = rectWidth
                self.is_random = False
            if not rectHeight:
                self.rectHeight = renpy.random.randint(4, 60)
                self.is_random = True
            else:
                self.rectHeight = rectHeight
                self.is_random = False

            # Make copies of the displayables
            for i in range(self.numRects):
                self.add(self.displayable)
                self.timers.append(random.random() * 0.4 + 0.1)

        # Rectangles show up on a grid
        def add(self, d):
            s = self.sm.create(d)
            s.x = random.randint(0, 23) * 32
            s.y = random.randint(0, 41) * 32
            if not self.is_random:
                s.width = self.rectWidth
                s.height = self.rectHeight
            else:
                s.width = renpy.random.randint(4, 60)
                s.height = renpy.random.randint(4, 60)
            self.rects.append(s)

        def update(self, st):
            for i, s in enumerate(self.rects):
                if st >= self.timers[i]:
                    s.x = random.randint(0, 23) * 32
                    s.y = random.randint(0, 41) * 32
                    self.timers[i] = st + random.random() * 0.4 + 0.1
            return 0

## Screen to show the static rectangles
screen hack_rectangle(w_timer=False):
    zorder 150
    add 'm_rectstatic'
    add 'm_rectstatic2'
    add 'm_rectstatic3'
    if w_timer:
        timer w_timer action Hide('hack_rectangle')

## Screen to more easily display images
screen display_img(img_list, force_show=False):
    zorder 10
    if persistent.hacking_effects or force_show:
        for img in img_list:
            add img[0] xpos img[1] ypos img[2]

