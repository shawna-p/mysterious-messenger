#************************************
# Emotes
#************************************
init offset = -10

init python:

    ## This defines another voice channel which the emoji
    ## sound effects play on. Players can adjust the volume
    ## of the emojis separately from voice, music, and sfx
    renpy.music.register_channel("voice_sfx", mixer="voice_sfx", loop=False)

    def set_voicesfx_volume(value=None):
        """Set the volume of the voice sfx channel."""

        if value is None:
            return MixerValue('voice_sfx')
        else:
            return SetMixer('voice_sfx', value)

    ## This list contains all of the emojis, linked to the correct sound
    ## effect. Essentially, if the dialogue matches the item on the left
    ## (e.g. {image=jaehee_angry}) then it will play the sound effect on
    ## the right. If you add your own custom emojis, you need to add
    ## them to this list so that they play the correct sound effect
    emoji_lookup = {
        '{image=jaehee_angry}': 'audio/sfx/Emotes/Jaehee/jaehee_angry.mp3',
        '{image=jaehee_happy}': 'audio/sfx/Emotes/Jaehee/jaehee_happy.mp3',
        '{image=jaehee_hehe}': 'audio/sfx/Emotes/Jaehee/jaehee_hehe.mp3',
        '{image=jaehee_huff}': 'audio/sfx/Emotes/Jaehee/jaehee_huff.mp3',
        '{image=jaehee_oops}': 'audio/sfx/Emotes/Jaehee/jaehee_oops.mp3',
        '{image=jaehee_question}': 'audio/sfx/Emotes/Jaehee/jaehee_question.mp3',
        '{image=jaehee_sad}': 'audio/sfx/Emotes/Jaehee/jaehee_sad.mp3',
        '{image=jaehee_well}': 'audio/sfx/Emotes/Jaehee/jaehee_well.mp3',
        '{image=jaehee_wow}': 'audio/sfx/Emotes/Jaehee/jaehee_wow.mp3',

        '{image=jumin_angry}': 'audio/sfx/Emotes/Jumin/jumin_angry.mp3',
        '{image=jumin_sad}': 'audio/sfx/Emotes/Jumin/jumin_sad.mp3',
        '{image=jumin_smile}': 'audio/sfx/Emotes/Jumin/jumin_smile.mp3',
        '{image=jumin_well}': 'audio/sfx/Emotes/Jumin/jumin_well.mp3',

        '{image=rika_happy}': 'audio/sfx/Emotes/Rika/rika_happy.mp3',
        '{image=rika_pout}': 'audio/sfx/Emotes/Rika/rika_pout.mp3',
        '{image=rika_cry}': 'audio/sfx/Emotes/Rika/rika_cry.mp3',

        '{image=ray_cry}': 'audio/sfx/Emotes/Ray/ray_cry.mp3',
        '{image=ray_happy}': 'audio/sfx/Emotes/Ray/ray_happy.mp3',
        '{image=ray_huff}': 'audio/sfx/Emotes/Ray/ray_huff.mp3',
        '{image=ray_question}': 'audio/sfx/Emotes/Ray/ray_question.mp3',
        '{image=ray_smile}': 'audio/sfx/Emotes/Ray/ray_smile.mp3',
        '{image=ray_well}': 'audio/sfx/Emotes/Ray/ray_well.mp3',
        '{image=ray_wink}': 'audio/sfx/Emotes/Ray/ray_wink.mp3',

        '{image=saeran2_cry}': 'audio/sfx/Emotes/Ray/ray_cry.mp3',
        '{image=saeran2_happy}': 'audio/sfx/Emotes/Ray/ray_happy.mp3',
        '{image=saeran2_huff}': 'audio/sfx/Emotes/Ray/ray_huff.mp3',
        '{image=saeran2_question}': 'audio/sfx/Emotes/Ray/ray_question.mp3',
        '{image=saeran2_smile}': 'audio/sfx/Emotes/Ray/ray_smile.mp3',
        '{image=saeran2_well}': 'audio/sfx/Emotes/Ray/ray_well.mp3',
        '{image=saeran2_wink}': 'audio/sfx/Emotes/Ray/ray_wink.mp3',

        '{image=saeran_expecting}': 'audio/sfx/Emotes/Saeran/saeran_expecting.mp3',
        '{image=saeran_happy}': 'audio/sfx/Emotes/Saeran/saeran_happy.mp3',
        '{image=saeran_questioning}': 'audio/sfx/Emotes/Saeran/saeran_questioning.mp3',
        '{image=saeran_well}': 'audio/sfx/Emotes/Saeran/saeran_well.mp3',

        '{image=seven_cry}': 'audio/sfx/Emotes/Seven/seven_cry.mp3',
        '{image=seven_huff}': 'audio/sfx/Emotes/Seven/seven_huff.mp3',
        '{image=seven_khee}': 'audio/sfx/Emotes/Seven/seven_khee.mp3',
        '{image=seven_love}': 'audio/sfx/Emotes/Seven/seven_love.mp3',
        '{image=seven_question}': 'audio/sfx/Emotes/Seven/seven_question.mp3',
        '{image=seven_what}': 'audio/sfx/Emotes/Seven/seven_what.mp3',
        '{image=seven_wow}': 'audio/sfx/Emotes/Seven/seven_wow.mp3',
        '{image=seven_yahoo}': 'audio/sfx/Emotes/Seven/seven_yahoo.mp3',
        '{image=seven_yoohoo}': 'audio/sfx/Emotes/Seven/seven_yoohoo.mp3',

        '{image=v_shock}': 'audio/sfx/Emotes/V/v_shock.mp3',
        '{image=v_smile}': 'audio/sfx/Emotes/V/v_smile.mp3',
        '{image=v_well}': 'audio/sfx/Emotes/V/v_well.mp3',
        '{image=v_wink}': 'audio/sfx/Emotes/V/v_wink.mp3',

        '{image=yoosung_angry}': 'audio/sfx/Emotes/Yoosung/yoosung_angry.mp3',
        '{image=yoosung_cry}': 'audio/sfx/Emotes/Yoosung/yoosung_cry.mp3',
        '{image=yoosung_happy}': 'audio/sfx/Emotes/Yoosung/yoosung_happy.mp3',
        '{image=yoosung_huff}': 'audio/sfx/Emotes/Yoosung/yoosung_huff.mp3',
        '{image=yoosung_puff}': 'audio/sfx/Emotes/Yoosung/yoosung_puff.mp3',
        '{image=yoosung_question}': 'audio/sfx/Emotes/Yoosung/yoosung_question.mp3',
        '{image=yoosung_thankyou}': 'audio/sfx/Emotes/Yoosung/yoosung_thankyou.mp3',
        '{image=yoosung_what}': 'audio/sfx/Emotes/Yoosung/yoosung_what.mp3',
        '{image=yoosung_wow}': 'audio/sfx/Emotes/Yoosung/yoosung_wow.mp3',
        '{image=yoosung_yahoo}': 'audio/sfx/Emotes/Yoosung/yoosung_yahoo.mp3',

        '{image=zen_angry}': 'audio/sfx/Emotes/Zen/zen_angry.mp3',
        '{image=zen_happy}': 'audio/sfx/Emotes/Zen/zen_happy.mp3',
        '{image=zen_hmm}': 'audio/sfx/Emotes/Zen/zen_hmm.mp3',
        '{image=zen_oyeah}': 'audio/sfx/Emotes/Zen/zen_oyeah.mp3',
        '{image=zen_question}': 'audio/sfx/Emotes/Zen/zen_question.mp3',
        '{image=zen_sad}': 'audio/sfx/Emotes/Zen/zen_sad.mp3',
        '{image=zen_shock}': 'audio/sfx/Emotes/Zen/zen_shock.mp3',
        '{image=zen_well}': 'audio/sfx/Emotes/Zen/zen_well.mp3',
        '{image=zen_wink}': 'audio/sfx/Emotes/Zen/zen_wink.mp3'
        }

