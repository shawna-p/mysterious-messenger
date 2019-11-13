init -6 python:

    ## This class stores the information needed for phone calls
    class Phone_Call(object):
        def __init__(self, caller, phone_label, call_status='incoming',
                avail_timeout=2, voicemail=False):
            self.caller = caller
            self.phone_label = phone_label
            self.call_time = False
            if (call_status == 'incoming' 
                    or call_status == 'outgoing' 
                    or call_status == 'missed' 
                    or call_status == 'voicemail'):
                self.call_status = call_status
            else:
                self.call_status = 'incoming'
            self.voicemail = voicemail
            self.playback = False
            self.avail_timeout = avail_timeout
            
        ## Phone calls will slowly expire if you don't call 
        ## the characters. The default expiry is after two chatrooms
        def decrease_time(self):
            global available_calls
            if self.avail_timeout == 'test':
                # You generally don't want to mess with this, but it
                # lets me make a call 'infinitely' available for testing
                pass
            else:
                self.avail_timeout -= 1
                if self.avail_timeout == 0:
                    available_calls.remove(self)
            
        ## Moves the call from 'available_calls' to 'call_history'
        def finished(self):
            global available_calls, call_history, observing            
            self.playback = True
            self.call_time = upTime()
            if self.voicemail:
                self.call_status = 'voicemail'
            else:
                if self in available_calls:
                    if self.avail_timeout != 'test':
                        available_calls.remove(self)
                
            if self.call_status == 'missed':
                self.call_status = 'outgoing'
            call_history.insert(0, self)
            observing = False

    ## If you hang up on a character who is calling you or
    ## miss their phone call, you can still call them back
    ## This creates a 'missed' phone call entry
    def call_hang_up_incoming(phonecall):    
        global call_history, available_calls        
        phonecall.call_status = 'missed'
        missed_call = copy(phonecall)
        missed_call.call_time = upTime()
        missed_call.playback = False
        if missed_call not in call_history:
            call_history.insert(0, missed_call)
        if phonecall not in available_calls:
            available_calls.append(phonecall)
        renpy.retain_after_load()
        
    ## If you hang up on a character, the conversation is
    ## no longer available
    def call_hang_up(phonecall):
        global available_calls
        if phonecall in available_calls:
            available_calls.remove(phonecall)
        
    ## Checks if a character has any available calls and
    ## returns the phonecall if so
    def call_available(who):
        global available_calls
        for phonecall in available_calls:
            if who == phonecall.caller:
                return phonecall
        return False
        
    _preferences.afm_enable = False
     
    if not persistent.set_afm:
        _preferences.afm_time = 15 # Or something. 
        persistent.set_afm = True
    
    def toggle_afm():
        _preferences.afm_enable = not _preferences.afm_enable
        renpy.restart_interaction()

    ## Makes any phonecalls associated with the current 
    ## chatroom available as appropriate
    def deliver_calls(lbl, expired=False, call_time=False):
        global available_calls, incoming_call, call_history
        global unseen_calls, test_em, all_characters
        missed_call = False
        phonecall = False
        # Adds available calls
        for c in all_characters:
            # Adds available outgoing calls to the list
            if renpy.has_label(lbl + '_phone_' + c.file_id):
                available_calls.append(Phone_Call(c, 
                    lbl + '_phone_' + c.file_id, 'outgoing'))

            # Updates the incoming call, or moves it if the call has expired
            if renpy.has_label(lbl + '_incoming_' + c.file_id):
                if expired:
                    phonecall = Phone_Call(c, lbl + '_incoming_' + c.file_id,
                                    'outgoing')
                    missed_call = Phone_Call(c, lbl + '_incoming_' + c.file_id,
                                    'missed')
                else:
                    incoming_call = Phone_Call(c, lbl + '_incoming_'
                                    + c.file_id, 'incoming')            
        
        # The player backed out of a chatroom; no missed call but we should
        # add it to the outgoing calls list
        if expired and not call_time and missed_call and phonecall:
            if phonecall not in available_calls:
                available_calls.append(phonecall)   

        # Otherwise, the chatroom expired so add the missed call as well
        # as an outgoing call
        elif expired and missed_call and phonecall:
            missed_call.playback = False
            missed_call.call_time = call_time                  
            if missed_call not in call_history:
                call_history.insert(0, missed_call)
            if phonecall not in available_calls:
                available_calls.append(phonecall)
            unseen_calls += 1
            
        renpy.retain_after_load()
        
