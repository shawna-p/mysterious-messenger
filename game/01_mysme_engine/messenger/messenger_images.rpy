## ********************************
## Chatroom Images
## ********************************

image answerbutton:
    block:
        "answer_dark" with Dissolve(0.5)
        1.0
        "answer_reg" with Dissolve(0.5)
        1.0
        repeat

image custom_answerbutton:
    block:
        "custom_answer_reg" with Dissolve(1.0)
        1.3
        "custom_answer_dark" with Dissolve(1.0)
        1.0
        repeat

image darklight_continue_button:
    block:
        "Phone UI/Continue-light.webp" with Dissolve(1.0)
        1.3
        "Phone UI/Continue-dark.webp" with Dissolve(1.0)
        1.0
        repeat

image custom_darklight_continue_button:
    block:
        "Phone UI/custom-continue-light.webp" with Dissolve(1.0)
        1.3
        "Phone UI/custom-continue-dark.webp" with Dissolve(1.0)
        1.0
        repeat


image phone_continue_button = ConditionSwitch(
    "persistent.custom_footers", "Phone UI/custom-continue.webp",
    "True", "Phone UI/Continue.webp"
)

# This is the actual button that's pressed; the program
# performs better having a transparent button vs an animated one
image transparent_answer = "Phone UI/answer_transparent.webp"

image pausebutton:
    "pause_sign" with Dissolve(0.5)
    1.0
    "transparent_img" with Dissolve(0.5)
    1.0
    repeat

image custom_pausebutton:
    "custom_pause_sign" with Dissolve(0.5)
    1.0
    "transparent_img" with Dissolve(0.5)
    1.0
    repeat

image pause_square = ConditionSwitch(
    "persistent.custom_footers", "Phone UI/custom-pause-square.webp",
    "True", "Phone UI/pause_square.webp"
)

image phone_pause = ConditionSwitch(
    "persistent.custom_footers", "Phone UI/custom-pause.webp",
    "True", "Phone UI/Pause.webp"
)

image phone_play = ConditionSwitch(
    "persistent.custom_footers", "Phone UI/custom-play.webp",
    "True", "Phone UI/Play.webp"
)

image save_exit = ConditionSwitch(
    "persistent.custom_footers", "Phone UI/custom-save-exit.webp",
    "True", "Phone UI/Save&Exit.webp"
)


image fast_slow_button = "Phone UI/fast-slow-transparent.webp"
image maxSpeed_selected_hover = Transform("max_speed_active", zoom=1.1)
image maxSpeed_hover = Transform("max_speed_inactive", zoom=1.1)
image speed_txt = ParameterizedText(style="speednum_style")
image close_button = Transform(Solid("#00000066"), size=(config.screen_width,99))

image signature = ConditionSwitch(
    "persistent.custom_footers", "Phone UI/signature01-dark.webp",
    "True", "Phone UI/signature01.webp"
)
image heart_sign = "Phone UI/heart-sign.webp"
image hg_sign = "Phone UI/hg-sign.webp"

image answer_dark = "Phone UI/Answer-Dark.webp"
image answer_reg = "Phone UI/Answer.webp"
image pause_sign = "Phone UI/pause_sign.webp"

image custom_answer_dark = "Phone UI/custom-answer.webp"
image custom_answer_reg = "Phone UI/custom-answer-dark.webp"
image custom_pause_sign = "Phone UI/custom-pause-sign.webp"

image phone_ui = ConditionSwitch(
    "persistent.custom_footers", "Phone UI/Phone-UI.webp",
    "True", "Phone UI/Phone-UI-old.webp"
)

image maxSpeed_selected_idle = "Phone UI/max_speed_active.webp"
image maxSpeed_idle = "Phone UI/max_speed_inactive.webp"
image back_arrow_btn = ConditionSwitch(
    "persistent.custom_footers", "Phone UI/back-arrow.webp",
    "True", "menu_back"
)

image choice_darken = Solid("#0000006e")
image save_trash = "Menu Screens/Main Menu/save_trash_hover.webp"

