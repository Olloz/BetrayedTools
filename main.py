import requests
import json
import time

json_data = open('private.json')
hypixeldata = json.load(json_data)
def linkeddiscord():

    data = requests.get(f'https://api.hypixel.net/guild?key={hypixeldata["hypixelKey"]}&name=Betrayed').json()
    guildMembers = [member["uuid"] for member in data["guild"]["members"]]
    for i in guildMembers:
        data2 = requests.get(f'https://api.hypixel.net/player?key={hypixeldata["hypixelKey"]}&uuid={i}').json()
        name = data2['player']['displayname']
        discord = data2['player'].get('socialMedia')
        if discord:
            print(f"{name}'s Linked Discord - {discord['links']['DISCORD']}")
        else:
            print(f"{name}'s Linked Discord - None")



def gexp():

    REQUIREMENT = 10000000000
    currentTime = int(time.time() * 1000)
    people = []
    data = requests.get(
        f"https://api.hypixel.net/guild?key={hypixeldata['hypixelKey']}&name=Betrayed").json()
    def getTotal(arr, length):
        total = 0
        for i in arr:
            total += i
        if len(arr) < length and total < REQUIREMENT:
            total = -1
        return total
    guildMembers = data["guild"]["members"]
    for guildMember in guildMembers:
        player = guildMember["uuid"]
        totalExp = getTotal(guildMember["expHistory"].values(), 7)
        if totalExp < REQUIREMENT and currentTime - guildMember["joined"] > 691200000:
            data2 = requests.get(
                f"https://api.hypixel.net/player?key={hypixeldata['hypixelKey']}&uuid=" + player).json()
            playerIGN = data2["player"]["displayname"]
            try:
                disc = data2["player"]["socialMedia"]["links"]["DISCORD"]
            except KeyError:
                disc = ""
            if disc != "":
                print("@" + disc)
            temp = [playerIGN, totalExp]
            people.append(temp)
            people.sort(key=lambda x: x[1])
    for i in people:
        print(i)

script = input("What script would you like to run? ")
if script == "GEXP":
    gexp()
elif script == "Linked Discord":
    linkeddiscord()
else:
    print("No Script found.")