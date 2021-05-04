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

where ``z`` is the variable of the character whom the player is calling or who is calling the player (see :ref:`Creating Characters` for a list of the existing characters).

The following section will cover **incoming** and **outgoing** calls to characters that are optional for continuing with the story. You can find more information on Story Calls at :ref:`Story Calls`.

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

You can also change the dialogue of a phone call depending on whether the player picked up when the character first called, or if they are calling the character back. For more on that, see :ref:`Phone Callbacks`.


Creating a Story Call
=====================

Mysterious Messenger also includes "story calls", phone calls from the characters which the player must see before they can continue with the story. Story calls can be standalone, appearing on the timeline as their own story with a trigger time, or they can be attached to chatrooms or standalone story mode items as well and played after the main/parent timeline item is complete.

To create a standalone story call, see :ref:`Story Calls`. Otherwise, the program will automatically create a story call if a certain naming convention is used. If the label of the parent item (i.e. a chatroom or standalone story mode) is ``newyear_4_2``, then you can create a label with the suffix ``_story_call_`` + the file_id of the character who will be calling the player e.g.

::

    label newyear_4_2_story_call_ja:
        # This is a label for a story call from the character ja

Unlike story mode labels, there is no "generic" story call; all story calls must come from a particular character who will be calling the player.

.. tip::
    If you want to hide the identity of the caller, you can create a special "Anonymous" ChatCharacter whose file_id you can use for the story call label.

Story calls, like chatrooms, can also expire if the player is playing in real-time or if they hang up in the middle of the call. Expired story calls are treated as though the caller left the player a voicemail. As with chatrooms, the expired version of the story call is found at the name of the original story call label + ``_expired``::

    label newyear_4_2_story_call_ja_expired:
        # The expired version of the phone call

A player who misses a story call or hangs up in the middle of it will either be able to play the expired version to continue the story, or can "buy back" the story call to experience the participated version.

Story call dialogue is written the same way as regular phone calls.


Writing a Phone Call
====================

Phone call dialogue uses the regular character variables and doesn't have any special arguments such as ``(img=True)`` or special fonts. Just use the character variable and write out dialogue in quotations e.g.

::

    label day_1_4_incoming_z:
        z "Hi, [name]! This is phone call dialogue."
        z "You write it like this."
        return


Phone call labels end with ``return`` like all other labels.

You may also find Ren'Py's "monologue mode" helpful, since you won't be switching between expressions or different speakers very often. See ``tutorial_5_coffee.rpy`` for an example of this.


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

This menu, like others, also takes a ``paraphrased`` argument for either the menu as a whole or for an individual choice. For more information, see :ref:`Paraphrased Choices`.

Note also that if you are writing out the main character's dialogue directly after a choice, the first line **does not** require a ``(pauseVal=0)`` clause.

Changing a Character's Voicemail
================================

If the program determines there are no phone calls available for a character when the player phones them, it will automatically play the character's voicemail instead. You can change the character's voicemail whenever you like during a route.

To update a character's voicemail, use::

    $ ja.voicemail = "voicemail_1"

where ``ja`` is the variable of the character whose voicemail you're changing, and ``voicemail_1`` is the name of the label where the voicemail can be found. The default voicemail, "voicemail_1", can be found in ``01_mysme_engine/phonecall_system.rpy``.