## These are defined for the (currently unused) create_a_chatroom
define jaehee_emotes = ['{image=jaehee_angry}',
                    '{image=jaehee_happy}',
                    '{image=jaehee_hehe}',
                    '{image=jaehee_huff}',
                    '{image=jaehee_oops}',
                    '{image=jaehee_question}',
                    '{image=jaehee_sad}',
                    '{image=jaehee_well}',
                    '{image=jaehee_wow}']

define jumin_emotes = [ '{image=jumin_angry}',
                    '{image=jumin_sad}',
                    '{image=jumin_smile}',
                    '{image=jumin_well}']

define rika_emotes = ['{image=rika_happy}',
                        '{image=rika_pout}',
                        '{image=rika_cry}']

define ray_emotes = ['{image=ray_cry}',
                    '{image=ray_happy}',
                    '{image=ray_huff}',
                    '{image=ray_question}',
                    '{image=ray_smile}',
                    '{image=ray_well}',
                    '{image=ray_wink}',

                    '{image=saeran2_cry}',
                    '{image=saeran2_happy}',
                    '{image=saeran2_huff}',
                    '{image=saeran2_question}',
                    '{image=saeran2_smile}',
                    '{image=saeran2_well}',
                    '{image=saeran2_wink}']

define saeran_emotes = ['{image=saeran_expecting}',
                    '{image=saeran_happy}',
                    '{image=saeran_questioning}',
                    '{image=saeran_well}']

