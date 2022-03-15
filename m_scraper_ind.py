from auth_info import *
from csv_saver import *
import re
# Indivual chat messages scraper. Set user info: phone number or nick with @
user = input("Enter user name/phone to parse message ")

if bool(re.search('[a-zA-Z]', user)) and user[0] != "@":
    user = "@"+user

# set limit of messages amount
while True:
    try:
        limit_msg = int(input("Enter messages count to parse "))
        break
    except:
        print("Enter integer...")
        continue

all_msg = []

for m in client.get_messages(user, limit=limit_msg):
    msg_lst = []
    from_ = "me"
    if m.from_id == None:
        from_ = user

    msg_lst.append(from_)
    msg_lst.append(m.message.replace('\t', ' ').replace("\n", "{ENTER}"))
    msg_lst.append(m.date)
    all_msg.append(msg_lst)

# reverse order of the list    
all_msg = all_msg[::-1]

# save the result
csv_save_ind(all_msg)

