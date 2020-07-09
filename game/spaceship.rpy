
init python:

    def spaceship_xalign_func(trans,st,at):
        """Make the spaceship float to a random location on the line."""

        global spaceship_xalign
        if st > 1.0:
            trans.xalign = spaceship_xalign
            return None
        else:
            trans.xalign = spaceship_xalign * st
            return 0
    
        trans.xalign = spaceship_xalign
        return None
        
    def spaceship_get_xalign(new_num=False):
        """
        Return a random position along the spaceship line at the bottom
        of the screen to move the spaceship to.
        """

        global spaceship_xalign
        if new_num:
            spaceship_xalign = renpy.random.random()
            spaceship_xalign = spaceship_xalign * 0.8 + 0.04
        return spaceship_xalign
        
    class RandomBag(object):
        """
        Class that is used to create a 'random bag' of supplied choices.

        Attributes:
        -----------
        choices : list
            A list of choices. Can be booleans, strings, ints, a mix, etc.
        bag : list
            A shuffled list of the provided choices.
        """

        def __init__(self, choices):
            """Creates a RandomBag object."""
            
            # The choices that go into the bag.
            self.choices = choices                        
            # A shuffled list of things in the bag.
            self.bag = [ ]                                

        def draw(self):
            """Removes an item from the bag."""

            # If the bag is empty,
            if not self.bag:                              
                # Replace it with a copy of choices,
                self.bag = list(self.choices)             
                 # Then randomize those choices.
                renpy.random.shuffle(self.bag)           

            # Return something from the bag.
            return self.bag.pop(0)                        
            
        def new_choices(self, choices):
            """Reset the bag with new choices."""

            self.choices = choices
            self.bag = list(self.choices)
            renpy.random.shuffle(self.bag)
            
    class SpaceThought(renpy.store.object):
        """
        Class which keeps track of 'Space Thoughts' in order to show the
        correct image + text combo to the player.

        Attributes:
        -----------
        char : ChatCharacter
            The character having this thought.
        thought : string
            The thought for this character.
        img : string
            The image used as the background for this thought.
        """

        def __init__(self, char, thought):
            """Creates a SpaceThought object."""

            self.char = char
            self.thought = thought
            self.img = char.file_id + '_spacethought'

        
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
        
        frame:
            xysize (680, 374)
            align (0.5, 0.5)
            background the_thought.img
            text "The spaceship's sensors have caught the RFA members' meaningless thoughts." style 'space_title1'
            
            frame:
                xysize (651, 240)
                align (0.5, 0.7)
                text the_thought.thought style 'space_thought_mid'
            
            text "The spaceship does not always move forward... it orbits around :D" style 'space_title2'
    

style space_title1:
    font gui.serif_1
    size 25
    text_align 0.5
    align (0.5, 0.12)
    color '#ff0'
    
style space_thought_mid:
    font gui.serif_1
    text_align 0.5
    align (0.5, 0.5)
    color '#fff'
    
style space_title2:
    font gui.serif_1
    size 22
    text_align 0.5
    align (0.5, 0.95)
    outlines [(absolute(1), '#743801', absolute(0), absolute(0))]
    color '#fff'
    

#########################################################
## Additional screens for the Honey Buddha Chip animation
#########################################################
screen chip_tap():

    modal True

    zorder 100
    
    add "choice_darken"
    fixed at chip_wobble:
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
    fixed at chip_wobble2:
        xysize(481,598)
        xalign 0.5
        yalign 0.6
        add "space_chip"
    
    fixed at hide_dissolve:
        xysize(750,640)
        xalign 0.5
        yalign 0.6
        add 'cloud_1' xpos 735 ypos 500 at cloud_shuffle1
        add 'cloud_2' xpos -20 ypos 310 at cloud_shuffle2
        add 'cloud_3' xpos 10 ypos 300 at cloud_shuffle3
        add 'cloud_4' xpos 300 at cloud_shuffle4
        add 'cloud_5' xpos 350 ypos 20 at cloud_shuffle5
        

label hbc_helper():
    $ prize = chip_prize_list.draw()
    $ prize_text = prize[0]
    # Add a bit of randomness to the heart payout
    $ prize_heart = (prize[1] 
        + (renpy.random.randint(0, prize[1]//10) 
            * renpy.random.choice([1, -1])))
    $ prize_hg = prize[2]

    $ new_hp_total = persistent.HP + prize_heart
    $ new_hg_total = persistent.HG + prize_hg

    call screen chip_end(prize_heart, prize_hg, new_hp_total, 
                         new_hg_total, prize_text)
    call screen chat_home()
    return

screen chip_end(prize_heart, prize_hg, new_hp_total, new_hg_total, prize_text):
    modal True

    zorder 100
    
    add "choice_darken"   

    add 'spotlight' xalign 0.5 yalign 0.0
    
    frame:
        xysize(481,598)
        xalign 0.5
        yalign 0.6
        add "space_chip"
        
    frame:
        xysize(647,270)
        xalign 0.5 yalign 0.55
        background 'space_prize_box'
            
        hbox:
            spacing 70
            xalign 0.5
            yalign 0.55
            frame:
                xysize(200,60)
                background 'space_black_box'
                text str(prize_heart) style 'chip_prize_text'
                add 'header_heart' xalign 0.15 yalign 0.5
                
                
            frame:
                xysize(200,60)
                background 'space_black_box'
                text str(prize_hg) style 'chip_prize_text'
                add 'header_hg' xalign 0.15 yalign 0.5
                
        frame:
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
                    SetField(persistent, 'HG', new_hg_total), 
                    Hide('chip_end'), 
                    SetVariable('chips_available', False), 
                    FileSave(mm_auto, confirm=False),
                    renpy.retain_after_load(),
                    Return()]

style chip_prize_text:
    color "#ffffff"
    font gui.sans_serif_1
    text_align 1.0
    size 37
    xalign 0.85
    yalign 0.5
    
style chip_prize_description_short:
    color '#ffffff'
    font gui.blocky_font
    text_align 0.5
    size 45
    xalign 0.5
    yalign 0.5

style chip_prize_description_long:
    color '#ffffff'
    font gui.blocky_font
    text_align 0.5
    size 37
    xalign 0.5
    yalign 0.5


    
    