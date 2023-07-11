.. _how-does-it-work:

======================
How does it all work?
======================

As Mysterious Messenger is the result of over 5 years of work (the past three of which have included daily updates), it now has a rather hefty amount of code, much of which is tailored to be easy-to-use from the front end. That can mean that it's hard to get your head around how it's doing all the "behind the scenes" stuff. This page is intended to walk you through some of the thought processes behind the various parts of Mysterious Messenger, and show examples of simplified versions of the classes and systems that make up the inner workings of the project.

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

The important part is the ``my_function(3)`` bit. To call the function, you use the function's name (``my_function``) and then a set of parentheses, which may or may not contain arguments that get passed to the function (in this case, ``3`` is passed to the function).

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

With that, we have the main tools we need to start putting together an actual chatroom. The only remaining pieces are the actual display of the messages, and how we store messages so we can display them on the screen.

Let's tackle that last one. For Mysterious Messenger, chatrooms are simply a series of ``ChatEntry`` objects in a list. The list is called ``chatlog``. Armed with that knowledge, we can fill out more of the missing ``__call__`` method for the ``ChatCharacter`` class::

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
            global chatlog

            chatlog.append(ChatEntry(self, what))


There are only two new lines, so we'll look at each one in turn. First, ``global chatlog``. This is because ``chatlog`` is a variable that's defined outside of the ChatCharacter class, so you need to tell Ren'Py where to find it. The variable itself is set up with the line ``default chatlog = [ ]`` elsewhere.

The second line is ``chatlog.append(ChatEntry(self, what))``, which is made up of two parts. First, ``ChatEntry(self, what)``. This creates a ``ChatEntry`` object, which as described earlier, holds information on a particular message. If you recall, the ``ChatEntry`` constructor takes two parameters, ``who`` and ``what``. The ``who`` in this case is the ChatCharacter who's sending the message, which is the ``self`` parameter. If you're not familiar with classes, ``self`` basically just refers to the object itself. If you had ``default em = ChatCharacter("Emma", "Profile Pics/Emma-1.webp")``, then it's like passing ``ChatEntry(em, what)`` if it's the ``__call__`` method of ``em`` that's being called. The second parameter, ``what``, is of course the dialogue of the message.

The second part is ``chatlog.append``. This appends a new item to our list, ``chatlog``. In this case, the item we are appending is a ``ChatEntry``, namely, ``ChatEntry(self, what)``. As a result, we will end up with a list of ``ChatEntry`` objects, each of which holds the sender of a message and the contents of said message.


Displaying the Chatrooms
-------------------------

Now that we have a method of writing dialogue and obtaining a list of messages in a chatroom, we can move on to displaying those messages. Again, Mysterious Messenger has a whole lot of features and other things it uses to display emojis, clickable CGs, links, and other features, but we'll simplify as much of that as possible here to keep it simple.

I won't be going into too much depth on each of the screen language elements I'm using here, as that's best left to a different tutorial. I'll briefly comment on my choices where relevant.

So, to start, let's construct an extremely simple screen::

    screen messenger():

        viewport:
            mousewheel True draggable True
            yinitial 1.0
            has vbox

            for msg in chatlog:
                hbox:
                    add msg.who.profile_pic
                    vbox:
                        text msg.who.name
                        text msg.what

I'll briefly go over what each of these pieces are. First, there's the ``viewport``. This is a scrollable area on the screen that we'll put all the messages into. You need to tell Ren'Py how its contents can be scrolled, so that's what ``mousewheel True`` and ``draggable True`` do - it should be able to be scrolled with the mouse scroll wheel, and clicked and dragged (or tapped and dragged on touch screen devices), so those are set to True.

Next, ``yinitial 1.0``. There's another piece of this puzzle that this code is missing, but to start, this means that when the messenger screen is shown, the viewport will start scrolled to the bottom. This is important, because we want to basically always be at the very bottom of the viewport so we can see new messages.

``has vbox`` is a special way of saying the viewport's children will be laid out top-to-bottom, one on top of the other (like a messenger). You could also do ``vbox:`` and indent the rest of the code one level over, but this just keeps it a little cleaner and saves us one level of indentation.

