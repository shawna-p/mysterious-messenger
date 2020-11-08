label example_solo_vn():
    play music narcissistic_jazz
    scene bg zen_room_day
    show zen side happy at vn_midright
    z "Good to see you here, [name]!"
    z "This is what's called a \"Solo VN\" or a \"Solo Story Mode\"."
    z neutral "It isn't attached to a chatroom, and can be scheduled to appear at a particular time."
    z happy "It can also have its own phone calls, text messages, plot branches, and other features."
    z "Unlike chatrooms and story calls, however, Story Mode items won't expire even if the player is playing in real-time."
    z neutral "Other than that, though, it works just like a regular Story Mode."
    z wink "So instead I thought I'd explain a few other aspects of the program you might not know about."
    z neutral "Is there anything you want to learn about?"
    call extra_features_showcase()
    z wink "Thanks for coming by! I hope you enjoy the program~"
    return

label extra_features_showcase():
    $ shuffle = False
    menu (paraphrased=True):
        extend ''
        "Bonus profile pictures":
            m "Tell me about bonus profile pictures."
            z happy "Sure! Bonus profile pictures were added by request for v3.0"
            z wink "You can request future features in the Mysterious Messenger Discord, too~"
            z neutral "There are two kinds of bonus profile pictures; the first is for characters like me,"
            z "And the second is for you, the player."
            z "Which do you want to hear about?"
            jump bonus_pfp_showcase
        "Extra gallery features":
            m "I want to know about extra gallery features."
            z happy "Of course!"
            z neutral "As of version 3.0, you can now hide certain albums in the gallery until an image has been unlocked in it."
            z "If an album is not in the \"all_albums\" list, or you use the special function \"hide_albums\", it will only appear in the Gallery screen after a photo has been unlocked."
            z "This means you can use it to hide empty albums, or to only show a Christmas album to a player who has earned a CG for that album, for example."
            z thinking "Hiding an album doesn't prevent the player from unlocking CGs contained in it."
            z neutral "Albums also work with the Bonus Profile Pictures system to allow the player to set their own and other characters' profile pictures to gallery images."
            z happy "And that's all! Is there anything else you wanted to learn about?"
        "Testing mode and developer features":
            m "Can you explain testing mode and other developer features?"
            z happy "I can! Developer features are intended to make testing a route easier for the user."
            z neutral "You can access the developer settings via the {b}Developer{/b} button on the home screen or from the main menu."
            show tut_dev_options at tutorial_anim(100)
            pause 0.5
            show tut_arrow:
                xpos 330
                ypos 540
            z "{b}Testing Mode{/b}, when checked, will add several features to the program."
            z "First, every time you enter a story item it is considered to be the \"first\" time."
            z "So that means you can make different choices each time, or even use the back button in chatrooms and the end call button in phone calls to force that story item to expire."
            hide tut_dev_options
            hide tut_arrow
            show tut_skip_to_end at tutorial_anim(100) behind tut_arrow
            pause 0.5
            show tut_arrow_vert:
                rotate 90
                xpos 455
                ypos 655
            z "Second, inside every chatroom will be a \"Skip to End\" button. If you click this, it will instantly show the Save & Exit sign at the bottom of the screen."
            z "You can use this to end a chatroom instantly if you're only testing certain parts."
            hide tut_skip_to_end
            hide tut_arrow_vert
            z "Or, if you're just testing text messages, phone calls, or plot branches, you can also right-click any item on the timeline and it will be instantly marked as played."
            z thinking "Note that this will {b}not{/b} execute any of the code inside the story item itself, so you won't get any heart points, for example."
            z neutral "It {b}will{/b}, however, mark the item as played/participated and execute its {b}_after{/b} label."
            z happy "It's good for quickly testing program flow."
            z neutral "It also prevents a lot of confirm-style windows from appearing; for example, you won't be asked to confirm if you want to buy back an expired chatroom."
            z "And you won't receive notifications like {b}You have 1 missed call{/b} on the home screen."
            z happy "This speeds up some of the most commonly done actions."
            show tut_dev_options at tutorial_anim(100)
            pause 0.5
            show tut_arrow:
                xpos 360
                ypos 575
            z neutral "If you want to jump right to a particular chatroom or Story Mode, for example, you can also toggle \"Unlock all story\"."
            z "This automatically makes all items on the timeline available to play and allows you to proceed through a plot branch even if you haven't played all the story items before it."
            z "Note that if you turn \"Unlock all story\" off on a save file where it was already activated, chatrooms and other story items will remain visible on the timeline screen,"
            z thinking "But you'll have to play through the items in order again and can't jump to later items before playing earlier ones."
            show tut_arrow:
                xpos 365
                ypos 612
            z neutral "There's also a toggle for \"Real-Time Mode\", which causes the game to run on real-time."
            z "So, story items will unlock based on the real-world time they are scheduled to be available at."
            hide tut_dev_options
            hide tut_arrow
            show tut_real_time at tutorial_anim(100)
            pause 0.5
            show tut_arrow_vert:
                rotate 90
                xpos 330
                ypos 800
            z "You can also purchase the next 24 hours' worth of content ahead of time at the bottom of the timeline screen on the most recent day."
            z happy "The program will remember to unlock items after a plot branch, too, if there's a plot branch in the middle of your 24 hours."
            hide tut_real_time
            hide tut_arrow_vert
            show tut_dev_options at tutorial_anim(100)
            pause 0.5
            show tut_arrow:
                xpos 342
                ypos 647
            z neutral "Next there's a toggle for \"Hacked Effect\", which will only work if you're not on the main menu."
            hide tut_dev_options
            hide tut_arrow
            show tut_hacking at tutorial_anim(100)
            z "It will change the music on the home screen and give the timeline items a \"glitchy\" overlay."
            z "Some effects will be disabled for players who have \"Hacking Effects\" turned off in Preferences."
            hide tut_hacking
            show tut_dev_options at tutorial_anim(100)
            pause 0.5
            show tut_arrow:
                xpos 575
                ypos 683
            z "Then there's \"Receive Hourglasses in Chatrooms\", which, if checked, will randomly award the player an hourglass for some lines of dialogue in chatrooms."
            z "If you're using Mysterious Messenger for a fanfic or for narrative purposes, you may want this option off."
            show tut_arrow:
                xpos 545
                ypos 720
            z happy "And finally, there's \"Use custom route select screen\"."
            z "There are more instructions on how to make your own route select screen in the wiki."
            z neutral "This will allow you to easily switch between your own routes and the built-in Tutorial Day."
            show tut_arrow:
                xpos 315
                ypos 800
            z thinking "There's also a button, \"Fix Persistent\"."
            z neutral "If you're having trouble with persistent values, but don't want to lose information like how many heart points you have and what gallery images you've unlocked, you can try using this button."
            hide tut_arrow
            hide tut_dev_options
            z "If you run into a major program issue though, don't hesitate to open an issue on the Mysterious Messenger GitHub or send a message in the Discord server."
            z happy "And that's all! Is there anything else you want to know about?"

        "That's all I wanted to know." (paraphrased=False):
            return
    jump extra_features_showcase

