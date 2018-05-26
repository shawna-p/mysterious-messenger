init offset = 5
init python:

    def open_file(thefile):
        global myfile, file_path
        myfile = open(file_path + thefile, 'a') # opens file for appending
        
    def close_file():
        global myfile
        myfile.close()
        
    def write_file(the_string):
        global myfile
        myfile.write(the_string)
        
    def file_endl():
        global myfile
        myfile.write('\n')
        
    class InputDialogue(InputValue):
        def __init__(self, var, default="Insert Text Here"):
            self.var = var
            
            if not hasattr(store, var):
                setattr(store, var, default)
                                    
        def get_text(self):
            return getattr(store, self.var)
            
        def set_text(self, s):                
            setattr(store, self.var, s)  
            global the_entry
            the_entry.what = s

        def enter(self):
            renpy.run(self.Disable())                
            raise renpy.IgnoreEvent()
                
    class Fonts(object):
        def __init__(self):
            self.reset()
            
        def reset(self):
            self.curly = False
            self.blocky = False
            self.big = False
            
            self.ser1 = False
            self.ser1b = False
            self.ser1xb = False
            
            self.ser2 = False
            self.ser2b = False
            self.ser2xb = False
            
            self.sser1 = False
            self.sser1b = False
            self.sser1xb = False
            
            self.sser2 = False
            self.sser2b = False
            self.sser2xb = False
            
        def clear_font(self):
            self.curly = False
            self.blocky = False            
            self.ser1 = False
            self.ser1b = False
            self.ser1xb = False            
            self.ser2 = False
            self.ser2b = False
            self.ser2xb = False            
            self.sser1 = False
            self.sser1b = False
            self.sser1xb = False            
            self.sser2 = False
            self.sser2b = False
            self.sser2xb = False
            
        def update(self):
            global f_style_begin, f_style_end            
            if self.curly:
                f_style_begin += '{=curly}'
                f_style_end = '{/=curly}' + f_style_end
            if self.blocky:
                f_style_begin += '{=blocky}'
                f_style_end = '{/=blocky}' + f_style_end            
            if self.ser1:
                f_style_begin += '{=ser1}'
                f_style_end = '{/=ser1}' + f_style_end
            if self.ser1b:
                f_style_begin += '{=ser1b}'
                f_style_end = '{/=ser1b}' + f_style_end
            if self.ser1xb:
                f_style_begin += '{=ser1xb}'
                f_style_end = '{/=ser1xb}' + f_style_end
            if self.ser2:
                f_style_begin += '{=ser2}'
                f_style_end = '{/=ser2}' + f_style_end
            if self.ser2b:
                f_style_begin += '{=ser2b}'
                f_style_end = '{/=ser2b}' + f_style_end
            if self.ser2xb:
                f_style_begin += '{=ser2xb}'
                f_style_end = '{/=ser2xb}' + f_style_end
            if self.sser1:
                f_style_begin += '{=sser1}'
                f_style_end = '{/=sser1}' + f_style_end
            if self.sser1b:
                f_style_begin += '{=sser1b}'
                f_style_end = '{/=sser1b}' + f_style_end
            if self.sser1xb:
                f_style_begin += '{=sser1xb}'
                f_style_end = '{/=sser1xb}' + f_style_end
            if self.sser2:
                f_style_begin += '{=sser2}'
                f_style_end = '{/=sser2}' + f_style_end
            if self.sser2b:
                f_style_begin += '{=sser2b}'
                f_style_end = '{/=sser2b}' + f_style_end
            if self.sser2xb:
                f_style_begin += '{=sser2xb}'
                f_style_end = '{/=sser2xb}' + f_style_end
            if self.big:
                f_style_begin += '{size=+10}'
                f_style_end = '{/size}' + f_style_end
                
    def clear_fonts(font_obj):
        font_obj.clear_font()
    
    def update_font(font_obj):
        font_obj.update()
        
    def reset_fonts(font_obj):
        global f_style_begin, f_style_end
        f_style_begin = ''
        f_style_end = ''
        font_obj.reset()
        
    def reduce_size(font_obj):
        global f_style_begin, f_style_end
        f_style_begin = ''
        f_style_end = ''
        font_obj.update()
            
        
## BY DEFAULT this file gets saved wherever your Ren'Py directory is,
## e.g. C:\Users\Your-Username\Documents\renpy-6.99.14.1-sdk
## If you want to save it somewhere else, you'll need to modify the variable below
## **Don't forget a \\ at the end**
default file_path = "C:\Users\Shawna\Documents\Personal\Messenger Test Extra Resources\\"
default thefile = 'my-script.txt'

default myfile = False

default f_dialogue = 'Input dialogue here'
default f_char = False

