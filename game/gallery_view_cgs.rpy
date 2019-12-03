
init python:
    ## This corrects the dialogue into a filepath for the program
    def cg_helper(what):
        album, cg_name = what.split('/')
        if album[-6:] != '_album':
            album += '_album'
        # These will be equal to a path like
        # CGs/common_album/cg-1.png
        return 'CGs/' + album + '/' + cg_name

    def smallCG(bigCG):
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