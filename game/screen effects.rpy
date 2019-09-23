init python:

    # A function to make the Max Speed button work
    def toggle_skipping():
        config.skipping = not config.skipping     

    # So you can increase/decrease the speed of the chat
    def slow_pv():
        global pv
        if pv <= 1.1:
            pv += 0.09  
        return
        
    def fast_pv():
        global pv
        if pv >= 0.53:
            pv -= 0.09
        return

    # This is a helper function for the heart icon that dynamically recolours a 
    # generic white heart depending on the character
    # See character definitions.rpy to define your own character & heart point
    def heart_icon_fn(st,at):
        if heartColor:
            colour = heartColor
        else:
            colour = white
        return im.MatrixColor("Heart Point/Unknown Heart Point.png", 
                                im.matrix.colorize("#000000", colour)), 0.1
        
    # Similarly, this recolours the heartbreak animation
    def heart_break_fn(st,at, picture):    
        if heartColor:
            colour = heartColor
        else:
            colour = white
        return im.MatrixColor(picture, im.matrix.colorize("#000000", colour)), 0.1
        
    # An experiment to recolour speech bubbles
    def glow_bubble_fn(st,at, glow_color='#000'):
        colour = glow_color
        return im.MatrixColor('Bubble/Special/sa_glow2.png', 
                            im.matrix.colorize(colour, '#fff')), 0.1
                            
    # An experiment to recolour speech bubbles
    def reg_bubble_fn(st,at, bubble_color='#000'):
        colour = bubble_color
        return im.MatrixColor('Bubble/white-Bubble.png', 
                            im.matrix.colorize('#000', colour)), 0.1
        
    

## Note: There is also a custom version of the chat footers
## (pause/play/save & exit/answer) that you can use by setting
## this variable to True. Otherwise, it will use the original assets
## If you change the variable here, you'll need to start the game over
## Otherwise it can also be changed from the Settings menu
default persistent.custom_footers = False

#************************************
# Heart Icons
#************************************ 
image heart_icon = DynamicDisplayable(heart_icon_fn)
image heartbreak1 = DynamicDisplayable(heart_break_fn, picture="Heart Point/HeartBreak/stat_animation_6.png")
image heartbreak2 = DynamicDisplayable(heart_break_fn, picture="Heart Point/HeartBreak/stat_animation_7.png")
image heartbreak3 = DynamicDisplayable(heart_break_fn, picture="Heart Point/HeartBreak/stat_animation_8.png")
image heartbreak4 = DynamicDisplayable(heart_break_fn, picture="Heart Point/HeartBreak/stat_animation_9.png")
image heartbreak5 = "Heart Point/HeartBreak/stat_animation_10.png"

image glow_bkgr_colorized = DynamicDisplayable(glow_bubble_fn)
#default glow_color = '#0ff'

default heartColor = '#000000'

# You call this to display the heart icon for a given character
label heart_icon(character, bad=False):
    python:
        heartColor = character.heart_color
        if character == r:
            character = sa
        if not observing and not no_heart:
            character.increase_heart(bad)
            chatroom_hp += 1
            persistent.HP += 1
    if not observing and not no_heart:
        show screen heart_icon_screen(character)
    return
    
# Displays the heart on-screen
screen heart_icon_screen(character):
    zorder 20   

    fixed at heart:
        yfit True
        xfit True
        add 'heart_icon'
        
    timer 0.62 action [Hide('heart_icon_screen')]
        
# Like the heart icon, call this to display the heart break   
label heart_break(character):
    python:
        heartColor = character.heart_color
        if character == r:
            character = sa
        if not observing and not no_heart:
            character.decrease_heart()
            chatroom_hp -= 1
            persistent.HP -= 1     
    if not observing and not no_heart:
        show screen heart_break_screen(character)
    return

# Displays the heartbreak on-screen
screen heart_break_screen(character):
    zorder 20
   
    fixed at heartbreak(0.0):
        yfit True
        xfit True
        add 'heartbreak1'
    fixed at heartbreak(0.12):
        yfit True
        xfit True
        add 'heartbreak2'
    fixed at heartbreak(0.24):
        yfit True
        xfit True
        add 'heartbreak3'
    fixed at heartbreak(0.36):
        yfit True
        xfit True
        add 'heartbreak4'
    fixed at heartbreak(0.48):
        yfit True
        xfit True
        add 'heartbreak5'
        
    timer 0.6 action [Hide('heart_break_screen')]

    
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
        
