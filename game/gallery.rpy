python early:

    class Album(renpy.store.object):
        """
        Class which holds the information needed to display all the CGs
        associated with a certain album.

        Attributes:
        -----------
        img : string
            The image name of the Displayable to use.
        locked_img : string
            The file path to the image that will be used as the "locked"
            thumbnail icon.
        thumbnail : string
            The file path to the image that will be used for the thumbnail.
        unlocked : bool
            True if this image can be viewed by the player.
        seen_in_album : bool
            True if this image has been viewed full-screen in the album.
        """

        def __init__(self, img, thumbnail=False,
                    locked_img="CGs/album_unlock.png"):
            """
            Creates an Album object to store information about gallery images.

            Parameters:
            -----------
            img : string
                The image name of the Displayable to use. Typically 750x1334px.
            thumbnail : string
                The file path to the image that will be used for the thumbnail.
                Should be 155x155px.
            locked_img : string
                The file path to the image that will be used in the "locked"
                thumbnail icon. Should be 155x155px.
            """

            self.img = img
            self.__locked_img = locked_img
            if thumbnail:
                self.__thumbnail = thumbnail
            else:
                if self.filename:
                    thumb_name = self.filename.split('.')
                    thumbnail = thumb_name[0] + '-thumb.' + thumb_name[1]
                    if renpy.loadable(thumbnail):
                        self.__thumbnail = thumbnail
                    else:
                        thumbnail = False
                if not thumbnail:
                    # If no thumbnail is provided, the program
                    # will automatically crop and scale the CG
                    self.__thumbnail = Transform(Crop((0, 200, 750, 750), img),
                                                        size=(155,155))
            self.unlocked = False
            self.__seen_in_album = False

        @property
        def filename(self):
            """Return the file name (including extension) for this image."""
            if '.' in self.img:
                return self.img
            try:
                return renpy.display.image.get_registered_image(self.img).filename
            except:
                print("WARNING: Could not retrieve filename associated with",
                    self.img)
            return False

        def unlock(self):
            """Unlock this image in the album."""

            if not self.unlocked:
                self.unlocked = True
                # Set a var so Album shows "NEW"
                store.new_cg += 1
                # Add this to the list of unlocked profile pictures
                if self.__thumbnail not in store.persistent.unlocked_prof_pics:
                    store.persistent.unlocked_prof_pics.append(
                        self.__thumbnail)
            renpy.retain_after_load()

        @property
        def thumbnail(self):
            """Return the correct thumbnail for this image."""

            if self.unlocked:
                return self.__thumbnail
            else:
                return self.__locked_img

        @thumbnail.setter
        def thumbnail(self, new_thumb):
            self.__thumbnail = new_thumb

        def get_thumb(self):
            """Retrieve the CG's thumbnail, regardless of its unlock state."""

            return self.__thumbnail

        def check_if_seen(self):
            """
            Check if this image was shown to the player and if so, unlock it.
            """

            if renpy.seen_image(self.img):
                self.unlock()

        @property
        def seen_in_album(self):
            return self.__seen_in_album

        @seen_in_album.setter
        def seen_in_album(self, new_bool):
            """Sets whether this image has been seen in the album yet."""

            if getattr(store, 'new_cg', False) and not self.__seen_in_album:
                if new_bool:
                    store.new_cg -= 1
            self.__seen_in_album = new_bool

        def __eq__(self, other):
            """Checks for equality between two Album objects."""

            if getattr(other, 'img', False):
                return self.img == other.img
            else:
                return False

        def __ne__(self, other):
            """Checks for equality between two Album objects."""

            if getattr(other, 'img', False):
                return self.img != other.img
            else:
                return False

