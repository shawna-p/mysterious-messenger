init -6 python:

    # This class stores the information needed for phone calls
    class Phone_Call(store.object):
        def __init__(self, caller, phone_label, call_status='incoming',
                avail_timeout=2, voicemail=False):
            self.caller = caller
            self.phone_label = phone_label
            self.call_time = False
            if call_status == 'incoming' or call_status == 'outgoing' or call_status == 'missed' or call_status == 'voicemail':
                self.call_status = call_status
            else:
                self.call_status = 'incoming'
            self.voicemail = voicemail
            self.playback = False
            self.avail_timeout = avail_timeout
            
        # Phone calls will slowly expire if you don't call the characters. The default
        # expiry is after two chatrooms
        def decrease_time(self):
            global available_calls
            self.avail_timeout -= 1
            if self.avail_timeout == 0:
                available_calls.remove(self)
            
        # Moves the call from 'available_calls' to 'call_history'
        def finished(self):
            global available_calls, call_history, observing            
            self.playback = True
            self.call_time = upTime()
            if self.voicemail:
                self.call_status = 'voicemail'
            else:
                if self in available_calls:
                    available_calls.remove(self)
                
            if self.call_status == 'missed':
                self.call_status = 'outgoing'
            call_history.insert(0, self)
            observing = False

    # If you hang up on a character who is calling you or
    # miss their phone call, you can still call them back
    # This creates a 'missed' phone call entry
    def call_hang_up_incoming(phonecall):    
        global call_history, available_calls        
        phonecall.call_status = 'missed'
        missed_call = copy.copy(phonecall)
        missed_call.call_time = upTime()
        missed_call.playback = False
        if missed_call not in call_history:
            call_history.insert(0, missed_call)
        if phonecall not in available_calls:
            available_calls.append(phonecall)
        renpy.retain_after_load
        
    # If you hang up on a character, the conversation is
    # no longer available
    def call_hang_up(phonecall):
        global available_calls
        if phonecall in available_calls:
            available_calls.remove(phonecall)
        
    # Checks if a character has any available calls and
    # returns the phonecall if so
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

    ## Makes any phonecalls associated with the current chatroom available as appropriate
    def deliver_calls(lbl):
        global available_calls, incoming_call
        ## Adds available calls
        if renpy.has_label(lbl + '_phone_ja'):
            available_calls.append(Phone_Call(ja, lbl + '_phone_ja', 'outgoing'))
        if renpy.has_label(lbl + '_phone_ju'):
            available_calls.append(Phone_Call(ju, lbl + '_phone_ju', 'outgoing'))
        if renpy.has_label(lbl + '_phone_r'):
            available_calls.append(Phone_Call(r, lbl + '_phone_r', 'outgoing'))
        if renpy.has_label(lbl + '_phone_ri'):
            available_calls.append(Phone_Call(ri, lbl + '_phone_ri', 'outgoing'))
        if renpy.has_label(lbl + '_phone_s'):
            available_calls.append(Phone_Call(s, lbl + '_phone_s', 'outgoing'))
        if renpy.has_label(lbl + '_phone_sa'):
            available_calls.append(Phone_Call(sa, lbl + '_phone_sa', 'outgoing'))
        if renpy.has_label(lbl + '_phone_u'):
            available_calls.append(Phone_Call(u, lbl + '_phone_u', 'outgoing'))
        if renpy.has_label(lbl + '_phone_v'):
            available_calls.append(Phone_Call(v, lbl + '_phone_v', 'outgoing'))
        if renpy.has_label(lbl + '_phone_y'):
            available_calls.append(Phone_Call(y, lbl + '_phone_y', 'outgoing'))
        if renpy.has_label(lbl + '_phone_z'):
            available_calls.append(Phone_Call(z, lbl + '_phone_z', 'outgoing'))
            
        ## Updates the incoming_call
        if renpy.has_label(lbl + '_incoming_ja'):
            incoming_call = Phone_Call(ja, lbl + '_incoming_ja', 'incoming')
        if renpy.has_label(lbl + '_incoming_ju'):
            incoming_call = Phone_Call(ju, lbl + '_incoming_ju', 'incoming')
        if renpy.has_label(lbl + '_incoming_r'):
            incoming_call = Phone_Call(r, lbl + '_incoming_r', 'incoming')
        if renpy.has_label(lbl + '_incoming_ri'):
            incoming_call = Phone_Call(ri, lbl + '_incoming_ri', 'incoming')
        if renpy.has_label(lbl + '_incoming_s'):
            incoming_call = Phone_Call(s, lbl + '_incoming_s', 'incoming')
        if renpy.has_label(lbl + '_incoming_sa'):
            incoming_call = Phone_Call(sa, lbl + '_incoming_sa', 'incoming')
        if renpy.has_label(lbl + '_incoming_u'):
            incoming_call = Phone_Call(u, lbl + '_incoming_u', 'incoming')
        if renpy.has_label(lbl + '_incoming_v'):
            incoming_call = Phone_Call(v, lbl + '_incoming_v', 'incoming')
        if renpy.has_label(lbl + '_incoming_y'):
            incoming_call = Phone_Call(y, lbl + '_incoming_y', 'incoming')
        if renpy.has_label(lbl + '_incoming_z'):
            incoming_call = Phone_Call(z, lbl + '_incoming_z', 'incoming')
        
        
