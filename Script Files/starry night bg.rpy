init -1 python:

    # Picks a random position for the star to appear at
    def star_func(trans,st,at):
        trans.ypos = renpy.random.random()
        trans.xpos = renpy.random.random()
        return None
        
# A starry night background with some static stars
image bg starry_night = "Phone UI/bg-starry-night.png"

# These are the stars that will be animated
image small star:
    function star_func
    block:
        "transparent.png" with Dissolve(1.0, alpha=True)
        0.9
        "Phone UI/small-star.png" with Dissolve(1.0, alpha=True)
        # This just tells the program to pick a number between 6 and 12
        # and then wait that many seconds before continuing with the animation
        renpy.random.randint(6, 11)
        repeat
        
image medium star:
    function star_func
    block:
        "Phone UI/medium-star.png" with Dissolve(1.0, alpha=True)
        renpy.random.randint(6, 12)
        "transparent.png" with Dissolve(1.0, alpha=True)
        1.3
        repeat
        
image big star:
    function star_func
    block:
        "Phone UI/big-star.png" with Dissolve(1.0, alpha=True)
        renpy.random.randint(7, 13)
        "transparent.png" with Dissolve(1.0, alpha=True)
        1.5
        repeat

# This makes it easier to call the starry night background
screen starry_night:
    image "bg starry_night"
    image "small star"
    image "small star"
    image "small star"
    image "medium star"
    image "medium star"
    image "medium star"
    image "big star"