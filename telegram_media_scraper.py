from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerUser
from telethon.tl.types import InputPeerEmpty
from auth_info import *

chats = []
last_date = None

# set the limit of members amount
chunk_size = 100000

# set limit of messages amount
while True:
    try:
        #limit_msg = int(input("Enter messages count to parse "))
        limit_msg = 1000
        break
    except:
        print("Enter integer...")
        continue

groups = [] 
result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)

for chat in chats:
    try:
        # if chat.megagroup == True:
        #     groups.append(chat)
        groups.append(chat)
    except:
        continue

# sort groups by alphabetic order
groups.sort(key=lambda x: x.title, reverse=False)

print('Choose a group to scrape messages from:')

i = 0
for g in groups:
    print(str(i) + '- ' + g.title)
    i+=1

g_index = input("Enter a Number: ")
target_group=groups[int(g_index)]

print('Fetching Messages...')

channel_entity=client.get_entity(target_group.title)
#client.get_participants(target_group.title) 
posts = client(GetHistoryRequest(
    peer=channel_entity,
    limit=limit_msg,
    offset_date=None,
    offset_id=0,
    max_id=0,
    min_id=0,
    add_offset=0,
    hash=0))

post_msg = posts.messages

# save the results
for m in post_msg:
    client.download_media(m.media)
