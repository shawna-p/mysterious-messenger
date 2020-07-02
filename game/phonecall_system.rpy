init -6 python:

    class PhoneCall(renpy.store.object):
        """
        Class that stores information needed to keep track of phone calls.

        Attributes:
        -----------
        caller : ChatCharacter
            ChatCharacter object of the other person in the phone call.
        phone_label : string
            The label to jump to for the phone call.
        call_time : upTime or False
            The time the phone call was made at.
        call_status : string
            Status of the phone call. One of 'incoming', 'outgoing', 'missed',
            or 'voicemail'.
        voicemail : bool
            True if this call is a voicemail message rather than a conversation.
        playback : bool
            True if this conversation can be 'replayed' from the call history.
        avail_timeout : int
            How many chatrooms to wait until this call expires.
        """

        def __init__(self, caller, phone_label, call_status='incoming',
                avail_timeout=2, voicemail=False):
            """
            Creates a PhoneCall object to keep track of phone call information.

            Parameters:
            -----------
            caller : ChatCharacter
                ChatCharacter object of the other person in the phone call.
            phone_label : string
                The label to jump to for the phone call.
            call_status : string
                Status of the phone call. One of 'incoming', 'outgoing', 'missed',
                or 'voicemail'.
            avail_timeout : int
                How many chatrooms to wait until this call expires.
            voicemail : bool
                True if this call is a voicemail message rather than a conversation.
            """

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
            
        def decrease_time(self):
            """
            Counts towards expiring this phone call so it is no longer
            available. By default phone calls will time out after two
            chatrooms.
            """

            global available_calls
            if self.avail_timeout == 'test':
                # You generally shouldn't mess with this, but it
                # lets you make a call 'infinitely' available for testing
                pass
            else:
                self.avail_timeout -= 1
                if self.avail_timeout == 0:
                    available_calls.remove(self)
            
        def finished(self):
            """Move this phone call from available_calls to call_history"""

            global available_calls, call_history, observing            
            self.playback = True
            self.call_time = upTime()
            if self.voicemail:
                self.call_status = 'voicemail'
            else:
                # You shouldn't be able to call a character back and get the
                # same conversation, so remove the call from available_calls
                if self in available_calls and self.avail_timeout != 'test':
                        available_calls.remove(self)
                
            # If you are calling back someone after missing their
            # call, it shows up in the history as an outgoing call
            if self.call_status == 'missed':
                self.call_status = 'outgoing'
            call_history.insert(0, self)
            observing = False

    def call_hang_up_incoming(phonecall):  
        """
        Create a missed phone call entry in call_history and add this
        call to available_calls so the player can call the character back.
        """  

        global call_history, available_calls        
        phonecall.call_status = 'missed'
        missed_call = copy(phonecall)
        missed_call.call_time = upTime()
        # Can't play this conversation back as it hasn't been viewed
        missed_call.playback = False
        if missed_call not in call_history:
            call_history.insert(0, missed_call)
        if phonecall not in available_calls:
            available_calls.append(phonecall)
        renpy.retain_after_load()
        
    def call_hang_up(phonecall):
        """
        If the player hangs up during a call, the conversation is no longer
        available. Remove this call from available_calls.
        """

        if phonecall in store.available_calls:
            store.available_calls.remove(phonecall)
        
    def call_available(who):
        """
        Check if a character has any available calls. Return the call if
        found, otherwise return False.
        """

        for phonecall in store.available_calls:
            if who == phonecall.caller:
                return phonecall
        return False
            
    def toggle_afm():
        """Toggle auto-forward mode on and off."""
        _preferences.afm_enable = not _preferences.afm_enable
        renpy.restart_interaction()

    def deliver_calls(lbl, expired=False, call_time=False):
        """
        Make any phonecalls associated with the current chatroom available.
        """

        global available_calls, incoming_call, call_history
        global unseen_calls, all_characters
        missed_call = False
        phonecall = False
        # Add available calls
        for c in all_characters:
            # Add available outgoing calls to the list
            if renpy.has_label(lbl + '_outgoing_' + c.file_id):
                available_calls.append(PhoneCall(c, 
                    lbl + '_outgoing_' + c.file_id, 'outgoing'))

            # Update the incoming call, or move it if the call has expired
            if renpy.has_label(lbl + '_incoming_' + c.file_id):
                if expired:
                    phonecall = PhoneCall(c, lbl + '_incoming_' + c.file_id,
                                    'outgoing')
                    missed_call = PhoneCall(c, lbl + '_incoming_' + c.file_id,
                                    'missed')
                else:
                    incoming_call = PhoneCall(c, lbl + '_incoming_'
                                    + c.file_id, 'incoming')            
        
        # The player backed out of a chatroom; no missed call but should
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
        
