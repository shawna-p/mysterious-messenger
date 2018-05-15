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

    # Add a name & colour here if you'd like to add
    # another heart icon
    heartcolour = {'s' : "#ff2626", 
                    'z' : "#c9c9c9", 
                    'ja' : "#d0b741", 
                    'ju' : "#a59aef", 
                    'y' : "#31ff26", 
                    'ri' : "#fcef5a",
                    'r' : "#b81d7b",
                    'v' : "#50b2bc",
                    'u' : "#ffffff",
                    'sa' : "#b81d7b",
                    } 
                    

    # This is a helper function for the heart icon
    # it dynamically recolours a generic white heart
    # depending on the character
    # If you'd like to define your own character & heart icon,
    # just add it to the heartcolour list
    # and when you type "call heart_icon(my_custom_character) it will
    # automatically recolour it
    def heart_icon_fn(st,at):
        if heartChar in heartcolour:
            colour = heartcolour[heartChar]
        else:
            colour = white
        return im.MatrixColor("Heart Point/Unknown Heart Point.png", im.matrix.colorize("#000000", colour)), 0.1
        
    # Similarly, this recolours the heartbreak animation
    # It has multiple frames, so there are a lot of 
    # similar functions defined below
    def heart_break_fn1(st,at):    
        if heartChar in heartcolour:
            colour = heartcolour[heartChar]
        else:
            colour = white
        return im.MatrixColor("Heart Point/HeartBreak/stat_animation_6.png", im.matrix.colorize("#000000", colour)), 0.1
        
    def heart_break_fn2(st,at):   
        if heartChar in heartcolour:
            colour = heartcolour[heartChar]
        else:
            colour = white
        return im.MatrixColor("Heart Point/HeartBreak/stat_animation_7.png", im.matrix.colorize("#000000", colour)), 0.1
        
    def heart_break_fn3(st,at):   
        if heartChar in heartcolour:
            colour = heartcolour[heartChar]
        else:
            colour = white
        return im.MatrixColor("Heart Point/HeartBreak/stat_animation_8.png", im.matrix.colorize("#000000", colour)), 0.1
        
    def heart_break_fn4(st,at):   
        if heartChar in heartcolour:
            colour = heartcolour[heartChar]
        else:
            colour = white
        return im.MatrixColor("Heart Point/HeartBreak/stat_animation_9.png", im.matrix.colorize("#000000", colour)), 0.1

# This is a variable that detects if you're choosing an option from a menu
# If so, it uses this variable to know it should disable most buttons
default choosing = False
# Variable that detects if the answer screen should be
# showing. Largely only useful if you view a CG when you should
# be answering a prompt
default pre_choosing = False
# Keeps track of the total number of hp (heart points) you've received per chatroom
default chatroom_hp = 0
# Keeps track of the total number of hg (hourglasses) you've earned per chatroom
default chatroom_hg = 0

#************************************
# Heart Icons
#************************************ 
image heart_icon = DynamicDisplayable(heart_icon_fn)
image heartbreak1 = DynamicDisplayable(heart_break_fn1)
image heartbreak2 = DynamicDisplayable(heart_break_fn2)
image heartbreak3 = DynamicDisplayable(heart_break_fn3)
image heartbreak4 = DynamicDisplayable(heart_break_fn4)
image heartbreak5 = "Heart Point/HeartBreak/stat_animation_10.png"

label heart_icon(character):
    show screen heart_icon_screen(character)
    return
    
screen heart_icon_screen(character):
    zorder 20
    python:
        global heartChar, chatroom_hp
        heartChar = character.file_id
        if character == r:
            character = sa
        character.add_heart()
        chatroom_hp += 1
        persistent.HP += 1
            
    if not observing:
        fixed at heart:
            yfit True
            xfit True
            add 'heart_icon'
        
    timer 0.62 action [Hide('heart_icon_screen')]
        
    
label heart_break(character):
    show screen heart_break_screen(character)
    return
    
    
screen heart_break_screen(character):
    zorder 20
    python:
        global heartChar, chatroom_hp
        heartChar = character.file_id
        if character == r:
            character = sa
        character.lose_heart()
        chatroom_hp -= 1
        persistent.HP -= 1
            
    if not observing:
        fixed at heartbreak1:
            yfit True
            xfit True
            add 'heartbreak1'
        fixed at heartbreak2:
            yfit True
            xfit True
            add 'heartbreak2'
        fixed at heartbreak3:
            yfit True
            xfit True
            add 'heartbreak3'
        fixed at heartbreak4:
            yfit True
            xfit True
            add 'heartbreak4'
        fixed at heartbreak5:
            yfit True
            xfit True
            add 'heartbreak5'
        
    timer 0.6 action [Hide('heart_break_screen')]

#####################################
# Answer Button
##################################### 

