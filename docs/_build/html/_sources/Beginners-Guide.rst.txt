.. _beginners-guide:

================
Beginner's Guide
================

If you want to create your own route and some of the technicalities are going over your head, this guide will take you through setting up a new route from start to finish. More specific pages will be referenced throughout. If you already know a bit about the program, you may want to start with [Setting up Sequential Chatrooms](Setting-up-Sequential-Chatrooms.md) instead.

.. toctree::
    :caption: Navigation

    beginners-guide


Getting Started
===============

If you've downloaded the program and assets (or created your own replacement assets), the first thing you should do is hit ``Launch`` from the Ren'Py launcher and play through the Tutorial Day to get a feel for what the program is capable of.

Opening the code in a code editor
---------------------------------

Next, you need to create a new ``.rpy`` file. This is where you will write the code that will tell Mysterious Messenger how you want your route to be set up. If you have a program to edit code in, such as VS Code or Atom, you should open that program. Otherwise, you can either download an editor online or tell Ren'Py to download it for you.

To get Ren'Py to download an editor for you, in the Ren'Py launcher under ``Preferences`` there is an option called ``Text Editor``. Click on that, and you'll see a variety of suggested editors. Of these, I recommend downloading Atom. Otherwise, you can tell Ren'Py to use the System Editor, and then when you double-click a ``.rpy`` file in the ``mysterious-messenger/game`` folder, tell it to always open ``.rpy`` files with your editor of choice.

``Return`` to the main screen of the Ren'Py launcher. Next, in your file explorer, open the ``mysterious-messenger/game`` folder. To keep things organized, you should create a new folder here. Call it ``my_new_route``.

Now you can open your code editing program and use ``File -> Open Folder...`` to navigate to the ``mysterious-messenger/game/my_new_route`` folder. It's blank for now, but you will add ``.rpy`` files to it soon.

Creating a new .rpy file
------------------------

Inside your code editor, you can use ``File -> New File``. Name this file ``my_route.rpy``. Don't forget you need to include ``.rpy`` at the end so the editor and program understand this file contains code for Ren'Py.

Defining the route
==================

Inside your new ``.rpy`` file, copy and paste the following code::

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

This defines a variable which is going to contain the information the program needs to understand how to display the route to the player. In particular, this defines the "Good End" of a route. In the history screen, when the player reaches the end of this route the final timeline item will show up under the title "Good End". This guide only covers how to add one ending, but if you want to learn more you can refer to the [Setting up Sequential Chatrooms](Setting-up-Sequential-Chatrooms.md) page.




A section
=========

A subsection
------------

A sub-subsection
^^^^^^^^^^^^^^^^


