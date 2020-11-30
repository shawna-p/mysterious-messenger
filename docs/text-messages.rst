=============
Text Messages
=============

.. toctree::
    :caption: Navigation

    text-Messages

There are two kinds of text messaging styles available in this program. The first, referred to as "regular text messages", delivers text messages in "chunks" which the player can reply to whenever they like. The second style, called "real-time text conversations", plays out similar to a one-on-one chatroom. The player receives an initial text message, and upon opening the text conversation, cannot leave until the conversation is over or the player chooses to end it themselves.

The compose text CDS
====================

The main way of writing text messages is with a special ``compose text`` CDS that looks like the following example::

    compose text s real_time:
        r "Hi, [name]."
        r "I wanted to show you how text messages work."
        r "Send a reply if you got this message okay!"
        label example_reply_1

The ``compose text`` CDS takes several options, which are explained below.

`who`
    Required. "who" should be the ChatCharacter variable of the character who is taking part in the conversation. e.g. ``s``

`real_time`
    Indicates that this text message should play out as a real-time text conversation. If this option is not present, the conversation is treated as a regular text message.

`deliver_at`
    Takes one of three arguments:

    * ``random`` to have the message delivered at a random time after the associated timeline item has been played but before the next one is made available. This is only applicable if the game is being played in real-time mode; otherwise, the message is simply delivered after the timeline item is played.
    * ``next_item`` to have the message delivered at a random time between the timeline item after this one and the item following it. e.g. if there are three items at 11:00, 12:00, and 13:00 and this text is in the ``after_`` label of the 11:00 item, ``deliver_at next_item`` will deliver this message sometime between 12:00 and 13:00, while ``deliver_at random`` would deliver the text message sometime between 11:00 and 12:00. This only works when the player is playing in real-time mode; otherwise, the message is simply delivered after its timeline item has been played.
    * ``00:00`` where ``00:00`` is any time formatted in 24-hour format. For example, ``14:23`` would cause the message to be delivered at ``14:23`` in real-time. This only works when the player is playing in real-time mode; otherwise, the message is delivered after the associated timeline item is played.

The dialogue inside the ``compose text`` block also takes options besides dialogue:

`pause <#>`
    Indicates that the delivery of the item after the pause should wait the given number of seconds before being delivered. This only occurs when the player is playing on real-time mode. ``pause`` also takes math expressions for the time e.g. ``pause 2*60`` would cause the following message to be delivered two minutes (120 seconds) after the previous message.

`label <labelname>`
    Sets the label the program should jump to in order to continue a conversation or allow the player to reply. ``labelname`` should not be in quotations. Including a label is optional; excluding it will simply not provide the player with the option to answer the text message.

Text messages can also include conditional statements to vary dialogue based on certain conditions. An example text message with several of these options combined might look like::

    label after_day_1_4:
        compose text ja real_time deliver_at 10:15:
            ja "Hello, [name]."
            pause 60
            ja "I had a moment of time on my break so I thought I would message you."
            if ja.heart_points > 5:
                ja "I would have liked to call and hear your voice, but time is short."
            label day_1_4_ja_msg

        return

    label day_1_4_ja_msg:
        ja "What are you doing right now?"
        menu:
            "Not too much. I'm glad you messaged.":
                ja "I see. I had a question for you, in fact."
            "Perhaps you can call me later?" if ja.heart_points > 5:
                ja "I would like that very much ^^"
                award heart ja
                ja "If you don't mind, I wanted to ask you:"
            "I'm actually kind of busy at the moment.":
                ja "Oh, I understand."
                ja "I'm sorry to have caught you at a bad time."
                ja "Before you go, however, I was hoping to ask:"
        ja "Do you like coffee?"
        menu:
            "I love coffee! I drink it every morning.":
                ja "You do? I think it can be nice to have a morning routine, certainly."
            "Only if I can have it with lots of cream and sugar.":
                ja "Ah, that's understandable."
                ja "Coffee can be rather bitter on its own."
            "I drink it straight black.":
                ja "That's very bold of you. Some coffees are rather bitter."
            "I don't really like coffee.":
                ja "I understand. It's not always to everyone's taste."
        ja "I'm afraid my break is over, but I'm glad I got to talk with you."
        ja "I hope we can speak again soon."

        return