init python:

    import string

    def merge_albums(p_album, update):
        """
        Update p_album to have the same items as update. Ensures that the
        unlocked status of the photo is preserved.
        """

        # Add photos in update to p_album
        for photo in update:
            if photo not in p_album:
                p_album.append(photo)
            else:
                # Ensure thumbnails are updated
                for p_photo in p_album:
                    if photo == p_photo:
                        p_photo.thumbnail = photo.get_thumb()
                        break
        # Remove photos in p_album that aren't in update
        for photo in p_album:
            if photo not in update:
                p_album.remove(photo)
        return p_album

    def merge_albums_string(alb):
        """Update persistent albums to be consistent with regular albums."""

        if alb[-6:] != "_album":
            alb += "_album"
        reg_album = getattr(store, convert_to_file_name(alb))
        per_album = getattr(store.persistent, convert_to_file_name(alb))

        merge_albums(per_album, reg_album)

    def check_for_CGs(all_albums):
        """Make sure all seen images are unlocked in the player's album."""

        if isinstance(all_albums[0], list):
            for p, a in all_albums:
                # Only need to go through persistent albums
                for cg in p:
                    cg.check_if_seen()
        else:
            for alb in all_albums:
                a = alb
                if alb[-6:] != "_album":
                    a += "_album"
                per_album = getattr(store.persistent, convert_to_file_name(a))
                for cg in per_album:
                    cg.check_if_seen()
        return

    def add_to_album(album, photo_list):
        """Add the photos in photo_list to album."""

        for photo in photo_list:
            if photo not in album:
                album.append(photo)

    def has_unseen(album):
        """Return True if an album has a photo that hasn't been seen."""

        for photo in album:
            if not photo.seen_in_album and photo.unlocked:
                return True
        return False

    def get_char_from_file_id(file_id):
        """
        Return the character name associated with the given file_id, or a
        capitalized version of the file_id otherwise.

        Used to retrieve Album titles/labels.
        """

        try:
            char = getattr(store, file_id)
            return char.name
        except AttributeError:
            for char in store.all_characters:
                if char.file_id == file_id:
                    return char.name

        return string.capwords(file_id)

    def convert_to_file_name(file_id):
        """Convert file_id into a computer-readable format for file names."""

        new_id = file_id

        if ' ' in file_id:
            new_id = new_id.replace(' ', '_')
        if "'" in file_id:
            new_id = new_id.replace("'", "")

        return new_id.lower()


    def hide_albums(album_list):
        """Hide the albums in album_list unless they have an unlocked photo."""

        global all_albums
        has_unlocked = False

        for album in album_list:
            for photo in getattr(store.persistent, album + "_album"):
                if photo.unlocked:
                    # This album can remain visible
                    has_unlocked = True
                    break
            if not has_unlocked:
                # None of the photos in this album are unlocked;
                # it shouldn't be visible in all_albums
                if album in all_albums:
                    all_albums.remove(album)
            has_unlocked = False



    def drag_box(drags, drop):
        """
        A callback for the translucent image displayed on top of the CGs
        when viewed full-screen. It is draggable to the left and right of
        the screen, and if a drop is successful, it displays the next or
        previous available album image.
        """

        global album_info_for_CG, fullsizeCG, swipe_anim
        global prev_cg_left, prev_cg_right
        al = album_info_for_CG[0]
        ind = album_info_for_CG[3]

        # If the player somehow didn't swipe far enough, ignore
        # their swipe
        if not drop:
            for item in drags:
                item.snap(0, 0)

        else:
            for item in drags:
                # Moves the translucent image back to its
                # default position
                item.snap(0, 0)

            if drop.drag_name == "Right":
                # The album goes back one item
                # First check if it's the first item
                found_item = False
                if len(al) > 0 and ind > 0:
                    # Now go backwards until it hits the beginning of
                    # the album or an unlocked CG
                    for i in range(ind-1, -1, -1):
                        if al[i].unlocked:
                            prev_cg_right = fullsizeCG
                            fullsizeCG = al[i].img
                            al[i].seen_in_album = True
                            album_info_for_CG[3] = i
                            found_item = True
                            if swipe_anim == "right":
                                swipe_anim = "right2"
                            else:
                                swipe_anim = "right"
                            break

            elif drop.drag_name == "Left":
                # Go forward one item
                # Check if it's the last item
                found_item = False
                if len(al) - 1 > ind:
                    # Now go forwards until it hits the end of the album
                    # or an unlocked CG
                    for i in range(ind+1, len(al)):
                        if al[i].unlocked:
                            prev_cg_left = fullsizeCG
                            fullsizeCG = al[i].img
                            al[i].seen_in_album = True
                            album_info_for_CG[3] = i
                            found_item = True
                            if swipe_anim == "left":
                                swipe_anim = "left2"
                            else:
                                swipe_anim = "left"
                            break

            renpy.restart_interaction()

    def toggle_close_drag():
        """A callback to hide or show the 'Close' sign."""

        store.close_visible = not close_visible
        renpy.restart_interaction()




default fullsizeCG = "cg common_1"
# This lets the player know if there are new CGs in
# the album
default new_cg = 0

image cg_frame = 'CGs/photo_frame.png'
image cg_frame_dark = 'CGs/photo_frame_dark.png'

image translucent_img = 'translucent.png'