define seven_emotes = ['{image=seven_cry}',
                    '{image=seven_huff}',
                    '{image=seven_khee}',
                    '{image=seven_love}',
                    '{image=seven_question}',
                    '{image=seven_what}',
                    '{image=seven_wow}',
                    '{image=seven_yahoo}',
                    '{image=seven_yoohoo}']

define v_emotes = ['{image=v_shock}',
                    '{image=v_smile}',
                    '{image=v_well}',
                    '{image=v_wink}']

define yoosung_emotes = ['{image=yoosung_angry}',
                    '{image=yoosung_cry}',
                    '{image=yoosung_happy}',
                    '{image=yoosung_huff}',
                    '{image=yoosung_puff}',
                    '{image=yoosung_question}',
                    '{image=yoosung_thankyou}',
                    '{image=yoosung_what}',
                    '{image=yoosung_wow}',
                    '{image=yoosung_yahoo}']

define zen_emotes = ['{image=zen_angry}',
                    '{image=zen_happy}',
                    '{image=zen_hmm}',
                    '{image=zen_oyeah}',
                    '{image=zen_question}',
                    '{image=zen_sad}',
                    '{image=zen_shock}',
                    '{image=zen_well}',
                    '{image=zen_wink}']

define all_emotes = (jaehee_emotes + jumin_emotes + rika_emotes
                    + ray_emotes + seven_emotes + saeran_emotes
                    + v_emotes + yoosung_emotes + zen_emotes)

## The image definitions of all the emojis follows
# ******** JAEHEE ******************

image jaehee_angry:
    "Gifs/Jaehee/emo_jaehee_angry1.webp"
    0.5
    "Gifs/Jaehee/emo_jaehee_angry2.webp"
    0.5
    repeat

image jaehee_happy:
    "Gifs/Jaehee/emo_jaehee_happy1.webp"
    0.5
    "Gifs/Jaehee/emo_jaehee_happy2.webp"
    0.5
    repeat

image jaehee_hehe:
    "Gifs/Jaehee/emo_jaehee_hehe1.webp"
    0.5
    "Gifs/Jaehee/emo_jaehee_hehe2.webp"
    0.5
    repeat

image jaehee_huff:
    "Gifs/Jaehee/emo_jaehee_huff1.webp"
    0.5
    "Gifs/Jaehee/emo_jaehee_huff2.webp"
    0.5
    repeat

image jaehee_oops:
    "Gifs/Jaehee/emo_jaehee_oops1.webp"
    0.5
    "Gifs/Jaehee/emo_jaehee_oops2.webp"
    0.5
    repeat

