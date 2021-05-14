=============
Text Messages
=============

.. toctree::
    :caption: Navigation

    text-messages

There are two kinds of text messaging styles available in this program. The first, referred to as "regular text messages", delivers text messages in "chunks" which the player can reply to whenever they like. The second style, called "real-time text conversations", plays out similar to a one-on-one chatroom. The player receives an initial text message, and upon opening the text conversation, cannot leave until the conversation is over or the player chooses to end it themselves.

The compose text CDS
====================

The main way of writing text messages is with a special ``compose text`` CDS that looks like the following example::

    compose text s real_time:
        s "Hi, [name]."
        s "I wanted to show you how text messages work."
        s "Send a reply if you got this message okay!"
        label example_reply_1

The ``compose text`` CDS takes several options, which are explained below.

`who`
    Required. "who" should be the ChatCharacter variable of the character who is taking part in the conversation. e.g. ``s``

`real_time`
    Indicates that this text message should play out as a real-time text conversation. If this option is not present, the conversation is treated as a regular text message.

`deliver_at`
    Takes one of four arguments:

    * ``random`` to have the message delivered at a random time after the associated timeline item has been played but before the next one is made available. This is only applicable if the game is being played in real-time mode; otherwise, the message is simply delivered after the timeline item is played.
    * ``next_item`` to have the message delivered at a random time between the timeline item after this one and the item following it. e.g. if there are three items at 11:00, 12:00, and 13:00 and this text is in the ``after_`` label of the 11:00 item, ``deliver_at next_item`` will deliver this message sometime between 12:00 and 13:00, while ``deliver_at random`` would deliver the text message sometime between 11:00 and 12:00. This only works when the player is playing in real-time mode; otherwise, the message is simply delivered after its timeline item has been played.
    * ``00:00`` where ``00:00`` is any time formatted in 24-hour format. For example, ``14:23`` would cause the message to be delivered at ``14:23`` in real-time. This only works when the player is playing in real-time mode; otherwise, the message is delivered after the associated timeline item is played.
    * ``now`` to show the player a notification for this text message immediately. **This is intended for use during chatrooms, phone calls, and Story Mode**. The message itself will only be sent after the player completes the story item. If they hang up the call or back out of the chatroom and cause it to expire, the text message will not appear in their inbox. See :ref:`Manually Sending Text Messages` for more information.

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

where ``s`` is the variable for the character who is sending the message. You can then write dialogue the same way as you would for a chatroom, including adding CGs, emojis, and changing fonts. You can use either the spreadsheet style or the ``msg`` CDS (see :ref:`Writing Chatroom Dialogue`).

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

For regular text messages, the label should immediately begin with a ``menu:`` so that the player is presented with a choice of answers. You can add as many or as few options as you wish. The dialogue here is written the same way as chatrooms, including awarding heart points. You can only award one heart point per reply. It can be for a character not in the conversation as well. For more information on heart points, see :ref:`Showing a Heart Icon`.

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


Real-Time Text Conversations
============================

Unlike regular text messages, real-time text conversations play out similar to a chatroom with a single character. The player receives a text message, and upon entering the conversation, cannot leave until either the conversation is over or the player exits the conversation manually and the conversation is lost.

.. note::
    Example files to look at:

    * tutorial_3_text_message.rpy
    * tutorial_3b_VN.rpy
    * tutorial_5_coffee.rpy
    * tutorial_11_story_call.rpy

    *A brief overview of the steps required (more detail below):*

    #. Create a label using the prefix ``after_`` + the name of the timeline item you want to send the text messages after e.g. ``label after_day_1_4``
    #. Write ``compose text z real_time:`` where ``z`` is the variable for the character who is sending the message.

        #. Optionally, you can also include arguments to tell the program when to deliver the message. Acceptable options are ``deliver_at 00:00`` where ``00:00`` is the time to deliver the message at, in 24-hour time; ``deliver_at random`` to deliver the message randomly before the next timeline item, or ``deliver_at next_item`` to deliver the message sometime between the next timeline item being available and the one after that.

    #. Write dialogue for the conversation, indented at least one level to the right underneath the ``compose_text`` line. You may also include conditionals here.

        #. You can also include the ``pause`` statement with a number of seconds to pause for, e.g. ``pause 2.0*60``. The message delivery will be "staggered", with the message after the pause waiting the given number of seconds before sending.

    #. (Optional) Include a label at the end which will be jumped to to continue the conversation e.g. ``label menu1``
    #. End the ``after_`` label with a return.
    #. (Optional) Create the label the player can jump to to continue the conversation.

        #. (Optional) Allow the player to reply to the text message again by writing ``$ s.text_label = "menu2"`` where ``s`` is the variable for the character sending the message and ``"menu2"`` is the name of the label to jump to to continue the conversation.

    #. Finish the reply label with ``return``

