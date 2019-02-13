##******************************
## USEFUL PYTHON FUNCTIONS
##******************************
init -6 python:
    
    # This class stores past chatrooms that you've visited
    # A more complete explanation of how to use it to set up chatrooms can be found
    # in the accompanying Script Generator spreadsheet
    class Chat_History(store.object):
        def __init__(self, title, save_img, chatroom_label, trigger_time, participants=[],
                        vn_obj=False, plot_branch=False):
            self.title = title
            self.save_img = save_img
            self.chatroom_label = chatroom_label
            self.trigger_time = trigger_time
            self.participants = participants
            self.vn_obj = vn_obj
            self.played = False
            self.participated = True
            self.available = False
            self.expired = False
            self.plot_branch = plot_branch
            
        def add_participant(self, chara):
            if not chara in self.participants:
                self.participants.append(chara)
            
            
    # This class stores the information needed for the Visual Novel portions of the game
    class VN_Mode(store.object):
        def __init__(self, vn_label, who=None, party=False):
            self.vn_label = vn_label
            self.who = who
            self.played = False
            self.available = False
            self.party = party
              
            
    # This object stores all the chatrooms you've viewed in the game. 
    class Archive(store.object):
        def __init__(self, day, archive_list=[], route='day_common2'):
            self.day = day
            self.archive_list = archive_list
            self.route = route
            
    # This function ensures the next chatroom or VN section becomes available
    # Currently they are available in sequence but the program could be modified
    # to make chatrooms available at the correct real-life times
    def next_chatroom():
        global chat_archive, available_calls, current_chatroom, test_ran
        triggered_next = False
        for archive in chat_archive:
            if archive.archive_list:
                for chatroom in archive.archive_list:
                    # Edge case; if they haven't played the currently
                    # available chatroom, don't make anything new
                    # available and stop
                    if chatroom.available and not chatroom.played:
                        triggered_next = True
                        break
                    # If the chatroom has an unavailable VN after it, make that available and stop
                    if chatroom.played and chatroom.vn_obj and not chatroom.vn_obj.available:
                        chatroom.vn_obj.available = True
                        triggered_next = True
                        break
                    # If they haven't played the VN yet, don't make anything new available and stop
                    if chatroom.played and chatroom.vn_obj and chatroom.vn_obj.available and not chatroom.vn_obj.played:
                        triggered_next = True
                        break              
                    # If the current chatroom isn't available, make it available and stop
                    # Also decrease the time old phone calls are available
                    if not chatroom.available:
                        chatroom.available = True
                        current_chatroom = chatroom
                        for phonecall in available_calls:
                            phonecall.decrease_time()
                        triggered_next = True
                        break               
            if triggered_next:
                break
                
    # A quick function to see how many chatrooms there are left to be played through
    # This is used so emails will always be delivered before the party
    def num_future_chatrooms():
        global chat_archive
        total = 0
        for archive in chat_archive:
            if archive.archive_list:
                for chatroom in archive.archive_list:
                    if not chatroom.played: 
                        total += 1
        return total
                
        
    # Delivers the next available text message and triggers an incoming
    # phone call, if applicable
    def deliver_next():
        global text_queue, incoming_call, available_calls, current_call
        for msg in text_queue:
            if msg.msg_list:
                msg.deliver()
                break             
        if incoming_call:
            current_call = incoming_call
            incoming_call = False
            renpy.call('new_incoming_call', phonecall=current_call)
    
    # This function takes a route (new_route) and merges it with the
    # current route
    def merge_routes(new_route, is_vn=False):
        global chat_archive
        current_chatroom.plot_branch = False
        for archive in chat_archive:
            for archive2 in new_route:
                if archive2.day == archive.day:
                    # If there is a conditional VN object
                    if is_vn:
                        # replace the old VN obj with the new one
                        archive.archive_list[-1].vn_obj = archive2.archive_list[0].vn_obj
                        del archive2.archive_list[0]
                        is_vn = False
                    
                    archive.archive_list += archive2.archive_list
                    archive.route = archive2.route
                    
        
            
# This archive will store every chatroom in the game. If done correctly,
# the program will automatically set variables and make chatrooms available
# for you
default chat_archive = [Archive('Tutorial', [Chat_History('Example Chatroom', 'auto', 'example_chat', '00:01'),                                     
                                    Chat_History('Inviting Guests', 'auto', 'example_email', '02:11', [z]),
                                    Chat_History('Text Message Example', 'auto', 'example_text', '02:53', [r], VN_Mode('vn_mode_tutorial', r)),
                                    Chat_History('Pass Out After Drinking Coffee Syndrome', 'auto', 'tutorial_chat', '04:05', [s]),
                                    Chat_History('Invite to the meeting', 'jumin', 'popcorn_chat', '07:07', [ja, ju], VN_Mode('popcorn_vn', ju)),
                                    Chat_History('Plot Branches', 'auto', 'plot_branch_tutorial', '10:44', [], False, True)]),
                        Archive('1st'),
                        Archive('2nd'),
                        Archive('3rd'),
                        Archive('4th'),
                        Archive('5th'),
                        Archive('6th'),
                        Archive('7th'),
                        Archive('8th'),
                        Archive('9th'),
                        Archive('10th'),
                        Archive('Final')]
                        
default tutorial_bad_end = [Archive('Tutorial', [Chat_History('An Unfinished Task', 'auto', 'tutorial_bad_end', '13:26', [v])] )]
default tutorial_good_end = [Archive('Tutorial', [ Chat_History('Plot Branches', 'auto', 'plot_branch_tutorial', '10:44', [], VN_Mode('plot_branch_vn')),
                                                   Chat_History('Onwards!', 'auto', 'tutorial_good_end', '13:26', [u], VN_Mode('good_end_party', None, True))] )]
                        
default seven_route = [ Archive('5th', [], 'day_s'),
                        Archive('6th', [], 'day_s'),
                        Archive('7th', [], 'day_s'),
                        Archive('8th', [], 'day_s'),
                        Archive('9th', [], 'day_s'),
                        Archive('10th', [], 'day_s'),
                        Archive('Final', [], 'day_s')]