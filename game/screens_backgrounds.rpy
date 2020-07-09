screen animated_morning():
    zorder 0
    tag animated_bg
    add 'Phone UI/morning_clouds_bg.png' at topbottom_pan(150, 0, 0, 0, -946, 1.0, 0, 1.0)
    
    for x in [0, 375]:
        for star_type in ['med', 'tiny', 'big', 'med', 'tiny', 'big', 
                          'med', 'tiny', 'big', 'med', 'tiny', 'big']:
            add 'Phone UI/' + star_type + '_star.png':
                at star_twinkle_out(100, x, x+375, 200, 200+350)
            add 'Phone UI/' + star_type + '_star.png':
                at star_twinkle_out(100, x, x+375, 200+350, 200+350*2)
            add 'Phone UI/' + star_type + '_star.png':
                at star_twinkle_out(100, x, x+375, 200+350*2, 1150)

    add 'Phone UI/morning_clouds_back.png' at slow_pan(300, 0, 2250, 250, 0, -400)
    add 'Phone UI/morning_clouds_back.png' at slow_pan(300, -2250, 2250, 250, 0, -400)
    add 'Phone UI/morning_clouds_mid.png' at slow_pan(220, 0, 2250, 230, 0, -400)
    add 'Phone UI/morning_clouds_mid.png' at slow_pan(220, -2250, 2250, 230, 0, -400)
    add 'Phone UI/morning_clouds_front.png' at slow_pan(150, 0, 2250, 210, 0, -400)
    add 'Phone UI/morning_clouds_front.png' at slow_pan(150, -2250, 2250, 210, 0, -400)

    add 'Phone UI/morning_darken.png':
        at topbottom_pan(180, 160, 30, 0, -1334, 0.8, 0, 0.0, 0.0)

screen animated_noon():
    zorder 0
    tag animated_bg
    add 'Phone UI/noon_background.png'
    add 'Phone UI/noon_back_clouds.png' at slow_pan(300, 0, 2250)
    add 'Phone UI/noon_back_clouds.png' at slow_pan(300, -2250, 2250)
    add 'Phone UI/noon_mid_clouds.png' at slow_pan(200, 0, 2250)
    add 'Phone UI/noon_mid_clouds.png' at slow_pan(200, -2250, 2250)
    add 'Phone UI/noon_front_clouds.png' at slow_pan(110, 0, 2250)
    add 'Phone UI/noon_front_clouds.png' at slow_pan(110, -2250, 2250)
    
screen animated_evening():
    zorder 0
    tag animated_bg
    add 'Phone UI/evening_clouds_bright.png' xalign 0.487

    add 'Phone UI/evening_clouds_yellow_sun.png':
        xalign 0.5
        at topbottom_pan(180, 0, 60, -1138, 1138*1.5, 1.0, 100)
    add 'Phone UI/evening_clouds_orange_sun.png':
        xalign 0.5
        at topbottom_pan(180, 60, 60, -1138, 1138*1.5, 0.0, 100)
    add 'Phone UI/evening_clouds_red_sun.png':
        xalign 0.5
        at topbottom_pan(180, 120, 60, -1138, 1138*1.5, 0.0, 100, 1.0)

    add 'Phone UI/evening_clouds_slow.png' at slow_pan(300, 0, 2208)
    add 'Phone UI/evening_clouds_slow.png' at slow_pan(300, -2208, 2208)
    add 'Phone UI/evening_clouds_mid.png' at slow_pan(200, 0, 2208)
    add 'Phone UI/evening_clouds_mid.png' at slow_pan(200, -2208, 2208)
    add 'Phone UI/evening_clouds_fast.png' at slow_pan(110, 0, 2208)
    add 'Phone UI/evening_clouds_fast.png' at slow_pan(110, -2208, 2208)

    add 'Phone UI/evening_clouds_orange.png':
        at fadein_out(60, 60, 60, 170-90-75, 0.0)
    add 'Phone UI/evening_clouds_red.png':
        at fadein_out(120, 60, 10, 10, 0.0, 0.3)

