# this one is for sending direct messages to friends
#reqirements python 3.8+
#facebook username, password, and friends lmao
#pip install fbchat
#run on personal computer, as it dosen't seem to work directly on Repl.it
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
    stop = 20
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
print("")
#syntax
#client.send(Message(text='<message>'), thread_id='<user id>', thread_type=ThreadType.USER)
#client.send(Message(text='<message>'), thread_id='<group id>', thread_type=ThreadType.GROUP)