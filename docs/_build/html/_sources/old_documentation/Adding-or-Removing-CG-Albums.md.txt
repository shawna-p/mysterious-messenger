# Adding or Removing CG Albums

For the purposes of this tutorial, these examples will show how to add a character named Bob to the program.

First, go to [gallery_album_definitions.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/gallery._album_definitionsrpy "gallery._album_definitionsrpy"). Here, you can define two images for Bob's album. The first is the background for the label under the album icon. Under the heading **Album Cover Images** you will see several image definitions that look like `cg_label_ja` and `cg_label_common`. If you want a custom label for Bob's album, define an image here e.g.

```renpy
image cg_label_b = "CGs/label_bg_b.png"
```

Next, a little further down, there are image definitions for the album covers such as `ja_album_cover` and `common_album_cover`. In-game these images are 157x138 pixels and are typically a picture of the character. Define an image here for Bob's album e.g.

```renpy
image b_album_cover = "CGs/b_album_cover.png"
```

Then under the heading **Album Declarations** you will see a list of definitions that begin with `default persistent.` and a list of identical definitions without the `persistent.` prefix. In order to make the albums expandable, you need to define one of each for a new album.

To define albums for Bob, add the line

```renpy
default persistent.b_album = []
```

under the persistent definitions, and then add

```renpy
default b_album = []
```

under the regular definitions. The name of this album should be the ChatCharacters's file_id + "_album", so for Bob it is `b_album`.

Next, in the definition for `all_albums`, you need to add Bob's file_id e.g.

```renpy
default all_albums = [
    'ju', 'z', 's', 'y', 'ja', 'v', 'u', 'r', 'common', 'b'
]
```

This will ensure Bob's album stays up-to-date if you add images to it.

If you've set everything up with the correct names, Bob should now have a working album when you click the Album button from the chat home screen. See [Showing CGs](Showing-CGs.md) for more information on adding CGs to the album and showing them in-game.


## Albums not associated with characters

If you want an album not associated with a character, there are some naming conventions you must follow so the program can find the correct files.

For example, if you want to add a "New Year's" album, you must do the following:

1. Add "new year's" to the `all_albums` definition. Capitalization doesn't matter, but note the use of double quotes (") instead of single so you don't have to escape the apostrophe.

```renpy
default all_albums = [
    'ju', 'z', 's', 'y', 'ja', 'v', 'u', 'r', 'common', "new year's"
]
```

2. Define your images as mentioned above using a certain naming scheme:
   1. Spaces will be turned into underscores
   2. Apostrophes will be removed
   3. Entire definition is in lowercase

So, your images for the "New Year's" will be found under `new_years` like Bob's was found under `b`:

```renpy
image cg_label_new_years = "Image for your label.png"
image new_years_album_cover = "Image for your album cover.png"
default persistent.new_years_album = []
default new_years_album = []
```

## Hiding Albums Until Unlocked

In some situations, you may want an album to not show up in the player's photo album until they have unlocked an image contained in it. For example, if you include a New Year's scenario, you may want to put related CGs in a New Year's album, but if the player hasn't unlocked or played through the New Year's scenario, you don't want the New Year's album to show up in their photo album screen.

In this case, you can use the line

```renpy
$ hide_albums(["new year's"])
```

to hide this album unless the player has unlocked a photo in it. The best place to put this is just before setting up a new route e.g.

```renpy
$ hide_albums(["new year's"])
$ new_route_setup(route=my_new_route)
```

If the player has already unlocked images in this album, it will continue to be shown. Otherwise, this album will only appear in the player's photo album once they have unlocked an image in it (this is taken care of automatically).

Note that since you are passing a list, you can pass multiple albums to be hidden e.g.

```renpy
$ hide_albums(["new year's", "christmas", "b"])
```
