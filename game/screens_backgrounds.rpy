## This is the file where the various animated backgrounds are defined.
## They are defined as screens instead of images for additional flexibility
## and animations.

screen animated_shake_borders():
    zorder 1
    # Add borders for shake
    add "#000" size (300, config.screen_height) xpos 0.0 xanchor 1.0
    add "#000" size (300, config.screen_height) xpos 1.0 xanchor 0.0
    add "#000" size (config.screen_width, 300) ypos 1.0 yanchor 0.0
    add "#000" size (config.screen_width, 300) ypos 0.0 yanchor 1.0

###########################################################
## Morning background
###########################################################

image animated_big_star = "Phone UI/animated_bgs/morning/big_star.webp"
image animated_med_star = "Phone UI/animated_bgs/morning/med_star.webp"
image animated_tiny_star = "Phone UI/animated_bgs/morning/tiny_star.webp"

image animated_morning_clouds_back = Composite(
    (2250*2, 1692),
    (0, 0), 'Phone UI/animated_bgs/morning/morning_clouds_back.webp',
    (2250, 0), 'Phone UI/animated_bgs/morning/morning_clouds_back.webp'
)
image animated_morning_clouds_mid = Composite(
    (2250*2, 1692),
    (0, 0), 'Phone UI/animated_bgs/morning/morning_clouds_mid.webp',
    (2250, 0), 'Phone UI/animated_bgs/morning/morning_clouds_mid.webp'
)
image animated_morning_clouds_front = Composite(
    (2250*2, 1692),
    (0, 0), 'Phone UI/animated_bgs/morning/morning_clouds_front.webp',
    (2250, 0), 'Phone UI/animated_bgs/morning/morning_clouds_front.webp'
)

transform move_clouds(t=150, ytime=1, ysize=0):
    subpixel True
    ysize int(max(config.screen_height-113-165, 1334,
        ysize*(float(config.screen_height-113-165)/1334.0)))
    fit "cover"
    parallel:
        yalign 0.0
        yoffset (0 if config.screen_height == 1334 else 165)
        linear ytime yalign (1.0 if ysize else 0.0)
    parallel:
        block:
            xpos 1.0 xanchor 1.0
            linear t xanchor 0.5 xpos 1.0
            repeat

screen animated_morning():
    zorder 0
    tag animated_bg
    add 'Phone UI/animated_bgs/morning/morning_clouds_bg.webp':
        at reverse_topbottom_pan(150, 0, 0, 1.0, 0, 1.0)
        ysize int(2280.0/1334.0*config.screen_height)

    default xran = config.screen_width // 2
    default yran = (config.screen_height-113-165) // 3

    # Add a bunch of stars
    for x in range(2):
        for y in range(3):
            for star_type in ['med', 'tiny', 'big', 'med', 'tiny', 'big']:
                add 'animated_{}_star'.format(star_type):
                    at star_twinkle_out(100,
                        x*xran, x*xran+xran,
                        y*yran+165, y*yran+yran+165)
                add 'animated_{}_star'.format(star_type):
                    at star_twinkle_out(100,
                        x*xran, x*xran+xran,
                        y*yran+165, y*yran+yran+165)
                add 'animated_{}_star'.format(star_type):
                    at star_twinkle_out(100,
                        x*xran, x*xran+xran,
                        y*yran+165, y*yran+yran+165)

    # Clouds
    # add 'gentle_snow_back' at colorize_snow_morning()
    add 'animated_morning_clouds_back' at move_clouds(300, 250, 1692)
    add 'animated_morning_clouds_mid' at move_clouds(220, 230, 1692)
    add 'animated_morning_clouds_front' at move_clouds(150, 210, 1692)
    # add 'gentle_snow_front' at colorize_snow_morning()

    # A gradient overlay to ease the transition from night into morning
    add 'Phone UI/animated_bgs/morning/morning_darken.webp':
        at reverse_topbottom_pan(180, 160, 30, 0.8, 0, 0.0, 0.0)

    use animated_shake_borders()

transform colorize_snow_morning():
    alpha 0.45
    linear 80 alpha 1.0

###########################################################
## Noon background
###########################################################

image animated_noon_clouds_back = Composite(
    (2250*2, 1334),
    (0, 0), 'Phone UI/animated_bgs/noon/noon_clouds_back.webp',
    (2250, 0), 'Phone UI/animated_bgs/noon/noon_clouds_back.webp'
)
image animated_noon_clouds_mid = Composite(
    (2250*2, 1334),
    (0, 0), 'Phone UI/animated_bgs/noon/noon_clouds_mid.webp',
    (2250, 0), 'Phone UI/animated_bgs/noon/noon_clouds_mid.webp'
)
image animated_noon_clouds_front = Composite(
    (2250*2, 1334),
    (0, 0), 'Phone UI/animated_bgs/noon/noon_clouds_front.webp',
    (2250, 0), 'Phone UI/animated_bgs/noon/noon_clouds_front.webp'
)

image animated_noon_bg = Transform(
    'Phone UI/animated_bgs/noon/noon_background.webp',
    ysize=config.screen_height, fit="cover")

screen animated_noon():
    zorder 0
    tag animated_bg
    add 'animated_noon_bg'
    # Clouds
    add 'animated_noon_clouds_back' at move_clouds(300)
    add 'animated_noon_clouds_mid' at move_clouds(200)
    add 'animated_noon_clouds_front' at move_clouds(110)

    use animated_shake_borders()

###########################################################
## Evening background
###########################################################

image animated_evening_clouds_back = Composite(
    (2208*2, 1334),
    (0, 0), "Phone UI/animated_bgs/evening/evening_clouds_back.webp",
    (2208, 0), "Phone UI/animated_bgs/evening/evening_clouds_back.webp"
)
image animated_evening_clouds_mid = Composite(
    (2208*2, 1334),
    (0, 0), "Phone UI/animated_bgs/evening/evening_clouds_mid.webp",
    (2208, 0), "Phone UI/animated_bgs/evening/evening_clouds_mid.webp"
)
image animated_evening_clouds_front = Composite(
    (2208*2, 1334),
    (0, 0), "Phone UI/animated_bgs/evening/evening_clouds_front.webp",
    (2208, 0), "Phone UI/animated_bgs/evening/evening_clouds_front.webp"
)

