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
        """

        def __init__(self, name, img=None, thumbnail=None,
                locked_img="CGs/album_unlock.webp", chat_img=None,
                chat_preview=None):

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
                        self.__thumbnail = thumbnail
                    else:
                        thumbnail = False
                if not thumbnail:
                    # If no thumbnail is provided, the program
                    # will automatically crop and scale the CG
                    self.thumb = Transform(img, crop_relative=True,
                                            crop=(0.0, 0.15, 1.0, 0.5625),
                                            size=(155,155))
            self.p_chat_img = chat_img
            self.p_chat_preview = chat_preview

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

            return self.name in store.persistent.gallery_unlocked

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

            store.persistent.gallery_unlocked.add(self.name)

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

    def unlock_albums_v3_3():
        """
        Unlock images associated with old-style albums.
        """
        global persistent

        # TODO: I assume we're passing in the albums somehow
        for p_album in albums:
            if p_album.unlocked:
                img = p_album.img
                try:
                    if isinstance(img, Transform):
                        print("WARNING: Could not add gallery image to unlocked list.")
                    elif isinstance(img, str):
                        persistent.gallery_unlocked.add(p_album.img)
                    else:
                        print("Could not identify type of image", img)
                except Exception as e:
                    print("WARNING: Error in processing album image:", e)





default persistent.gallery_unlocked = set()
default persistent.seen_in_gallery = set()