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


    class MultiTouch(renpy.Displayable):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.text = ""
            self.x = 0
            self.y = 0
            self.zoom = 1.0
            self.rotate = 0

        def render(self, width, height, st, at):

            r = renpy.Render(width, height)

            square_width = int(200*self.zoom)
            square_size = int((square_width**2+square_width**2)**0.5)

            ren = renpy.render(Transform("#f0f8",
                xysize=(square_width, square_width),
                rotate=self.rotate,
                anchor=(0.5, 0.5)), width, height, st, at)
            #r.blit(ren, (self.x, self.y))
            r.blit(ren, (config.screen_width//2-square_size//2,
                        config.screen_height//2-square_size//2))

            # ren = renpy.render(Text(self.text), width, height, st, at)
            # r.blit(ren, (0, 0))

            renpy.redraw(self, 0)

            return r

        def normalize_pos(self, x, y):
            return (int(x*config.screen_width), int(y*config.screen_height))

        def event(self, ev, x, y, st):

            if ev.type == pygame.FINGERMOTION:
                # print("Finger motion")
                self.text = "Finger motion"
            elif ev.type == pygame.FINGERDOWN:
                # print("Finger down")
                self.text = "Finger down"
            elif ev.type == pygame.FINGERUP:
                # print("Finger up")
                self.text = "Finger up"
            elif ev.type == pygame.MULTIGESTURE:
                # print("Multigesture")
                self.text = "Multigesture"
                # try:
                #     print(ev.touchId, ev.dTheta, ev.dDist, self.normalize_pos(ev.x, ev.y), ev.numFingers)
                # except Exception as e:
                #     print("Couldn't do multitouch print", e)
                #self.zoom += ev.dTheta*10
                self.rotate += int(ev.dTheta*360)
                self.zoom += ev.dDist*15
                self.zoom = max(0.25, self.zoom)
            else:
                self.text = "Not recognized"

            if ev.type in (pygame.FINGERMOTION, pygame.FINGERDOWN, pygame.FINGERUP):
                try:
                    #print(ev.touchId, ev.fingerId, self.normalize_pos(ev.x, ev.y))
                    self.x, self.y = self.normalize_pos(ev.x, ev.y)
                except Exception as e:
                    print("something went wrong:", e)


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
