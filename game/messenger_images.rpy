## ********************************
## Chatroom Images
## ********************************


image answerbutton: 
    block:
        "answer_dark" with Dissolve(0.5, alpha=True)
        1.0
        "answer_reg" with Dissolve(0.5, alpha=True)
        1.0
        repeat
        
image custom_answerbutton:
    block:
        "custom_answer_reg" with Dissolve(1.0, alpha=True)
        1.3
        "custom_answer_dark" with Dissolve(1.0, alpha=True)
        1.0
        repeat

image darklight_continue_button:
    block:
        "Phone UI/Continue-light.png" with Dissolve(1.0, alpha=True)
        1.3
        "Phone UI/Continue-dark.png" with Dissolve(1.0, alpha=True)
        1.0
        repeat

image custom_darklight_continue_button:
    block:
        "Phone UI/custom-continue-light.png" with Dissolve(1.0, alpha=True)
        1.3
        "Phone UI/custom-continue-dark.png" with Dissolve(1.0, alpha=True)
        1.0
        repeat


image phone_continue_button = ConditionSwitch(
    "persistent.custom_footers", "Phone UI/custom-continue.png",
    "True", "Phone UI/Continue.png"
)

# This is the actual button that's pressed; the program
# performs better having a transparent button vs an animated one
image transparent_answer = "Phone UI/answer_transparent.png"

image pausebutton:
    "pause_sign" with Dissolve(0.5, alpha=True)
    1.0
    "transparent_img" with Dissolve(0.5, alpha=True)
    1.0
    repeat
    
image custom_pausebutton:
    "custom_pause_sign" with Dissolve(0.5, alpha=True)
    1.0
    "transparent_img" with Dissolve(0.5, alpha=True)
    1.0
    repeat

image pause_square = ConditionSwitch(
    "persistent.custom_footers", "Phone UI/custom-pause-square.png",
    "True", "Phone UI/pause_square.png"
)

image phone_pause = ConditionSwitch(
    "persistent.custom_footers", "Phone UI/custom-pause.png",
    "True", "Phone UI/Pause.png"
)

image phone_play = ConditionSwitch(
    "persistent.custom_footers", "Phone UI/custom-play.png",
    "True", "Phone UI/Play.png"
)

image save_exit = ConditionSwitch(
    "persistent.custom_footers", "Phone UI/custom-save-exit.png",
    "True", "Phone UI/Save&Exit.png"
)



image fast_slow_button = "Phone UI/fast-slow-transparent.png"
image maxSpeed = Transform("Phone UI/max_speed_active.png", zoom=1.1)
image noMaxSpeed = Transform("Phone UI/max_speed_inactive.png", zoom=1.1)
image speed_txt = ParameterizedText(style="speednum_style")
image close_button = Transform(Solid("#00000066"), size=(750,99))


image signature = ConditionSwitch(
    "persistent.custom_footers", "Phone UI/signature01-dark.png",
    "True", "Phone UI/signature01.png"
)
image heart_sign = "Phone UI/heart-sign.png"
image hg_sign = "Phone UI/hg-sign.png"

image answer_dark = "Phone UI/Answer-Dark.png"
image answer_reg = "Phone UI/Answer.png"
image pause_sign = "Phone UI/pause_sign.png"

image custom_answer_dark = "Phone UI/custom-answer.png"
image custom_answer_reg = "Phone UI/custom-answer-dark.png"
image custom_pause_sign = "Phone UI/custom-pause-sign.png"

image phone_ui = ConditionSwitch(
    "persistent.custom_footers", "Phone UI/Phone-UI.png",
    "True", "Phone UI/Phone-UI-old.png"
)

image max_speed_active = "Phone UI/max_speed_active.png"
image max_speed_inactive = "Phone UI/max_speed_inactive.png"
image back_arrow_btn = ConditionSwitch(
    "persistent.custom_footers", "Phone UI/back-arrow.png",
    "True", "menu_back"
)

image choice_darken = Solid("#0000006e")
image save_trash = "Menu Screens/Main Menu/save_trash_hover.png"

image sign_btn = ConditionSwitch(
    "persistent.custom_footers", "Phone UI/sign-button-dark.png",
    "True", "Phone UI/sign-button.png"
)
image sign_btn_clicked = ConditionSwitch(
    "persistent.custom_footers", "Phone UI/sign-button-clicked-dark.png",
    "True", "Phone UI/sign-button-clicked.png"
)

image battery_high = "Phone UI/battery_high.png"
image battery_med = "Phone UI/battery_med.png"
image battery_low = "Phone UI/battery_low.png"
image battery_empty_img = "Phone UI/battery_empty.png"
image battery_charged = "Phone UI/battery_charged.png"
image battery_charging = "Phone UI/battery_charging.png"

image skip_intro_idle = "Phone UI/skip_intro_available.png"
image skip_intro_hover = "Phone UI/skip_intro_pressed.png"

image hack scroll: 
    "hack_long"
    subpixel True
    yalign 0.0
    linear 1.0 yalign 1.0
    yalign 0.0
    linear 1.0 yalign 1.0
    yalign 0.0
    linear 1.0 yalign 1.0
    
image redhack scroll:
    "red_hack_long"
    subpixel True
    yalign 0.0
    linear 1.0 yalign 1.0
    yalign 0.0
    linear 1.0 yalign 1.0
    yalign 0.0
    linear 1.0 yalign 1.0
    
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