screen animated_evening():
    zorder 0
    tag animated_bg

    default yinit = -1*(config.screen_height-113-165)

    add 'Phone UI/animated_bgs/evening/evening_clouds_bright.webp':
        ysize config.screen_height

    # There are three different sun colours for the evening as the sun sets
    add 'Phone UI/animated_bgs/evening/evening_clouds_yellow_sun.webp':
        xalign 0.5
        at topbottom_pan(movetime=180, delay1=0, fadetime=60,
            init_y=yinit, y_move=yinit*-1.5, start_alpha=1.0, delay_2=100)
    add 'Phone UI/animated_bgs/evening/evening_clouds_orange_sun.webp':
        xalign 0.5
        at topbottom_pan(movetime=180, delay1=60, fadetime=60,
            init_y=yinit, y_move=yinit*-1.5, start_alpha=0.0, delay_2=100)
    add 'Phone UI/animated_bgs/evening/evening_clouds_red_sun.webp':
        xalign 0.5
        at topbottom_pan(movetime=180, delay1=120, fadetime=60,
            init_y=yinit, y_move=yinit*-1.5, start_alpha=0.0, delay_2=100,
            disappear=1.0)

    # Clouds
    # add 'gentle_snow_back' at colorize_snow_evening()
    add 'animated_evening_clouds_back' at move_clouds(300)
    add 'animated_evening_clouds_mid' at move_clouds(200)
    add 'animated_evening_clouds_front' at move_clouds(110)
    # add 'gentle_snow_front' at colorize_snow_evening()

    # These gradients help blend the sun colours with the sky and clouds
    add 'Phone UI/animated_bgs/evening/evening_clouds_orange.webp':
        at fadein_out(delay1=45, fadein=45, fadeout=45, delay_2=170-90-75, start_alpha=0.0)
        ysize config.screen_height
    add 'Phone UI/animated_bgs/evening/evening_clouds_red.webp':
        at fadein_out(delay1=90, fadein=45, fadeout=10, delay_2=10, start_alpha=0.0, end_alpha=0.3)
        ysize config.screen_height

    use animated_shake_borders()


define config.gl2 = True
transform colorize_snow_evening():
    matrixcolor TintMatrix("#fff")
    linear 60 matrixcolor TintMatrix("#fce9cc")
    linear 60 matrixcolor TintMatrix("#ffecdb")
    linear 60 matrixcolor TintMatrix("#ffeaec")

###########################################################
## Night background
###########################################################

image animated_night_big_star = "Phone UI/animated_bgs/night/night_big_star.webp"
image animated_night_med_star = "Phone UI/animated_bgs/night/night_med_star.webp"
image animated_night_tiny_star = "Phone UI/animated_bgs/night/night_tiny_star.webp"

image animated_shooting_star1 = 'Phone UI/animated_bgs/night/night_shooting_star_1.webp'
image animated_shooting_star2 = 'Phone UI/animated_bgs/night/night_shooting_star_2.webp'

image animated_night_bg = 'Phone UI/animated_bgs/night/night_background.webp'

init python:
    class StarSprite():
        """
        A small class to hold information on a given star so it can be
        generated as a sprite.
        """
        def __init__(self, img, animation, delay_min, delay_max,
                xmin, xmax, ymin, ymax):
            delay = renpy.random.randint(delay_min, delay_max)
            self.x = renpy.random.randint(xmin, xmax)
            self.y = renpy.random.randint(ymin, ymax)

            if animation is not None:
                self.displayable = At(img, animation(delay))
            else:
                self.displayable = img

    ## Use sprites for stars
    def make_stars():
        star_manager = SpriteManager(predict=['animated_night_med_star',
            'animated_night_tiny_star', 'animated_night_big_star'])
        star_sprites = [ ]

        # The range of where the star can be on-screen
        xran = config.screen_width // 3
        yran = (config.screen_height-113-165) // 4

        for j in range(2): # Double the number of stars
            for x in range(3):
                for y in range(4):
                    for i in range(0, 200, 50):
                        # Make some stars twinkle in
                        star_sprites.append(StarSprite('animated_night_tiny_star',
                            star_twinkle_in2, i, i+50, x*xran, x*xran+xran,
                            y*yran, y*yran+yran))
                        star_sprites.append(StarSprite('animated_night_med_star',
                            star_twinkle_in2, i, i+50, x*xran, x*xran+xran,
                            y*yran, y*yran+yran))
                        star_sprites.append(StarSprite('animated_night_big_star',
                            star_twinkle_in2, i, i+50, x*xran, x*xran+xran,
                            y*yran, y*yran+yran))
                        # Make some stars fade in and stay stationary
                        star_sprites.append(StarSprite('animated_night_tiny_star',
                            star_fade_in2, i, i+50, x*xran, x*xran+xran,
                            y*yran, y*yran+yran))
                        star_sprites.append(StarSprite('animated_night_med_star',
                            star_fade_in2, i, i+50, x*xran, x*xran+xran,
                            y*yran, y*yran+yran))
                        star_sprites.append(StarSprite('animated_night_big_star',
                            star_fade_in2, i, i+50, x*xran, x*xran+xran,
                            y*yran, y*yran+yran))
                    # Make some stars already exist
                    star_sprites.append(StarSprite('animated_night_tiny_star',
                        None, 0, 0, x*xran, x*xran+xran, y*yran, y*yran+yran))
                    star_sprites.append(StarSprite('animated_night_med_star',
                        None, 0, 0, x*xran, x*xran+xran, y*yran, y*yran+yran))
                    star_sprites.append(StarSprite('animated_night_big_star',
                        None, 0, 0, x*xran, x*xran+xran, y*yran, y*yran+yran))

        # Add them all to the sprite manager
        all_sprites = [ ]
        for sprite in star_sprites:
            all_sprites.append(star_manager.create(sprite.displayable))

        # Position them all
        for info, sprite in zip(star_sprites, all_sprites):
            sprite.x = info.x
            sprite.y = info.y

        return star_manager

