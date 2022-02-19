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
            self.height = self.width * 16 / 9
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
    ## This class defines the little blinking pieces of the screen tear effect
    class TearPiece:
        def __init__(self, startY, endY, offtimeMult, ontimeMult,
                        offsetMin, offsetMax):
            self.startY = startY
            self.endY = endY
            self.offTime = (random.random() * 0.2 + 0.2) * offtimeMult
            self.onTime = (random.random() * 0.2 + 0.2) * ontimeMult
            self.offset = 0
            self.offsetMin = offsetMin
            self.offsetMax = offsetMax

        def update(self, st):
            st = st % (self.offTime + self.onTime)
            if st > self.offTime and self.offset == 0:
                self.offset = random.randint(self.offsetMin, self.offsetMax)
            elif st <= self.offTime and self.offset != 0:
                self.offset = 0

    ## This class defines a renpy displayable made up of `number`
    ## of screen tear sections, that bounce back and forth, based
    ## on ontimeMult & offtimeMult and each piece is randomly offset
    ## by an amount between offsetMin & offsetMax
    class Tear(renpy.Displayable):
        def __init__(self, number, offtimeMult, ontimeMult,
                        offsetMin, offsetMax, srf=None):
            super(Tear, self).__init__()
            self.width, self.height = renpy.get_physical_size()
            # Force screen to 9:16 ratio
            if float(self.width) / float(self.height) > 9.0/16.0:
                self.width = self.height * 9 / 16
            else:
                self.height = self.width * 16 / 9
            self.number = number
            # Use a special image if specified, or tear
            # current screen by default
            if not srf: self.srf = screenshot_srf()
            else: self.srf = srf

            # Rip the screen into `number` pieces
            self.pieces = []
            tearpoints = [0, self.height]
            for i in range(number):
                tearpoints.append(random.randint(10, self.height - 10))
            tearpoints.sort()
            for i in range(number+1):
                self.pieces.append(TearPiece(tearpoints[i],
                                    tearpoints[i+1], offtimeMult,
                                    ontimeMult, offsetMin, offsetMax))

        ## Render the displayable
        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)
            render.blit(self.srf, (0,0))
            # Render each piece
            for piece in self.pieces:
                piece.update(st)
                subsrf = (self.srf.subsurface((0,
                            max(0, piece.startY - 1),
                            self.width,
                            max(0, piece.endY - piece.startY))))
                            #.pygame_surface()
                render.blit(subsrf, (piece.offset, piece.startY))
            renpy.redraw(self, 0)
            return render

## Define the screen for Ren'Py; by default, tear the screen into 10 pieces
screen tear(number=10, offtimeMult=1, ontimeMult=1, offsetMin=0,
                            offsetMax=50, w_timer=False, srf=None):
    zorder 150 #Screen tear appears above pretty much everything
    add Tear(number, offtimeMult, ontimeMult, offsetMin,
                                offsetMax, srf) size (config.screen_width,config.screen_height)
    if w_timer:
        timer w_timer action Hide('tear')

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