image jaehee_question:
    "Gifs/Jaehee/emo_jaehee_question1.webp"
    0.5
    "Gifs/Jaehee/emo_jaehee_question2.webp"
    0.5
    repeat

image jaehee_sad:
    "Gifs/Jaehee/emo_jaehee_sad1.webp"
    0.5
    "Gifs/Jaehee/emo_jaehee_sad2.webp"
    0.5
    repeat

image jaehee_well:
    "Gifs/Jaehee/emo_jaehee_well1.webp"
    0.5
    "Gifs/Jaehee/emo_jaehee_well2.webp"
    0.5
    repeat

image jaehee_wow:
    "Gifs/Jaehee/emo_jaehee_wow1.webp"
    0.5
    "Gifs/Jaehee/emo_jaehee_wow2.webp"
    0.5
    repeat


# ******** JUMIN ******************

image jumin_angry:
    "Gifs/Jumin/emo_jumin_angry1.webp"
    0.5
    "Gifs/Jumin/emo_jumin_angry2.webp"
    0.5
    repeat

image jumin_sad:
    "Gifs/Jumin/emo_jumin_sad1.webp"
    0.5
    "Gifs/Jumin/emo_jumin_sad2.webp"
    0.5
    repeat

image jumin_smile:
    "Gifs/Jumin/emo_jumin_smile1.webp"
    0.5
    "Gifs/Jumin/emo_jumin_smile2.webp"
    0.5
    repeat

image jumin_well:
    "Gifs/Jumin/emo_jumin_well1.webp"
    0.5
    "Gifs/Jumin/emo_jumin_well2.webp"
    0.5
    repeat


# ******** RAY ******************

image ray_cry:
    "Gifs/Ray/emo_ray_cry1.webp"
    0.5
    "Gifs/Ray/emo_ray_cry2.webp"
    0.5
    repeat

image ray_happy:
    "Gifs/Ray/emo_ray_happy1.webp"
    0.5
    "Gifs/Ray/emo_ray_happy2.webp"
    0.5
    repeat

image ray_huff:
    "Gifs/Ray/emo_ray_huff1.webp"
    0.5
    "Gifs/Ray/emo_ray_huff2.webp"
    0.5
    repeat

image ray_question:
    "Gifs/Ray/emo_ray_question1.webp"
    0.5
    "Gifs/Ray/emo_ray_question2.webp"
    0.5
    repeat

image ray_smile:
    "Gifs/Ray/emo_ray_smile1.webp"
    0.5
    "Gifs/Ray/emo_ray_smile2.webp"
    0.5
    repeat

image ray_well:
    "Gifs/Ray/emo_ray_well1.webp"
    0.5
    "Gifs/Ray/emo_ray_well2.webp"
    0.5
    repeat

image ray_wink:
    "Gifs/Ray/emo_ray_wink1.webp"
    0.5
    "Gifs/Ray/emo_ray_wink2.webp"
    0.5
    repeat

# ******** RIKA ******************
# Credit to Sakekobomb for the emotes
# Used with permission

image rika_happy:
    "Gifs/Rika/emo_rika_happy1.webp"
    0.5
    "Gifs/Rika/emo_rika_happy2.webp"
    0.5
    repeat

image rika_pout:
    "Gifs/Rika/emo_rika_pout1.webp"
    0.5
    "Gifs/Rika/emo_rika_pout2.webp"
    0.5
    repeat

image rika_cry:
    "Gifs/Rika/emo_rika_cry1.webp"
    0.5
    "Gifs/Rika/emo_rika_cry2.webp"
    0.5
    repeat


# ******** SAERAN ******************

image saeran_expecting:
    "Gifs/Saeran/emo_saeran_expecting1.webp"
    0.5
    "Gifs/Saeran/emo_saeran_expecting2.webp"
    0.5
    repeat

image saeran_happy:
    "Gifs/Saeran/emo_saeran_happy1.webp"
    0.5
    "Gifs/Saeran/emo_saeran_happy2.webp"
    0.5
    repeat

