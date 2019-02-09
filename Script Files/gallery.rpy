python early:

    class Album(store.object):
        def __init__(self, img, thumbnail=False, locked_img="CGs/album_unlock.png", unlocked=False):
            # images should be 750x1334
            self.img = img
            self.locked_img = locked_img
            # Thumbnails should be 155x155
            if thumbnail:
                self.thumbnail = thumbnail
            else:
                # If no thumbnail is provided, the program
                # will automatically crop and scale the CG
                self.thumbnail = Transform(Crop((0, 0, 750, 750), img), zoom=0.2067)
            self.unlocked = unlocked
            
        def unlock(self):
            global new_cg
            self.unlocked = True
            # Set a var so Album shows "NEW"
            new_cg = True
            renpy.retain_after_load
            
        def return_thumbnail(self):
            if self.unlocked:
                return self.thumbnail
            else:
                return self.locked_img
                
        def __eq__(self, other):
            if getattr(other, 'img', False):
                return self.img == other.img
            else:
                return False

        def __ne__(self, other):
            if getattr(other, 'img', False):
                return self.img != other.img
            else:
                return False
                
init python:

    ## This function updates p_album to have
    ## the same items as update
    def merge_albums(p_album, update):        
        for photo in update:
            if photo not in p_album:
                p_album.append(photo)
        return p_album

    
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
## these variables are used. This is where you'll actually
## declare all of the Album objects you need
default ja_album = []
default ju_album = []
default r_album = [ Album("CGs/r_album/cg-1.png") ]
default s_album = [ Album("CGs/s_album/cg-1.png") ]
default u_album = []
default v_album = []
default y_album = []
default z_album = []
default common_album = [ Album("CGs/common_album/cg-1.png"),
                        Album("CGs/common_album/cg-2.png"),
                        Album("CGs/common_album/cg-3.png")]


    
## This screen shows all of the various characters/folders
## available in the photo gallery
screen photo_album:

    # Ensure this replaces the main menu.
    tag menu

    # The background
    use starry_night()
    use menu_header('Photo Album', Show('chat_home', Dissolve(0.5)))
    
    window:
        align (0.5, 1.0)
        xysize (735, 1170)
        # A grid of buttons.
        vbox:
            align (0.5, 0.4)
            spacing 40
            # Each hbox can have a maximum of 3 characters in it, but you can
            # have less than three as well. You can also add another row by
            # adding another hbox
            hbox:
                use char_album('cg_label_ju', 'Jumin Han', persistent.ju_album, 'ju_album_cover')            
                use char_album('cg_label_z', 'ZEN', persistent.z_album, 'z_album_cover')
                use char_album('cg_label_s', '707', persistent.s_album, 's_album_cover')
            hbox:
                use char_album('cg_label_y', 'Yoosung★', persistent.y_album, 'y_album_cover')
                use char_album('cg_label_ja', 'Jaehee Kang', persistent.ja_album, 'ja_album_cover')
                use char_album('cg_label_v', 'V', persistent.v_album, 'v_album_cover')
            hbox:
                use char_album('cg_label_u', 'Unknown', persistent.u_album, 'u_album_cover')
                use char_album('cg_label_r', 'Ray', persistent.r_album, 'r_album_cover')
                use char_album('cg_label_common', 'Common', persistent.common_album, 'common_album_cover')
            
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
                window at album_tilt:
                    xysize (157, 137)
                    foreground 'cg_frame_dark'
                    background cover
                    align (1.0, 0.0)
                    xoffset 35
                    yoffset -42
                
                ## Window with the framed image
                window:
                    xysize (157, 137)
                    foreground 'cg_frame'
                    background cover
                    align (0.5, 0.5)
                    
            window:
                xysize (241, 64)
                background caption
                hover_foreground caption
                if len(name) > 6:
                    text name + ' (' + str(len(album)) + ')' style 'album_text_long'
                else:
                    text name + ' (' + str(len(album)) + ')' style 'album_text_short'
                    
        action Show('character_gallery', album=album, caption=caption, name=name)
            
        
        
## This screen shows individual images unlocked for each character
screen character_gallery(album, caption, name):

    tag menu
    use starry_night()
    use menu_header('Photo Album', Show('photo_album', Dissolve(0.5)))
    
    $ num_rows = max(len(album)/4, 1)
    
    vbox:
        align (0.5, 1.0)
        xysize (745, 1170)
        spacing 5
        window:
            xysize (241, 64)
            xalign 0.01
            add caption
            if len(name) > 6:
                text name + ' (' + str(len(album)) + ')' style 'album_text_long'
            else:
                text name + ' (' + str(len(album)) + ')' style 'album_text_short'
        
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
            

            for photo in album:
                imagebutton:
                    idle photo.return_thumbnail()
                    if photo.unlocked:                        
                        action [SetVariable("fullsizeCG", photo.img), Call("viewCG", album=True, album_info=[album, caption, name])]
                    else:
                        action Show("confirm", message="This image is not yet unlocked",
                    yes_action=Hide('confirm'))                    
            
            # This fills out the rest of the grid
            for i in range((4*num_rows) - len(album)):
                null
 
        
        
        