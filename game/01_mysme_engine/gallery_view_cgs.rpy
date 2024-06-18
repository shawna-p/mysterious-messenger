
init python:
    def cg_helper(what, who=False, instant_unlock=False):
        """
        Correct the dialogue into a filepath for unlocking a CG or
        adding it to an unlock list to unlock later.

        Parameters:
        -----------
        what : string
            The dialogue that triggered this CG to be unlocked. Generally
            a simplified path to the CG.
        who : ChatCharacter
            The person who sent the message with the CG.
        instant_unlock : bool
            True if this CG should be unlocked immediately. Otherwise, it is
            added to a list and unlocked later (used, for example, in
            unlocking CGs sent through text message).
        """

        if what.startswith("cg "):
            # don't need to add cg to the start of this filepath
            filepath = what
        else:
            filepath = "cg " + what
        # Name of the album should be the letters before the first _
        # e.g. "cg common_1" -> common
        try:
            split_name = filepath.split('_')[0].split(' ')[1]
            album_name = split_name + '_album'
            cg_list = getattr(store, album_name)
        except:
            ScriptError("Couldn't get album name from CG image \"", what, '"',
            header="CG Albums",
            subheader="Showing a CG in a Chatroom or Text Message")
            return

        alb_obj = None
        for photo in cg_list:
            if photo.name == what or photo.name == filepath:
                alb_obj = photo
                if instant_unlock or not who or who.right_msgr:
                    photo.unlock()
                elif who:
                    who.text_msg.cg_unlock_list.append([cg_list, photo])
                break

            elif Album(filepath) == photo:
                alb_obj = photo
                if instant_unlock or not who or who.right_msgr:
                    photo.unlock()
                elif who:
                    who.text_msg.cg_unlock_list.append([cg_list, photo])
                break

        # Ensure the album for this photo is visible in the album screen.
        # Useful if you've hidden an album until an image in it is unlocked.

        if split_name not in store.all_albums:
            store.all_albums.append(split_name)

        if alb_obj:
            return alb_obj.chat_img

        return filepath

    def smallCG(bigCG):
        """Return a downsized version of bigCG."""

        if isinstance(bigCG, Album):
            return bigCG.chat_thumb
        elif isinstance(bigCG, GalleryImage):
            return bigCG.chat_thumb


        if bigCG.startswith("cg "):
            pass
        else:
            bigCG = "cg " + bigCG
        return Transform(bigCG, zoom=0.35)

#####################################
# View CGs
#####################################

default close_visible = True
default textmsg_CG = False

label viewCG(textmsg=False):
    $ close_visible = True
    $ textmsg_CG = textmsg
    call screen viewCG_fullsize()
    return

## This is the screen where you can view a full-sized CG when you
## click it. It has a "Close" button that appears/disappears
## when you click the CG.
screen viewCG_fullsize(fullsizeCG):
    zorder 5

    default fullscreen_on = False

    add "black"

    dismiss action ToggleVariable("close_visible", False, True)

    if isinstance(fullsizeCG, Album) or isinstance(fullsizeCG, GalleryImage):
        add fullsizeCG.chat_img:
            align (0.5, 0.5)
            if fullscreen_on:
                ysize config.screen_height fit "cover"
            else:
                xsize 750 ysize None fit "contain"
    else:
        add fullsizeCG:
            align (0.5, 0.5)
            if fullscreen_on:
                ysize config.screen_height fit "cover"
            else:
                xsize 750 ysize None fit "contain"

    if close_visible:
        frame:
            background Solid("#00000066")
            xysize (config.screen_width, 99)

            textbutton "Close":
                style_prefix "CG_close"
                action Return()
                if persistent.dialogue_outlines:
                    text_outlines [ (2, "#000") ]
                    text_font gui.sans_serif_1xb

            if config.screen_height != 1334:
                button:
                    style_prefix 'cg_full'
                    padding (10, 40)
                    align (1.0, 0.5) xoffset -60
                    action ToggleScreenVariable('fullscreen_on')
                    has hbox
                    text "[[" xalign 1.0
                    fixed:
                        xsize 30
                        text "{}".format("-" if fullscreen_on else "+") xalign 0.5
                    text "]" xalign 0.0

# Style for the Close button when viewing a fullscreen CG
style CG_close_button:
    yalign 0.5 xpos 20
    padding (10, 40)

style CG_close_button_text:
    is text
    font gui.sans_serif_1b
    color "#ffffff"
    size 45
    hover_color "#b3f3ee"