default unseen_calls = 0
default in_phone_call = False
default call_countdown = 10

########################################################
## The phone menu screen, which displays a list of all
## the phone calls you've received
########################################################
screen phone_calls():

    tag menu

    on 'show' action [FileSave(mm_auto, confirm=False)]
    on 'replace' action [FileSave(mm_auto, confirm=False)]

    use menu_header("Call History", [Show('chat_home', Dissolve(0.5)), 
                                     FileSave(mm_auto, confirm=False)]):

            
                
        window:
            xalign 0.5
            yalign 0.13
            maximum(700,70)
            has hbox
            xalign 0.5
            spacing 40
            style_prefix "phone_contacts"
            # History/Contacts tabs
            textbutton _('{image=call_history_icon}  History'):
                hover_background None
                background "menu_tab_active"            
                    
            textbutton _('{image=contact_icon}  Contacts'):                
                action Show("phone_contacts", Dissolve(0.5))
    

        viewport:
            xsize 725
            ysize 1070
            draggable True
            mousewheel True

            xalign 0.5
            yalign 0.95
            
            vbox:
                spacing 10

                for i in call_history:

                    $ call_status = 'call_' + i.call_status
                    if i.playback:
                        $ replay_bkgr = 'call_replay_active'
                    else:
                        $ replay_bkgr = 'call_replay_inactive'
                    window:                                                       
                        background 'message_idle_bkgr'   
                        xysize (725, 150)

                        has hbox
                        spacing 10  
                        align (0.5, 0.5)
                        window:
                            xysize (135, 135)
                            align (0.5, 0.5)
                            add Transform(i.caller.prof_pic, size=(127,127)):
                                yalign 0.5 xalign 0.5
                        
                        window:
                            xmaximum 320
                            yalign 0.5
                            has vbox
                            align (0.0, 0.5)
                            text i.caller.name + ' {image=[call_status]}':
                                style "save_slot_text"
                            spacing 40                                    
                            text ("[i.call_time.twelve_hour]:[i.call_time.minute]"
                                    + " [i.call_time.am_pm], [i.call_time.day]/"
                                    + "[i.call_time.month_num]"):
                                style "save_slot_text"
                            
                        window:
                            xysize (230, 135) 
                            align (0.5, 0.5)                        
                            has hbox
                            align (0.5, 0.5)
                            spacing 30
                            imagebutton:                        
                                idle replay_bkgr
                                align(0.5, 0.5)
                                xysize(96,85)
                                hover Transform(replay_bkgr, zoom=1.1)
                                if i.playback:
                                    action [SetVariable('observing', True), 
                                            Jump(i.phone_label)]

                            imagebutton:                        
                                idle 'call_back' 
                                align(0.5, 0.5)
                                xysize(96,85)
                                hover Transform('call_back', zoom=1.1)
                                if call_available(i.caller):
                                    action [Preference("auto-forward", "enable"), 
                                    Show('outgoing_call', 
                                        phonecall=call_available(i.caller))]
                                else:
                                    action [Preference("auto-forward", "enable"), 
                                    Show('outgoing_call', 
                                        phonecall=i.caller.voicemail, 
                                        voicemail=True)]     

    
########################################################
## This screen shows you all your phone contacts so
## you can call them
########################################################