Writing a Text Conversation
---------------------------

To have a character initiate a text conversation, like with regular text messages, you need to have a label that follows a specific naming convention. For example, if your timeline item is called

::

    label casual_route_2_4:

then you need to create a label called

::

    label after_casual_route_2_4:

Then you will compose the text message. This uses a special ``compose text`` CDS::

    compose text ju real_time:
        ju "I didn't understand what Luciel wrote in the chatroom earlier."
        ju "What exactly does 'yeet' mean?"

The main difference between this and regular text messages is the addition of the ``real_time`` option. This tells the program that this conversation will play out in real time once the player enters the conversation rather than having all the messages delivered at once.

Dialogue underneath the ``compose text`` statement can be written the same way as it is for chatrooms, and allows the use of both the spreadsheet style as well as the ``msg`` CDS. Text message conversations can also have CGs, emojis, and special fonts.

.. warning::
    Text messages currently do not support special speech bubbles.

Any dialogue written under the ``compose text`` statement will show up as "backlog" before the user enters the conversation, so it is usually brief.

You can compose text messages for as many characters as you like, and mix and match regular text messages with real-time text conversations freely. There are also additional options available to you for scheduling when the first text message is delivered. See :ref:`The compose text CDS` for more.


Continuing a Text Message Conversation
--------------------------------------

To allow the player to continue the text message conversation, you must provide a label for the program to jump to when the player opens that text message. This is done with the ``label`` argument inside the ``compose text`` CDS::

    compose text ju real_time:
        ju "I didn't understand what Luciel wrote in the chatroom earlier."
        ju "What exactly does 'yeet' mean?"
        label casual_2_4_ju_reply

The program will then jump to the label ``casual_2_4_ju_reply`` to continue the conversation. You will write dialogue inside the label identically to a chatroom::

    label after_casual_route_2_4:
        compose text ju real_time:
            msg ju "I didn't understand what Luciel wrote in the chatroom earlier."
            msg ju "What exactly does 'yeet' mean?" ser1
            label casual_2_4_ju_reply

        return

    label casual_2_4_ju_reply:
        msg ju "I tried to search the Urban Dictionary, but I didn't understand the results." ser1
        menu:
            "You say it when you throw something.":
                ju "When you throw something?"
                ju "Hmm. I don't know if I really understand."
                ju "But thank you for attempting to explain, nevertheless."
                award heart ju
            "lololol you're so funny Jumin.":
                ju "It was not my intention to be a source of entertainment."
                ju "But I suppose I am glad if I was able to bring some levity to your day."
        msg ju "Perhaps I will ask Assistant Kang for further clarification." ser1
        return

You can add additional dialogue after the reply label, and as many or as few menus (for choices) as you like. Unlike with regular text messages, because the conversation occurs in real time, you may also award or take away heart points as many times as you like during the conversation using ``award heart`` and ``break heart``. The whole label should end with ``return``.

Leaving a Real-Time Text Conversation
-------------------------------------

Since real-time text conversations function more closely to chatrooms, if the player clicks the "Back" button during a real-time text conversation, they will be asked if they'd like to end the conversation.

**Backing out of a real-time text conversation means that conversation will no longer be available to continue**, though the player will retain any heart points or CGs they unlocked before they exited the conversation. There is no option to "replay" text message conversations, but unlike chatrooms a text message conversation does not expire until another text message overwrites it.


Text Message Backlog
====================

If you would like text messages to appear as "backlog" in the player's text message inbox to serve as backstory or to set up a route, there is a special CDS to make writing this easier. You can set the text message timestamps to be several real-life days in the past, and even specify what time a message should appear to be sent at::

   add backlog s -4 time 23:22:
        s "do u think Jumin would hire me as his assistant?"
        msg s "Maybe he'd even let me take care of Elly for him ^^" curly
        if s.heart_points < 5 or ju.heart_points > 5:
            m "Not really likely, no"
            s "Aw T_T"
            s "I would be such a good worker!!"
        else:
            m "You'd be such a good cat mom!!"
            s "Right???"
            s "Maybe I should ask to be hired as his cat nanny."
            s "He needs a cat nanny, doesn't he?"

``add backlog`` takes the following options:

`who`
    The character whose text message this backlog is being added to. Should be a ChatCharacter object.

    e.g. s

`day`
    Optional. An integer representing the number of days from the present day this message should be sent at. Negative numbers indicate a number of days in the past e.g. ``-1`` indicates the message should have a timestamp indicating it was sent yesterday (1 day ago). If not present, the message will appear to be sent on the current date.

    e.g. -7

