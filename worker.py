import fbchat
from getpass import getpass
from fbchat.models import Message, ThreadType


class SendMessageToFB():
    def __init__(self): 
        self.client = None
        self.username = None
    
    def send_message(self, msg, friend):
        return self.client.send(Message(text=msg), thread_id=friend.uid, thread_type=ThreadType.USER)

    def process_request(self):
        self.get_client_id()
        no_of_friends = int(input("Number of friends: "))
        for i in range(no_of_friends):
            name = input("Name: ")
            friends = self.client.searchForUsers(name)  # return a list of names
            friend = friends[0]
            msg = input("Message: ")
            sent = self.send_message(msg, friend)
            if sent:
                print("Message sent successfully!")
        self.client.logout()
    
    def get_client_id(self):
        '''
        Get fb connection for given user
        '''
        self.username = input("Username: ")
        self.client = fbchat.Client(self.username, getpass())
        print('facebook connection esstablished successfully')
    
if __name__=="__main__":
    client_obj = SendMessageToFB()
    client_obj.process_request()