## This screen shows all of the various characters/folders
## available in the photo gallery
screen photo_album():

    # Ensure this replaces the main menu.
    tag menu

    if not main_menu:
        on 'replace' action FileSave(mm_auto, confirm=False)
        on 'show' action FileSave(mm_auto, confirm=False)

    python:
        if main_menu:
            return_action = Show('select_history', Dissolve(0.5))
        else:
            return_action = Show('chat_home', Dissolve(0.5))

        grid_row = -(-len(all_albums) // 3)
        full_grids = (len(all_albums) // 3) * 3

        null_height = (((1170 - (220*grid_row) - (40*(grid_row-1))) // 2) - 50)

    use menu_header('Photo Album', return_action):

        if isinstance(all_albums[0], list):
            # Retained for backwards compatibility. Displays the albums.
            frame:
                xysize (750, 1170)
                align (0.5, 0.5)
                has vbox
                align (0.5, 0.4)
                spacing 40
                # Each hbox can have a maximum of 3 characters in it, but you can
                # have less than three as well. You can also add another row by
                # adding another hbox
                hbox:
                    use char_album('cg_label_ju', 'Jumin Han',
                                    persistent.ju_album, 'ju_album_cover')
                    use char_album('cg_label_z', 'ZEN',
                                    persistent.z_album, 'z_album_cover')
                    use char_album('cg_label_s', '707',
                                    persistent.s_album, 's_album_cover')
                hbox:
                    use char_album('cg_label_y', 'Yoosung★',
                                    persistent.y_album, 'y_album_cover')
                    use char_album('cg_label_ja', 'Jaehee Kang',
                                    persistent.ja_album, 'ja_album_cover')
                    use char_album('cg_label_v', 'V',
                                    persistent.v_album, 'v_album_cover')
                hbox:
                    use char_album('cg_label_u', 'Unknown',
                                    persistent.u_album, 'u_album_cover')
                    use char_album('cg_label_r', 'Ray',
                                    persistent.r_album, 'r_album_cover')
                    use char_album('cg_label_common', 'Common',
                                    persistent.common_album, 'common_album_cover')
        else:
            viewport:
                draggable True
                mousewheel True
                scrollbars "vertical"
                align (0.5, 0.5)
                xysize(750, 1170)

                has vbox
                # Centers the grid in the viewport, if necessary
                if null_height > 0:
                    null height null_height

                grid 5 grid_row:
                    align (0.5, 0.5)
                    # Negative xspacing allows the program to center
                    # two items below a row of 3, if necessary
                    xspacing -134
                    yspacing 40
                    for i in range(0, full_grids, 3):
                        use char_album(all_albums[i])
                        null
                        use char_album(all_albums[i+1])
                        null
                        use char_album(all_albums[i+2])

                    # Fill in uneven grid spots
                    if len(all_albums) % 3 == 2:
                        null
                        use char_album(all_albums[-2])
                        null
                        use char_album(all_albums[-1])
                        null
                    elif len(all_albums) % 3 == 1:
                        null
                        null
                        use char_album(all_albums[-1])
                        null
                        null





## This displays a button with an image and a caption
## that will take you to the desired character's album
screen char_album(caption, name=None, album=None, cover=None):

    python:
        if name is None:
            # Caption is actually the file_id
            file_id = caption
            caption = 'cg_label_' + convert_to_file_name(file_id)
            name = get_char_from_file_id(file_id)
            album = getattr(store.persistent,
                    convert_to_file_name(file_id) + "_album")
            cover = convert_to_file_name(file_id) + "_album_cover"


    button:
        vbox:
            spacing 5
            xsize 245

            fixed:
                xysize (175, 150)
                align (0.5, 0.5)
                ## Window with the tilted image
                frame at album_tilt:
                    xysize (157, 137)
                    foreground 'cg_frame_dark'
                    background cover
                    align (1.0, 0.0)
                    xoffset 35
                    yoffset -42

                ## Window with the framed image
                frame:
                    xysize (157, 137)
                    foreground 'cg_frame'
                    background cover
                    align (0.5, 0.5)

                if has_unseen(album):
                    add 'new_sign' align (1.0, 0.0)

            frame:
                xysize (241, 64)
                background caption
                hover_foreground caption
                if len(name) > 6:
                    text name + ' (' + str(len(album)) + ')':
                        style 'album_text_long'
                else:
                    text name + ' (' + str(len(album)) + ')':
                        style 'album_text_short'

        action Show('character_gallery', album=album,
                                caption=caption, name=name)



## This screen shows individual images unlocked for each character
screen character_gallery(album, caption, name):

    tag menu
    $ num_rows = max(len(album) // 4 + (len(album) % 4 > 0), 1)

    use menu_header('Photo Album', Show('photo_album', Dissolve(0.5))):

        vbox:
            align (0.5, 1.0)
            xysize (745, 1170)
            spacing 5
            frame:
                xysize (241, 64)
                xalign 0.01
                add caption
                if len(name) > 6:
                    text name + ' (' + str(len(album)) + ')':
                        style 'album_text_long'
                else:
                    text name + ' (' + str(len(album)) + ')':
                        style 'album_text_short'

            vpgrid id 'gallery_vp':
                xysize (740, 1100)
                yfill True
                rows num_rows
                cols 4
                draggable True
                mousewheel True
                if len(album):
                    scrollbars "vertical"
                side_xalign 1.0
                side_spacing 15
                align (0.5, 0.0)
                spacing 20


                for index, photo in enumerate(album):
                    imagebutton:
                        idle photo.thumbnail
                        if not photo.seen_in_album and photo.unlocked:
                            foreground 'new_sign'
                        action If(photo.unlocked,
                            [SetVariable("fullsizeCG", photo.img),
                            SetField(photo, 'seen_in_album', True),
                            SetVariable('close_visible', True),
                            SetVariable('album_info_for_CG',
                                [album, caption, name, index]),
                            Show('viewCG_fullsize_album', album=album,
                                caption=caption, name=name)],

                            CConfirm("This image is not yet unlocked"))

                # This fills out the rest of the grid
                for i in range((4*num_rows) - len(album)):
                    null

style album_text_short:
    align (0.5, 0.5)
    text_align 0.5
    color '#fff'
    font gui.sans_serif_1
    size 30

style album_text_long:
    align (0.5, 0.5)
    text_align 0.5
    color '#fff'
    font gui.sans_serif_1
    size 25

## Some additional variables specifically used
## for the next label and screen
default album_info_for_CG = []
default swipe_anim = False
default prev_cg_right = False
default prev_cg_left = False

## This is the screen where you can view a full-sized CG when you
## click it. It has a working "Close" button that appears/disappears
## when you click the CG. This particular variant lets the player
## "swipe" to view the various images without backing out to the
## album screen to switch between them
screen viewCG_fullsize_album(album, caption, name):
    zorder 5
    tag menu

    use starry_night()

    # This draggroup defines two hotspots on the left and
    # right side of the screen to detect which direction
    # the CG has been dragged. 'the_CG' is actually just a
    # nearly-transparent overlay that the player drags onto
    # the left or right side of the screen
    draggroup:
        drag:
            drag_name "Left"
            child Transform('translucent_img', size=(70,1334))
            draggable False
            xalign 0.0
        drag:
            drag_name "Right"
            draggable False
            child Transform('translucent_img', size=(70, 1334))
            xalign 1.0
        drag:
            drag_name "the_CG"
            drag_handle (0, 0, 750, 1334)
            child 'translucent_img'
            dragged drag_box
            droppable False
            clicked toggle_close_drag
            drag_offscreen True
            xalign 0.5
            yalign 0.5

    # This slightly repetitive code makes the program
    # animate in the "swipes" as the player goes through
    # the album
    # Ren'Py will only animate if the animation is different,
    # which is why there are two "left"s and "right"s
    if swipe_anim == "left":
        if prev_cg_left:
            add prev_cg_left at cg_swipe_left_hide
            add fullsizeCG at cg_swipe_left
        else:
            add fullsizeCG
    elif swipe_anim == "right":
        if prev_cg_right:
            add prev_cg_right at cg_swipe_right_hide
            add fullsizeCG at cg_swipe_right
        else:
            add fullsizeCG
    elif swipe_anim == "left2":
        if prev_cg_left:
            add prev_cg_left at cg_swipe_left_hide
            add fullsizeCG at cg_swipe_left2
        else:
            add fullsizeCG
    elif swipe_anim == "right2":
        if prev_cg_right:
            add prev_cg_right at cg_swipe_right_hide
            add fullsizeCG at cg_swipe_right2
        else:
            add fullsizeCG
    else:
        add fullsizeCG

    # Show the close button if it's visible
    if close_visible:
        imagebutton:
            xalign 0.5
            yalign 0.0
            focus_mask True
            idle "close_button"
            action [SetVariable('prev_cg_left', False),
                    SetVariable('prev_cg_right', False),
                    Show('character_gallery', album=album,
                        caption=caption, name=name)]

        text "Close" style "CG_close":
            if persistent.dialogue_outlines:
                outlines [ (2, "#000",
                            absolute(0), absolute(0)) ]
                font gui.sans_serif_1b

