init python:

    def toggle_skipping():
        config.skipping = not config.skipping
        
        

    # Add a name & colour here if you'd like to add
    # another heart icon
    heartcolour = {'Sev': "#ff2626", 
                    'Zen': "#c9c9c9", 
                    'Ja': "#d0b741", 
                    'Ju': "#a59aef", 
                    'Yoo' : "#31ff26", 
                    'Rika' : "#fcef5a",
                    'Ray' : "#b81d7b",
                    'V' : "#50b2bc",
                    'Unk' : "#ffffff",
                    'Sae' : "#b81d7b",
                    } 

    # This is a helper function for the heart icon
    # it dynamically recolours a generic white heart
    # depending on the character
    # If you'd like to define your own character & heart icon,
    # just add another elif statement along with the colour you want
    # and when you type "call heart_icon("my custom character") it will
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

default choosing = False

image heart_icon = DynamicDisplayable(heart_icon_fn)
image heartbreak1 = DynamicDisplayable(heart_break_fn1)
image heartbreak2 = DynamicDisplayable(heart_break_fn2)
image heartbreak3 = DynamicDisplayable(heart_break_fn3)
image heartbreak4 = DynamicDisplayable(heart_break_fn4)
image heartbreak5 = "Heart Point/HeartBreak/stat_animation_10.png"

label heart_icon(character):
    $ heartChar = character
    show heart_icon onlayer heart at heart
    $ addchat("answer","",0.62)
    #hide heart_icon onlayer heart
    # it'd be easy to do something like if heartChar == "Sev": ++sevPoint
    # if you're counting heart points
    return
    
label heart_break(character):
    $ heartChar = character
    show heartbreak1 onlayer heart at heartbreak
    $ addchat("answer", "",0.12)
    hide heartbreak1 onlayer heart

    show heartbreak2 onlayer heart at heartbreak
    $ renpy.pause(0.12, hard=True)
    hide heartbreak2 onlayer heart

    show heartbreak3 onlayer heart at heartbreak
    $ renpy.pause(0.12, hard=True)
    hide heartbreak3 onlayer heart

    show heartbreak4 onlayer heart at heartbreak
    $ renpy.pause(0.12, hard=True)
    hide heartbreak4 onlayer heart

    show heartbreak5 onlayer heart at heartbreak
    $ renpy.pause(0.12, hard=True)
    hide heartbreak5 onlayer heart

    # again, could subtract heart points easily here
    return

# Call this label before you show a menu
# to show the answer button
label answer:
    if config.skipping:
        $ addchat("answer","",0)
    else:
        $ addchat("answer","",0.5)
    hide screen pause
    call screen answer_button
    return

    
image answerbutton: 
    block:
        "Phone UI/Answer-Dark.png" with Dissolve(0.5, alpha=True)
        0.5
        "Phone UI/Answer-Dark.png"
        0.5
        "Phone UI/Answer.png" with Dissolve(0.5, alpha=True)
        0.5
        "Phone UI/Answer.png"
        0.5
        repeat
        
image pausebutton:
    "Phone UI/pause_sign.png" with Dissolve(0.5, alpha=True)
    0.5
    "Phone UI/pause_sign.png"
    0.5
    "transparent.png" with Dissolve(0.5, alpha=True)
    0.5
    "transparent.png"
    0.5
    repeat

screen answer_button:
    if not choosing:
        image "pausebutton"
        image "Phone UI/pause_square.png"
        image "answerbutton" ypos 1220
    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 0
        ypos 1220
        focus_mask None
        idle "Phone UI/answer_transparent.png"#"answerbutton"
        activate_sound "sfx/UI/answer_screen.mp3"
        #hover "Phone UI/Answer-Dark.png"
        action [ToggleVariable("choosing", False, True), Show("pause"), Return()]

        
# This simplifies things when you're setting up a chatroom,
# so call it when you're about to begin
# If you pass it the name of the background you want (enclosed in
# single ' or double " quotes) it'll set that up too
# Note that it automatically clears the chatlog, so if you want
# to change the background but not clear the messages on-screen,
# you'll also have to pass it 'False' as its second argument
label chat_begin(background=None, clearchat=True):
    if clearchat:
        $ chatlog = []
    show screen phone_overlay
    show screen clock_screen
    show screen messenger_screen  
    show screen pause
    # Fills the beginning of the screen with 'empty space' so the messages begin
    # showing up at the bottom of the screen (otherwise they start at the top)
    if clearchat:
        $ addchat("filler","\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",0)
    
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

# This function isn't quite perfect, as it does flicker
# a little bit when pausing. It does, however, pause the
# dialogue
screen pause:
    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 0
        ypos 1220
        focus_mask True
        idle "Phone UI/Pause.png"
        if not choosing:
            action [Call("play"), Return()]
    if choosing:        
        image "Phone UI/choice_dark.png"
        
label play:
    $ addchat("pause","",0)
    #$ addchat("pause","",0)
    #call screen play_button
    show screen play_button
    pause
    hide screen play_button
    return
    
