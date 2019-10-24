#####################################
# Answer Button
##################################### 

# Call this label before you show a menu
# to show the answer button
label answer(from_cg=False): 
    if not inst_text:
        if from_cg:
            hide screen viewCG
        else:
            $ pauseFailsafe()
            #$ addchat(answer, '', 0.2)    
        $ pre_choosing = True
        call screen answer_button
        show screen pause_button
    else:
        if from_cg:
            hide screen viewCG
        else:
            $ text_pauseFailsafe(inst_text.private_text)
            #$ addtext_instant(answer, '', 0.2)
        $ pre_choosing = True
        call screen text_answer
        show screen text_pause_button
            
    return
        
screen answer_button():
    zorder 4
    tag chat_footer
    if persistent.custom_footers:
        add "custom_pausebutton" xalign 0.96 yalign 0.16
        add "custom_pause_square" yalign 0.59
    else:
        add "pausebutton" xalign 0.96 yalign 0.16
        add "Phone UI/pause_square.png" yalign 0.59
    if persistent.custom_footers:
        add "custom_answerbutton" ypos 1220
    else:
        add "answerbutton" ypos 1220
        
    imagebutton:
        ypos 1220
        focus_mask None
        idle "Phone UI/answer_transparent.png"
        activate_sound "sfx/UI/answer_screen.mp3"
        action [Show('pause_button'), Return()]   

    
#####################################
# Pause/Play footers
#####################################
   
# This is the screen that shows the pause button
# (but the chat is still playing)
screen pause_button():
    zorder 4
    tag chat_footer
    
    imagebutton:
        ypos 1220
        focus_mask True
        if persistent.custom_footers:
            idle "custom_pause"
        else:
            idle "Phone UI/Pause.png"
        if not choosing:
            action [Call("play"), Return()]
     
    if not choosing:
        # Fast button
        imagebutton:
            xalign 0.985
            yalign 0.997
            focus_mask None
            idle "fast-slow-button"
            action [Function(fast_pv), Show("speed_num")]
                
        # Slow button
        imagebutton:
            xalign 0.015
            yalign 0.997
            focus_mask None
            idle "fast-slow-button"
            action [Function(slow_pv), Show('speed_num')]
        
# This is automatically called when you pause the chat;
# it makes sure no messages are skipped        
label play():
    if not inst_text:
        #$ chatlog.append(Chatentry(chat_pause,'',upTime()))
        call screen play_button
        show screen pause_button
    else:
        #$ inst_text.private_text.append(Chatentry(chat_pause, '', upTime()))
        call screen text_play_button
        show screen text_pause_button
    return
    
# This screen is visible when the chat is paused;
# shows the play button
screen play_button():
    zorder 4
    tag chat_footer
    if not choosing:
        if persistent.custom_footers:
            add "custom_pausebutton" xalign 0.96 yalign 0.16
            add "custom_pause_square" yalign 0.59
        else:
            add "pausebutton" xalign 0.96 yalign 0.16
            add "Phone UI/pause_square.png" yalign 0.59
    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 0
        ypos 1220
        focus_mask True
        if persistent.custom_footers:
            idle "custom_play"
        else:
            idle "Phone UI/Play.png"
        action [Show('pause_button'), Return()]
        

#####################################
# Chat Header Overlay
#####################################

default no_heart = False

## This screen shows the header/footer above the chat
screen phone_overlay():  
    zorder 2
    add "Phone UI/Phone-UI.png"   # You can set this to your own image
    
    python:
        list_of_char = ''
        for index, chara in enumerate(in_chat):
            list_of_char += chara
            if index+1 < len(in_chat):
                list_of_char += ', '

    fixed:
        xysize(150,80)
        align (0.16, 0.055)
        imagebutton:
            align (0.5, 0.5)
            focus_mask True
            idle "Phone UI/max_speed_inactive.png"
            hover "noMaxSpeed"
            selected config.skipping
            selected_idle "Phone UI/max_speed_active.png"
            selected_hover "maxSpeed"
            if not choosing:
                action Function(toggle_skipping)
                
    if not observing:
        window:
            align (0.75, 0.055)
            xysize (400, 80)
            text list_of_char style 'in_chat_list_style'


                
    add myClock align(1.0, 0.0)
    
    if not starter_story:
        fixed:
            xysize (40,50)
            align (0.05, 0.065)
            imagebutton:
                align (0.5, 0.5)
                idle "Phone UI/back-arrow.png"
                hover Transform("Phone UI/back-arrow.png", zoom=1.2)
                if observing or current_chatroom.expired:
                    action Jump('chat_back')
                else:
                    action Show("confirm", message="Do you really want to exit this chatroom? Please note that you cannot participate once you leave. If you want to enter this chatroom again, you will need to buy it back.", 
                                    yes_action=[Hide('confirm'), 
                                    Jump('chat_back')], 
                                    no_action=Hide('confirm'))    


