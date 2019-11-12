default current_background = "morning"

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
        
image pausebutton:
    "pause_sign" with Dissolve(0.5, alpha=True)
    1.0
    "transparent_img" with Dissolve(0.5, alpha=True)
    1.0
    repeat
    

image fast_slow_button = "Phone UI/fast-slow-transparent.png"
image maxSpeed = Transform("Phone UI/max_speed_active.png", zoom=1.1)
image noMaxSpeed = Transform("Phone UI/max_speed_inactive.png", zoom=1.1)
image speed_txt = ParameterizedText(style = "speednum_style")
image close_button = "CGs/close-overlay.png"

image save_exit = "Phone UI/Save&Exit.png"  
image signature = "Phone UI/signature01.png"
image heart_hg = "Phone UI/heart-hg-sign.png"

## Custom Chat Footers
image custom_answerbutton:
    block:
        "custom_answer_reg" with Dissolve(1.0, alpha=True)
        1.3
        "custom_answer_dark" with Dissolve(1.0, alpha=True)
        1.0
        repeat
        
image custom_pause = "Phone UI/custom-pause.png"
image custom_play = "Phone UI/custom-play.png"
image custom_save_exit = "Phone UI/custom-save-exit.png"
image custom_pausebutton:
    "custom_pause_sign" with Dissolve(0.5, alpha=True)
    1.0
    "transparent_img" with Dissolve(0.5, alpha=True)
    1.0
    repeat
image custom_pause_square = "Phone UI/custom-pause-square.png"
## End custom chat footers

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