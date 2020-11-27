# Creating the Party

**Example Files to look at: [tutorial_8_plot_branches.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_8_plot_branches.rpy "tutorial_8_plot_branches")**

The party at the end of a route functions almost exactly the same as any other VN section. The only real difference is how the icon itself displays.

To create the party, you just need to name the label correctly. If the chatroom before the party is called

```renpy
label my_chat:
```

then the party will be found at

```renpy
label my_chat_party:
```

Before the party, the player will automatically be shown which guests are attending the party and it will unlock them in the guestbook. Since this is likely the end of the route, you should take a look at [Ending a Route](Ending-a-Route.md) for more information on that.

Note that if you want to do any final "checks" before starting the party, you should put them at the beginning of the `_party` label. For example, you can check how many guests the player has successfully invited:

```renpy
label my_chat_party:
    if attending_guests() >= 10:
        jump my_party_good_end
    else:
        jump my_party_bad_end

label my_party_good_end:
    # Your party VN here

label my_party_bad_end:
    # Your party VN here
```
