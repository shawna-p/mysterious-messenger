# Showing CGs

**Example files to look at: [tutorial_5_coffee.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_5_coffee.rpy "tutorial_5_coffee")**

In chatrooms, sometimes characters will post images that the player can click on to view full-size. These images will also be automatically unlocked in the corresponding Album once the player has seen them.

For any CG you would like to show in-game, you must first go to [gallery_album_definitions.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/gallery.rpy "gallery_album_definitions.rpy") and define the image under the **CGs** header. For this example, a fourth CG found in the **Common** album will be added.

First, define the image:

```renpy
image cg common_4 = "CGs/common_album/cg-4.png"
```

The name of the cg must be `cg` + the name of the album it is found in, minus "album", plus an underscore and some ID such as a number or a descriptor of the cg. Other possible definitions could be

```renpy
image cg common_flower = "CGs/common_album/cg-flower.png"
image cg ju_meeting = "CGs/ju_album/ju-meeting.png"
```

After defining your image, you must add it to the correct album. See [[Adding or Removing CG Albums]] for more on creating new albums as well.

```renpy
default common_album = [
    Album("cg common_1"),
    Album("cg common_2"),
    Album("cg common_3"),
    Album("cg common_4")
]
```

In this example, no thumbnail was added. However, if you want to define a particular image thumbnail for this CG, the `Album` object might look like

```renpy
Album("cg common_4", "CGs/thumbnails/common_4_thumbnail.png")
```

The way you will show CGs differs depending on where you show it.

## Showing CGs in Chatrooms or Text Messages

To show a CG in the chatroom, simply put the name of the CG in the character's dialogue e.g.

```renpy
s "cg common_4" (img=True)
```

or

```renpy
s "common_4" (img=True)
```

You must ensure that the argument `img=True` accompanies the dialogue. The program will take care of resizing the image for the chatroom or text message and allowing the player to view it full-size. It will also unlock it in the appropriate album and notify the player if they have not yet seen the image in the album.

## Showing CGs in a Visual Novel section

All you need to do to have an image unlock after showing it in a Visual Novel section is to show it to the player. This can be done either through

```renpy
scene cg common_4
```

or

```renpy
show cg common_4
```

whichever is appropriate for that section. Unlike `show`, `scene` will clear the screen of any character sprites before showing the CG. In most cases this is what you will want.

If you need to, you can also hide the CG by writing

```renpy
hide cg
```

or by including another `scene` statement to reset the background. You can see an example of a CG posted this way in [tutorial_8_plot_branches.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_8_plot_branches.rpy "tutorial_8_plot_branches").
