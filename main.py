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

    data = requests.get(f'https://api.hypixel.net/guild?key={hypixeldata["hypixelKey"]}&name=Betrayed').json()
    values = sorted([(member["uuid"], total) for member in data["guild"]["members"] if
                     (total := sum(member["expHistory"].values())) < 30000], key=lambda x: x[1], reverse=True)

    def to_username(uuid):
        return \
        requests.get(f"https://api.hypixel.net/player?key={hypixeldata['hypixelKey']}&uuid={uuid}").json()["player"][
            "displayname"]

    for value in values:
        player = value[0]
        username = to_username(value[0])
        gexp = value[1]
        data2 = requests.get(f"https://api.hypixel.net/player?key={hypixeldata['hypixelKey']}&uuid={player}").json()
        if not "player" in data2:
            print("Error")
            continue
        disc = "VERIFICATION REQUIRED"
        if "socialMedia" in data2['player'] and "DISCORD" in data2["player"]['socialMedia']['links']:
            disc = data2['player']['socialMedia']['links']['DISCORD']
        print(f"{username} - {gexp} - {disc}")

script = input("What script would you like to run? ")
if script == "GEXP":
    gexp()
elif script == "Linked Discord":
    linkeddiscord()
else:
    print("No Script found.")