init python:

          
    ##********************************************
    ## For ease of creating instant text messages
    ##******************************************** 
    
    
    
    ## This is taken almost directly from the same code in message.rpy
    ## It allows the text messages to show up one-by-one
    def addtext_instant(who, what, pauseVal, img=False, bounce=False, specBubble=None):
        global choosing, pre_choosing, pv, textbackup, oldPV, observing
        global persistent, cg_testing
        choosing = False
        pre_choosing = False
        
        if who != m:        
            textlog = who.private_text
        elif inst_text:   
            textlog = inst_text.private_text
                
        if pauseVal == None:
            pauseVal = pv
                        
        if len(textlog) > 1:
            finalchat = textlog[-2]
            if finalchat.who.file_id == 'delete':
                # This bubble doesn't display; delete it
                del textlog[-2]
                
        if who.file_id != 'delete':
            text_pauseFailsafe(textlog)
            textbackup = Chatentry(who, what, upTime(), img, bounce, specBubble)
            oldPV = pauseVal
            
        if pauseVal == 0:
            pass
        elif not renpy.get_screen('inst_text_message_screen'):
            pass
        elif who.file_id == 'delete':
            renpy.pause(pv)
        else:
            typeTime = what.count(' ') + 1 # equal to the number of words
            # Since average reading speed is 200 wpm or 3.3 wps
            typeTime = typeTime / 3
            if typeTime < 1.5:
                typeTime = 1.5
            typeTime = typeTime * pauseVal
            renpy.pause(typeTime)
            
        if img == True:
            if (what in emoji_lookup 
                    and renpy.get_screen('inst_text_message_screen')):
                renpy.play(emoji_lookup[what], channel="voice_sfx")
            elif "{image=" not in what and not observing:
                # We want to unlock the CG in the gallery
                # These will be equal to a path like
                # CGs/common_album/cg-1.png
                cg_filepath = cg_helper(what)
                album, cg_name = what.split('/')
                if album[-6:] != '_album':
                    album += '_album'
                cg_testing = ""
                cg_testing += album + " "
                cg_testing += cg_filepath
                # Now we need to search for that CG
                for photo in getattr(persistent, album):
                    if cg_filepath == photo.img:
                        cg_testing += "found it "
                        photo.unlock()
                        break
                    else:
                        cg_testing += "didn't find it "
        
        textlog.append(Chatentry(who, what, upTime(), img, bounce, specBubble))
        
    
            
    ## Function that checks if an entry was successfully added to the chat
    ## A temporary fix for the pause button bug
    ## This also technically means a character may be unable to post the exact
    ## same thing twice in a row depending on when the pause button is used
    def text_pauseFailsafe(textlog):
        global reply_instant, textbackup
        
        # If we're resetting the backup, we're done
        if textbackup == 'Reset':
            return
        
        if len(textlog) > 0:
            last_text = textlog[-1]
        else:
            return
        if last_text.who.file_id == 'delete':
            if len(textlog) > 1:
                last_text = textlog[-2]
            else:
                return
        elif last_text.who == filler:
            return
                
        if last_text.who.file_id == textbackup.who.file_id and last_text.what == textbackup.what:
            # the last entry was successfully added; we're done
            return
        else:
            # add the backup entry
            if reply_instant or not renpy.get_screen('inst_text_message_screen'):
                reply_instant = False
            else:
                typeTime = textbackup.what.count(' ') + 1
                typeTime = typeTime / 3
                if typeTime < 1.5:
                    typeTime = 1.5
                typeTime = typeTime * oldPV
                renpy.pause(typeTime)
            
            if textbackup.img == True:
                if textbackup.what in emoji_lookup and renpy.get_screen('inst_text_message_screen'):
                    renpy.play(emoji_lookup[textbackup.what], channel="voice_sfx")
               
            textlog.append(Chatentry(textbackup.who, textbackup.what, upTime(), textbackup.img, textbackup.bounce, textbackup.specBubble))
            
    

default textbackup = Chatentry(filler,"","")
default persistent.instant_texting = False
default inst_text = False
  