label bonus_pfp_showcase():
    $ shuffle = False
    menu (paraphrased=True):
        extend ''
        "Bonus profile pictures for me":
            m "Tell me about bonus profile pictures for me."
            z happy "When you click on your profile picture from the home screen,"
            z "You'll be taken to the Profile screen, where you can see some statistics like how many endings you've collected, and who you have heart points with."
            show tut_player_pfp2 at tutorial_anim(100)
            z neutral "You can also change your name, pronouns, and profile picture here."
            show tut_arrow:
                xpos 350
                ypos 580
            z "Just click your profile picture to bring up a screen with all the profile pictures you've unlocked for the game."
            hide tut_arrow
            hide tut_player_pfp2
            show tut_player_pfp at tutorial_anim(100)
            z "There are five default images, and as you play, you will also see the profile pictures and gallery images of other characters be added."
            z "If you're playing without Testing Mode turned on, unlocking a new profile picture to use will cost 1 hourglass."
            hide tut_player_pfp
            if not observing:
                if not persistent.animated_icons:
                    $ renpy.show_screen(allocate_notification_screen(),
                        message="Hourglass +1")
                else:
                    $ renpy.show_screen(allocate_hg_screen())
                $ renpy.music.play("audio/sfx/UI/select_4.mp3", channel='sound')
                $ collected_hg += 1
                z wink "I'll give you one now so you can try it out later~"
            z neutral "If you have Testing Mode turned on from the Developer settings, it won't cost you any hourglasses."
            z "You don't have to do anything to make sure profile pictures show up here;"
            z "If you show a CG in-game, or change a character's profile picture, it will automatically be available to use as a profile picture."
            play sound door_knock_sfx
            "(A knock at the door)"
            z surprised "Hmm? Someone's here?"
            play sound door_open_sfx
            "(The door opens)"
            show zen at vn_left with ease
            show seven front serious at vn_right with easeinright
            s "Zen! How could you forget to tell [them] about profile picture callbacks!"
            z "Huh? I was just getting to that..."
            hide zen
            show seven front happy at vn_center
            s "Hi, [name]!"
            s "I wanted to tell you about profile picture callbacks."
            s neutral "So, whenever you change your profile picture, a special callback function is called."
            s "It's passed some helpful arguments, like how long it's been since the player last changed their profile picture,"
            s "what the last profile picture was,"
            s "and who the current profile picture is associated with, if applicable."
            s "But, you can find all that in the wiki."
            s happy "The important part is you can use this to have the characters react when you change your profile picture!"
            s "You can have them send you a text message, change their spaceship thoughts, or even call you."
            s "The possibilities are nearly endless!"
            hide seven
            show zen side neutral at vn_left with easeinleft
            show seven side neutral at vn_right with easeinright
            z "It WOULD be nice if [name] changed [their] profile picture to a picture of me..."
            z wink "Who could resist this beautiful face, right?"
            s happy "I think [they]'ll have fun with it~"
            s "I should go. Toodles!"
            hide seven with easeoutright
            show zen happy at vn_midright with ease
            z "Whew, what an explanation. Is there anything else you wanted to know about?"

        "Bonus profile pictures for the characters":
            m "I want to know about bonus profile pictures for the characters."
            z happy "Sure!"
            z neutral "You can change the other characters' profile pictures in code to suit a particular chatroom or story beat,"
            z "But you can also use a \"bonus\" profile picture to change their profile picture at any time in-game."
            z "Gameplay-wise, this is considered a fun feature for the player rather than the character's actual profile picture at that moment in time."
            show tut_other_pfp1 at tutorial_anim(140, 0)
            z thinking "To change a character's profile picture, go to their profile on the home screen and click on their profile picture."
            z neutral "If you're playing without Testing Mode turned on, you'll see a grid of the images you've seen in-game, and likely some boxes with \"?\" in them for images you haven't yet seen."
            show tut_arrow:
                xpos 440
                ypos 925
            z "You can use heart points you've collected with that character to unlock their bonus profile pictures."
            hide tut_other_pfp1
            hide tut_arrow
            show tut_other_pfp2 at tutorial_anim(140, 0)
            extend ''
            hide tut_other_pfp2
            show tut_other_pfp3 at tutorial_anim(140, 0)
            show tut_arrow:
                rotate 180
                xpos 50
                ypos 460
            z "There is also an option to \"Revert to default\", which will revert to whatever the character's profile picture was set to in the code."
            z "If you have Testing Mode turned on from the Developer settings, all the profile pictures will be available, including ones you haven't seen in-game."
            hide tut_arrow
            hide tut_other_pfp3
            z happy "I hope you find it a useful feature!"
            z neutral "Is there anything else you wanted to know about?"
        "I want to know about something else." (paraphrased=False):
            z "Sure! What do you want to know?"
            jump extra_features_showcase

    jump bonus_pfp_showcase
