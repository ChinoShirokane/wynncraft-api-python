import requests
import ast
import json
import os

API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise RuntimeError("API_KEY environment variable is not set. Please set it before running this script by using export API_KEY = 'your API key here'.")   

choice = input("Please enter a number based on what you want to do: \n1. List online players \n2. Get player profile \n3. List a player's characters \n4. Get a character's data \n5. Get a character's ability tree \n6. Exit \n")
if choice == "1":
    choice1 = input("Would you like to see online players in a specific world? (y/n): ")
    if choice1 == "n":
        response = requests.get(
            "https://api.wynncraft.com/v3/player",
            headers={"Authorization": f"Bearer {API_KEY}"}
        )
        with open("dataOnlinePlayers.json", "w") as f:
            print(response.json(), file=f)
        with open("dataOnlinePlayers.json", "r") as f:
            data = ast.literal_eval(f.read())
        with open("dataOnlinePlayers.json", "w") as f:
            json.dump(data, f, indent=2)
        with open("dataOnlinePlayers.json", "r") as f:
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
        with open("dataOnlinePlayersWorld.json", "w") as f:
            print(response.json(), file=f)
        with open("dataOnlinePlayersWorld.json", "r") as f:
            data = ast.literal_eval(f.read())
        with open("dataOnlinePlayersWorld.json", "w") as f:
            json.dump(data, f, indent=2)
        with open("dataOnlinePlayersWorld.json", "r") as f:
            data = json.load(f)
        for username, server in data["players"].items():
            print (f"Username: {username}")