screen answer_button:
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
screen pause_button:
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
label play:
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
screen play_button:
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
screen phone_overlay:  
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
                                    yes_action=[Hide('confirm'), Jump('chat_back')], 
                                    no_action=Hide('confirm'))    
                                        
          
## This label takes care of what happens when the
## player hits the back button during a chatroom
label chat_back:
    # If you're replaying a chatroom or it's already
    # expired, you can back out without repercussions
    if observing or current_chatroom.expired:
        $ config.skipping = False
        $ greeted = False
        $ choosing = False
        hide screen phone_overlay
        hide screen messenger_screen
        hide screen save_and_exit
        hide screen play_button
        hide screen answer_button
        hide screen pause_button
        stop music
        show screen chat_home
        hide screen chat_home
        call screen chatroom_timeline(current_day, current_day_num)
    else:
        # If you back out of a chatroom, it expires
        $ current_chatroom.expired = True
        # And if you bought it back, it still expires
        $ current_chatroom.buyback = False
        $ current_chatroom.buyahead = False
        $ current_chatroom.participated = False
        # Reset participants
        $ current_chatroom.reset_participants()
        $ chatroom_hp = 0
        $ chatroom_hg = 0
        $ config.skipping = False   
        $ greeted = False         
        $ choosing = False
        $ most_recent_chat = current_chatroom
        hide screen phone_overlay
        hide screen messenger_screen
        hide screen save_and_exit
        hide screen play_button
        hide screen answer_button
        hide screen pause_button
        hide screen vn_overlay
        # Deliver text and calls        
        # if not current_chatroom.plot_branch:
        # Checks for a post-chatroom label; triggers even if there's a VN
        # Otherwise delivers texts etc
        if renpy.has_label('after_' + current_chatroom.chatroom_label): 
            $ renpy.call('after_' + current_chatroom.chatroom_label)
        $ deliver_all()
        $ deliver_calls(current_chatroom.chatroom_label, True)
        $ renpy.retain_after_load()
        stop music
        show screen chat_home
        hide screen chat_home
        call screen chatroom_timeline(current_day, current_day_num)


    

#####################################
# Chat Speed Modifiers
#####################################

## This speeds up/slows down the speed of the chat

screen speed_num:
    python:
        global pv  
        if pv <= 0.45:
            speednum = "9"
        elif pv <= 0.54:
            speednum = "8"
        elif pv <= 0.63:
            speednum = "7"
        elif pv <= 0.72:
            speednum = "6"
        elif pv <= 0.81:
            speednum = "5"
        elif pv <= 0.90:
            speednum = "4"
        elif pv <= 0.99:
            speednum = "3"
        elif pv <= 1.08:
            speednum = "2"
        elif pv <= 1.17:
            speednum = "1" 
        else:
            speednum = "!!"
            
    text "{size=30}SPEED{/size}\n [speednum]" style 'speednum_style'
    
    timer 0.4 action Hide('speed_num', Dissolve(0.4))


#####################################
# View CGs
#####################################
    
default close_visible = True
default textmsg_CG = False
default album_CG = False
default CG_who = text_messages[0]

label viewCG(textmsg=False, album=False, album_info=[]):
    $ close_visible = True
    $ textmsg_CG = textmsg
    $ album_CG = album
    call screen viewCG_fullsize
    if album:
        call screen character_gallery(album_info[0], album_info[1], album_info[2])
    return
    
## This is the screen where you can view a full-sized CG when you
## click it. It has a working "Close" button that appears/disappears 
## when you click the CG

screen viewCG_fullsize:
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
            if pre_choosing and not textmsg_CG and not album_CG:
                action [Call("answer", from_cg=True)]
            # From a text message, not instant texting
            elif textmsg_CG and not persistent.instant_texting:
                action [Hide("viewCG_fullsize"), Show("text_message_screen", the_msg=CG_who)]
            # From an instant text message, before an answer button
            elif textmsg_CG and pre_choosing:
                action [Hide("viewCG_fullsize"), Show("inst_text_message_screen", the_sender=CG_who), Call("answer", from_cg=True)] #[Hide("viewCG_fullsize"), Show("inst_text_message_screen", the_sender=CG_who)]
            # From an instant text message, not before an answer button
            elif textmsg_CG and inst_text:
                action [Hide("viewCG_fullsize"), Show("inst_text_message_screen", the_sender=CG_who), Call('play')]
            # Convo is over, just viewing CGs in a text message
            elif textmsg_CG:
                action [Hide("viewCG_fullsize"), Show("inst_text_message_screen", the_sender=CG_who)]
            # From the album
            elif album_CG:
                action [Hide('viewCG_fullsize'), Return()]
            # From the chatroom, not before an answer button
            else:
                action [Call("play")]
        
        text "Close" style "CG_close"

        
