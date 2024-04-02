from colorama import Fore
import requests as rq
from flask import Flask, request
import config

app = Flask(__name__)

print(Fore.GREEN, """
-----------------------------------------
 __          __  _     _                 _    _____
 \ \        / / | |   | |               | |  |  __ \\
  \ \  /\  / /__| |__ | |__   ___   ___ | | _| |__) | __ _____  ___   _
   \ \/  \/ / _ \ '_ \| '_ \ / _ \ / _ \| |/ /  ___/ '__/ _ \ \/ / | | |
    \  /\  /  __/ |_) | | | | (_) | (_) |   <| |   | | | (_) >  <| |_| |
     \/  \/ \___|_.__/|_| |_|\___/ \___/|_|\_\_|   |_|  \___/_/\_\\__, |
                                                                   __/ |
                                                                  |___/
""")
print(Fore.GREEN, "-----------------------------------------")

@app.route("/api/send/<channelid>/<webhook>", methods=['POST', 'GET'])
def api_send(channelid, webhook):
    if request.method == 'POST':
        data = request.json  
        if data is None:
            return "empty_data", 400  
        else:
            r = rq.post(url=f"https://discord.com/api/webhooks/{channelid}/{webhook}", json=data)
            return r.text
    elif request.method == 'GET':
        r = rq.get(url=f"https://discord.com/api/webhooks/{channelid}/{webhook}")
        return r.text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT)
