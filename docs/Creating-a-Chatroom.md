# Creating a Chatroom

**Example files to look at: [tutorial_5_coffee.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_5_coffee.rpy "tutorial_5_coffee"), [tutorial_6_meeting.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_6_meeting.rpy)**

_A brief overview of the steps required (more detail below):_

> 1. Create a new `.rpy` file (Optional, but recommended)
> 1. Create a label for the chatroom
>     1. You may also want to fill this in to the `Script Generator.xlsx spreadsheet` so you can set up your route later (see [Setting up Sequential Chatrooms](Setting-up-Sequential-Chatrooms.md))
> 1. After the label, write `call chat_begin('noon')` where `'noon'` is replaced by whatever time of day/background you want to use
> 1. Add a `play music yourmusic` where `yourmusic` is replaced by the desired music variable
> 1. Write the chatroom (you may want to use `Script Generator.xlsx`)
> 1. End the chatroom with `jump chat_end`

The first thing you should do when creating a chatroom is create a new `.rpy` file and name it something descriptive so you'll know where to find that chatroom. If you're planning on making a lot of chatrooms (say, for a route), you should come up with a consistent naming scheme such as `day_1_chatroom_3.rpy` or `chatroom_1_3.rpy`so it's easier to find the correct files later on.

In your newly created `.rpy` file, start off by making a label:

```renpy
label day1_1:
```

Don't forget the colon after the label name. Your label name also can't have any spaces in it, nor can it begin with a number.

Next, it's time to begin the chatroom. Note that everything under the label __must be indented at least one level to the right__. Look at the example files mentioned above if you're not sure what this means. To begin the chat, use the call:

```renpy
call chat_begin("earlyMorn")
```

chat_begin |
-----------|
`background, clearchat=True, resetHP=True` |

The text in quotes tells the program what background to use. Your options are:

* morning
* noon
* evening
* night
* earlyMorn
* hack
* redhack
* redcrack

Note that it *is* case-sensitive, so you need to get the capitals right. The `chat_begin` function will also clear the chat log (aka your message history, so when you begin a new chatroom there are no messages on the screen at the beginning), but you can pass it a second argument so that it doesn't clear the chat log. That looks like this:

```renpy
call chat_begin("hack", clearchat=False)
```

The other thing the `chat_begin` call does is set the heart points the player has collected in this chatroom to zero. In general, this makes sure that if the player collected 15 heart points in the last chatroom, they start again at zero for this chatroom. Unless you are changing the chatroom background in the middle of a chatroom, you can usually leave this as True. If you don't want to set the chatroom heart points to zero, you need to tell it the `resetHP` argument is `False`:

```renpy
call chat_begin("hack", resetHP=False)
```

Besides preventing the program from resetting heart points, if `resetHP = False` the program will also assume you're calling `chat_begin` in the middle of a chatroom and thus don't want the participants reset. Otherwise, the list of participants shown at the top of the screen during a chatroom will also display people who have entered and then exited the chatroom. If you're not calling `chat_begin` in the middle of a chatroom, you usually want `resetHP` to be `True`.

So now that the chat is set up, you probably want to play some music. Music is played like so:

```renpy
play music mystic_chat
```

where `mystic_chat` can be replaced by the name of whatever music you want. There are several files already pre-defined in [variables_music_sound.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/variables_music_sound.rpy) under the heading **BACKGROUND MUSIC DEFINITIONS**. If you want to define your own music files, be sure to add them to the `music_dictionary` so they are compatible with audio captions. See [Adding new Audio](Adding-new-Audio.md) for more information.

Finally, to end your chatroom, you need to write

```renpy
jump chat_end
```

To learn more about how to write dialogue for your chatroom, check out [Using the Chatroom Spreadsheet](Using-the-Chatroom-Spreadsheet.md).