image saeran_questioning:
    "Gifs/Saeran/emo_saeran_questioning1.webp"
    0.5
    "Gifs/Saeran/emo_saeran_questioning2.webp"
    0.5
    repeat

image saeran_well:
    "Gifs/Saeran/emo_saeran_well1.webp"
    0.5
    "Gifs/Saeran/emo_saeran_well2.webp"
    0.5
    repeat

# ******** SAERAN (Sweater) ******************
# ** Credit to its-a-me-haruhi.tumblr.com for
#     the recolours

image saeran2_cry:
    "Gifs/Saeran2/emo_sae_cry1.webp"
    0.5
    "Gifs/Saeran2/emo_sae_cry2.webp"
    0.5
    repeat

image saeran2_happy:
    "Gifs/Saeran2/emo_sae_happy1.webp"
    0.5
    "Gifs/Saeran2/emo_sae_happy2.webp"
    0.5
    repeat

image saeran2_huff:
    "Gifs/Saeran2/emo_sae_huff1.webp"
    0.5
    "Gifs/Saeran2/emo_sae_huff2.webp"
    0.5
    repeat

image saeran2_question:
    "Gifs/Saeran2/emo_sae_question1.webp"
    0.5
    "Gifs/Saeran2/emo_sae_question2.webp"
    0.5
    repeat

image saeran2_smile:
    "Gifs/Saeran2/emo_sae_smile1.webp"
    0.5
    "Gifs/Saeran2/emo_sae_smile2.webp"
    0.5
    repeat

image saeran2_well:
    "Gifs/Saeran2/emo_sae_well1.webp"
    0.5
    "Gifs/Saeran2/emo_sae_well2.webp"
    0.5
    repeat

image saeran2_wink:
    "Gifs/Saeran2/emo_sae_wink1.webp"
    0.5
    "Gifs/Saeran2/emo_sae_wink2.webp"
    0.5
    repeat

# ******** SEVEN ******************

image seven_cry:
    "Gifs/Seven/emo_seven_cry1.webp"
    0.5
    "Gifs/Seven/emo_seven_cry2.webp"
    0.5
    repeat

image seven_huff:
    "Gifs/Seven/emo_seven_huff1.webp"
    0.5
    "Gifs/Seven/emo_seven_huff2.webp"
    0.5
    repeat

image seven_khee:
    "Gifs/Seven/emo_seven_khee1.webp"
    0.5
    "Gifs/Seven/emo_seven_khee2.webp"
    0.5
    repeat

image seven_love:
    "Gifs/Seven/emo_seven_love1.webp"
    0.5
    "Gifs/Seven/emo_seven_love2.webp"
    0.5
    repeat

image seven_question:
    "Gifs/Seven/emo_seven_question1.webp"
    0.5
    "Gifs/Seven/emo_seven_question2.webp"
    0.5
    repeat

image seven_what:
    "Gifs/Seven/emo_seven_what1.webp"
    0.5
    "Gifs/Seven/emo_seven_what2.webp"
    0.5
    repeat

image seven_wow:
    "Gifs/Seven/emo_seven_wow1.webp"
    0.5
    "Gifs/Seven/emo_seven_wow2.webp"
    0.5
    repeat

image seven_yahoo:
    "Gifs/Seven/emo_seven_yahoo1.webp"
    0.5
    "Gifs/Seven/emo_seven_yahoo2.webp"
    0.5
    repeat

image seven_yoohoo:
    "Gifs/Seven/emo_seven_yoohoo1.webp"
    0.5
    "Gifs/Seven/emo_seven_yoohoo2.webp"
    0.5
    repeat


# ************* V ******************

image v_shock:
    "Gifs/V/emo_v_shock1.webp"
    0.5
    "Gifs/V/emo_v_shock2.webp"
    0.5
    repeat

image v_smile:
    "Gifs/V/emo_v_smile1.webp"
    0.5
    "Gifs/V/emo_v_smile2.webp"
    0.5
    repeat

image v_well:
    "Gifs/V/emo_v_well1.webp"
    0.5
    "Gifs/V/emo_v_well2.webp"
    0.5
    repeat

