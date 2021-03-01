====================
Introduction
====================

Welcome to Mysterious Messenger, a messenger game created in Ren'Py. This guide was created to help users understand how the program works together, and how to take advantage of the various functions.

This guide is best used by navigating to the sections with the information you need as you need it rather than reading it from start-to-finish. Most sections have a line at the top that says "Example files to look at"; these will usually show the features described in the guide in action in the program itself. As much as possible, the code has been annotated to help you understand what's happening in the program. Additionally, you'll find plenty of code excerpts in this guide itself. They look like this::

    label day_1_chatroom_1():
        scene earlyMorn
        play music mystic_chat
        enter chatroom u

        u "Congratulations! You've created your first chatroom."

        menu:
            "That's amazing!":
                u "Isn't it? I'm glad you think so."
            "This is a lot of work.":
                u "I'm sure it will get easier with practice!"
                u "There are plenty of wiki pages to help you out, too."

        u "I'm leaving now. Good luck!"
        exit chatroom u
        return

Most of these code excerpts are taken directly from the program itself and can be copied in to use for your own test purposes.

Some sections will also have a "quick-start" guide at the beginning; they look like this:

.. note::
    Example files to look at:

    * tutorial_5_coffee.rpy
    * tutorial_6_meeting.rpy

    *A brief overview of the steps required (more detail below):*

    #. Create a new ``.rpy`` file (Optional, but recommended)
    #. Create a new label for the chatroom.
    #. Set the background with ``scene morning`` where ``morning`` is replaced by whatever time of day/background you want to use.
    #. Add background music with ``play music mystic_chat`` where ``mystic_chat`` is replaced by the desired music variable.
    #. Write the chatroom dialogue.

        #. You may want to use either ``Script Generator.xlsx`` or the ``msg`` CDS.

    #. End the label with ``return``.

If you just need a quick reminder of what to do to get some code up and running, you can refer to this. If you need more detail, however, the rest of that section will explain further.

If you haven't already, you should also play through the Tutorial Day in the program at least once to get a feel for what the program is capable of. Then, if you're new to Ren'Py and/or to programming, you should take a look at the :ref:`Beginner's Guide`, which will take you through the steps to make the first chatroom of a new route playable.
