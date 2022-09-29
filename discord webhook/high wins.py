# sends a message whenever there is a new high win in bloxflip

import requests
import json
import time
import datetime


url = "https://api.bloxflip.com/live-feed/high-wins"
webhook = "" #your webhook url

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36", 'Accept-Encoding': 'gzip, deflate, br', 'Accept': '*/*', 'Connection': 'keep-alive'}

while True:
    ct = datetime.datetime.now()
    r = requests.get(url=url, headers=headers)
    wins = r.json()

    betamount = wins["bets"][0]["bet"]
    winnings = wins["bets"][0]["winnings"]
    gamemode = wins["bets"][0]["gamemode"]
    robloxid = wins["bets"][0]["userId"]
    username = wins["bets"][0]["username"]
    multiplier = wins["bets"][0]["multiplier"]
    uuid = wins["bets"][0]["uuid"]
    profile = f"https://www.roblox.com/headshot-thumbnail/image?userId={robloxid}&width=50&height=50&format=png"

    payload = {
        "embeds": [
            {
                "title": "High Wins",
                "description": f"Bet amount: **{betamount}**\nWinning: **{winnings}** (**x{multiplier}** multiplier)\nGamemode: **{gamemode}**\n\nRoblox ID: **{robloxid}**\nUUID: **{uuid}**",
                "color":12799823,
                "author":{
                "name":username,
                "icon_url":profile
            },
                "footer":{
                    "text": f"Todat at {ct}"
                }
            }
        ],
    }
    posthighwins = requests.post(url=webhook, json=payload)
    print(str(posthighwins.status_code) + " sent")

    time.sleep(1)
