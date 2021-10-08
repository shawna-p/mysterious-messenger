
label example_email():
    $ z.prof_pic = 'Profile Pics/Zen/zen-6.webp'
    scene evening
    play music narcissistic_jazz

    z 'Hey, [name], I had an idea for a guest we should invite.'
    z 'Can we invite zentherainbowunicorn?'

    # This tells the program not to shuffle the last choice. You generally
    # will not use this.
    $ shuffle = "last"
    menu:
        "That sounds great!":
            invite rainbow # Use this to invite your guest
            z "Great! I'll tell them to send you a message."

        "I'll pass":
            z "Oh, okay. No problem!"

        # This is for testing; it both makes any emails you haven't
        # replied to timeout faster, and if you're waiting for the
        # guest to email you, it makes them reply more quickly.
        "I'd like to deliver my email replies more quickly." if email_list:
            z "Sure, I can take care of that."
            python:
                for email in email_list:
                    email.send_sooner()
            z "So what this does is decreases both the timeout countdown by 5,"
            z "And also decreases the number of chatrooms you need to go through to deliver the next email by 5."
            z "They'll decrease by an additional 1 when you exit this chatroom."
            z "In other words, guests will reply to you more quickly!"
    z "If you ever want to learn about inviting guests in the game,"
    z "there's a whole section on emails in the documentation."
    z "You can also look at {b}tutorial_2_emails.rpy{/b}"
    z "to see how this invitation works,"
    z "and {b}email_template.rpy{/b} has a template to make your own guests."
    z "Anyway, enjoy~!"

    exit chatroom z

    return

## This is the 'expired' version of the chatroom
label example_email_expired():
    $ z.prof_pic = 'Profile Pics/Zen/zen-6.webp'
    scene evening
    play music narcissistic_jazz
    z "Hey, [name], I had an idea for a guest we should invite."
    z "Oh... [they_re] not here."  (bounce=True, specBubble="sigh_m")
    z "Hmm."
    z "Well, you can always buy back this chatroom and let me know if you want to invite them or not!"
    z "I'll see you around~" (bounce=True, specBubble="flower_m")
    exit chatroom z
    return

