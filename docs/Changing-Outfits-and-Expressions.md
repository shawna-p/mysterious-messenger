# Changing Outfits and Expressions

**Example files to look at: [tutorial_6_meeting.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_6_meeting.rpy "tutorial_6_meeting"), [tutorial_3b_VN.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_3b_VN.rpy "tutorial_3b_VN")**

To show a character, look at [character_definitions.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/character_definitions.rpy "character_definitions.rpy") and find the character you want to show under the **Character VN Expressions Cheat Sheet** header.

To show a character, use their name tag (usually their first name) + any additional expression, position, outfit, or accessory tags as applicable. In practice, this means if you want to show `jaehee` with the expression `happy` and wearing her `glasses`, write

```renpy
show jaehee glasses happy
```

Since Jaehee does not have any additional positions (such as a "side" or "front" position), you don't need to include that when you show her on-screen. However, a character like V *does* have multiple positions, and so a similar statement for him would look like

```renpy
show v side angry glasses
```

where `v` is the character, `side` is the position, `angry` is his expression, and `glasses` indicates he should be shown wearing glasses.

To change the character's outfit, when you show them you should include the attribute name of the outfit you'd like them to wear e.g.

```renpy
show yoosung suit surprised
```

In this case, `yoosung` is the character, `suit` is his outfit, and `surprised` is his expression.

Note that attributes can be listed in any order after the character, so `show yoosung surprised suit` is equally correct.

Characters with accessories (glasses, hoods, masks) can include those keywords as well e.g.

```renpy
show v front mint_eye worried hood_up at vn_right with easeinright
```

which will show `V` in his `front` position wearing his `mint_eye` cloak with the `hood_up` at the position `vn_right` after being "eased in" (`easeinright`) from the right side of the screen.

Luckily, after you've shown a character on-screen the first time, Ren'Py will remember which attributes you showed them with so that you don't have to write out the whole attribute list every time after that. For example

```renpy
show v front mint_eye worried hood_up at vn_right with easeinright
v "Some sample dialogue."
show v thinking
v "More dialogue."
```

The second `show` statement remembers the attributes `v` was shown with previously, namely `front mint_eye hood_up` since the `thinking` expression replaces the `worried` expression. So he will still be shown in his front position with the mint_eye cloak and his hood_up, just with the `thinking` expression.

## Attribute Shorthand

There is also another way of simplifying showing characters even further -- since characters are defined with an "image" tag in mind, after showing them on screen the first time you can change tags directly during dialogue like so:

```renpy
show seven front happy party
s "Some dialogue while happy."
s worried "Some dialogue with the party outfit in the front pose, but worried."
s normal "Now in the normal outfit, and still worried and in the front position."
```

Note that you can only change expressions this way after the character has already been shown on-screen.

For more on Image Attributes, see the [Ren'Py documentation pages on Dialogue and Narration](https://www.renpy.org/doc/html/dialogue.html?highlight=attribute#say-with-image-attributes "Ren'Py Dialogue and Narration documentation").

## Hiding Characters

When you're done showing a character on-screen, you only have to use their name to hide them:

```renpy
show seven front happy party
s "Some dialogue while happy."
hide seven
```
