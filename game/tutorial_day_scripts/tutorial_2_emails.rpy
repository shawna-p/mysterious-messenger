
label example_email():

    call chat_begin('evening') 
    call play_music(narcissistic_jazz)
    
    z 'Hey, [name], I had an idea for a guest we should invite.'
    z 'Can we invite zentherainbowunicorn?'
        
    call answer 
    # This tells the program not to shuffle the last choice
    $ shuffle = "last"  
    menu:
        "That sounds great!":
            m 'That sounds great!' (pauseVal=0)
            call invite(rainbow) # Use this to invite your guest
            z "Great! I'll tell her to send you a message."
        
        "I'll pass":
            m "I'll pass." (pauseVal=0)
            z "Oh, okay. No problem!"    
            
        # This is for testing; it both makes any emails you haven't
        # replied to timeout faster, and if you're waiting for the 
        # guest to email you, it makes them reply more quickly. 
        "I'd like to deliver my email replies more quickly." if email_list:
            m "I'd like to deliver my email replies more quickly." (pauseVal=0)
            z "Sure, I can take care of that."
            python:
                for email in email_list:
                    email.send_sooner()
            z "So what this does is decreases both the timeout countdown by 5,"
            z "And also decreases the number of chatrooms you need to go through to deliver the next email by 5."
            z "They'll decrease by an additional 1 when you exit this chatroom."
            z "In other words, guests will reply to you more quickly!"
    z "If you ever want to learn about inviting guests in the game,"
    z "there's a whole section on emails in the wiki."
    z "You can also look at {b}tutorial_2_emails.rpy{/b}"
    z "It shows how this invitation works,"
    z "and has a template to invite other people."
    z "Anyway, enjoy~!"
    
    call exit(z) 
            
    jump chat_end

## This is the 'expired' version of the chatroom
label example_email_expired():
    call chat_begin('evening')
    call play_music(narcissistic_jazz)
    z "Hey, [name], I had an idea for a guest we should invite." 
    z "Oh... [they_re] not here."   (bounce=True, specBubble="sigh_m")
    z "Hmm." 
    z "Well, you can always buy back this chatroom and let me know if you want to invite them or not!" 
    z "I'll see you around~"   (bounce=True, specBubble="flower_m")
    call exit(z)
    jump chat_end

