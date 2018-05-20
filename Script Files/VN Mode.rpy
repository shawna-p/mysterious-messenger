#************************************
#************************************
#********Visual Novel Mode***********
#************************************
#************************************


## BACKGROUNDS **********************

image bg mint_eye_room = "VN Mode/Backgrounds/mint_eye_room.png"





## CHARACTERS ***********************

define sev = Character("707", what_font="00 fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf", 
                            what_color="#ffffff", window_background="VN Mode/Chat Bubbles/vnmode_2.png",
                            who_color="fff5ca", who_size=40)
define yoo = Character("Yoosung")
define mc = Character("[name]")     # dynamic=True?
define jae = Character("Jaehee")
define jum = Character("Jumin")
define V = Character("V")
define ri = Character("Rika")
define sae = Character("Saeran", what_font="00 fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf", 
                            what_color="#ffffff", window_background="VN Mode/Chat Bubbles/vnmode_8.png",
                            who_color="fff5ca", who_size=40)
define ray = Character("Ray", what_font="00 fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf", 
                            what_color="#ffffff", window_background="VN Mode/Chat Bubbles/vnmode_9.png",
                            who_color="fff5ca", who_size=40)
define un = Character("???")
define zen = Character("Zen", what_font="00 fonts/NanumMyeongjo (Serif font 1)/NanumMyeongjo-Regular.ttf", 
                            what_color="#ffffff", window_background="VN Mode/Chat Bubbles/vnmode_1.png",
                            who_color="fff5ca", who_size=40)

default sev_face = None
default sev_body = "normal"
default sae_face = None
default sae_body = "unknown"
default zen_body = "normal"
default zen_face = None

# Yes this looks long, but this encompasses all of Seven's expressions
# from his front-facing positions
image seven front = ConditionSwitch(
        "sev_face == 'happy'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sev_body == 'normal'", "VN Mode/707/seven_body_0.png",
                "sev_body == 'arm'", "VN Mode/707/seven_body_1.png",
                "sev_body == 'party'", "VN Mode/707/seven_party_0.png"),
            (182, 145), "VN Mode/707/seven_face_0.png",
            ),
        "sev_face == 'blush'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sev_body == 'normal'", "VN Mode/707/seven_body_0.png",
                "sev_body == 'arm'", "VN Mode/707/seven_body_1.png",
                "sev_body == 'party'", "VN Mode/707/seven_party_0.png"),
            (182, 145), "VN Mode/707/seven_face_1.png",
            ),
        "sev_face == 'neutral'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sev_body == 'normal'", "VN Mode/707/seven_body_0.png",
                "sev_body == 'arm'", "VN Mode/707/seven_body_1.png",
                "sev_body == 'party'", "VN Mode/707/seven_party_0.png"),
            (182, 145), "VN Mode/707/seven_face_2.png",
            ),
        "sev_face == 'surprise'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sev_body == 'normal'", "VN Mode/707/seven_body_0.png",
                "sev_body == 'arm'", "VN Mode/707/seven_body_1.png",
                "sev_body == 'party'", "VN Mode/707/seven_party_0.png"),
            (182, 145), "VN Mode/707/seven_face_3.png",
            ),
        "sev_face == 'serious'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sev_body == 'normal'", "VN Mode/707/seven_body_0.png",
                "sev_body == 'arm'", "VN Mode/707/seven_body_1.png",
                "sev_body == 'party'", "VN Mode/707/seven_party_0.png"),
            (182, 145), "VN Mode/707/seven_face_4.png",
            ),
        "sev_face == 'eyes closed'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sev_body == 'normal'", "VN Mode/707/seven_body_0.png",
                "sev_body == 'arm'", "VN Mode/707/seven_body_1.png",
                "sev_body == 'party'", "VN Mode/707/seven_party_0.png"),
            (182, 145), "VN Mode/707/seven_face_5.png",
            ),
        "sev_face == 'sad'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sev_body == 'normal'", "VN Mode/707/seven_body_0.png",
                "sev_body == 'arm'", "VN Mode/707/seven_body_1.png",
                "sev_body == 'party'", "VN Mode/707/seven_party_0.png"),
            (182, 141), "VN Mode/707/seven_face_6.png",
            ),
        "sev_face == 'worried'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sev_body == 'normal'", "VN Mode/707/seven_body_0.png",
                "sev_body == 'arm'", "VN Mode/707/seven_body_1.png",
                "sev_body == 'party'", "VN Mode/707/seven_party_0.png"),
            (182, 145), "VN Mode/707/seven_face_7.png",
            ),
        "sev_face == 'dark'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sev_body == 'normal'", "VN Mode/707/seven_body_0.png",
                "sev_body == 'arm'", "VN Mode/707/seven_body_1.png",
                "sev_body == 'party'", "VN Mode/707/seven_party_0.png"),
            (182, 145), "VN Mode/707/seven_face_8.png",
            ),
        "sev_face == 'angry'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sev_body == 'normal'", "VN Mode/707/seven_body_0.png",
                "sev_body == 'arm'", "VN Mode/707/seven_body_1.png",
                "sev_body == 'party'", "VN Mode/707/seven_party_0.png"),
            (182, 145), "VN Mode/707/seven_face_9.png",
            ),
        "sev_face == 'hurt'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sev_body == 'normal'", "VN Mode/707/seven_body_0.png",
                "sev_body == 'arm'", "VN Mode/707/seven_body_1.png",
                "sev_body == 'party'", "VN Mode/707/seven_party_0.png"),
            (182, 141), "VN Mode/707/seven_face_10.png",
            ),
        "sev_face == None", "VN Mode/707/seven_body_0.png")


