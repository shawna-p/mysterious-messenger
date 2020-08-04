## This file contains deprecated functions, classes, screens, and labels
## that are no longer required for the current version of Mysterious Messenger
## but are maintained here for backwards compatibility

init python:

    # Renamed to next_story_time
    def next_chat_time():
        return next_story_time()

    # Renamed to make_24h_available
    def chat_24_available():
        return make_24h_available()

    # Renamed to check_and_unlock_story
    def next_chatroom():
        return check_and_unlock_story()