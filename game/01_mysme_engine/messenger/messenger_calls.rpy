########################################################
## This file contains several functions related to
## the messenger system. It's organized as follows:
##   label chat_begin
##   def set_chatroom_background
##   label chat_end
##   label chat_end_route
##   label vn_during_chat
##   label chat_back
##   screen save_and_exit
##      label press_save_and_exit
##   screen signature_screen
########################################################

#####################################
# Chat Setup
#####################################

# This simplifies things when you're setting up a chatroom,
# so call it when you're about to begin.
# Pass it the name of the background you want (enclosed in
# single ' or double " quotes).
# Note that it automatically clears the chatlog, so if you want
# to change the background but not clear the messages on-screen,
# you also have to pass it 'False' as its second argument.

label chat_begin(background=None, clearchat=True, resetHP=True):
    $ set_chatroom_background(background)
    $ begin_timeline_item(generic_chatroom, clearchat, resetHP)
    return

## This label simplifies setting up backgrounds for chatrooms
## It takes the name of a background and shows the corresponding
## static or animated background
init python:
    def set_chatroom_background(new_bg):
        """Set the correct background and nickname colour."""

        if new_bg is None:
            renpy.scene()
            renpy.show('bg black')
            store.current_background = 'morning'
            return

        if new_bg[:3] == 'bg ':
            new_bg = new_bg[3:]

        store.current_background = new_bg
        if new_bg in store.all_static_backgrounds:
            renpy.scene()
            renpy.show('bg ' + new_bg)
        # If the background is misspelled or can't be found, set
        # a generic black background
        else:
            renpy.scene()
            renpy.show('bg black')
            store.current_background = 'morning'
            print("WARNING: Could not find the background \"bg " + new_bg + "\"")
            renpy.show_screen('script_error',
                message="Could not find the background \"bg " + new_bg + "\"")

        if store.persistent.animated_backgrounds:
            if new_bg in store.all_animated_backgrounds:
                try:
                    renpy.show_screen('animated_' + new_bg, _layer='animated_bg')
                except:
                    print("WARNING: Could not find the screen \"animated_"
                        + new_bg + "\"")
                    renpy.show_screen('script_error',
                        message="Could not find the screen \"animated_"
                            + new_bg + "\"")
            elif new_bg == 'hack':
                renpy.show_screen('animated_hack_background', _layer='animated_bg')
            elif new_bg == 'redhack':
                renpy.show_screen('animated_hack_background', red=True, _layer='animated_bg')

        if new_bg in store.black_text_bgs:
            store.nickColour = store.black
        else:
            store.nickColour = store.white

        # Add this background to the replay log, if applicable
        if not store.observing and not store.persistent.testing_mode:
            bg_entry = ('background', store.current_background)
            store.current_timeline_item.replay_log.append(bg_entry)

        return


## This label ends a chatroom.
label chat_end():
    if starter_story and not renpy.get_return_stack():
        jump end_prologue
    return

## Jump to this label at the very end of the route to show a good/bad/normal
# ending sign and return the player to the main menu.
label chat_end_route():
    jump end_route

## This label clears the necessary chatroom variables to allow
## you to show a VN section in the middle of a chatroom
## The VN section needs to be defined in its own separate label
label vn_during_chat(vn_label, clearchat_on_return=False, new_bg=False,
                     reset_participants=False, end_after_vn=False):

    # Add an instruction for the replay log
    if (not observing and not persistent.testing_mode):
        $ vn_jump_entry = ("vn jump",
            [vn_label, clearchat_on_return, new_bg, reset_participants])
        $ current_timeline_item.replay_log.append(vn_jump_entry)

    # Give the player a moment to read the last of the messages
    # before jumping to the VN
    $ renpy.pause(persistent.pv*2.0)
    call screen continue_button
    # Hide all the chatroom screens
    $ reset_story_vars(vn_jump=True)

    # Setup the VN stuff
    window auto

    show screen vn_overlay
    $ vn_choice = True
    $ _history_list = []
    $ _history = True
    $ _preferences.afm_enable = False

    # Don't worry about setting `observing` as it should
    # still be set from the connected chatroom
    $ renpy.call(vn_label)

    # At this point the program has returned from the VN section
    # and must set up the chatroom again, unless the chat is supposed
    # to end now
    if end_after_vn:
        return

    $ reset_story_vars(vn_jump=True)
    if clearchat_on_return:
        $ chatlog = []
        $ addchat(filler, "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", 0)

    if not clearchat_on_return:
        # If the chat isn't cleared this cleans up the transition
        # between VN and chatroom
        show screen non_menu_loading_screen
        show screen phone_overlay
        show screen messenger_screen
        show screen pause_button
        window hide
        if new_bg:
            $ set_chatroom_background(new_bg)
        else:
            $ set_chatroom_background(current_background)
        pause 0.5
        hide screen non_menu_loading_screen
    else:
        show screen phone_overlay
        show screen messenger_screen
        show screen pause_button
        window hide
        if new_bg:
            $ set_chatroom_background(new_bg)
        else:
            $ set_chatroom_background(current_background)

    python:
        if reset_participants:
            in_chat = []
            for person in reset_participants:
                in_chat.append(person.name)
                if not observing:
                    current_timeline_item.add_participant(person)

    # If this is part of a replayed chatroom, go back to
    # the replay log (NOT replayed from the History in the
    # main menu)
    if (observing and not vn_choice and not text_msg_reply
            and not in_phone_call and not email_reply
            and not _in_replay):
        $ replay_from = chatroom_replay_index
        jump chatroom_replay
    return