Voicemails are written the same way as regular phone calls, though there are no restrictions on what a voicemail label can be called (but it's recommended you pick a descriptive name for it, probably including the word "voicemail").

You can use a character to say voicemail dialogue, or you can use the "generic" voicemail character, ``vmail_phone`` to say dialogue e.g.

::

    label voicemail_1():
        voice "voice files/voicemail_1.mp3"
        vmail_phone "The person you have called is unavailable right now. Please leave a message at the tone or try again."
        return

As shown above, you can also add voice files to the voicemail, which will be played during the next line of dialogue.

Phone Callbacks
================

Missed Calls
------------

Sometimes the player will miss a call from a character, either from playing in real-time or by ignoring the call when it comes up. By default, when the player calls the character back, if that call is available then the player will receive the exact same conversation they would have had with the character if they had picked up the phone when they initially called.

However, you can also alter the dialogue to account for the player calling the character back. The program will look for this alternate dialogue under a special label with the suffix ``_incoming_z_callback`` where ``z`` is the file_id of the character whom the player is phoning back. More specifically, if you had the following chatroom and incoming call::

    label day_7_chat_4():

        scene morning
        s "This is some dialogue for the chatroom!"
        return

    label day_7_chat_4_incoming_s():
        s "Hello [name]!"
        s "I'm glad you picked up~"
        # ...
        return

Then you can create the "callback" label for ``s``'s incoming call at::

    label day_7_chat_4_incoming_s_callback():
        s "[name]!!! You called me back, haha."
        s "I thought maybe you were busy so I didn't wanna bother you."
        s "But I'm glad you called."
        # ...
        return

If this ``callback`` label is present, the program will jump to it when the player is calling the character back instead of going to the regular ``incoming_s`` label. In replay, if the player has seen both the callback version of the call as well as the regular version, they will be prompted with a menu that allows them to pick whether they want to replay the regular version or the callback version.

If you'll be reusing dialogue between the two phone calls, it might be useful to create a second label that both calls can jump to. For example::

    label day_7_chat_4():
        scene morning
        s "This is some dialogue for the chatroom!"
        return

    label day_7_chat_4_incoming_s():
        s "Hello [name]!"
        s "I thought maybe you'd be having lunch and wouldn't pick up."
        jump day_7_chat_4_incoming_s_ending

    label day_7_chat_4_incoming_s_callback():
        s "[name]!!! You called me back, haha."
        s "I thought maybe you were busy so I didn't wanna bother you."
        s "But I'm glad you called."
        jump day_7_chat_4_incoming_s_ending

    label day_7_chat_4_incoming_s_ending():
        s "Are you busy right now?"
        menu:
            "No, not particularly.":
                s "Great! So I had this idea for a cat cafe I wanted to bring up in the chatroom."
                s "Don't tell Jaehee though, okay? She might get mad."
            "Yeah, I should probably get something done today.":
                s "Aw... don't be like that..."
                s "But, if you really have to leave, I'll understand."
                s "Just call me back when you're free!"
        s "Oh... looks like I actually have to go already. I'm sorry for ditching you!"
        s "Let's talk again later in the chatroom. Toodles!"
        return

The two calls start differently, but both jump to the ``day_7_chat_4_incoming_s_ending`` label to finish off the phone call. This can help keep your code more organized so you're not repeating dialogue in two separate labels.

Hanging Up
-----------

You can also define a callback for when the player hangs up in the middle of a phone call. First, in ``variables_editable.rpy`` scroll down to the header **PHONE HANG UP CALLBACK** and find the variable ``default phone_hangup_callback``. By default, it is set to the example function ``hang_up_callback_fn``, but you can change this to whatever you like or even change it in the middle of a route.

``phone_hangup_callback`` should be given the name of a function which takes one parameter, the call that the player was in the middle of when they hung up the phone. The call is stored as a PhoneCall object, which has several useful fields you can access for more information on the call such as the caller and the label it's attached to. The most relevant fields are:

`caller`
    The ChatCharacter object of the person the player was on the phone with.

`phone_label`
    A string with the name of the label where this phone call is found.

`call_status`
    A string that is one of "incoming", "outgoing", "missed", or "voicemail". Details the status of the phone call.

`voicemail`
    True if this phone call is a character's voicemail message rather than a proper conversation. Typically if you check this variable, it's to ignore it.


You can use as many of these fields to check for details on the phone call as you like, then use that information to narrow down what the program should do.


Phone-Only Characters
======================

Like with Story Mode, sometimes you may have a character who only needs to exist for a phone call but doesn't need all the bells and whistles of a full ChatCharacter definition. There are two ways to define such characters:

Dialogue-Only Phone Characters
-------------------------------

For characters that only need to speak in phone calls, but don't need a profile picture or any other information, you can create a regular Character and inherit from the ``phone_char`` object. This applies in situations such as:

* The player can hear the voice of someone else in the background of a call (e.g. the player called Yoosung, but can hear a professor talking in the background on occasion)
* The player called a regular character, but the person who picked up was not the regular character (e.g. the player phoned Jumin, but his father picked up instead)
* You are defining a specific voicemail voice

These characters don't need their own profile picture, but should have their own Character object to speak dialogue with so that the player can properly use the voice tagging system to mute characters they don't want to listen to.

To define a dialogue-only phone character, you can do::

    define hana_phone = Character("Hana", kind=phone_character)

You can then write dialogue in-game via::

    hana_phone "This is some dialogue said by Hana."
    hana_phone "It uses the other_voice tag."



Incoming Call Phone Characters
-------------------------------

For characters who can call the player, but don't need a fully-fledged character definition, there's the special ``PhoneCharacter`` class you can use to define a character for phone calls.

PhoneCharacters only need a name, a profile picture, and a file_id. Like with regular characters, the file_id is used to associate them with phone calls, so you can write incoming call labels that are automatically detected by the program. It also helps the program find the phone call to fill out the History.

A typical PhoneCharacter definition might look as follows::

    default hana_phone  = PhoneCharacter("Hana", "Profile Pics/Other/hana-1.webp", 'ha')

You can put this definition anywhere you like, though it's usually a good idea to keep your character definitions in a central place where you can find them later.

Then, to write a phone call for this character, you can add a label like you would with the regular cast of characters::

    label day_3_chat_7():
        scene evening
        y "Hi [name], sorry to bother you with this!"
        y "I'm about to write a test so I gave your number to a friend."
        y "She'll call you if anything changes."
        y "Wish me luck!"
        exit chatroom y

    label day_3_chat_7_incoming_ha():
        hana_phone "Hi, this is... um, [name], I think? Yoosung gave me your number."
        hana_phone "Nothing's wrong, I just wanted to check if the number worked."
        hana_phone "Haha, this is actually pretty awkward, so I think I'll hang up now."
        hana_phone "Bye."
        return

A ``PhoneCharacter`` acts the same as a ``ChatCharacter`` in nearly all respects, including the ability to update their profile picture, name, and more, but they won't appear in the player's contact list or on the home screen as a character profile. If you want that functionality, you should define them as a ChatCharacter instead (see :ref:`Creating Characters`).

Additionally, if the player misses a call from a ``PhoneCharacter``, they will only be able to call the character back if that call is still available. In practice, this means that the player can't call a ``PhoneCharacter`` whenever they like; only when an outstanding call is available. Outgoing calls to ``PhoneCharacter``s are technically supported if an outgoing call is available; however, if you wish to allow for outgoing calls, you should define this character using the ``ChatCharacter`` class instead of ``PhoneCharacter``, as phone-only characters do not have a contact image which makes it difficult for players to call them.