image seven side = ConditionSwitch(
        "sev_face == 'happy'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sev_body == 'normal'", "VN Mode/707/seven_sidebody_0.png",
                "sev_body == 'arm'", "VN Mode/707/seven_sidebody_1.png",
                "sev_body == 'party'", "VN Mode/707/seven_valentines_0.png"),
            (260, 147), "VN Mode/707/seven_sideface_0.png",
            ),
        "sev_face == 'concern'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sev_body == 'normal'", "VN Mode/707/seven_sidebody_0.png",
                "sev_body == 'arm'", "VN Mode/707/seven_sidebody_1.png",
                "sev_body == 'party'", "VN Mode/707/seven_valentines_0.png"),
            (255, 147), "VN Mode/707/seven_sideface_1.png",
            ),
        "sev_face == 'surprise'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sev_body == 'normal'", "VN Mode/707/seven_sidebody_0.png",
                "sev_body == 'arm'", "VN Mode/707/seven_sidebody_1.png",
                "sev_body == 'party'", "VN Mode/707/seven_valentines_0.png"),
            (257, 147), "VN Mode/707/seven_sideface_2.png",
            ),
        "sev_face == 'eyes closed'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sev_body == 'normal'", "VN Mode/707/seven_sidebody_0.png",
                "sev_body == 'arm'", "VN Mode/707/seven_sidebody_1.png",
                "sev_body == 'party'", "VN Mode/707/seven_valentines_0.png"),
            (260, 147), "VN Mode/707/seven_sideface_3.png",
            ),
        "sev_face == 'sad'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sev_body == 'normal'", "VN Mode/707/seven_sidebody_0.png",
                "sev_body == 'arm'", "VN Mode/707/seven_sidebody_1.png",
                "sev_body == 'party'", "VN Mode/707/seven_valentines_0.png"),
            (253, 150), "VN Mode/707/seven_sideface_4.png",
            ),
        "sev_face == 'neutral'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sev_body == 'normal'", "VN Mode/707/seven_sidebody_0.png",
                "sev_body == 'arm'", "VN Mode/707/seven_sidebody_1.png",
                "sev_body == 'party'", "VN Mode/707/seven_valentines_0.png"),
            (255, 151), "VN Mode/707/seven_sideface_5.png",
            ),
        "sev_face == 'dark'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sev_body == 'normal'", "VN Mode/707/seven_sidebody_0.png",
                "sev_body == 'arm'", "VN Mode/707/seven_sidebody_1.png",
                "sev_body == 'party'", "VN Mode/707/seven_valentines_0.png"),
            (257, 147), "VN Mode/707/seven_sideface_6.png",
            ),
        "sev_face == 'angry'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sev_body == 'normal'", "VN Mode/707/seven_sidebody_0.png",
                "sev_body == 'arm'", "VN Mode/707/seven_sidebody_1.png",
                "sev_body == 'party'", "VN Mode/707/seven_valentines_0.png"),
            (256, 135), "VN Mode/707/seven_sideface_7.png",
            ),
        "sev_face == 'worried'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sev_body == 'normal'", "VN Mode/707/seven_sidebody_0.png",
                "sev_body == 'arm'", "VN Mode/707/seven_sidebody_1.png",
                "sev_body == 'party'", "VN Mode/707/seven_valentines_0.png"),
            (252, 147), "VN Mode/707/seven_sideface_8.png",
            ),
        "sev_face == None", "VN Mode/707/seven_sidebody_0.png")
        
