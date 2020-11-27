# How Emails Work

**Example files to look at: [tutorial_2_emails.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/tutorial_day_scripts/tutorial_2_emails.rpy "tutorial_2_emails")**

After you define your guest and invite them to the party, the guest will immediately send the player an initial email. From this point onwards, if the player **does not** reply to the email, after every chatroom a variable attached to every Email object called `timeout_count` will decrease by 1. By default, it starts at 25. This number resets back to 25 as soon as the player replies to the email. However, if the timer reaches 0 (aka the player has gone through 25 chatrooms/VN sections since they first received the email), the email will be considered **timed out** and can no longer be replied to. If you'd like to change this number, look at the `Email` class, found in [email_system.rpy](https://github.com/shawna-p/mysterious-messenger/blob/master/game/email_system.rpy "email_system.rpy").

If the player *does* reply to the email, the program will calculate when it should return the guest's reply. For example, if there are 30 chatrooms left to be played through, and this is the first email reply in the chain (there are up to three total replies in a successful email chain), the program will determine that the maximum number of chatrooms it can wait before delivering the guest's reply is `30 / 3 = 10` chatrooms. It will then generate a number between 10 and `10 - 7 = 3`, and that number will be the number of chatrooms the program will wait before delivering the guest's reply to the player's inbox. This number is stored in the field `deliver_reply` and is decreased by 1 after every completed chatroom or VN.

The guest's odds of attending the party depend on several factors:

* If the player chooses the wrong response to the guests very first email, the guest will not attend the party
* If the guest's email chain has timed out, the guest will not attend the party
* If the player has not read the last reply in the chain, the guest will not attend the party.
  * This means that even if the player got all three responses correct, if they have not read the final email sent by the guest, that guest will not attend the party
* If the player got the first response right and the second incorrect, the guest has a 1 in 3 chance of attending the party. This is calculated as soon as the player inputs the wrong response.
* If the player gets the first two responses correct but the third response wrong, the guest has a 2 in 3 chance of attending the party. This is calculated as soon as the player inputs the incorrect response.
* If the player gets all three responses correct, the guest is guaranteed to attend the party

A guest will be unlocked in the guest book as soon as the player invites them to the party, but further information will only be unlocked if the guest actually attends the party.
