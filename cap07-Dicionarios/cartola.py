import requests, json

clubes = requests.get("https://api.cartola.globo.com/clubes").text
clubes = json.loads(clubes)

for clube in clubes.values():
    print (clube["nome"], clube["escudos"]["45x45"])