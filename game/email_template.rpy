## ****************************************************
## A TEMPLATE EMAIL GUEST
## ****************************************************

default example_guest = Guest("example",
## The first string, "example", is what will show up in the
## email chain as the guest's 'email' e.g. "longcat" shows up
## as "@longcat" in the email chain. This is also the variable
## you use for reply labels, not the name of the variable
"Email/Thumbnails/guest_unlock_icon.webp",
## The second string is the image to use for the guest's
## thumbnail. It should be 155x155px
## Because the variable is 'example_guest', when you want to
## invite this person, you will write: invite example_guest

## Initial Message
"""Dear [name],

You can write whatever you want in here. It is the first message that is sent
to you after you invite the guest. Note that any new lines you write here will
be new lines in the actual email; you can look to the previous guest for ideas
on formatting. This example simply has breaks in the middle of lines to make
it easier to read when editing code.

From, your example guest""", # don't forget the comma after the quotes

## FIRST MESSAGE - *Question the guest asked here*

## It's a good idea to write down what the answer is to get to this response
## in the comments so you don't forget
## Answer -> CORRECT ANSWER HERE
## First Message (correct)

"""This is what your character will send the guest after selecting the correct
response to the email. You can use their name in the email by typing [name]""",

## Reply to correct message

"""This is what the guest will send you after you replied
to their first email correctly""",

## Answer -> INCORRECT ANSWER HERE
## First Message (incorrect)

"""This is what your character writes to the guest when they
choose the wrong response""",

## Reply to incorrect message

"""And this is the response the guest will write you after you choose
the incorrect response. Usually they say something that indicates they
don't want to go to the party""",

## SECOND MESSAGE - *Question the guest asked here*

## Answer -> CORRECT ANSWER HERE
## Second Message (correct)

"""This is your message to the guest with the correct response""",

## Reply to correct message

"""This is the guest's reply to your message after you choose the
correct response""",

## Answer -> INCORRECT ANSWER HERE
## Second Message (incorrect)

"""This is your message to the guest with the incorrect response""",

## Reply to incorrect message

"""This is the guest's reply to your message after you choose the
wrong response""",

## THIRD MESSAGE - *Question the guest asked here*

## Answer -> CORRECT ANSWER HERE
## Third Message (correct)

"""This is your message to the guest with the correct response""",

## Reply to correct message

"""This is the guest's reply to your message after you chose the
correct response. It usually says something about seeing you at
the party, as this is the final message""",

## Answer -> INCORRECT ANSWER HERE
## Third Message (incorrect)

"""This is your message to the guest with the incorrect response""",

## Reply to incorrect message

"""This is the guest's reply to your message after you choose
the wrong response."""

## These next fields are optional but used for the guestbook
## Large (usually chibi) image for the party, no wider than 315px
"Email/Guest Images/rainbow_unicorn.webp",

## Short description about the guest
"Example Guest, an example guest for this program.",

## Personal Info section on the guest
"Example Guest was made for users to better understand how to create a guest.",

## The ChatCharacter variable of the person who should talk about this
## guest in the long description
s,

## What the previous character says about this guest
"Here, the character from the last variable (Seven) will say this.",

## The expression/displayable name of the character to show
'seven front party happy',

## The name of the guest as it should appear in their
## dialogue box
"Example Guest",

## The dialogue the guest says when they attend the party
"The guest will probably mention something about the party."
) # Don't forget a closing bracket at the end

label example_reply1():
    # The guest is called "example", so the
    # reply labels will be called
    # example_reply1, example_reply2, and example_reply3

    menu:
        "Answer 1":
            # Passing 'True' indicates that this is the correct reply
            # Either answer can be correct, not necessarily the first option
            # The program will randomly shuffle the answers when showing
            # them to the user
            $ current_email.set_reply(True)

        "Answer 2":
            # Similarly, passing 'False' indicates this was the wrong reply
            # and will fail the email chain
            $ current_email.set_reply(False)

    jump email_end # This ensures your response is saved after you reply

label example_reply2():

    menu:
        "Answer 1":
            $ current_email.set_reply(True)

        "Answer 2":
            $ current_email.set_reply(False)

    jump email_end

label example_reply3():

    menu:
        "Answer 1":
            $ current_email.set_reply(True)

        "Answer 2":
            $ current_email.set_reply(False)

    jump email_end