########################################################               
## This screen takes care of the popups that notify
## the user when there is a new text message (instant var.) 
########################################################            
screen text_msg_popup_instant(the_char):

    #modal True
    zorder 100
    
    python:
        if len(the_char.private_text) > 0:
            last_msg = the_char.private_text[-1]
        else:
            last_msg = False
            
        name_len = len(name)
        name_cut = 54 - name_len
        
    
    window:
        maximum(621,373)
        background 'text_popup_bkgr'
        xalign 0.5
        yalign 0.4
        imagebutton:
            align (1.0, 0.22)
            idle 'input_close'
            hover 'input_close_hover'
            action [Hide('text_msg_popup_instant')]
            
        hbox:
            yalign 0.05
            xalign 0.03
            spacing 15
            add 'new_text_envelope'
            text 'NEW' color '#73f1cf' yalign 1.0 font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Bold.ttf"
        
        vbox:
            xalign 0.3
            yalign 0.85
            spacing 20
            hbox:
                spacing 20                
                add Transform(the_char.prof_pic, size=(110,110))
                
                vbox:
                    spacing 10
                    text "From: " + the_char.name color '#fff'
                    
                    window:
                        maximum(420,130)
                        background 'text_popup_msg' 
                        text text_popup_preview(last_msg) size 30 xalign 0.5 yalign 0.5 text_align 0.5
            
            
            textbutton _('Go to'):
                text_style 'mode_select'
                xalign 0.5
                xsize 220
                ysize 70
                text_size 28
                background 'menu_select_btn' padding(20,20)
                hover_foreground Transform('menu_select_btn', alpha=0.5)
                if not (renpy.get_screen('in_call') or renpy.get_screen('incoming_call') or renpy.get_screen('outgoing call')):
                    if the_char.private_text_label:
                        action [Hide('text_msg_popup_instant'), SetField(the_char, "private_text_read", True), 
                                SetVariable("CG_who", the_char), 
                                Hide('save_load'),
                                Hide('menu'),
                                Hide('chat_footer'), 
                                Hide('phone_overlay'), 
                                Hide('settings_screen'),
                                Jump(the_char.private_text_label)]
                    else:
                        action [Hide('text_msg_popup_instant'), SetField(the_char, "private_text_read", True), 
                                SetVariable("CG_who", the_char), 
                                Hide('save_load'),
                                Hide('menu'),
                                Hide('chat_footer'), 
                                Hide('phone_overlay'), 
                                Hide('settings_screen'),
                                Show('inst_text_message_screen', the_sender=the_char)]

    timer 3.25:
        action Hide('text_msg_popup_instant', Dissolve(0.25))
  
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
                activate_sound "sfx/UI/answer_screen.mp3"
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
        
########################################################
## This is the screen that actually displays the
## message, though it mostly borrows from the chatroom
## display screen
########################################################
screen inst_text_message_screen(the_sender):

    tag menu
                
    python:
        yadj.value = yadjValue  

    use menu_header(the_sender.name, Show('text_message_hub', 
                Dissolve(0.5)), True):
            
        viewport yadjustment yadj: # viewport id "VP":
            draggable True
            mousewheel True
            ysize 1040
                            
            has vbox:
                spacing -20
                use text_dialogue_instant(the_sender.private_text)
                
    #use inactive_text_answer
                                
                            
                            
########################################################  
## Displays the dialogue for the text message screen
########################################################
screen text_dialogue_instant(texts):
 
    python:
        chatLength = len(texts) - 1
        begin = chatLength - 10
        if begin >= 0:
            pass
        else:
            begin = 0
        
        if chatLength > 0:
            finalchat = texts[-1]
            if finalchat.who == "answer":
                if begin > 0:
                    begin -= 1
                
    #for n, i index id(i) in enumerate(texts[begin:]):
    for i index id(i) in texts[begin:]:

        #if chatLength > 0 and (n != 0 or begin != 0):
        #    if i.thetime.day != texts[n + begin - 1].thetime.day:
        #        use text_date_separator(i.thetime)     
        #elif begin == 0 and n == 0:
        #    use text_date_separator(i.thetime)
                       
        use text_animation_instant(i)
        

