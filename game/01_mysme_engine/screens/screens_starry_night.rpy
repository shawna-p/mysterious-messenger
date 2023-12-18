init -1 python:

    def create_snight_manager():
        """
        Create and return a SpriteManager object based on the list of StarSprite
        objects passed in. Also positions each individual sprite at a random
        x, y position based on the attributes of the StarSprite.
        """
        # Add them all to the sprite manager
        star_sprites = [ ]

        # The range of where the star can be on-screen
        xran = config.screen_width // 3
        yran = (config.screen_height) // 4

        for i in range(2):
            for x in range(3):
                for y in range(4):
                    for star_type in ['medium', 'small']:
                        star_sprites.append(StarSprite(
                            '{}_star_static'.format(star_type),
                            star_twinkle_quickly, 0, 0,
                            x*xran, x*xran+xran,
                            y*yran, y*yran+yran))

        return create_star_manager(star_sprites)

transform star_twinkle_quickly(num1):
    alpha 0.6
    block:
        ease 0.6 + renpy.random.random() alpha 0.6
        linear renpy.random.randint(3, 12) + renpy.random.random()
        ease 0.5 + renpy.random.random() alpha 0.0
        linear 0.3
        repeat

## These are the stars that will be animated
image small_star_static = "Menu Screens/Main Menu/small-star.webp"
image medium_star_static = "Menu Screens/Main Menu/medium-star.webp"
## The actual background image; used for the menu screens and also text messages
image starry_night_img = Composite(
    (config.screen_width, config.screen_height),
    (0, 0), "#000",
    (0, 0), "bg starry_night",
    (0, 0), create_snight_manager(),
)

# This makes it easier to use the starry night background
screen starry_night():
    add 'starry_night_img'
    add Transform("#000", alpha=persistent.starry_contrast)

image load_circle:
    'loading_circle_stationary'
    block:
        rotate 0
        linear 2.0 rotate 360
        repeat

image load_tip = "Menu Screens/Main Menu/loading_tip.webp"
image load_close = "Menu Screens/Main Menu/loading_close.webp"
image load_tip_panel = Frame("Menu Screens/Main Menu/loading_tip_panel.webp", 300,100,80,80)


## This ensures that the player has to set up their profile
## the very first time they open the game
label before_main_menu():
    if persistent.first_boot:
        call screen profile_pic
    $ define_variables(unlock_pics=False)
    return

screen loading_screen():

    zorder 90
    tag menu

    use starry_night()

    frame:
        maximum(600,320)
        xalign 0.5
        yalign 0.42
        add "load_tip_panel"

    frame:
        maximum(540, 140)
        xalign 0.5
        yalign 0.445
        text renpy.random.choice(loading_tips) style "loading_tip"

    text "Loading..." style "loading_text"

    add 'load_circle' xalign 0.5 yalign 0.745
    imagebutton:
        xalign 0.966
        yalign 0.018
        idle 'load_close'
        hover Transform('load_close', zoom=1.05)
        action [Return()]


    add 'load_tip 'xalign 0.13 yalign 0.32

style loading_text:
    xalign 0.5
    yalign 0.607
    color "#fff"
    text_align 0.5
    font gui.sans_serif_1
    size 34

style loading_tip:
    xalign 0.5
    text_align 0.5
    yalign 0.4
    color "#fff"
    font gui.sans_serif_1
    size 34

