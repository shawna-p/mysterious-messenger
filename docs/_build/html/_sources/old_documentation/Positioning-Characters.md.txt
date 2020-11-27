# Writing a VN Section

**Example files to look at: [tutorial_6_meeting.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_6_meeting.rpy "tutorial_6_meeting"), [tutorial_3b_VN.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_3b_VN.rpy "tutorial_3b_VN")**

There are several pre-defined positions you can move the characters to. These are:

* vn_farleft
* vn_left
* vn_midleft
* vn_center
* vn_midright
* vn_right
* vn_farright
* default

Not every position will work for every character due to spacing and differences in sprite design. You can define more positions in [vn_mode.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/vn_mode.rpy "vn_mode.rpy") under **Transforms/VN Positions**.

`vn_center` is a unique position because it moves the character closer to the screen in addition to centering them. It's often used to imply the character is talking directly to the player. However, if you want to move a character who is currently shown in the `vn_center` position to another position, you have to `hide` them first. See the example files for examples of this.

To show a character at a given position, write

```renpy
show jumin front at vn_right
```

where `jumin front` is the name + attributes of the character you want to show (e.g. expressions, outfits, etc), and `vn_right` is the position to show them in. You can also add a transition like so:

```renpy
show jumin side happy at vn_left with ease
```

where `ease` is a transition. (See [Transitions](https://www.renpy.org/doc/html/transitions.html) in the Ren'Py documentation for more).