## This is how you will set up guests for the party. A template follows 
## this definition. The first variable is the name of the guest, aka what 
## shows up in the email hub as @guestname The second variable is the path
## to the image you'd like to use as the guest icon. It should be 155x155 px
default rainbow = Guest("rainbow", 
    "Email/Thumbnails/rainbow_unicorn_guest_icon.png",

## Initial Message
"""Hi [name]!

Really excited to hear about this party you're holding! Can't wait to see how things will turn out for you.
Zen told me to make sure your inbox is working, and well, if you're reading this, I guess it is! So that's good.
I did have one quick question though -- will the party be held inside or outside? Please let me know as soon as possible!

Thanks,

Rainbow Unicorn""",

## FIRST MESSAGE - what kind of party?

## Answer -> Indoor Party
## First Message (correct)

"""Dear Rainbow,

I'm pleased to inform you that the party will be indoors. No need for umbrellas or sunscreen!
Hope to see you there,

Sincerely,

[name], the party coordinator""",

## Reply to correct message

"""Hi again,

Oh, how wonderful! I was worried about what the weather would be like on the day of the party.
I thought of another question: what kind of music will there be at the party?

Hope to hear from you soon,

Rainbow Unicorn""",

## Answer -> Outdoor Party
## First Message (incorrect)

"""Dear Rainbow,

We're planning for an outdoor party! There are gardens at the venue that will be perfect for an elegant party.
Hope to see you there!

Sincerely,

[name], the party coordinator""",

## Reply to incorrect message
    
"""Hi again,

Oh dear, I'm afraid I have terrible allergies and that may not work out well for me. I appreciate the time you've taken to email me but I may have to decline.

Thank you for the invitation, and best of luck to you and the party.

Rainbow Unicorn""",

## SECOND MESSAGE - what kind of music?

## Answer -> Smooth Jazz
## Second Message (correct)

"""Dear Rainbow,

We've got a wonderful playlist full of smooth jazz songs to play at the party. We're also looking into the possibility of a live band!
Hope that answers your question.

Sincerely,

[name]""",

## Reply to correct message

"""Dear [name],

Oh, that's just fantastic news. Jazz is such a lovely music genre, isn't it? Just between the two of us, I'm also quite partial to video game soundtrack music. But I don't expect you to play that at the party!
You've been so kind with your answers, and if you don't mind, I had one last question -- what sort of food will there be at the party? Please let me know when you can!

From, Rainbow""",

## Answer -> Heavy Metal
## Second Message (incorrect)

"""Hi Rainbow,

I've found some wonderful heavy metal music to play at the party! Screaming vocals really set the mood, don't you think? I hope you'll enjoy the music!

Sincerely,

[name], the party coordinator""",

## Reply to incorrect message

"""Hi again,

Oh dear, heavy metal? I can't say I enjoy that sort of music. I appreciate the invitation, but now that I know you'll be playing heavy metal music... I'll have to think more on it.

Thank you for your help.

Rainbow""",

## THIRD MESSAGE - what kind of food?

## Answer -> Spicy Food
## Third Message (correct)

"""To the lovely Rainbow,

There will be a delicious selection of spicy food at the party! In particular there will be experienced chefs from places such as India and Mexico who will be catering. I hope your taste buds are ready!

Sincerely,

[name]""",

## Reply to correct message

"""To [name],

Wow! I adore spicy foods; it's almost as though you read my mind! I will most certainly have to come and sample the dishes you've described.
Thank you very much for taking the time to answer my questions. I'll see you at the party!

Best,

Rainbow""",

## Answer -> Seafood
## Third Message (incorrect)

"""To the lovely Rainbow,

We're planning to serve a variety of seafood at the party! There will be plenty of dishes to try, like fried octopus, shrimp tempura, and caviar. Hope you come with an appetite!

From,

[name]""",

## Reply to incorrect message


"""To [name],

That certainly sounds... interesting! I can't really consider myself a fan of seafood, however, so you'll have to excuse me for my lack of enthusiasm.
That said, I do appreciate you taking the time to answer me. I'm a bit undecided on whether or not to attend, but wish you the best of luck with the preparations!

Sincerely,

Rainbow Unicorn""",

## These next fields are optional but used for the guestbook
## Large (usually chibi) image for the party, no wider than 
## 315px or so
"Email/Guest Images/rainbow_unicorn.png",

## Short description about the guest
"Rainbow Unicorn, the creator of this program.",

## Personal Info section on the guest
"Rainbow started working on this project back in 2018 and she's excited to share it with the world!",

## The ChatCharacter variable of the person who should talk about this 
## guest in the long description
z,

## What the previous character says about this guest
"Is Rainbow's name a reference to me? Haha, well, I am quite a rainbow unicorn if I do say so myself~",

## The expression/displayable name of the character to show
'zen front party happy',

## The name of the guest as it should appear in their
## dialogue box
"Rainbow",

## The dialogue the guest says when they attend the party
"Oh, it's so exciting to be at the party! I can't wait to see everyone."
)

# This needs to be the name of the guest + _reply + the reply number
# For example, if my guest is named Bob (with the capital B) and this
# is the first reply, it would be called Bob_reply1
# Be sure to pay attention to any capitals you have in the guest's name
# or the program won't be able to find the right label
label rainbow_reply1(): 

    menu:
        'Indoor party.':
            # Passing 'True' indicates that this is the correct reply
            $ current_email.set_reply(True) 
        
        'Outdoor party.':
            # Similarly, passing 'False' indicates this was the wrong reply
            # and will fail the email chain
            $ current_email.set_reply(False)            
        
    jump email_end
    

label rainbow_reply2():
    menu:
        # You can put the True and False answers in any order; the program
        # will shuffle the answers for you before showing them to the player
        'Smooth Jazz.':
            $ current_email.set_reply(True)
        'Heavy Metal.':
            $ current_email.set_reply(False)
    jump email_end
    
label rainbow_reply3():
    menu:
        'Spicy Food.':
            # You can also pass set_reply a number after True/False
            # If you do, that will be the number of chatrooms after 
            # which the reply to your email will be sent to you.
            # Otherwise, the program calculates an appropriate number
            # based on how many chatrooms are yet to be played
            $ current_email.set_reply(True, 1)
        'Seafood.':
            $ current_email.set_reply(False)
    jump email_end
    

## ****************************************************
## A TEMPLATE EMAIL GUEST
## ****************************************************

