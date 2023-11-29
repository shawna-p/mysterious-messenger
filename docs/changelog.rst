================
Full Changelog
================

.. toctree::
    :caption: Navigation

    changelog

3.4.0
=====

.. _major-3-4-0:

Major New Features
-------------------

.. list-table::
    :widths: 15, 85
    :header-rows: 1

    * - **Feature**
      - **Description**
    * - :ref:`Achievements`
      - An achievement system will allow you to easily grant and display player achievements in an achievement gallery. Sample achievements for Tutorial Day have been added.
    * - Gallery Zoom Update
      - The gallery has been updated to allow for multi-touch gestures, such as pinch zoom and swiping between images. Note that while the default gallery definitions are updated to include this, you must modify older declarations to use the special ``GalleryAlbum`` class wrapper to get this functionality. Older code will continue to work, but without touch gestures. See: :ref:`CG Albums` for more.

.. _minor-3-4-0:

Minor New Features
-------------------

.. list-table::
    :widths: 15, 85
    :header-rows: 1

    * - **Feature**
      - **Description**
    * - Chatroom scrolling
      - You can now scroll backwards in a chatroom without pausing and the game will not attempt to drag you back down towards the recent messages. A banner at the bottom of the screen will let you jump to the recent messages.
    * - Android Back Button
      - The Android back button will now correctly activate the "back" action in the UI when available.
    * - Hearts to Hourglasses
      - You can exchange 100 hearts for 1 hourglass by clicking the "+" next to hourglasses in the header.
    * - :ref:`Gendered Term Improvement<Pronoun Integration>`
      - The GenderedTerm class lets you set up gendered terms once and have them update automatically based on the player's pronouns and gender, improving ``get_term`` introduced in 3.3.0.
    * - Hourglass confirmation screen
      - New ``hourglass_spend_confirmation`` screen will display the number of hourglasses to be used for things like bonus profile pictures. You can use the new :ref:`SpendHourglass<Spending Hourglasses>` action to easily display it.


.. _fixes-3-4-0:

Fixes
------

.. list-table::
    :widths: 15, 85
    :header-rows: 1

    * - **Fix**
      - **Description**
    * - Special speech bubbles
      - Being on the right side of the messenger no longer requires using the special speech bubble function to get special bubbles.
    * - Guest positioning
      - Guests arriving at the party are better positioned relative to variable screen heights.
    * - Chat Creator special bubbles
      - Fixed an issue where you could only edit a special speech bubble's style and not set it beforehand.
    * - ``hide_albums``
      - Fixed an issue with ``hide_albums`` not working properly.
    * - Screen optimization
      - Screens have been better optimized to reduce repeated Python code.
    * - 8.1 Upgrade
      - The code has been updated for compatibility with v8.1+ of Ren'Py.
    * - Phone UI
      - Phone dialogue has been slightly updated to even out the length of lines using subtitle breaking.
    * - Dialogue bubble fix
      - Special bubbles used by a character on the right side of the chat appear properly.
    * - Sprite layered images
      - Sprite layered images are set up to not require positioning information (will require redownloading the assets).
    * - :ref:`Pronouns update<Pronoun Integration>`
      - Pronouns have been updated to use a series of classes rather than individual variables, and as such do not require redeclaring individual variables like ``they``/``them`` every time the pronoun changes.
    * - Style properties
      - Various style properties (particularly outlines) have been cleaned up across the program.
    * - Updated screen language
      - ``dismiss`` has replaced full-screen buttons where possible (7.5/8.0+).


.. _qol-3-4-0:

QoL Improvements
--------------------

.. list-table::
    :widths: 15, 85
    :header-rows: 1

    * - **Feature**
      - **Description**
    * - Animated Background Performance
      - Improved the performance of the stars in the animated backgrounds for night, early morning, and morning.
    * - Animated Background Simplification
      - Simplified the transform and image code for the animated backgrounds.
    * - Private class attributes
      - Private class attributes have been turned into single-underscore versions where possible to avoid issues with files moving or being renamed impeding save compatibility.
    * - Chat Creator updates
      - Modernized chat creator to use nearrect and dismiss (7.5/8.0).

.. _incompat-3-4-0:

Incompatible
--------------------

