================
Emails
================

.. toctree::
    :caption: Navigation

    emails


.. note::
    Example files to look at:

    * tutorial_2_emails.rpy
    * email_template.rpy

    *A brief overview of the steps required (more detail below):*

    #. Open **email_template.rpy** and copy-paste ``example_guest`` into a new file.
    #. Rename the guest and follow the instructions to fill out the various fields.


Writing an Email Chain
======================

Emails in this program have several additional features:

* You may have a varying number of emails in a chain (limited only by how many email icons will fit comfortably on the email button)
* You may have as as few as one or up to five responses available to answer
* Emails can have "branching paths"; simply answering one email incorrectly does not necessarily mean the whole email chain is failed.
* Guests are automatically added to the guestbook. Some information about them is unlocked when the player invites them to the party, and additional information is added after the guest has attended the party.
* Viewing a guest's information for the first time in the guestbook awards the player an hourglass.

The easiest way to get started writing an email is to copy the definition for ``example_guest`` inside **email_template.rpy** and modify it to your needs. The various fields are explained with comments in the file itself so you understand what information to give it. The newest feature is the use of ``EmailReply`` objects, which allow email chains a greater degree of flexibility. This is explained below.

    **EmailReply**\ (choice_text, player_msg, guest_reply, continue_chain=None, email_success=None)

    A class intended to facilitate writing email replies.

    `choice_text`
        A string. The text of the choice to reply to the email.
    `player_msg`
        A string. The message the player writes after the choice is made.
    `guest_reply`
        A string. The guest's reply to the player's message.
    `continue_chain`
        If this email chain will continue after the player selects this reply, this is a list of EmailReply objects that will be available the next time the player is given the opportunity to reply.
    `email_success`
        If explicitly set to a boolean value, this indicates if it ends the email chain in a good (True) or bad (False) way.


Both the ``player_msg`` and ``guest_reply`` fields use a special helper function called ``filter_whitespace``, which removes leading and trailing whitespace (mostly the "space" character) from the string and turns a single newline into a space. Double newlines are preserved.

In practice, this means you can use line breaks to keep your email messages readable inside your code editing program, and can use indentation to better show a chain of emails.

If you want to preserve single newlines exactly as written, there is a variable in ``variables_editable.rpy`` called ``email_newline_to_space``. By default, this value is ``True`` (aka it will convert single newlines to a space), but you can set it to ``False`` in order to have newlines remain exactly as written. Note that you'll need to start a new game in order to see changes in email display.

In order to have "branching paths" for emails, you must use the ``continue_chain`` field. The example below demonstrates how to write an email chain with three initial responses that each lead to a different second email::

    default longcat = Guest(
    "longcat",
    "Long Cat",
    "Email/Thumbnails/longcat.webp",
    "Email/Guest Images/longcat.webp",
    "Long Cat, the longest cat in the world.",
    "Meow? Mrrrow... meow meow.",
    """To [name]:

    Meow? Meow meow.

    From, Long Cat""",

    [ EmailReply(
        "There will be fish at the party",

        """Dear Long Cat,

        We will have fish at the party, meow!

        From, [name]""",

        """To [name]:

        Meow!!! Mew meowww. Mrow?

        From, Long Cat""",

        [ EmailReply(
            "Tuna fish",

            """Dear Long Cat,

            The fish will be tuna fish, meow!

            From, [name]""",

            """To [name]:

            Mrow... mew.

            From, Long Cat""",

            email_success=True

        ), EmailReply(
            "Salmon",

            """Dear Long Cat,

            We will have salmon available at the party, meow!

            From, [name]""",

            """To [name]:

            Meow!!! Mew meow mew.

            From, Long Cat""",

            email_success=True

        )]

    ), EmailReply(
        "Laser pointers",

        """Dear Long Cat,

        We will be giving out laser pointers to the guests at the party! I
        hope you find this a source of entertainment.

        From, [name]""",

        """To [name]:

        Hiss!!! Mrow... meow.

        From, Long Cat""",

        email_success=False,

        continue_chain=[ EmailReply(
            "No laser pointers",

            """Dear Long Cat,

            My apologies for the misunderstanding; there will no longer be laser
            pointers at the party. Hope to see you there!

            From, [name]""",

            """To [name]:

            Mew mew meow!

            From, Long Cat""",

            email_success=True

        ), EmailReply(
            "Yarn",

            """Dear Long Cat,

            Beside the laser pointers, we will also have plenty of yarn for your
            enjoyment. Hope to see you there!

            From, [name]""",

            """To [name]:

            Hisssss! Hiss!!!

            From, Long Cat""",

            email_success=False
        )]

    ), EmailReply(
        "Meow meow meow!",

        """Dear Long Cat,

        Meow! Mew mew mew, mrow, meow!

        From, [name]""",

        """To [name]:

        Purrrrrr.... meow.

        From, Long Cat""",

        email_success=True

    )],

    "Meow meow! Purr....",
    s,
    "Omg it's Long Cat!!! I need to find and pet them...",
    "seven front party happy",
    num_emails=2
    )

Though the example above is long, it functions as follows:

    First email:
        "There will be fish at the party" (correct)
            Second email:
                "Tuna fish" (correct)
                "Salmon" (correct)
        "Laser pointers" (wrong)
            Second email:
                "No laser pointers" (correct)
                "Yarn" (wrong)
        "Meow meow meow!" (correct)