#####################################
# Save & Exit
#####################################
   
# This is the screen that shows Save & Exit at the bottom
screen save_and_exit(end_route=False):
    zorder 4
    tag chat_footer
    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 0
        ypos 1220
        focus_mask True
        if persistent.custom_footers:
            idle "custom_save_exit"
        else:
            idle "save_exit"
        if not end_route:
            action [Jump("press_save_and_exit")]
        else:
            action Return()
        
label press_save_and_exit(phone=True):
    if observing:
        $ config.skipping = False
        $ greeted = False
        $ choosing = False
        hide screen phone_overlay
        hide screen save_and_exit
        hide screen play_button
        hide screen answer_button
        hide screen pause_button
        hide screen messenger_screen
        stop music
        call screen chatroom_timeline(current_day, current_day_num)
        # call screen chat_select # call history_select_screen etc
    else:
        call screen signature_screen(phone)        
        $ persistent.HG += chatroom_hg
        $ chatroom_hp = 0
        $ chatroom_hg = 0
        $ config.skipping = False   
        $ greeted = False         
        $ choosing = False
        $ no_heart = False
        hide screen phone_overlay
        hide screen messenger_screen
        hide screen save_and_exit
        hide screen vn_overlay
        if not current_chatroom.played:
            $ current_chatroom.played = True
            if not starter_story and not current_chatroom.buyback:
                $ most_recent_chat = current_chatroom
        
        if not current_chatroom.expired and not current_chatroom.buyback:
            # Checks for a post-chatroom label; won't trigger if there's a VN section
            # Otherwise delivers phone calls/texts/etc
            if renpy.has_label('after_' + current_chatroom.chatroom_label) and not current_chatroom.vn_obj: 
                $ renpy.call('after_' + current_chatroom.chatroom_label)
            # If you just finished a VN section, mark it as played and deliver emails/phone calls
            if not phone and current_chatroom.vn_obj and not current_chatroom.vn_obj.played and current_chatroom.vn_obj.available:
                $ current_chatroom.vn_obj.played = True
                if renpy.has_label('after_' + current_chatroom.chatroom_label):
                    $ renpy.call('after_' + current_chatroom.chatroom_label)
        elif current_chatroom.plot_branch and current_chatroom.vn_obj and not current_chatroom.vn_obj.played and current_chatroom.vn_obj.available:
            $ current_chatroom.vn_obj.played = True
        elif not current_chatroom.plot_branch and not phone and current_chatroom.vn_obj and not current_chatroom.vn_obj.played and current_chatroom.vn_obj.available:
            $ current_chatroom.vn_obj.played = True
                
        if not current_chatroom.expired and not current_chatroom.buyback:
            $ deliver_calls(current_chatroom.chatroom_label)
            
        if current_chatroom.expired and not current_chatroom.buyback:
            $ current_chatroom.participated = False
        else:
            $ current_chatroom.participated = True
        $ deliver_emails()   
        $ next_chatroom()
        $ renpy.retain_after_load()
        if not chips_available:
            $ chips_available = hbc_bag.draw()
        
        stop music
        if starter_story:
            $ starter_story = False
            call screen chat_home
            return
        else:
            $ deliver_next()
            show screen chat_home
            hide screen chat_home
            call screen chatroom_timeline(current_day, current_day_num)
            return

    
