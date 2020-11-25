# Spaceship Thoughts

**Example files to look at: [tutorial_6_meeting.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_6_meeting.rpy "tutorial_6_meeting")**

When the floating spaceship isn't giving out chips, you can click it to view a random thought from one of the characters. You can find the existing variable definitions in [spaceship_variables.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/spaceship_variables.rpy "spaceship_variables.rpy").

The variable `space_thoughts` can be modified to change the spaceship thoughts the player sees upon starting the game, or you can modify them in the `after_` label of any chatroom. You can have as many or as few `SpaceThought` objects in the list as you like -- even multiple thoughts for the same character. A `SpaceThought` only has two fields -- the first is the ChatCharacter variable of the character whose thought it is, and the second is the thought itself.

SpaceThought |
-------------|
`char, thought` |

To change the spaceship thoughts, in the `after_` label of the chatroom after which you want the spaceship thoughts to change, add the line

```renpy
$ space_thoughts.new_choices([
    SpaceThought(ja, "New thought here.")
])
```

You can add more `SpaceThought` objects to the list, separating them with commas. This line will clear the previous list of thoughts and replace it with your new list after the player has gone through the chatroom (and the VN mode as well, if there is one).
