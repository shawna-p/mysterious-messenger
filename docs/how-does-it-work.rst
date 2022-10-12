.. _how-does-it-work:

======================
How does it all work?
======================

As Mysterious Messenger is the result of over 4 years of work (the past two of which have included daily updates), it now has a rather hefty amount of code, much of which is tailored to be easy-to-use from the front end. That can mean that it's hard to get your head around how it's doing all the "behind the scenes" stuff. This page is intended to walk you through some of the thought processes behind the various parts of Mysterious Messenger, and show examples of simplified versions of the classes and systems that make up the inner workings of the project.

.. toctree::
    :caption: Navigation

    how-does-it-work


The Chatrooms
===============

The fundamental parts of the chatrooms are built upon two classes: ``ChatCharacter`` and ``ChatEntry``.

ChatCharacter
-------------

The ChatCharacter class, as its name implies, holds information on the characters who speak in chatrooms. The most important information that they hold are things like the character's name and profile picture. ChatCharacters in this program hold a ton of additional information, too - they store how many heart points the player has with that character, their heart icon and speech bubble colours, their cover photos and status updates, and more.

That said, this class once started out in an extremely simplified form. Fundamentally, it looked like this::

    class ChatCharacter(object):
        """
        A class which holds information on a single character in the game
        for participating in chatrooms.

        Attributes:
        -----------
        name : string
            The name of the character, as it appears in a chatroom.
        profile_pic : Displayable
            The profile picture for this character.
        """

        def __init__(self, name, profile_pic):
            """
            Create a ChatCharacter object for use in chatrooms.
            """
            self.name = name
            self.profile_pic = profile_pic