default font_styles = [ ['curly', 'blocky', 'big'], ['ser1', 'ser1b', 'ser1xb'],
                        ['ser2', 'ser2b', 'ser2xb'], ['sser1', 'sser1b', 'sser1xb'],
                        ['sser2', 'sser2b', 'sser2xb'] ]
                        
default f_style_begin = ''
default f_style_end = ''
default f_font_style = Fonts()

default the_entry = Chatentry(ju, 'Some sample text', upTime())#Chatentry(ju, 'Input dialogue here', pv)
    
default bubble_background = "Bubble/" + the_entry.who.file_id + "-Glow.png"

screen create_archive:

    tag menu
    
    use starry_night
    use menu_header('Create a Chatroom', MainMenu())
        
    window:
        xalign 0.5
        yalign 0.13
        maximum(700,70)
        has hbox
        xalign 0.5
        spacing 40
        # Create Chatroom/Set up Route tabs
        textbutton _('Create Chatroom'):
            text_style "settings_tabs" 
            xsize 290
            ysize 65
            background "menu_tab_active"            
                
        textbutton _('Set up Route'):
            text_style "settings_tabs" 
            xsize 290
            ysize 65
            background "menu_tab_inactive"
            hover_background "menu_tab_inactive_hover"
            action NullAction
 

    viewport:
        xsize 725
        ysize 1070
        draggable True
        mousewheel True

        xalign 0.5
        yalign 0.95
        
        
        vbox:
            align (0.1, 0.0)
            text "Select a Character" style 'creator_title'
            side ('t b'):
                spacing 20
                xysize(700, 90)
                viewport id 'character_select':
                    draggable True
                    mousewheel "horizontal"
                    xysize(700, 85)
                    align (0.5, 0.5)
                    hbox:
                        spacing 10
                        for i in character_list:
                            if i.participant_pic:
                                imagebutton:
                                    hover_foreground 'char_foreground2'
                                    selected_foreground 'char_foreground'
                                    idle i.participant_pic
                                    selected (the_entry.who == i)
                                    action [SetField(the_entry, 'who', i),
                                            SetField(the_entry, 'specBubble', None)]
                            elif i == m:
                                imagebutton:
                                    hover_foreground 'char_foreground2'
                                    selected_foreground 'char_foreground'
                                    selected (the_entry.who == i)
                                    idle Transform('Profile Pics/MC/MC-1.png', zoom=0.725)
                                    action [SetField(the_entry, 'who', i),
                                            SetField(the_entry, 'bounce', False),
                                            SetField(the_entry, 'specBubble', None)]
                
                bar value XScrollValue('character_select') style 'creator_hscroll'
        
            null height 30
        
            ## Dialogue Input
            window:   
                xysize (730, 370)
                align (0.5, 0.5)
                hbox:
                    spacing 20
                    xalign 0.5
                    yalign 0.5
                    button:
                        xysize (500, 300)
                        xalign 0.1
                        yalign 0.5
                        background 'input_square' padding(40, 40)
                        viewport:
                            mousewheel True
                            xysize (650,230)
                            xalign 0.1
                            yalign 0.5
                            text f_style_begin + the_entry.what + f_style_end
                        action Show('dialogue_input_popup', width=680, height=500)
                    
                    vbox:
                        align (0.5, 0.5)
                        spacing 20
                        textbutton _('Emojis'):
                            text_style 'mode_select'
                            xysize (170,80)
                            background 'menu_select_btn' padding(20,20)
                            hover_background 'menu_select_btn_hover'
                            action Show("pick_emoji", character=the_entry.who)
                            
                        textbutton _('Exit/Enter'):
                            text_style 'mode_select'
                            xysize (170,110)
                            background 'menu_select_btn' padding(20,20)
                            hover_background 'menu_select_btn_hover'
                            action Show("pick_emoji", character=the_entry.who)
                            
                        textbutton _('Speech Bubbles'):
                            text_style 'mode_select'
                            xysize (170,110)
                            background 'menu_select_btn' padding(20,20)
                            hover_background 'menu_select_btn_hover'
                            action Show("pick_bubble", character=the_entry.who)
                
        
            text "Font Options" style 'creator_title'

            window:
                xysize(700, 220)
                align (0.5, 0.5)
                hbox:
                    spacing 10
                    align (0.5, 0.5)
                    for f in font_styles:                            
                        vbox:
                            spacing 10
                            for f_var in f:
                                if f_var != 'big':
                                    textbutton _('Text'):
                                        text_style f_var
                                        text_text_align 0.5 text_xalign 0.5 text_yalign 0.5
                                        text_color '#fff'
                                        style 'creator_font_button'
                                        action [Function(clear_fonts, font_obj=f_font_style),
                                                SetField(f_font_style, f_var, True),
                                                Function(update_font, font_obj=f_font_style),
                                                renpy.retain_after_load]
                                else:
                                    textbutton _('Big'):
                                        text_size gui.text_size + 10
                                        text_text_align 0.5 text_xalign 0.5 text_yalign 0.5
                                        text_color '#fff'
                                        xysize (90, 60)
                                        if not f_font_style.big:
                                            background "menu_tab_inactive"
                                            hover_background "menu_tab_inactive_hover"
                                            action [SetField(f_font_style, f_var, True),
                                                    Function(update_font, font_obj=f_font_style),
                                                    renpy.retain_after_load]
                                        else:
                                            background "menu_tab_inactive_hover2"
                                            action [SetField(f_font_style, f_var, False),
                                                    Function(reduce_size, font_obj=f_font_style),
                                                    renpy.retain_after_load]

                    window:
                        xysize(220, 200)
                        align (0.5, 0.5)
                        text '<- Regular' color '#fff' yalign 0.1
                        text '<- {=sser1b}{color=#fff}Bold{/color}{/=sser1b}' color '#fff' yalign 0.5
                        text '<- {=sser1xb}{color=#fff}Extra Bold{/color}{/=sser1xb}' color '#fff' yalign 0.9
        
            textbutton _('Reset Font to Default'):                    
                text_text_align 0.5 text_xalign 0.5 text_yalign 0.5
                align (0.5, 0.5)
                text_color '#fff'
                style 'creator_button'
                action [Function(reset_fonts, font_obj=f_font_style), renpy.retain_after_load]
        
            text "Preview" style 'creator_title'
        
            $ bubbleBackground = "Bubble/" + the_entry.who.file_id + "-Bubble.png"
        
            window:
                xysize (700, 450)
                background Transform("bg-earlyMorn.jpg", crop=(50,300,700,450))
                viewport:
                    draggable True
                    xysize (700, 450)
                    use chat_animation(the_entry, False)
        
        
        
        
        
            null height 300
            hbox:
                align (0.5, 0.5)
                style 'creator_hbox'
                textbutton _('Test writing to file'):
                    text_style 'creator_button_text'
                    style 'creator_button'
                    action [Function(write_file, the_string='Hello World'), Show('notify', message="Success 2")]
                
                textbutton _('End Line'):
                    text_style 'creator_button_text'
                    style 'creator_button'
                    action [Function(file_endl), Show('notify', message="Success 2")]
                    
                textbutton _('Save Changes'):
                    text_style 'creator_button_text'
                    style 'creator_button'
                    action [Function(close_file), Function(open_file, thefile=thefile), Show('notify', message="Success3")]  

            
        
            
    #on 'show' action [Function(open_file, thefile=thefile), Show('notify', message="File Opened")]
    #on 'replace' action [Function(open_file, thefile=thefile), Show('notify', message="File Opened")]
    #on 'hide' action [Function(close_file), Show('notify', message="File Closed")]
    #on 'replaced' action [Function(close_file), Show('notify', message="File Closed")]
    
    #timer 60.0 action [Function(close_file), Function(open_file, thefile=thefile), Show('notify', message="Autosaved")] repeat True
    
    
