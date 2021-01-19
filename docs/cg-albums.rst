
==========
CG Albums
==========

Adding a CG Album
==================

Albums Associated a Character
-----------------------------

For this tutorial, this example shows how to add a character named Emma to the game. You can view Emma's character definition and more in :ref:`Adding a New Character to Chatrooms`.

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


Albums not Associated With a Character
---------------------------------------

If you want an album that isn't associated with any particular character, such as a "Common" album, the program expects you to follow certain naming conventions so it can find the correct album cover, label, and variables.

For example, if you wanted to add a "New Year's" album, you must do the following:

1. Add "new year's" to the ``all_albums`` definition. If a string is all lowercase, the first letter will be capitalized when it is displayed on the Album screen, but otherwise capitalization is preserved. Also note the use of double quotes (") instead of single so you don't have to escape the apostrophe.

::

    default all_albums = [
        'ju', 'z', 's', 'y', 'ja', 'v', 'u', 'r', 'common', "New Year's"
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


Adding a CG After Starting the Game
------------------------------------

While in most cases you should define your CGs in ``gallery_album_definitions.rpy``, you can also add new CGs to an album after the game has already started with the function ``add_to_album``. This function takes two parameters:

`album`
    The album variable that should contain this new CG.

    e.g. ``ja_album``

`photo_list`
    An ``Album`` or list of ``Album`` objects which should be added to the given album variable above.

    e.g. [ Album("cg s_4"), Album("cg s_5") ]

Typically you would use this function at the beginning of a route, particularly if the route is DLC since this will allow you to add images to the album without having to directly modify the ``gallery_album_definitions.rpy`` file. An example may look like::

    label new_year_prologue():

        $ new_route_setup(route=new_years_route, chatroom_label='new_year_prologue',
        participants=[ja])
        $ paraphrase_choices = True

        # Album definitions for this new route
        $ add_to_album(ja_album, Album('cg ja_ny_1'))
        $ add_to_album(ju_album, Album("cg ju_ny_1"))
        $ add_to_album(s_album, [ Album("cg s_ny_1"), Album("cg s_ny_2") ])

        $ character_list = [ju, z, s, y, ja, m]
        $ heart_point_chars = [ju, z, s, y, ja]

        # Route prologue begins here




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



Defining a CG
==============

For any CG you would like to show in-game, you must first go to ``gallery_album_definitions.rpy`` and define an image under the **CGs** header. For this example, a fourth CG in the **Common** album will be added. CG images should take up the entire screen, which is 750x1334 px. CGs of other sizes may not display correctly.

First, define the image::

    image cg common_4 = "CGs/common_album/cg-4.webp"

The name of the cg must be ``cg`` + the name of the album it is found in, minus "album", plus an underscore and some identifier for the image such as a number (``4``), or a descriptor of the CG. Other possible CG definitions might be::

    image cg common_flower = "CGs/common_album/cg-flower.webp"
    image cg ju_meeting = "CGs/ju_album/ju-meeting-office.webp"

After defining your image, you must add it to the correct album. See :ref:`Adding a CG Album` for more on creating new albums as well.

::

    default common_album = [
        Album("cg common_1"),
        Album("cg common_2"),
        Album("cg common_3"),
        Album("cg common_4")
    ]

In this example, no unique thumbnail was specified. If the program can find an image with the suffix ``-thumb`` before the file extension, it will use that as the thumbnail. So, since the image is found at "CGs/common_album/cg-4.webp", the program will look for a thumbnail image at "CGs/common_album/cg-4-thumb.webp".

Otherwise, you can also manually specify a thumbnail as the second argument to Album::

    Album("cg common_4", "CGs/thumbnails/common_4_thumbnail.webp")

Typically thumbnails are 150x150 px. If one is not provided, the given CG is cropped and resized to the appropriate size.

Large Thumbnails
-----------------

For better compatibility with the new profile picture system, you may also want to provide a "larger" version of a thumbnail for use in profile pictures on the profile screen. The program will search for an image with the name of the thumbnail + the suffix ``-b`` before the file extension. So, if our "cg common_4" isn't given a different thumbnail, it will look for the large version of the thumbnail at "CGs/common_album/cg-4-thumb-b.webp".

If you provided a different thumbnail, as in ``Album("cg common_4", "CGs/thumbnails/common_4_thumbnail.webp")``, then the large version is expected to be called "CGs/thumbnails/common_4_thumbnail-b.webp".


Showing a CG in a Chatroom or Text Message
===========================================

In chatrooms or text messages, sometimes characters will post images that the player can click on the view full-size. These images will automatically be unlocked in the appropriate Album once the player has seen them.

To show a CG in the chatroom, put the name of the CG in the character's dialogue e.g.

::

    s "cg common_4" (img=True)
    # or with the msg CDS
    msg s "cg common_4" img

You can also omit ``cg `` at the beginning, so long as you remember to mark it as an image::

    y "common_4" (img=True)
    msg z "common_4" img

The program will take care of resizing the CG for the chatroom and allowing the player to view it full-size. It will also unlock the CG in the appropriate album and notify the player if they have not yet seen the image in the album. If this is the first time the player has seen this image, it will also become available for use as a bonus profile picture (see :ref:`Bonus Profile Pictures`).

You can see an example of a CG posted in a text message in ``tutorial_3b_VN.rpy``, and an example of a CG posted during a chatroom in ``tutorial_5_coffee.rpy``.


Showing a CG during Story Mode
===============================

All you need to do to have an image unlock after showing it in a Story Mode section is to show it to the player. This can be done through the ``scene`` or ``show`` statements. ``scene`` will clear the screen of any existing character sprites/backgrounds etc before showing the image.

::

    ju "I wanted to show you how the lounge has been decorated."
    scene cg common_4
    show jumin front neutral
    ju "Do you like it?"

or

::

    ja "Oh, no, I've spilled the flour everywhere."
    show cg common_4
    ja "Could you get something to clean this up with?"

In most cases, you will probably use ``scene`` to show a CG image to the player instead of ``show``.

The CG can be cleared from the screen either by replacing it with another ``scene`` statement or by explicitly hiding it with ``hide cg``::

    u "I wanted to show you how the lounge has been decorated."
    scene cg common_4
    show jumin front neutral
    ju "Do you like it?"
    scene bg meeting_room # This clears the CG from the screen
    ju "I think it turned out rather well."

or

::

    ja "Oh, no, I've spilled the flour everywhere."
    show cg common_4
    ja "Could you get something to clean this up with?"
    hide cg # This clears the CG from the screen
    show jaehee happy
    ja "I'm sorry for the trouble."

You can see an example of a CG posted during a Story Mode section in ``tutorial_8_plot_branches.rpy``.

