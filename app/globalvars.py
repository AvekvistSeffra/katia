import core.log as log
import sys
import json

logger = log.Log("Runtime", log.LogLevel.WARN, filepath="log.txt")

style = dict()

try:
    with open(f"data/graphics/style.json") as f:
        style = json.loads(f.read())
except FileNotFoundError:
    logger.error("Could not find 'style.json' in 'data/graphics'. Try downloading one from GitHub or making your own. ")
    sys.exit(1)

fonts = style["fonts"]
current_scheme = style["color_scheme"]

print(current_scheme["text_color"])
