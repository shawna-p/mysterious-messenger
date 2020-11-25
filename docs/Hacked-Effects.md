# Hacked Effects

In your route, you may want to cause the program to appear as though it has been hacked. There are a few features to help you achieve this look. First, there is a variable called `hacked_effect` that, if set to `True`, will cause the chatroom timeline to have additional "broken" backgrounds, and will also show a glitchy screen tear effect every 10 seconds or so. You can set this variable to `True` at any point during your route; simply including the line

```
$ hacked_effect = True
```

in an `after_` label, for example, will activate it. Similarly, `$ hacked_effect = False` will get rid of these effects.

While you are testing a route, there is also an option to toggle the `hacked_effect` on/off in the **Developer** settings from the chat hub screen.

**Note:** Many players may find the hacked effects distracting or irritating, so they should be used sparingly. There are also options in the Settings screen to turn off these effects, so know that not every player will be able to see or appreciate these effects.

## The tear screen

There is a special screen called the `tear` screen which will cause the screen to be split into several smaller pieces that are offset a little from their original position. It's used to create the hacked effect in the chatroom timeline screen, but can also be shown in the middle of any ordinary chatroom/phone call/VN Mode/etc. You can call it like so:

```renpy
call tear_screen(number=10, offtimeMult=0.4, ontimeMult=0.4, 
    offsetMin=-10, offsetMax=30, w_timer=0.18, p=0.5)
```

where `10` is the number of pieces to tear; `0.4` is the value for both `offtimeMult` and `ontimeMult` respectively -- this controls how much the pieces bounce back and forth; `-10` is the minimum offset for the pieces (this can be negative, positive, or zero); `30` is the maximum offset for the pieces (can also be negative, positive, or zero; offset just means how far the pieces will move away from their origin point, in pixels); and `0.5` is how long the program should display the tear screen for before hiding.

You can also briefly show an image on-screen before showing the tear screen in order to have that image "torn" as well. For this, you can use the special screen `display_img`:

```renpy
show screen display_img([ ['vn_party', 200, 400] ])
pause 0.0001
call tear_screen(40, 0.4, 0.2, -100, 100, 0.3, 0.3)
hide screen display_img
```

The `display_img` screen will show an image in the specified position. It takes a lists of lists as its sole parameter. Each item in the list should be a list of three items: the image to display (which can be the name of a previously declared image, as above, a string with a path to the file name, or a Transform with the image, among other things), then the xpos, and then the ypos. So, in this case, the program displays the image `'vn_party'` at an xpos of 200 and a ypos of 400.

The short pause after showing the `display_img` screen gives the program enough time to register the images before it takes a screenshot for the tear screen. Call the tear screen as normal. Be sure to hide the `display_img` screen at the end.

## The hack_rectangle screen

The `hack_rectangle` screen will also help create a "hacked" effect. It will show several random rectangles on the screen, and works well when paired with the tear screen. For example:

```renpy
call hack_rectangle_screen(t=0.2, p=0.01)
call tear_screen(number=10, offtimeMult=0.4, ontimeMult=0.2,
    offsetMin=-10, offsetMax=30, w_timer=0.18, p=0.18)
```

This will show the `hack_rectangle` screen for 0.2 seconds (`t=0.2`), and after pausing for 0.01 seconds (`p=0.01`) to give the program time to register the images on-screen, it shows the `tear` screen for 0.18 seconds.

## Static white squares

The program also has a screen called `white_squares` which randomly shows a sequence of white "static" squares on top of the screen. It is used for the chatroom select screen when `hacked_effect` is True. To call it, use

```renpy
call white_square_screen(t=0.16, p=0.17)
```

where `t=0.16` is how long to show the screen for (0.16 seconds) and `p=0.17` tells the program how long to pause for before continuing (0.17 seconds).

## Inverting the screen colours

Finally, there is also a screen called `invert` which will take a screenshot of the currently displayed screen and invert the colours:

```renpy
call invert_screen(t=0.19, p=0.2)
```

where `t=0.19` is how long to show the screen for (0.19 seconds) and `p=0.2` is how long the program should pause for before continuing (0.2 seconds). This works well with screens that were previously mentioned. For example:

```renpy
call hack_rectangle_screen(t=0.2, p=0.01)
call invert_screen(t=0.19, p=0.01)
call tear_screen(number=10, offtimeMult=0.4, ontimeMult=0.2, 
            offsetMin=-10, offsetMax=30, w_timer=0.18, p=0.01)
call white_square_screen(t=0.16, p=0.17)
```