screen animated_night():
    zorder 0
    tag animated_bg

    default star_sprites = make_stars()

    add 'animated_night_bg':
        ysize max(1334, config.screen_height-113-165) fit "cover"
    # Gradient overlay
    add 'Phone UI/animated_bgs/night/night_overlay.webp':
        at topbottom_pan2(100, 100, 50, 1.0, 0, 0.0, 0.0)
    fixed:
        xysize (config.screen_width, config.screen_height-113-165) # Don't bother adding stars behind the UI
        align (0.5, 1.0)
        yoffset -113

        add star_sprites

        # Shooting stars
        add 'animated_shooting_star1' at shooting_star
        add 'animated_shooting_star2' at shooting_star

    use animated_shake_borders()

###########################################################
## Early morning background
###########################################################

screen animated_earlyMorn():
    zorder 0
    tag animated_bg
    add 'Phone UI/animated_bgs/earlyMorn/earlymorn_background.webp':
        at reverse_topbottom_pan(150, 0, 0, 1.0, 0, 1.0)

    default xran = config.screen_width // 3
    default yran = (config.screen_height-113-165) // 4

    fixed:
        # Stars
        xysize (config.screen_width, 1134)
        align (0.5, 0.6)
        for x in range(3):
            for y in range(4):
                for star_type in ['med', 'tiny', 'big']:
                    add 'animated_night_{}_star'.format(star_type):
                        at star_twinkle_randomly(
                            x*xran, x*xran+xran,
                            y*yran, y*yran+yran)
                    add 'animated_night_{}_star'.format(star_type):
                        at star_place_randomly(
                            x*xran, x*xran+xran,
                            y*yran, y*yran+yran)

    frame:
        # Constellations
        xysize (config.screen_width, 1050)
        xalign 0.5
        yoffset 170
        add 'gemini_constellation' align (0.1, 0.05)
        add 'libra_constellation' align (0.05, 0.5)
        add 'virgo_constellation' align (0.02, 0.98)

        add 'pisces_constellation' align (0.85, 0.35)
        add 'scorpius_constellation' align (0.7, 0.75)

        add 'aries_constellation' align (0.98, 0.01)
        add 'capricorn_constellation' align (0.95, 0.98)

    use animated_shake_borders()


image gemini_constellation:
    "Phone UI/animated_bgs/earlyMorn/gemini_stars.webp"
    random.randint(60, 80)
    block:
        "Phone UI/animated_bgs/earlyMorn/gemini_stars.webp"
        3.0
        "Phone UI/animated_bgs/earlyMorn/gemini_const.webp" with CropMove(3.0, 'irisout')
        5.0
        "Phone UI/animated_bgs/earlyMorn/gemini_symbol.webp" with Dissolve(3.0)
        5.0
        'Phone UI/animated_bgs/earlyMorn/gemini_stars.webp' with Dissolve(5.0)
        140 + random.random()
        repeat

image libra_constellation:
    "Phone UI/animated_bgs/earlyMorn/libra_stars.webp"
    random.randint(120, 140)
    block:
        "Phone UI/animated_bgs/earlyMorn/libra_stars.webp"
        3.0
        "Phone UI/animated_bgs/earlyMorn/libra_const.webp" with CropMove(3.0, 'irisout')
        5.0
        "Phone UI/animated_bgs/earlyMorn/libra_symbol.webp" with Dissolve(3.0)
        5.0
        'Phone UI/animated_bgs/earlyMorn/libra_stars.webp' with Dissolve(5.0)
        140 + random.random()
        repeat

image virgo_constellation:
    "Phone UI/animated_bgs/earlyMorn/virgo_stars.webp"
    random.randint(20, 40)
    block:
        "Phone UI/animated_bgs/earlyMorn/virgo_stars.webp"
        3.0
        "Phone UI/animated_bgs/earlyMorn/virgo_const.webp" with CropMove(3.0, 'irisout')
        5.0
        "Phone UI/animated_bgs/earlyMorn/virgo_symbol.webp" with Dissolve(3.0)
        5.0
        'Phone UI/animated_bgs/earlyMorn/virgo_stars.webp' with Dissolve(5.0)
        140 + random.random()
        repeat

image pisces_constellation:
    "Phone UI/animated_bgs/earlyMorn/pisces_stars.webp"
    random.randint(0, 20)
    block:
        "Phone UI/animated_bgs/earlyMorn/pisces_stars.webp"
        3.0
        "Phone UI/animated_bgs/earlyMorn/pisces_const.webp" with CropMove(3.0, 'irisout')
        5.0
        "Phone UI/animated_bgs/earlyMorn/pisces_symbol.webp" with Dissolve(3.0)
        5.0
        'Phone UI/animated_bgs/earlyMorn/pisces_stars.webp' with Dissolve(5.0)
        140 + random.random()
        repeat

image scorpius_constellation:
    "Phone UI/animated_bgs/earlyMorn/scorpius_stars.webp"
    random.randint(80, 100)
    block:
        "Phone UI/animated_bgs/earlyMorn/scorpius_stars.webp"
        3.0
        "Phone UI/animated_bgs/earlyMorn/scorpius_const.webp" with CropMove(3.0, 'irisout')
        5.0
        "Phone UI/animated_bgs/earlyMorn/scorpius_symbol.webp" with Dissolve(3.0)
        5.0
        'Phone UI/animated_bgs/earlyMorn/scorpius_stars.webp' with Dissolve(5.0)
        140 + random.random()
        repeat

image aries_constellation:
    "Phone UI/animated_bgs/earlyMorn/aries_stars.webp"
    random.randint(100, 120)
    block:
        "Phone UI/animated_bgs/earlyMorn/aries_stars.webp"
        3.0
        "Phone UI/animated_bgs/earlyMorn/aries_const.webp" with CropMove(3.0, 'irisout')
        5.0
        "Phone UI/animated_bgs/earlyMorn/aries_symbol.webp" with Dissolve(3.0)
        5.0
        'Phone UI/animated_bgs/earlyMorn/aries_stars.webp' with Dissolve(5.0)
        140 + random.random()
        repeat