* The character sprite expressions have been updated to not require positioning properties. You will need to download the latest assets and overwrite any existing VN sprites to avoid odd positioning issues. If you need the old VN assets, you need to restore the layeredimage definitions with the old positioning information.
* While not incompatible, as they are still included in the engine, the pronoun verbs ``is_are``, ``has_have``, and ``do_does`` have been retired in favour of their simpler counterparts (``are``, ``have``, and ``do``, such that lines can be more readable with ``[they] [are] coming.`` rather than ``[they] [is_are] coming.``). Your script will not require updating, but I suggest you use the new versions going forwards.

3.3.0
=====

It should be noted that this new release supports Ren'Py 8.0+, which uses Python 3. It is suggested you move to Ren'Py 8+ with new games, as Python 3 offers greater flexibility.

.. _major-3-3-0:

Major New Features
-------------------

.. list-table::
    :widths: 15, 85
    :header-rows: 1

    * - **Feature**
      - **Description**
    * - :ref:`Automatic chatroom backgrounds<Creating a Chatroom>`
      - The game will automatically set up chatroom backgrounds based on the time of day the chatroom occurs at. You can override this automatic background by providing your own e.g. ``scene morning``.
    * - Adaptable screen size
      - The game can adapt to screen sizes taller than the original 9:16 ratio e.g. 9:19

.. _minor-3-3-0:

Minor New Features
-------------------

.. list-table::
    :widths: 15, 85
    :header-rows: 1

    * - **Feature**
      - **Description**
    * - :ref:`Manually award hourglasses<Awarding an Hourglass>`
      - Convenience function added for more control over when the player is awarded an hourglass.
    * - :ref:`Chat vs Gallery CGs<Defining a CG>`
      - Show a different image in chatrooms than in the gallery when sending CGs.
    * - :ref:`Phone call expiry dict<Phone Call Expiry>`
      - A convenience dictionary to easily customize how long phone calls should be availlable for.
    * - :ref:`Email testing hub<Testing Emails>`
      - An email testing hub from the Developer settings in-game allows you to quickly invite guests, send replies, and test the party.
    * - VN Screen shake
      - You can use ``show shake`` during Story Mode (VN mode) to shake the screen. Takes into account the player's accessibility preferences.
    * - :ref:`Splash Screen`
      - The splash screen has been relocated and updated to make it easy to add your own image and "Tap to Start" before entering the main menu.
    * - Award Hearts
      - You can provide a number to ``break heart`` or ``award heart`` to award/break multiple hearts at once.

.. _fixes-3-3-0:

Fixes
------

.. list-table::
    :widths: 15, 85
    :header-rows: 1

    * - **Fix**
      - **Description**
    * - Doc improvements
      - Added doc pages on :ref:`deleting messages<Removing Messages from the Chatlog>` and :ref:`adding greetings<Adding Greeting Messages>`.
    * - Profile picture callback fix
      - Profile picture callbacks still go off even if you use a text message or email popup notification to leave the profile screen.
    * - History fix
      - Fixed an issue when rewatching chatrooms in the history after buying back that same chatroom during the story.
    * - MC Profile Picture bug
      - Fixed a bug with the ``add_mc_pfp`` function to properly unlock profile pictures as seen.
    * - Animated Backgrounds
      - Animated backgrounds move more smoothly and don't have any stuttering lines when looping.
    * - Guest Comment Interpolation
      - Guest comments in the guestbook properly interpolate variables like ``[name]`` or pronouns like ``[they]``. There is also a dissolve transition in/out of viewing the comment.
    * - Guest Hourglasses
      - Fixed an issue where players weren't awarded an hourglass upon first viewing a guest's information in the guestbook.
    * - Branch VNs
      - Fixed an issue with branch VNs that would cause a script error dialogue for trigger times.
    * - Background shake
      - Improved how background shake is set up. Backgrounds without an animated version still shake when animated backgrounds are turned on.
    * - Timeline display
      - The timeline correctly displays the "5th DAY" with the suffix when opening a particular day's timeline list.
    * - Chat Creator
      - Fixed an issue where the chat creator didn't correctly export other characters' special bubbles.
    * - Hack tear screen update
      - The hacking "tear" effect is updated for Ren'Py 8 and functions better with large numbers of sections.
    * - Text message preview
      - The text message preview can handle any number of interpolated variables, as needed.
    * - CG Gallery fixes
      - Fix CG gallery thumbnails with automatic cropping.