image sign_btn = ConditionSwitch(
    "persistent.custom_footers", "Phone UI/sign-button-dark.webp",
    "True", "Phone UI/sign-button.webp"
)
image sign_btn_clicked = ConditionSwitch(
    "persistent.custom_footers", "Phone UI/sign-button-clicked-dark.webp",
    "True", "Phone UI/sign-button-clicked.webp"
)

image battery_high = "Phone UI/battery_high.webp"
image battery_med = "Phone UI/battery_med.webp"
image battery_low = "Phone UI/battery_low.webp"
image battery_empty_img = "Phone UI/battery_empty.webp"
image battery_charged = "Phone UI/battery_charged.webp"
image battery_charging = "Phone UI/battery_charging.webp"

image skip_intro_idle = "Phone UI/skip_intro_available.webp"
image skip_intro_hover = "Phone UI/skip_intro_pressed.webp"
image skip_to_end_idle = "Phone UI/skip_to_end_available.webp"
image skip_to_end_hover = "Phone UI/skip_to_end_pressed.webp"

image hack scroll:
    "hack_long"
    subpixel True
    yalign 0.0
    linear 1.0 yalign 1.0
    yalign 0.0
    linear 1.0 yalign 1.0
    yalign 0.0
    linear 1.0 yalign 1.0

image hack scroll reverse:
    "hack_long"
    subpixel True
    yalign 1.0
    linear 1.0 yalign 0.0
    yalign 1.0
    linear 1.0 yalign 0.0
    yalign 1.0
    linear 1.0 yalign 0.0

image redhack scroll:
    "red_hack_long"
    subpixel True
    yalign 0.0
    linear 1.0 yalign 1.0
    yalign 0.0
    linear 1.0 yalign 1.0
    yalign 0.0
    linear 1.0 yalign 1.0

image redhack scroll reverse:
    "red_hack_long"
    subpixel True
    yalign 1.0
    linear 1.0 yalign 0.0
    yalign 1.0
    linear 1.0 yalign 0.0
    yalign 1.0
    linear 1.0 yalign 0.0

image red_static_scroll:
    "Phone UI/red_static_scroll.webp"
    subpixel True
    yalign 0.0
    linear 1.5 yalign 1.0
    yalign 0.0
    linear 1.5 yalign 1.0

image red_static_reverse:
    "Phone UI/red_static_scroll.webp"
    subpixel True
    yalign 1.0
    linear 1.5 yalign 0.0
    yalign 1.0
    linear 1.5 yalign 0.0

image red_static_background = Fixed(
    Transform("center_bg:Phone UI/bg_red_static.webp", zoom=1.19, align=(0.5, 0.5)),
    "Phone UI/red_static_scroll.webp",
    xysize=(config.screen_width,1334)
)

image screen_crack = "center_bg:Phone UI/screen_crack.webp"

image banner annoy:
    "Banners/Annoy/annoy_0.webp"
    0.12
    "Banners/Annoy/annoy_1.webp"
    0.12
    "Banners/Annoy/annoy_2.webp"
    0.12
    "Banners/Annoy/annoy_3.webp"
    0.12
    "Banners/Annoy/annoy_4.webp"
    0.12
    "Banners/Annoy/annoy_5.webp"
    0.12

image banner heart:
    "Banners/Heart/heart_0.webp"
    0.12
    "Banners/Heart/heart_1.webp"
    0.12
    "Banners/Heart/heart_2.webp"
    0.12
    "Banners/Heart/heart_3.webp"
    0.12
    "Banners/Heart/heart_4.webp"
    0.12
    "Banners/Heart/heart_5.webp"
    0.12

image banner lightning:
    "Banners/Lightning/lightning_0.webp"
    0.12
    "Banners/Lightning/lightning_1.webp"
    0.12
    "Banners/Lightning/lightning_2.webp"
    0.12
    "Banners/Lightning/lightning_3.webp"
    0.12
    "Banners/Lightning/lightning_4.webp"
    0.12
    "Banners/Lightning/lightning_5.webp"
    0.12

image banner well:
    "Banners/Well/well_0.webp"
    0.12
    "Banners/Well/well_1.webp"
    0.12
    "Banners/Well/well_2.webp"
    0.12
    "Banners/Well/well_3.webp"
    0.12
    "Banners/Well/well_4.webp"
    0.12
    "Banners/Well/well_5.webp"
    0.12