``for msg in chatlog`` is a Python loop. This will loop over every item in the provided list, ``chatlog``. Each loop, the current message the loop is looking at is stored in ``msg`` (which is an arbitrary and temporary variable name I selected; this could've easily been ``for entry in chatlog:`` or ``for chat_message in chatlog``, for example).

Now we get into the nitty-gritty of displaying the actual chat messages. A pretty typical setup is to have the character's profile picture on the left, and then to the right of the profile picture, there's the person's name on top of the text of their message. But, how do each of those parts work?

The ``hbox`` is there to arrange the items from left-to-right beside each other. The first item is ``add msg.who.profile_pic``, which adds the profile picture to the hbox. This works because if you recall, ``msg`` is equal to a ``ChatEntry`` object that's part of the ``chatlog`` list. A ``ChatEntry`` has a ``who`` field, which is the ``ChatCharacter`` object of the person sending the message. And a ``ChatCharacter`` object has a ``profile_pic`` field, which contains their profile picture. So, ``add msg.who.profile_pic`` adds the profile picture of the person who sent the message.

Then beside the profile picture there is a ``vbox``, which organizes its children by stacking them from top-to-bottom as mentioned. In this case, the top item is ``text msg.who.name``, which adds the sender's name, and the bottom item is ``text msg.what``, which adds the text of the message itself.

With all that, in a fresh project, you should be able to write something like::

    define e = ChatCharacter("Eileen", "gui/window_icon.png")
    label start():
        show screen messenger
        e "This is some test dialogue!"
        e "The whole thing hasn't been put together quite yet, though."
        e "Stay tuned for the rest!"
        pause
        return

and you'll see the barebones version of the messenger system forming. Notably, all messages will just get added instantly to the chatlog; this is because there isn't any particular logic telling it to wait between messages yet. It also doesn't automatically scroll to the bottom when new messages arrive, which we'll fix later as well.

Pausing between messages
------------------------

In most cases, you'll want to simulate the characters typing/reading before they post a message so chatrooms aren't just a slew of instantly-sent messages. In Mysterious Messenger, there's a lot of other logic going on in each message, so I use a helper function, ``addchat``, to help with the calculations and other work. However, for a simplified version, it can go right into the ``__call__`` method from before::

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
            global chatlog

            # Calculate a rough time estimate for how long before
            # posting this message
            # Let's assume each word has 6 characters (letters) and they
            # are typing at a brisk 100wpm
            # This formula becomes num_characters/6 characters per word
            # = # of words / 100wpm = number of minutes to type
            # *60 = # of seconds to type
            wait_time = len(what)/6.0/100.0*60.0

            # Now wait for that number of seconds
            renpy.pause(wait_time)

            # *Now* add the message
            chatlog.append(ChatEntry(self, what))

The new lines here are ``wait_time = len(what)/6.0/100.0*60.0`` and ``renpy.pause(wait_time)``. The first line calculates a time to wait for before posting a message to the chatlog. The second actually waits for that number of seconds. Note that ``len(what)`` is the number of characters in the message - so, "Hello!" is 6 characters long, and according to the formula, would take 0.6 seconds to post.

.. tip::

    The actual wait times can be much more involved, and include calculations on more than just the length of the current message. For example, you might consider looking at the current chatlog to see if the last message was posted by a different character, in which case perhaps they take a little extra time to send because they need to read the message first before they start to type. Mysterious Messenger uses a logarithmic curve to calculate how long a message takes to send, with very short messages taking a comparatively longer time than a linear function, and longer messages beginning to take similar amounts of time despite increasing length. Gameplay-wise, this prevents very short messages from feeling like they're being posted at lightning speed, and very long messages from feeling like they grind the chatroom speed to a halt.

    If you'd like to get creative, you might consider both reading and typing times, particularly if you have a way of tracking who is "typing" a message at any given moment.

Now when you run your script, there should be pauses between when each message gets posted to the chatlog. The last crucial piece of the puzzle is getting the viewport to stay at the bottom so it displays each new message. Let's look at that now::

    default messenger_yadjustment = ui.adjustment()
    screen messenger():

        viewport:
            mousewheel True draggable True
            yinitial 1.0
            yadjustment messenger_yadjustment
            has vbox

            for msg in chatlog:
                hbox:
                    add msg.who.profile_pic
                    vbox:
                        text msg.who.name
                        text msg.what

We'll also make a small adjustment to the ChatCharacter class's ``__call__`` method::

    def __call__(self, what, **kwargs):
        global chatlog, messenger_yadjustment

        # Calculate a rough time estimate for how long before
        # posting this message
        # Let's assume each word has 6 characters (letters) and they
        # are typing at a brisk 100wpm
        # This formula becomes num_characters/6 characters per word
        # = # of words / 100wpm = number of minutes to type
        # *60 = # of seconds to type
        wait_time = len(what)/6.0/100.0*60.0

        # Now wait for that number of seconds
        renpy.pause(wait_time)

        # *Now* add the message
        chatlog.append(ChatEntry(self, what))

        # Scroll to the bottom to see it
        messenger_yadjustment.value = float('inf')

There are plenty of things happening here. Let's look at the new additions one by one.

First, ``default messenger_yadjustment = ui.adjustment()``. This is one of the vanishingly rare cases where a ``ui.`` method is still relevant in modern Ren'Py (things like ``ui.timer``, ``ui.imagebutton`` etc are vastly outdated and replaced with their screen language counterparts like ``timer`` and ``imagebutton``). It creates a special "adjustment" object, which tracks the scroll value of the viewport it's associated with as well as its range. It's set up with ``default`` because it's going to change over time as we add to the viewport and as it scrolls down to the bottom, and in general we want to remember where that position is.

Second, inside the viewport, there's a new line ``yadjustment messenger_yadjustment``. This assigns the value we made above to the chatroom viewport, so it tracks the scroll value of the chatroom viewport.

Lastly, inside the ChatCharacter ``__call__`` method, there's the line ``messenger_yadjustment.value = float('inf')``. Note also that ``messenger_yadjustment`` has been imported via ``global`` at the top of the method alongside ``chatlog``. This line sets the **value** of the adjustment object we made to infinity. The two main values an adjustment object tracks is the viewport **range**, which is the total space that can be scrolled in the viewport, and its current **value**, which is where the viewport is currently scrolled to. For the messenger system, this should always be the maximum possible value so that it stays at the bottom of the viewport to see the new messages. This is the most quick-and-dirty way to get the viewport to stay scrolled to the bottom, but it does have the drawback that every time a new message is posted to the chat (and thus the ``__call__`` method is executed, setting the viewport adjustment to infinity), it will scroll to the bottom of the screen, including in the case that the player is trying to backread the messages while new messages are being posted. For more elegant solutions that only jump to the bottom of the viewport if the user has scrolled suitably close to the bottom of the viewport, you can compare ``messenger_yadjustment.value`` with ``yadjustment.range`` to see if they're "close enough" to justify setting it to infinity to view a new message at the bottom of the screen.

Next Steps
-----------

Now almost all of the pieces are in place. There will be pauses before adding each message to the screen, the viewport will stay scrolled to the bottom, and you have a simple way of writing dialogue for chatrooms. What are some of the next steps?

First, you will probably want to adjust the styling on the messenger screen so messages have backgrounds of some kind. The easiest way to do this is to put ``text msg.what`` inside a ``frame`` which has an expandable background (generally you define those with ``Frame`` - note the capital F, it's different from the screen element ``frame``). If you don't give the frame a set xysize (e.g. ``xysize (None, None)``) then the frame will only be as large as it needs to be to contain the text. For your typical messenger, you should give the frame an ``xmaximum`` so the text doesn't spill over past the edge of the screen, but you should make sure ``xsize`` and ``ysize`` are ``None``, as mentioned.

As mentioned earlier, you may also want to adjust the line ``messenger_yadjustment.value = float('inf')`` to take into account the current scroll position so the game is not constantly scrolling to the bottom even when the player has scrolled back to view past messages. Mysterious Messenger solves this both by checking how close the player is to the bottom of the viewport and also by ensuring new messages don't remove old ones while the player isn't at the bottom of the viewport (see below).

For long chatrooms, it's a good idea to restrict how many messages appear on-screen at once to avoid taking up too much memory. You can do this with list splicing. The simplest version looks like ``for msg in chatlog[-20:]:`` to only show the 20 most recent messages, for example. Mysterious Messenger uses a variable for this value so the player can adjust it to their liking, and so it can prevent new messages from removing old ones while the player isn't at the bottom of the viewport.

Finally, you can work on added complexity, like adding CGs, stickers (emojis), special speech bubbles, different fonts, animations, etc. My tip for you is that if you *can* add something to the ChatCharacter or ChatEntry class, you should generally do so to help with code readability and organization. For example, 90% of the messenger styles are properties of the ChatEntry class, so an entry can just query the specific property it needs to get the right styling for things like left-aligned messages vs right-aligned ones. Similarly, characters "own" their own speech bubble images and heart icon colours.

