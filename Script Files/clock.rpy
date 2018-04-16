## This code is slightly modified from trooper6's clock code found on the 
## Lemma Soft forums

init -2:
    style digi_clock:
        is default
        font "00 fonts/SamsungSans-Light.ttf"
        color "#ffffff"
        yalign 0.5

init -1 python:
    from datetime import datetime #This is to get the real world datetime
    
    img = ["00 images/VintageClockBase450x450.png", "00 images/VintageClockHour450x450.png", 
        "00 images/VintageClockMinute450x450.png", "00 images/VintageClockSecond400x400.png", 
        "00 images/DigitalClockBase460x200.png"]
    """
    Use your own clock images here, or use the ones I provided.
    Note: your analogue clock images need to be square, your digital base can be 
    any size but keeping it close to the ratio of 460x200 gives the best results.
    Important: You should have four images listed in this order--The Analogue 
    Clock Base, The Hour Hand, The Minute Hand, The Second Hand, The Digital Clock Base
    """
    renpy.music.register_channel("TockBG", mixer= "sfx", loop=True)
    renpy.music.register_channel("ChimeBG", mixer= "sfx", loop=False, tight=True) 
    renpy.music.register_channel("Alarm", mixer= "sfx", loop=False, tight=True)   
    """These are here so that the various clock sounds play on their own sound channels."""
    
    def clock_audio_pause(): #I use this to pause the audio of the clock when I go to various screens, this is also why it isn't part of the clock, but this in the demo?
        try:
            myClock.a_sound_on(False, False)
        except:
            pass
    
    """As a Creater Defined Displayable this needs to extend the Displayable class)"""
    class Clock(renpy.Displayable):
        
        #The clock class constructor
        def __init__(self, ana=True, h=0, m=0, resize=150, sH=True, mil_time=False, **kwargs):
            """
            This constructor takes the following arguments:
            ana = True gives the analogue version of the clock, False gives digital
            h=Hours the clock should start on
            m=Minutes the clock should start on
            resize=How big you want your clock images to be
            sH=If you want the second hand to be visible or not
            If you do not give any arguments when you create the clock, it will default to
             a clock with 0 hours, 0 minutes, 150 pixels square, with a second hand showing
            """
            super(Clock, self).__init__(**kwargs)
            
            #These lines are for setting up the images used and the size of them
            self.width = resize
            self.d_height = (resize*32)/100
            self.base_image = im.Scale(img[0], resize, resize)
            self.hour_hand_image = im.Scale(img[1], resize, resize)
            self.minute_hand_image = im.Scale(img[2], resize, resize)
            self.second_hand_image = im.Scale(img[3], resize, resize)
            self.digital_base_image = im.Scale("00 images/DigitalClockBase460x200.png", 
                self.width, self.d_height)
            self.offset = (resize*2**0.5-resize)/2
            self.second_hand_visible = sH
 
            #Variables for handling time
            self.minutes = (h*60)+m 
            self.seconds = self.minutes*60
            self.seconds_target = 0 
            self.step = 0 
            self.old_second = None #Used in autorun
            self.alarm_hr = 0
            self.alarm_min = 0
            
            #Variables for determining the clock modes
            self.analogue = ana
            self.auto_run = False
            self.realtime_run = False
            self.forward = True
            self.mil_time = mil_time

            #Variables for handling sound
            self.second_sound_on = False
            self.chime_on = False
            self.last_minute = 0 #Used for chimes
            self.play_chime = False #Chimes are currenlty running or not
            self.alarm_on = False
            self.last_aminute = 0 #Used for alarm
            self.play_alarm = False #Used for alarm
                    
        # Function that continuously updates the graphics of the clock
        def render(self, width, height, st, at):
            if self.seconds_target:
                if self.forward:
                    #Advances the seconds variable until it is the same as the seconds_target variable
                    if self.seconds_target > self.seconds:
                        self.seconds += self.step
                    #Resets the seconds_target variable
                    if self.seconds_target <= self.seconds:
                        self.seconds_target = 0
                else:   
                    if self.seconds_target < self.seconds:
                        self.seconds -= self.step
                    if self.seconds_target >= self.seconds:
                        self.seconds_target = 0
                        self.forward = True
            #Makes sure the minutes variable is always in sync with the seconds variable
            if self.minutes != self.seconds//60:
                self.minutes = self.seconds//60
                
            # Calculating how many seconds have passed today.
            if self.seconds >= 86400:
                self.seconds -= 86400

                if self.seconds_target:
                    self.seconds_target -= 86400
    
            elif self.seconds < 0:
                self.seconds += 86400
                
                if self.seconds_target:
                    self.seconds_target += 86400
                    
            #This is all the render information for the Analogue Clock
            if self.analogue:                
                # Create transform to rotate the second hand
                tM = Transform(child=self.minute_hand_image, rotate=self.seconds*0.1, 
                    subpixel=True)
                tH = Transform(child=self.hour_hand_image, rotate=self.seconds*0.008333, 
                    subpixel=True)

                # Create a render for the children.
                base_render = renpy.render(self.base_image, width, height, st, at)
                minute_render = renpy.render(tM, width, height, st, at)
                hour_render = renpy.render(tH, width, height, st, at)
            
                #If we are in chime_run mode, checks to see the chimes need to be rung
                if self.chime_on == True:
                    if self.last_minute != self.minutes:
                        self.play_chime = False
                        self.last_minute = self.minutes
                    self.start_chime()

                # Create the render we will return.
                render = renpy.Render(self.width, self.width)

                # Blit (draw) the child's render to our render.
                render.blit(base_render, (0, 0))
                render.blit(minute_render, (-self.offset, -self.offset))
                render.blit(hour_render, (-self.offset, -self.offset))
                
                #If the second hand is visible: renders, transforms, and adds it to our clock
                if self.second_hand_visible:
                    tS = Transform(child=self.second_hand_image, rotate=self.seconds*6, 
                        subpixel=True)
                    sec_render = renpy.render(tS, width, height, st, at)
                    render.blit(sec_render, (-self.offset, -self.offset))
            #This is all the render information for the Digital Clock
            else:
                # create the text that will go in the Digital Clock and boxes text sits in 
                ftht = self.d_height * 0.6
                col =Text(":", style="digi_clock", size=ftht)  
                time = list(Text("{0:02d}".format(item), style="digi_clock", size=ftht) 
                    for item in self.get_time())
                fxsize = (self.width-10)//4
                
                # Determine what to display based on if the seconds are  visible
                if self.second_hand_visible:
                    digi_text = HBox(Fixed(time[0], xsize=fxsize), col, Fixed(time[1], 
                        xsize=fxsize), col, Fixed(time[2], xsize=fxsize), xalign=0.5)
                else:
                    digi_text = HBox(Fixed(time[0], xsize=fxsize), col, Fixed(time[1], 
                        xsize=fxsize), xalign=0.5)
                
                #Put all of our pieces into one Fixed Box
                digi = Fixed(self.digital_base_image, digi_text, xysize=(self.width, 
                    self.d_height)) 
                #Create a render for our Fixed Box
                digi_render = renpy.render(digi, width, height, st, at)
                    
                # Create the render we will return.
                render = renpy.Render(self.width, self.d_height)

                # Blit (draw) the child's render to our render.
                render.blit(digi_render, (0,0))
                
            #Runs the realclock and autoclock functions 
            if not self.seconds_target:
                self.realclock()
                self.autoclock(st)

            #If we are in alarm_on mode, checks to see the alarm need to be rung
            if self.alarm_on == True:
                if self.last_aminute != self.minutes:
                    self.play_alarm = False
                    self.last_aminute = self.minutes
                self.start_alarm()
                    
            #This makes sure our object redraws itself after it makes changes
            renpy.redraw(self, 0)

            # Return the render.
            return render
          
        #####These are methods you can call to do things when using the clock            
        #Returns the current hours, minutes, and seconds of the clock
        def get_time(self):
            h, m = divmod(self.minutes, 60)
            h = int(h)
            m = int(m)
            s = self.seconds%60
            s = int(s) #Can this be placed above?
            if self.mil_time:
                if h > 23:
                    h = h%24
            else:
                if h is 0:
                    h = 12
                elif h > 12:
                    h = h%12
            return h, m, s
            
        #Directly set the time of the clock
        def set_time(self, h=0, m=0):
            """
            h = hours
            m = minutes
            """
            fh, fm = self.fix_time(h,m)
            self.seconds = ((fh*60)+fm)*60
            
        #Manually add time to the clock, with or without animation
        def add_time(self, h=0, m=0, animate=0): 
            """
            h = hours
            m = minutes
            animate = the number of seconds it takes for the time to be added
            """
            if self.realtime_run == False:
                num = ((h*60)+m)*60
                if animate:
                    self.step = num // float(animate*60)
                    self.seconds_target = self.seconds + num
                else:
                    self.seconds += num
                    
        #Manually add time to the clock, with or without animation
        def sub_time(self, h=0, m=0, animate=0): 
            """
            h = hours
            m = minutes
            animate = the number of seconds it takes for the time to be subtracted
            """
            if self.realtime_run == False:
                self.forward = False
                num = ((h*60)+m)*60
                if animate:
                    self.step = num // float(animate*60)
                    self.seconds_target = self.seconds - num
                else:
                    self.seconds -= num
                
        #Determines how much time has passed since a given time
        def time_passed(self, start_h=0, start_m=0, days_ago=0, comb_min=True):
            """
            h, m are the hours and minutes that make up the starting time you
            want to test against
            start_day is the day you'd like to start the time passed count from. That first day is 0
            comb_min, if true it returns just the total minutes, if False returns hours and mintues
            """
            oldnum = (start_h*60)+start_m
            nh, nm, ns = self.get_time()
            newnum = (nh*60)+nm
                
            minpassed = newnum-oldnum
            if days_ago > 0:
                minpassed += (days_ago*1440)
            tph, tpm = divmod(minpassed, 60)
            if comb_min:
                return minpassed
            else:
                return tph, tpm
        
        #Sets the runmode of the clock, the second hand, and the sound
        def runmode(self, mode, secOn=True, chOn=True):
            """
            mode= The mode of the clock: auto, real, or none (None turns off the clock) 
            snd= Turns on or off sound
            """
            if self.analogue:
                self.a_sound_on(secOn, chOn)
            if mode == "none":
                self.seconds_target = 0
                self.realtime_run = False
                self.auto_run = False
            else:
                if mode == "auto":
                    self.realtime_run = False
                    self.auto_run = True
                elif mode == "real":
                    self.auto_run = False
                    self.realtime_run = True
        
        #Sets the analogue sounds for the clock
        def a_sound_on(self, secOn, chOn):
            """
            secOn = Turns the second hand sound on or off
            chOn = Turns the chime sound on or off
            """
            if self.analogue:
                self.second_sound_on = secOn
                self.chime_on = chOn
                if self.second_sound_on:
                    if renpy.music.is_playing(channel='TockBG'):
                        renpy.music.stop(channel='TockBG', fadeout=0.1)
                    renpy.music.play("00 sounds/ClockTick1.flac", channel='TockBG')
                else:
                    renpy.music.stop(channel='TockBG')
                if not self.chime_on:
                    renpy.music.stop(channel='ChimeBG')
        
        #Sets the alarm for the digital clock
        def set_alarm (self, h=0, m=0, on=True):
            fh,fm= self.fix_time(h,m)
            self.alarm_hr = fh
            self.alarm_min = fm
            self.alarm_on = on
            
        #####These functions are used internally, no need to call them yourself
        #Returns a list of all the child displayables for this displayable.
        def visit(self):
            return [self.base_image, self.hour_hand_image, self.minute_hand_image, 
                self.second_hand_image, self.digital_base_image]

        #Runs the clock mechanism automatically
        def autoclock(self, st):
            if self.auto_run:
                self.realtime_run = False
                dt = int(st)
                if self.old_second != dt:
                    self.seconds += 1
                    self.old_second = dt

        #Runs the clock based on the real world time        
        def realclock(self):
            if self.realtime_run:
                self.auto_run = False 
                t = datetime.today()
                self.seconds = (3600 * t.hour) + (60 * t.minute) + t.second
                
        #Determines how many chimes should ring at any given hour and creates audio queue
        def chime_looper(self):
            h, m, s = self.get_time()
            if h is 0:
                h = 12
            elif h > 12:
                h = h%12
            ch = ["00 sounds/ChimePart.ogg",]*(h-1)
            ch.append("00 sounds/Chime1.ogg")
            return ch
        
        #Plays clock chimes on the hour
        def start_chime(self): 
            if self.chime_on:    
                if not self.play_chime:
                    if self.minutes%60 == 0:
                        self.play_chime = True
                        cf = self.chime_looper()
                        renpy.music.queue(cf, channel='ChimeBG')
        
        #Plays the alarm when the time has arrived
        def start_alarm(self): 
            if self.alarm_on:    
                if not self.play_alarm:
                    h, m, s = self.get_time()
                    if self.alarm_hr == h and self.alarm_min == m:
                        self.play_alarm = True
                        if self.analogue:
                            renpy.music.play("00 sounds/BellAlarm.wav", channel='Alarm')
                        else:
                            renpy.music.play("00 sounds/digital-alarm.wav", channel='Alarm')   
                            
        #Make sure the time is within the 0-24hr range
        def fix_time(self, h,m):
            if self.mil_time:
                if m > 59:
                    hadd, m = m%60
                    h += hadd
                if h > 23:
                    h = h%24
            else:
                if m > 59:
                    hadd, m = m%60
                    h += hadd
                if h is 0:
                    h = 12
                elif h > 12:
                    h = h%12
            return h,m
            