`time ##:##`
    Optional. A timestamp in 24-hour format that indicates the time this first message should appear to have been sent at. Requires a leading zero for times < 10am e.g. 1:05 AM is written as ``01:05`` and 1:30 PM is written as ``13:30``.

    e.g. time 05:16

Next, you will write the dialogue for the text messages. These are written like regular text messages, and you can use both the ``msg`` CDS as well as the spreadsheet method to write dialogue.

The text message backlog statement **does not** support the use of Python, jumps, or many other features besides dialogue inside the text message block; these messages are intended to be used as setup and are not part of active conversations, so any Python or calculations should be done outside of the ``add backlog`` CDS.

However, the ``add backlog`` CDS **does** support conditional if/elif/else statements so that you can vary messages based on certain conditions. In the example at the top of this section, you can see that the message varies based on the number of heart points the player has with certain characters.

``add backlog`` does not support adding labels to jump to in order to reply to a conversation, as it is intended to setup "past" conversations. ``compose text`` is suitable for creating conversations that the player may respond to (see :ref:`The compose text CDS`).

Adjusting Timestamps
---------------------

All lines, regardless of the way they're written, take the special option ``time`` after the dialogue. This allows you to further customize when the messages are sent at e.g.

::

    add backlog ja -13:
        m "Good luck for your first day at the new job, Jaehee ^^" time 07:03
        ja "Thank you very much, [name]" time 07:15
        ja "{image=jaehee_happy}"
        ja "I will do my best!" time 07:18

The above example will have a timestamp 13 days in the past at 7:03 AM for the first message from the MC. The next message, from Jaehee, is also 13 days in the past but has a timestamp for 7:15 AM. The third message does not have an explicit timestamp, so the program will calculate a brief delay between the time given for the previous message and the time the program estimates it would take someone to write the current message. Since Jaehee is merely posting an emoji, this delay will be under a minute long so it will likely also have a timestamp of 7:15 AM. Finally, the last message has a timestamp at 7:18 AM.

Additionally, there is the special line ``pause`` which will cause the program to add the given number of seconds to the timestamp just after the pause statement. For example::

    add backlog ju -17 time 20:32:
        ju "Good evening, [name]."
        ju "You've been with the RFA for a month now so I hoped to ask you a question."
        pause 110
        m "What is it?"
        pause 60*2
        ju "Would you consider a position at C&R International?"

The first message will have a timestamp of 20:32. The second message will take a few seconds to write but likely under a minute, so it will have a timestamp of 20:32 as well. After that, there is a pause statement for 110 seconds. This guarantees that the program will add 110 seconds to its calculation of how long the next message should take to type, so the MC's message will have a timestamp of 20:34.

Finally, after the MC's line there is a pause of 60*2 seconds, so 2 minutes. This will force an additional two-minute delay between the timestamp of the next message, from Jumin, and the MC's message. The last message from Jumin should have a time stamp of 20:36.

.. note::
    The program will add several seconds to each backlog message's timestamp from the initial start timestamp unless an exact ``time`` argument is given. The exact number of seconds depends on the length of the message. This means that if a character has 10 messages in their text message backlog, there is likely to be at least a minute or more of difference in the timestamps of later messages to simulate the real-life time it would take to type out all 10 messages.


Manually Sending Text Messages
================================

Normally, the program will take care of text message delivery after a story item. This allows for consistency across real-time and sequential play styles, as the program can execute an item's ``after_`` label without needing to check through its entire story label. However, there may be some situations where you prefer that a character sends a text message in response to some immediate event. For that, you can use the special delivery time ``deliver_at now`` to trigger a text message to send immediately.

::

    label day_4_chatroom_5_incoming_y():
        y "[name]!! I thought of a really funny thing I wanted to share with you."
        y "Um, one sec, I'll message you the picture."
        compose text y deliver_at now:
            y "look at this lolol"
            y "common_3" img
        y "It's good, right? I thought it was really creative.

In the above example, Yoosung sends the player a text message during a phone call. After Yoosung says "Um, one sec, I'll message you the picture." the player will see a text message popup with a preview of the last text message (in this case, because Yoosung sent an image, it will say "Yoosung sent an image."). This popup is non-interactive; there will not be a button to take the player to the text message immediately and they will need to wait until the phone call is over.

Note also that text messages sent in this way will only actually be delivered to the player's inbox if they complete the story item where the text message occurs. If they end or jump out of the story item prematurely, such as by hanging up or hitting the back button on chatrooms, the text messages will not be sent even though the player saw a notification during the story item itself. This prevents the player from accumulating a bunch of text messages without properly completing the story item.