#************************************
# Countdown Screen
#************************************

# Not actually in MysMe; this is just a screen to test out timed responses
# Could be a neat game mechanic
 # I set a default reaction time of 5 seconds
screen countdown(timer_jump, count_time=5):
    timer count_time repeat False action [ Hide('countdown'), 
                                            Jump(timer_jump) ]
    bar value AnimatedValue(0, count_time, count_time, count_time):
        at alpha_dissolve

screen hidden_countdown(count_time=5): 
    timer count_time repeat False action [ Hide('hidden_countdown'), Return() ]
    bar value AnimatedValue(0, count_time, count_time, count_time):
        at alpha_dissolve
        
        
screen answer_countdown(count_time=5):
    zorder 5
    timer count_time repeat False action [ Hide('answer_countdown'), 
                                    Hide('continue_answer_button'), 
                                    Show('pause_button'), 
                                    SetVariable("timed_choose", False) ]
    bar value AnimatedValue(0, count_time, count_time, count_time):
        at alpha_dissolve 
        style 'answer_bar'
        

#************************************
# Continue Answer
#************************************

# Some experiments with getting the chat to continue
# while you come up with a response

default timed_choose = False
default reply_instant = False
default using_timed_menus = False

label continue_answer(themenu, count_time=5):

    # We want the timed answers to speed up/slow
    # down based on how fast the player has the
    # chat speed set to. Default is 0.8, increased/
    # decreased by 0.09 (aka increased/decreased by
    # 11.25% each time)
    python:
        modifier = 1.00
        if config.skipping:
            # Max Speed active
            modifier = 0.0
        elif pv <= 0.45:
            # speednum = "9"
            modifier = 0.1125*-4
        elif pv <= 0.54:
            # speednum = "8"
            modifier = 0.1125*-3
        elif pv <= 0.63:
            # speednum = "7"
            modifier = 0.1125*-2
        elif pv <= 0.72:
            # speednum = "6"
            modifier = 0.1125*-1
        elif pv <= 0.81:
            # speednum = "5"
            modifier = 0.00
        elif pv <= 0.90:
            # speednum = "4"
            modifier = 0.1125*1
        elif pv <= 0.99:
            # speednum = "3"
            modifier = 0.1125*2
        elif pv <= 1.08:
            # speednum = "2"
            modifier = 0.1125*3
        elif pv <= 1.17:
            # speednum = "1" 
            modifier = 0.1125*4
        else:
            # speednum = "!!"
            modifier = 0.00
        # So if the player has speed 9, which is pv=0.44 or 
        # 145% as fast as regular speed, the time should also
        # decrease by 45%
        count_time += count_time * modifier
        test_em = count_time

    # Here we make it so that timed menus don't show
    # up for players who are skipping through entire
    # conversations or who are replaying an existing
    # chatroom. Not allowing 'observing' players to 
    # choose an answer avoids the problem of players
    # who didn't initially choose an answer being unable
    # to continue
    if not config.skipping and not observing:
        $ using_timed_menus = True
        show screen answer_countdown(count_time)
        hide screen viewCG
        $ pre_choosing = True
        show screen continue_answer_button(themenu)
    else:
        $ timed_choose = False
    return

screen continue_answer_button(themenu):
    zorder 4
    tag chat_footer
    if persistent.custom_footers:
        add "custom_answerbutton" ypos 1220
    else:
        add "answerbutton" ypos 1220
    
    imagebutton:
        ypos 1220
        focus_mask None
        idle "Phone UI/answer_transparent.png"
        activate_sound "sfx/UI/answer_screen.mp3"
        action [SetVariable("choosing", True), 
                SetVariable('timed_choose', True), 
                Hide('continue_answer_button'), 
                Show('pause_button'), 
                Jump(themenu)] 
        
style answer_bar:
    bar_invert True
    thumb 'gui/slider/horizontal_idle_thumb.png'
    left_bar Frame('gui/slider/left_horizontal_bar.png',4,4)
    right_bar Frame('gui/slider/right_horizontal_bar.png',4,4)
    left_gutter 18
    right_gutter 18
    thumb_offset 18
    ypos 1210
    