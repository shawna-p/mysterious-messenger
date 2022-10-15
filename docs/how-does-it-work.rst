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

Basically, the class needs to hold information so the characters can be displayed in chatrooms. Boiled down to only the essentials, that means it needs a name field and a profile picture field, since both of those get displayed on the chatroom screens.

The next piece of the puzzle that makes the class work is the special ``__call__`` method. This is a special Python method which is invoked when a class object is executed as if it's a function.

That sounds kind of confusing, but let me rephrase. When you call a function in Python, that looks like this::

    # The function declaration
    def my_function(x):
        return x+1

    # Now to call the function
    y = my_function(3)

The important part is the ```my_function(3)`` bit. To call the function, you use the function's name (``my_function``) and then a set of parentheses, which may or may not contain arguments that get passed to the function (in this case, ``3`` is passed to the function).

Importantly, you can use an object in place of the function name, and that will cause the ``__call__`` method to be executed. So if you had the following::

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

        def __call__(self, x):
            return x+1

Then you could recreate the example from above with::

    # Declare a ChatCharacter object
    em = ChatCharacter("Emma", "Profile Pics/Emma-1.webp")

    # Call the ChatCharacter object as if it was a function
    # to invoke __call__
    y = em(3)

This has the same effect of setting ``y`` to ``4`` as earlier. ``em(3)`` invokes the ChatCharacter's ``__call__`` method, which takes the supplied argument ``x``, adds 1 to it, and returns the result.

Of course, adding 1 to the provided argument doesn't really do much to progress us towards having a functioning chatroom. So, how can you repurpose this?

Well, crucially, the ``__call__`` method is exactly how Ren'Py allows you to write character dialogue in-game. Usually a character is declared with a line like ``define e = Character("Eileen")``, which sets up ``e`` as an object of a class called ``ADVCharacter`` (this is because ``Character`` is technically a function, not a class itself, and there are actually two separate classes, ``ADVCharacter`` and ``NVLCharacter`` which are used depending on whether the character is ``kind=nvl`` or not - but, that's kind of off-topic, and not really important to this overview). Then you can write dialogue like ``e "This is some dialogue!"``.

The same thing goes here. We want to be able to use the ChatCharacter to write dialogue like ``em "Some dialogue."`` so it's easy to read and modify the script. Luckily, if you define a ``__call__`` method, you can actually benefit off of Ren'Py's scripting system and do just that. But, we have to handle the dialogue!

So, what does a proper ``ChatCharacter`` ``__call__`` method definition look like?

::

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

        def __call__(self, what, **kwargs):
            # Do something here?

Let's not get too ahead of ourselves. First, you need to think about what kind of information you need. In the simplest case, you'll only need the dialogue itself - that is, in a line like ``em "Hello there!"``, the ``"Hello there!"`` is an argument that's passed to ``__call__`` for you to parse. In the ``__call__`` method above, I called that argument ``what``, piggybacking off of what Ren'Py uses for things like the ``say`` screen.

There's also a mysterious additional argument, ``**kwargs``. This is a special Python convention which means that the ``__call__`` method can take any number of *keyword arguments*. This is important because when you piggyback off of Ren'Py's built-in scripting systems, it wants to pass in a special keyword argument called ``interact``. ``interact`` is almost always True by default, meaning that the game will wait for the player to interact with it in some way before proceeding with the next line. Since you won't be handling dialogue the way Ren'Py does, you don't directly need this argument, but you *do* still have to be prepared for Ren'Py to automatically pass it along (and you'll get an error if you don't include this).

Fundamentally, all you're doing here is looking for one argument to be passed, which will be the dialogue. We'll store that dialogue in a parameter called ``what``.

And now we have to take a detour to look at the second essential piece to this puzzle, the ``ChatEntry`` class, since we can't finish writing the ``__call__`` method without it.

ChatEntry
----------

The ``ChatEntry`` class is designed to hold the information on a single message that makes up a chatroom. A chatroom is actually just a list of ``ChatEntry`` objects.

Once again, though the actual ``ChatEntry`` class is quite complex, let's look at the bare essentials of the class. As with the ``ChatCharacter`` class, the only information we really need to store for a message is 1) who sent it, and 2) what they sent (the message). So, with that in mind, here is a pared-down version of the ChatEntry class::

    class ChatEntry(object):
        """
        A class which holds information on a single message in the game
        as part of a chatroom.

        Attributes:
        -----------
        who : ChatCharacter
            The character who sent the message.
        what : string
            The contents of the message.
        """

        def __init__(self, who, what):
            """
            Create a ChatEntry object for use in chatrooms.
            """
            self.who = who
            self.what = what

This looks similar to the ``ChatCharacter`` class in some ways - both take in a couple of parameters and store them as object fields. The two fields we're storing are called ``who`` - again, borrowing from Ren'Py's ``say`` system implementation. This is the person who sent the message. Note that it isn't just a string - it's a ``ChatCharacter`` object. This is important because the message will need to access the properties of the ``ChatCharacter`` object in order to display properly, namely, the profile picture and name fields. In theory, you could pass this information off individually to the ChatEntry, but it's much easier and more concise to just pass the whole ChatCharacter.

The second field is the ``what`` field which, as mentioned, borrows from Ren'Py's convention of using ``who`` and ``what`` in the say screen and in other internal functions. This is just the dialogue, or the text contents of the message.

With that, we have all the tools we need to start putting together an actual chatroom.
