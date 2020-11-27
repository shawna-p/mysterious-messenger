# Including a VN During a Chatroom

**Example files to look at: [tutorial_9_storytelling.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_9_storytelling.rpy "tutorial_9_storytelling")**

A brief overview of the steps required (more detail below): |
------------------------------------------------------------|

> 1. Create a chatroom as you usually would (see [Creating a Chatroom](Creating-a-Chatroom.md))
> 2. When you want the VN to interrupt the chatroom, use `call vn_during_chat('name_of_vn_label')`
>     1. If you want to clear the chat history after the VN returns to the chatroom section, pass the argument `clearchat_on_return=True` e.g. `call vn_during_chat('name_of_vn_label', clearchat_on_return=True)`
>     2. If you want to change the background between chatroom sections, pass the argument `new_bg="morning"` where `"morning"` is the name of the new background e.g. `call vn_during_chat('name_of_vn_label', new_bg="morning")`
>     3. If you want to change the list of chatroom participants between chatroom sections, pass the argument `reset_participants=[y, s, m]` where `[y, s, m]` is a list of ChatCharacter objects who you want to show participating in the chatroom e.g. `call vn_during_chat('name_of_vn_label', reset_participants=[z, m])`
>     4. If you don't want to return to the chatroom section after jumping to a VN, use `call vn_during_chat('name_of_vn_label', end_after_vn=True)` and then instead of `jump chat_end` use `jump vn_end`.
> 3. Create the VN label (e.g. `label name_of_vn_label`) and write the VN section as normal (see [Writing a VN section](Writing-a-VN-Section.md)) but __do not__ use `call vn_begin` or `jump vn_end` and instead write `return` at the end of the label
> 4. Continue writing the rest of the chatroom beneath your `call vn_during_chat` line and end with `jump chat_end` as usual

## Note on usage

This page explains how to include a VN section __in the middle of a chatroom__, such that the player will be viewing the chatroom and it will immediately transition to the VN section and back to the chatroom in the same 'scene'. This is different from how VN sections usually play out in-game: that is, first the player views a chatroom, is returned to the chatroom timeline screen, and then must select the corresponding Story Mode (VN) section to proceed. If you are interested in the latter, see [Writing a VN section](Writing-a-VN-Section.md).

First, you'll start by setting up a chatroom the way you usually would (see [Creating a Chatroom](Creating-a-Chatroom.md)). If you'd like to start with a VN that turns into a chatroom later, you must still begin with `call chat_begin("morning")` where `"morning"` is the name of the background you will use for the chatroom. E.g.

```renpy
label my_chatroom:
    call chat_begin("night")
    play music lonesome_practicalism
    call enter(r)
    r "Some dialogue."
```

Next, wherever you would like to have the VN appear and interrupt the chatroom, write `call vn_during_chat('my_vn_label')` where `'my_vn_label'` is the name of the label you will create for your VN section.

For the VN section, create a label with the name you gave it earlier, e.g.

```renpy
label my_vn_label:
```

In this label, you must write the VN section. It is written the same way as a regular VN -- see [Writing a VN section](Writing-a-VN-Section.md) -- however you __should not__ begin with `call vn_begin` and should just begin the VN section. E.g.

```renpy
label my_vn_label:
    scene bg rika_apartment
    # This next line is optional; if you want the music to continue from the
    # chatroom you can leave it out, or use `stop music`
    play music lonesome_practicalism
    show jaehee glasses happy
    ja "This is some example dialogue."
```

Aside from the beginning and ending, everything can be written the same as described in the sections on VN writing.

To end the VN, use `return` instead of `jump vn_end` e.g.

```renpy
label my_vn_label:
    scene bg rika_apartment
    show jaehee glasses happy
    ja "This is some example dialogue."
    menu:
        extend ''
        "Neat!":
            m "Neat!"
        "Boring.":
            m "Boring."
    ja neutral "The VN section is now over."
    return
```

The program will then return to the point after which you wrote `call vn_during_chat` and you can resume the chatroom as usual.

## Clearing the chat log on return

If you would like to clear the chat log after returning from the VN section (that is, the player won't see the previous messages in the conversation), you can also pass the `vn_during_chat` another argument like so:

```renpy
u "Here's some test chatroom dialogue."
u "The game will jump to the VN section after this message."
call vn_during_chat('my_vn_label', clearchat_on_return=True)
u "The chatroom resumes from here, but the message history is gone."
```

## Changing backgrounds between chatrooms

You can also change the chatroom background when it returns. To do so, pass `call vn_during_chat` the argument `new_bg="morning"` where `"morning"` is the new background you want to use. E.g.

```renpy
u "This scene plays out more like two separate chatrooms with a VN in between them."
call exit(u)
call vn_during_chat('my_vn_label', clearchat_on_return=True, new_bg="night")
call enter(u)
u "The chatroom resumes from here, but the message history is gone and the background has changed."
```

## Modifying the chatroom participants

If you want to change the list of participants in the chatroom between scenes, you can pass `call vn_during_chat` the argument `reset_participants=[ja, m]` where `[ja, m]` is a list of the ChatCharacter objects you want in the new chatroom. Note that you must include the main character (`m`) in this list if you want the player to appear as though they are participating in this chatroom.

For example,

```renpy
s "Anyway, I should leave."
call exit(s)
y "Me too!"
call exit(y)
call vn_during_chat('my_vn_label', clearchat_on_return=True, new_bg="night", reset_participants=[ja, ju, m])
ja "This chatroom now looks like there are three people present, 'ja', 'ju', and the player ('m')"
```

## Ending the scene after a VN

If you don't want the player to return to a chatroom section and instead want them to see the chatroom, then a VN, and then the scene ends without returning to a chatroom section, you can pass the `end_after_vn` argument to the `vn_during_chat` call e.g.

```renpy
u "Anyway, this is the end of the scene."
call exit(u)
call vn_during_chat("my_last_vn_label", end_after_vn=True)
jump vn_end
```

If you are ending on a VN, use `jump vn_end` after the call to `vn_during_chat` instead of `jump chat_end`.
