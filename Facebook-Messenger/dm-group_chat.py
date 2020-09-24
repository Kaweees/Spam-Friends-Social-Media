# this one is for sending direct messages to friends
import fbchat 
from fbchat import ThreadType
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
no_of_friends = get_interger("Number of group chats: ")
for i in range(no_of_friends): 
  group_id = get_interger("Group chat id: ")
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
        sent = client.sendMessage(msg,  thread_id=group_id, thread_type=ThreadType.GROUP)
      except:
        print("Message sent unsuccessfully... ")
      else:
        if sent: 
          print("Message sent successfully!")
print("task ended")