# This shows the signature screen, which records your total heart points
# It shows hourglass points as well but currently there is no way to get
# more hourglasses
screen signature_screen(phone=True):
    zorder 5
    modal True
    if phone and not persistent.custom_footers:
        add "save_exit" ypos 1220
    elif phone and persistent.custom_footers:
        add "custom_save_exit" ypos 1220
    add "Phone UI/choice_dark.png"
    window:
        xalign 0.5
        yalign 0.5
        xsize 682
        ysize 471
        background 'signature'
        has vbox
        spacing 10
        null height 140 width 682
        text "This conversation will be archived in the RFA records." style "save_exit_text" xalign 0.5     
        fixed:
            xalign 0.5
            ysize 60
            xfit True
            add "heart_hg" 
            hbox:
                spacing 170
                yalign 0.5
                xoffset 65
                window:
                    xsize 70
                    ysize 40
                    text "[chatroom_hp]" style "points" xalign 1.0
                window:
                    xsize 80
                    ysize 40
                    text "[chatroom_hg]" style "points" xalign 1.0
        
        text "I hereby agree to treat this conversation as confidential." style "save_exit_text"
        
        textbutton _('sign'):
            xysize (211, 52)
            text_style 'sign'
            align (0.5, 0.842)
            focus_mask True
            background "Phone UI/sign-button.png" padding(20,20)
            activate_sound "sfx/UI/end_chatroom.mp3"
            hover_background "Phone UI/sign-button-clicked.png"
            action Return()


#####################################
# Hack scrolls, banners, enter/exit
#####################################
        
#************************************
# Hack Scrolls
#************************************
# You can call this when you want to display the green
# scrolled hacking effect

screen hack_screen(hack):
    zorder 10
    modal True
    add 'black'
    window at flicker:
        xysize (750,1334)
        background hack
        
    timer 3.0 action Hide('hack_screen')
        
    
label hack:
    $ chatlog.append(Chatentry(answer,'',upTime))
    show screen hack_screen('hack scroll')
    pause 3.0
    hide screen hack_screen
    return
    
label redhack:
    $ chatlog.append(Chatentry(answer,'',upTime))
    show screen hack_screen('redhack scroll')
    pause 3.0
    hide screen hack_screen
    return
    
#************************************
# Banners
#************************************

# These are the special "banners" that crawl across the screen
# Just call them using "call banner('well')" etc

label banner(banner):
    show screen banner_screen(banner)
    return
    
screen banner_screen(banner):
    zorder 10
    window at truecenter:
        add 'banner ' + banner
        
    timer 0.72 action Hide('banner_screen')
    
    
#************************************
# Chatroom Enter/Exit
#************************************
# This does some of the code for you when you want a character
# to enter/exit a chatroom. It adds characters to the chatroom's
# participant list if they enter during a chatroom.

label enter(chara):

    $ mystring = chara.name + " has entered the chatroom."
    
    $ addchat(special_msg, mystring, pv)
    if chara.name not in in_chat:
        $ in_chat.append(chara.name)
    
    if not observing:
        $ current_chatroom.add_participant(chara)
    
    $ renpy.restart_interaction
    return
    
label exit(chara):
    
    $ mystring = chara.name + " has left the chatroom."    
    $ addchat(special_msg, mystring, pv)
    if chara.name in in_chat:
        $ in_chat.remove(chara.name)
    $ renpy.restart_interaction
    return

    
#************************************
# Countdown Screen
#************************************

# Not actually in MysMe; this is just a screen to test out timed responses
# Could be a neat game mechanic
screen countdown(timer_jump, count_time=5): # I set a default reaction time of 5 seconds
    timer count_time repeat False action [ Hide('countdown'), Jump(timer_jump) ]
    bar value AnimatedValue(0, count_time, count_time, count_time) at alpha_dissolve

screen hidden_countdown(count_time=5): # I set a default reaction time of 5 seconds
    timer count_time repeat False action [ Hide('hidden_countdown'), Return() ]
    bar value AnimatedValue(0, count_time, count_time, count_time) at alpha_dissolve
        
        
screen answer_countdown(count_time=5): # I set a default reaction time of 5 seconds
    zorder 5
    timer count_time repeat False action [ Hide('answer_countdown'), Hide('continue_answer_button'), 
                                    Show('pause_button'), SetVariable("timed_choose", False) ]
    bar value AnimatedValue(0, count_time, count_time, count_time) at alpha_dissolve style 'answer_bar'
        
#************************************
# Continue Answer
#************************************

# Some experiments with getting the chat to continue while you come up with a response

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
        action [SetVariable("choosing", True), SetVariable('timed_choose', True), 
                Hide('continue_answer_button'), Show('pause_button'), Jump(themenu)] 
        
style answer_bar:
    bar_invert True
    thumb 'gui/slider/horizontal_idle_thumb.png'
    left_bar Frame('gui/slider/left_horizontal_bar.png',4,4)
    right_bar Frame('gui/slider/right_horizontal_bar.png',4,4)
    left_gutter 18
    right_gutter 18
    thumb_offset 18
    ypos 1210
    
    
    
    
    
    
    