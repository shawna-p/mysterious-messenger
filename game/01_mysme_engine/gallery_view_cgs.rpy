
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

        if what[:3] == "cg ":
            # don't need to add cg to the start of this filepath
            filepath = what
        else:
            filepath = "cg " + what
        # Name of the album should be the letters before the first _
        # e.g. "cg common_1" -> common
        album_name = filepath.split('_')[0].split(' ')[1] + '_album'
        cg_list = getattr(store.persistent, album_name)

        for photo in cg_list:
            if Album(filepath) == photo:
                if instant_unlock or not who or who.right_msgr:
                    photo.unlock()
                elif who:
                    who.text_msg.cg_unlock_list.append([cg_list, photo])

        # Ensure the album for this photo is visible in the album screen.
        # Useful if you've hidden an album until an image in it is unlocked.
        if filepath.split('_')[0].split(' ')[1] not in store.all_albums:
            store.all_albums.append(filepath.split('_')[0].split(' ')[1])

        return filepath

    def smallCG(bigCG):
        """Return a downsized version of bigCG."""

        if bigCG[:3] == "cg ":
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
    imagebutton:
        xalign 0.5
        yalign 0.5
        focus_mask True
        idle fullsizeCG
        action ToggleVariable("close_visible", False, True)

    if close_visible:
        imagebutton:
            xalign 0.5
            yalign 0.0
            focus_mask True
            idle "close_button"
            action Return()

        text "Close" style "CG_close":
            if persistent.dialogue_outlines:
                outlines [ (2, "#000",
                            absolute(0), absolute(0)) ]
                font gui.sans_serif_1xb

# Style for the Close button when viewing a fullscreen CG
style CG_close is text:
    xalign 0.06
    yalign 0.016
    font gui.sans_serif_1
    color "#ffffff"
    size 45