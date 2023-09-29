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
        thumbnail_tuple : tuple (string, tuple, bool)
            A tuple which can be saved in a persistent set for unlockable
            profile pictures denoting how an image is to be cropped.
        """

        def __init__(self, img, thumbnail=False,
                    locked_img="CGs/album_unlock.webp",
                    chat_img=None,
                    chat_thumb=None):
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
            chat_img : Displayable
                A displayable containing the image to show full-screen in
                the chatroom (as opposed to in the gallery).
            chat_thumb : Displayable
                A displayable containing the image to show as a small thumbnail
                in the chatroom (as opposed to the gallery).
            """

            self.img = img
            self._locked_img = locked_img
            if thumbnail:
                self._thumbnail = thumbnail
            else:
                if self.filename:
                    thumb_name = self.filename.split('.')
                    thumbnail = thumb_name[0] + '-thumb.' + thumb_name[1]
                    if renpy.loadable(thumbnail):
                        self._thumbnail = thumbnail
                    else:
                        thumbnail = False
                if not thumbnail:
                    # If no thumbnail is provided, the program
                    # will automatically crop and scale the CG
                    self._thumbnail = Transform(img, crop_relative=True,
                                            crop=(0.0, 0.15, 1.0, 0.5625),
                                            size=(155,155))
            self.unlocked = False
            self._seen_in_album = False
            self.thumbnail_tuple = (self.filename, (0.0, 0.15, 1.0, 0.5625), True)
            self._chat_img = chat_img
            self.__chat_thumb = chat_thumb or chat_img

        @property
        def chat_thumb(self):
            """
            Return the image as it should appear in the chat as a thumbnail.
            """

            try:
                if self.__chat_thumb is not None:
                    return self.__chat_thumb
                elif self._chat_img is not None:
                    return Transform(self._chat_img, zoom=0.35)
            except Exception:
                pass
            return Transform(self.img, zoom=0.35)

        @property
        def chat_preview(self):
            return self.chat_thumb

        @property
        def chat_img(self):
            """
            Return the image as it should appear full-screen in the chat.
            """

            try:
                if self._chat_img is not None:
                    return self._chat_img
            except Exception:
                try:
                    self._chat_img = self.__chat_img
                    if self._chat_img is not None:
                        return self._chat_img
                except:
                    pass
            return self.img

        @property
        def filename(self):
            """Return the file name (including extension) for this image."""
            try:
                if '.' in self.img and renpy.loadable(self.img):
                    return self.img
                elif ('.' in self.img
                        and renpy.loadable(self.img.split('.')[0] + '.webp')):
                    self.img = self.img.split('.')[0] + '.webp'
                    return self.img
            except:
                pass
            reg_img = renpy.get_registered_image(self.img)
            try:
                if reg_img is None:
                    if not renpy.image_exists(self.img):
                        raise
                    else:
                        return False
                return reg_img.filename
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
                try:
                    temp = self._thumbnail
                except:
                    self._thumbnail = self.__thumbnail
                if (self._thumbnail not in store.persistent.unlocked_prof_pics
                        and self.thumbnail_tuple
                            not in store.persistent.unlocked_prof_pics):
                    add_img_to_set(store.persistent.unlocked_prof_pics,
                        self.get_thumb())

            renpy.retain_after_load()

        @property
        def name(self):
            """Retain compatibility with new gallery definitions."""
            return self.img

        @property
        def thumbnail_tuple(self):
            try:
                return self._thumbnail_tuple
            except:
                pass
            try:
                self._thumbnail_tuple = self.__thumbnail_tuple
                return self._thumbnail_tuple
            except:
                return None

        @thumbnail_tuple.setter
        def thumbnail_tuple(self, new_thumb):
            try:
                self._thumbnail_tuple = new_thumb
            except:
                pass

        @property
        def locked(self):
            return not self.unlocked

        @property
        def thumbnail(self):
            """Return the correct thumbnail for this image."""

            if self.unlocked:
                try:
                    return self._thumbnail
                except:
                    self._thumbnail = self.__thumbnail
                    return self._thumbnail
            else:
                try:
                    return self._locked_img
                except:
                    self._locked_img = self.__locked_img
                    return self._locked_img


        @thumbnail.setter
        def thumbnail(self, new_thumb):
            try:
                if not renpy.loadable(self.__thumbnail):
                    thumb_name = self.__thumbnail.split('.')[0] + '.webp'
                    if renpy.loadable(thumb_name):
                        self.__thumbnail = thumb_name
                        return
            except:
                # Assume it was a cropped image
                if self.filename:
                    img = self.filename.split('.')[0] + '.webp'
                else:
                    img = self.img
                if renpy.loadable(img):
                    self.__thumbnail = Transform(img, crop_relative=True,
                                            crop=(0.0, 0.15, 1.0, 0.5625),
                                            size=(155,155))
                    self.thumbnail_tuple = (img, (0.0, 0.15, 1.0, 0.5625), True)
                    return

            self.__thumbnail = new_thumb

        def get_thumb(self, exclude_transform=False):
            """Retrieve the CG's thumbnail, regardless of its unlock state."""

            # if (isinstance(self.__thumbnail, renpy.display.transform.Transform)
            #         and exclude_transform):
            #     return self.__thumbnail.child.filename

            # try:
            #     if not renpy.loadable(self.__thumbnail):
            #         thumb_name = self.__thumbnail.split('.')[0] + '.webp'
            #         if renpy.loadable(thumb_name):
            #             self.__thumbnail = thumb_name
            # except:
            #     try:
            #         # Assume it was a cropped image
            #         img = self.filename.split('.')[0] + '.webp'
            #         if renpy.loadable(img) and not exclude_transform:
            #             self.__thumbnail = Transform(img, crop_relative=True,
            #                                 crop=(0.0, 0.15, 1.0, 0.5625),
            #                                 size=(155,155))
            #         elif renpy.loadable(img):
            #             return img
            #     except:
            #         pass

            return self.__thumbnail

        def check_if_seen(self):
            """
            Check if this image was shown to the player and if so, unlock it.
            """

            if renpy.seen_image(self.img):
                self.unlock()

        @property
        def seen_in_album(self):
            try:
                return self._seen_in_album
            except:
                self._seen_in_album = self.__seen_in_album
                return self._seen_in_album

        @seen_in_album.setter
        def seen_in_album(self, new_bool):
            """Sets whether this image has been seen in the album yet."""

            if getattr(store, 'new_cg', False) and not self.seen_in_album:
                if new_bool:
                    store.new_cg -= 1
            self._seen_in_album = new_bool

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
                        try:
                            p_photo.thumbnail = photo.get_thumb()
                        except:
                            pass
                        break
        # Remove photos in p_album that aren't in update
        remove_list = [ ]
        for photo in p_album:
            if photo not in update:
                remove_list.append(photo)
        for photo in remove_list:
                p_album.remove(photo)
        return p_album

    def merge_albums_string(alb):
        """Update persistent albums to be consistent with regular albums."""

        if alb[-6:] != "_album":
            alb += "_album"
        alb_s = convert_to_file_name(alb)
        try:
            reg_album = getattr(store, alb_s)
        except:
            ScriptError("Couldn't find variable \"", alb_s,
                "\" to update albums.", header="CG Albums",
                subheader="Adding a CG Album")
            return
        # Set any non-existent persistent albums to an empty list
        try:
            per_album = getattr(store.persistent, alb_s)
        except:
            per_album = None
        if per_album is None:
            # No point merging with nothing
            return


        merge_albums(per_album, reg_album)

    def check_for_CGs(all_albums):
        """Make sure all seen images are unlocked in the player's album."""

        if isinstance(all_albums[0], list) or isinstance(all_albums[0], tuple):
            for p, a in all_albums:
                # Only need to go through persistent albums
                for cg in p:
                    cg.check_if_seen()
        else:
            for alb in all_albums:
                a = alb
                if not alb.endswith("_album"):
                    a += "_album"
                try:
                    per_album = getattr(store.persistent, convert_to_file_name(a))
                except:
                    ScriptError("Couldn't find variable \"", convert_to_file_name(a),
                        "\" to update albums.", header="CG Albums",
                        subheader="Adding a CG Album")
                    return
                if per_album is None:
                    # Look through the regular album
                    try:
                        per_album = getattr(store, convert_to_file_name(a))
                    except:
                        ScriptError("Couldn't find variable \"", convert_to_file_name(a),
                            "\" to update albums.", header="CG Albums",
                            subheader="Adding a CG Album")
                        return
                for cg in per_album:
                    cg.check_if_seen()
        return

    def add_to_album(album, photo_list):
        """Add the photos in photo_list to album."""

        global all_albums
        if not isinstance(photo_list, list):
            photo_list = [ photo_list ]
        for photo in photo_list:
            if photo not in album:
                album.append(photo)
        if isinstance(all_albums[0], list) or isinstance(all_albums[0], tuple):
            for p_album, reg_album in all_albums:
                merge_albums(p_album, reg_album)
        else: # Should be a string
            for alb in all_albums:
                merge_albums_string(alb)

    def has_unseen(album):
        """Return True if an album has a photo that hasn't been seen."""

        for photo in album:
            if not photo.seen_in_album and photo.unlocked:
                return True
        return False

    def get_name_from_file_id(file_id):
        """
        Return the character name associated with the given file_id, or a
        capitalized version of the file_id otherwise.

        Used to retrieve Album titles/labels.
        """

        result = get_char_from_file_id(file_id)
        if result is None:
            # This album name isn't associated with a character; probably
            # a title like "Common"
            file_lower = file_id.lower()
            if file_id == file_lower:
                return string.capwords(file_id)
            else:
                # Assume the capitalization is intentional
                return file_id
        else:
            return result.name

    def convert_to_file_name(file_id):
        """Convert file_id into a computer-readable format for file names."""

        new_id = file_id

        try:
            if ' ' in file_id:
                new_id = new_id.replace(' ', '_')
            if "'" in file_id:
                new_id = new_id.replace("'", "")

            return new_id.lower()
        except:
            print("WARNING: Received non-string file_id for file name:", file_id)
            return str(file_id)

    def hide_albums(album_list):
        """Hide the albums in album_list unless they have an unlocked photo."""

        global all_albums

        if not isinstance(album_list, list):
            album_list = [ album_list ]

        for album in album_list:
            skip_album = False
            if not album.endswith("_album"):
                full_alb = album + "_album"
            else:
                full_alb = album
                album = album[:-6]
            try:
                per_album = getattr(store.persistent, convert_to_file_name(full_alb))
            except:
                ScriptError("Couldn't find variable \"", convert_to_file_name(full_alb),
                    "\" to hide albums.", header="CG Albums",
                    subheader="Adding a CG Album")
                return
            if per_album is None:
                # Look through the regular album
                try:
                    per_album = getattr(store, convert_to_file_name(full_alb))
                except:
                    ScriptError("Couldn't find variable \"", convert_to_file_name(full_alb),
                        "\" to hide albums.", header="CG Albums",
                        subheader="Adding a CG Album")
                    return

            for photo in per_album:
                if photo.unlocked:
                    # This album can remain visible
                    skip_album = True
                    break
            if skip_album:
                continue

            # None of the photos in this album are unlocked;
            # it shouldn't be visible in all_albums
            if album in all_albums:
                all_albums.remove(album)

    def reset_albums():
        """
        Reset the persistent albums to lock all images and re-sync with
        the original variables.
        """

        global all_albums
        if isinstance(all_albums[0], tuple) or isinstance(all_albums[0], list):
            for p_album, reg_album in all_albums:
                p_album = [ ]
            merge_albums(p_album, reg_album)
        else: # Should be a string
            for alb in all_albums:
                # Fetch the album variable name
                if alb[-6:] != "_album":
                    alb += "_album"
                alb_s = convert_to_file_name(alb)
                try:
                    p_album = getattr(store.persistent, alb_s)
                    reg_album = getattr(store, alb_s)
                except:
                    ScriptError("Couldn't find variable \"", alb_s,
                        "\" to reset albums.", header="CG Albums",
                        subheader="Adding a CG Album")
                    return
                setattr(store.persistent, alb_s, [ ])
                merge_albums(p_album, reg_album)
        # Reset seen images
        store.persistent._seen_images.clear()
        renpy.reload_script()

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
                # Move the translucent image back to its
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
# This lets the player know if there are new CGs in the album.
default new_cg = 0

