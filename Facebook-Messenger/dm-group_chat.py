# this one is for sending direct messages to friends
import fbchat 
from getpass import getpass 

def get_user_info_and_login():
  try:
    username = input('Username: ')
    client = fbchat.Client(username, getpass()) 
    print('Login sucessful ')
  except:
    print('Login unsucessful, please try again. ')
    get_user_info_and_login()
  return client

def get_interger(string_params):
  try:
    x = int(input(string_params))
  except:
    print('Please enter an interger')
    get_interger(string_params)
  return x

def message_friend(client, friend):
  lines = get_interger("Number of Bee Movie lines you would like to send: ") # the amount of lines of the Bee Movie that are sent to your Facebook friend
  L = []
  filepath = 'beemovie.txt'
  with open(filepath) as fp:
    for i, line in enumerate(fp):
      L += [("Line {}: {}".format(i+1, line))]
    for i in range(0,lines):
      msg = L[i]
      try:
        sent = client.sendMessage(msg,  thread_id=friend.uid)
        print(sent)
      except:
        print("Message sent unsuccessfully... ")
      else:
        if sent: 
          print("Message sent successfully!")
client = get_user_info_and_login()
no_of_friends = get_interger("Number of friends: ")
for i in range(no_of_friends): 
  name = str(input("Name: ")) 
  friends = client.searchForUsers(name)  # return a list of names 
  friend = friends[0] 
  # msg = str(input("Message: ")) 
  lines = get_interger("Number of Bee Movie lines you would like to send: ") # the amount of lines of the Bee Movie that are sent to your Facebook friend
  L = []
  filepath = 'beemovie.txt'
  with open(filepath) as fp:
    for i, line in enumerate(fp):
      L += [("Line {}: {}".format(i+1, line))]
    for i in range(0,lines):
      msg = L[i]
      try:
        sent = client.sendMessage(msg,  thread_id=friend.uid)
      except:
        print("Message sent unsuccessfully... ")
      else:
        if sent: 
          print("Message sent successfully!")
    #message_friend(client, friend)
  #msg = str(input("Message: ")) 
  #sent = client.sendMessage(msg,  thread_id=friend.uid)
print("task ended")
#syntax
#client.send(Message(text='<message>'), thread_id='<user id>', thread_type=ThreadType.USER)
#client.send(Message(text='<message>'), thread_id='<group id>', thread_type=ThreadType.GROUP)