image capricorn_constellation:
    "Phone UI/animated_bgs/earlyMorn/capricorn_stars.webp"
    random.randint(40, 60)
    block:
        "Phone UI/animated_bgs/earlyMorn/capricorn_stars.webp"
        3.0
        "Phone UI/animated_bgs/earlyMorn/capricorn_const.webp" with CropMove(3.0, 'irisout')
        5.0
        "Phone UI/animated_bgs/earlyMorn/capricorn_symbol.webp" with Dissolve(3.0)
        5.0
        'Phone UI/animated_bgs/earlyMorn/capricorn_stars.webp' with Dissolve(5.0)
        140 + random.random()
        repeat

###########################################################
## Reused Transforms
###########################################################
# Slowly pan an image across the screen for timing seconds. Optionally,
# also pan it in the y direction. The x direction repeats but the y
# direction does not.
transform slow_pan(timing=0, y_timing=0, ysize=0):
    ysize max(config.screen_height-113-165, 1334, ysize)
    fit "cover"
    yoffset (-113 if (config.screen_height-113-165 > 1334) else 0)
    subpixel True
    parallel:
        block:
            xpos 1.0 xanchor 1.0
            linear timing xpos 1.0 xanchor 0.5
            repeat
    parallel:
        block:
            yalign 0.0
            easein y_timing yalign 1.0

transform topbottom_pan2(movetime, delay1, fadetime, start_alpha, delay2,
        disappear=0.0, fadein_alpha=1.0):
    # Start anchored to the bottom
    yalign 1.0
    alpha start_alpha subpixel True
    parallel:
        linear movetime yalign 0.0
    parallel:
        delay1
        linear fadetime alpha fadein_alpha
        delay2
        alpha disappear

transform reverse_topbottom_pan(movetime, delay1, fadetime, start_alpha, delay2,
        disappear=0.0, fadein_alpha=1.0):
    # Start anchored to the top
    yalign 0.0
    alpha start_alpha subpixel True
    parallel:
        linear movetime yalign 1.0
    parallel:
        delay1
        linear fadetime alpha fadein_alpha
        delay2
        alpha disappear

# Slowly pan an image from the top of the screen to the bottom. Optionally,
# includes an alpha transform.
transform topbottom_pan(movetime, delay1, fadetime, init_y, y_move,
        start_alpha, delay_2, disappear=0.0, fadein_alpha=1.0):
    yalign 0.0 yoffset init_y alpha start_alpha subpixel True
    # Total distance to move is y_move + init_y
    parallel:
        linear movetime yoffset (y_move + init_y)
    parallel:
        delay1
        linear fadetime alpha fadein_alpha
        delay_2
        alpha disappear

# Slowly fade an image in and out
transform fadein_out(delay1, fadein, fadeout, delay_2,
        start_alpha, end_alpha=0.0):
    alpha start_alpha
    delay1
    linear fadein alpha 0.3
    delay_2
    linear fadeout alpha end_alpha

# Currently unused; pans the moon across the screen
transform moon_pan():
    xpos -360 ypos -200 yoffset 0 xoffset 0 zoom 0.5
    parallel:
        easein_cubic 250 xoffset 800
    parallel:
        easein 250 yoffset 1000
    parallel:
        linear 250 zoom 1.0
    parallel:
        230
        linear 20  alpha 0.0
    repeat

# Currently unused; used to rotate the whole star field around the screen
transform star_rotate(speed):
    rotate 0 subpixel True
    block:
        rotate 0
        linear speed rotate 360
        repeat

# Randomly chooses a direction and origin point to spawn a shooting star
transform shooting_star():
    rotate 0 xzoom 1 xoffset 0 yoffset 0 alpha 0.0 subpixel True
    (renpy.random.randint(20, 70) + renpy.random.random())
    choice:
        rotate 40 xpos renpy.random.randint(0, 600) ypos renpy.random.randint(190, 900)
        parallel:
            ease 0.2 alpha 1.0
            linear 0.1
            ease 0.2 alpha 0.0
        parallel:
            easeout_quad 0.5 xoffset 525 yoffset 667
        parallel:
            linear 0.5 rotate 70
    choice:
        xzoom -1 rotate -10 xpos renpy.random.randint(0, 600) ypos renpy.random.randint(190, 900)
        parallel:
            ease 0.2 alpha 1.0
            linear 0.1
            ease 0.2 alpha 0.0
        parallel:
            easeout_quad 0.5 xoffset -600 yoffset 133
        parallel:
            linear 0.5 rotate -20
    choice:
        xzoom -1 rotate -60 xpos renpy.random.randint(0, 600) ypos renpy.random.randint(190, 900)
        parallel:
            ease 0.2 alpha 1.0
            linear 0.1
            ease 0.2 alpha 0.0
        parallel:
            easeout_quad 0.5 xoffset -300 yoffset 534
        parallel:
            linear 0.5 rotate -80
    choice:
        xzoom -1 rotate -10 xpos renpy.random.randint(0, 600) ypos renpy.random.randint(190, 900)
        parallel:
            ease 0.2 alpha 1.0
            linear 0.1
            ease 0.2 alpha 0.0
        parallel:
            easeout_quad 0.5 xoffset -375 yoffset 133
        parallel:
            linear 0.5 rotate -20
    choice:
        xzoom -1 rotate -50 xpos renpy.random.randint(0, 600) ypos renpy.random.randint(190, 900)
        parallel:
            ease 0.2 alpha 1.0
            linear 0.1
            ease 0.2 alpha 0.0
        parallel:
            easeout_quad 0.5 xoffset -375 yoffset 667
        parallel:
            linear 0.5 rotate -80
    choice:
        rotate 10 xpos renpy.random.randint(0, 600) ypos renpy.random.randint(190, 900)
        parallel:
            ease 0.2 alpha 1.0
            linear 0.1
            ease 0.2 alpha 0.0
        parallel:
            easeout_quad 0.5 xoffset 600 yoffset 133
        parallel:
            linear 0.5 rotate 20
    choice:
        rotate 50 xpos renpy.random.randint(0, 600) ypos renpy.random.randint(190, 900)
        parallel:
            ease 0.2 alpha 1.0
            linear 0.1
            ease 0.2 alpha 0.0
        parallel:
            easeout_quad 0.5 xoffset 225 yoffset 400
        parallel:
            linear 0.5 rotate 80
    repeat
