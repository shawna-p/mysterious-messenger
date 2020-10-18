label example_solo_story_call():
    # Story Calls are just like any other phone call. You can type dialogue
    # out as usual.
    ja "Hello, [name]. I hope I haven't found you at a bad time."
    # Menus don't need a `call answer` before them, and they should have the
    # special caption `extend ''` to ensure the last line of dialogue remains
    # on-screen while the player makes a choice.
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
        "I love cats!":
            ja "You're like Mr. Han, then. He's had Elizabeth as long as I've known him."
            ja "Or perhaps you're more like Luciel. I know he is fond of cats, though I would not trust him to look after one."
        "I have a pet cat.":
            ja "Oh, you do? I'm sure Mr. Han would be happy to talk to you about your cat."
        "I'm allergic to cats.":
            ja "I see. You're like Zen then. He can't be around a cat longer than a few seconds before he's sneezing."
            ja "I am not particularly fond of cats myself, but I'm glad they don't make me sneeze."
        "Cats are okay but I like dogs better.":
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