import json

with open("sample_game.json", "r", encoding="utf-8") as f:
    game_data = json.load(f)

with open("game.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("__GAME_DATA__", json.dumps(game_data))

with open("game_final.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Game built: game_final.html")
