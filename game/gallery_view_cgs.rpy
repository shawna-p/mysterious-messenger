
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
    # $ print("viewCG, pre_choosing", pre_choosing, "textmsg_CG", textmsg_CG, "CG_who", CG_who, "CG_who.real_time_text", CG_who.real_time_text, "text_person", text_person)
    call screen viewCG_fullsize()
    return
    
## This is the screen where you can view a full-sized CG when you
## click it. It has a "Close" button that appears/disappears 
## when you click the CG

screen viewCG_fullsize():
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
            # From the chatroom, before an answer button
            if pre_choosing and not textmsg_CG:
                action [Call("answer", from_cg=True)]
            # From a text message, not real time texting
            elif textmsg_CG and not CG_who.real_time_text:
                action [Hide("viewCG_fullsize"), 
                        Show("text_message_screen", sender=CG_who)]
            # From a real time text message, before an answer button
            elif textmsg_CG and pre_choosing:
                action [Hide("viewCG_fullsize"), 
                        Show("text_message_screen", sender=CG_who), 
                        Call("answer", from_cg=True)]
                
            # From a real time text message, not before an answer button
            elif textmsg_CG and text_person:
                action [Hide("viewCG_fullsize"), 
                        Show("text_message_screen", 
                            sender=CG_who), Call('play')]
            # Convo is over, just viewing CGs in a text message
            elif textmsg_CG:
                action [Hide("viewCG_fullsize"), 
                        Show("text_message_screen", sender=CG_who,
                            animate=False)]
            # From the chatroom, not before an answer button
            else:
                action [Call("play")]
        
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