# Beginning a Text Conversation

**Example files to look at: [tutorial_3_text_message.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_3_text_message.rpy "tutorial_3_text_message")**

A brief overview of the steps required (more detail below): |
------------------------------------------------------------|

> 1. Create a label using the prefix `after_` + the name of the chatroom you want to send the text messages after e.g. `label after_my_chatroom`
> 2. Begin the text chain with `call compose_text(s, real_time=True)` where `s` is the variable for the character who is sending the message
> 3. Write dialogue for the conversation. You may use `Script Generator.xlsx` to assist with this.
> 4. End the text chain with `call compose_text_end('convo1')` where `'convo1'` is an optional label to jump to to allow the player to reply to the message
> 5. End the entire `after_` label with the line `return`
> 6. Create a label for the conversation (e.g. `label convo1:`) and begin with `call text_begin(s)` where `s` is the variable for the character sending the message
> 7. Write the text message dialogue as you would a chatroom, including elements such as `(pauseVal=0)` after the MC's dialogue.
> 9. Finish the conversation label with `jump text_end`

To have the characters begin a text conversation with the player after a chatroom, much like regular text messages, you need to have a label that follows a specific naming convention. For example, if your chatroom is called

```renpy
label my_chatroom:
```

then you need to create a label called

```renpy
label after_my_chatroom:
```

Then to begin writing the dialogue that will appear in the popup notifying the player of a new text message, begin with

```renpy
call compose_text(r, real_time=True)
```

where r is the variable of the character who will text the player. `real_time=True` indicates to the program that this conversation will take place "in real-time" once the player enters the conversation.

You can then write the character's dialogue the way you would in a chatroom. These messages will show up as a "backlog" of sorts before the player enters the conversation, so it should be brief.

At the end of the initial messages, write

```renpy
call compose_text_end('convo1')
```

where `'convo1'` is the name of the label to jump to to continue the text message conversation. This can be named anything, though it's recommended you come up with a consistent naming scheme so you don't accidentally have two labels with the same name.

You can repeat this for as many text conversations as you'd like to have, beginning each with `call compose_text(r, real_time=True)` and ending with `call compose_text_end('convo1')`, of course swapping out the character variables and label names for different values.

Next, create a label with the name you passed it in `compose_text_end` and begin it with `call text_begin(r)` where `r` is the variable of the character who is in the conversation.

```renpy
label convo1:
    call text_begin(r)
```

Next, write out the conversation just like a chatroom, including adding CGs, emojis, and changing fonts. Text messages do not currently support special speech bubbles. You can begin the label with additional dialogue before a menu choice. Like in chatrooms, menu choices should be preceeded with `call answer` in order to show the answer button at the bottom of the screen. Unlike regular text messages, you can award the player as many heart points as you would like, as they will be awarded in real-time.

Finally, end the text conversation with

```renpy
jump text_end
```

An example of a label to jump to for a real-time text conversation might look like the following:

```renpy
label convo1:
    call text_begin(r)
    r "Some sample text."
    r "This is continuing the conversation from before."
    call answer
    menu:
        "Choice 1":
            m "Choice 1" (pauseVal=0)
            r "Reply to choice 1."
        "Choice 2":
            m "Choice 2" (pauseVal=0)
            call heart_icon(r)
            r "Reply to choice 2."
    r "More dialogue for the conversation."
    call answer
    menu:
        "Choice 3":
            m "Choice 3" (pauseVal=0)
            r "Reply to choice 3."
        "Choice 4":
            m "Choice 4" (pauseVal=0)
            call heart_icon(r)
            r "Reply to choice 4."
    r "Final dialogue."
    jump text_end
```
