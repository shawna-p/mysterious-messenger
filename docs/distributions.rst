==============
Distributions
==============

If you would like to package up the engine to distribute to personal acquaintances, there are some options for developers that you may want to turn off or modify.

In ``variables_editable.rpy``, there is a section near the top with the header ``## FOR RELEASE``. Here, several values are set before the game starts.

* ``persistent.testing_mode`` - Typically, for a release, you will want this to be False. This variable toggles on some options which are useful for testing, such as allowing you to skip to the end of a chatroom, and also makes it so that chatrooms can be endlessly replayed and never expire.