# Fades a star in after waiting some arbitrary number of seconds
transform star_fade_in(delay_min, delay_max, x_min=0, x_max=0, y_min=0, y_max=0):
    alpha 0.0 xpos renpy.random.randint(x_min, x_max) ypos (renpy.random.randint(y_min, y_max))
    renpy.random.randint(delay_min, delay_max)
    ease 1.0 + renpy.random.random() alpha 1.0
# Places a star at a random position on the screen, within certain bounds
transform star_place_randomly(x_min=0, x_max=0, y_min=0, y_max=0):
    alpha 0.6 xpos renpy.random.randint(x_min, x_max) ypos (renpy.random.randint(y_min, y_max))
# Places a star randomly on the screen, then animates it twinkling on occasion
transform star_twinkle_randomly(x_min=0, x_max=0, y_min=0, y_max=0):
    alpha 0.6 xpos renpy.random.randint(x_min, x_max) ypos (renpy.random.randint(y_min, y_max))
    block:
        ease 1.0 + renpy.random.random() alpha 0.6
        linear renpy.random.randint(4, 16) + renpy.random.random()
        ease 1.1 + renpy.random.random() alpha 0.0
        linear 0.3
        repeat
# Animates a star blinking onto the screen, then makes it twinkle occasionally
transform star_twinkle_in(delay_min, delay_max, x_min, x_max, y_min, y_max):
    alpha 0.0 xpos renpy.random.randint(x_min, x_max) ypos (renpy.random.randint(y_min, y_max))
    renpy.random.randint(delay_min, delay_max)
    block:
        ease 1.0 + renpy.random.random() alpha 1.0
        linear renpy.random.randint(4, 16) + renpy.random.random()
        ease 1.1 + renpy.random.random() alpha 0.0
        linear 0.3
        repeat