screen dialogue_input_popup(width=550, height=313):

    zorder 100
    modal True
    
    $ old_dialogue = the_entry.what
    $ d_input = Input(value=InputDialogue("the_entry.what", the_entry.what), style="dialogue_text")
    $ yadj.value = yadjValue  
    
    window:
        maximum(width, height)
        background 'input_popup_bkgr'
        xalign 0.5
        yalign 0.4
        imagebutton:
            align (1.0, 0.0)
            idle 'input_close'
            hover 'input_close_hover'
            action [Hide('dialogue_input_popup'), SetField(the_entry, 'what', old_dialogue), renpy.retain_after_load, Show('create_archive')]
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.6            
            window:
                xysize (width - 50,height - 220)
                xalign 0.5
                background 'input_square' padding(40,40)
                viewport yadjustment yadj:
                    mousewheel True
                    xysize (width - 90,height - 240)
                    xalign 0.5
                    yalign 0.5
                    add d_input xalign 0.5 yalign 0.5
            textbutton _('Confirm'):
                text_style 'mode_select'
                xalign 0.5
                xsize 240
                ysize 80
                background 'menu_select_btn' padding(20,20)
                hover_background 'menu_select_btn_hover'
                action [Hide('dialogue_input_popup'), SetField(the_entry, 'img', False), Show('create_archive')]
                
