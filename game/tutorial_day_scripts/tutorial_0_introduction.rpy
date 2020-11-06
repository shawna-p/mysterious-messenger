label start():

    # This call sets up which route the game is going to use -- in this
    # case, tutorial_route, defined in route_setup.rpy. You will give
    # it the name of whatever you'd like your own route to be.
    # You can have text messages or phone calls after this introduction by
    # using labels such as `starter_chat_incoming_ja` or `after_starter_chat`.
    # You can also include a Story Mode section sometime during the
    # introduction by using `call vn_begin`, though that isn't shown here.
    $ new_route_setup(route=tutorial_route)

    # This tells the program which characters' profiles you want to see
    # on the hub screen / available for phone calls / etc
    $ character_list = [ju, z, s, y, ja, v, m, r, ri]
    # This tells the program which characters to show on the Profile screen
    # next to how many heart points the player has earned
    $ heart_point_chars = [ju, z, s, y, ja, v, r, ri]

    # You can set this at the beginning of a route. If True, the program will
    # assume choices are "paraphrased", and will expect you to write out any
    # character dialogue after the choice. If False, the program will
    # automatically cause the main character to say the exact dialogue
    # contained in the choice. This can be changed on a per-menu or per-choice
    # basis. If you wrote your script prior to v3.0, you probably want to set
    # this to True.
    $ paraphrase_choices = False

    # For this route, some specific profile picture callbacks are defined
    # in a function called "tutorial_pfp_dialogue". That function is defined
    # at the end of this file.
    $ mc_pfp_callback = tutorial_pfp_dialogue

    ## If you don't want an introduction, you can uncomment this line.
    ## When the player starts the game, they will be immediately taken
    ## to the hub screen.
    # jump skip_intro_setup

    # If you want to begin with a phone call, this is
    # how you do it. Just replace 'u' with whatever
    # character you want to call the player
    call new_incoming_call(u)

    # This is used to remember a choice the player made. It is only used
    # in this particular label, so it is not defaulted outside the label.
    $ regular_intro = False

    u """

    Oh! You picked up; I'm so relieved.

    I thought maybe you wouldn't since my number wouldn't be listed in your phone.

    """

    if persistent.HP:
        u "It looks like you've played through some of this program before! I'm happy you've come back~"
        u "There are lots of new things to check out in the most recent version, so I hope you'll give Tutorial Day another playthrough."
        u "Since you're so seasoned, I'll let you start right away."
        u "But before that, I wanted to ask -- do you want to change any of your animation settings? I can turn off the hacking effects and screenshake if you want."
        menu:
            extend ''
            "Tell me about the animation settings.":
                u "Got it. Sometimes the program has animations like the scrolling hacked code effect, or banners in the chatrooms. There is also a screen shake animation. Do you want any of these animations turned off?"
            "I'm good to go; take me to the rest of the game!":
                u "Sounds good! I'll see you later~"
                # This is pretty specific to this particular chat; you
                # should not have to do this. It simply makes it easier
                # for players who have already played through the game
                # to get to the chat hub
                jump skip_intro_setup
            "I'd like to see the regular intro.":
                $ regular_intro = True
                u "Okay!"
                u "I'm calling because I was hoping you could help me test a new app I made. What do you think?"
                jump regular_intro
    else:
        "I'm calling because I was hoping you could help me test a new app I made. What do you think?"

        menu regular_intro:
            extend ''
            "Testing? What would I need to do?":
                # Because paraphrase_choices is False, the program will
                # automatically cause the MC to say this dialogue, so it is
                # unnecessary to write it.
                pass
            "Sounds like a lot of work.":
                u "Oh, it's not bad, I promise!"

        u """

        All you have to do is use the app, and then you let me know if you run into problems or bugs.

        It'll help me make a much better program, in the end.

        You only need to use it as much as you have time for. And in return you get to test out my program earlier than anyone else!

        So what do you say?

        """

        menu:
            extend ''
            "I suppose I'll give it a shot.":
                pass

        u """

        You will? Wonderful!

        I also wanted to ask -- how do you feel about short flashing animations?

        Sometimes the program has animations like the scrolling hacked code effect, or banners in the chatrooms. There is also a screen shake animation.

        """

    menu:
        extend ''
        "I don't want to see any flashing animations or screenshake.":
            # These `if not observing` statements are to make sure a player
            # playing this from the History screen won't inadvertently have
            # their settings changed on them.
            if not observing:
                $ persistent.screenshake = False
                $ persistent.banners = False
                $ persistent.hacking_effects = False
            u "Understandable! I've turned all those animations off for you."

        "I'm okay with some effects but not with others.":
            if not observing:
                $ persistent.hacking_effects = False
            u "Okay! I've just turned the hacking effect off for now since it shows up in the next chatroom."

        "You can keep all the animations on.":
            if not observing:
                $ persistent.screenshake = True
                $ persistent.banners = True
                $ persistent.hacking_effects = True
            u "Got it!"

    u """

    If you ever want to change which animations you see, you can find toggles for each of them in the {b}Settings{/b}.

    There are other accessibility options there as well, such as audio captions for background music and sound effects.

    """

    if persistent.HP and not regular_intro:
        u "Alright, enjoy the program!"
        jump skip_intro_setup

    u """

    Alright, so when this call ends I'll send you a chatroom message with a bit more information on getting started from here.

    Good luck!

    """

    # Instead of ending the label here, you can continue with
    # a chatroom. If you don't want the phonecall beforehand,
    # just delete that section.
    # Feel free to modify the chatroom beyond this point. You need to use
    # `call chat_begin` here to ensure the chatroom is set up properly, since
    # the program doesn't know if you want to begin the route with a chatroom,
    # phone call, or Story Mode (VN), so you need to specify in the prologue.
    call chat_begin('hack')
    show hack effect
    scene hack

    play music mystic_chat

    enter chatroom u
    u "You're here!"
    u "Thank you for helping me ^^"
    u "As you can see, this is a sort of \"introductory\" chatroom. It works a lot like the other chatrooms,"
    u "but with a couple of changes you can see in {b}tutorial_0_introduction.rpy{/b}"
    u "I recommend you get familiar with how regular chatrooms and phonecalls work before you look at this chat, though!"

    call answer
    menu:
        "What should I look at first?":
            u "Well, the first thing I recommend is to just play through the Tutorial Day."
            u "It showcases some of the features so you know what sorts of things you can do with the program."

    u "I won't keep you much longer. Enjoy the program!"
    exit chatroom u

    jump end_prologue