# Places a star on the screen, twinkling randomly until it disappears
transform star_twinkle_out(delay1, x_min, x_max, y_min, y_max):
    alpha 1.0 xpos renpy.random.randint(x_min, x_max) ypos (renpy.random.randint(y_min, y_max))
    block:
        ease 1.0 + renpy.random.random() alpha 1.0
        linear renpy.random.randint(4, 16) + renpy.random.random()
        ease 1.1 + renpy.random.random() alpha 0.0
        linear 0.3
        repeat (delay1 // 18) + 1

transform star_fade_in2(delay):
    alpha 0.0
    pause delay
    ease 1.0+renpy.random.random() alpha 1.0
transform star_twinkle_in2(delay):
    alpha 0.0
    pause delay
    block:
        ease 1.0 + renpy.random.random() alpha 1.0
        linear renpy.random.randint(4, 16) + renpy.random.random()
        ease 1.1 + renpy.random.random() alpha 0.0
        linear 0.3
        repeat


###########################################################
## Hack background
###########################################################

init python:
    def scramble_text(txt):
        """Find random blocks of text to replace with symbols."""

        symbols = ['!', '@', '#', '$', '%', '^', '&', '*']
        new_txt = ""
        random_nums = []
        prev_pos = 0
        # Generate x random numbers
        x = 25
        for i in range(x):
            the_min = ((len(txt)-10) // x) * i
            the_max = ((len(txt)-10) // x) * (i+1)
            loop_counter = 0
            test_pair = (random.randint(the_min+1, the_max),
                            random.randint(1, min( ((len(txt)-10)//x), 6)))
            block_start = test_pair[0] - 1
            block_end = test_pair[0] + test_pair[1] + 1

            while '{' in txt[block_start:block_end]:
                # Can't have the { tag in the block of text; Ren'Py uses
                # it for interpolation and other things so it causes too
                # many issues. Try to find a chunk without it.
                loop_counter += 1
                test_pair = (random.randint(the_min+1, the_max),
                            random.randint(1, min( ((len(txt)-10)//x), 6)))
                if loop_counter > 20:
                    # print_file("looped to 20")
                    break
            if loop_counter <= 20:
                random_nums.append( test_pair )

        # Replace each section of characters with random symbols
        for position, stringlen in random_nums:
            symbol_str = ''
            for i in range(stringlen):
                if txt[position+i] == '{':
                    symbol_str += '{'
                    # print_file("Found a {{ at", position+i, ", ignoring")
                elif txt[position+i] == '\n':
                    symbol_str += '\n'
                    # print_file("Found a newline")
                else:
                    symbol_str += random.choice(symbols)
            # new_txt will be whatever txt was up until the position
            if new_txt == "":
                new_txt += txt[:position]
            else:
                new_txt += txt[prev_pos:position]
            prev_pos = position + stringlen
            symbol_str = "{color=#000}" + symbol_str + "{/color}"
            new_txt += symbol_str

        new_txt += txt[random_nums[-1][0] + random_nums[-1][1]:]

        # original_new_len = str(len(new_txt))
        # new_txt += "\nThe random numbers:"
        # for position, stringlen in random_nums:
        #     new_txt += "\n" + str(position) + " " + str(stringlen)
        # new_txt += "\nLength of original string: "
        # new_txt += str(len(txt))
        # new_txt += "\nLength of new_string: "
        # new_txt += original_new_len

        return new_txt

screen animated_hack_background(red=False):
    zorder 0
    tag animated_bg
    add 'Phone UI/hacking_bg.webp' yalign 0.75 xysize (config.screen_width, config.screen_height)
    default hacking_text_to_scramble = hacking_text
    frame:
        ysize config.screen_height-113-165
        xsize 1100
        yalign 0.5
        xoffset 30
        yoffset 30
        text hacking_text_to_scramble:
            size 16
            xsize 1100
            if not red:
                color "#9be64e"
                outlines [ (1, "#76b04caa", absolute(0), absolute(0)),
                        (2, "#76b04c40", absolute(0), absolute(0)),
                        (4, "#76b04c20", absolute(0), absolute(0))]
            else:
                color "#e7a9ac60"
                outlines [ (1, "#c63f4560", absolute(0), absolute(0)),
                        (2, "#dd7b7c40", absolute(0), absolute(0)),
                        (4, "#dd7b7c20", absolute(0), absolute(0))]
            font "fonts/Anonymous/Anonymous.ttf"
            line_spacing 10
            #slow_cps 20
        #add 'hack_text_img'

    # Only show these effects if the player has opted in to hacking effects,
    # as they cause the screen to flash occasionally.
    if persistent.hacking_effects:
        timer random.randint(2, 6):
            action SetScreenVariable('hacking_text_to_scramble',
                scramble_text(hacking_text))
            repeat True
        timer 0.21:
            action If(hacking_text_to_scramble != hacking_text,
                SetScreenVariable('hacking_text_to_scramble', hacking_text), [])
            repeat True

        timer random.randint(8, 16):
            action If(not random.randint(0, 2),
                If(not random.randint(0, 4),
                    [Show('hack_rectangle_2', w_timer=0.1),
                    Show('hack_tear', w_timer=0.18)],
                    Show('hack_tear', w_timer=0.18)),
                [])
            repeat True
        timer random.randint(5, 10) + random.randint(10, 30):
            action Show('white_squares_2', w_timer=0.3) repeat True

    use animated_shake_borders()

screen hack_tear(number=10, offtimeMult=0.4, ontimeMult=0.2, offsetMin=-10,
                offsetMax=30, w_timer=0.18, srf=None):
    zorder 1
    add Tear(number, offtimeMult, ontimeMult, offsetMin,
                                offsetMax, srf) size (config.screen_width,config.screen_height)
    timer w_timer action Hide('hack_tear')

screen white_squares_2(w_timer=0.5):
    zorder 1
    add 'hacked_white_squares'
    timer w_timer action Hide('white_squares_2')

screen hack_rectangle_2(w_timer=0.2):
    zorder 2
    add 'm_rectstatic'
    timer w_timer action Hide('hack_rectangle_2')

define hacking_text = """
struct group_info init_groups = {{ .usage = ATOMIC_INIT(2) };
struct group_info *groups_alloc(int gidsetsize){{
    struct group_info *group_info;
    int nblocks;
    int i;

    nblocks = (gidsetsize + NGROUPS_PER_BLOCK - 1) / NGROUPS_PER_BLOCK;
    /* Make sure we always allocate at least one indirect block pointer */
    nblocks = nblocks ? : 1;
    group_info = kmalloc(sizeof(*group_info) + nblocks*sizeof(gid_t *), GFP_User);
    if (lgroup_info)
        return NULL;
    group_info->ngroups = gidsetsize;
    group_info->nblocks = nblocks;
    atomic_set(&group_info->usage, 1);

    if gidsetsize <= NGROUPS_SMALL)
        group_info->blocks(0) = group_info->small_block;
    else {{
        for (i=0; i < nblocks; ++i) {{
            gid_t *b;
            b = (void*)__get_free_page(GFP_USER);
            if (lb)
                goto out_undo_partial_alloc;
            group_info->blocks(i) = b;
        }
    }
    return group_info;
}

out_undo_partial_alloc:
    while (--i >= 0) {{
        free_page((unsigned long)group_info->blocks(i));
    }
    kfree(group_info);
    return NULL;

EXPORT_SYMBOL(groups_alloc);

void groups_free(struct group_info *group_info)
{{
    if (group_info->blocks(0) != group_info->small_block) {{
        int i;
        for (i = 0; i < group_info->nblocks; i++) {{
            free_page((unsigned long)group_info->blocks(i));
        }
    }
    kfree(group_info);
}

EXPORT_SYMBOL(groups_free);
"""
# /* export the group_info to a user-space array */
# static int groups_to_user(gid_t __user *grouplist,
#         const struct group_info *group_info);
# {{
#     int i;
#     unsigned int count = group_info->ngroups;

#     for (i=0; i < group_info->nblocks; i++) {{
#         unsigned int cp_count = min(NGROUPS_PER_BLOCK, count);
#         unsigned int len = cp_count * sizeof(*grouplist);

#         if (copy_to_user(gouplist.group_info->blocks(i).len))
#             return DEFAULT;

#         grouplist += NGROUPS_PER_BLOCK;
#         count -= cp_count;
#     }
#     return 0;
# }
# """

###########################################################
## Rainy day background
###########################################################

image single_raindrop = "Phone UI/animated_bgs/rainy_day/single_raindrop.webp"

init python:
    rain_mult = 25
    def big_rain(xspeed=0, yspeed=(50*rain_mult, 100*rain_mult), start=100,
            count=10):
        img = Transform('single_raindrop', zoom=1.3, alpha=0.5)

        return SnowBlossom2(img, count=count, border=-70,#border=25,
            xspeed=xspeed,
            yspeed=yspeed,
            start=start, fluttering=0, fast=True)

    def med_rain(xspeed=0, yspeed=(32*rain_mult, 75*rain_mult), start=100,
            count=75, alpha=1.0):
        if alpha == 1.0:
            img = 'single_raindrop'
        else:
            img = Transform('single_raindrop', alpha=alpha)

        return SnowBlossom2(img, count=count, border=-70,#border=25,
            xspeed=xspeed,
            yspeed=yspeed,
            start=start, fluttering=0, fast=True)

    def tiny_rain(xspeed=0, yspeed=(32*rain_mult, 75*rain_mult), start=100,
            count=150):
        img = Transform('single_raindrop', zoom=0.6)
        return SnowBlossom2(img, count=count, border=-70,#border=25,
            xspeed=xspeed,
            yspeed=yspeed,
            start=start, fluttering=0, fast=True)

image simulated_rain = Fixed(
    med_rain(start=0, alpha=0.5), med_rain(start=75),
    med_rain(start=150, alpha=0.5), med_rain(start=225, alpha=0.25),

    tiny_rain(start=0), tiny_rain(start=100),
    tiny_rain(start=200), tiny_rain(start=250)
)

image front_rain = Fixed(
    big_rain(start=0), big_rain(start=150)
)

image lightning_clouds = Composite(
    (2250*2, 1334),
    (0, 0), 'Phone UI/animated_bgs/rainy_day/rainy_clouds_lightning.webp',
    (2250, 0), 'Phone UI/animated_bgs/rainy_day/rainy_clouds_lightning.webp',
)

image animated_rainy_clouds_back = Composite(
    (2250*2, 1334),
    (0, 0), 'Phone UI/animated_bgs/rainy_day/rainy_clouds_back.webp',
    (2250, 0), 'Phone UI/animated_bgs/rainy_day/rainy_clouds_back.webp'
)
image animated_rainy_clouds_mid = Composite(
    (2250*2, 1334),
    (0, 0), 'Phone UI/animated_bgs/rainy_day/rainy_clouds_mid.webp',
    (2250, 0), 'Phone UI/animated_bgs/rainy_day/rainy_clouds_mid.webp'
)
image animated_rainy_clouds_front = Composite(
    (2250*2, 1334),
    (0, 0), 'Phone UI/animated_bgs/rainy_day/rainy_clouds_front.webp',
    (2250, 0), 'Phone UI/animated_bgs/rainy_day/rainy_clouds_front.webp'
)
image animated_rainy_clouds_underlay = Composite(
    (2250*2, 1334),
    (0, 0), Transform('Phone UI/animated_bgs/rainy_day/rainy_clouds_cloud_underlay.webp', xzoom=-1),
    (2250, 0), Transform('Phone UI/animated_bgs/rainy_day/rainy_clouds_cloud_underlay.webp', xzoom=-1)
)

screen animated_rainy_day():
    zorder 0
    tag animated_bg
    add 'Phone UI/animated_bgs/rainy_day/rainy_clouds_gradient.webp':
        ysize config.screen_height
    # Clouds
    add 'animated_rainy_clouds_underlay' at move_clouds(400)
    add 'lightning_clouds' at move_clouds(200), lightning_cloud_flash()
    add 'animated_rainy_clouds_back' at move_clouds(300)
    add 'animated_rainy_clouds_mid' at move_clouds(200)
    add 'simulated_rain'
    add 'animated_rainy_clouds_front' at move_clouds(110)
    add Solid("#000") size (config.screen_width, 3) yalign 1.0
    add 'front_rain'

    use animated_shake_borders()

# A transform that causes lightning to randomly appear and flash
transform lightning_cloud_flash():
    block:
        # The lightning
        alpha 0.0
        choice:
            pause 10
        choice:
            pause 5
        choice:
            pause 15
        ease 0.04 alpha 0.4
        linear 0.04 alpha 0.0
        ease 0.08 alpha 0.6
        linear 0.04 alpha 0.0
        ease 0.1 alpha 1.0
        linear 0.08 alpha 0.0
        repeat

###########################################################
## Snow background
###########################################################

image snow_giant = "Phone UI/animated_bgs/snow/snow_giant.webp"
image snow_med = "Phone UI/animated_bgs/snow/snow_med.webp"
image snow_tiny = "Phone UI/animated_bgs/snow/snow_tiny.webp"

init python:
    def giant_snow(xspeed=0, yspeed=(50, 100), start=100,
            count=5, fluttering=10):
        return SnowBlossom2("snow_giant", count=count,
            border=-70,#border=123,
            xspeed=xspeed,
            yspeed=yspeed,
            start=start, fluttering=fluttering, fast=True)

    def med_snow(xspeed=0, yspeed=(32, 75), start=100,
            count=75, fluttering=10, alpha=1.0):
        if alpha == 1.0:
            img = 'snow_med'
        else:
            img = Transform('snow_med', alpha=alpha, xzoom=-1.0)

        return SnowBlossom2(img, count=count, border=-70,#border=25,
            xspeed=xspeed,
            yspeed=yspeed,
            start=start, fluttering=fluttering, fast=True)


    def tiny_snow(xspeed=0, yspeed=(32, 75), start=100,
            count=150, fluttering=10):

        return SnowBlossom2('snow_tiny', count=count, border=-70,#border=25,
            xspeed=xspeed,
            yspeed=yspeed,
            start=start, fluttering=fluttering, fast=True)

## Snow image definitions
image gentle_snow_back = Fixed(
    med_snow(start=0, alpha=0.5), med_snow(start=75, alpha=0.5),
    med_snow(start=150, alpha=0.5), med_snow(start=225, alpha=0.5),

    tiny_snow(start=0), tiny_snow(start=50), tiny_snow(start=100),
    tiny_snow(start=150), tiny_snow(start=200), tiny_snow(start=250)
)

image gentle_snow_front = Fixed(
    giant_snow(start=0), giant_snow(start=100), giant_snow(start=200),
    med_snow(start=0), med_snow(start=75), med_snow(start=150),
    med_snow(start=225)
)


image animated_snow_clouds_back = Transform('animated_noon_clouds_back', alpha=0.2)
image animated_snow_clouds_mid = Transform('animated_noon_clouds_mid', alpha=0.2)
image animated_snow_clouds_front = Transform('animated_noon_clouds_front', alpha=0.2)

screen animated_snowy_day():
    zorder 0
    tag animated_bg

    add "Phone UI/animated_bgs/snow/snow_bg2.webp":
        ysize config.screen_height

    # Clouds
    add 'animated_snow_clouds_back' at move_clouds(300)
    add 'gentle_snow_back'
    add 'animated_snow_clouds_mid' at move_clouds(200)
    add 'animated_snow_clouds_front' at move_clouds(110)
    add 'gentle_snow_front'

image animated_morning_snow_clouds_back = Transform('animated_noon_clouds_back', alpha=0.8)
image animated_morning_snow_clouds_mid = Transform('animated_noon_clouds_mid', alpha=0.8)
image animated_morning_snow_clouds_front = Transform('animated_noon_clouds_front', alpha=0.8)


screen animated_morning_snow():
    zorder 0
    tag animated_bg

    add "Phone UI/animated_bgs/snow/snow_bg1.webp":
        ysize config.screen_height

    # Clouds
    add 'animated_morning_snow_clouds_back' at move_clouds(300)
    add 'gentle_snow_back'
    add 'animated_morning_snow_clouds_mid' at move_clouds(200)
    add 'animated_morning_snow_clouds_front' at move_clouds(110)
    add 'gentle_snow_front'

    use animated_shake_borders()


# Code adapted from SnowBlossom2 code on the lemmasoft forums.
# Original link: https://lemmasoft.renai.us/forums/viewtopic.php?t=36421
init -100 python:

    def SnowBlossom2(d, count=10, border=50, xspeed=(20, 50),
            yspeed=(100, 200), start=0, fluttering=0, flutteringspeed=0.01,
            fast=False, horizontal=False):

        """
        :doc: sprites_extra

        The snowblossom effect moves multiple instances of a sprite up,
        down, left or right on the screen. When a sprite leaves the screen, it
        is returned to the start.

        `d`
            The displayable to use for the sprites.

        `border`
            The size of the border of the screen. The sprite is considered to be
            on the screen until it clears the border, ensuring that sprites do
            not disappear abruptly.

        `xspeed`, `yspeed`
            The speed at which the sprites move, in the horizontal and vertical
            directions, respectively. These can be a single number or a tuple of
            two numbers. In the latter case, each particle is assigned a random
            speed between the two numbers. The speeds can be positive or negative,
            as long as the second number in a tuple is larger than the first.

        `start`
            The delay, in seconds, before each particle is added. This allows
            the particles to start at the top of the screen, while not looking
            like a "wave" effect.

        `fluttering`
            The width of fluttering in pixel.

        `flutteringspeed`
            The speed of fluttering.

        `fast`
            If true, particles start in the center of the screen, rather than
            only at the edges.

        `horizontal`
            If true, particles appear on the left or right side of the screen,
            rather than the top or bottom.
            """

        # If going horizontal, swap the xspeed and the yspeed.
        if horizontal:
            xspeed, yspeed = yspeed, xspeed

        return Particles(SnowBlossomFactory2(image=d,
                                            count=count,
                                            border=border,
                                            xspeed=xspeed,
                                            yspeed=yspeed,
                                            start=start,
                                            fluttering=fluttering,
                                            flutteringspeed=flutteringspeed,
                                            fast=fast,
                                            rotate=horizontal))


    class SnowBlossomFactory2(renpy.python.NoRollback):

        # Determines whether we calculate things from left to right instead
        # of from top to bottom
        rotate = False

        def __setstate__(self, state):
            self.start = 0
            vars(self).update(state)
            self.init()

        def __init__(self, image, count, xspeed, yspeed, border, start,
                fluttering, flutteringspeed, fast, rotate=False):
            self.image = renpy.easy.displayable(image)
            self.count = count
            self.xspeed = xspeed
            self.yspeed = yspeed
            self.border = border
            self.start = start
            self.fluttering = fluttering
            self.flutteringspeed = flutteringspeed
            self.fast = fast
            self.rotate = rotate
            self.init()

        def init(self):
            # Get a random float between 0 and self.start for all the particles
            self.starts = [ random.uniform(0, self.start)
                for _i in xrange(0, self.count) ]
            self.starts.append(self.start)
            # Sort them from earliest to latest appearance
            self.starts.sort()

        def create(self, particles, st):

            def ranged(n):
                if type(n) == tuple:
                    # Return a random float between range n[0] and n[1]
                    return random.uniform(n[0], n[1])
                else:
                    # Otherwise just return the number
                    return n

            if not particles and self.fast:
                # Show some particles on screen instantly if there aren't
                # any showing yet
                rv = [ ]

                for _i in xrange(0, self.count):
                    rv.append(SnowBlossomParticle2(self.image,
                                                ranged(self.xspeed),
                                                ranged(self.yspeed),
                                                self.border,
                                                st,
                                                self.fluttering,
                                                self.flutteringspeed,
                                                random.uniform(0, 100),
                                                fast=True,
                                                rotate=self.rotate))
                return rv

            # Otherwise, wait to display particles until their start time
            if particles is None or len(particles) < self.count:

                # Check to see if we have a particle ready to start. If not,
                # don't start it.
                if particles and st < self.starts[len(particles)]:
                    return None

                return [ SnowBlossomParticle2(self.image,
                                            ranged(self.xspeed),
                                            ranged(self.yspeed),
                                            self.border,
                                            st,
                                            self.fluttering,
                                            self.flutteringspeed,
                                            random.uniform(0, 100),
                                            fast=False,
                                            rotate=self.rotate) ]

        def predict(self):
            return [ self.image ]


    class SnowBlossomParticle2(renpy.python.NoRollback):

        def __init__(self, image, xspeed, yspeed, border, start, fluttering,
                flutteringspeed, offset, fast, rotate):

            # Correct to 1; otherwise could be dividing by zero
            if yspeed == 0:
                yspeed = 1

            self.image = image
            self.xspeed = xspeed
            self.yspeed = yspeed
            self.border = border
            self.start = start
            self.fluttering = fluttering
            self.flutteringspeed = flutteringspeed
            self.offset = offset
            self.rotate = rotate
            self.angle = 0


            if not rotate:
                sh = renpy.config.screen_height
                sw = renpy.config.screen_width
            else:
                sw = renpy.config.screen_height
                sh = renpy.config.screen_width

            # Start above or below the edge of the screen, as needed
            if self.yspeed > 0:
                self.ystart = -border
            else:
                self.ystart = sh + border

            # travel_time is the screen height + 2*border (aka height of the
            # particle itself so it clears the edge of the screen) divided
            # by the speed
            travel_time = (2.0 * border + sh) / abs(yspeed)

            # How far the particle should travel in the x direction during
            # the given travel time
            xdist = xspeed * travel_time

            # Minimum x distance to cover is 0, maximum is the width of
            # the screen + the distance it needs to cover
            x0 = min(-xdist, 0)
            x1 = max(sw + xdist, sw)

            # Figure out a start position between the min and max
            self.xstart = random.uniform(x0, x1)

            # If fast, this particle can begin on-screen
            if fast:
                self.ystart = random.uniform(-border, sh + border)
                self.xstart = random.uniform(0, sw)

        def update(self, st):
            # how long the particle has been on-screen for
            to = st - self.start
            self.angle += self.flutteringspeed

            xpos = self.xstart + to * self.xspeed + math.sin(self.angle)*self.fluttering
            ypos = self.ystart + to * self.yspeed

            if not self.rotate:
                sh = renpy.config.screen_height
            else:
                sh = renpy.config.screen_width

            if ypos > sh + self.border:
                # This particle can be deleted; it's past the border
                return None

            if ypos < -self.border:
                # This particle shouldn't be displayed; it's above the border
                return None

            if not self.rotate:
                return int(xpos), int(ypos), to + self.offset, self.image
            else:
                return int(ypos), int(xpos), to + self.offset, self.image
