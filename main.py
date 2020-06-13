# this one is for sending direct messages to friends
import fbchat 
from getpass import getpass 

username = str(input("Username: ")) 
client = fbchat.Client(username, getpass()) 
no_of_friends = int(input("Number of friends: ")) 
for i in range(no_of_friends): 
    name = str(input("Name: ")) 
    friends = client.searchForUsers(name)  # return a   list of names 
    friend = friends[0] 
    #msg = str(input("Message: ")) 
    stop = 20 #stop is the amount of lines of the Bee Movie that are sent to your Facebook friend
    L = []
    filepath = 'beemovie.txt'
    with open(filepath) as fp:
      for i, line in enumerate(fp):
        L += [("Line {}: {}".format(i+1, line))]
      for i in range(0,stop):
        msg = L[i]
        sent = client.sendMessage(msg,  thread_id=friend.uid)
        #print(msg)
        if sent: 
          print("Message sent successfully!")
    #msg = str(input("Message: ")) 
    #sent = client.sendMessage(msg,  thread_id=friend.uid)
print("task ended")
#syntax
#client.send(Message(text='<message>'), thread_id='<user id>', thread_type=ThreadType.USER)
#client.send(Message(text='<message>'), thread_id='<group id>', thread_type=ThreadType.GROUP)