if choice == "2":
    choiceUser = input("Please enter an username: ")
    response = requests.get(
        f"https://api.wynncraft.com/v3/player/{choiceUser}",
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    with open("dataPlayerProfile.json", "w") as f:
        print(response.json(), file=f)
    with open("dataPlayerProfile.json", "r") as f:
        data = ast.literal_eval(f.read())
    with open("dataPlayerProfile.json", "w") as f:
        json.dump(data, f, indent=2)
    with open("dataPlayerProfile.json", "r") as f:
        data = json.load(f)
    print (f"Online: {data["online"]}")
    print (f"Last seen: {data["server"]}")
    response = requests.get(
        f"https://api.wynncraft.com/v3/player/{choiceUser}/characters",
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    with open("dataPlayerCharacter.json", "w") as f:
        print(response.json(), file=f)
    with open("dataPlayerCharacter.json", "r") as f:
        dataUser = ast.literal_eval(f.read())
    with open("dataPlayerCharacter.json", "w") as f:
        json.dump(dataUser, f, indent=2)
    for uuid, player in dataUser.items():
        if (uuid == data["activeCharacter"]):
            print (f'Active class: {player["type"]}')

    print (f"UUID: {data["uuid"]}")
    print (f"Rank: {data["rank"]}")
    print (f"Support rank: {data["supportRank"]}")
    print (f"Last joined: {data["lastJoin"]}")
    print (f"Veteran: {data["veteran"]}")
    print (f"Playtime (hours): {data["playtime"]}")

    globData = data["globalData"]
    print (f'Content completion: {globData["contentCompletion"]}')
    print (f'Wars: {globData["wars"]}')
    print (f'Total level: {globData["totalLevel"]}')
    print (f'Mobs killed: {globData["mobsKilled"]}')
    print (f'Chests found: {globData["chestsFound"]}')

    dungeon = globData["dungeons"]
    print (f'Dungeons: {dungeon["total"]}')

    print (f'World events completed: {globData["worldEvents"]}') #this and the lootrun counter is just wrong somehow (either that or im tripping), blame wynncraft 
    print (f'Lootruns completed: {globData["lootruns"]}')

    guilds = data["guild"]
    print (f'Guild name: {guilds["name"]}')
    print (f'Guild prefix: {guilds["prefix"]}')
    print (f'Guild rank: {guilds["rank"]}')

    print ("\n")
    raid = globData["raids"]
    print (f'Raids completed: {raid["total"]}')
    raidInfo = raid["list"]
    print (f'TCC: {raidInfo["The Canyon Colossus"]}')
    print (f'NOL: {raidInfo["Orphion's Nexus of Light"]}')
    print (f'TNA: {raidInfo["The Nameless Anomaly"]}')
    print (f'NOTG: {raidInfo["Nest of the Grootslangs"]}')
    print (f'WTP: {raidInfo["Nest of the Grootslangs"]}')

    graid = globData["guildRaids"]
    print (f'Guild raids completed: {graid["total"]}')
    graidInfo = graid["list"]
    print (f'GTCC: {graidInfo["The Canyon Colossus"]}')
    print (f'GNOL: {graidInfo["Orphion's Nexus of Light"]}')
    print (f'GTNA: {graidInfo["The Nameless Anomaly"]}')
    print (f'GNOTG: {graidInfo["Nest of the Grootslangs"]}')
    print (f'GWTP: {graidInfo["Nest of the Grootslangs"]}')

    print ("\n")
    ranks = data.get("ranking", {})
    print (f'NOL graid ranking: {ranks.get("orphionSrGPlayers", 0)}')
    print (f'NOL raid ranking: {ranks.get("orphionSrPlayers", 0)}')
    print (f'NOL completion ranking: {ranks.get("orphionCompletion", 0)}')
    print (f'NOTG graid ranking: {ranks.get("grootslangSrGPlayers", 0)}')
    print (f'NOTG raid ranking: {ranks.get("grootslangSrPlayers", 0)}')
    print (f'NOTG completion ranking: {ranks.get("grootslangCompletion", 0)}')
    print (f'TNA graid ranking: {ranks.get("namelessSrGPlayers", 0)}')
    print (f'TNA raid ranking: {ranks.get("namelessSrPlayers", 0)}')
    print (f'TNA completion ranking: {ranks.get("namelessCompletion", 0)}')
    print (f'TCC graid ranking: {ranks.get("colossusSrGPlayers", 0)}')
    print (f'TCC raid ranking: {ranks.get("colossusSrPlayers", 0)}')
    print (f'TCC completion ranking: {ranks.get("colossusCompletion", 0)}')
    print (f'WTP graid ranking: {ranks.get("frumaSrGPlayers", 0)}')
    print (f'WTP raid ranking: {ranks.get("frumaSrPlayers", 0)}')
    print (f'WTP completion ranking: {ranks.get("frumaCompletion", 0)}')

if choice == "3":
    choiceUser = input("Please enter an username: ")
    response = requests.get(
        f"https://api.wynncraft.com/v3/player/{choiceUser}/characters",
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    with open("dataCharacterList.json", "w") as f:
        print(response.json(), file=f)
    with open("dataCharacterList.json", "r") as f:
        dataPlayer = ast.literal_eval(f.read())
    with open("dataCharacterList.json", "w") as f:
        json.dump(dataPlayer, f, indent=2)
    for uuid, player in dataPlayer.items():
        print(f"Class: {player["type"]}, UUID: {uuid}")

if choice == "4":
    choiceUser = input("Please enter an username: ")
    response = requests.get(
        f"https://api.wynncraft.com/v3/player/{choiceUser}/characters",
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    with open("dataCharacterList.json", "w") as f:
        print(response.json(), file=f)
    with open("dataCharacterList.json", "r") as f:
        dataPlayer = ast.literal_eval(f.read())
    with open("dataCharacterList.json", "w") as f:
        json.dump(dataPlayer, f, indent=2)
    for uuid, player in dataPlayer.items():
        print(f"Class: {player["type"]}, UUID: {uuid}")
    choiceClass = input("Enter the UUID of the class you want to see: ")
    response = requests.get(
        f"https://api.wynncraft.com/v3/player/{choiceUser}/characters/{choiceClass}",
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    with open("dataCharacterDetails.json", "w") as f:
        print(response.json(), file=f)
    with open("dataCharacterDetails.json", "r") as f:
        dataCharacter = ast.literal_eval(f.read())
    with open("dataCharacterDetails.json", "w") as f:
        json.dump(dataCharacter, f, indent=2)
    
    print (f'Type: {dataCharacter["type"]}')
    print (f'Nickname: {dataCharacter["nickname"]}')
    print (f'Level: {dataCharacter["level"]}')
    print (f'XP: {dataCharacter["xp"]}')
    print (f'Total level: {dataCharacter["totalLevel"]}')
    print (f'Gamemode: {dataCharacter["gamemode"]}')
    print (f'Content completion: {dataCharacter["contentCompletion"]}')
    print (f'Wars: {dataCharacter["wars"]}')
    print (f'Playtime: {dataCharacter["playtime"]}')
    print (f'Mobs killed: {dataCharacter["mobsKilled"]}')
    print (f'Chests found: {dataCharacter["chestsFound"]}')
    print (f'Items identified: {dataCharacter["itemsIdentified"]}') #i do not know why this thing stays 0 every single time, blame wynncraft again
    print (f'Blocks walked: {dataCharacter["blocksWalked"]}') #i give up
    print (f'Logins: {dataCharacter["logins"]}')
    print (f'Deaths: {dataCharacter["deaths"]}')
    print (f'Discoveries: {dataCharacter["discoveries"]}')

    pvp = dataCharacter["pvp"]
    print (f'PVP kills: {pvp["kills"]}')
    print (f'PVP deaths: {pvp["deaths"]}')

    print ("\n")
    sp = dataCharacter.get("skillPoints", {})
    for stat in ("strength", "dexterity", "intelligence", "defense", "agility"):
        print (f"{stat.capitalize()}: {sp.get(stat, 0)}")
    
    print ("\n")
    raidChara = dataCharacter.get("raids", {})
    print (f"Raids: {raidChara.get("total", 0)}")
    raidCharaList = raidChara.get("list", {})
    for raidList in ("The Canyon Colossus", "Orphion's Nexus of Light", "The Nameless Anomaly", "Nest of the Grootslangs", "The Wartorn Palace"):
        print (f'{raidList}: {raidCharaList.get(raidList, 0)}')

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