# Number of calls the player missed
default unseen_calls = 0
# True if the player is in a phone call (for choice menus etc)
default in_phone_call = False
# Number of seconds to wait for the player to pick up incoming calls
default call_countdown = 10

########################################################
## The phone menu screen, which displays a list of all
## the phone calls the player has received
########################################################
screen phone_calls():

    tag menu

    on 'show' action [FileSave(mm_auto, confirm=False)]
    on 'replace' action [FileSave(mm_auto, confirm=False)]

    use menu_header("Call History", [Show('chat_home', Dissolve(0.5)), 
                                     FileSave(mm_auto, confirm=False)]):
    
        frame:
            style_prefix "phone_contacts"            
            has hbox            
            # History/Contacts tabs
            button:
                hover_background None
                background "menu_tab_active"    
                has hbox
                add 'call_history_icon'
                text "History"
            null width 10         
            button:
                action Show("phone_contacts", Dissolve(0.5))
                has hbox
                add 'contact_icon'
                text "Contacts"
            
        viewport:
            style_prefix 'call_display'          
            draggable True
            mousewheel True
            scrollbars "vertical"
            has vbox
            for i in call_history:
                $ call_status = 'call_' + i.call_status
                if i.playback:
                    $ replay_bkgr = 'call_replay_active'
                else:
                    $ replay_bkgr = 'call_replay_inactive'
                
                frame:          
                    style_prefix None                                           
                    background 'message_idle_bkgr'   
                    xysize (705, 150)

                    has hbox
                    spacing 10  
                    align (0.5, 0.5)
                    frame:
                        xysize (135, 135)
                        align (0.5, 0.5)
                        add i.caller.get_pfp(127):
                            yalign 0.5 xalign 0.5
                    
                    frame:
                        xsize 300
                        yalign 0.5
                        has vbox
                        align (0.0, 0.5)
                        text i.caller.name + ' {image=[call_status]}':
                            style "save_slot_text"
                        spacing 40                                    
                        text i.call_time.get_phone_time() style "save_slot_text"
                        
                    frame:
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
                                        SetVariable('current_call', i),
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

style call_display_viewport:
    xalign 0.5
    yalign 0.95
    xsize 725
    ysize 1070

style call_display_vbox:
    spacing 10

style call_display_side:      
    spacing 5


########################################################
## This screen shows you all the player's phone contacts
## so they can call them
########################################################

