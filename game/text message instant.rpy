
default textbackup = Chatentry(filler,"","")
default persistent.instant_texting = False
 
  
########################################################  
## Includes the 'answer' button at the bottom
########################################################
screen text_answer():       
    tag chat_footer
    vbox at text_footer_disappear:
        yalign 0.98
        xalign 0.5
        window:
            ymaximum 40
            background 'text_msg_line'
        button:
            xsize 468
            ysize 95
            xalign 0.5
            background 'text_answer_active'
            hover_background 'text_answer_animation'  
            if not renpy.get_screen("choice"):
                action [Show('text_pause_button'), Return()]
                activate_sound "audio/sfx/UI/answer_screen.mp3"
            add 'text_answer_text' xalign 0.5 yalign 0.5
            
screen inactive_text_answer():
    tag chat_footer
    vbox at text_footer_disappear:
        yalign 0.98
        xalign 0.5
        window:
            ymaximum 40
            background 'text_msg_line'
        button:
            xsize 468
            ysize 95
            xalign 0.5
            background 'text_answer_inactive'
            add 'text_answer_text' xalign 0.5 yalign 0.5
            
#####################################
# Pause/Play footers
#####################################
   
# This is the screen that shows the pause button
# (but the chat is still playing)
screen text_pause_button():
    zorder 4
    tag chat_footer
    
    vbox at text_footer_disappear:
        yalign 0.98
        xalign 0.5
        window:
            ymaximum 40
            background 'text_msg_line'
        imagebutton:
            xalign 0.5
            focus_mask True
            idle "text_pause_button"
            if not choosing:
                action [Call("play"), Return()]
     
    
# This screen is visible when the chat is paused;
# shows the play button
screen text_play_button():
    zorder 4
    tag chat_footer
    
    vbox at text_footer_disappear:
        yalign 0.98
        xalign 0.5
        window:
            ymaximum 40
            background 'text_msg_line'
        imagebutton:
            xalign 0.5
            focus_mask True
            idle "text_play_button"
            action [Show('text_pause_button'), Return()]
        
    
## A label that lets you leave instant text message
## conversations, but you can't get them back
label leave_inst_text():
    $ textlog = text_person.text_msg.msg_list                        
    if len(textlog) > 1:
        $ finalchat = textlog[-1]
        if finalchat.who.file_id == 'delete':
            # This bubble doesn't display; delete it
            $ del textlog[-1]
    $ config.skipping = False   
    $ greeted = False         
    $ choosing = False
    $ textbackup = 'Reset'
    hide screen text_play_button
    hide screen text_answer
    hide screen text_pause_button
    hide screen inactive_text_answer
    $ text_person.finished_text()
    $ text_person = None
    $ renpy.retain_after_load()    
    call screen text_message_hub
    
label text_begin(who):    
    $ text_person = who
    $ who.private_text_read = True
    show screen inst_text_message_screen(who)
    show screen text_pause_button
    $ renpy.retain_after_load()
    return
        
        
label inst_text_begin(who):
    $ who.private_text_read = False
    $ inst_text = True
    $ textbackup = 'Reset'
    $ renpy.retain_after_load()
    return
    
label inst_text_end():
    $ inst_text = False
    $ textbackup = 'Reset'
    $ renpy.retain_after_load()
    return
    