In this case, the last message of the ``compose text`` block will be the one delivered at the requested time (10:15), so the first message (Hello, [name]) is delivered around 10:14 and the final message at 10:15. The first message may be delivered slightly earlier depending on whether the player has more than 5 heart points with ``ja`` or not, as the program also calculates roughly how long it would take to type out each message and staggers delivery time accordingly. ``pause`` allows you to fine-tune this timing.



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

where ``s`` is the variable for the character who is sending the message. You can then write dialogue the same way as you would for a chatroom, including adding CGs, emojis, and changing fonts. You can use either the spreadsheet style or the ``msg`` CDS [[INSERT LINK HERE]].

.. warning::
    Text messages currently do not support special speech bubbles.

Note that all dialogue for a text message should be indented one level to the right so as to be underneath the ``compose text`` statement::

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

        compose text z:
            z "Hi [name]!"
            z "Hope your morning has been good so far."
            z "Did you eat breakfast yet?"
            label my_reply_1

        return

Replying to a Text Message
--------------------------

If you gave ``compose text`` a label, when the player presses "Answer", the program will jump to that label to continue the conversation. There are no restrictions on what you can call this label, but it's recommended you come up with a consistent naming scheme to avoid accidentally creating several labels with the same name (which will cause errors).

Create a new reply for the label from your text message::

    label my_reply_1:
        menu:
            "No, I haven't eaten yet.":
                z "That's no good! You should eat something soon."
            "Yup! I ate as soon as I woke up.":
                z "That's good to hear."
                award heart z
        z "Eating breakfast in the morning is really important."
        return

For regular text messages, the label should immediately begin with a ``menu:`` so that the player is presented with a choice of answers. You can add as many or as few options as you wish. The dialogue here is written the same way as chatrooms, including awarding heart points. You can only award one heart point per reply. It can be for a character not in the conversation as well. For more information on heart points, see [[INSERT LINK HERE]].

Finally, end the whole label with ``return``.

Replying after the first message
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want the player to be able to reply again after the first message, you need to tell the program where it can find the label to continue the conversation with ``$ z.text_label = "menu2"`` where ``z`` is the variable of the character who is taking part in the conversation and ``menu2`` is the name of the label to jump to. A text message chain with two opportunities to reply might look like::

    label after_my_chatroom:

        compose text z:
            z "Hi [name]!"
            z "Hope your morning has been good so far."
            z "Did you eat breakfast yet?"
            label my_reply_1

        return

    label my_reply_1:
        menu:
            "No, I haven't eaten yet.":
                z "That's no good! You should eat something soon."
            "Yup! I ate as soon as I woke up.":
                z "That's good to hear."
        z "Eating breakfast in the morning is really important."
        z "Do you have any plans for the day?"
        $ z.text_label = "my_reply_2"
        return

    label my_reply_2:
        menu:
            "Maybe you should call me~":
                z "!!"
                z "{image=zen_wink}" (img=True)
                z "Haha, maybe I will~"
            "Nah, I'm going to be lazy today.":
                z "Sometimes it's nice to have days like that."
        z "It was good talking with you!"
        return

How Text Message Delivery Works
-------------------------------

When you write text messages inside an ``after_`` label, those messages are added to a "delivery pool" which is delivered to the player in increments after they finish playing the associated timeline item. So, if you composed text messages for characters A, B, and C, the player may receive Character A's message immediately upon returning to the home screen, and will then receive Character B and C's messages either by waiting around on the home screen or performing other actions such as replying to other text message or emails.

Similarly, if the player has replied to Character A's message, Character A's response gets added to the pool and will eventually be delivered to the player after some time has passed.

All text messages in the delivery pool are immediately delivered as soon as the player clicks to enter the timeline screen.

In this program, there are no time limits on when you can or can't reply to text messages. However, if a character sends the player a new text message and the player hasn't replied to the previous conversation, they will no longer be able to continue the older conversation.
