# Ending a Route

When the player has reached the end of the route, there is a special call to show the player an ending screen and return them to the main menu.

## Ending a Route after a VN

If you end the route after a VN, at the end of the VN label, write

```renpy
$ ending = 'good'
jump vn_end_route
```

where `'good'` is one of `'good'`, `'normal'`, or `'bad'`. It will show the correct ending screen before returning to the main menu.

## Ending a Route after a Chatroom

At the end of the chatroom label, write

```renpy
$ ending = 'bad'
jump chat_end_route
```

where `'good'` is one of `'good'`, `'normal'`, or `'bad'`. It will show the correct ending before returning to the main menu.