.. _qol-3-3-0:

QoL Improvements
--------------------

.. list-table::
    :widths: 15, 85
    :header-rows: 1

    * - **Feature**
      - **Description**
    * - Remember save page
      - The game remembers which save page you last used.
    * - Main Menu Screen Actions
      - Common actions for buttons on the main menu and home screen have been turned into functions for easier UI modification.
    * - Check for updates in thread
      - The updater launches a separate thread to check for updates so the UI is not paused/frozen while waiting for the results of the check.
    * - ``gamestate``
      - Whether the program is in a chatroom, phone call, VN/Story Mode, or text message is tracked via a consistent `gamestate` variable.
    * - Available call indicator
      - A new dev option will add a "NEW" sign under a contact's icon when there is a call available for them and add an ``Online`` indicator on their profile screen.
    * - :ref:`get_terms<Using Gendered Terms>`
      - Convenience function for using gendered terms to refer to the player.
    * - Developer Release Options
      - Added a section to ``variables_editable.rpy`` which can be customized for sharing a program distribution with others.
    * - :ref:`Email newlines<Writing an Email Chain>`
      - You can turn off the parser that turns email single newlines into a space (``email_newline_to_space``).
    * - :ref:`Gallery update<CG Albums>`
      - The gallery has been redone to cause fewer headaches overall and requires one definition instead of two.
    * - ``big`` text tag
      - There is now a ``{big}`` text tag which can be used similarly to how ``big`` is used for the msg CDS.
    * - Popup updates
      - Popups have been updated to take advantage of screen tags. An infinite number of popups of any type can be on screen at any time (so, no more restrictions on how many text message popups, heart icons, or stackable notifications etc you can see at once).

.. _incompat-3-3-0:

Incompatible
--------------------

* While not strictly incompatible, the gallery system has been updated to use constants rather than both a default and a persistent album variable. The game will attempt to transfer over any unlocked photos from the old gallery version into the new one. It is recommended that you update your gallery definitions to use ``define`` and the new ``GalleryImage`` class rather than ``Album``. You can find more information :ref:`in the docs on the gallery.<Defining a CG>`


3.2.0
=====

.. _major-3-2-0:

Major New Features
-------------------

.. list-table::
    :widths: 15, 85
    :header-rows: 1

    * - **Feature**
      - **Description**
    * - :ref:`Chatroom Creator`
      - A visual creator to write chatrooms and export them to code or watch them as played in-game.
    * - Update to 7.4+
      - Mysterious Messenger takes advantage of 7.4+ update such as matrixcolor. You will now require Ren'Py 7.4+ to run Mysterious Messenger.

.. _minor-3-2-0:

Minor New Features
-------------------

.. list-table::
    :widths: 15, 85
    :header-rows: 1

    * - **Feature**
      - **Description**
    * - :ref:`Phone hang up callback<Hanging Up>`
      - A special function is called when the player hangs up in the middle of a call, which you can use to alter the game state.
    * - :ref:`Manually send text messages<Manually Sending Text Messages>`
      - Manually send text messages during chatrooms, phone calls, Story Mode, or whenever you like.
    * - Vanderwood expressions
      - Vanderwood has new expressions thanks to `Rom <https://twitter.com/RomRom1705>`_
    * - Choose profile picture
      - (Windows only) Choose a profile picture from your computer to use in-game.


.. _fixes-3-2-0:

Fixes
------

.. list-table::
    :widths: 15, 85
    :header-rows: 1

    * - **Fix**
      - **Description**
    * - Starter story fix
      - Intro chats can properly have incoming calls and don't boot you out to the main menu.
    * - Updater fix
      - Updater properly remembers ignored releases and stops checking for updates when it reaches your current version.
    * - Skip Intro/Save & Exit
      - The chatlog no longer clears when finishing the starter story before exiting to the home screen.
    * - SFX Audio Captions
      - Sound effects are correctly looked up in the sfx dictionary, not the music dictionary.
    * - ``hide_albums`` fix
      - ``hide_albums`` function works correctly again.
    * - Save file names
      - Save file names are more reliably saved using json files instead of string separators.
    * - Fix Persistent button
      - Fix persistent now works with user-defined albums
    * - Animated background screen shake
      - Animated backgrounds now get black bars offscreen to the left and right to improve the appearance of screenshake while animated backgrounds are active.
    * - Tear screen fix
      - The tear screen feature has been updated for Ren'Py 8.0