default example_guest = Guest("example", 
## The first string, "example", is what will show up in the 
## email chain as the guest's 'email' e.g. "longcat" shows up
## as "@longcat" in the email chain. This is also the variable
## you use for reply labels, not the name of the variable
"Email/Thumbnails/guest_unlock_icon.png",
## The second string is the image to use for the guest's 
## thumbnail. It should be 155x155px
## Because the variable is 'example_guest', when you want to 
## invite this person, you will write: call invite(example_guest)

## Initial Message
"""Dear [name],

You can write whatever you want in here. It is the first message that is sent
to you after you invite the guest. Note that any new lines you write here will
be new lines in the actual email; you can look to the previous guest for ideas
on formatting. This example simply has breaks in the middle of lines to make
it easier to read when editing code.

From, your example guest""", # don't forget the comma after the quotes

## FIRST MESSAGE - *Question the guest asked here*

## It's a good idea to write down what the answer is to get to this response
## in the comments so you don't forget
## Answer -> CORRECT ANSWER HERE
## First Message (correct)

"""This is what your character will send the guest after selecting the correct
response to the email. You can use their name in the email by typing [name]""", 

## Reply to correct message

"""This is what the guest will send you after you replied 
to their first email correctly""",

## Answer -> INCORRECT ANSWER HERE
## First Message (incorrect)

"""This is what your character writes to the guest when they 
choose the wrong response""",

## Reply to incorrect message
    
"""And this is the response the guest will write you after you choose
the incorrect response. Usually they say something that indicates they 
don't want to go to the party""",

## SECOND MESSAGE - *Question the guest asked here*

## Answer -> CORRECT ANSWER HERE
## Second Message (correct)

"""This is your message to the guest with the correct response""",

## Reply to correct message

"""This is the guest's reply to your message after you choose the 
correct response""",

## Answer -> INCORRECT ANSWER HERE
## Second Message (incorrect)

"""This is your message to the guest with the incorrect response""",

## Reply to incorrect message

"""This is the guest's reply to your message after you choose the 
wrong response""",

## THIRD MESSAGE - *Question the guest asked here*

## Answer -> CORRECT ANSWER HERE
## Third Message (correct)

"""This is your message to the guest with the correct response""",

## Reply to correct message

"""This is the guest's reply to your message after you chose the 
correct response. It usually says something about seeing you at 
the party, as this is the final message""",

## Answer -> INCORRECT ANSWER HERE
## Third Message (incorrect)

"""This is your message to the guest with the incorrect response""",

## Reply to incorrect message

"""This is the guest's reply to your message after you choose 
the wrong response."""

## These next fields are optional but used for the guestbook
## Large (usually chibi) image for the party, no wider than 315px
"Email/Guest Images/rainbow_unicorn.png",

## Short description about the guest
"Example Guest, an example guest for this program.",

## Personal Info section on the guest
"Example Guest was made for users to better understand how to create a guest",

## The ChatCharacter variable of the person who should talk about this 
## guest in the long description
s,

## What the previous character says about this guest
"Here, the character from the last variable (seven) will say this.",

## The expression/displayable name of the character to show
'seven front party happy',

## The name of the guest as it should appear in their
## dialogue box
"Example Guest",

## The dialogue the guest says when they attend the party
"The guest will probably mention something about the party."
) # Don't forget a closing bracket at the end

label example_reply1(): 
    # The guest is called "example", so the
    # reply labels will be called
    # example_reply1, example_reply2, and example_reply3

    menu:
        "Answer 1":
            # Passing 'True' indicates that this is the correct reply
            # Either answer can be correct, not necessarily the first option
            # The program will randomly shuffle the answers when showing
            # them to the user
            $ current_email.set_reply(True) 
        
        "Answer 2":
            # Similarly, passing 'False' indicates this was the wrong reply
            # and will fail the email chain
            $ current_email.set_reply(False)            
        
    jump email_end # This ensures your response is saved after you reply
    
label example_reply2(): 

    menu:
        "Answer 1":
            $ current_email.set_reply(True) 
        
        "Answer 2":
            $ current_email.set_reply(False)          
        
    jump email_end
    
label example_reply3(): 

    menu:
        "Answer 1":
            $ current_email.set_reply(True) 
        
        "Answer 2":
            $ current_email.set_reply(False)    
            
    jump email_end