image saeran front = ConditionSwitch(
        "sae_face == 'happy'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sae_body == 'unknown'", "VN Mode/Unknown/unknown_body_0.png",
                "sae_body == 'ray'", "VN Mode/Unknown/unknown_body_2.png",
                "sae_body == 'suit'", "VN Mode/Unknown/unknown_body_3.png",
                "sae_body == 'saeran'", "VN Mode/Unknown/unknown_body_4.png"),
            (205, 140), "VN Mode/Unknown/unknown_face_0.png",
            ),
        "sae_face == 'smile'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sae_body == 'unknown'", "VN Mode/Unknown/unknown_body_0.png",
                "sae_body == 'ray'", "VN Mode/Unknown/unknown_body_2.png",
                "sae_body == 'suit'", "VN Mode/Unknown/unknown_body_3.png",
                "sae_body == 'saeran'", "VN Mode/Unknown/unknown_body_4.png"),
            (201, 140), "VN Mode/Unknown/unknown_face_1.png",
            ),
        "sae_face == 'neutral'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sae_body == 'unknown'", "VN Mode/Unknown/unknown_body_0.png",
                "sae_body == 'ray'", "VN Mode/Unknown/unknown_body_2.png",
                "sae_body == 'suit'", "VN Mode/Unknown/unknown_body_3.png",
                "sae_body == 'saeran'", "VN Mode/Unknown/unknown_body_4.png"),
            (204, 145), "VN Mode/Unknown/unknown_face_2.png",
            ),
        "sae_face == 'angry'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sae_body == 'unknown'", "VN Mode/Unknown/unknown_body_0.png",
                "sae_body == 'ray'", "VN Mode/Unknown/unknown_body_2.png",
                "sae_body == 'suit'", "VN Mode/Unknown/unknown_body_3.png",
                "sae_body == 'saeran'", "VN Mode/Unknown/unknown_body_4.png"),
            (204, 147), "VN Mode/Unknown/unknown_face_3.png",
            ),
        "sae_face == 'eyes closed'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sae_body == 'unknown'", "VN Mode/Unknown/unknown_body_0.png",
                "sae_body == 'ray'", "VN Mode/Unknown/unknown_body_2.png",
                "sae_body == 'suit'", "VN Mode/Unknown/unknown_body_3.png",
                "sae_body == 'saeran'", "VN Mode/Unknown/unknown_body_4.png"),
            (207, 140), "VN Mode/Unknown/unknown_face_4.png",
            ),
        "sae_face == 'tense'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sae_body == 'unknown'", "VN Mode/Unknown/unknown_body_0.png",
                "sae_body == 'ray'", "VN Mode/Unknown/unknown_body_2.png",
                "sae_body == 'suit'", "VN Mode/Unknown/unknown_body_3.png",
                "sae_body == 'saeran'", "VN Mode/Unknown/unknown_body_4.png"),
            (203, 144), "VN Mode/Unknown/unknown_face_5.png",
            ),
        "sae_face == 'creepy'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sae_body == 'unknown'", "VN Mode/Unknown/unknown_body_0.png",
                "sae_body == 'ray'", "VN Mode/Unknown/unknown_body_2.png",
                "sae_body == 'suit'", "VN Mode/Unknown/unknown_body_3.png",
                "sae_body == 'saeran'", "VN Mode/Unknown/unknown_body_4.png"),
            (198, 145), "VN Mode/Unknown/unknown_face_6.png",
            ),
        "sae_face == 'cry'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sae_body == 'unknown'", "VN Mode/Unknown/unknown_body_0.png",
                "sae_body == 'ray'", "VN Mode/Unknown/unknown_body_2.png",
                "sae_body == 'suit'", "VN Mode/Unknown/unknown_body_3.png",
                "sae_body == 'saeran'", "VN Mode/Unknown/unknown_body_4.png"),
            (202, 137), "VN Mode/Unknown/unknown_face_7.png",
            ),
        "sae_face == 'blush'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sae_body == 'unknown'", "VN Mode/Unknown/unknown_body_0.png",
                "sae_body == 'ray'", "VN Mode/Unknown/unknown_body_2.png",
                "sae_body == 'suit'", "VN Mode/Unknown/unknown_body_3.png",
                "sae_body == 'saeran'", "VN Mode/Unknown/unknown_body_4.png"),
            (205, 145), "VN Mode/Unknown/unknown_face_15.png",
            ),
        "sae_face == 'sob'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sae_body == 'unknown'", "VN Mode/Unknown/unknown_body_0.png",
                "sae_body == 'ray'", "VN Mode/Unknown/unknown_body_2.png",
                "sae_body == 'suit'", "VN Mode/Unknown/unknown_body_3.png",
                "sae_body == 'saeran'", "VN Mode/Unknown/unknown_body_4.png"),
            (205, 143), "VN Mode/Unknown/unknown_face_16.png",
            ),
        "sae_face == 'teary'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sae_body == 'unknown'", "VN Mode/Unknown/unknown_body_0.png",
                "sae_body == 'ray'", "VN Mode/Unknown/unknown_body_2.png",
                "sae_body == 'suit'", "VN Mode/Unknown/unknown_body_3.png",
                "sae_body == 'saeran'", "VN Mode/Unknown/unknown_body_4.png"),
            (208, 144), "VN Mode/Unknown/unknown_face_17.png",
            ),
        "sae_face == 'nervous'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sae_body == 'unknown'", "VN Mode/Unknown/unknown_body_0.png",
                "sae_body == 'ray'", "VN Mode/Unknown/unknown_body_2.png",
                "sae_body == 'suit'", "VN Mode/Unknown/unknown_body_3.png",
                "sae_body == 'saeran'", "VN Mode/Unknown/unknown_body_4.png"),
            (203, 142), "VN Mode/Unknown/unknown_face_18.png",
            ),
        "sae_face == 'sad'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sae_body == 'unknown'", "VN Mode/Unknown/unknown_body_0.png",
                "sae_body == 'ray'", "VN Mode/Unknown/unknown_body_2.png",
                "sae_body == 'suit'", "VN Mode/Unknown/unknown_body_3.png",
                "sae_body == 'saeran'", "VN Mode/Unknown/unknown_body_4.png"),
            (202, 146), "VN Mode/Unknown/unknown_face_19.png",
            ),
        "sae_face == 'worried'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sae_body == 'unknown'", "VN Mode/Unknown/unknown_body_0.png",
                "sae_body == 'ray'", "VN Mode/Unknown/unknown_body_2.png",
                "sae_body == 'suit'", "VN Mode/Unknown/unknown_body_3.png",
                "sae_body == 'saeran'", "VN Mode/Unknown/unknown_body_4.png"),
            (205, 146), "VN Mode/Unknown/unknown_face_20.png",
            ),
        "sae_face == 'distant'", LiveComposite(
            (425, 1005),
            (0, 0), ConditionSwitch(
                "sae_body == 'unknown'", "VN Mode/Unknown/unknown_body_0.png",
                "sae_body == 'ray'", "VN Mode/Unknown/unknown_body_2.png",
                "sae_body == 'suit'", "VN Mode/Unknown/unknown_body_3.png",
                "sae_body == 'saeran'", "VN Mode/Unknown/unknown_body_4.png"),
            (205, 142), "VN Mode/Unknown/unknown_face_21.png",
            ),
        "sae_face == None", "VN Mode/Unknown/unknown_body_0.png")
        
