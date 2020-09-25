# Spam-Friend's-Social-Media
Python script that is supposed to read a selected number of lines of the Bee Movie's script from a ".txt" file and direct message those lines to friend or group chat on certain social medias.

## Installation Instructions
You can download or modify the program by Cloning or Downloading the project or by saving it as a ".zip" file.
Once the downloaded file is extracted into a separate folder, follow these instructions:

### Python Setup
1. Install Python 3.x or latest version.
2. Open cmd/termial/etc.
3. Use the command python `python -m pip install --upgrade pip` to upgrade pip (if pip isn't working, try [this](https://stackoverflow.com/questions/23708898/pip-is-not-recognized-as-an-internal-or-external-command)).
4. Use the command `pip install fbchat` for Facebook Messenger. Documentation for `fbchat` could be found [here](https://fbchat.readthedocs.io)
5. Support for other platforms coming soon

## Running

### Facebook Messenger
1. If direct messaging (dming) just friends, have the name the of friend on Facbook ready.
2. Run `dm-friend.py` located at `/Facebook-Messenger/dm-friend.py`
3. Login and input the name of the friend when prompted.
1. If direct messaging a group chat, find the group chat ID by logging into to fabebook messenger on a computer and copying part of the URL as shown below.
![GC ID Image](/assets/img/GC-ID.PNG)
2. Run `dm-friend.py` located at `/Facebook-Messenger/dm-group_chat.py`
3. Login and input the Group Chat when prompted.