screen phone_contacts():

    tag menu
    use menu_header("Contacts", Show('chat_home', Dissolve(0.5))):
    
        frame:
            style_prefix "phone_contacts"            
            has hbox
            # Call History/Contacts tabs
            button:
                action Show("phone_calls", Dissolve(0.5))
                has hbox
                add 'call_history_icon'
                text "History"
            null width 10
            button:
                hover_background None
                background "menu_tab_active"
                has hbox
                add 'contact_icon'
                text "Contacts"                
        
        viewport:    
            style_prefix 'call_display'
            draggable True
            mousewheel True
            scrollbars "vertical" 
            if (len(character_list) > 9
                    or m in character_list and len(character_list) < 10):
                xoffset 20
            has vbox
            xysize (705, 1070)   
            xalign 0.5  
            spacing 0  
            
            # Only characters in character_list show up as contacts
            # though any character in the all_characters list can 
            # phone the player
            if (len(character_list) > 9
                    or m in character_list and len(character_list) > 10):
                use phone_contacts_grid(3, -(-len(character_list) // 3))
            else:
                null height 10
                use phone_contacts_grid(3, 3)

style phone_contacts_frame:
    xalign 0.5
    yalign 0.13
    maximum(700,70)

style phone_contacts_hbox:
    xalign 0.5
    spacing 20
    yalign 0.5

style phone_contacts_text:
    color '#fff'
    font gui.sans_serif_1
    text_align 0.5
    xalign 0.5
    yalign 0.5

style phone_contacts_button:
    xsize 290
    ysize 65
    background "menu_tab_inactive"
    hover_background "menu_tab_inactive_hover"
    activate_sound 'audio/sfx/UI/phone_tab_switch.mp3'        

## This makes the phone contacts screen "flexible" so you can
## have as many or as few characters as you like
screen phone_contacts_grid(x_num, y_num):

    $ has_mc = 0

    grid x_num y_num:        
        style_prefix 'contacts_grid'
        
        for person in character_list:
            if person == m:
                $ has_mc = 1
            else:
                vbox:
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
        
style contacts_grid_grid:
    align (0.5, 0.3)
    xspacing 60
    yspacing 100

style contacts_grid_vbox:
    spacing 25

style contact_text:
    color '#fff' 
    xalign 0.5 
    text_align 0.5
    font sans_serif_1b
    
style caller_id:
    color '#fff'
    xalign 0.5
    text_align 0.5
    font gui.sans_serif_1
    size 70
    yoffset 10
    
style call_text:
    color '#fff'
    xalign 0.5
    yalign 0.5
    text_align 0.5
    font gui.sans_serif_1
    
## This label ensures the rest of the phone conversation will
## not play out if the player hangs up
label hang_up():
    $ renpy.end_replay()
    if observing:
        $ observing = False
    else:
        $ call_hang_up(phonecall=current_call)
    call screen phone_calls
    return
    
########################################################
## This is the screen that displays the dialogue when
## you're in a phone call
########################################################
screen in_call(who=ja):

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

    default show_timer = True
    default countup = 0

    use menu_header("In Call"):
        fixed:
            xysize (750, 1250)
            vbox: 
                style_prefix 'phone_timer'
                add AlphaMask(who.get_pfp(130), 
                        'rounded-rectangle-mask.png') xalign 0.5 
                text who.name size 45
                hbox:
                    text "{0:01}:".format(countup//60) 
                    text "{0:01}".format((countup%60)//10)
                    text "{0:01}".format((countup%60)%10)
            if not starter_story:
                use phone_footer(False, "call_pause", 
                                [Hide('say'), Jump('hang_up')])
            else:
                use phone_footer(False, "call_pause", False)
                                   
    if show_timer:
        timer 1.0 action SetScreenVariable('countup', countup+1) repeat True
                
style phone_timer_text:
    color "#fff" 
    text_align 0.5 
    xalign 0.5 
    size 28

style phone_timer_hbox:
    xalign 0.5
    spacing 1

style phone_timer_vbox:
    yalign 0.08 
    xalign 0.5    
    spacing 10


########################################################
## This is the screen when you're receiving an incoming
## call
########################################################
screen incoming_call(phonecall, countdown_time=10):
    tag menu
    
    on 'hide' action Function(renpy.music.stop)
    use menu_header("In Call"):
        frame:
            xysize (750, 1250)
            frame:
                xfill True
                ysize 500
                yalign 0.1
                background 'call_overlay'                
                has hbox
                align (0.5, 0.5)
                spacing -10
                frame:
                    xysize(120,220)
                    align (1.0, 0.1)
                    has hbox
                    align (1.0, 0.5)
                    spacing -15
                    add 'call_signal_ll' align (0.5, 0.5)
                    null width 10
                    add 'call_signal_ml' align (0.5, 0.5)            
                    add 'call_signal_sl' align (0.5, 0.5)
                frame:
                    align (0.5, 0.5)
                    xsize 350
                    has vbox
                    align (0.5, 0.5)
                    spacing 15
                    add phonecall.caller.get_pfp(237):
                        align (0.5, 0.5)
                    text phonecall.caller.name style 'caller_id'
                frame:
                    xysize(120,220)
                    align (0.0, 0.1)
                    has hbox
                    align (0.0, 0.5)
                    spacing -15
                    add 'call_signal_sr' align (0.5, 0.5)
                    add 'call_signal_mr' align (0.5, 0.5)
                    null width 10
                    add 'call_signal_lr' align (0.5, 0.5)
            
            frame:
                xfill True
                yalign 0.53
                has vbox
                align (0.5, 0.6)
                spacing 10
                text "Incoming Call" color '#fff' xalign 0.5 size 40
                if not starter_story:
                    text "[call_countdown]" xalign 0.5  color '#fff' size 80
                
            if starter_story:
                use phone_footer([Stop('music'), 
                                SetVariable('current_call', phonecall), 
                                Return()], 
                                    "headphones", False)
            else:
                use phone_footer([Stop('music'), 
                                Preference("auto-forward", "enable"), 
                                SetVariable('current_call', phonecall), 
                                Jump(phonecall.phone_label)],
                                "headphones",
                                [Stop('music'), 
                                Function(call_hang_up_incoming, current_call),
                                Show('chat_home')])
  
                
    on 'show' action SetScreenVariable('call_countdown', countdown_time)
    on 'replace' action SetScreenVariable('call_countdown', countdown_time)
    if not starter_story:
        timer 1.0 action If(call_countdown>1, 
                            SetScreenVariable("call_countdown", 
                            call_countdown-1),
                            [Function(call_hang_up_incoming, current_call),
                            Show('chat_home')]) repeat True
 
    
## Screen that shows the pick up/answer buttons at the bottom
screen phone_footer(answer_action=False, 
                    center_item=False, 
                    hangup_action=False):
    frame:
        xysize(710, 200)
        yalign 0.95
        xalign 0.5
        has hbox
        align (0.5, 0.5)
        spacing 10
        frame:
            xysize(160,160)
            align (0.5, 0.5)
            if answer_action:
                imagebutton:
                    align (0.5, 0.5)
                    idle 'call_answer'
                    hover Transform('call_answer', zoom=1.1)
                    action answer_action
        fixed:
            xysize (323, 160)            
            if center_item == "headphones":
                add 'call_headphones' yalign 1.0 xalign 0.5
            elif center_item == "call_pause":
                 imagebutton:
                    align (0.5, 0.5)
                    if _preferences.afm_enable: #preferences.afm_time > 0:
                        idle 'call_pause'
                        action [SetScreenVariable('show_timer', False),
                                PauseAudio('voice', value=True), 
                                Function(toggle_afm)] 
                                #Preference("auto-forward", "toggle")
                    else:
                        idle 'call_play'
                        action [SetScreenVariable('show_timer', True),
                                PauseAudio('voice', value=False), 
                                Function(toggle_afm)] 
                                #Preference("auto-forward", "toggle"
            
        frame:
            xysize(160,160)
            align (0.5, 0.5)
            if hangup_action:
                imagebutton:
                    align (0.5, 0.5)
                    idle 'call_hang_up'
                    hover Transform('call_hang_up', zoom=1.1)
                    action hangup_action
    
########################################################
## This is the screen when you're making a phone call
## to another character
########################################################

define phone_dial_sfx = "audio/sfx/phone ring.mp3"

screen outgoing_call(phonecall, voicemail=False):
    tag menu
    
    
    on 'show' action Function(renpy.music.play, ["<silence 1.5>", 
                        phone_dial_sfx, "<silence 1.5>"], loop=True)
    on 'replace' action Function(renpy.music.play, ["<silence 1.5>", 
                        phone_dial_sfx, "<silence 1.5>"], loop=True)
    
    use menu_header("In Call"):
        frame:
            xysize (750, 1250)
            frame:
                xfill True
                ysize 500
                yalign 0.16
                background 'call_overlay'
                
                has hbox
                align (0.5, 0.5)
                spacing -10
                frame:
                    xysize(120,220)            
                    align (0.5, 0.5)
                    xsize 350
                    has vbox
                    align (0.5, 0.5)
                    spacing 15
                    add phonecall.caller.get_pfp(237):
                        align (0.5, 0.5)
                    text phonecall.caller.name style 'caller_id'
                    
            frame:
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
                
            use phone_footer(False, "headphones", 
                            [Stop('music'), Show('phone_calls')])    
                   
    if voicemail:
        timer randint(8, 10) action If(phonecall, [Stop('music'), 
                                        SetVariable('current_call', phonecall), 
                                        Jump(phonecall.phone_label)], 
                                        Show('phone_calls'))
    else:
        timer randint(2, 7) action [Stop('music'), 
                                    SetVariable('current_call', phonecall), 
                                    Jump(phonecall.phone_label)]
    
## Screen used to say dialogue for phone characters
screen phone_say(who, what):

    window:
        style_prefix None
        style 'call_window'
        text what id "what":
            if persistent.dialogue_outlines:
                outlines [ (absolute(2), "#000", 
                            absolute(0), absolute(0)) ]
    


## Allows the program to jump to the incoming call
label new_incoming_call(phonecall):
    play music persistent.phone_tone loop
    call screen incoming_call(phonecall=phonecall)
    return
 
## This label sets up the appropriate variables/actions when you begin
## a phone call
label phone_begin():
    if starter_story:
        $ set_name_pfp()
    stop music
    # This stops it from recording the dialogue
    # from the phone call in the history log
    $ _history = False
    $ in_phone_call = True
    hide screen incoming_call
    hide screen outgoing_call
    
    # Hide all the popup screens
    $ hide_all_popups()
    
    if _in_replay:
        $ observing = True
        $ set_name_pfp()
        $ set_pronouns()
        
    show screen in_call(current_call.caller)
    return
    
## This label sets the appropriate variables/actions when you finish
## a phone call
label phone_end():
    if not starter_story:
        if not observing:
            $ current_call.finished()
        $ in_phone_call = False
        if not _in_replay and not observing:
            $ persistent.completed_chatrooms[current_call.phone_label] = True
        $ current_call = False    
        $ observing = False
        $ _history = True
        $ renpy.retain_after_load()
        $ renpy.end_replay()
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
    return
