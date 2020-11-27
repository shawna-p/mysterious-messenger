# Adding Spaceship Thoughts for a New Chatroom

First, go to [spaceship_variables.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/spaceship_variables.rpy "spaceship_variables.rpy"). Under the heading **Spaceship thought images** you will see several images defined.

For the purposes of this tutorial, these examples will show how to add a character named Bob to the program.

At the end of the declarations, add another image for Bob, using his file_id for the name + "_spacethought".

```renpy
image b_spacethought = "Menu Screens/Spaceship/b_spacethought.png"
```

This image should be 651x374 pixels and will be shown behind the thought the character has when the spaceship icon is clicked.

You can then give Bob a `SpaceThought` when updating the `space_thoughts` list, which is found at the top of the file e.g.

```renpy
default space_thoughts = RandomBag( [
    SpaceThought(b, "Your thought here."),
    SpaceThought(b, "More thoughts.")
])
```
