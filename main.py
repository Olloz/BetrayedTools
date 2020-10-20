import requests
import json

def linkeddiscord():
    json_data = open('private.json')
    hypixeldata = json.load(json_data)
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

linkeddiscord()
