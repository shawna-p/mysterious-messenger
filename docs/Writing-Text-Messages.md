# Writing Text Messages

**Example files to look at: [tutorial_5_coffee.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_5_coffee.rpy "tutorial_5_coffee"), [tutorial_3_text_message.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_3_text_message.rpy "tutorial_3_text_message")**

_A brief overview of the steps required (more detail below):_

> 1. Create a label using the prefix `after_` + the name of the chatroom you want to send the text messages after e.g. `label after_my_chatroom`
> 2. Begin the text chain with `call compose_text(s)` where `s` is the variable for the character who is sending the message
> 3. Write dialogue for the conversation. You may use `Script Generator.xlsx` to assist with this.
> 4. End the text chain with `call compose_text_end('menu1')` where `'menu1'` is an optional label to jump to to allow the player to reply to the message
> 5. End the entire `after_` label with the line `return`
> 6. Create a label for the reply (e.g. `label menu1:`) and begin with `call text_begin(s)` where `s` is the variable for the character sending the message
> 7. Add a menu and optionally award the player a heart point
> 8. (Optional) Allow the player to reply to the text message again by writing `$ s.text_label = 'menu2'` where `s` is the variable for the character sending the message and `'menu2'` is the name of the menu to jump to to let the player reply to the message. Repeat steps 6-9 for this new label.
> 9. Finish the reply label with `jump text_end`

## Sending the initial text message

To have character text the player after a chatroom, the program looks for a label with a specific naming convention. For example, if your chatroom is called

```renpy
label my_chatroom:
```

then you need to create a label called

```renpy
label after_my_chatroom:
```

Next, write

```renpy
call compose_text(s)
```

where `s` is the variable for the character who is sending the message. You can then write dialogue the same way as you would for a chatroom, including adding CGs, emojis, and changing fonts. Text messages do not currently support special speech bubbles.

Finally, end the message with

```renpy
call compose_text_end('menu1')
```

where `'menu1'` is an optional parameter that tells the program to jump to that label when the player presses "Answer" in this text message conversation. If you do not include a label to jump to, the player will be able to read this message but will not be able to respond.

Finally, end the `after_` label with the line

```renpy
return
```

## Replying to Text Message

If you passed `compose_text_end` an argument such as `'menu1'`, then you need to create a label called `label menu1` that the program will jump to when the player presses "Answer". There are no restrictions on what you can call this label, but it's recommended you come up with a consistent naming scheme to avoid accidentally creating several labels with the same name.

Create a new label for the reply as you named before.

```renpy
label menu1:
    call text_begin(s)
    menu:
        "Choice 1":
            m "Choice 1"
            # Additional dialogue
        "Choice 2":
            m "Choice 2"
            # Additional dialogue
    s "Optional additional dialogue seen regardless of choice."
    jump text_end
```

You begin the label with `call text_begin(s)` where `s` is the variable of the character the player is messaging. Then you should immediately begin with a `menu:` and give the player whatever choices you wish. This is written the same way as chatrooms.

### Awarding Heart Points

You can award the player heart points for a text message response the same way you do in chatrooms. For regular text messages, the player can only receive one heart point per message reply; any additional heart point calls will simply overwrite the first one. Awarding heart points looks like this:

```renpy
label menu1:
    call text_begin(s)
    menu:
        "Heart Point Choice 1":
            m "Heart Point Choice 1"
            call heart_icon(s)
            # Additional dialogue
        "Heart Point Choice 2":
            m "Heart Point Choice 2":
            call heart_icon(y)
            # Additional dialogue
    # Optional additional dialogue
    jump text_end
```

In the above example, depending on the player's choice, they either receive a heart point with `s` or `y`.

### Allowing multiple replies

If you want to allow the player to continue replying to a regular text messages, then before `jump text_end` you must include the line

```renpy
$ s.text_label = "menu2"
```

where `s` is the variable of the character in the conversation and `"menu2"` is the label to jump to for the player to continue replying. You could also include this line nested under a specific menu option in case you only want the player to be able to continue replying if they pick a certain response.

A text message conversation with two replies might look like the following:

```renpy
label after_my_chatroom:
    ## Text message to ja
    call compose_text(ja)
    ja "A sample text message."
    call compose_text_end("sample1")

label sample1:
    call text_begin(ja)
    menu:
        "Sample reply":
            m "Sample reply"
            call heart_icon(ja)
        "Sample reply 2":
            m "Sample reply2"
            ja "Sample response."
    ja "Response seen regardless of choice."
    $ ja.text_label = "sample2"
    jump text_end

label sample2:
    call text_begin(ja)
    menu:
        "Sample reply 3":
            m "Sample reply 3"
        "Sample reply 4":
            m "Sample reply 4"
            call heart_icon(ja)
            ja "Sample response."
    jump text_end
```