image saeran mask = ConditionSwitch(
        "sae_face == 'happy'", LiveComposite(
            (425, 1005),
            (0, 0), "VN Mode/Unknown/unknown_body_1.png",
            (205, 140), "VN Mode/Unknown/unknown_face_8.png",
            ),
        "sae_face == 'smile'", LiveComposite(
            (425, 1005),
            (0, 0), "VN Mode/Unknown/unknown_body_1.png",
            (205, 140), "VN Mode/Unknown/unknown_face_9.png",
            ),
        "sae_face == 'neutral'", LiveComposite(
            (425, 1005),
            (0, 0), "VN Mode/Unknown/unknown_body_1.png",
            (205, 148), "VN Mode/Unknown/unknown_face_10.png",
            ),
        "sae_face == 'angry'", LiveComposite(
            (425, 1005),
            (0, 0), "VN Mode/Unknown/unknown_body_1.png",
            (205, 146), "VN Mode/Unknown/unknown_face_11.png",
            ),
        "sae_face == 'eyes closed'", LiveComposite(
            (425, 1005),
            (0, 0), "VN Mode/Unknown/unknown_body_1.png",
            (205, 144), "VN Mode/Unknown/unknown_face_12.png",
            ),
        "sae_face == 'tense'", LiveComposite(
            (425, 1005),
            (0, 0), "VN Mode/Unknown/unknown_body_1.png",
            (205, 144), "VN Mode/Unknown/unknown_face_13.png",
            ),
        "sae_face == 'creepy'", LiveComposite(
            (425, 1005),
            (0, 0), "VN Mode/Unknown/unknown_body_1.png",
            (202, 146), "VN Mode/Unknown/unknown_face_14.png",
            ),
        "sae_face == None", "VN Mode/Unknown/unknown_body_1.png")
        
        