.. _qol-3-2-0:

QoL Improvements
--------------------

.. list-table::
    :widths: 15, 85
    :header-rows: 1

    * - **Feature**
      - **Description**
    * - msg CDS underline
      - The message CDS takes optional ``underline`` or ``under`` arguments to underline text.
    * - SFX in replay
      - Sound effects are included in chatroom replays.
    * - Profile picture scaling
      - Profile pictures now crop and size themselves to fit the desired dimensions rather than squash/stretching into a square


3.1.0
======

.. _major-3-1-0:

Major New Features
-------------------

.. list-table::
    :widths: 15, 85
    :header-rows: 1

    * - **Feature**
      - **Description**
    * - :ref:`Missed calls callback<Phone Callbacks>`
      - Phone calls can play out differently depending on whether the player is calling back a missed incoming call or not. Also supported in the History.
    * - :ref:`Phone call-only characters<Phone-Only Characters>`
      - Can create a PhoneCharacter specifically for phone calls who won't show up in the player's contacts.
    * - :ref:`Input prompts<Getting Input from the Player>`
      - Can get typed input from players anywhere in the game.
    * - Profile Updates
      - Players can choose their gender separately from their pronouns, and enter a chatroom username separately from their regular name.

.. _minor-3-1-0:

Minor New Features
-------------------

.. list-table::
    :widths: 15, 85
    :header-rows: 1

    * - **Feature**
      - **Description**
    * - :ref:`reset_participants<Resetting Chatroom Participants>`
      - New function allows you to easily reset the participants list in the middle of a chatroom.
    * - :ref:`Link wait pause button<Developer Settings>`
      - Dev toggle allows you to toggle the footer while waiting for the player to click a link to be the pause button.
    * - :ref:`Reversable hack effect<Showing the Hacked Scroll Effect>`
      - The scrolling hacked effects can be reversed to scroll in the other direction.
    * - :ref:`LinkJump<Link Actions>`
      - New action for links to jump to somewhere else in a chatroom (including menus).
    * - :ref:`IfChatStopped<Link Actions>`
      - New action for links that changes depending on whether the chat is stopped or not.
    * - New backgrounds
      - Three new backgrounds have been added: ``snowy_day``, ``rainy_day``, and ``morning_snow``


.. _fixes-3-1-0:

Fixes
------
.. list-table::
    :widths: 15, 85
    :header-rows: 1

    * - **Fix**
      - **Description**
    * - Pause button fix
      - Pausing chatrooms and real-time text messages has been overhauled to cause fewer issues with skipped messages.
    * - Vanderwooo
      - Fixed Vanderwood's name getting cut off in the phone contacts.
    * - Erroneous msg CDS errors
      - Skip Intro and Jump to End now work properly with the msg CDS during chatrooms.
    * - Skip Intro fix
      - Skipping the introduction no longer causes real-time text message to prompt you about leaving even though the conversation is over.
    * - Participated fix
      - Fixes a bug so the MC's profile picture shows up in the list of participants after playing a chatroom.
    * - Unlocked Profile Pics Fix
      - Default profile pictures for characters now only unlock after you've seen them as part of the game.


.. _qol-3-1-0:

QoL Improvements
--------------------

.. list-table::
    :widths: 15, 85
    :header-rows: 1

    * - **Feature**
      - **Description**
    * - :ref:`Reset Albums<Developer Settings>`
      - You can tell the program to forget all seen images and unlocked album entries without losing other persistent variable progress.


.. _other-3-1-0:

Other
--------------------

.. list-table::
    :widths: 15, 85
    :header-rows: 1

    * - **Feature**
      - **Description**
    * - Animated bg relocation
      - Animated background images have been relocated into their own folder inside of the **Phone UI** image folder for better organization.


3.0.1
======

You can find the docs for v3.0.1 here: https://mysterious-messenger.readthedocs.io/en/v3.0.1/

.. _major-3-0-1:

Major New Features
-------------------