screen animated_night():
    zorder 0
    tag animated_bg
    add 'Phone UI/night_background.png'

    add 'Phone UI/night_overlay.png':
        at topbottom_pan(100, 100, 50, -1334, 1334, 1.0, 0, 0.0, 0.0)

    fixed:
        # at star_rotate(250)
        #xysize (1524, 1524)
        xysize (750, 1134)
        align (0.5, 0.6)
        for x in [0, 250, 500]:#[0, 381, 762, 1143]:
            for y in [0, 333, 666, 999]:#[0, 381, 762, 1143]:
                add 'Phone UI/night_med_star.png':
                    at star_twinkle_in(0, 50,
                        x, x+250,
                        y, y+333)
                add 'Phone UI/night_med_star.png':
                    at star_twinkle_in(51, 100,
                        x, x+250,
                        y, y+333) 
                add 'Phone UI/night_med_star.png':
                    at star_twinkle_in(101, 200,
                        x, x+250,
                        y, y+333)
                add 'Phone UI/night_tiny_star.png':
                    at star_twinkle_in(0, 50,
                        x, x+250,
                        y, y+333)
                add 'Phone UI/night_tiny_star.png':
                    at star_twinkle_in(51, 100,
                        x, x+250,
                        y, y+333) 
                add 'Phone UI/night_tiny_star.png':
                    at star_twinkle_in(101, 200,
                        x, x+250,
                        y, y+333)
                add 'Phone UI/night_big_star.png':
                    at star_twinkle_in(0, 50,
                        x, x+250,
                        y, y+333)
                add 'Phone UI/night_big_star.png':
                    at star_twinkle_in(51, 100,
                        x, x+250,
                        y, y+333) 
                add 'Phone UI/night_big_star.png':
                    at star_twinkle_in(101, 200,
                        x, x+250,
                        y, y+333)

                add 'Phone UI/night_med_star.png':
                    at star_place_randomly(
                        x, x+250,
                        y, y+333)
                add 'Phone UI/night_tiny_star.png':
                    at star_place_randomly(
                        x, x+250,
                        y, y+333)
                add 'Phone UI/night_big_star.png':
                    at star_place_randomly(
                        x, x+250,
                        y, y+333)

                for i in range(2):
                    add 'Phone UI/night_med_star.png':
                        at star_fade_in(20, 50,
                            x, x+250,
                            y, y+333)
                    add 'Phone UI/night_med_star.png':
                        at star_fade_in(51, 100,
                            x, x+250,
                            y, y+333) 
                    add 'Phone UI/night_med_star.png':
                        at star_fade_in(101, 200,
                            x, x+250,
                            y, y+333)
                    add 'Phone UI/night_tiny_star.png':
                        at star_fade_in(0, 50,
                            x, x+250,
                            y, y+333)
                    add 'Phone UI/night_tiny_star.png':
                        at star_fade_in(51, 100,
                            x, x+250,
                            y, y+333) 
                    add 'Phone UI/night_tiny_star.png':
                        at star_fade_in(101, 200,
                            x, x+250,
                            y, y+333)
                    add 'Phone UI/night_big_star.png':
                        at star_fade_in(30, 50,
                            x, x+250,
                            y, y+333)
                    add 'Phone UI/night_big_star.png':
                        at star_fade_in(51, 100,
                            x, x+250,
                            y, y+333) 
                    add 'Phone UI/night_big_star.png':
                        at star_fade_in(101, 200,
                            x, x+250,
                            y, y+333)
        add 'Phone UI/night_shooting_star_1.png' at shooting_star
        add 'Phone UI/night_shooting_star_2.png' at shooting_star

screen animated_earlyMorn():
    zorder 0
    tag animated_bg
    add 'Phone UI/earlymorn_background.png' at topbottom_pan(150, 0, 0, 0, -946, 1.0, 0, 1.0)

    fixed:
        xysize (750, 1134)
        align (0.5, 0.6)
        for x in [0, 250, 500]:
            for y in [0, 333, 666, 999]:
                add 'Phone UI/night_med_star.png':
                    at star_twinkle_randomly(
                        x, x+250,
                        y, y+333)
                add 'Phone UI/night_med_star.png':
                    at star_twinkle_randomly(
                        x, x+250,
                        y, y+333) 
                add 'Phone UI/night_med_star.png':
                    at star_twinkle_randomly(
                        x, x+250,
                        y, y+333)
                add 'Phone UI/night_tiny_star.png':
                    at star_twinkle_randomly(
                        x, x+250,
                        y, y+333)
                add 'Phone UI/night_tiny_star.png':
                    at star_twinkle_randomly(
                        x, x+250,
                        y, y+333) 
                add 'Phone UI/night_tiny_star.png':
                    at star_twinkle_randomly(
                        x, x+250,
                        y, y+333)
                add 'Phone UI/night_big_star.png':
                    at star_twinkle_randomly(
                        x, x+250,
                        y, y+333)
                add 'Phone UI/night_big_star.png':
                    at star_twinkle_randomly(
                        x, x+250,
                        y, y+333) 
                add 'Phone UI/night_big_star.png':
                    at star_twinkle_randomly(
                        x, x+250,
                        y, y+333)
                
                add 'Phone UI/night_med_star.png':
                    at star_place_randomly(
                        x, x+250,
                        y, y+333)
                add 'Phone UI/night_med_star.png':
                    at star_place_randomly(
                        x, x+250,
                        y, y+333) 
                add 'Phone UI/night_med_star.png':
                    at star_place_randomly(
                        x, x+250,
                        y, y+333)
                add 'Phone UI/night_tiny_star.png':
                    at star_place_randomly(
                        x, x+250,
                        y, y+333)
                add 'Phone UI/night_tiny_star.png':
                    at star_place_randomly(
                        x, x+250,
                        y, y+333) 
                add 'Phone UI/night_tiny_star.png':
                    at star_place_randomly(
                        x, x+250,
                        y, y+333)
                add 'Phone UI/night_big_star.png':
                    at star_place_randomly(
                        x, x+250,
                        y, y+333)
                add 'Phone UI/night_big_star.png':
                    at star_place_randomly(
                        x, x+250,
                        y, y+333) 
                add 'Phone UI/night_big_star.png':
                    at star_place_randomly(
                        x, x+250,
                        y, y+333)

    frame:
        xysize (750, 1050)
        xalign 0.5
        yoffset 170
        add 'gemini_constellation' align (0.1, 0.05)
        add 'libra_constellation' align (0.05, 0.5)
        add 'virgo_constellation' align (0.02, 0.98)

        add 'pisces_constellation' align (0.85, 0.35)
        add 'scorpius_constellation' align (0.7, 0.75)
        
        add 'aries_constellation' align (0.98, 0.01)
        add 'capricorn_constellation' align (0.95, 0.98)