screen pick_emoji(character):

    zorder 100
    modal True
    
    window:
        maximum(680, 1000)
        background 'input_popup_bkgr'
        xalign 0.5
        yalign 0.6
        imagebutton:
            align (1.0, 0.0)
            idle 'input_close'
            hover 'input_close_hover'
            action [Hide('pick_emoji'), renpy.retain_after_load, Show('create_archive')]
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.6            
            window:
                xysize (630,780)
                xalign 0.5
                background 'input_square' padding(40,40)
                vpgrid:
                    mousewheel True
                    xysize (590,760)
                    align (0.5, 0.5)
                    cols 2
                    for emote in character.emote_list:
                        button:
                            xysize(290,290)
                            hover_background '#e0e0e0'
                            selected_background '#a8a8a8'
                            selected (the_entry.what == emote)
                            text emote align (0.5, 0.5)
                            action [SetField(the_entry, 'what', emote), 
                                    SetField(the_entry, 'img', True)]
                            
                    
            textbutton _('Confirm'):
                text_style 'mode_select'
                xalign 0.5
                xsize 240
                ysize 80
                background 'menu_select_btn' padding(20,20)
                hover_background 'menu_select_btn_hover'
                action [Hide('pick_emoji'), Show('create_archive')]
                
                
                
screen pick_bubble(character):

    zorder 100
    modal True
    
    window:
        maximum(780, 1000)
        background 'input_popup_bkgr'
        xalign 0.5
        yalign 0.6
        imagebutton:
            align (1.0, 0.0)
            idle 'input_close'
            hover 'input_close_hover'
            action [Hide('pick_bubble'), renpy.retain_after_load, Show('create_archive')]
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.6            
            window:
                xysize (730,780)
                xalign 0.5
                background 'input_square' padding(40,40)
                vpgrid:
                    mousewheel True
                    xysize (690,760)
                    align (0.5, 0.5)
                    cols 2
                    for bubble in bubble_list[:2]:
                        if renpy.loadable(bubble[0] + character.file_id + bubble[1]):
                            $ thebubble = bubble[0] + character.file_id + bubble[1]
                            $ bubblename = bubble[1][1:-4]
                            if bubblename == 'Glow':
                                $ bounces = True
                            else:
                                $ bounces = False
                            button:
                                xysize(350,225)
                                hover_background '#e0e0e0'
                                selected_background '#a8a8a8'
                                selected ((the_entry.bounce == bounces) and (the_entry.specBubble == None))
                                align (0.5, 0.5)
                                window:
                                    xysize (300, 180)
                                    align (0.5, 0.5)
                                    background Frame(thebubble, 25, 25)
                                action [SetField(the_entry, 'specBubble', None), 
                                            SetField(the_entry, 'img', False),
                                            SetField(the_entry, 'bounce', bounces)]
               
                    for bubble in bubble_list[2:]:
                        if renpy.loadable(bubble[0] + character.file_id + bubble[1]):
                            $ thebubble = bubble[0] + character.file_id + bubble[1]
                            $ bubblename = bubble[1][1:-4]
                            button:
                                xysize(350,225)
                                hover_background '#e0e0e0'
                                selected_background '#a8a8a8'
                                selected (the_entry.specBubble == bubblename)
                                align (0.5, 0.5)
                                add Transform(thebubble, zoom=0.5) align (0.5, 0.5)
                                    
                                    
                                action [SetField(the_entry, 'specBubble', bubblename), 
                                        SetField(the_entry, 'img', False),
                                        SetField(the_entry, 'bounce', True)]
                            
                    
            textbutton _('Confirm'):
                text_style 'mode_select'
                xalign 0.5
                xsize 240
                ysize 80
                background 'menu_select_btn' padding(20,20)
                hover_background 'menu_select_btn_hover'
                action [Hide('pick_bubble'), Show('create_archive')]
    
    
style creator_vbox is vbox
style creator_button is button
style creator_button_text is button_text

style creator_hscroll:
    base_bar Frame('gui/scrollbar/horizontal_hover_bar.png',0,0)
    ysize 11
    thumb 'gui/scrollbar/horizontal_hover_thumb.png'
    yoffset 15

style dialogue_text:
    color '#000'
    text_align 0.0
    
style creator_vbox:
    align (0.5, 0.5)
    spacing 30
    
style creator_hbox:
    align (0.5, 0.5)
    spacing 10
    
style creator_title:
    color '#fff'
    size 35
    outlines [ (1, '#277177', 3, 2) ]
    font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-ExtraBold.ttf"

style creator_button is default:    
    xsize 231
    ysize 70
    background "menu_tab_inactive"
    hover_background "menu_tab_inactive_hover"

style creator_font_button:    
    xysize (90, 60)
    background "menu_tab_inactive"
    hover_background "menu_tab_inactive_hover"
    selected_idle_background "menu_tab_inactive_hover2"
    
style creator_button_text is default:
    color '#fff'
    size 28
    font "00 fonts/NanumGothic (Sans Serif Font 1)/NanumGothic-Regular.ttf"
    text_align 0.5
    xalign 0.5
    yalign 0.5
    
    
    
    
    
    
    
    
    
    
    
    