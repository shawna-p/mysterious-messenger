# Useful Built-in Features

Besides just modifying the code, the program has some extra features built into the Settings screen specific to this program. Many are useful when creating new content.

## VN Dialogue Settings

**Text Speed** – By default, this slider is set to maximum, which will make text appear instantaneously. However, if set to slower speeds, it will cause phone call text and Story Mode (Visual Novel) text to appear letter-by-letter at the desired speed.

**Auto-Forward Time** – This program includes an 'auto' feature for VN sections as well as phone calls. Setting this bar farther to the right results in a shorter delay between showing new lines of dialogue, and setting it farther to the left gives you more time to read dialogue before the program moves on to the next line.

**VN Window Opacity** - Sliding this value to the left makes the text window in Story Mode completely transparent, while sliding it completely to the right will make it completely opaque.

**Background Contrast** - Sliding this value to the right dims the starry night background used for most menu screens. Sliding it completely to the right makes the background completely black.

**Custom UI changes** – If checked, the program will change some of the UI elements in the game to be more consistent with the new turquoise and black colour scheme. It also includes some subtle animation for the choice screens. Does not affect gameplay in any way.

## VN Skip Settings

**Unseen Text** – By default, this option is checked. If unchecked, the program will stop skipping/stop Max Speed when it comes across text you've never seen before. It remembers which text you have seen across playthroughs.

**After Choices** – By default, this option is also checked. If unchecked, the game will stop Max Speed/skipping after you make a choice and you will need to press the Skip/Max Speed button again.

**Transitions** – If checked, this causes the program to not show transitions when skipping.

## Accessibility Options

**Hacking Effect** – Turns on/off various flashing "hacked" animations.

**Screen Shake** - Turns on/off screen shake.

**Chatroom Banners** - Turns on/off animation for banners during chatrooms.

**Auto-Answer Timed Menus** - Will automatically show the answer menu to the player after a timed menu's timer has run out.

**Animated Icons** - Turns heart icon and hourglass animations into small text notifications. Note that you can also choose to not award hourglasses in the chatroom at all by unchecking **Receive Hourglasses in Chatrooms** in the Developer settings.

**Dialogue outlines** - Renders an outline on fonts during VN sections and phone calls.

* There is also an **Audio Caption** button on the Sound tab in the settings. Checking this will make the program display a notification describing background music and sound effects.

## Developer Settings

These options are helpful when testing a route, though you likely don't want them present in a game release. They can be found both on the main chat home screen as well as on the main menu under the button labelled **Developer**.

**Testing Mode** - Unlocks all chatrooms in a route (up to a plot branch or the end of a route, whichever comes first) and makes them available to play, regardless of whether you've seen previous chatrooms or not. When Testing Mode is on, chatrooms will also never expire, and you can play them many times without being restricted to choices you made previously.

Plot branches can be proceeded through, though the program will still take into account the conditions required to branch (such as number of chatrooms that were participated in) in order to determine which path to branch onto. To mitigate this, at the top of your `_branch` label, you can include a check for `if persistent.testing_mode`, after which you can direct the program to merge the route you want to test. The `if` statement should end with `jump plot_branch_end` so that the program does not attempt to merge more than one route.

**Real-Time Mode** - From here, you can check this option to have the game play out in real-time.

**Hacked Effect** - Turns on/off the messenger "hacked" effects. This particular variable only affects the save file where it was activated from. It causes the chatroom timeline screens to "glitch" and changes the music on the menu screens.

**Receive Hourglasses in Chatrooms** - Unchecking this option will stop awarding players hourglasses during chatrooms. Currently hourglasses are awarded on a pseudo-random basis when a character posts a special bubble from a subset of all special bubbles. This option is useful if the chatroom is intended to be seen as a video and not played through, for example.

**Use custom route select screen** - Checking this option will cause the program to use the screen titled `custom_route_select_screen` instead of `route_select_screen` when the player chooses a route at the start of the game. See [[Customizing the Route Select Screen]] for more.

**Fix Persistent** - This is an option primarily intended for users updating Mysterious Messenger from older versions (<2.0) to fix issues with saved persistent values. If Ren'Py is complaining of compatibility issues with persistent values, you can try using this option to fix it.