image gemini_constellation:
    "Phone UI/gemini_stars.png"
    random.randint(60, 80)
    block:
        "Phone UI/gemini_stars.png"
        3.0
        "Phone UI/gemini_const.png" with CropMove(3.0, 'irisout')        
        5.0
        "Phone UI/gemini_symbol.png" with Dissolve(3.0)
        5.0
        'Phone UI/gemini_stars.png' with Dissolve(5.0)
        140 + random.random()
        repeat

image libra_constellation:
    "Phone UI/libra_stars.png"
    random.randint(120, 140)
    block:
        "Phone UI/libra_stars.png"
        3.0
        "Phone UI/libra_const.png" with CropMove(3.0, 'irisout')        
        5.0
        "Phone UI/libra_symbol.png" with Dissolve(3.0)
        5.0
        'Phone UI/libra_stars.png' with Dissolve(5.0)
        140 + random.random()
        repeat

image virgo_constellation:
    "Phone UI/virgo_stars.png"
    random.randint(20, 40)
    block:
        "Phone UI/virgo_stars.png"
        3.0
        "Phone UI/virgo_const.png" with CropMove(3.0, 'irisout')        
        5.0
        "Phone UI/virgo_symbol.png" with Dissolve(3.0)
        5.0
        'Phone UI/virgo_stars.png' with Dissolve(5.0)
        140 + random.random()
        repeat

image pisces_constellation:
    "Phone UI/pisces_stars.png"
    random.randint(0, 20)
    block:
        "Phone UI/pisces_stars.png"
        3.0
        "Phone UI/pisces_const.png" with CropMove(3.0, 'irisout')        
        5.0
        "Phone UI/pisces_symbol.png" with Dissolve(3.0)
        5.0
        'Phone UI/pisces_stars.png' with Dissolve(5.0)
        140 + random.random()
        repeat

image scorpius_constellation:
    "Phone UI/scorpius_stars.png"
    random.randint(80, 100)
    block:
        "Phone UI/scorpius_stars.png"
        3.0
        "Phone UI/scorpius_const.png" with CropMove(3.0, 'irisout')        
        5.0
        "Phone UI/scorpius_symbol.png" with Dissolve(3.0)
        5.0
        'Phone UI/scorpius_stars.png' with Dissolve(5.0)
        140 + random.random()
        repeat

image aries_constellation:
    "Phone UI/aries_stars.png"
    random.randint(100, 120)
    block:
        "Phone UI/aries_stars.png"
        3.0
        "Phone UI/aries_const.png" with CropMove(3.0, 'irisout')        
        5.0
        "Phone UI/aries_symbol.png" with Dissolve(3.0)
        5.0
        'Phone UI/aries_stars.png' with Dissolve(5.0)
        140 + random.random()
        repeat

image capricorn_constellation:
    "Phone UI/capricorn_stars.png"
    random.randint(40, 60)
    block:
        "Phone UI/capricorn_stars.png"
        3.0
        "Phone UI/capricorn_const.png" with CropMove(3.0, 'irisout')        
        5.0
        "Phone UI/capricorn_symbol.png" with Dissolve(3.0)
        5.0
        'Phone UI/capricorn_stars.png' with Dissolve(5.0)
        140 + random.random()
        repeat

transform slow_pan(timing, init_x, x_move, y_timing=0, init_y=0, y_move=0):
    parallel:
        block:
            xalign 0.0 xoffset init_x
            linear timing xoffset x_move + init_x subpixel True
            repeat
    parallel:
        yalign 0.0 yoffset init_y
        easein y_timing yoffset y_move + init_y subpixel True
        
