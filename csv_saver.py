import csv

def csv_save_ind(list_info):
    with open("messages_ind_db.csv", "a", encoding='UTF-8') as f:
        writer = csv.writer(f, delimiter="\t", lineterminator="\n")

        if open("messages_ind_db.csv", "r").read() == "":
            writer.writerow(["sender", "message", "date"])
        
        for m in list_info:
            writer.writerow(m) 

def csv_save_group(list_info):
    with open("messages_group_db.csv", "a", encoding='UTF-8') as f:
        writer = csv.writer(f, delimiter="\t", lineterminator="\n")

        if open("messages_group_db.csv", "r").read() == "":
            writer.writerow(["chat_name", "sender", "message", "date"])
        
        for m in list_info:
            writer.writerow(m) 