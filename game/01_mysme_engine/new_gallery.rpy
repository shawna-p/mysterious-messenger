init python:

    class GalleryImage(renpy.store.object):
        """
        Class which holds information needed to show a single
        gallery image.

        Attributes:
        -----------
        name : string
            A unique, human-readable name of the image. Used to unlock it
            in the gallery.
        img : string
            The image name of the Displayable to use.
        thumbnail : string
            The file path to the image that will be used for the thumbnail.
        locked_img : string
            The file path to the image that will be used as the "locked"
            thumbnail icon.
        chat_img : Displayable
            A displayable containing the image to show full-screen in the
            chatroom (as opposed to in the gallery).
        chat_preview : Displayable
            A displayable containing the image to show as a small preview
            in the chatroom (as opposed to in the gallery).
        condition : string
            A string representing a condition which, if checked, should
            indicate whether this image should be shown in the gallery
            or not. Usually a persistent variable e.g. "persistent.dlc1"
        """

        def __init__(self, name, img=None, thumbnail=None,
                locked_img="CGs/album_unlock.webp", chat_img=None,
                chat_preview=None, condition=None):
            """Create a GalleryImage object."""

            self.name = name
            # The image name and image itself are the same
            if img is None:
                self.img = name
            else:
                self.img = img
            self.locked_img = locked_img

            if thumbnail:
                self.thumb = thumbnail
            else:
                if self.filename:
                    thumb_name = self.filename.split('.')
                    thumbnail = thumb_name[0] + '-thumb.' + thumb_name[1]
                    if renpy.loadable(thumbnail):
                        self.thumb = thumbnail
                    else:
                        thumbnail = False
                if not thumbnail:
                    # If no thumbnail is provided, the program
                    # will automatically crop and scale the CG
                    self.thumb = Transform(self.img, crop_relative=True,
                                            crop=(0.0, 0.15, 1.0, 0.5625),
                                            xysize=(155,155))
            self.p_chat_img = chat_img
            self.p_chat_preview = chat_preview

            self.condition = condition or "True"

        def evaluate_condition(self):
            """Evaluate whether this image should be shown in the gallery."""
            try:
                return eval(self.condition)
            except:
                return True

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

        @property
        def chat_preview(self):
            """
            Return the image as it should appear in the chat as a preview.
            """

            try:
                if self.p_chat_preview is not None:
                    return self.p_chat_preview
                elif self.p_chat_img is not None:
                    return Transform(self.p_chat_img, zoom=0.35)
            except Exception:
                pass
            return Transform(self.img, zoom=0.35)

        @property
        def chat_thumb(self):
            return self.chat_preview

        @property
        def chat_img(self):
            """
            Return the image as it should appear full-screen in the chat.
            """

            try:
                if self.p_chat_img is not None:
                    return self.p_chat_img
            except Exception:
                pass
            return self.img

        @property
        def locked(self):
            """Return whether this image has been unlocked or not."""

            return self.name not in store.persistent.gallery_unlocked

        @property
        def unlocked(self):
            return not self.locked

        @property
        def thumbnail(self):
            """Return the correct thumbnail for this image."""

            if self.locked:
                return self.locked_img
            else:
                return self.thumb

        def get_thumbnail(self):
            """Return this images thumbnail regardless of unlock state."""
            return self.thumb

        def unlock(self):
            """Unlock this image."""

            if not self.locked:
                return

            store.persistent.gallery_unlocked.add(self.name)

            # Set a var so Album shows "NEW"
            store.new_cg += 1
            # Add this to the list of unlocked profile pictures
            if (self.thumb not in store.persistent.unlocked_prof_pics
                    and (self.filename, (0.0, 0.15, 1.0, 0.5625), True)
                        not in store.persistent.unlocked_prof_pics):
                add_img_to_set(store.persistent.unlocked_prof_pics,
                    self.get_thumbnail())

            renpy.retain_after_load()

        def check_if_seen(self):
            """
            Check if this image was shown to the player and if so, unlock it.
            """
            if renpy.seen_image(self.img):
                self.unlock()

        @property
        def seen_in_album(self):
            return self.name in store.persistent.seen_in_gallery

        @seen_in_album.setter
        def seen_in_album(self, new_bool):
            """Sets whether this image has been seen in the album yet."""

            if getattr(store, 'new_cg', False) and not self.seen_in_album:
                if new_bool:
                    store.new_cg -= 1
            if new_bool:
                store.persistent.seen_in_gallery.add(self.name)
            elif self.name in store.persistent.seen_in_gallery:
                store.persistent.seen_in_gallery.remove(self.name)

        def __eq__(self, other):
            """Checks for equality between two Album objects."""

            if getattr(other, 'name', False):
                return self.name == other.name
            else:
                return False

        def __ne__(self, other):
            """Checks for equality between two Album objects."""

            if getattr(other, 'name', False):
                return self.name != other.name
            else:
                return False


    def check_for_old_albums(set_popup=True):
        """Check if we need to update old albums to the new style."""

        if store.persistent.seen_new_gallery_popup is not None:
            set_popup = False

        albums = [ ]
        if isinstance(all_albums[0], list) or isinstance(all_albums[0], tuple):
            for p, a in all_albums:
                if a:
                    for img in a:
                        if isinstance(img, GalleryImage):
                            return False
                        else:
                            if set_popup:
                                store.persistent.seen_new_gallery_popup = True
                            return True
        else:
            for alb in all_albums:
                a = alb
                if not alb.endswith("_album"):
                    a += "_album"
                try:
                    a_album = getattr(store, convert_to_file_name(a))
                except:
                    pass
                if a_album:
                    for img in a_album:
                        if isinstance(img, GalleryImage):
                            return False
                        else:
                            if set_popup:
                                store.persistent.seen_new_gallery_popup = True
                            return True
        return False

    def unlock_albums_v3_3():
        """
        Unlock images associated with old-style albums.
        """
        global persistent, all_albums

        check_for_CGs(all_albums)

        # Get the persistent album names
        albums = [ ]
        for p in all_albums:
            try:
                if not p.endswith("_album"):
                    x = getattr(persistent, "{}_album".format(p))
                else:
                    x = getattr(persistent, p)
                if x is not None:
                    albums.append(x)
                continue
            except:
                pass
            try:
                # It's a list or tuple of [persistent, regular]
                x = p[0]
                if x is not None:
                    albums.append(x)
            except:
                pass

        for p_album in albums:
            for p in p_album:
                if p.unlocked:
                    img = p.img
                    try:
                        if isinstance(img, Transform):
                            print("WARNING: Could not add gallery image to unlocked list.")
                        elif isinstance(img, str):
                            persistent.gallery_unlocked.add(p.img)
                        else:
                            print("Could not identify type of image", img)
                        print_file("Successfully updated", img)
                    except Exception as e:
                        print("WARNING: Error in processing album image:", e)
                else:
                    print_file("Image", p.img, "was not unlocked")

    def get_all_gallery_images(if_unlocked=False, obj=False):
        """
        Return a list of all the declared gallery images in the game, optionally
        only if they've been unlocked.

        Parameters:
        -----------
        if_unlocked : bool
            If True, only unlocked album images will be returned.
        obj : bool
            If True, the function will return the Album/GalleryImg objects.
            If False, the function will return the full-size image path.

        Returns:
        --------
            GalleryImg[] or string[]
        Returns a string of GalleryImg (or Album, for older versions) objects
        or a list of strings corresponding to album images, depending on the
        value of obj.
        """
        # Get the albums
        if isinstance(all_albums[0], list) or isinstance(all_albums[0], tuple):
            albums = [ getattr(persistent, convert_to_file_name("{}_album".format(a))) for a, b in store.all_albums ]
        else:
            albums = [ getattr(store, convert_to_file_name("{}_album".format(a))) for a in store.all_albums ]

        # Remove empty albums
        albums = [ a for a in albums if a ]

        # Put all the Album or GalleryImage items together
        all_imgs = [ ]
        for a in albums:
            all_imgs.extend(a)

        if if_unlocked:
            # Filter out locked images
            if obj:
                return [ a for a in all_imgs if not a.locked ]
            else:
                return [ a.img for a in all_imgs if not a.locked ]
        else:
            if obj:
                return all_imgs
            else:
                return [ a.img for a in all_imgs ]



screen gallery_popup():

    default gal_close = [
        SetField(persistent, 'seen_new_gallery_popup', True),
        Function(unlock_albums_v3_3),
        Hide('gallery_popup')
    ]

    button:
        background "#0008" xysize (config.screen_width, config.screen_height)
        action gal_close

    use confirm(
        ("Thanks for downloading Mysterious Messenger! The gallery system "
        + "has updated since the last version, so we'll take a moment now to "
        + "ensure your images remain unlocked. See the documentation for more "
        + "on how to update your gallery to the new definition style."
        ), gal_close
    )


default persistent.seen_new_gallery_popup = None
# Set of images unlocked in the gallery
default persistent.gallery_unlocked = set()
# Set of images which have been viewed in the gallery
default persistent.seen_in_gallery = set()