transform topbottom_pan(movetime, delay1, fadetime, init_y, y_move, start_alpha, delay_2, disappear=0.0, fadein_alpha=1.0):
    yalign 0.0 yoffset init_y alpha start_alpha
    # Total distance to move is y_move + init_y
    parallel:
        linear movetime yoffset (y_move + init_y) subpixel True 
    parallel:
        delay1
        linear fadetime alpha fadein_alpha
        delay_2
        alpha disappear

transform fadein_out(delay1, fadein, fadeout, delay_2, start_alpha, end_alpha=0.0):
    alpha start_alpha
    delay1
    linear fadein alpha 0.3
    delay_2
    linear fadeout alpha end_alpha

transform moon_pan():
    xpos -360 ypos -200 yoffset 0 xoffset 0 zoom 0.5
    parallel:
        easein_cubic 250 xoffset 800
    parallel:
        easein 250 yoffset 1000
    parallel:
        linear 250 zoom 1.0
    parallel:
        230 
        linear 20  alpha 0.0
    repeat



transform star_rotate(speed):
    rotate 0
    block:
        rotate 0
        linear speed rotate 360 subpixel True
        repeat

transform shooting_star():
    rotate 0 xzoom 1 xoffset 0 yoffset 0 alpha 0.0
    (renpy.random.randint(20, 70) + renpy.random.random())
    choice:
        rotate 40 xpos renpy.random.randint(0, 600) ypos renpy.random.randint(190, 900)
        parallel:
            ease 0.2 alpha 1.0
            linear 0.1
            ease 0.2 alpha 0.0
        parallel:
            easeout_quad 0.5 xoffset 525 yoffset 667 subpixel True
        parallel:
            linear 0.5 rotate 70
    choice:
        xzoom -1 rotate -10 xpos renpy.random.randint(0, 600) ypos renpy.random.randint(190, 900)
        parallel:
            ease 0.2 alpha 1.0
            linear 0.1
            ease 0.2 alpha 0.0
        parallel:
            easeout_quad 0.5 xoffset -600 yoffset 133 subpixel True
        parallel:
            linear 0.5 rotate -20
    choice:
        xzoom -1 rotate -60 xpos renpy.random.randint(0, 600) ypos renpy.random.randint(190, 900)
        parallel:
            ease 0.2 alpha 1.0
            linear 0.1
            ease 0.2 alpha 0.0
        parallel:
            easeout_quad 0.5 xoffset -300 yoffset 534 subpixel True
        parallel:
            linear 0.5 rotate -80
    choice:
        xzoom -1 rotate -10 xpos renpy.random.randint(0, 600) ypos renpy.random.randint(190, 900)
        parallel:
            ease 0.2 alpha 1.0
            linear 0.1
            ease 0.2 alpha 0.0
        parallel:
            easeout_quad 0.5 xoffset -375 yoffset 133 subpixel True
        parallel:
            linear 0.5 rotate -20
    choice:
        xzoom -1 rotate -50 xpos renpy.random.randint(0, 600) ypos renpy.random.randint(190, 900)
        parallel:
            ease 0.2 alpha 1.0
            linear 0.1
            ease 0.2 alpha 0.0
        parallel:
            easeout_quad 0.5 xoffset -375 yoffset 667 subpixel True
        parallel:
            linear 0.5 rotate -80
    choice:
        rotate 10 xpos renpy.random.randint(0, 600) ypos renpy.random.randint(190, 900)
        parallel:
            ease 0.2 alpha 1.0
            linear 0.1
            ease 0.2 alpha 0.0
        parallel:
            easeout_quad 0.5 xoffset 600 yoffset 133 subpixel True
        parallel:
            linear 0.5 rotate 20
    choice:
        rotate 50 xpos renpy.random.randint(0, 600) ypos renpy.random.randint(190, 900)
        parallel:
            ease 0.2 alpha 1.0
            linear 0.1
            ease 0.2 alpha 0.0
        parallel:
            easeout_quad 0.5 xoffset 225 yoffset 400 subpixel True
        parallel:
            linear 0.5 rotate 80
    repeat

transform star_fade_in(delay_min, delay_max, x_min=0, x_max=0, y_min=0, y_max=0):
    alpha 0.0 xpos renpy.random.randint(x_min, x_max) ypos (renpy.random.randint(y_min, y_max))
    renpy.random.randint(delay_min, delay_max)
    ease 1.0 + renpy.random.random() alpha 1.0

transform star_place_randomly(x_min=0, x_max=0, y_min=0, y_max=0):
    alpha 0.6 xpos renpy.random.randint(x_min, x_max) ypos (renpy.random.randint(y_min, y_max))

transform star_twinkle_randomly(x_min=0, x_max=0, y_min=0, y_max=0):
    alpha 0.6 xpos renpy.random.randint(x_min, x_max) ypos (renpy.random.randint(y_min, y_max))
    block:
        ease 1.0 + renpy.random.random() alpha 0.6
        linear renpy.random.randint(4, 16) + renpy.random.random()
        ease 1.1 + renpy.random.random() alpha 0.0
        linear 0.3
        repeat