.. list-table::
    :widths: 15, 85
    :header-rows: 1

    * - **Feature**
      - **Description**
    * - Chatroom Links
      - Characters can now post links in chatrooms. Clicking a link can cause a variety of actions to occur, such as jumping to a Story Mode section or showing a CG.
    * - Vanderwood
      - Vanderwood has been added as a fully-fledged character with his own profile, chat bubbles, heart icon, and more.
    * - Additional Assets
      - Story Mode has new characters. Chatrooms have two new timeline backgrounds, a new secure chat background, a cracked glass overlay, and a new secure lock opening animation. There is a new red static hack effect.

.. _minor-3-0-1:

Minor New Features
--------------------

.. list-table::
    :widths: 15, 85
    :header-rows: 1

    * - **Feature**
      - **Description**
    * - Character definitions condensed
      - Players now only need to define a ChatCharacter for a new character, and their vn_char and phone_char fields will be automatically defined.
    * - Auto-defined Story Mode window background
      - Users can now supply a character's definition with the ``window_color`` field to automatically colour the dialogue background in Story Mode.

.. _fixes-3-0-1:

Fixes
------

.. list-table::
    :widths: 15, 85
    :header-rows: 1

    * - **Fix**
      - **Description**
    * - Phone call replay
      - Replaying a phone call always begins with the phone audio playing automatically.
    * - Bonus profile pictures
      - There is better error checking for bonus profile pictures. Characters without a greeting image can still use their profile picture next to the number of hearts earned with them.
    * - Saves track the next day
      - Save files now track the name of the next day when loading in real-time.

.. _qol-3-0-1:

QoL Improvements
--------------------

.. list-table::
    :widths: 15, 85
    :header-rows: 1

    * - **Feature**
      - **Description**
    * - Tutorial Day Introduction
      - If you hold Ctrl (Skip) during the introductory phone call on Tutorial Day, you will automatically go directly to the home screen, skipping the introduction.
    * - :ref:`exclude_suffix<Setting up a Route>`
      - Can now exclude the automatic "Day" suffix appended to RouteDay objects.

.. _other-3-0-1:

Other
--------------------

.. list-table::
    :widths: 15, 85
    :header-rows: 1

    * - **Feature**
      - **Description**
    * - Guest grade update
      - The images used for your guest grade after all party guests have arrived have been updated.


3.0.0
=======

.. _major-3-0-0:

Major New Features
--------------------

.. list-table::
    :widths: 15, 85
    :header-rows: 1

    * - **Feature**
      - **Description**
    * - StoryMode
      - Story Mode sections can exist separately from chatrooms and take a trigger time and a title. This also replaces the previous `VNMode` class.
    * - StoryCall
      - Phone calls can appear in the timeline and be mandatory for story progression. If a story call expires, the character will leave a voicemail. Story calls can exist on their own with a trigger time or can be attached to Story Mode sections or chatrooms. Only one story call per character is allowed, but multiple story calls with different callers can exist on the same timeline item.
    * - `msg` CDS
      - A new way of writing chatroom and text message dialogue. Automatically adds text tags and parses emojis as images. Can also add new speech bubbles and fonts to work with this CDS.
    * - `text backlog` CDS
      - Allows messages to be added as "backlog" to a character's text message conversation history. Can manually set the date/time the message appears, relative to the current date/time.
    * - `compose text` CDS
      - Replaces calls like `call compose_text(r)` and `call compose_text_end("menu_a2")`. Makes it easier to set up and write text messages, and even schedule when they should be delivered.
    * - Choice paraphrasing
      - Can turn `paraphrase_choices` on or off on a global, per-menu, or per-choice basis to dictate whether or not the program should automatically make the main character say the dialogue in the selected choice.
    * - Bonus profile pictures
      - Characters have bonus profile pictures that are unlocked based on user-defined conditions or when seen in-game. NPC profile pictures cost 5 heart points with that character to unlock, and player profile pictures cost 1 hourglass. These values are modifiable.
    * - Profile picture callback
      - When the player changes their profile picture, a special function is called that allows the characters to comment on their profile picture choice (e.g. by phoning them or sending a text message)
    * - `scene` and `show` extention
      - `scene` and `show` have been extended to allow chatroom backgrounds to be set with `scene morning` instead of `call chat_begin('morning')`. Most other effects, such as banners, can be shown via `show` commands like `show banner heart` or `show hack effect`.
    * - `timed menu` CDS
      - Timed menus are now typed like regular menus. The dialogue before the first choice will dictate how long the timer is. Choices are shown on-screen while the characters continue messaging. A preferences option turns timed menus into regular menus, and a slider allows for timed menu "bullet time" so that the chat speed can be fast but timed menus slow down to give players time to read.
    * - Email system improvements
      - Email chains can be of an arbitrary length with any number of replies. Failing an email can still continue an email chain. A string parser makes using triple-quoted strings to type emails much more readable. Players can choose to reply to an email later after clicking Reply.
    * - `call chat_begin` / `jump phone_end`-style calls removed
      - The program handles the setup and cleanup of all timeline items. All labels can simply begin without further ado and all labels can end with `return`.

