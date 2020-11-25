# Timed Menus

**Example files to look at: [tutorial_4_timed_menus.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_4_timed_menus.rpy "tutorial_4_timed_menus"), [tutorial_9_storytelling.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_9_storytelling.rpy "tutorial_9_storytelling")**

If a timed menu is used instead of a regular one, the answer button will appear at the bottom of the screen for a specific period of time before disappearing. The chat will continue on while the answer button is displayed. The time the player has left to answer is shown above the answer bar as a planet moving towards the right side of the screen. When it reaches the right side, the answer button will disappear.

There are a few special things to note about timed answers:

* **The time the player has to press the answer button changes depending on how fast they have the chatroom speed set to**. If, when writing the menu, you give the player 10 seconds to reply, the answer button will stay on screen for 10 seconds when the player has the chatroom speed set to 5, but it will stay on the screen for 5.5 seconds for a player with the chatroom speed at 9 and for 14.5 seconds for a player with chatroom speed set to 1.
  * This is so that players who have a slower reading speed will still be able to read the same number of messages as a player with a faster reading speed before the answer button times out
* **If a player is on Max Speed, it will skip the timed menu entirely**, with no opportunity for the player to press the answer button
* **As soon as the player hits the answer button, the chat will stop until they choose an answer**. For example, if the player has 10 seconds to answer and presses the answer button after 5 seconds, the answer choices that appear will not go away even after the 10 seconds are up
* **A player who selects the answer button before the time is up will miss any messages that they might have seen if they waited to press the answer button**. For example, if the timer is 10 seconds long and the player presses the answer button after 5 seconds, they will be unable to see any messages that would have been sent in the next 5 seconds if they had waited
* **If the player replays a chatroom with timed menus, the answer button will not appear at all**/all timed answers will "time out". This is due to possible replay issues in the event that a player has never seen the menu options before.

## How to write a timed menu

Writing timed menus works very similarly to regular menus. Whenever you'd like the answer button to become available, include the line

```renpy
call continue_answer("menu1", 8)
```

where `"menu1"` is the name of the menu to jump to when the player presses the answer button, and `8` is the number of seconds to show the answer button to a player with chatroom speed set to 5. It may take some trial and error to determine how long you should display the answer button for and how many messages the player might see before answering. If you don't provide the number of seconds for the answer button to remain on-screen, it will default to 5 seconds.

