python early:

    class Album(store.object):
        def __init__(self, img, thumbnail=False, 
                    locked_img="CGs/album_unlock.png", unlocked=False):
            # images should be 750x1334
            self.img = img
            self.locked_img = locked_img
            # Thumbnails should be 155x155
            if thumbnail:
                self.thumbnail = thumbnail
            else:
                # If no thumbnail is provided, the program
                # will automatically crop and scale the CG
                self.thumbnail = Transform(Crop((0, 0, 750, 750), img), 
                                                        size=(155,155))
            self.unlocked = unlocked
            
        def unlock(self):
            global new_cg
            if not self.unlocked:
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
        
    ## This is a callback for the translucent image displayed
    ## on top of the CGs. It is draggable to the left and right
    ## of the screen, and if successful, displays the next or 
    ## previous available image to the player
    def drag_box(drags, drop):
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
                # We're going back one item
                # First check if it's the first item
                found_item = False
                if len(al) > 0 and ind > 0:
                    # Now we go backwards until we hit the beginning of
                    # the album or an unlocked CG
                    for i in range(ind-1, -1, -1):
                        if al[i].unlocked:
                            prev_cg_right = fullsizeCG
                            fullsizeCG = al[i].img
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
                    # Now we go forwards until we hit the end of the album
                    # or an unlocked CG
                    for i in range(ind+1, len(al)):
                        if al[i].unlocked:
                            prev_cg_left = fullsizeCG
                            fullsizeCG = al[i].img
                            album_info_for_CG[3] = i
                            found_item = True
                            if swipe_anim == "left":
                                swipe_anim = "left2"
                            else:
                                swipe_anim = "left"
                            break
                            
            renpy.restart_interaction()
                
    ## This is a simple callback to hide or show
    ## the "Close" sign when the image is clicked
    def toggle_close_drag():
        global close_visible
        close_visible = not close_visible
        renpy.restart_interaction()

    
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
screen photo_album():

    # Ensure this replaces the main menu.
    tag menu

    use menu_header('Photo Album', Show('chat_home', Dissolve(0.5))):
    
        # A grid of buttons.
        window:
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
            window:
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
                        idle photo.return_thumbnail()
                        if photo.unlocked:                        
                            action [SetVariable("fullsizeCG", photo.img), 
                                    Call("view_album_CG", 
                                        album_info=[album, caption, name, index])]
                        else:
                            action Show("confirm", 
                                    message="This image is not yet unlocked",
                                    yes_action=Hide('confirm'))                    
                
                # This fills out the rest of the grid
                for i in range((4*num_rows) - len(album)):
                    null
 
## Some additional variables specifically used
## for the next label and screen
default album_info_for_CG = []
default swipe_anim = False
default prev_cg_right = False
default prev_cg_left = False

## This label facilitates viewing CGs fullsize and returning
## to the Album screen when finished
label view_album_CG(album_info=[]):
    $ close_visible = True
    $ album_info_for_CG = album_info
    call screen viewCG_fullsize_album
    call screen character_gallery(album_info[0], album_info[1], album_info[2])

    
## This is the screen where you can view a full-sized CG when you
## click it. It has a working "Close" button that appears/disappears 
## when you click the CG. This particular variant lets the user
## "swipe" to view the various images without backing out to the 
## album screen proper
screen viewCG_fullsize_album():
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
            child Transform('translucent.png', size=(70,1334))
            draggable False
            xalign 0.0
        drag:
            drag_name "Right"
            draggable False
            child Transform('translucent.png', size=(70, 1334))
            xalign 1.0
        drag:
            drag_name "the_CG"
            drag_handle (0, 0, 750, 1334)
            child 'translucent.png'
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
        
    # Toggles whether or not the close button is visible
    if close_visible:
        imagebutton:
            xalign 0.5
            yalign 0.0
            focus_mask True
            idle "close_button"
            action [SetVariable('prev_cg_left', False), 
                    SetVariable('prev_cg_right', False),
                    Hide('viewCG_fullsize'), Return()]
        
        text "Close" style "CG_close"        
        
        