.. _minor-3-0-0:

Minor New Features
--------------------

.. list-table::
    :widths: 15, 85
    :header-rows: 1

    * - **Feature**
      - **Description**
    * - `add_to_album` function
      - Allows you to append a photo to an album after the game has begun.
    * - `hide_albums` function
      - If set, allows you to hide albums from the Album screen unless they have an unlocked CG in them already. Takes a list or a single Album.
    * - `_branch` for parties
      - The Party can exist on its own with a trigger time, and may have a `_branch` label which will execute when the player enters the party.
    * - Guestbook Hourglasses
      - The player is awarded 1 hourglass (HG) the first time they view a guest in the guestbook.
    * - `invite guest` CDS
      - Replaces `call invite(guest)`.
    * - `award heart` and `break heart` CDS
      - Replaces `call heart_icon(s)` and `call heart_break(s)`, respectively. `break heart` can also be written as `heart break`.
    * - `enter chatroom` and `exit chatroom` CDS
      - New way of writing `call enter(s)` and `call exit(s)` respectively.
    * - Custom speech bubbles
      - Can use provided functions to set custom speech bubbles or do things like let Unknown use Ray's speech bubbles.
    * - `was_expired` variable
      - This variable is set before the game executes an `after_` label. Allows you to change dialogue depending on whether or not the associated item was participated in or if it expired.
    * - `-b` and `-thumb` for album images
      - You can now define thumbnails and `-b` variants on thumbnails for gallery images. These variants will be used for bonus profile pictures.
    * - History screen customization
      - Can now add backgrounds to routes in the history screen. A rectangular image will automatically have the corners cropped to fit the button. Can also add prologues through a special variable in `variables_editable.rpy`.
    * - `.webp` and `.ogg` conversion
      - Most images have been converted to `.webp` to reduce file size. Some audio files have been converted to `.ogg` for similar reasons.
    * - `call answer` removed
      - `call answer` is no longer required before a chatroom or text message menu.
    * - `custom_route_select_screen`
      - Can easily switch between a custom route select screen and the default one. Default route select improved to have additional graphics.

.. _fixes-3-0-0:

Fixes
--------------------

.. list-table::
    :widths: 15, 85
    :header-rows: 1

    * - **Fix**
      - **Description**
    * - History cleanup
      - RouteDays without content don't show up in the History. Single-day routes are centered in the screen.
    * - `buyahead`
      - Buying 24 hours in advance while playing in real-time will continue to unlock items up to the 24 hour mark after proceeding through a plot branch in the middle of the purchased 24 hours.
    * - Text message preview
      - Text message previews can properly handle text tags such as special fonts or sizes.
    * - Sign screen
      - Sign screen doesn't show hourglasses/heart points if the player was just replaying it or the item was expired.
    * - Pronoun fixes
      - Capitalized variants of pronoun variables are automatically defined.
    * - Observing improvements
      - Replaying Story Mode/phone calls during a playthrough now only presents you with the choices you made on that particular playthrough.
    * - Screen shake
      - Screen shake now works with animated backgrounds. It can be shown via `show shake`.
    * - Profile picture flexibility
      - Profile pictures can now use solid colours or cropped/transformed images.
    * - Messenger Error screen
      - The program will try to catch operational errors and award the player an hourglass if something fails but it is able to recover.
    * - Viewing CGs
      - Viewing CGs full-screen while on the messenger or viewing a text message now simply halts the game state while it is being viewed instead of manually pausing the chat.
    * - Home screen grid fix
      - The home screen now properly calculates how many pictures it will be showing so the grid is not over- or underfull.

