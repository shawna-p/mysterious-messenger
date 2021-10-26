#####################################
## Backgrounds
#####################################

image bg door = "VN Mode/Backgrounds/rika_door_closed.webp"
image bg door_open = "VN Mode/Backgrounds/rika_door_open.webp"
image bg stair = "VN Mode/Backgrounds/rika_apartment_elevator.webp"
image bg mint_eye_room = "VN Mode/Backgrounds/mint_eye_room.webp"
image bg rika_apartment = "VN Mode/Backgrounds/rika_apartment.webp"
image bg cr_meeting_room = "VN Mode/Backgrounds/cr_meeting_room.webp"
image bg yoosung_room_day = "VN Mode/Backgrounds/yoosung_room_day.webp"
image bg yoosung_room_night = "VN Mode/Backgrounds/yoosung_room_night.webp"
image bg zen_room_day = "VN Mode/Backgrounds/zen_room_day.webp"
image bg rfa_party_3 = "VN Mode/Backgrounds/rfa_party_3.webp"
image bg hallway = "VN Mode/Backgrounds/hallway.webp"
image bg rika_door_closed = "VN Mode/Backgrounds/rika_door_closed.webp"
image bg rika_door_open = "VN Mode/Backgrounds/rika_door_open.webp"
image bg guest_walkway = Fixed(
    Transform("#000", size=(750, 1334)),
    Transform("VN Mode/Backgrounds/guest_walkway.webp",
        xalign=0.5, yalign=0.7))
image bg good_end = "VN Mode/Backgrounds/good_end.webp"
image bg normal_end = "VN Mode/Backgrounds/normal_end.webp"
image bg bad_end = "VN Mode/Backgrounds/bad_end.webp"
image bg black = '#000000'


#####################################
## Transforms/VN Positions
#####################################

# In order from leftmost to rightmost pose
transform vn_farleft:
    xalign 0.0
    yalign 1.0
    xoffset -300
    yoffset 0
    zoom 1.0

transform vn_left:
    xalign 0.0
    yalign 1.0
    xoffset -100
    zoom 1.0

transform vn_midleft:
    xalign 0.0
    yalign 1.0
    xoffset -50
    zoom 1.0

transform vn_center:
    xalign 0.5
    yalign 0.5
    zoom 1.15
    yoffset 280
    xoffset 0
    xanchor 0.5
    yanchor 0.5

transform vn_midright:
    xalign 1.0
    yalign 1.0
    xoffset 50
    zoom 1.0

transform vn_right:
    xalign 1.0
    yalign 1.0
    xoffset 100
    zoom 1.0

transform vn_farright:
    xalign 1.0
    yalign 1.0
    yoffset 0
    xoffset 300
    zoom 1.0
