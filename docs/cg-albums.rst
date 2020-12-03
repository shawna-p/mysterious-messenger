
==========
CG Albums
==========

Adding a CG Album
==================

For this tutorial, this example shows how to add a character named Emma to the game. You can view Emma's character definition and more in [[INSERT LINK HERE]].

Albums are defined in ``gallery_album_definitions.rpy``. There are two images to define and two album variables.

First, under the heading **Album Cover Images**, you will see images that look like ``cg_label_ja``. This is the background of the small label that contains the name of the album. For Emma, you will define an image like::

    image cg_label_em = "CGs/label_bg_em.webp"

The important thing is that it is called ``cg_label_em`` where ``em`` is the character's file_id. You can look at the existing images to see what they look like. The CG label is typically 241x64 px.

Below that is a set of images like ``ja_album_cover``. This is the image that will be displayed as a button to click and open the album. It typically has an image of the associated character and is 157x137 px. Emma's image definition will look like::

    image em_album_cover = "CGs/em_album_cover.webp"

The important part is that it's called ``em_album_cover`` where ``em`` is the character's file_id.

Next, you need to define two album variables. The first one, at the top, is persistent. In most cases, it will begin empty. These variables are used to keep track of which images the player has unlocked across all playthroughs.

::

    default persistent.em_album = []

The album should be the character's file_id + album, so in this case it's ``persistent.em_album``.

Similarly, Emma's regular album definition will look like::

    default em_album = []

Again, this is the character's file_id + album.

At the bottom of the file, you will also see a definition for the variable ``all_albums``. You need to add Emma's file_id here so that her album shows up in the Album screen::

    default all_albums = [
        'ju', 'z', 's', 'y', 'ja', 'v', 'u', 'r', 'common', 'em'
    ]

You can reorganize this list as you see fit. Albums are organized in rows of three on the Album screen. So, the following definition would be equally correct, depending on which characters you wanted to have albums::

    default all_albums = [
        'ju', 'z', 's', 'y', 'ja', 'em', 'common'
    ]

.. tip::
    If a player has already unlocked an image inside an album, it will be automatically added to ``all_albums``. If you're making a new route and don't want some characters' albums to appear, you must both 1) remove them from ``all_albums`` and 2) Use ``Reset Persistent`` from the Ren'Py launcher to cause Ren'Py to forget which CGs you unlocked over other routes.


Albums not Associated With Characters
-------------------------------------

If you want an album that isn't associated with any particular character, such as a "Common" album, the program expects you to follow certain naming conventions so it can find the correct album cover, label, and variables.

For example, if you wanted to add a "New Year's" album, you must do the following:

1. Add "new year's" to the ``all_albums`` definition. Capitalization doesn't matter, but note the use of double quotes (") instead of single so you don't have to escape the apostrophe.

::

    default all_albums = [
        'ju', 'z', 's', 'y', 'ja', 'v', 'u', 'r', 'common', "new year's"
    ]

2. Determine what the program will expect the variables to be called.

The program uses a specific naming scheme to process strings into file and variable names:

1. Spaces are turned into underscores (e.g. "bonus images" -> "bonus_images")
2. Apostrophes are removed (e.g. "valentine's day -> "valentines_day")
3. Entire word is in lowercase (e.g. "RFA Bonus" -> "rfa_bonus")

So, using the rules above, "new year's" in the ``all_albums`` definition will become "new_years". You can then define the two images and two album definitions like you did for Emma above::

    image cg_label_new_years = "Image for your label.png"
    image new_years_album_cover = "Image for your album cover.png"
    default persistent.new_years_album = []
    default new_years_album = []




Hiding Albums Until Unlocked
=============================

In some situations, you may want an album to not show up in the player's photo album until they have unlocked an image contained in it. For example, if you include a New Year's scenario, you may want to put related CGs in a New Year's album, but if the player hasn't unlocked or played through the New Year's scenario, you don't want the New Year's album to show up in their photo album screen.

In this case, you can use the line

::

    $ hide_albums(["new year's"])

to hide this album unless the player has unlocked a photo in it. The best place to put this is just before setting up a new route e.g.

::

    $ hide_albums(["new year's"])
    $ new_route_setup(route=my_new_route)


If the player has already unlocked images in this album, it will continue to be shown. Otherwise, this album will only appear in the player's photo album once they have unlocked an image in it (this is taken care of automatically).

Note that since you are passing a list, you can pass multiple albums to be hidden e.g.

::

    $ hide_albums(["new year's", "christmas", "b"])