screen play_button:
    if not choosing:
        image "pausebutton"
        image "Phone UI/pause_square.png"
    else:
        image "Phone UI/choice_dark.png"
    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 0
        ypos 1220
        focus_mask True
        idle "Phone UI/Play.png"
        action Return()# [Hide("play"), Show("pause")]#, Return()]
        

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

image maxSpeed = im.FactorScale("Phone UI/max_speed_active.png",1.1)
image noMaxSpeed = im.FactorScale("Phone UI/max_speed_inactive.png",1.1)
        
## This screen just shows the header/footer above the chat
screen phone_overlay:  
    image "Phone UI/Phone-UI.png"   # You can set this to your own image
    if config.skipping:
        imagebutton:
            xanchor 0.0
            yanchor 0.0
            xpos 100
            ypos 73
            focus_mask True
            idle "Phone UI/max_speed_active.png"
            hover "maxSpeed"
            action [toggle_skipping, renpy.restart_interaction]
    else:
        imagebutton:
            xanchor 0.0
            yanchor 0.0
            xpos 100
            ypos 73
            focus_mask True
            idle "Phone UI/max_speed_inactive.png"
            hover "noMaxSpeed"
            action [toggle_skipping, renpy.restart_interaction]

   
## Currently not working; this will eventually be the screen where
## you can view a full-sized CG by clicking on it   
screen viewCG(cg_to_view):
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        #pos gui.phone_text_pos
        focus_mask True
        idle cg_to_view
        action [Hide(viewCG), Return]

# You can call this when you want to display the green
# scrolled hacking effect
# Don't forget to show your desired background after calling
# the hack screen or pass the background name to chat_begin
# If you don't use chat_begin, you'll need to make sure
# you show the phone_overlay/messenger_screen/pause screens

image hack scroll: 
    "Hack-Long.png"
    subpixel True
    yalign 0.0
    linear 1.0 yalign 1.0
    yalign 0.0
    linear 1.0 yalign 1.0
    
image redhack scroll:
    "Hack-Red-Long.png"
    subpixel True
    yalign 0.0
    linear 1.0 yalign 1.0
    yalign 0.0
    linear 1.0 yalign 1.0
    
label hack:
    $ addchat("answer","",0)
    hide screen phone_overlay
    hide screen messenger_screen 
    hide screen pause
    hide screen clock_screen
    scene black
    show hack scroll at flicker
    $ renpy.pause(0.72, hard=True)
    show hack scroll at flicker
    $ renpy.pause(0.72, hard=True)
    hide hack scroll
    return
    
label redhack:
    $ addchat("answer","",0)
    hide screen phone_overlay
    hide screen messenger_screen 
    hide screen pause
    hide screen clock_screen
    scene black
    show redhack scroll at flicker
    $ renpy.pause(0.72, hard=True)
    show redhack scroll at flicker
    $ renpy.pause(0.72, hard=True)
    hide redhack scroll
    return
    
# These are the special "banners" that crawl across the screen
# Just call them using "call banner_well" etc

#************************************
# Banners
#************************************
image banner annoy:
    "Banners/Annoy/annoy_0.png"
    0.12
    "Banners/Annoy/annoy_1.png"
    0.12
    "Banners/Annoy/annoy_2.png"
    0.12
    "Banners/Annoy/annoy_3.png"
    0.12
    "Banners/Annoy/annoy_4.png"
    0.12
    "Banners/Annoy/annoy_5.png"
    0.12
    
image banner heart:
    "Banners/Heart/heart_0.png"
    0.12
    "Banners/Heart/heart_1.png"
    0.12
    "Banners/Heart/heart_2.png"
    0.12
    "Banners/Heart/heart_3.png"
    0.12
    "Banners/Heart/heart_4.png"
    0.12
    "Banners/Heart/heart_5.png"
    0.12
        
image banner lightning:
    "Banners/Lightning/lightning_0.png"
    0.12
    "Banners/Lightning/lightning_1.png"
    0.12
    "Banners/Lightning/lightning_2.png"
    0.12
    "Banners/Lightning/lightning_3.png"
    0.12
    "Banners/Lightning/lightning_4.png"
    0.12
    "Banners/Lightning/lightning_5.png"
    0.12
    
image banner well:
    "Banners/Well/well_0.png"
    0.12
    "Banners/Well/well_1.png"
    0.12
    "Banners/Well/well_2.png"
    0.12
    "Banners/Well/well_3.png"
    0.12
    "Banners/Well/well_4.png"
    0.12
    "Banners/Well/well_5.png"
    0.12
    
label banner_lightning:
    show banner lightning at truecenter onlayer heart
    $ addchat("answer","",0.72)
    hide banner lightning onlayer heart
    return
    
label banner_heart:
    show banner heart at truecenter onlayer heart
    $ addchat("answer","",0.72)
    hide banner heart onlayer heart
    return
    
label banner_well:
    show banner well at truecenter onlayer heart
    $ addchat("answer","",0.72)
    hide banner well onlayer heart
    return
    
label banner_annoy:
    show banner annoy at truecenter onlayer heart
    $ addchat("answer","",0.72)
    hide banner annoy onlayer heart
    return
    
screen input(prompt, defAnswer = ""):

    window style "input_window":
        text prompt style "input_prompt"
        input id "input" default defAnswer style "input_answer"
        

        
        
    
