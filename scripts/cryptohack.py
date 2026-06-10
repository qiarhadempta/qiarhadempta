import requests, json, re
from datetime import datetime

USERNAME = "schrodycat"

r = requests.get(f"https://cryptohack.org/api/user/{USERNAME}/")
data = r.json()

score    = data.get("score", 0)
rank     = data.get("rank", 0)
level    = data.get("level", 0)
solved   = len(data.get("solved_challenges", []))
updated  = datetime.utcnow().strftime("%d %b %Y, %H:%M UTC")

block = f"""<!-- CRYPTOHACK_START -->
![Score](https://img.shields.io/badge/Score-{score}pts-C9B1FF?style=flat-square)
![Rank](https://img.shields.io/badge/Rank-%23{rank}-a78bfa?style=flat-square)
![Solved](https://img.shields.io/badge/Solved-{solved}%20challenges-7c5cbf?style=flat-square)
![Level](https://img.shields.io/badge/Level-{level}-c9d1d9?style=flat-square)

> Updated: {updated}
<!-- CRYPTOHACK_END -->"""

with open("README.md", "r") as f:
    readme = f.read()

readme = re.sub(
    r"<!-- CRYPTOHACK_START -->.*?<!-- CRYPTOHACK_END -->",
    block,
    readme,
    flags=re.DOTALL
)

with open("README.md", "w") as f:
    f.write(readme)

print(f"Updated: score={score}, rank={rank}, solved={solved}")