## A very simple screen used for transitions
screen non_menu_loading_screen():
    zorder 100
    add Solid("#000")
    use loading_screen


#####################################
# Save & Exit
#####################################

# This is the screen that shows Save & Exit at the bottom
screen save_and_exit():
    zorder 4
    tag chat_footer
    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 0
        ypos 1220
        focus_mask True
        idle "save_exit"
        keysym "K_SPACE"
        action Return()

label press_save_and_exit():
    return


# This shows the signature screen, which records your total heart points
# It shows hourglass points as well
screen signature_screen(phone=True):
    zorder 5
    modal True
    style_prefix "sig_screen"
    if phone:
        add "save_exit" ypos 1220
    add "choice_darken"
    frame:
        has vbox
        spacing 10
        null height 70
        if (observing or current_timeline_item.currently_expired):
            null height 10
        text "This conversation will be archived in the RFA records.":
            layout 'subtitle'
            size 30
            if persistent.custom_footers:
                color "#fff"
        if not (observing or current_timeline_item.currently_expired):
            hbox:
                style_prefix "sig_points"
                frame:
                    background 'heart_sign'
                    text str(get_collected_hp())
                frame:
                    background 'hg_sign'
                    text str(collected_hg)

        text "I hereby agree to treat this conversation as confidential.":
            if persistent.custom_footers:
                color "#fff"

        if (observing or current_timeline_item.currently_expired):
            null height 15

        textbutton _('sign'):
            if persistent.custom_footers:
                text_color "#fff"
            action Return()
            keysym "K_SPACE"

style sig_screen_frame:
    xalign 0.5
    yalign 0.5
    xsize 682
    ysize 471
    background 'signature'

style sig_screen_vbox:
    align (0.5, 0.5)

style sig_points_fixed:
    xalign 0.5
    ysize 60
    xsize 682

style sig_points_hbox:
    spacing 105
    yalign 0.5
    xalign 0.5

style sig_points_frame:
    ysize 60
    xsize 154
    padding (62, 12, 20, 12)

style sig_points_text:
    is text
    yalign 1.0
    xalign 1.0
    text_align 1.0
    font sans_serif_1
    color "#ffffff"

style sig_screen_text:
    is text
    xalign 0.5
    text_align 0.5
    size 25
    xsize 600
    font gui.sans_serif_1

style sig_screen_button:
    xysize (211, 52)
    align (0.5, 0.842)
    focus_mask True
    background 'sign_btn' padding(20,20)
    activate_sound "audio/sfx/UI/end_chatroom.mp3"
    hover_background 'sign_btn_clicked'

style sig_screen_button_text:
    is text
    xalign 0.5
    yalign 0.607
    text_align 0.5
    size 30
    font gui.sans_serif_1

## Jumping to this label during an introductory/prologue label
## allows the program to properly set up variables before taking
## the player to the chat home screen
label skip_intro_setup():
    if _in_replay:
        $ renpy.end_replay()
    $ persistent.first_boot = False
    $ persistent.on_route = True

    if vn_choice:
        $ vn_choice = False
        $ phone = False
    $ most_recent_item = story_archive[0].archive_list[0]
    $ collected_hp = {'good': [], 'bad': [], 'break': []}
    $ collected_hg = 0
    $ reset_story_vars()

    show screen loading_screen

    # Add this label to the list of completed labels
    $ current_timeline_item.mark_self_played()
    if not current_timeline_item.expired:
        # Checks for a post-chatroom label
        # Otherwise delivers phone calls/texts/etc
        $ current_timeline_item.call_after_label()
        $ deliver_calls(current_timeline_item.item_label)

    # Deliver emails and trigger the next chatroom (if applicable)
    $ deliver_emails()
    $ check_and_unlock_story()
    # Make sure any images shown are unlocked
    $ check_for_CGs(all_albums)
    $ renpy.retain_after_load()
    # Check to see if the honey buddha chips should be available
    if not chips_available:
        $ chips_available = hbc_bag.draw()

    # This helps clean up the transition between sections
    # in case it takes the program a few moments to calculate
    # messages, emails, etc
    pause 0.2
    hide screen loading_screen
    $ starter_story = False
    $ print_file("\nAbout to call chat_home")
    $ renpy.save(mm_auto)
    call screen chat_home
    $ print_file("\nWe did indeed return here")
    return






