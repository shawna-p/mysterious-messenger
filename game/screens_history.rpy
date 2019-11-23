##############################################
## This screen allows you to view replays
## of chatrooms and phone calls you've already
## seen in-game
###############################################

image history_button = Frame('Menu Screens/History/main02_button_01.png',
                                49, 52, 270, 53)
image history_button_hover = Fixed('history_button', 
                            Transform('history_button', alpha=0.5))
image history_icon_album = 'Menu Screens/History/history_icon_album.png'
image history_icon_chat = 'Menu Screens/History/history_icon_chat.png'
image history_icon_call = 'Menu Screens/History/history_icon_call.png'
image history_icon_guest = 'Menu Screens/History/history_icon_guest.png'

## This screen lets you view the album or the chat history
screen select_history():

    tag menu

    use menu_header("History", Show('main_menu', Dissolve(0.5))):

        style_prefix "select_history" 
        window: 
            hbox:      
                spacing 30    
                button:
                    action Show('photo_album', Dissolve(0.5))
                    hbox:
                        add 'history_icon_album' yalign 0.5
                        text 'ALBUM'
                button:
                    action Show('select_history_route', Dissolve(0.5))
                    hbox:
                        add 'history_icon_chat' yalign 0.5
                        text "CHAT HISTORY" 


style select_history_hbox:
    is default
    spacing 15
    align (0.5, 0.5)

style select_history_button:
    is default
    align (0.5, 0.2)
    background 'history_button'
    hover_background 'history_button_hover'
    padding (40,20,40,30)
    xysize (318,114)

style select_history_text:
    is default
    color "#fff" 
    size 28 
    xsize 50 
    font sans_serif_1b
    align (0.5, 0.5)

style select_history_window:
    is default
    xysize (740, 1100)
    align (0.5, 0.5)


screen select_history_route():

    tag menu

    use menu_header("History", Show('main_menu', Dissolve(0.5))):

        style_prefix 'history_route'
        for route in all_routes:
            textbutton _(route[0] + " Route"):
                action NullAction()#Show('chat_select')

style history_route_button:
    is other_settings_end_button
    padding (30,30)

style history_route_button_text:
    is mode_select

