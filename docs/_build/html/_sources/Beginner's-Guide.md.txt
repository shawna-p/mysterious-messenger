# Beginner's Guide

If you want to create your own route and some of the technicalities are going over your head, this guide will take you through setting up a new route from start to finish. More specific pages will be referenced throughout. If you already know a bit about the program, you may want to start with [[Setting up Sequential Chatrooms]] instead.

Navigation:

1. [Getting Started](#getting-started)
   1. [Opening the code in a code editor](#opening-the-code-in-a-code-editor)
   2. [Creating a new .rpy file](#creating-a-new-rpy-file)
2. [Defining the route](#defining-the-route)
   1. [Ensuring the route shows up in History](#ensuring-the-route-shows-up-in-history)
3. [Accessing the new route](#accessing-the-new-route)
4. [Creating the Introduction](#creating-the-introduction)
5. [Defining Chatrooms](#defining-chatrooms)
   1. [Creating the first chatroom](#creating-the-first-chatroom)
   2. [Creating an expired chatroom](#creating-an-expired-chatroom)
6. [Playing the route](#playing-the-route)
7. [Next Steps](#next-steps)

## Getting Started

If you've downloaded the program and assets (or created your own replacement assets), the first thing you should do is hit `Launch` from the Ren'Py launcher and play through the Tutorial Day to get a feel for what the program is capable of.

### Opening the code in a code editor

Next, you need to create a new `.rpy` file. This is where you will write the code that will tell Mysterious Messenger how you want your route to be set up. If you have a program to edit code in, such as Atom or VS Code, you should open that program. Otherwise, you can either download an editor online or tell Ren'Py to download it for you.

To get Ren'Py to download the editor for you, in the Ren'Py launcher under `Preferences` there is an option called `Text Editor`. Click on that, and you'll see a variety of suggested editors. Of these, I recommend downloading Atom. Otherwise, you can tell Ren'Py to use the System Editor, and then when you double-click a `.rpy` file in the `mysterious-messenger/game` folder, tell it to always open `.rpy` files with your editor of choice.

`Return` to the main screen of the Ren'Py launcher. Next, in your file explorer, open the `mysterious-messenger/game` folder. To keep things organized, you should create a new folder here. Call it `my_new_route`.

Now you can open your code editing program and use `File -> Open Folder...` to navigate to the `mysterious-messenger/game/my_new_route` folder. It's blank for now, but you will add `.rpy` files to it soon.

### Creating a new .rpy file

Inside your code editor, you can use `File -> New File`. Name this file `my_route.rpy`. Don't forget you need to include `.rpy` at the end so the editor and program understand this file contains code for Ren'Py.

## Defining the route

Inside your new `.rpy` file, copy and paste the following code:

```renpy
default my_route_good_end = ["Good End",
    RouteDay('1st'),
    RouteDay('2nd'),
    RouteDay('3rd'),
    RouteDay('4th'),
    RouteDay('5th'),
    RouteDay('6th'),
    RouteDay('7th'),
    RouteDay('8th'),
    RouteDay('9th'),
    RouteDay('10th'),
    RouteDay('Final')]
```

This defines a variable which is going to contain the information the program needs to understand how to display the route to the player. In the history screen, this will show up under the title "Good End". This guide only covers how to add one ending, but if you want to learn more you can refer to the [[Setting up Sequential Chatrooms]] page.

### Ensuring the route shows up in History

The last variable you defined is just for the "Good End" of a route. You might want multiple endings, maybe with different characters or to reflect how the player's choices affected the narrative. This next variable tells the program that the various endings are part of the same "route". For now, you only have one ending, the "Good End", but you might add more later.

Beneath the code from earlier, copy and paste the following code:

```renpy
default my_new_route = Route(
    default_branch=my_route_good_end,
    branch_list=[],
    route_history_title="My New"
)
```

This tells the program which endings are associated with this route. `route_history_title="My New"` means that in the History screen, this route will be displayed as "My New Route".

## Accessing the new route

Now you need to tell the program to begin your route when the player hits the "Original Story" button from the main menu. To do this, you need to modify `screens_menu.rpy`, so open that file in your editor. It is located inside the game folder at `mysterious-messenger/game/screens_menu.rpy`.

Next, scroll down to `screen route_select_screen()`. The code will look like this currently:

```renpy
screen route_select_screen():
    tag menu
    use menu_header("Mode Select", Show('main_menu', Dissolve(0.5))):
        fixed:
            xysize (720, 1170)
            yalign 1.0
            xalign 0.5
            # New code after here
            vbox:
                style 'route_select_vbox'
                button:
                    style 'route_select_button'
                    action Start()
                    text "Start Game" style 'menu_text_small' align (0.5, 0.5)
```

You need to modify the second-last line to direct the program to your introductory label. The line `action Start()` should be changed to `action Start("my_route_introduction")` so the whole thing will look like the following:

```renpy
screen route_select_screen():
    tag menu
    use menu_header("Mode Select", Show('main_menu', Dissolve(0.5))):
        fixed:
            xysize (720, 1170)
            yalign 1.0
            xalign 0.5
            # New code after here
            vbox:
                style 'route_select_vbox'
                button:
                    style 'route_select_button'
                    action Start("my_route_introduction")
                    text "Start Game" style 'menu_text_small' align (0.5, 0.5)
```

## Creating the Introduction

Now you are going to create a very simple introduction for your route. To keep things organized, you should create a new `.rpy` file like you did last time. Call this one `my_route_intro.rpy`.

Now you need to create a label that the program will jump to when the player hits the Start button. Copy and paste the following code into your new file:

```renpy
label my_route_introduction:
    $ new_route_setup(route=my_new_route)
    call chat_begin('morning')
    play music mystic_chat
    call enter(u)
    u "This is an example chatroom! You can customize it more later."
    call exit(u)
    jump chat_end
```

This is where the program will go when the player hits the Start button. It tells the program which route to start the player on (in this case, `my_new_route` from earlier), and then sets up a chatroom.

`call chat_begin('morning')` tells the program to set up the chatroom with the "morning" background. For more information, see [[Creating a Chatroom]].

`play music mystic_chat` tells the program to play the "mystic_chat" music in the background. The usual Ren'Py method of playing music has been overwritten with this method, which supports audio captions. For more information, see [[Adding Music and SFX]].

`call enter(u)` and `call exit(u)` display messages like "Unknown has entered the chatroom". For more information, see [[Useful Chatroom Functions]].

`jump chat_end` tells the program that the chatroom is over. Typically it will show the Save & Exit screen to the player and return them to the chatroom hub or timeline screen.

All of these features and more are covered under the **Chatrooms** section in the wiki.

You're welcome to flesh this chatroom out more later.

## Defining Chatrooms

Now you need to create the first chatroom of the day for your route, so return to your file `my_route.rpy`. This file should contain the code:

```renpy
default my_route_good_end = ["Good End",
    RouteDay('1st'),
    RouteDay('2nd'),
    RouteDay('3rd'),
    RouteDay('4th'),
    RouteDay('5th'),
    RouteDay('6th'),
    RouteDay('7th'),
    RouteDay('8th'),
    RouteDay('9th'),
    RouteDay('10th'),
    RouteDay('Final')]
```

This will display a list of "Days" on the timeline screen, but there are no chatrooms for the player to go through just yet. You'll be creating the first chatroom now. Modify the code above so that it now looks like the following:

```renpy
default my_route_good_end = ["Good End",
    RouteDay('1st',
        [ChatHistory("Welcome!", 'day_1_chatroom_1', '00:01')
        ]),
    RouteDay('2nd'),
    RouteDay('3rd'),
    RouteDay('4th'),
    RouteDay('5th'),
    RouteDay('6th'),
    RouteDay('7th'),
    RouteDay('8th'),
    RouteDay('9th'),
    RouteDay('10th'),
    RouteDay('Final')]
```

The main thing that has changed is the code after `RouteDay('1st',`, which now has something called a `ChatHistory` object. These objects hold information that tells the program information like the title of the chatroom ("Welcome!"), the label where the program can find the chatroom ('day_1_chatroom_1'), and the time the chatroom should appear at ('00:01', aka 1 minute past midnight).

Next, you need to define your new chatroom, similar to what you did for the introduction.

### Creating the first chatroom

Like before, you should create a new .rpy file in order to keep things organized. Call this one `day_1_chatroom_1.rpy`.

Now you need to define the body of the chatroom. This chatroom will be fairly basic. First, you define the label you gave the `ChatHistory` object earlier, and then you define the body of the chatroom like so:

```renpy
label day_1_chatroom_1():
    call chat_begin("earlyMorn")
    play music mystic_chat
    call enter(u)

    u "Congratulations! You've created your first chatroom."

    menu:
        "That's amazing!":
            m "That's amazing!" (pauseVal=0)
            u "Isn't it? I'm glad you think so."
        "This is a lot of work.":
            m "This is a lot of work." (pauseVal=0)
            u "I'm sure it'll get easier with practice!"
            u "There are plenty of wiki pages to help you out, too."

    u "I'm leaving now. Good luck!"
    call exit(u)
    jump chat_end
```

This defines a very basic chatroom with the character "Unknown" (u). In this particular chatroom, the player is allowed to make a choice, as defined under the `menu:` code. For more on writing chatrooms and creating choices, see [[Useful Chatroom Functions]] and [[Creating a Chatroom]]. There are many more things you can do besides just chatrooms as well, such as having characters send text messages or call the player. For more on those, see the corresponding sections in the wiki.

### Creating an expired chatroom

There's one last thing you should do before finishing your first chatroom. If the player is playing in real-time, or chooses to back out of a chatroom before they've finished viewing it, the chatroom might "expire". Typically this means that the player will then see a version of the chatroom where they don't get to participate in the conversation.

The program automatically looks for this "expired chatroom" using the name of the original chatroom + the suffix `_expired`. So you should define your expired chatroom beneath the regular chatroom like so:

```renpy
label day_1_chatroom_1_expired():
    call chat_begin("earlyMorn")
    play music mystic_chat
    call enter(u)

    u "Oh... it appears [name] is not here."
    u "Well, I'll come back later. Bye!"

    call exit(u)
    jump chat_end
```

This is the chatroom the player will see if it is expired. It can be as similar or as different from the original non-expired chatroom as you like.

## Playing the route

To play your new route, close the program if open and re-launch it. Select "Settings" from the main menu and then navigate to the "Others" tab and select "Start Over". Then press "Original Story" and "Start Game" to play your new route!

## Next steps

I recommend you take a look at the wiki pages about chatrooms to learn how to write more complex chatrooms, such as [[Creating a Chatroom]], [[Using the Chatroom Spreadsheet]], and [[Useful Chatroom Functions]]. You should also look at the corresponding example chatroom files included with the program, such as [tutorial_5_coffee.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_5_coffee.rpy "tutorial_5_coffee"), as they have many notes included explaining the various features you will see when you play that chatroom on Tutorial Day.

Once you're comfortable writing and modifying chatrooms, you can look into adding text messages, then phone calls, and finally emails. You should also look at [[Setting up Sequential Chatrooms]] for more information on how to set up a full route. Good luck!
