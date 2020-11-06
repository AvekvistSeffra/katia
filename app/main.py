from typing import cast
import pyglet
import glooey
import json
import sys

import log

class Spell:
    def __init__(self, name, level, school, ritual, casting_time, components, duration, classes, description, upcasting, script):
        self.name = name
        self.level = level
        self.school = school
        self.ritual = ritual
        self.casting_time = casting_time
        self.components = components
        self.duration = duration
        self.classes = classes
        self.description = description
        self.upcasting = upcasting
        self.script = script

classes = dict()
spells = dict()

logger = log.Log("Core", log.LogLevel.INFO, filepath="log.txt")

try:
    with open("data/compendium/spells.json") as f:
        spells = json.loads(f.read())
    with open("data/compendium/classes.json") as f:
        classes = json.loads(f.read())
    for spell in spells:
        if spell["name"] != "":
            logger.trace(spell["name"])
    for cls in classes:
        if cls["name"] != "":
            logger.trace(cls["name"])
except FileNotFoundError:
    logger.error("Could not find file 'compendium.json' in 'data' folder. \nTry downloading one from GitHub or building your own. ")
    sys.exit(1)

window = pyglet.window.Window(640, 480, "Katia", resizable=True)
window.set_icon(pyglet.image.load("data/icon/katia.ico"))
window.set_minimum_size(400, 300)

gui = glooey.Gui(window)

class WesnothLabel(glooey.Label):
    custom_font_name = "Lato Regular"
    custom_font_size = 10
    custom_color = "#b9ad86"
    custom_alignment = "center"

label = WesnothLabel(spells[0]["name"])

button = glooey.Button(spells[1]["name"])
button.push_handlers(on_click = lambda w: print(f"{w} clicked!"))

vbox = glooey.VBox()
vbox.add(label)
vbox.add(button)

hbox = glooey.HBox()
hbox.add(vbox)
hbox.add(WesnothLabel(classes[0]["name"]))

gui.add(hbox)

@window.event
def on_resize(width, height):
    gui.resize()
    pass

pyglet.app.run()