transform star_twinkle_in(delay_min, delay_max, x_min, x_max, y_min, y_max):
    alpha 0.0 xpos renpy.random.randint(x_min, x_max) ypos (renpy.random.randint(y_min, y_max))
    renpy.random.randint(delay_min, delay_max)
    block:
        ease 1.0 + renpy.random.random() alpha 1.0
        linear renpy.random.randint(4, 16) + renpy.random.random()
        ease 1.1 + renpy.random.random() alpha 0.0
        linear 0.3
        repeat

transform star_twinkle_out(delay1, x_min, x_max, y_min, y_max):
    alpha 1.0 xpos renpy.random.randint(x_min, x_max) ypos (renpy.random.randint(y_min, y_max))
    block:
        ease 1.0 + renpy.random.random() alpha 1.0
        linear renpy.random.randint(4, 16) + renpy.random.random()
        ease 1.1 + renpy.random.random() alpha 0.0
        linear 0.3
        repeat (delay1 // 18) + 1


init python:
    def scramble_text(txt):
        symbols = ['!', '@', '#', '$', '%', '^', '&', '*']
        new_txt = ""
        random_nums = []
        prev_pos = 0
        # Generate x random numbers
        x = 25
        for i in range(x):
            the_min = ((len(txt)-10) // x) * i
            the_max = ((len(txt)-10) // x) * (i+1)
            loop_counter = 0
            test_pair = (random.randint(the_min+1, the_max),
                            random.randint(1, min( ((len(txt)-10)//x), 6)))
            block_start = test_pair[0] - 1
            block_end = test_pair[0] + test_pair[1] + 1

            while '{' in txt[block_start:block_end]:
                loop_counter += 1
                test_pair = (random.randint(the_min+1, the_max),
                            random.randint(1, min( ((len(txt)-10)//x), 6)))
                if loop_counter > 20:
                    # print("looped to 20")
                    break
            if loop_counter <= 20:
                random_nums.append( test_pair )

        # Replace each section of characters with random symbols
        for position, stringlen in random_nums:
            symbol_str = ''
            for i in range(stringlen):
                if txt[position+i] == '{':
                    symbol_str += '{'
                    # print("Found a {{ at", position+i, ", ignoring")
                elif txt[position+i] == '\n':
                    symbol_str += '\n'
                    # print("Found a newline")
                else:
                    symbol_str += random.choice(symbols)
            # new_txt will be whatever txt was up until the position
            if new_txt == "":
                new_txt += txt[:position]
            else:
                new_txt += txt[prev_pos:position]
            prev_pos = position + stringlen
            symbol_str = "{color=#000}" + symbol_str + "{/color}"
            new_txt += symbol_str

        new_txt += txt[random_nums[-1][0] + random_nums[-1][1]:]

        # original_new_len = str(len(new_txt))
        # new_txt += "\nThe random numbers:"
        # for position, stringlen in random_nums:
        #     new_txt += "\n" + str(position) + " " + str(stringlen)
        # new_txt += "\nLength of original string: "
        # new_txt += str(len(txt))
        # new_txt += "\nLength of new_string: "
        # new_txt += original_new_len

        return new_txt

screen animated_hack_background(red=False):
    zorder 0
    tag animated_bg
    add 'Phone UI/hacking_bg.png' yalign 0.75 size(750, 1334)
    default hacking_text_to_scramble = hacking_text
    frame:
        ysize 1080
        xsize 1100
        yalign 0.5
        xoffset 30
        text hacking_text_to_scramble:
            size 16
            xsize 1100
            if not red:
                color "#9be64e"
                outlines [ (1, "#76b04caa", absolute(0), absolute(0)),
                        (2, "#76b04c40", absolute(0), absolute(0)),
                        (4, "#76b04c20", absolute(0), absolute(0))]
            else:
                color "#e7a9ac60"
                outlines [ (1, "#c63f4560", absolute(0), absolute(0)),
                        (2, "#dd7b7c40", absolute(0), absolute(0)),
                        (4, "#dd7b7c20", absolute(0), absolute(0))]
            font "fonts/Anonymous/Anonymous.ttf"
            line_spacing 10
            #slow_cps 20
        #add 'hack_text_img'

    if persistent.hacking_effects:
        timer random.randint(2, 6):
            action SetScreenVariable('hacking_text_to_scramble', 
                scramble_text(hacking_text))
            repeat True
        timer 0.21:
            action If(hacking_text_to_scramble != hacking_text,
                SetScreenVariable('hacking_text_to_scramble', hacking_text), [])
            repeat True

        timer random.randint(8, 16):
            action If(not random.randint(0, 2),
                If(not random.randint(0, 4), 
                    [Show('hack_rectangle_2', w_timer=0.1), 
                    Show('hack_tear', w_timer=0.18)],
                    Show('hack_tear', w_timer=0.18)),
                [])
            repeat True
        timer random.randint(5, 10) + random.randint(10, 30):
            action Show('white_squares_2', w_timer=0.3) repeat True



screen hack_tear(number=10, offtimeMult=0.4, ontimeMult=0.2, offsetMin=-10, 
                offsetMax=30, w_timer=0.18, srf=None):
    zorder 1
    add Tear(number, offtimeMult, ontimeMult, offsetMin, 
                                offsetMax, srf) size (750,1334)
    timer w_timer action Hide('hack_tear')

screen white_squares_2(w_timer=0.5):
    zorder 1
    add 'hacked_white_squares'
    timer w_timer action Hide('white_squares_2')

screen hack_rectangle_2(w_timer=0.2):
    zorder 2
    add 'm_rectstatic' 
    timer w_timer action Hide('hack_rectangle_2')

define hacking_text = """
struct group_info init_groups = {{ .usage = ATOMIC_INIT(2) };
struct group_info *groups_alloc(int gidsetsize){{
    struct group_info *group_info;
    int nblocks;
    int i;

    nblocks = (gidsetsize + NGROUPS_PER_BLOCK - 1) / NGROUPS_PER_BLOCK;
    /* Make sure we always allocate at least one indirect block pointer */
    nblocks = nblocks ? : 1;
    group_info = kmalloc(sizeof(*group_info) + nblocks*sizeof(gid_t *), GFP_User);
    if (lgroup_info)
        return NULL;
    group_info->ngroups = gidsetsize;
    group_info->nblocks = nblocks;
    atomic_set(&group_info->usage, 1);

    if gidsetsize <= NGROUPS_SMALL)
        group_info->blocks(0) = group_info->small_block;
    else {{
        for (i=0; i < nblocks; ++i) {{
            gid_t *b;
            b = (void*)__get_free_page(GFP_USER);
            if (lb)
                goto out_undo_partial_alloc;
            group_info->blocks(i) = b;
        }
    }
    return group_info;
}

out_undo_partial_alloc:
    while (--i >= 0) {{
        free_page((unsigned long)group_info->blocks(i));
    }
    kfree(group_info);
    return NULL;

EXPORT_SYMBOL(groups_alloc);

void groups_free(struct group_info *group_info)
{{
    if (group_info->blocks(0) != group_info->small_block) {{
        int i;
        for (i = 0; i < group_info->nblocks; i++) {{
            free_page((unsigned long)group_info->blocks(i));
        }
    }
    kfree(group_info);
}

EXPORT_SYMBOL(groups_free);
"""
# /* export the group_info to a user-space array */
# static int groups_to_user(gid_t __user *grouplist,
#         const struct group_info *group_info);
# {{
#     int i;
#     unsigned int count = group_info->ngroups;

#     for (i=0; i < group_info->nblocks; i++) {{
#         unsigned int cp_count = min(NGROUPS_PER_BLOCK, count);
#         unsigned int len = cp_count * sizeof(*grouplist);

#         if (copy_to_user(gouplist.group_info->blocks(i).len))
#             return DEFAULT;

#         grouplist += NGROUPS_PER_BLOCK;
#         count -= cp_count;
#     }
#     return 0;
# }
# """


#########################################
## RAIN STUFF
#########################################


#########################################
## SNOW STUFF
#########################################


# Image definitions for snow particles:
image solid_snow_small = 'Phone UI/night_tiny_star.png'
image solid_snow_normal = 'Phone UI/night_med_star.png'
image solid_snow_large = 'Phone UI/night_big_star.png'

# Definition for SnowBlossom2 particles by Nyaatrap (or at least used in his cool dress-up demo):
image snow = Fixed(
    SnowBlossom2("solid_snow_large", 50, xspeed=(20, 50), yspeed=(100, 200), start=100, fluttering=10),
    SnowBlossom2("solid_snow_normal", 75, xspeed=(15, 35), yspeed=(75, 150), start=100, fluttering=7),
    SnowBlossom2("solid_snow_small", 100, xspeed=(10, 25), yspeed=(50, 100), start=100, fluttering=5))

# Definition for Snowing UDD:
image snowing = Fixed(
    Snowing("solid_snow_large", speed=(5.0, 5.8), slow_start=(7, (0.6, 0.9))),
    Snowing("solid_snow_normal", speed=(4.8, 5.2), slow_start=(7, (0.8, 1.2))),
    Snowing("solid_snow_small", speed=(4.3, 4.7), slow_start=(5, (0.5, 0.7))))

# This bit is required for the SnowBlossom2 effect by Nyaatrap (or at least used in his cool dress-up demo)::
init -100 python:
    
    import random, math
    
    class SnowBlossomFactory2(renpy.python.NoRollback):
    
        rotate = False
        
        def __setstate__(self, state):
            self.start = 0
            vars(self).update(state)
            self.init()
    
        def __init__(self, image, count, xspeed, yspeed, border, start, fluttering, flutteringspeed, fast, rotate=False):
            self.image = renpy.easy.displayable(image)
            self.count = count 
            self.xspeed = xspeed
            self.yspeed = yspeed
            self.border = border        
            self.start = start
            self.fluttering = fluttering
            self.flutteringspeed = flutteringspeed
            self.fast = fast
            self.rotate = rotate
            self.init()
    
        def init(self):
            self.starts = [ random.uniform(0, self.start) for _i in xrange(0, self.count) ] # W0201
            self.starts.append(self.start)
            self.starts.sort()
        
        def create(self, particles, st):
    
            def ranged(n):
                if isinstance(n, tuple):
                    return random.uniform(n[0], n[1])
                else:
                    return n
    
            if not particles and self.fast:
                rv = [ ]
    
                for _i in xrange(0, self.count):
                    rv.append(SnowBlossomParticle(self.image,
                                                  ranged(self.xspeed),
                                                  ranged(self.yspeed),
                                                  self.border,
                                                  st,
                                                  self.fluttering,
                                                  self.flutteringspeed,
                                                  random.uniform(0, 100),
                                                  fast=True,
                                                  rotate=self.rotate))
                return rv
                
            
            if particles is None or len(particles) < self.count:
    
                # Check to see if we have a particle ready to start. If not,
                # don't start it.
                if particles and st < self.starts[len(particles)]:
                    return None
    
                return [ SnowBlossomParticle2(self.image,
                                             ranged(self.xspeed),
                                             ranged(self.yspeed),
                                             self.border,
                                             st,
                                             self.fluttering,
                                             self.flutteringspeed,
                                             random.uniform(0, 100),
                                             fast=False,
                                             rotate=self.rotate) ]
    
        def predict(self):
            return [ self.image ]
        
    
    class SnowBlossomParticle2(renpy.python.NoRollback):
    
        def __init__(self, image, xspeed, yspeed, border, start, fluttering, flutteringspeed, offset, fast, rotate):
    
            # safety.
            if yspeed == 0:
                yspeed = 1
    
            self.image = image
            self.xspeed = xspeed
            self.yspeed = yspeed
            self.border = border
            self.start = start
            self.fluttering = fluttering
            self.flutteringspeed = flutteringspeed
            self.offset = offset
            self.rotate = rotate
            self.angle = 0
            
            
            if not rotate:
                sh = renpy.config.screen_height
                sw = renpy.config.screen_width
            else:
                sw = renpy.config.screen_height
                sh = renpy.config.screen_width
                
                
            if self.yspeed > 0:
                self.ystart = -border
            else:
                self.ystart = sh + border
            
    
            travel_time = (2.0 * border + sh) / abs(yspeed)
    
            xdist = xspeed * travel_time
    
            x0 = min(-xdist, 0)
            x1 = max(sw + xdist, sw)
    
            self.xstart = random.uniform(x0, x1)
    
            if fast:
                self.ystart = random.uniform(-border, sh + border)
                self.xstart = random.uniform(0, sw)
    
        def update(self, st):
            to = st - self.start
            self.angle += self.flutteringspeed
            
    
            xpos = self.xstart + to * self.xspeed + math.sin(self.angle)*self.fluttering
            ypos = self.ystart + to * self.yspeed
    
            if not self.rotate:
                sh = renpy.config.screen_height
            else:
                sh = renpy.config.screen_width
            
            if ypos > sh + self.border:
                return None
    
            if ypos < -self.border:
                return None
    
            if not self.rotate:
                return int(xpos), int(ypos), to + self.offset, self.image
            else:
                return int(ypos), int(xpos), to + self.offset, self.image
        
                
    def SnowBlossom2(d,
                    count=10,
                    border=50,
                    xspeed=(20, 50),
                    yspeed=(100, 200),
                    start=0,
                    fluttering=0,
                    flutteringspeed=0.01,
                    fast=False,
                    horizontal=False):
    
        """
        :doc: sprites_extra
    
        The snowblossom effect moves multiple instances of a sprite up,
        down, left or right on the screen. When a sprite leaves the screen, it
        is returned to the start.
    
        `d`
            The displayable to use for the sprites.
    
        `border`
            The size of the border of the screen. The sprite is considered to be
            on the screen until it clears the border, ensuring that sprites do
            not disappear abruptly.
    
        `xspeed`, `yspeed`
            The speed at which the sprites move, in the horizontal and vertical
            directions, respectively. These can be a single number or a tuple of
            two numbers. In the latter case, each particle is assigned a random
            speed between the two numbers. The speeds can be positive or negative,
            as long as the second number in a tuple is larger than the first.
    
        `start`
            The delay, in seconds, before each particle is added. This can be
            allows the particles to start at the top of the screen, while not
            looking like a "wave" effect.
            
        'fluttering'
            The width of fluttering in pixel.
            
        'flutteringspeed'
            The speed of fluttering.
            
        `fast`
            If true, particles start in the center of the screen, rather than
            only at the edges.
    
        `horizontal`
            If true, particles appear on the left or right side of the screen,
            rather than the top or bottom.
            """
        
        # If going horizontal, swap the xspeed and the yspeed.
        if horizontal:
            xspeed, yspeed = yspeed, xspeed
    
        return Particles(SnowBlossomFactory2(image=d,
                                            count=count,
                                            border=border,
                                            xspeed=xspeed,
                                            yspeed=yspeed,
                                            start=start,
                                            fluttering=fluttering,
                                            flutteringspeed=flutteringspeed,
                                            fast=fast,
                                            rotate=horizontal))



# This bit is required for the Snowing effect:
transform particle(d, delay, startpos, endpos, speed):
    subpixel True
    pause delay
    d
    pos startpos
    linear speed pos endpos

init python:
    class Snowing(renpy.Displayable, NoRollback):
        def __init__(self, d, interval=(0.2, 0.3), start_pos=((-200, config.screen_width), 0), end_pos=({"offset": (100, 200)}, config.screen_height), speed=4.0, slow_start=False, transform=particle, **kwargs):
            """Creates a 'stream' of displayable...
            
            @params:
            -d: Anything that can shown in Ren'Py.
            -interval: Time to wait before adding a new particle. Expects a tuple with two floats.
            -start_pos: x, y starting positions. This expects a tuple of two elements containing either a tuple or an int each.
            -end_pos: x, y end positions. Same rule as above but in addition a dict can be used, in such a case:
                *empty dict will result in straight movement
                *a dict containing an "offset" key will offset the ending position by the value. Expects an int or a tuple of two ints. Default is (100, 200) and attempts to simulate a slight wind to the right (east).
            -speed: A time before particle eaches the end_pos. Expects float or a tuple of floats.
            -slow_start: If not the default False, this will expect a tuple of (time, (new_interval_min, new_interval_max)):
                *This will override the normal interval when the Displayable is first shown for the "time" seconds with the new_interval.
            -transform: ATL function to use for the particles.
                
            The idea behind the design is to enable large amounts of the same displayable guided by instructions from a specified ATL function to
            reach end_pos from start_pos in speed amount of seconds (randomized if needs be). For any rotation, "fluff" or any additional effects different ATL funcs with parallel can be used to achieve the desired effect.
            """
            super(Snowing, self).__init__(**kwargs)
            self.d = renpy.easy.displayable(d)
            self.interval = interval
            self.start_pos = start_pos
            self.end_pos = end_pos
            self.speed = speed
            self.slow_start = slow_start
            self.transform = transform
            
            self.next = 0
            self.shown = {}
        
        def render(self, width, height, st, at):
                
            rp = store.renpy
                
            if not st:
                self.next = 0
                self.shown = {}
                
            render = rp.Render(width, height)
            
            if self.next <= st:
                speed = rp.random.uniform(self.speed[0], self.speed[1])  if isinstance(self.speed, (list, tuple)) else self.speed
                    
                posx = self.start_pos[0]
                posx = rp.random.randint(posx[0], posx[1]) if isinstance(posx, (list, tuple)) else posx
                
                posy = self.start_pos[1]
                posy = rp.random.randint(posy[0], posy[1]) if isinstance(posy, (list, tuple)) else posy
                
                endposx = self.end_pos[0]
                if isinstance(endposx, dict):
                    offset = endposx.get("offset", 0)
                    endposx = posx + rp.random.randint(offset[0], offset[1]) if isinstance(offset, (list, tuple)) else offset
                else:
                    endposx = rp.random.randint(endposx[0], endposx[1]) if isinstance(endposx, (list, tuple)) else endposx
                
                endposy = self.end_pos[1]
                if isinstance(endposy, dict):
                    offset = endposy.get("offset", 0)
                    endposy = posy + randint.randint(offset[0], offset[1]) if isinstance(offset, (list, tuple)) else offset
                else:
                    endposy = rp.random.randint(endposy[0], endposy[1]) if isinstance(endposy, (list, tuple)) else endposy
                
                self.shown[st + speed] = self.transform(self.d, st, (posx, posy), (endposx, endposy), speed)
                if self.slow_start and st < self.slow_start[0]:
                    interval = self.slow_start[1]
                    self.next = st + rp.random.uniform(interval[0], interval[1])
                else:
                    self.next = st + rp.random.uniform(self.interval[0], self.interval[1])
            
            for d in self.shown.keys():
                if d < st:
                    del(self.shown[d])
                else:
                    d = self.shown[d]
                    render.blit(d.render(width, height, st, at), (d.xpos, d.ypos))
                    
            rp.redraw(self, 0)
            
            return render
            
        def visit(self):
            return [self.d]