image cg_frame = 'CGs/photo_frame.webp'
image cg_frame_dark = 'CGs/photo_frame_dark.webp'

image translucent_img = Frame('translucent.webp', 0, 0)

## This screen shows all of the various characters/folders
## available in the photo gallery.
screen photo_album():

    # Ensure this replaces other menu screens
    tag menu

    if not main_menu:
        on 'replace' action [AutoSave()]
        on 'show' action [AutoSave()]

    python:
        if main_menu:
            return_action = Show('select_history', Dissolve(0.5))
        else:
            return_action = Show('chat_home', Dissolve(0.5))

        grid_row = -(-len(all_albums) // 3)
        full_grids = (len(all_albums) // 3) * 3

        null_height = (((1170 - (220*grid_row) - (40*(grid_row-1))) // 2) - 50)

    use menu_header('Photo Album', return_action):

        if isinstance(all_albums[0], list) or isinstance(all_albums[0], tuple):
            # Retained for backwards compatibility. Displays the albums.
            frame:
                xysize (config.screen_width, 1170)
                align (0.5, 0.5)
                has vbox
                align (0.5, 0.4)
                spacing 40
                # Each hbox can have a maximum of 3 characters in it, but you can
                # have less than three as well. You can also add another row by
                # adding another hbox.
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
            vpgrid:
                cols 5
                draggable True
                mousewheel True
                scrollbars "vertical"
                align (0.5, 0.5)
                xysize(config.screen_width, config.screen_height-164)
                if null_height > 0:
                    yoffset null_height
                # Negative xspacing allows the program to center
                # two items below a row of 3, if necessary.
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
## that will take you to the desired character's album.
screen char_album(caption, name=None, album=None, cover=None):

    python:
        if name is None:
            # Caption is actually the file_id
            file_id = caption
            caption = 'cg_label_' + convert_to_file_name(file_id)
            name = get_name_from_file_id(file_id)
            album = getattr(store,
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
                hover_background Fixed(caption, caption)
                if len(name) > 6:
                    text name + ' (' + str(get_album_len(album)) + ')':
                        style 'album_text_long'
                else:
                    text name + ' (' + str(get_album_len(album)) + ')':
                        style 'album_text_short'

        action Show('character_gallery', album=album,
                                caption=caption, name=name)



## This screen shows individual images unlocked for each character
screen character_gallery(album, caption, name):

    tag menu

    use menu_header('Photo Album', Show('photo_album', Dissolve(0.5))):

        vbox:
            align (0.5, 1.0)
            xysize (745, config.screen_height-164)
            spacing 5
            frame:
                xysize (241, 64)
                xalign 0.01
                add caption
                if len(name) > 6:
                    text name + ' (' + str(get_album_len(album)) + ')':
                        style 'album_text_long'
                else:
                    text name + ' (' + str(get_album_len(album)) + ')':
                        style 'album_text_short'

            vpgrid id 'gallery_vp':
                xysize (740, config.screen_height-234)
                yfill True
                cols 4
                draggable True
                mousewheel True
                if get_album_len(album):
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
                        action MMViewGallery(index, photo, album, caption, name)


init python:
    def MMViewGallery(index, photo, album, caption, name):
        if isinstance(album, GalleryAlbum):
            final_action = ViewGallery(album.zg, photo.name)
        else:
            final_action = Show('viewCG_fullsize_album', album=album,
                caption=caption, name=name)

        return If(photo.unlocked,
            [SetVariable("fullsizeCG", photo.img),
            SetField(photo, 'seen_in_album', True),
            SetVariable('close_visible', True),
            SetVariable('album_info_for_CG',
                [album, caption, name, index]),
            final_action],

            CConfirm("This image is not yet unlocked"))

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
## album screen to switch between them.
screen viewCG_fullsize_album(album, caption, name):
    zorder 5
    tag menu

    default fullscreen_on = False

    #use starry_night()
    add "black"

    # This draggroup defines two hotspots on the left and
    # right side of the screen to detect which direction
    # the CG has been dragged. 'the_CG' is actually just a
    # nearly-transparent overlay that the player drags onto
    # the left or right side of the screen
    draggroup:
        drag:
            drag_name "Left"
            child Transform('translucent_img', xysize=(70,config.screen_height))
            draggable False
            xalign 0.0
        drag:
            drag_name "Right"
            draggable False
            child Transform('translucent_img', xysize=(70, config.screen_height))
            xalign 1.0
        drag:
            drag_name "the_CG"
            drag_handle (0, 0, config.screen_width, config.screen_height)
            child 'translucent_img'
            dragged drag_box
            droppable False
            clicked toggle_close_drag
            drag_offscreen True
            xalign 0.5
            yalign 0.5

    # This slightly repetitive code makes the program animate in the
    # "swipes" as the player goes through the album.
    # Ren'Py will only animate if the animation is different,
    # which is why there are two "left"s and "right"s.
    if swipe_anim == "left":
        if prev_cg_left:
            add prev_cg_left at cg_swipe_left_hide:
                if fullscreen_on:
                    xsize None ysize config.screen_height fit "cover"
                else:
                    xsize 750 ysize None fit "contain"
            add fullsizeCG at cg_swipe_left:
                if fullscreen_on:
                    xsize None ysize config.screen_height fit "cover"
                else:
                    xsize 750 ysize None fit "contain"
        else:
            add fullsizeCG:
                align (0.5, 0.5)
                if fullscreen_on:
                    xsize None ysize config.screen_height fit "cover"
                else:
                    xsize 750 ysize None fit "contain"
    elif swipe_anim == "right":
        if prev_cg_right:
            add prev_cg_right at cg_swipe_right_hide:
                if fullscreen_on:
                    xsize None ysize config.screen_height fit "cover"
                else:
                    xsize 750 ysize None fit "contain"
            add fullsizeCG at cg_swipe_right:
                if fullscreen_on:
                    xsize None ysize config.screen_height fit "cover"
                else:
                    xsize 750 ysize None fit "contain"
        else:
            add fullsizeCG:
                align (0.5, 0.5)
                if fullscreen_on:
                    xsize None ysize config.screen_height fit "cover"
                else:
                    xsize 750 ysize None fit "contain"
    elif swipe_anim == "left2":
        if prev_cg_left:
            add prev_cg_left at cg_swipe_left_hide:
                if fullscreen_on:
                    xsize None ysize config.screen_height fit "cover"
                else:
                    xsize 750 ysize None fit "contain"
            add fullsizeCG at cg_swipe_left2:
                if fullscreen_on:
                    xsize None ysize config.screen_height fit "cover"
                else:
                    xsize 750 ysize None fit "contain"
        else:
            add fullsizeCG:
                align (0.5, 0.5)
                if fullscreen_on:
                    xsize None ysize config.screen_height fit "cover"
                else:
                    xsize 750 ysize None fit "contain"
    elif swipe_anim == "right2":
        if prev_cg_right:
            add prev_cg_right at cg_swipe_right_hide:
                if fullscreen_on:
                    xsize None ysize config.screen_height fit "cover"
                else:
                    xsize 750 ysize None fit "contain"
            add fullsizeCG at cg_swipe_right2:
                if fullscreen_on:
                    xsize None ysize config.screen_height fit "cover"
                else:
                    xsize 750 ysize None fit "contain"
        else:
            add fullsizeCG:
                align (0.5, 0.5)
                if fullscreen_on:
                    xsize None ysize config.screen_height fit "cover"
                else:
                    xsize 750 ysize None fit "contain"
    else:
        add fullsizeCG:
            align (0.5, 0.5)
            if fullscreen_on:
                xsize None ysize config.screen_height fit "cover"
            else:
                xsize 750 ysize None fit "contain"

    # Show the close button if it's visible.
    if close_visible:
        frame:
            background Solid("#00000066")
            xysize (config.screen_width, 99)

            textbutton "Close":
                style_prefix "CG_close"
                if persistent.dialogue_outlines:
                    text_outlines [ (2, "#000",
                                absolute(0), absolute(0)) ]
                    text_font gui.sans_serif_1b
                action [SetVariable('prev_cg_left', False),
                    SetVariable('prev_cg_right', False),
                    Show('character_gallery', album=album,
                        caption=caption, name=name)]

            if config.screen_height != 1334:
                button:
                    style_prefix 'cg_full'
                    padding (10, 40)
                    align (1.0, 0.5) xoffset -60
                    action ToggleScreenVariable('fullscreen_on')
                    has hbox
                    text "[[" xalign 1.0:
                        if persistent.dialogue_outlines:
                            outlines [ (2, "#000",
                                        absolute(0), absolute(0)) ]
                            font gui.sans_serif_1xb
                    fixed:
                        xsize 30
                        text "{}".format("-" if fullscreen_on else "+") xalign 0.5:
                            if persistent.dialogue_outlines:
                                outlines [ (2, "#000",
                                            absolute(0), absolute(0)) ]
                                font gui.sans_serif_1xb
                    text "]" xalign 0.0:
                        if persistent.dialogue_outlines:
                            outlines [ (2, "#000",
                                        absolute(0), absolute(0)) ]
                            font gui.sans_serif_1xb

style cg_full_text:
    size 45
    color "#fff"
    hover_color "#b3f3ee"
                font gui.sans_serif_1b


