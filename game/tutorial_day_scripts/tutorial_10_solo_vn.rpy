label example_solo_vn():
    call vn_begin
    play music i_draw
    show bg mint_eye_room
    show v front happy
    v "This is some example dialogue."
    v thinking "I don't know if this will work."
    v "Anyway."
    jump vn_end

label example_solo_vn_incoming_v():
    call phone_begin()
    v """
    
    This is a test call.

    Is it working?

    I hope so.

    Anyway I'll hang up.

    """
    jump phone_end

label example_solo_vn_branch():
    if attending_guests() >= 1:
        # Good End
        # Since this means the program should simply continue
        # on with the rest of the route, you can use
        $ continue_route()
        # which tells the program to get rid of the plot branch
        # icon and continue the game as normal
    else:
        # Bad End
        $ merge_routes(tutorial_bad_end)
    jump plot_branch_end