.. _qol-3-0-0:

QoL Improvements
--------------------

.. list-table::
    :widths: 15, 85
    :header-rows: 1

    * - **Feature**
      - **Description**
    * - `play music` and `play sound`
      - New CDSs replace `call play_music()` and `call play_sfx()`. Can be typed and used the same way as the regular Ren'Py function, but is now compatible with audio captions.
    * - Custom ending screens
      - Can now define your own ending image and pass the whole string to the `ending` variable upon ending a route.
    * - `create_incoming_call`
      - Easy way of creating a new incoming call; intended primarily to be used in combination with profile picture callbacks.
    * - Keyboard shortcuts
      - Space bar selects most chatroom footer options, like play/pause/answer/save & exit and the Sign button. Left/right arrows decrease/increase the chat speed.
    * - TimelineItem class
      - All timeline items (chatrooms and VN mode) have been switched to inherit from a base TimelineItem class. The new classes allow for more flexibility such as standalone story calls and story mode sections, and the individual items in a chain can all have a separate `after_` label.
    * - String to filename conversion
      - Guest names and album names can be converted to a filename which the program can search for to find images associated with that name. `all_albums` definitions can be modified to reflect this.
    * - `persistent.testing_mode` improvements
      - Activating `Testing Mode` from the Developer options will now show a button to instantly end a chatroom. It also removes a lot of the confirm-style message and allows you to right-click an item on the timeline to instantly mark it as played for testing purposes.
    * - `persistent.unlock_all_story`
      - An option, Unlock All Story, in the Developer options will make all timeline items immediately available. Plot branches can be proceeded through without playing all prior items.
    * - Save slots
      - Save slots are now paged rather than one long list.
    * - `add_choices` for spaceship thoughts
      - Can now append a new choice to a list of spaceship thoughts.
    * - `main_character` variable
      - A character defined as the main character will say non-paraphrased dialogue automatically and be moved to the right side of the messenger.
    * - `persistent.pv`
      - `pv` (for chatroom speed) is now persistent and will carry over across playthroughs and on the history screens.

.. _other-3-0-0:

Other
--------------------

.. list-table::
    :widths: 15, 85
    :header-rows: 1

    * - **Feature**
      - **Description**
    * - Folder restructure
      - Engine code has been moved to the `01_mysme_engine` folder. Modifiable code, or code that is expected to be added to by the user, is directly inside the `game/` folder.
    * - Casual and Jaehee Route
      - A stub implementation of Casual Story and Jaehee Route is implemented as an example. Allows for easy testing of real-time mechanics and demonstrates a complete route definition with branches for multiple endings.
    * - `show_empty_menus`
      - Can choose whether timed menus with no choices (e.g. all choices have conditions which evaluate to False) should show their dialogue or be skipped altogether.
    * - Script error screen
      - The program will try to detect when you have made an error in your script and notify you or direct you to an appropriate wiki page rather than crashing.
    * - `missing_label` and `missing_image` callbacks
      - The program will try to correct and/or recover from missing labels or missing images without disrupting the program.
    * - `use_timed_menus`
      - `persistent.autoanswer_timed_menus` has been renamed to `persistent.use_timed_menus`. The preference option is titled Timed Menus.

.. _vars-3-0-0:

Renamed Variables
--------------------

.. list-table::
    :header-rows: 1

    * - **Old Name**
      - **New Name**
    * - post_chat_actions
      - reset_story_vars
    * - persistent.completed_chatrooms
      - persistent.completed_story
    * - plot_branch_end()
      - execute_plot_branch
    * - num_future_chatrooms
      - num_future_timeline_items
    * - chatroom_hg
      - collected_hg
    * - chatroom_hp
      - collected_hp
    * - chat_archive
      - story_archive
    * - .chatroom_label
      - .item_label
    * - most_recent_chat
      - most_recent_item
    * - current_chatroom
      - current_timeline_item
    * - screen chatroom_item
      - timeline_item_display
    * - screen chatroom_item_history
      - timeline_item_history
    * - screen chatroom_timeline
      - timeline
    * - next_chatroom
      - check_and_unlock_story
    * - next_chat_time
      - next_story_time
    * - chat_24_available
      - make_24h_available
    * - screen chat_select
      - day_select
    * - screen day_select
      - day_display
