# How Text Message Delivery Works

When you write text messages in the `after_` label that are to be sent to the player, those messages are added to a 'queue' which is delivered to the player in increments after they finish playing the associated chatroom/VN. So, if you composed text messages from characters A, B, and C, the player may receive Character A's message immediately upon returning to the 'home' screen, and then will receive Character B and C's messages either by waiting around on the home screen or performing other actions such as replying to other text messages or emails.

Similarly, if the player has replied to Character A's message, Character A's response gets added to the queue and will be eventually delivered to the player after some time has passed.

All text messages in the queue are immediately delivered as soon as the player clicks to enter the chatroom timeline screen.

In this program, there is no time limit on when you can or can't reply to text messages. However, if a character sends the player a new text message and they haven't replied to the previous conversation, they will no longer be able to continue that older conversation.