init -1 python:
    def tutorial_pfp_dialogue(time_diff, prev_pic, current_pic, who):
        """
        An example callback function for when the player changes their
        profile picture.
        """

        # time_diff is a timedelta object wrapped in a MyTimeDelta class to
        # make accessing fields easier. Its most useful fields are `days`,
        # `minutes`, `hours`, and `seconds`. Each field is rounded DOWN to the
        # nearest value e.g. if 2 minutes have passed, seconds = 120,
        # minutes = 2, and hours and days = 0.
        if time_diff.seconds < 10:
            # This is for testing; most times you will want a larger number
            # such as `if time_diff.hours < 2` so that the player is discouraged
            # from constantly changing their profile picture to check for
            # a callback. In this case, the program will return if it's been
            # less than 10 seconds since the profile picture was changed.
            return


        # Otherwise, figure out what to do based on the other properties.
        # There are lots of things to check, and many more program variables
        # you can take advantage of which aren't shown here.
        if (store.today_day_num == 0
                and who == None
                and "CGs/common_album/cg-1" in current_pic):
            # This statement checks: Is today Tutorial Day? (since Tutorial
            # Day is the first day on the route, its index is 0)
            # Who is associated with this image? (None for common album)
            # Is this image "cg-1" from the common album?

            # If so, this is the silly pass-out-after-drinking-caffeine
            # screenshot. Seven will send the player a text message, so the
            # game should jump to the label returned here.
            return "seven_pfp_callback_coffee"

        if (who == None and "CGs/common_album/cg-2" in current_pic):
            # This checks for the picture the player can send Zen during
            # a text message conversation.

            # You can return a list of labels, and the program will use the
            # first one that hasn't been seen before in this playthrough.
            return ['zen_pfp_callback_unknown1', 'zen_pfp_callback_unknown2']

        return

label seven_pfp_callback_coffee():
    compose text s real_time:
        s "lolololol [name]"
        s "u saved the screenshot for ur profile pic??"
        label seven_pfp_callback_coffee_menu
    return

label seven_pfp_callback_coffee_menu:
    call answer
    menu:
        "Ya lol I thought it was funny >.<":
            award heart s
            s "Omg"
            msg s "{image=seven_wow}"
            s "ur hilarious lolol"
        "Where did you get this screenshot? I can't find it on Cherrypedia":
            s "[name] omg"
            s "Don't tell me"
            s "ur like Yoosung lolol"
            call answer
            menu:
                "Huh? I don't understand":
                    s "lololol"
                    s "Don't worry about it."
                "lolol I'm pulling your leg":
                    s "!!!"
                    s "Wow ur something else lol"
    s "Talk to u later!"
    return

label zen_pfp_callback_unknown1():
    # The first time you change your profile picture to this, Zen will
    # call you. This creates an incoming call that will be delivered when
    # the player is on the main menu.
    $ create_incoming_call("zen_pfp_callback_unknown1_incoming", who=z)
    return

label zen_pfp_callback_unknown1_incoming():
    z "Hi [name]!"
    menu:
        extend ''
        "Zen? What are you calling me for?":
            z "Aw babe, don't be like that~ I was just thinking about you."
        "Zen! I missed you~":
            z "Don't say things like that haha, you never know what a man might be thinking."
    z "I had a question for you, actually. I saw that you changed your profile picture recently."
    if sent_zen_unknown_pic:
        z "It's the picture you messaged me earlier, right?"
    else:
        z "I'm not supposed to remember this, but on a different playthrough you sent me that picture in a text message."
    z "I was just wondering who it is. It's not a picture of you, is it?"
    if persistent.pronoun == "she/her":
        z "I mean I was kind of under the impression that you're a girl but... we've never met in person so I wanted to ask."
    menu:
        extend ''
        "Someone sent me that picture a while ago.":
            z "So it's not a picture of you? Oh, okay."
            z "You should send me some selfies sometime though~ I'm sure you're very cute!"
        "That's a picture of me.":
            z "Oh, really? Oh. Okay. Well thank you for telling me!"
            menu:
                extend ''
                "Lol I'm just kidding.":
                    $ last_c = name[-1]
                    z "[name][last_c][last_c] I can't believe you'd tease me like this haha."

    z "Anyway, I have some stuff I should do today yet. Thanks for talking with me!"
    return

label zen_pfp_callback_unknown2():
    # The second time you change your profile picture to the Unknown picture,
    # Zen's space thoughts will change. Using `add_choices` instead of
    # `new_choices` will allow you to add to the existing choices instead
    # of replacing them.
    $ space_thoughts.add_choices(
        SpaceThought(z, "[name] changed [their] profile picture to that random guy again... why [do_does] [they] like that picture so much?")
    )
    return