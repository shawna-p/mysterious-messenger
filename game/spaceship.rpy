
init python:

    # This is used to make the spaceship float to a random 
    # location on the line
    def spaceship_xalign_func(trans,st,at):
        if st > 1.0:
            trans.xalign = spaceship_xalign
            return None
        else:
            trans.xalign = spaceship_xalign * st
            return 0
    
        global spaceship_xalign
        trans.xalign = spaceship_xalign
        return None
        
    # Returns a random position along the spaceship line at the bottom
    # of the screen
    def spaceship_get_xalign(new_num=False):
        global spaceship_xalign
        if new_num:
            spaceship_xalign = renpy.random.random()
            spaceship_xalign = spaceship_xalign * 0.8 + 0.04
        return spaceship_xalign
        
    # This code is used to create a 'random' function that
    # will occasionally activate the Honey Buddha Chip bag
    class RandomBag(object):

        def __init__(self, choices):
            # The choices that go into the bag.
            self.choices = choices                        
            # A shuffled list of things in the bag.
            self.bag = [ ]                                

        def draw(self):
            # If the bag is empty,
            if not self.bag:                              
                # Replace it with a copy of choices,
                self.bag = list(self.choices)             
                 # Then randomize those choices.
                renpy.random.shuffle(self.bag)           

            # Return something from the bag.
            return self.bag.pop(0)                        
            
        # Reset the bag with new choices
        def new_choices(self, choices):                   
            self.choices = choices
            self.bag = [ ]
            
    # This class keeps track of "Space Thoughts" in 
    # order to show the correct image + text combo
    # to the player
    class SpaceThought(object):
        def __init__(self, char, thought):
            self.char = char
            self.thought = thought
            self.img = char.file_id + '_spacethought'
            
# This is what a list of thoughts for the spaceship will 
# look like
default space_thoughts = RandomBag( [
    SpaceThought(ja, "I should have broken these shoes in better before wearing them to work today."),
    SpaceThought(ju, "I wonder how Elizabeth the 3rd is doing at home."),
    SpaceThought(s, "Maybe I should Noogle how to get chip crumbs out of my keyboard..."),
    SpaceThought(y, "Yes! Chocolate milk is on sale!"),
    SpaceThought(z, "Maybe I should learn how to braid my hair..."),
    SpaceThought(r, "I can't believe I accidentally used one of the other Believer's shampoo. My hair smells like lemons."),
    SpaceThought(ri, "Hmm... the soup tastes different today."),
    SpaceThought(sa, "So... sleepy..."),
    SpaceThought(v, "The weather is so very lovely today. Maybe I'll go for a walk.") 
    ] )
        
#########################################################
## Floating spaceship thoughts
#########################################################

screen spaceship_thoughts():
    
    modal True
    
    $ the_thought = space_thoughts.draw()
            
    button:
        background "choice_darken"
        xysize (750, 1334)
        activate_sound 'audio/sfx/UI/select_6.mp3'
        action Hide('spaceship_thoughts', Dissolve(0.5))
        
        window:
            xysize (680, 374)
            align (0.5, 0.5)
            background the_thought.img
            text "The spaceship's sensors have caught the RFA members' meaningless thoughts." style 'space_title1'
            
            window:
                xysize (651, 240)
                align (0.5, 0.7)
                text the_thought.thought style 'space_thought_mid'
            
            text "The spaceship does not always move forward... it orbits around :D" style 'space_title2'
    



#########################################################
## Additional screens for the Honey Buddha Chip animation
#########################################################
screen chip_tap():

    modal True

    zorder 100
    
    add "choice_darken"
    window at chip_wobble:
        xysize(481,598)
        xalign 0.5
        yalign 0.6
        imagebutton:
            idle "space_chip"
            activate_sound 'audio/sfx/UI/select_6.mp3'
            action Jump('chip_prize')
        add 'space_tap_large' at large_tap
        add 'space_tap_med' at med_tap
        add 'space_tap_small' at small_tap
        
    
 
label chip_prize():
    #$ reset_spaceship_pos = True
    #$ spaceship_xalign = 0.04
    hide screen chip_tap
    show screen chip_cloud
    show screen chat_home(True)
    pause 2.5
    hide screen chip_cloud 
    $ chips_available = False
    jump hbc_helper
 
screen chip_cloud():
    modal True

    zorder 100
        
    add "choice_darken"
    window at chip_wobble2:
        xysize(481,598)
        xalign 0.5
        yalign 0.6
        add "space_chip"
    
    window at hide_dissolve:
        xysize(750,640)
        xalign 0.5
        yalign 0.6
        add 'cloud_1' xpos 735 ypos 500 at cloud_shuffle1
        add 'cloud_2' xpos -20 ypos 310 at cloud_shuffle2
        add 'cloud_3' xpos 10 ypos 300 at cloud_shuffle3
        add 'cloud_4' xpos 300 at cloud_shuffle4
        add 'cloud_5' xpos 350 ypos 20 at cloud_shuffle5
        

label hbc_helper():
    # Picks a number between 1 and 130 for the chip prize
    $ prize_heart = renpy.random.randint(1, 130)
    $ new_hp_total = persistent.HP + prize_heart
    # Picks a phrase for the item
    $ prize_text = chip_prize_list.draw()
    call screen chip_end(prize_heart, new_hp_total, prize_text)
    call screen chat_home()
    return

screen chip_end(prize_heart, new_hp_total, prize_text):
    modal True

    zorder 100
    
    add "choice_darken"   

    add 'spotlight' xalign 0.5 yalign 0.0
    
    window:
        xysize(481,598)
        xalign 0.5
        yalign 0.6
        add "space_chip"
        
    window:
        xysize(647,270)
        xalign 0.5 yalign 0.55
        background 'space_prize_box'
            
        hbox:
            spacing 70
            xalign 0.5
            yalign 0.55
            window:
                xysize(200,60)
                background 'space_black_box'
                text str(prize_heart) style 'chip_prize_text'
                add 'header_heart' xalign 0.15 yalign 0.5
                
                
            window:
                xysize(200,60)
                background 'space_black_box'
                # You could give out hourglasses here too, but since I've
                # never gotten one from the HBC animation I've just left
                # it permanently at 0
                text '0' style 'chip_prize_text'
                add 'header_hg' xalign 0.15 yalign 0.5
                
        window:
            xysize(600,100)
            align(0.5, 0.05)
            if len(prize_text) > 50:
                text prize_text style 'chip_prize_description_long'
            else:
                text prize_text style 'chip_prize_description_short'
        imagebutton:
            idle 'space_continue'
            hover 'space_continue_hover'
            xalign 0.5
            yalign 0.85
            action [SetField(persistent, 'HP', new_hp_total), 
                    Hide('chip_end'), 
                    SetVariable('chips_available', False), 
                    FileSave(mm_auto, confirm=False),
                    renpy.retain_after_load(),
                    Return()]
        
   
default chip_prize_list = RandomBag( ['A clump of cat hair.',
    "Jumin's old toothbrush.",
    "Some Honey Buddha Chip crumbs.",
    "Jaehee's spare pair of glasses.",
    "Yoosung's left sock."] )
    # Feel free to add more things
    
    