image zen front = ConditionSwitch(
    "zen_face == 'happy'", LiveComposite(
        (425, 978),
        (0, 0), ConditionSwitch(
            "zen_body == 'normal'", "VN Mode/Zen/zen_body_0.png",
            "zen_body == 'arm'", "VN Mode/Zen/zen_body_1.png",
            "zen_body == 'party'", "VN Mode/Zen/zen_party_0.png"),
        (140, 118), "VN Mode/Zen/zen_face_0.png",
        ),
        "zen_face == None", "VN Mode/Zen/zen_body_0.png")
        
## Seven's front expressions:
# happy, blush, neutral, surprise, serious, eyes closed,
# sad, worried, dark, angry, hurt
## Side expressions:
# happy, concern, surprise, sad, neutral, dark, angry, worried

## Saeran's front expressions:
# happy, smile, neutral, angry, eyes closed, tense, creepy, cry,
# blush, sob, teary, nervous, sad, worried, distant
## Mask expressions: 
# happy, smile, neutral, angry, eyes closed, tense, creepy

label vn_mode:

    call vn_setup

    scene bg mint_eye_room

    $ sev_body = 'normal'
    $ sev_face = 'happy'
    $ sae_body = 'ray'
    $ sae_face = 'neutral'
    
    show seven front at default
    sev "Hello~!"
    sev "This is what the VN mode looks like so far."
    show seven front at right with ease
    show saeran front at left with easeinleft
    ray "It's not perfect, but you can fit two characters on-screen."
    $ sae_face = 'happy'
    ray "With some more work, hopefully it will look like it does in-game!"
    
    call press_save_and_exit(False)
    
label vn_setup:
    $ chatroom_hp = 0
    hide screen starry_night
    hide screen phone_overlay
    hide screen messenger_screen 
    hide screen pause_button
    hide screen chatroom_timeline
    $ vn_choice = True
        
    if current_chatroom.vn_obj.played:
        $ observing = True
    else:
        $ observing = False
        