default unseen_calls = 0
default in_phone_call = False
default call_countdown = 10

########################################################
## The phone menu screen, which displays a list of all
## the phone calls you've received
########################################################
screen phone_calls:

    tag menu

    use starry_night()
    
    use menu_header("Call History", Show('chat_home', Dissolve(0.5)))
    
    on 'show' action SetVariable('unseen_calls', 0)
    
    on 'show':
       if renpy.music.get_playing(channel='music') != mystic_chat:
           action renpy.music.play(mystic_chat, loop=True)
    
    window:
        xalign 0.5
        yalign 0.13
        maximum(700,70)
        has hbox
        xalign 0.5
        spacing 40
        # History/Contacts tabs
        textbutton _('{image=call_history_icon}  History'):
            text_style "settings_tabs" 
            xsize 290
            ysize 65
            background "menu_tab_active"            
                
        textbutton _('{image=contact_icon}  Contacts'):
            text_style "settings_tabs" 
            xsize 290
            ysize 65
            background "menu_tab_inactive"
            hover_background "menu_tab_inactive_hover"
            action Show("phone_contacts", Dissolve(0.5))
            activate_sound 'sfx/UI/phone_tab_switch.mp3'
 

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
                    $ replay_bkgr = 'Phone UI/Phone Calls/call_button_replay_active.png'
                else:
                    $ replay_bkgr = 'Phone UI/Phone Calls/call_button_replay_inactive.png'
                window:                                                       
                    background 'message_idle_bkgr'   
                    xysize (750, 150)

                    has hbox
                    spacing 10  
                    align (0.5, 0.5)
                    window:
                        xysize (135, 135)
                        align (0.5, 0.5)
                        add i.caller.prof_pic yalign 0.5 xalign 0.5 at text_zoom
                    
                    window:
                        xmaximum 320
                        yalign 0.5
                        has vbox
                        align (0.0, 0.5)
                        text i.caller.name + ' {image=[call_status]}' style "save_slot_text"
                        spacing 40                                    
                        text "[i.call_time.twelve_hour]:[i.call_time.minute] [i.call_time.am_pm], [i.call_time.day]/[i.call_time.month_num]" style "save_slot_text"
                        
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
                                action [SetVariable('observing', True), Jump(i.phone_label)]

                        imagebutton:                        
                            idle 'call_back' 
                            align(0.5, 0.5)
                            xysize(96,85)
                            hover Transform('Phone UI/Phone Calls/call.png', zoom=1.1)
                            if call_available(i.caller):
                                action Show('outgoing_call', phonecall=call_available(i.caller))
                            else:
                                action Show('outgoing_call', phonecall=i.caller.voicemail, voicemail=True)       

    
########################################################
## This screen shows you all your phone contacts so
## you can call them
########################################################

screen phone_contacts:

    tag menu
    use starry_night()
    use menu_header("Contacts", Show('chat_home', Dissolve(0.5)))
    
    window:
        xalign 0.5
        yalign 0.13
        maximum(700,70)
        has hbox
        xalign 0.5
        spacing 40
        # Call History/Contacts tabs
        textbutton _('{image=call_history_icon}  History'):
            text_style "settings_tabs" 
            xsize 290
            ysize 65
            background "menu_tab_inactive"
            hover_background "menu_tab_inactive_hover"
            action Show("phone_calls", Dissolve(0.5))
            activate_sound 'sfx/UI/phone_tab_switch.mp3'
                
        textbutton _('{image=contact_icon}  Contacts'):
            text_style "settings_tabs" 
            xsize 290
            ysize 65
            background "menu_tab_active"
            
    
    viewport:    
        xysize (725, 1070)
        draggable True
        mousewheel True

        xalign 0.5
        yalign 0.95
        
        has vbox
        xysize (725, 1070)       
        
        grid 3 3:        
            
            align (0.5, 0.3)
            xspacing 60
            yspacing 100
            
            for person in character_list:
                if person == m:
                    pass
                else:
                    vbox:
                        spacing 25
                        imagebutton:
                            background person.file_id + '_contact'
                            idle person.file_id + '_contact'
                            hover_foreground person.file_id + '_contact'
                            if call_available(person):
                                action Show('outgoing_call', phonecall=call_available(person))
                            else:
                                action Show('outgoing_call', phonecall=person.voicemail, voicemail=True)
                        text person.name style 'contact_text'
                    
            add 'empty_contact'
        
    
# This label ensures the rest of the phone conversation will
# not play out if you hang up
label hang_up:
    $ observing = False
    $ call_hang_up(phonecall=current_call)
    call screen phone_calls
    