image v_wink:
    "Gifs/V/emo_v_wink1.webp"
    0.5
    "Gifs/V/emo_v_wink2.webp"
    0.5
    repeat


# ********* YOOSUNG ******************

image yoosung_angry:
    "Gifs/Yoosung/emo_yoosung_angry1.webp"
    0.5
    "Gifs/Yoosung/emo_yoosung_angry2.webp"
    0.5
    repeat

image yoosung_cry:
    "Gifs/Yoosung/emo_yoosung_cry1.webp"
    0.5
    "Gifs/Yoosung/emo_yoosung_cry2.webp"
    0.5
    repeat

image yoosung_happy:
    "Gifs/Yoosung/emo_yoosung_happy1.webp"
    0.5
    "Gifs/Yoosung/emo_yoosung_happy2.webp"
    0.5
    repeat

image yoosung_huff:
    "Gifs/Yoosung/emo_yoosung_huff1.webp"
    0.5
    "Gifs/Yoosung/emo_yoosung_huff2.webp"
    0.5
    repeat

image yoosung_puff:
    "Gifs/Yoosung/emo_yoosung_puff1.webp"
    0.5
    "Gifs/Yoosung/emo_yoosung_puff2.webp"
    0.5
    repeat

image yoosung_question:
    "Gifs/Yoosung/emo_yoosung_question1.webp"
    0.5
    "Gifs/Yoosung/emo_yoosung_question2.webp"
    0.5
    repeat

image yoosung_thankyou:
    "Gifs/Yoosung/emo_yoosung_thankyou1.webp"
    0.5
    "Gifs/Yoosung/emo_yoosung_thankyou2.webp"
    0.5
    repeat

image yoosung_what:
    "Gifs/Yoosung/emo_yoosung_what1.webp"
    0.5
    "Gifs/Yoosung/emo_yoosung_what2.webp"
    0.5
    repeat

image yoosung_wow:
    "Gifs/Yoosung/emo_yoosung_wow1.webp"
    0.5
    "Gifs/Yoosung/emo_yoosung_wow2.webp"
    0.5
    repeat

image yoosung_yahoo:
    "Gifs/Yoosung/emo_yoosung_yahoo1.webp"
    0.5
    "Gifs/Yoosung/emo_yoosung_yahoo2.webp"
    0.5
    repeat


# ************ ZEN ******************

image zen_angry:
    "Gifs/Zen/emo_zen_angry1.webp"
    0.5
    "Gifs/Zen/emo_zen_angry2.webp"
    0.5
    repeat

image zen_happy:
    "Gifs/Zen/emo_zen_happy1.webp"
    0.5
    "Gifs/Zen/emo_zen_happy2.webp"
    0.5
    repeat

image zen_hmm:
    "Gifs/Zen/emo_zen_hmm1.webp"
    0.5
    "Gifs/Zen/emo_zen_hmm2.webp"
    0.5
    repeat

image zen_oyeah:
    "Gifs/Zen/emo_zen_oyeah1.webp"
    0.5
    "Gifs/Zen/emo_zen_oyeah2.webp"
    0.5
    repeat

image zen_question:
    "Gifs/Zen/emo_zen_q1.webp"
    0.5
    "Gifs/Zen/emo_zen_q2.webp"
    0.5
    repeat

image zen_sad:
    "Gifs/Zen/emo_zen_sad1.webp"
    0.5
    "Gifs/Zen/emo_zen_sad2.webp"
    0.5
    repeat

image zen_shock:
    "Gifs/Zen/emo_zen_shock1.webp"
    0.5
    "Gifs/Zen/emo_zen_shock2.webp"
    0.5
    repeat

image zen_well:
    "Gifs/Zen/emo_zen_well1.webp"
    0.5
    "Gifs/Zen/emo_zen_well2.webp"
    0.5
    repeat

image zen_wink:
    "Gifs/Zen/emo_zen_wink1.webp"
    0.5
    "Gifs/Zen/emo_zen_wink2.webp"
    0.5
    repeat

