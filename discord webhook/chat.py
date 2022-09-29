# sends all the current bloxflip chat to your discord webhook

import requests
import time
import datetime


chaturl = "https://api.bloxflip.com/chat/history"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36", 'Accept-Encoding': 'gzip, deflate, br', 'Accept': '*/*', 'Connection': 'keep-alive'}




webhook = "" #enter your webhook url

while True:
  ct = datetime.datetime.now()
  r = requests.get(url=chaturl, headers=headers)
  chat = r.json()

  latestchat = chat["messages"][0]["content"]
  username = chat["messages"][0]["bloxFlipUser"]["robloxUsername"]
  userrobloxid = str(chat["messages"][0]["bloxFlipUser"]["robloxId"])
  profile = f"https://www.roblox.com/headshot-thumbnail/image?userId={userrobloxid}&width=50&height=50&format=png"

  payload = {
    "embeds": [
      {
      "description": latestchat,
      "color": 5791892,
        "author": {
        "name": username,
        "icon_url": profile
        },
          "footer": {
            "text": f"Today at {ct}"
          }
      }
    ],
    }
  webhooksend = requests.post(url=webhook, json=payload)
  print(webhooksend.status_code )
  time.sleep(1)