########################################################
## This is the screen that displays the dialogue when
## you're in a phone call
########################################################

screen in_call():

    tag menu
    use starry_night()
    use menu_header("In Call")
    
    add 'call_headphones' yalign 0.12 xalign 0.5
    
    on 'show' action [renpy.music.stop(), SetVariable('in_phone_call', True), Preference('auto-forward after click', 'enable')]
    on 'hide' action [SetVariable('in_phone_call', False), Preference('auto-forward after click', 'disable')] 
                        #Preference('auto-forward time', original_afm_time)]
    on 'replace' action [renpy.music.stop(), SetVariable('in_phone_call', True), Preference('auto-forward after click', 'enable')]
    on 'replaced' action [SetVariable('in_phone_call', False), Preference('auto-forward after click', 'disable')] 
                        #Preference('auto-forward time', original_afm_time)]
                        

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
                    action Function(toggle_afm) #Preference("auto-forward", "toggle")
                    
                else:
                    idle 'call_play'
                    action Function(toggle_afm) #Preference("auto-forward", "toggle")
        null width 100
        window:
            xysize(160,160)
            align (0.5, 0.5)
            imagebutton:
                align (0.5, 0.5)
                idle 'call_hang_up'
                hover Transform('Phone UI/Phone Calls/call_button_hang_up.png', zoom=1.1)
                action [Hide('say'), Jump('hang_up')]#Preference('auto-forward time', original_afm_time), Jump('hang_up')]
                
                

########################################################
## This is the screen when you're receiving an incoming
## call
########################################################
screen incoming_call(phonecall, countdown_time=10):
    tag menu
    use starry_night()
    use menu_header("In Call")
        
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
            add Transform(phonecall.caller.prof_pic, zoom=2.15) align (0.5, 0.5)
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
                hover Transform('Phone UI/Phone Calls/call_button_answer.png', zoom=1.1)
                action [SetVariable('current_call', phonecall), Jump(phonecall.phone_label)]
        null width 100
        add 'call_headphones' yalign 1.0
        null width 100
        window:
            xysize(160,160)
            align (0.5, 0.5)
            imagebutton:
                align (0.5, 0.5)
                idle 'call_hang_up'
                hover Transform('Phone UI/Phone Calls/call_button_hang_up.png', zoom=1.1)
                action Jump('incoming_hang_up')
                
    on 'show' action SetScreenVariable('call_countdown', countdown_time)
    on 'replace' action SetScreenVariable('call_countdown', countdown_time)
    timer 1.0 action If(call_countdown>1, SetScreenVariable("call_countdown", call_countdown-1), Jump('incoming_hang_up')) repeat True
    
label incoming_hang_up:
    $ call_hang_up_incoming(current_call)
    call screen chat_home
    
########################################################
## This is the screen when you're making a phone call
## to another character
########################################################

define phone_dial_sfx = "sfx/phone ring.mp3"

screen outgoing_call(phonecall, voicemail=False):
    tag menu
    use starry_night()
    use menu_header("In Call")
    
    
    on 'show' action renpy.music.play(["<silence 1.5>", phone_dial_sfx, "<silence 1.5>"])
    on 'replace' action renpy.music.play(["<silence 1.5>", phone_dial_sfx, "<silence 1.5>"])
    
    
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
            add Transform(phonecall.caller.prof_pic, zoom=2.15) align (0.5, 0.5)
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
                hover Transform('Phone UI/Phone Calls/call_button_hang_up.png', zoom=1.1)
                action [renpy.music.stop, Show('phone_calls')]
       
    if voicemail:
        timer randint(8, 10) action If(phonecall, [renpy.music.stop, 
                                        SetVariable('current_call', phonecall), 
                                        Jump(phonecall.phone_label)], Show('chat_home'))
    else:
        timer randint(2, 8) action [renpy.music.stop, 
                                    SetVariable('current_call', phonecall), 
                                    Jump(phonecall.phone_label)]
    
## Allows the program to jump to the incoming call
label new_incoming_call(phonecall):
    call screen incoming_call(phonecall=phonecall)
 
## This label sets up the appropriate variables/actions when you begin
## a phone call
label phone_begin:
    stop music
    hide screen incoming_call
    hide screen outgoing_call
    show screen in_call
    return
    
## This label sets the appropriate variables/actions when you finish
## a phone call
label phone_end:
    if not observing:
        $ current_call.finished()
    $ current_call = False    
    $ observing = False
    $ renpy.retain_after_load()
    call screen phone_calls
    return
    
##*************************************************
## VOICEMAILS
##*************************************************
## For ease of keeping track of the different voicemails,
## they are defined here
label voicemail_1:
    call phone_begin
    voice "Phone UI/Phone Calls/Voicemail/voicemail_1.ogg"
    vmail_phone "The person you have called is unavailable right now. Please leave a message at the tone or try again."
    call phone_end