# Call this label before you show a menu
# to show the answer button
label answer:
    #pause 0.2
    #$ chatlog.append(Chatentry(answer,'',upTime))
    $ addchat(answer, '', 0.2)
    hide screen viewCG
    $ pre_choosing = True
    call screen answer_button
    show screen pause_button
    return
        
screen answer_button:
    zorder 4
    tag chat_footer
    add "pausebutton" xalign 0.96 yalign 0.16
    add "Phone UI/pause_square.png" yalign 0.59
    add "answerbutton" ypos 1220
        
    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 0
        ypos 1220
        focus_mask None
        idle "Phone UI/answer_transparent.png"
        activate_sound "sfx/UI/answer_screen.mp3"
        action [Show('pause_button'), Return]   

    
#####################################
# Pause/Play footers
#####################################
   
# This is the screen that shows the pause button
# (but the chat is still playing)
screen pause_button:
    zorder 4
    tag chat_footer
    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 0
        ypos 1220
        focus_mask True
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
            action [fast_pv, Show("speed_num")]
                
        # Slow button
        imagebutton:
            xalign 0.015
            yalign 0.997
            focus_mask None
            idle "fast-slow-button"
            action [slow_pv, Show('speed_num')]
          
label play:
    $ chatlog.append(Chatentry(chat_pause,'',upTime))
    call screen play_button
    show screen pause_button
    return
    
# This screen is visible when the chat isn't paused
screen play_button:
    zorder 4
    tag chat_footer
    if not choosing:
        add "pausebutton" xalign 0.96 yalign 0.16
        add "Phone UI/pause_square.png" yalign 0.59
    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 0
        ypos 1220
        focus_mask True
        idle "Phone UI/Play.png"
        action [Show('pause_button'), Return]
        

#####################################
# Chat Header Overlay
#####################################

## This screen shows the current time in the top righthand corner
## It's currently just for cosmetic purposes since I wanted to 
## display the current time as if it were a real phone
# The real MysMe screen doesn't technically have this
# but eventually it will likely be adapted to show the time like
# you see in VN sections

screen clock_screen:
    zorder 3
    add myClock:
        xalign 1.0
        yalign 0.0
                
## This screen just shows the header/footer above the chat
screen phone_overlay:  
    zorder 2
    add "Phone UI/Phone-UI.png"   # You can set this to your own image
    if config.skipping:
        imagebutton:
            xanchor 0.0
            yanchor 0.0
            xpos 100
            ypos 73
            focus_mask True
            idle "Phone UI/max_speed_active.png"
            hover "maxSpeed"
            if not choosing:
                action [toggle_skipping, renpy.restart_interaction]
                # The restart_interaction makes it so the Max Speed button
                # is visibly toggled after you press it
    else:
        imagebutton:
            xanchor 0.0
            yanchor 0.0
            xpos 100
            ypos 73
            focus_mask True
            idle "Phone UI/max_speed_inactive.png"
            hover "noMaxSpeed"
            if not choosing:
                action [toggle_skipping, renpy.restart_interaction]

    

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

label viewCG:
    $ close_visible = True
    hide screen clock_screen
    call screen viewCG_fullsize
    show screen clock_screen
    return
    
## This is the screen where you can view a full-sized CG when you
## click it in the chatroom. It has a working "Close" button
## that appears/disappears when you click the CG
## It can be fairly easily adapted to show CGs in a gallery as well

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
            if pre_choosing:
                action [Call("answer")]
            else:
                action [Call("play")]
        
        text "Close" style "CG_close"

        
#####################################
# Save & Exit
#####################################
   
# Call this label to show the save & exit sign
label save_exit:
    #answer "" (pauseVal=0)
    if observing:
        if config.skipping:
            $ config.skipping = False
        hide screen clock_screen
        $ greeted = False
        $ choosing = False
        hide screen phone_overlay
        hide screen messenger_screen
        return # call history_select_screen etc
    call screen save_and_exit
    return

# This is the screen that shows Save & Exit at the bottom
screen save_and_exit:
    zorder 4
    tag chat_footer
    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 0
        ypos 1220
        focus_mask True
        idle "save_exit"
        action [Jump("press_save_and_exit")]
        
label press_save_and_exit:
    call screen signature_screen
    $ persistent.HG += chatroom_hg
    $ chatroom_hp = 0
    $ chatroom_hg = 0
    $ config.skipping = False   
    $ greeted = False
    if current_chatroom.text_label and not current_chatroom.played:
        $ renpy.call(current_chatroom.text_label)
    $ choosing = False
    hide screen clock_screen
    hide screen phone_overlay
    hide screen messenger_screen
    hide screen save_and_exit
    $ current_chatroom.played = True
    $ renpy.retain_after_load()
    call screen chat_home

    
# This shows the signature screen, which records your total heart points
# It shows hourglass points as well but currently there is no way to get
# more hourglasses

