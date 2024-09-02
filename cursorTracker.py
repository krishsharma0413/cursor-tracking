import mouse
import json
import time
from datetime import datetime
from pytz import timezone

ist = timezone("Asia/Kolkata")
fileName = f"./data/corpus-{int(datetime.now(ist).timestamp())}.json"
universalDict = []

def listener(e):
    universalDict.append({x:y for x,y in zip(("x", "y"), mouse.get_position())})
    with open(fileName, "w", encoding="utf-8") as f:
        json.dump({"data":universalDict}, f, ensure_ascii=False, indent=4)

mouse.hook(listener)

while 1:
    time.sleep(1)