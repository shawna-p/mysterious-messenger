init python:

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
        
    def call_hang_up(phonecall):
        global available_calls
        if phonecall in available_calls:
            available_calls.remove(phonecall)
        
    def call_available(who):
        global available_calls
        for phonecall in available_calls:
            if who == phonecall.caller:
                return phonecall
        return False
        
        
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
    
    window:
        xalign 0.5
        yalign 0.13
        maximum(700,70)
        has hbox
        xalign 0.5
        spacing 40
        # Account / Sound / Others tab
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


label call_test:
    $ call_history = [Phone_Call(s, phone_label='call_test', title='POADCS', call_time=upTime()),
                        Phone_Call(y, phone_label='call_test', title='POADCS', call_time=upTime()),
                        Phone_Call(ju, phone_label='call_test', title='POADCS', call_time=upTime()),
                        Phone_Call(r, phone_label='call_test', title='POADCS', call_time=upTime())]
                        
    $ renpy.retain_after_load()
    call screen phone_calls   
        

    
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
        # Account / Sound / Others tab
        textbutton _('{image=call_history_icon}  History'):
            text_style "settings_tabs" 
            xsize 290
            ysize 65
            background "menu_tab_inactive"
            hover_background "menu_tab_inactive_hover"
            action Show("phone_calls", Dissolve(0.5))
                
        textbutton _('{image=contact_icon}  Contacts'):
            text_style "settings_tabs" 
            xsize 290
            ysize 65
            background "menu_tab_active"
            
    
    $ call_status = 'call_incoming'

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
    
    on 'show' action [SetVariable('in_phone_call', True), Preference('auto-forward after click', 'enable')]
    on 'hide' action [SetVariable('in_phone_call', False), Preference('auto-forward after click', 'disable'), 
                        Preference('auto-forward time', original_afm_time)]
    on 'replace' action [SetVariable('in_phone_call', True), Preference('auto-forward after click', 'enable')]
    on 'replaced' action [SetVariable('in_phone_call', False), Preference('auto-forward after click', 'disable'), 
                        Preference('auto-forward time', original_afm_time)]

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
                if preferences.afm_time > 0:
                    idle 'call_pause'
                    action Preference('auto-forward time', 0)
                else:
                    idle 'call_play'
                    action Preference('auto-forward time', original_afm_time)
        null width 100
        window:
            xysize(160,160)
            align (0.5, 0.5)
            imagebutton:
                align (0.5, 0.5)
                idle 'call_hang_up'
                hover Transform('Phone UI/Phone Calls/call_button_hang_up.png', zoom=1.1)
                action [Hide('say'), Preference('auto-forward time', original_afm_time), Jump('hang_up')]
                
                

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
screen outgoing_call(phonecall, voicemail=False):
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
                action Show('phone_calls')
       
    if voicemail:
        timer 10 action If(phonecall, [SetVariable('current_call', phonecall), Jump(phonecall.phone_label)], Show('chat_home'))
    else:
        timer randint(2, 10) action [SetVariable('current_call', phonecall), Jump(phonecall.phone_label)]
    
    
    