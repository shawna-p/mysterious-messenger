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
                # If no thumbnail is provided, the program
                # will automatically crop and scale the CG
                self.__thumbnail = Transform(Crop((0, 200, 750, 750), img), 
                                                        size=(155,155))
            self.unlocked = False
            self.__seen_in_album = False
            
        def unlock(self):
            """Unlock this image in the album."""

            if not self.unlocked:
                self.unlocked = True
                # Set a var so Album shows "NEW"
                store.new_cg += 1            
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

    def merge_albums(p_album, update):   
        """Update p_album to have the same items as update."""

        print("Merging albums")
        for photo in update:
            if photo not in p_album:
                p_album.append(photo)
                print("Added a photo,",photo)
            else:
                # Ensure thumbnails are updated
                for p_photo in p_album:
                    if photo == p_photo:
                        p_photo.thumbnail = photo.get_thumb()
        return p_album

    def check_for_CGs(all_albums):
        """Make sure all seen images are unlocked in the player's album."""

        for p, a in all_albums:
            # Only need to go through persistent albums
            for cg in p:
                cg.check_if_seen()
        return

    def has_unseen(album):
        """Return True if an album has a photo that hasn't been seen."""

        for photo in album:
            if not photo.seen_in_album and photo.unlocked:
                return True
        return False
        
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


#************************************
# CGs
#************************************

# CGs are automatically resized in the chatroom, but you have to
# make sure the original dimensions are 750x1334
# The name of the cg must be "cg " + the name of the album minus
# "album" e.g. ju_album -> "ju", common_album -> "common"
# + a number or some other indicator of what the image is
image cg common_1 = "CGs/common_album/cg-1.png"
image cg common_2 = "CGs/common_album/cg-2.png"
image cg common_3 = "CGs/common_album/cg-3.png"

image cg s_1 = "CGs/s_album/cg-1.png"

image cg r_1 = "CGs/r_album/cg-1.png"

default fullsizeCG = "cg common_1"
# This lets the player know if there are new CGs in
# the album
default new_cg = 0

image cg_frame = 'CGs/photo_frame.png'
image cg_frame_dark = 'CGs/photo_frame_dark.png'
image cg_label_common = 'CGs/label_bg_common.png'  
image cg_label_ja = 'CGs/label_bg_ja.png'  
image cg_label_ju = 'CGs/label_bg_ju.png'  
image cg_label_other = 'CGs/label_bg_other.png'  
image cg_label_r = 'CGs/label_bg_r.png'  
image cg_label_s = 'CGs/label_bg_s.png'  
image cg_label_u = 'CGs/label_bg_u.png'  
image cg_label_v = 'CGs/label_bg_v.png'  
image cg_label_y = 'CGs/label_bg_y.png'  
image cg_label_z = 'CGs/label_bg_z.png' 

image ja_album_cover = 'CGs/ja_album_cover.png'
image ju_album_cover = 'CGs/ju_album_cover.png'
image r_album_cover = 'CGs/r_album_cover.png'
image s_album_cover = 'CGs/s_album_cover.png'
image u_album_cover = 'CGs/u_album_cover.png'
image v_album_cover = 'CGs/v_album_cover.png'
image y_album_cover = 'CGs/y_album_cover.png'
image z_album_cover = 'CGs/z_album_cover.png'
image common_album_cover = 'CGs/common_album_cover.png'

image translucent_img = 'translucent.png'
    
#************************************
# Album Declarations
#************************************
## These are the persistent photo album variables
## They let you keep unlocked photos available across
## different playthroughs
default persistent.ja_album = []
default persistent.ju_album = []
default persistent.r_album = []
default persistent.s_album = []
default persistent.u_album = []
default persistent.v_album = []
default persistent.y_album = []
default persistent.z_album = []
default persistent.common_album = []

## In order to allow for albums to be easily expanded,
## these variables are used. This is where you actually
## declare all of the Album objects you need
default ja_album = [ ]
default ju_album = [ ]
default r_album = [ Album("cg r_1") ]
default s_album = [ Album("cg s_1") ]
default u_album = []
default v_album = []
default y_album = []
default z_album = []
default common_album = [ Album("cg common_1"),
                        Album("cg common_2"),
                        Album("cg common_3")]

# This list allows the program to automatically merge the persistent
# and regular albums each time the game is started
# Each item in the list is a tuple that has the persistent album as its
# first item and the regular album variable as its second
default all_albums = [  
    [persistent.ju_album, ju_album],
    [persistent.z_album, z_album],
    [persistent.s_album, s_album],
    [persistent.y_album, y_album],
    [persistent.ja_album, ja_album],
    [persistent.v_album, v_album],
    [persistent.u_album, u_album],
    [persistent.r_album, r_album],
    [persistent.common_album, common_album]
]

    
## This screen shows all of the various characters/folders
## available in the photo gallery
screen photo_album():

    # Ensure this replaces the main menu.
    tag menu
    
    if not main_menu:
        on 'replace' action FileSave(mm_auto, confirm=False)
        on 'show' action FileSave(mm_auto, confirm=False)
    
    if main_menu:
        $ return_action = Show('select_history', Dissolve(0.5))
    else:
        $ return_action = Show('chat_home', Dissolve(0.5))

    use menu_header('Photo Album', return_action):
    
        # A grid of buttons.
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
            
## This displays a button with an image and a caption
## that will take you to the desired character's album
screen char_album(caption, name, album, cover):

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
                            
                            Show("confirm", 
                                    message="This image is not yet unlocked",
                                    yes_action=Hide('confirm')))                  
                
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
        
        