Incorrect answers decrease the guest's odds of attending the party, while correct answers will increase the odds. A "perfect" email chain (one where ``num_emails`` emails are replied to correctly) will guarantee the guest's attendance at the party.

.. warning::
    As of Ren'Py v7.4.10, there continues to be a bug with how Ren'Py handles quotes within triple-quoted strings that causes emails to display oddly (usually without the whitespace preserved). To circumvent this, you can "escape" apostrophes and quotes (``'`` and ``"`` respectively) with a backslash ``\`` e.g.

    ::

        """Dear guest,

        Thanks for your concern. There isn\'t any need to bring your own beverages or \"wine\", as we will have refreshments at the party.

        Yours,

        [name]"""

    You can see that the apostrophe in ``isn't`` is escaped ``isn\'t`` as are the quotes around "wine" ``\"wine\"``.

Calculating if a Guest Will Attend
==================================

The program follows its own set of logic for determining if a guest will attend the party. A guest is **guaranteed** to attend the party when:

* The player has correctly answered ``num_emails`` with the guest
* The player has read the guest's final reply and the email is marked as Completed

A guest will **never** attend the party if:

* The player has not read the most recent email
* The email chain is not complete
* The player did not get any emails correct
* The email chain has timed out

If the player has read all the guest's emails and reached the end of an email chain with them, then the odds of the guest attending depend on how many emails the player got correct with them. In the Long Cat example above, if the player answers "There will be fish at the party" -> "Tuna fish" or "There will be fish at the party" -> "Salmon", then Long Cat is guaranteed to attend the party.

If the player answers "Laser pointers" -> "Yarn" then the email chain will be failed and Long Cat will not attend the party.

If the player answers "Laser pointers" -> "No laser pointers", then Long Cat will have a 50% (1/2) chance of attending the party.

If the player answers "Meow meow meow!" then Long Cat will have a 50% chance of attending the party, even though there are no further emails, since ``num_emails`` is 2 and the player only got 1 answer correct.

The odds of a guest attending the party are calculated after the email is answered. In other words, if a guest has a 50% chance of attending the party, reloading a save just before playing the party will not change whether they attend or not.

A guest will be unlocked in the guest book as soon as the player invites them to the party, but further information will only be unlocked if the guest actually attends the party.

Checking in-game if a Guest Will Attend
----------------------------------------

Once an email chain is completed, you can check whether or not a particular guest is attending via the ``attending`` field e.g.

::

    if rainbow.attending:
        ja "It's so good to see Rainbow here!"


Inviting a Guest
================

After defining your guest, you can invite them to the party using the line::

    invite your_guest

where ``your_guest`` is the variable you made when defining the guest using

::

    default your_guest = Guest(...)

.. tip::
    You can also use ``call invite(your_guest)`` to invite a guest.

After the player finishes the timeline item where the guest was invited, they will receive the first email from the guest.

How Emails are Sent
===================

After the guest is invited to the party, the player will receive an initial email from them. From that point onwards, if the player **does not** reply to the email, after every timeline item a variable attached to every Email object called ``timeout`` will decrease by 1. By default, ``timeout`` begins at 25.

The timeout counter will reset to 25 as soon as the player replies to the email. However, if the timer reaches 0 (aka the player has gone through 25+ timeline items since they first received the email), the email will be considered **timed out** and can no longer be replied to.

Once the player replies to the email, the program calculates when it should send the guest's reply based on how many timeline items remain in the route. For example, if there are 20 remaining timeline items on the route and 2 remaining emails in the chain, then the maximum number of timeline items the program will wait before delivering an email reply is ``20 / 2 = 10``. The minimum number of timeline items it will wait is 1 or ``10 - 7 = 3``, whichever is larger -- in this case, 3.


The Guestbook
===============

There are several fields when defining a Guest which correspond to text which will appear in the guestbook. These are:

`comment_who`
    The ChatCharacter object of the character who will talk about this guest in the guestbook.

    e.g. ``s``

`comment_what`
    What the above character will say about the guest.

    e.g. "I can't believe I got to meet Long Cat!"

`comment_img`
    A string that corresponds to a defined image or layeredimage attributes to display the sprite of the character who is talking about the guest.

    e.g. "seven front party happy"

The player will also receive 1 hourglass the first time they view a guest's entry in the guestbook after successfully inviting them to the party. The ``short_desc`` field's contents are shown to the player in the guestbook after they first invite the guest, and the ``personal_info`` field is revealed in the guestbook only after the guest has successfully attended the party.


Testing Emails
===============

While you are writing a route, you might want to test email chains and party comments without going through the whole game just to invite the guest. To do that, load up a save file and then click the Developer button from the home screen. Next, click on **Test Emails**.

Here you will find a list of all the guests the game could find to invite. Simply click the guest's name to invite them to the party. Some other buttons are available at the bottom of the screen:

`Force email replies`
    Causes all undelivered emails to be delivered at once. (For example, if you sent a reply to a guest, then clicking **Force email replies** would immediately deliver the guest's response to your inbox).

`Invite all guests`
    Invites every possible guest. All their emails will appear in your inbox. Note that it is possible to invite the same guest more than once with this method.

`Start Party`
    Begins the guest showcase part of the party. Guests only attend if their email chains have been successfully completed as described in :ref:`Calculating if a Guest Will Attend`.

`Indicate correct answers`
    If turned on, the "correct" email answer will be have a checkmark in the corner when replying to emails.

