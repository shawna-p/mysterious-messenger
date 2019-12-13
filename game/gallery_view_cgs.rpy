
init python:
    ## This corrects the dialogue into a filepath for the program
    ## and unlocks the CG or adds it to the to-unlock list
    def cg_helper(what, who=False, instant_unlock=False):
        if what[:3] == "cg ":
            # don't need to add it
            filepath = what
        else:
            filepath = "cg " + what
        print("CG path", filepath)
        # Name of the album should be the letters before the first _
        # e.g. "cg common_1" -> common
        album_name = what.split('_')[0] + '_album'
        print("album_name", album_name)
        cg_list = getattr(store.persistent, album_name)

        for photo in cg_list:
            if Album(filepath) == photo:
                if instant_unlock or not who or who.right_msgr:
                    photo.unlock()
                elif who:
                    who.text_msg.cg_unlock_list.append([cg_list, photo])

        return filepath

    def smallCG(bigCG):
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
                        Show("text_message_screen", sender=CG_who)]
            # From the chatroom, not before an answer button
            else:
                action [Call("play")]
        
        text "Close" style "CG_close"

# Style for the Close button when viewing a fullscreen CG
style CG_close is text:
    xalign 0.06
    yalign 0.016
    font gui.sans_serif_1
    color "#ffffff"
    size 45