## This is how you will set up guests for the party. A template can be found
## in email_template.rpy along with more detailed explanations of the fields.
default rainbow = Guest(
## Because the variable is 'rainbow', when you want to
## invite this person, you will write: invite rainbow

## The first string, "example", is what will show up in the
## email chain as the guest's 'email' e.g. "longcat" shows up
## as "@longcat" in the email chain.
"rainbow",

## The next string is the name of the guest as it should show up in the
## guestbook when they arrive at the party e.g. "Long Cat"
"Rainbow",

## This string is the image to use for the guest's
## thumbnail. It should be 155x155px
"Email/Thumbnails/rainbow_unicorn_guest_icon.webp",

## This string is the file path to the full-body image of this guest. It will
## be shown when they attend the party. It is a larger (usually chibi) image
## for the party, no wider than 315px.
"Email/Guest Images/rainbow_unicorn.webp",

## This next string is a short description of the guest, shown in the
## guestbook when they have been invited.
"Rainbow Unicorn, the creator of this program.",

## Personal Info section on the guest, shown in the guestbook after the
## guest has attended the party.
"Rainbow started working on this project back in 2018 and they're excited to share it with the world!",

## This is the beginning email that will be sent to the player after the guest
## is invited. It is usually easier to write this with triple quotes so you
## can incorporate line breaks. This text is parsed to remove leading whitespace
## and replace single newlines with a space, so you can indent the string
## for readability and keep it within the character limit.
"""Hi [name]!

Really excited to hear about this party you\'re holding! Can\'t wait to see
how things will turn out for you. Zen told me to make sure your inbox is
working, and well, if you\'re reading this, I guess it is! So that\'s good.

I did have one quick question though -- will the party be held inside or
outside? Please let me know as soon as possible!

Thanks,

Rainbow Unicorn""", # don't forget the comma after the quotes

## This differs from the previous way to define guests. Here, you will define
## the sequence of choices the player has to answer the guest.
[ EmailReply(
    ## An EmailReply object holds the information needed for an email message.
    ## The first argument is the text that will appear on the choice box when
    ## the player opts to answer the email.
    "Indoor Party",

    ## The next argument is the message that the player will send to the guest
    """Dear Rainbow,

    I\'m pleased to inform you that the party will be indoors. No need for
    umbrellas or sunscreen!

    Hope to see you there,

    [name], the party coordinator""", # Don't forget the comma

    ## And this is the reply the guest will send the player.
    """Hi again,

    Oh, how wonderful! I was worried about what the weather would be like
    on the day of the party. I thought of another question: what kind of
    music will there be at the party?

    Hope to hear from you soon,

    Rainbow Unicorn""", # Don't forget the comma

    ## Now, since this choice continues the chain, you will add another
    ## EmailReply object.
    [EmailReply(
        "Smooth Jazz",

        """Dear Rainbow,

        We\'ve got a wonderful playlist full of smooth jazz songs to
        play at the party. We\'re also looking into the possibility of
        a live band!

        Hope that answers your question.

        Sincerely,

        [name]""",

        """Dear [name],

        Oh, that\'s just fantastic news. Jazz is such a lovely music genre,
        isn\'t it? Just between the two of us, I\'m also quite partial to video
        game soundtrack music. But I don\'t expect you to play that at the party!

        You\'ve been so kind with your answers, and if you don\'t mind, I had
        one last question -- what sort of food will there be at the party?
        Please let me know when you can!

        From, Rainbow""",

        ## Once again, this is the good reply, so the chain continues
        [EmailReply(
            "Spicy food",

            """To the lovely Rainbow,

            There will be a delicious selection of spicy food at the party!
            In particular there will be experienced chefs from places such as
            India and Mexico who will be catering. I hope your taste buds
            are ready!

            Sincerely,

            [name]""",

            """To [name],

            Wow! I adore spicy foods; it\'s almost as though you read my mind!
            I will most certainly have to come and sample the dishes you\'ve
            described.

            Thank you very much for taking the time to answer my questions.
            I\'ll see you at the party!

            Best,

            Rainbow""",
            ## This is the end of this particular chain, so no more EmailReply.
            ## However, you need to indicate whether getting to this reply
            ## resulted in a successful email chain or a failed one.
            email_success=True
        ), # Don't forget a comma here if you want to add more choices
        ## This is another choice for the menu
        EmailReply(
            "Seafood",

            """To the lovely Rainbow,

            We\'re planning to serve a variety of seafood at the party! There
            will be plenty of dishes to try, like fried octopus, shrimp
            tempura, and caviar. Hope you come with an appetite!

            From,

            [name]""",

            """To [name],

            That certainly sounds... interesting! I can\'t really consider
            myself a fan of seafood, however, so you\'ll have to excuse me
            for my lack of enthusiasm.

            That said, I do appreciate you taking the time to answer me. I\'m
            a bit undecided on whether or not to attend, but wish you the
            best of luck with the preparations!

            Sincerely,

            Rainbow Unicorn""",
            ## This is the end of the email chain, but this was the incorrect
            ## reply, so indicate that.
            email_success=False
        )   # If you like, you can add a comma here and add another EmailReply
            # object to the list. However, this menu has two choices, so it
            # ends with a square bracket here to finish the list.
        ]
    ),
    ## This is a choice that will show up alongside the "Smooth Jazz" choice.
    ## Note the indentation of the list elements.
    EmailReply(
        "Heavy Metal",

        """Hi Rainbow,

        I\'ve found some wonderful heavy metal music to play at the party!
        Screaming vocals really set the mood, don\'t you think? I hope you\'ll
        enjoy the music!

        Sincerely,

        [name], the party coordinator""",

        """Hi again,

        Oh dear, heavy metal? I can\'t say I enjoy that sort of music. I
        appreciate the invitation, but now that I know you\'ll be playing
        heavy metal music... I\'ll have to think more on it.

        Thank you for your help.

        Rainbow""",

        ## This email also ends the chain, so it is set to False here
        email_success=False
    )]
),
## And this choice shows up alongside the "Indoor Party" choice.
EmailReply(
    "Outdoor party",

    """Dear Rainbow,

    We\'re planning for an outdoor party! There are gardens at the venue that
    will be perfect for an elegant party. Hope to see you there!

    Sincerely,

    [name], the party coordinator""",

    """Hi again,

    Oh dear, I\'m afraid I have terrible allergies and that may not work out
    well for me. I appreciate the time you\'ve taken to email me but I may have
    to decline.

    Thank you for the invitation, and best of luck to you and the party.

    Rainbow Unicorn""",

    email_success=False
)], # There's a comma here to continue adding information to the guest; the
# remaining fields are optional but recommended. They appear when the guest
# attends the party and when the player clicks on the guest's entry in the
# guestbook.

## The dialogue Rainbow says when arriving at the party.
"Oh, it's so exciting to be at the party! I can't wait to see everyone.",

## The ChatCharacter variable of the person who should talk about this
## guest in the long description in the guestbook.
z,

## What the previous character says about this guest.
"Is Rainbow's name a reference to me? Haha, well, I am quite a rainbow unicorn if I do say so myself~",

## The expression/displayable name of the character to show
"zen front party happy",

## This indicates the maximum number of emails the player can exchange with
## this guest. Getting every email correct will guarantee their presence at
## the party. By default this is 3 but you may change it here like so.
num_emails=3

) # Don't forget a closing bracket at the end
