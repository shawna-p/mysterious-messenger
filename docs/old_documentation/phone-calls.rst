.. _phone-calls:

===========
Phone Calls
===========

.. toctree::
    :caption: Navigation

    phone-calls


Creating a Regular Phone Call
=============================

.. note::
    Example files to look at:

    * tutorial_5_coffee.rpy
    * tutorial_11_story_call.rpy

    *A brief overview of the steps required (more detail below):*

    #. Create a label + the correct suffix for the phone call.
        #. ``my_label_outgoing_ja`` to make an outgoing call to the character ``ja`` available.
        #. ``my_label_incoming_ja`` to trigger an incoming call from the character ``ja`` after the corresponding timeline item has been played.
        #. ``my_label_story_call_ja`` to create a required Story Call after this timeline item from the character ``ja``.
    #. Write the phone call dialogue.
    #. End the phone call with ``return``

Phone calls that are tied to a particular timeline item follow a specific naming convention so the program can find them and make them available to the player. If you have a timeline item (i.e. a chatroom, Story Mode section, or Story Call) titled

::

    label day_1_4:

then an **incoming** call should be named::

    label day_1_4_incoming_z:

an **outgoing** call should be named::

    label day_1_4_outgoing_z:

and an attached Story Call should be named::

    label day_1_4_story_call_z:

where ``z`` is the variable of the character whom the player is calling or who is calling the player (see [[INSERT LINK HERE]] for a list of the existing characters).

The following section will cover **incoming** and **outgoing** calls to characters that are optional for continuing with the story. You can find more information on Story Calls at [[INSERT LINK HERE]].

Incoming Calls
--------------

Once the player is done playing through a timeline item, the program will automatically make any calls associated with that timeline item (through the naming convention mentioned above) available. If the program finds an **incoming call** label, then when the player finishes the timeline item they will receive an incoming call from the associated character. They have ten seconds to pick the phone call up, or they can reject the call and phone the character back later.

.. note::
    There can only be one incoming phone call after a given timeline item. However, it is possible to have both an incoming call after a chatroom as well as a different incoming call after an attached Story Mode.

**If the player rejects the incoming call** or lets the timer run out without answering it, it acts like an **outgoing** call and the player can phone the character back. The player can typically play one additional timeline item before the phone call "expires" and they cannot call the character back to receive that conversation.

Outgoing Calls
--------------

Once a player finishes playing through an item that has associated outgoing calls (linked through the naming conventions mentioned above), all the associated outgoing calls will be made available. The player must then click on the characters in their Contacts list or use the redial button next to a past phone call on the History tab to call the character.

An outgoing call is typically available immediately after its associated timeline item and for one additional timeline item following when it became available, after which it will "expire" and the player will be unable to view that conversation by calling the character.

.. note::
    There can be up to one outgoing call per character available after each timeline item. If a player misses an incoming call from a character who also has an outgoing call, both conversations will be added to the pool of available calls. The player can then call the character back multiple times to receive both conversations.

Missed Calls
------------

If the timer on an incoming phone call runs out, the phone call will be marked as "missed" and moved to the pool of available calls. The player can then call the character back to receive that conversation.

Phone calls can also be missed if real-time mode is turned on from the Developer settings. If an incoming call is scheduled to occur after a chatroom at 10:20 and the player opens the game after a new chatroom became available at 13:30, then they will receive a notification of a missed call at 13:30 (just before the new chatroom). If not too much time has passed since the missed call, they can then phone the character back to receive that conversation.

Additionally, if the player is using the game but has not yet played the 10:20 chatroom by 13:30, then if the game is open at 13:30 they will receive an incoming call which they can either accept or reject. This acts the same way as if the incoming call had been received immediately after playing the chatroom.


Writing a Phone Call
====================

Phone call dialogue uses the regular character variables and doesn't have any special arguments such as ``(img=True)`` or special fonts. Just use the character variable and write out dialogue in quotations e.g.

::

    label day_1_4_incoming_z:
        z "Hi, [name]! This is phone call dialogue."
        z "You write it like this."
        return


Phone call labels end with ``return`` like all other labels.

You may also find Ren'Py's "monologue mode" helpful, since you won't be switching between expressions or different speakers very often. See [[INSERT LINK HERE]] for an example of this.


Providing Choices
=================

Menus for phone calls are written very similarly to menus in other parts of the game::

    menu:
        extend ''
        "I love cats.":
            ju "I do as well."
        "I like dogs better.":
            ju "Hmm. I will respectfully disagree with your opinion."

The only notable difference is that you should include the line ``extend ''`` right after the ``menu:`` statement and before the first choice. This will keep the dialogue said just before the menu on-screen while the choices are visible.

This menu, like others, also takes a ``paraphrased`` argument for either the menu as a whole or for an individual choice. For more information, see [[INSERT LINK HERE]].

Note also that if you are writing out the main character's dialogue directly after a choice, the first line **does not** require a ``(pauseVal=0)`` clause.
