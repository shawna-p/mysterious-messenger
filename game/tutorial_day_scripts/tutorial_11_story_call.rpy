# This is a special variable for this phone call, where the player
# might reveal their thoughts on cats.
default cat_feelings = None

label example_solo_story_call():
    # Story Calls are just like any other phone call. You can type dialogue
    # out as usual.
    ja "Hello, [name]. I hope I haven't found you at a bad time."
    # Menus in phone calls need the special caption `extend ''` to ensure the
    # last line of dialogue remains on-screen while the player makes a choice.
    menu:
        extend ''
        "No, not at all!":
            ja "Ah, that's good to hear."
        "I was going to do something, but then you called first.":
            ja "I see. I will try to keep this phone call short so you can get back to what you were doing."
    ja "How would you say you're enjoying the messenger so far?"
    menu:
        extend ''
        "It's good but it's confusing!":
            ja "That's understandable. There are many things to learn, after all."
        "I'm really liking it so far!":
            ja "I'm happy to hear that! The program has grown a lot since it first began."

    # This is monologue mode; it's particularly well-suited for phone calls
    # because there's no need to change expressions or speakers. Each line
    # will be treated as a new line of dialogue.
    ja """I heard that this program originally started just as an experiment, and wasn't intended to be a fully-fledged app at all.

    But now it's filled with many excellent features and new ways to interact with the messenger and other systems.

    Even me calling you now -- if you didn't pick up, I'd have left you a voicemail.

    You used to not have voicemail, so I had to wait for you to call me back.

    Mr. Han informed me that tomorrow he would like to bring Elizabeth to the office. I'm shuddering just to think at the amount of cat hair that will get all over things...

    I'd like to think she will be kept in a carrier, but I'm sure Mr. Han will want to let her out to roam around his office.

    Do you like cats, [name]? I don't know if I ever asked.

    """
    # You can add as many choices as you like to a menu.
    menu:
        extend ''
        "I have a pet cat.":
            # This sets a variable to remember that the player said they
            # own a cat.
            $ cat_feelings = "owns"
            ja "Oh, you do? I'm sure Mr. Han would be happy to talk to you about your cat."
        "I love cats!":
            # Similarly, this variable is used to remember what the player
            # said about cats.
            $ cat_feelings = "love"
            ja "You're like Mr. Han, then. He's had Elizabeth as long as I've known him."
            ja "Or perhaps you're more like Luciel. I know he is fond of cats, though I would not trust him to look after one."
        "I'm allergic to cats.":
            $ cat_feelings = "allergic"
            ja "I see. You're like Zen then. He can't be around a cat longer than a few seconds before he's sneezing."
            ja "I am not particularly fond of cats myself, but I'm glad they don't make me sneeze."
        "Cats are okay but I like dogs better.":
            $ cat_feelings = "prefer dogs"
            ja "Hmm, I can agree with that. Though I'm not particularly fond of pet fur so I don't think I would own one, myself."

    ja """Hmm? Mr. Kim? Oh, yes, of course.

    I'm sorry, [name], but I have to go. I hope you have a wonderful day.

    """
    menu:
        extend ''
        "You too, Jaehee!":
            pass
        "Have fun at work~":
            pass
    ja "Thank you. I will talk with you again later. Good-bye."
    return

## This is the label the program jumps to if the player misses this call from
## Jaehee. Like expired chatrooms, this is usually treated as a "missed call"
## and the caller will leave the player a voicemail instead.
label example_solo_story_call_expired():

    ja """Oh, I see you're not available. I had some free time at work and thought I would give you a call.

    I hope this message finds you well. The day has been passing very slowly at the office today.

    Mr. Han informed me that tomorrow he would like to bring Elizabeth to the office. I'm shuddering just to think at the amount of cat hair that will get all over things...

    I'd like to think she will be kept in a carrier, but I'm sure Mr. Han will want to let her out to roam around his office.

    Do you like cats, [name]? I don't know if I ever asked.

    Hmm? Mr. Kim? Oh, yes, of course.

    I should hang up. I hope we can speak again soon on the messenger.

    """

    return

## This is the after_ label for the example story call. It's called and used
## the same as after_ labels on chatrooms or Story Mode.
label after_example_solo_story_call():

    # You can also have text messages deliver at specific times, if the player
    # is playing in real-time. In this case, the story call is at 9:30, and the
    # next chatroom is at 11:28. If the player finishes the call at 10:00, this
    # text still won't be delivered until 10:42. If they finish the call at
    # 11:15, the text will be delivered immediately when it ends.
    if was_expired:
        # This text message will *only* be sent if the player did not
        # see the call before it expired and got the voicemail instead.
        compose text ja deliver_at 10:42:
            ja "I'm sorry I missed you when I called earlier."
            # This tells the program to wait two minutes (120 seconds) before
            # Jaehee sends the next part of her message. You can use it to
            # stagger message delivery times for added realism.
            pause 2*60
            ja "I hope we can speak again soon."
            # This text message does not have a reply label, so you cannot
            # reply to Jaehee, just read the message.

    else:
        # This text only shows up for a player who picked up Jaehee's call.
        # `deliver_at next_item` tells the program to deliver this text message
        # some time randomly after the next chatroom, but before the one after
        # that. So, it will be delivered after the 11:28 chatroom, but before
        # the 13:44 one.
        compose text ja deliver_at next_item:
            ja "I'm sorry I had to hang up so suddenly."
            ja "It was good to talk to you."
            # You can add conditional statements in here to modify what
            # Jaehee's next message is. Here, the program checks if the player
            # said they own or love cats.
            if cat_feelings in ['love', 'owns']:
                ja "I know you mentioned you like cats, so I apologize if I seemed disinterested."
                ja "I think cats make lovely pets for many people, though I do not want one myself."
            elif cat_feelings == "allergic":
                ja "It was interesting to learn that you're allergic to cats as well."
                ja "I hadn't realized it was such a common allergen."
            elif cat_feelings == "prefer dogs":
                ja "You mentioned you prefer dogs to cats."
                ja "Do you own a dog?"
                # This is the only case in which the player can reply.
                label ja_text_own_dog
            # You could add an 'else' here; the only reason the program would
            # *not* execute one of the above conditional statements however
            # is if the player is using Testing Mode and skipped the call.
    # Don't forget to end with `return`
    return

label ja_text_own_dog():
    menu:
        "I have a big dog for protection.":
            ja "Oh, that's understandable."
            ja "It can be nice to have a dog around, especially if you're living alone."
        "I have a small dog.":
            ja "Oh, I see."
        "I don't have a dog, but I want one.":
            ja "Perhaps one day you will be able to get one, then."
            ja "I always hear it's better to adopt from shelters if possible."
        "My dog's a total cuddle bug.":
            msg ja "{image=jaehee_happy}"
            ja "That sounds sweet."
        "I like dogs, but don't want to own one right now.":
            ja "It sounds like you've put some thought into it."
            ja "That's a sensible way of approaching things."
    ja "Well, I should return to work."
    ja "Thank you for talking with me."
    return


