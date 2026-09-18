import requests
import ast
import json
import os

choice = input("Please enter a number based on what you want to do: \n1. List online players \n2. Get player profile \n3. List a player's characters \n4. Get a character's data \n5. Get a character's ability tree \n6. Exit \n")
API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise RuntimeError("API_KEY environment variable is not set. Please set it before running this script by using export API_KEY = 'your API key here'.")   

if choice == "1":
    choice1 = input("Would you like to see online players in a specific world? (y/n): ")
    if choice1 == "n":
        response = requests.get(
            "https://api.wynncraft.com/v3/player",
            headers={"Authorization": f"Bearer {API_KEY}"}
        )
        with open("data1.json", "w") as f:
            print(response.json(), file=f)
        with open("data1.json", "r") as f:
            data = ast.literal_eval(f.read())
        with open("data1.json", "w") as f:
            json.dump(data, f, indent=2)
        with open("data1.json", "r") as f:
            data = json.load(f)
        print (f"Total online players: {data["total"]}")
        for username, server in data["players"].items():
            print(f"Username: {username}, World: {server}")
    else:
        choiceServer = input("Please enter the world's name (eg. NA1, EU24): ")
        response = requests.get(
            f"https://api.wynncraft.com/v3/player?server={choiceServer}",
            headers={"Authorization": f"Bearer {API_KEY}"}
        )
        with open("data2.json", "w") as f:
            print(response.json(), file=f)
        with open("data2.json", "r") as f:
            data = ast.literal_eval(f.read())
        with open("data2.json", "w") as f:
            json.dump(data, f, indent=2)
        with open("data2.json", "r") as f:
            data = json.load(f)
        for username, server in data["players"].items():
            print (f"Username: {username}")


if choice == "2":
    choiceUser = input("Please enter an username: ")
    response = requests.get(
        f"https://api.wynncraft.com/v3/player/{choiceUser}",
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    with open("data3.json", "w") as f:
        print(response.json(), file=f)
    with open("data3.json", "r") as f:
        data = ast.literal_eval(f.read())
    with open("data3.json", "w") as f:
        json.dump(data, f, indent=2)
    with open("data3.json", "r") as f:
        data = json.load(f)
    print (f"Online: {data["online"]}")
    print (f"Last seen: {data["server"]}")
    response = requests.get(
        f"https://api.wynncraft.com/v3/player/{choiceUser}/characters",
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    with open("data.json", "w") as f:
        print(response.json(), file=f)
    with open("data.json", "r") as f:
        dataUser = ast.literal_eval(f.read())
    with open("data.json", "w") as f:
        json.dump(dataUser, f, indent=2)
    for uuid, player in dataUser.items():
        if (uuid == data["activeCharacter"]):
            print (f'Active class: {player["type"]}')
    print (f"UUID: {data["uuid"]}")
    print (f"Rank: {data["rank"]}")
    print (f"Support rank: {data["supportRank"]}")

if choice == "3":
    choiceUser = input("Please enter an username: ")
    response = requests.get(
        f"https://api.wynncraft.com/v3/player/{choiceUser}/characters",
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    print(response.json())

if choice == "4":
    choiceUser = input("Please enter an username: ")
    response = requests.get(
        f"https://api.wynncraft.com/v3/player/{choiceUser}/characters",
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    with open("data.json", "w") as f:
        print(response.json(), file=f)
    with open("data.json", "r") as f:
        data = ast.literal_eval(f.read())
    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)
    for uuid, player in data.items():
        print(f"Class: {player["type"]}, UUID: {uuid}")
    choiceClass = input("Enter the UUID of the class you want to see: ")
    response = requests.get(
        f"https://api.wynncraft.com/v3/player/{choiceUser}/characters/{choiceClass}",
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    print(response.json())

if choice == "5":
    choiceUser = input("Please enter an username: ")
    response = requests.get(
        f"https://api.wynncraft.com/v3/player/{choiceUser}/characters",
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    with open("data.json", "w") as f:
        print(response.json(), file=f)
    with open("data.json", "r") as f:
        data = ast.literal_eval(f.read())
    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)
    for uuid, player in data.items():
        print(f"Class: {player["type"]}, UUID: {uuid}")
    choiceClass = input("Enter the UUID of the class you want to see: ")
    response = requests.get(
        f"https://api.wynncraft.com/v3/player/{choiceUser}/characters/{choiceClass}/abilities",
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    print(response.json())

if choice == "6":
    print("")
