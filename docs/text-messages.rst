=============
Text Messages
=============

.. toctree::
    :caption: Navigation

    text-Messages

There are two kinds of text messaging styles available in this program. The first, referred to as "regular text messages", delivers text messages in "chunks" which the player can reply to whenever they like. The second style, called "real-time text conversations", plays out similar to a one-on-one chatroom. The player receives an initial text message, and upon opening the text conversation, cannot leave until the conversation is over or the player chooses to end it themselves.

Regular Text Messages
=====================

.. note::
    Example files to look at:

    * tutorial_3_text_message.rpy
    * tutorial_3b_VN.rpy
    * tutorial_5_coffee.rpy
    * tutorial_11_story_call.rpy

    *A brief overview of the steps required (more detail below):*

    #. Create a label using the prefix ``after_`` + the name of the timeline item you want to send the text messages after e.g. ``label after_day_1_4``
    #. Write ``compose text z:`` where ``z`` is the variable for the character who is sending the message.
        #. Optionally, you can also include arguments to tell the program when to deliver the message. Acceptable options are ``deliver_at 00:00`` where ``00:00`` is the time to deliver the message at, in 24-hour time; ``deliver_at random`` to deliver the message randomly before the next timeline item, or ``deliver_at next_item`` to deliver the message sometime between the next timeline item being available and the one after that.
    #. Write dialogue for the conversation, indented at least one level to the right underneath the ``compose_text`` line. You may also include conditionals here.
        #. You can also include the ``pause`` statement with a number of seconds to pause for, e.g. ``pause 2.0*60``. The message delivery will be "staggered", with the message after the pause waiting the given number of seconds before sending.
    #. (Optional) Include a label at the end which will be jumped to to continue the conversation e.g. ``label menu1``
    #. End the ``after_`` label with a return.
    #. (Optional) Create the label the player can jump to to continue the conversation.
        #. (Optional) Allow the player to reply to the text message again by writing ``$ s.text_label = "menu2"`` where ``s`` is the variable for the character sending the message and ``"menu2"`` is the name of the label to jump to to continue the conversation.
    #. Finish the reply label with ``return``


Sending a Text Message
----------------------

To have a character text the player after a chatroom, the program looks for a label with a special naming convention. For example, if your chatroom is called

::
    label my_chatroom:

then you should create a label called

::

    label after_my_chatroom:

Next, inside the ``after_`` label, use the special ``compose text`` CDS::

    compose text s:

where ``s`` is the variable for the character who is sending the message. You can then write dialogue the same way as you would for a chatroom, including adding CGs, emojis, and changing fonts. Text messages currently do not support special speech bubbles. You can use either the spreadsheet style or the ``msg`` CDS [[INSERT LINK HERE]]. Note that all dialogue for a text message should be indented one level to the right so as to be underneath the ``compose text`` statement::

    compose text s:
        msg s "This is an example text message!" curly
        msg s "You can write lots of dialogue here."
        msg s "Just make sure it's indented at the correct level~"

Finally, if you would like the player to be able to reply, include the name of a label the program should jump to in order to find that reply::

    compose text s:
        msg s "This is an example text message!" curly
        msg s "You can write lots of dialogue here."
        msg s "Just make sure it's indented at the correct level~"
        label my_reply_1

where ``my_reply_1`` is the name of the label the program should jump to in order to continue this conversation when the player opens the message. If you don't want the player to be able to reply, then you can simply omit this line. They will be able to read the text messages but won't be able to respond.

Finally, end the ``after_`` label with the line ``return``.

::

    label after_my_chatroom:

        compose text s:
            s "This is an example text message."
            s "The conversation will continue later."
            s "In the label below."
            label my_reply_1

        return

Replying to a Text Message
--------------------------



