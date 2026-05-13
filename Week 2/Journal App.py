from pathlib import Path
import json
import datetime

file_path = Path("Journal.json")


def create_entry():

    with open("Journal.json","r") as file:
        data = json.load(file)

    if len(data) == 0:
        entry_id = 1
    else:
        entry_id = data[-1]["id"] + 1
    title = input("Enter title for the journal")
    text = input("Context: ")
    date = datetime.date.today().strftime("%d%m%y")

    new_entry = {
        "id" : entry_id,
        "date" : date,
        "title" : title,
        "data" : text
    }

    data.append(new_entry)

    with open("Journal.json","w") as file:
        json.dump(data,file,indent=4)

def read_entry():
    user_ip = input("Enter the ID of the record you want to read(format(DDMMYY): ")
    with open("Journal.json","r") as file:
        data = json.load(file)

    found = False
    for entry in data:
        if user_ip == entry["date"]:
            print("record found")
            print(f"date: {entry["date"]}")
            print(f"id: {entry["id"]}")
            print(f"title: {entry["title"]}")
            print(f"Context: {entry["data"]}")
            found = True
            break

    if found == False:
        print("no entry found")

def search_entry():
    user_ip = input("enter date in the DDMMYY format: ")
    with open("Journal.json","r") as file:
        data = json.load(file)

    found = False
    for entry in data:
        if user_ip == entry["date"]:
            print("record found")
            break

    if found == False:
        print("no entry found")


print("=====Welcome to my Journal=====\n")
while True:
    print("1.Create a entry\n2.Read an Entry\n3.Search an entry by date(DDMMYY)\n4.Exit\n")
    print("Enter your choice: ")
    choice = int(input())

    match choice:
        case 1:
            create_entry()
        case 2:
            read_entry()
        case 3:
            search_entry()
        case 4:
            print("Thank you for visiting")
            break
        case _:
            print("Invalid choice!!")