screen phone_contacts():

    tag menu
    use menu_header("Contacts", Show('chat_home', Dissolve(0.5))):
    
        window:
            xalign 0.5
            yalign 0.13
            maximum(700,70)
            has hbox
            xalign 0.5
            spacing 40
            style_prefix "phone_contacts"
            # Call History/Contacts tabs
            textbutton _('{image=call_history_icon}  History'):
                action Show("phone_calls", Dissolve(0.5))
                    
            textbutton _('{image=contact_icon}  Contacts'):
                hover_background None
                background "menu_tab_active"
                
        
        viewport:    
            xysize (725, 1070)
            draggable True
            mousewheel True

            xalign 0.5
            yalign 0.95
            
            has vbox
            xysize (725, 1070)       
            
            # Only characters in character_list show up as contacts
            # though any character in the all_characters list can 
            # phone the player
            if len(character_list) > 10:
                use phone_contacts_grid(3, -(-len(character_list) // 3))
            else:
                use phone_contacts_grid(3, 3)

style phone_contacts_button_text:
    color '#fff'
    font "fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
    text_align 0.5
    xalign 0.5
    yalign 0.5

style phone_contacts_button:
    xsize 290
    ysize 65
    background "menu_tab_inactive"
    hover_background "menu_tab_inactive_hover"
    activate_sound 'sfx/UI/phone_tab_switch.mp3'        

## This makes the phone contacts screen "flexible" so you can
## have as many or as few characters as you like
screen phone_contacts_grid(x_num, y_num):

    $ has_mc = 0

    grid x_num y_num:        
            
        align (0.5, 0.3)
        xspacing 60
        yspacing 100
        for person in character_list:
            if person == m:
                $ has_mc = 1
            else:
                vbox:
                    spacing 25
                    imagebutton:
                        background person.file_id + '_contact'
                        idle person.file_id + '_contact'
                        hover_foreground person.file_id + '_contact'
                        if call_available(person):
                            action [Preference("auto-forward", "enable"), 
                                    Show('outgoing_call', 
                                        phonecall=call_available(person))]
                        else:
                            action [Preference("auto-forward", "enable"), 
                                    Show('outgoing_call', 
                                        phonecall=person.voicemail, 
                                        voicemail=True)]
                    text person.name style 'contact_text'
        
        for i in range((x_num*y_num + has_mc) - len(character_list)):
            add 'empty_contact'
        
    
## This label ensures the rest of the phone conversation will
## not play out if you hang up
label hang_up():
    $ observing = False
    $ call_hang_up(phonecall=current_call)
    call screen phone_calls
    
########################################################
## This is the screen that displays the dialogue when
## you're in a phone call
########################################################

screen in_call():

    tag menu
    on 'show' action [renpy.music.stop(), 
                        SetVariable('in_phone_call', True), 
                        Preference('auto-forward after click', 'enable')]
    on 'hide' action [SetVariable('in_phone_call', False),
                        Preference('auto-forward after click', 'disable')] 
    on 'replace' action [renpy.music.stop(), 
                        SetVariable('in_phone_call', True), 
                        Preference('auto-forward after click', 'enable')]
    on 'replaced' action [SetVariable('in_phone_call', False), 
                        Preference('auto-forward after click', 'disable')]
                        
    use menu_header("In Call"):
        window:
            xysize (750, 1170)
            add 'call_headphones' yalign 0.12 xalign 0.5
            

            window:
                xysize(710, 200)
                yalign 0.95
                xalign 0.5
                has hbox
                align (0.5, 0.5)
                spacing 10
                window:
                    xysize(160,160)
                    align (0.5, 0.5)
                null width 100
                window:
                    xysize (65,75)
                    align (0.5, 0.5)
                    imagebutton:
                        align (0.5, 0.5)
                        if _preferences.afm_enable: #preferences.afm_time > 0:
                            idle 'call_pause'
                            action [PauseAudio('voice', value=True), 
                                    Function(toggle_afm)] #Preference("auto-forward", "toggle")
                            
                        else:
                            idle 'call_play'
                            action [PauseAudio('voice', value=False), 
                                    Function(toggle_afm)] #Preference("auto-forward", "toggle")
                null width 100
                window:
                    xysize(160,160)
                    align (0.5, 0.5)
                    if not starter_story:
                        imagebutton:
                            align (0.5, 0.5)
                            idle 'call_hang_up'
                            hover Transform('call_hang_up', zoom=1.1)
                            action [Hide('say'), Jump('hang_up')]
                        
                

########################################################
## This is the screen when you're receiving an incoming
## call
########################################################
screen incoming_call(phonecall, countdown_time=10):
    tag menu
    
    on 'hide' action Function(renpy.music.stop)
    use menu_header("In Call"):
        window:
            xysize (750, 1170)
            window:
                xfill True
                ysize 500
                yalign 0.16
                background 'call_overlay'
                
                has hbox
                align (0.5, 0.5)
                spacing -10
                window:
                    xysize(120,220)
                    align (1.0, 0.1)
                    has hbox
                    align (1.0, 0.5)
                    spacing -15
                    add 'call_signal_ll' align (0.5, 0.5)
                    null width 10
                    add 'call_signal_ml' align (0.5, 0.5)            
                    add 'call_signal_sl' align (0.5, 0.5)
                window:
                    align (0.5, 0.5)
                    xsize 350
                    has vbox
                    align (0.5, 0.5)
                    spacing 15
                    add Transform(phonecall.caller.prof_pic, size=(237,237)):
                        align (0.5, 0.5)
                    text phonecall.caller.name style 'caller_id'
                window:
                    xysize(120,220)
                    align (0.0, 0.1)
                    has hbox
                    align (0.0, 0.5)
                    spacing -15
                    add 'call_signal_sr' align (0.5, 0.5)
                    add 'call_signal_mr' align (0.5, 0.5)
                    null width 10
                    add 'call_signal_lr' align (0.5, 0.5)
            
            window:
                xfill True
                yalign 0.55
                has vbox
                align (0.5, 0.5)
                spacing 10
                text "Incoming Call" color '#fff' xalign 0.5 size 40
                if not starter_story:
                    text "[call_countdown]" xalign 0.5  color '#fff' size 80
                
                
            window:
                xysize(710, 200)
                yalign 0.95
                xalign 0.5
                has hbox
                align (0.5, 0.5)
                spacing 10
                window:
                    xysize(160,160)
                    align (0.5, 0.5)
                    imagebutton:
                        align (0.5, 0.5)
                        idle 'call_answer'
                        hover Transform('call_answer', zoom=1.1)
                        if starter_story:
                            action Return()
                        else:
                            action [Function(renpy.music.stop), 
                                    Preference("auto-forward", "enable"), 
                                    SetVariable('current_call', phonecall), 
                                    Jump(phonecall.phone_label)]
                null width 100
                add 'call_headphones' yalign 1.0
                null width 100
                window:
                    xysize(160,160)
                    align (0.5, 0.5)
                    if not starter_story:
                        imagebutton:
                            align (0.5, 0.5)
                            idle 'call_hang_up'
                            hover Transform('call_hang_up', zoom=1.1)
                            action [Function(renpy.music.stop), 
                                    Jump('incoming_hang_up')]
                
    on 'show' action SetScreenVariable('call_countdown', countdown_time)
    on 'replace' action SetScreenVariable('call_countdown', countdown_time)
    if not starter_story:
        timer 1.0 action If(call_countdown>1, 
                            SetScreenVariable("call_countdown", 
                            call_countdown-1), 
                            Jump('incoming_hang_up')) repeat True
    
## If you hang up an incoming call, you can
## still call that character back
label incoming_hang_up():
    $ call_hang_up_incoming(current_call)
    call screen chat_home
    
########################################################
## This is the screen when you're making a phone call
## to another character
########################################################

define phone_dial_sfx = "sfx/phone ring.mp3"

screen outgoing_call(phonecall, voicemail=False):
    tag menu
    
    
    on 'show' action renpy.music.play(["<silence 1.5>", 
                        phone_dial_sfx, "<silence 1.5>"])
    on 'replace' action renpy.music.play(["<silence 1.5>", 
                        phone_dial_sfx, "<silence 1.5>"])
    
    use menu_header("In Call"):
        window:
            xysize (750, 1170)
            window:
                xfill True
                ysize 500
                yalign 0.16
                background 'call_overlay'
                
                has hbox
                align (0.5, 0.5)
                spacing -10
                window:
                    xysize(120,220)            
                    align (0.5, 0.5)
                    xsize 350
                    has vbox
                    align (0.5, 0.5)
                    spacing 15
                    add Transform(phonecall.caller.prof_pic, size=(237,237)):
                        align (0.5, 0.5)
                    text phonecall.caller.name style 'caller_id'
                    
            window:
                xfill True
                yalign 0.55
                has hbox
                align (0.5, 0.5)
                spacing 30
                add 'call_connect_triangle' at delayed_blink2(0.0, 1.4) xalign 0.25
                add 'call_connect_triangle' at delayed_blink2(0.2, 1.4) xalign 0.35
                add 'call_connect_triangle' at delayed_blink2(0.4, 1.4) xalign 0.45
                add 'call_connect_triangle' at delayed_blink2(0.6, 1.4) xalign 0.55
                add 'call_connect_triangle' at delayed_blink2(0.8, 1.4) xalign 0.65
                add 'call_connect_triangle' at delayed_blink2(1.0, 1.4) xalign 0.75
                
                
            window:
                xysize(710, 200)
                yalign 0.95
                xalign 0.5
                has hbox
                align (0.5, 0.5)
                spacing 10
                window:
                    xysize(160,160)
                    align (0.5, 0.5)
                null width 100
                add 'call_headphones' yalign 1.0
                null width 100
                window:
                    xysize(160,160)
                    align (0.5, 0.5)
                    imagebutton:
                        align (0.5, 0.5)
                        idle 'call_hang_up'
                        hover Transform('call_hang_up', zoom=1.1)
                        action [renpy.music.stop, Show('phone_calls')]
       
    if voicemail:
        timer randint(8, 10) action If(phonecall, [renpy.music.stop, 
                                        SetVariable('current_call', phonecall), 
                                        Jump(phonecall.phone_label)], 
                                        Show('phone_calls'))
    else:
        timer randint(2, 8) action [renpy.music.stop, 
                                    SetVariable('current_call', phonecall), 
                                    Jump(phonecall.phone_label)]
    


## Allows the program to jump to the incoming call
label new_incoming_call(phonecall):
    play music persistent.phone_tone loop
    call screen incoming_call(phonecall=phonecall)
 
## This label sets up the appropriate variables/actions when you begin
## a phone call
label phone_begin():
    stop music
    # This stops it from recording the dialogue
    # from the phone call in the history log
    $ _history = False
    $ in_phone_call = True
    hide screen incoming_call
    hide screen outgoing_call
    
    # Hide all the popup screens
    hide screen text_msg_popup
    hide screen text_msg_popup_instant
    hide screen email_popup
    
    show screen in_call
    return
    
## This label sets the appropriate variables/actions when you finish
## a phone call
label phone_end():
    if not starter_story:
        if not observing:
            $ current_call.finished()
        $ in_phone_call = False
        $ current_call = False    
        $ observing = False
        $ _history = True
        $ renpy.retain_after_load()
        call screen phone_calls
    return
    
##*************************************************
## VOICEMAILS
##*************************************************
## For ease of keeping track of the different voicemails,
## they are defined here
label voicemail_1():
    call phone_begin 
    voice "voice files/voicemail_1.mp3"
    vmail_phone "The person you have called is unavailable right now. Please leave a message at the tone or try again."
    call phone_end 