After calling `continue_answer`, you should write more dialogue that will continue to be sent to the chatroom until the player hits the answer button. In most cases, the time it takes to display this dialogue should be the number of seconds you show the answer button for. If you just want the player to have a limited time to answer before the chat moves on, see [Pausing for an answer](#pausing-for-an-answer).

Next, write the menu. To use timed menus, you need to give each menu a name so the program can jump to it when the player hits the answer button.

```renpy
if timed_choose:
    menu menu1:
        "Choice 1":
            m "Choice 1."
        "Choice 2":
            m "Choice 2."
else:
    s "Optional dialogue here."
s "Regular dialogue resumes here."
```

The main things to note is that you must write `if timed_choose:` before your menu, and you must name the menu what you called it earlier in the `continue_answer` call.

Including `if timed_choose` ensures that if the player doesn't answer before the timer runs out, then they won't see the menu. Optionally, you can include an `else` statement like you see in the example. Dialogue indented under the `else` statement will only be seen by a player who did not click on the answer button and let the menu time out.

Unlike for regular menus, the dialogue immediately after a choice usually does **not** need the argument `(pauseVal=0)`. For ordinary menus, this reduces the delay between when the player selects a choice and when it displays in chat, but because timed menus allow the player to interrupt the flow of dialogue, it feels more natural for there to be a delay between selecting an answer and having it display in-chat.

Otherwise, timed menus work almost the same as regular menus, and can be nested as well. See [[How to let the player make a choice | Useful-Chatroom-Functions#How_to_let_the_player_make_a_choice]] for more information on regular menus.

### Example chatroom

An example of a chatroom with timed menus for interruptions may look as follows:

```renpy
call continue_answer("menu1", 8)
s "You only have so long to reply,"
s "and when the planet at the bottom of the screen reaches the right side,"
s "BAM!!"
s "The opportunity to answer has passed!!!"
s "You write these menus a bit differently than regular menus"
s "You'll see an example of it in this code."

if timed_choose:
    menu menu1:
        "Slow down! Timed menus??":
            m "Slow down! Timed menus??"
            s "Whoops lolol I got a bit excited"
            s "Yup! Maybe try playing through this chatroom a few times to see what happens?"

        "So I can choose between listening or interrupting?" :
            m "So I can choose between listening or interrupting?"
            s "Yeah! If you just let the chat play out,"
            s "you'll see different dialogue than if you'd decided to answer."

else:
    s "If you don't reply and just listen,"
    s "maybe you'll see some interesting dialogue!"

s "The timer will be faster or slower depending on what your chatroom speed is"
```

(This code can be seen in-game by playing through the Timed Menus chatroom on Tutorial Day).

In a chatroom using the code above, a player who chooses the option "Slow down! Timed menus??" will see the following dialogue:

```renpy
s "You only have so long to reply,"

## Dialogue that may or may not be seen depending on
## how fast the player presses the Answer button
s "and when the planet at the bottom of the screen reaches the right side,"
s "BAM!!"
s "The opportunity to answer has passed!!!"
s "You write these menus a bit differently than regular menus"
s "You'll see an example of it in this code."
## End of optional dialogue

m "Slow down! Timed menus??"
s "Whoops lolol I got a bit excited"
s "Yup! Maybe try playing through this chatroom a few times to see what happens?"
s "The timer will be faster or slower depending on what your chatroom speed is"
```

A player who chooses the option "So I can choose between listening or interrupting?" will see the following dialogue:

```renpy
s "You only have so long to reply,"

## Dialogue that may or may not be seen depending on
## how fast the player presses the Answer button
s "and when the planet at the bottom of the screen reaches the right side,"
s "BAM!!"
s "The opportunity to answer has passed!!!"
s "You write these menus a bit differently than regular menus"
s "You'll see an example of it in this code."
## End of optional dialogue

m "So I can choose between listening or interrupting?"
s "Yeah! If you just let the chat play out,"
s "you'll see different dialogue than if you'd decided to answer."
s "The timer will be faster or slower depending on what your chatroom speed is"
```

Finally, a player who does not press the Answer button and lets the chat play out will see the following dialogue:

```renpy
s "You only have so long to reply,"
s "and when the planet at the bottom of the screen reaches the right side,"
s "BAM!!"
s "The opportunity to answer has passed!!!"
s "You write these menus a bit differently than regular menus"
s "You'll see an example of it in this code."
s "If you don't reply and just listen,"
s "maybe you'll see some interesting dialogue!"
s "The timer will be faster or slower depending on what your chatroom speed is"
```

## Pausing for an answer

If you would like to have the conversation pause for a moment to allow the player to interrupt, but continue on if they say nothing, there is a special function you can use in combination with a `timed_pause` call. For example, a chat like the following:

```renpy
u "Have you heard of it?"

call continue_answer("other_storytelling_menu1", 5)
call timed_pause(5)

if timed_choose:
    menu other_storytelling_menu1:
        "Yes.":
            m "Yes." (pauseVal=0)
            u "I thought you would."
        "No.":
            m "No." (pauseVal=0)
            u "Oh? I'm surprised."

u "Most people are familiar with it already."
```

After the line "Have you heard of it?", the chat will pause for 5 seconds (or longer/shorter depending on the player's chat speed) and the answer button will flash at the bottom of the screen. If, after the five seconds have passed, the player hasn't answered, the chat will continue on from the line "Most people are familiar with it already."

If the player chooses to answer, the chat will continue on with their response like a normal menu. The major difference between this method and the previous one is that no new messages will be shown to the player after the answer button becomes available. The first method is better suited for "interruptions", whereas this method is better suited for direct questions asked of the player. There are many more ways you can combine these methods for interesting storytelling techniques!

In order to wait for a response using a timed menu, you need to use `call continue_answer("menu1", 5)` where `"menu1"` is the name of the menu to jump to if the player presses the Answer button and `5` is the number of seconds to wait for a response for a player on chatroom speed 5.

Below the call you need to write `call timed_pause(5)` where `5` is the  number of seconds to wait for a response. Typically this would be the same as the number in the previous call; however, you can combine this with additional chat messages for a more dynamic experience as well. This label pause for a length of time that takes into account the speed the player has the chatroom set at so players with the chatroom speed set very high or very low will see the same number of messages, and the chat will pause for the same relative time. Otherwise, if you wrote `pause 5`, for example, a player with the chatroom speed set to 9 would see the timed answer timer finish counting down in less than 5 seconds, but the chat won't move on until the 5 seconds are up.

The line `if timed_choose:` is necessary here as well so that players who don't press the answer option won't see the menu. Be sure to indent your menu underneath it and give it the same name as you passed to `continue_answer`.

### Example results

In a chatroom using the code above, a player who chooses the option "Yes." will see the following dialogue:

```renpy
u "Have you heard of it?"
m "Yes."
u "I thought you would."
u "Most people are familiar with it already."
```

A player who chooses the option "No." will see the following dialogue:

```renpy
u "Have you heard of it?"
m "No."
u "Oh? I'm surprised."
u "Most people are familiar with it already."
```

And a player who does not press the answer button during the chat will see the following dialogue:

```renpy
u "Have you heard of it?"
u "Most people are familiar with it already."
```