screen signature_screen:
    zorder 5
    modal True
    add "save_exit" ypos 1220
    add "Phone UI/choice_dark.png"
    #add "signature" xalign 0.5 yalign 0.5
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
            xsize 211
            ysize 52
            text_style 'sign'
            xalign 0.5
            yalign 0.842
            focus_mask True
            background "Phone UI/sign-button.png" padding(20,20)
            activate_sound "sfx/UI/end_chatroom.mp3"
            hover_background "Phone UI/sign-button-clicked.png"
            action Return


        
    
    
#####################################
# Chat Setup
#####################################

# This simplifies things when you're setting up a chatroom,
# so call it when you're about to begin
# If you pass it the name of the background you want (enclosed in
# single ' or double " quotes) it'll set that up too
# Note that it automatically clears the chatlog, so if you want
# to change the background but not clear the messages on-screen,
# you'll also have to pass it 'False' as its second argument

label chat_begin(background=None, clearchat=True, resetHP=True):
    $ global pv
    if clearchat:
        $ chatlog = []
        $ pv = 0.8
    if resetHP:
        $ chatroom_hp = 0
    hide screen starry_night
    show screen phone_overlay
    show screen clock_screen
    show screen messenger_screen 
    show screen pause_button
    # Fills the beginning of the screen with 'empty space' so the messages begin
    # showing up at the bottom of the screen (otherwise they start at the top)
    if clearchat:
        $ chatlog.append(Chatentry(filler,"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",upTime))
        
    # Sets the correct background and nickname colour
    # You'll need to add other backgrounds here if you define
    # new ones
    if background == "morning":
        scene bg morning
        $ nickColour = black
    elif background == "noon":
        scene bg noon
        $ nickColour = black
    elif background == "evening":
        scene bg evening
        $ nickColour = black
    elif background == "night":
        scene bg night
        $ nickColour = white
    elif background == "earlyMorn":
        scene bg earlyMorn
        $ nickColour = white
    elif background == "hack":
        scene bg hack
        $ nickColour = white
    elif background == "redhack":
        scene bg redhack
        $ nickColour = white
    return
        
#************************************
# Hack Scrolls
#************************************
# You can call this when you want to display the green
# scrolled hacking effect
# Don't forget to show your desired background after calling
# the hack screen or pass the background name to chat_begin

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
    return
    
label redhack:
    $ chatlog.append(Chatentry(answer,'',upTime))
    show screen hack_screen('redhack scroll')
    pause 3.0
    return
    
# These are the special "banners" that crawl across the screen
# Just call them using "call banner_well" etc

#************************************
# Banners
#************************************

label banner(banner):
    show screen banner_screen(banner)
    return
    
screen banner_screen(banner):
    zorder 10
    window at truecenter:
        add 'banner ' + banner
        
    timer 0.72 action Hide('banner_screen')
        
    
#************************************
# Input Screen
#************************************
    
# This is just the screen you see when the program
# prompts you to enter a username
screen input(prompt, defAnswer = ""):

    window style "input_window":
        text prompt style "input_prompt"
        input id "input" default defAnswer style "input_answer"
        
#************************************
# Countdown Screen
#************************************

# Not actually in MysMe; this is just a screen to test out timed responses
# Could be a neat game mechanic
screen countdown(timer_jump, time=5): # I set a default reaction time of 5 seconds
    timer time repeat False action [ Hide('countdown'), Jump(timer_jump) ]
    bar value AnimatedValue(0, time, time, time) at alpha_dissolve

screen hidden_countdown(time=5): # I set a default reaction time of 5 seconds
    timer time repeat False action [ Hide('hidden_countdown'), Return ]
    bar value AnimatedValue(0, time, time, time) at alpha_dissolve
        
        
screen answer_countdown(time=5): # I set a default reaction time of 5 seconds
    timer time repeat False action [ Hide('answer_countdown'), Hide('continue_answer_button'), ToggleVariable("timed_choose", False, True) ]
    bar value AnimatedValue(0, time, time, time) at alpha_dissolve
        
#************************************
# Continue Answer
#************************************

# Some experiments with getting the chat to continue while you come up with a response

default timed_choose = False

label continue_answer(themenu, time=5):
    $ timed_choose = True
    show screen answer_countdown(time)
    hide screen viewCG
    $ pre_choosing = True
    show screen continue_answer_button(themenu)
    return

        
screen continue_answer_button(themenu):
    zorder 4
    image "answerbutton" ypos 1220
    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 0
        ypos 1220
        focus_mask None
        idle "Phone UI/answer_transparent.png"
        activate_sound "sfx/UI/answer_screen.mp3"
        action [ToggleVariable("choosing", False, True), Hide('continue_answer_button'), Jump(themenu)] 
    
    
    
    
    
    
    
    