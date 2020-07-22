# Chip thoughts are organized in a tuple with three items:
# The description, approximate number of hearts, and number of hourglasses
default chip_prize_list = RandomBag( [
    ('A clump of cat hair.', 30, 0),
    ("Jumin's old toothbrush.", 20, 0),
    ("Some Honey Buddha Chip crumbs.", 24, 0),
    ("Jaehee's spare pair of glasses.", 65, 0),
    ("Yoosung's left sock.", 33, 0),
    ("Your middle school photo album!", 19, 0),
    ("Toothpaste that tastes like Honey Buddha Chips", 69, 0),
    ("A completion certificate for mid-level dating.", 100, 0),
    ("It's a present for you.", 67, 0),
    ("A very normal industrial product.", 86, 0),
    ("This Honey Boss Chip began in 1987 England...", 34, 0),
    ("Disco lights! Let's dance!", 69, 0),
    ("Yoosung's blessed hair strands. Blow on it and make a wish!", 443, 4),
    ("A chip bag full of chip dust", 10, 0),
    ("There's mold on these...", 19, 0)
    # Feel free to add more things
    ] )

            
# This is what a list of thoughts for the spaceship will 
# look like
default space_thoughts = RandomBag( [
    SpaceThought(ja, "I should have broken these shoes in better before wearing them to work today."),
    SpaceThought(ju, "I wonder how Elizabeth the 3rd is doing at home."),
    SpaceThought(s, "Maybe I should Noogle how to get chip crumbs out of my keyboard..."),
    SpaceThought(y, "Yes! Chocolate milk is on sale!"),
    SpaceThought(z, "Maybe I should learn how to braid my hair..."),
    SpaceThought(r, "I can't believe I accidentally used one of the other Believer's shampoo. My hair smells like lemons."),
    SpaceThought(ri, "Hmm... the soup tastes different today."),
    SpaceThought(sa, "So... sleepy..."),
    SpaceThought(v, "The weather is so very lovely today. Maybe I'll go for a walk.") 
    ] )

## ********************************
## Spaceship on the chat hub
## ********************************
image space_chip_active:
    "Menu Screens/Spaceship/spaceship_chip_inactive.png"
    2.7
    block:
        "Menu Screens/Spaceship/spaceship_chip_active.png"
        1.16
        "Menu Screens/Spaceship/spaceship_chip_glow.png"
        1.16
        repeat
image space_chip_active2:
    "Menu Screens/Spaceship/spaceship_chip_active.png"
    1.16
    "Menu Screens/Spaceship/spaceship_chip_glow.png"
    1.16
    repeat    
image space_chip_explode = "Menu Screens/Spaceship/spaceship_chip_explode.png"
image space_chip_inactive = "Menu Screens/Spaceship/spaceship_chip_inactive.png"
image space_dot_line = "Menu Screens/Spaceship/dot_line.png"
image space_gray_dot = "Menu Screens/Spaceship/spaceship_dot_white.png"
image space_yellow_dot = "Menu Screens/Spaceship/spaceship_dot_yellow.png"
image space_transparent_btn = "Menu Screens/Spaceship/space-transparent-button.png"
image spaceship = "Menu Screens/Spaceship/spaceship_craft.png"
image space_flame:
    "Menu Screens/Spaceship/spaceship_flame_big.png"
    0.6
    "Menu Screens/Spaceship/spaceship_flame_small.png"
    0.6
    repeat

## ********************************
## Spaceship chip animations
## ********************************

image space_chip = "Menu Screens/Spaceship/chip.png"
image space_tap_large:
    "Menu Screens/Spaceship/tap_0.png"
    0.55
    "Menu Screens/Spaceship/tap_1.png"
    0.6
    repeat
image space_tap_med:
    "Menu Screens/Spaceship/tap_1.png"
    0.62
    "Menu Screens/Spaceship/tap_0.png"
    0.45
    repeat
image space_tap_small:
    "Menu Screens/Spaceship/tap_0.png"
    0.48
    "Menu Screens/Spaceship/tap_1.png"
    0.56
    repeat    
image space_tap_to_close = "Menu Screens/Spaceship/close.png"

image cloud_1 = "Menu Screens/Spaceship/cloud_1.png"
image cloud_2 = "Menu Screens/Spaceship/cloud_2.png"
image cloud_3 = "Menu Screens/Spaceship/cloud_3.png"
image cloud_4 = "Menu Screens/Spaceship/cloud_4.png"
image cloud_5 = "Menu Screens/Spaceship/cloud_5.png"

image space_spotlight = "Menu Screens/Spaceship/spotlight.png"

image spotlight:
    'space_spotlight'
    alpha 0.6
    block:
        rotate 0
        linear 15.0 rotate 360
        repeat
        
image space_prize_box = "Menu Screens/Spaceship/space_prize_box.png"
image space_black_box = Frame("Menu Screens/Spaceship/main03_black_box.png",30,30,30,30)
image space_continue = "Menu Screens/Spaceship/Continue.png"
image space_continue_hover = "Menu Screens/Spaceship/Continue_hover.png"