screen text_animation_instant(i):
    python:       
        transformVar = incoming_message
        if i.img == True:
            if "{image=" in i.what:
                pass
            else:
                transformVar = null_anim
                
        ## This determines how long the line of text is. If it needs to wrap
        ## it, it will pad the bubble out to the appropriate length
        ## Otherwise each bubble would be exactly as wide as it needs to be and no more
        if not i.img:
            t = Text(i.what)
            z = t.size()
            my_width = int(z[0])
            my_height = int(z[1])
        
        text_time = i.thetime.twelve_hour + ':' + i.thetime.minute + ' ' + i.thetime.am_pm
        
        
    ## First, the profile picture, no animation
    if i.who.name == 'msg' or i.who.name == 'filler':
        window:
            style i.who.name + '_bubble'
            text i.what style i.who.name + '_bubble_text'
            
    elif i.who.file_id != 'delete':
        window:
            if i.who == m:
                style 'MC_profpic_text'
            else:
                style 'profpic_text'
                
            add Transform(i.who.prof_pic, size=(110,110))
        
        ## Now add the dialogue
             
        fixed:
            if i.who != m:
                style 'text_msg_npc_fixed'
            else:
                style 'text_msg_mc_fixed'
            
            hbox at transformVar:
                spacing 5 
                if i.who != m:
                    ypos -10
                    
                else:
                    ypos 5    
                    if i.img and not "{image=" in i.what:
                        text text_time color '#fff' yalign 1.0 size 23 yoffset 25
                    else:
                        text text_time color "#fff" yalign 1.0 size 23                    
                
                window:                 
                    ## Check if it's an image
                    if i.img == True:
                        if i.who != m:
                            style 'img_text_message'
                        else:
                            style 'mc_img_text_message'
                        # Check if it's an emoji
                        if "{image=" in i.what:
                            if i.who != m:
                                style 'reg_bubble_text'
                            else:
                                style 'reg_bubble_MC_text'
                            text i.what style "bubble_text"
                        else:   # it's a CG
                            $ fullsizeCG = cg_helper(i.what)
                            imagebutton at small_CG:
                                bottom_margin 50
                                focus_mask True
                                idle fullsizeCG
                                if not choosing:
                                    action [SetVariable("fullsizeCG", cg_helper(i.what)), Call("viewCG", textmsg=True), Return()]
            
                    
                    else:        
                        if i.who != m:
                            style 'reg_bubble_text'
                        else:
                            style 'reg_bubble_MC_text'
                        if my_width > gui.longer_than:
                            text i.what style "bubble_text_long" min_width gui.long_line_min_width color '#fff'
                        else:            
                            text i.what style "bubble_text" color '#fff'
                            
                if i.who != m:
                    if i.img == True and not "{image=" in i.what:
                        text text_time color '#fff' yalign 1.0 size 23 yoffset 40 xoffset 10
                    else:
                        text text_time color "#fff" yalign 1.0 size 23
      
    #use anti_text_animation(i)  
       
            
screen anti_text_animation(i):
    python:       
        transformVar = anti_incoming_message
        if i.img == True:
            if "{image=" in i.what:
                pass
            else:
                transformVar = anti_small_CG
                
        if not i.img:
            t = Text(i.what)
            z = t.size()
            my_width = int(z[0])
            my_height = int(z[1])

            
    if i.who.file_id != 'delete':        
        ## Now add the dialogue             
        fixed:
            if i.who != m:
                style 'text_msg_npc_fixed'
            else:
                style 'text_msg_mc_fixed'
            
            hbox:
                spacing 5 
                if i.who != m:
                    ypos -10                    
                else:
                    ypos 5                    
                
                window at transformVar:                 
                    ## Check if it's an image
                    if i.img == True:
                        if i.who != m:
                            style 'img_text_message'
                        else:
                            style 'mc_img_text_message'
                        # Check if it's an emoji
                        if "{image=" in i.what:
                            if i.who != m:
                                style 'reg_bubble_text'
                            else:
                                style 'reg_bubble_MC_text'
                            text i.what style "bubble_text"
                        else:   # it's a CG
                            $ fullsizeCG = cg_helper(i.what)
                            add fullsizeCG
            
                    
                    else:        
                        if i.who != m:
                            style 'reg_bubble_text'
                        else:
                            style 'reg_bubble_MC_text'
                        if my_width > gui.longer_than:
                            text i.what style "bubble_text_long" min_width gui.long_line_min_width color '#fff'
                        else:            
                            text i.what style "bubble_text" color '#fff'
                            
    
## A label that lets you leave instant text message
## conversations, but you can't get them back
label leave_inst_text():
    $ textlog = inst_text.private_text                        
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
    $ inst_text.finished_text()
    $ inst_text = False
    $ renpy.retain_after_load()    
    call screen text_message_hub
    
label text_begin(who):    
    $ inst_text = who
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
    
