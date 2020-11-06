import pyglet
import glooey
import json
import core.log as log
import sys

class AuthenticationWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__(640, 480, "Katia Login", resizable=False)

        self.set_icon(pyglet.image.load("data/icon/katia.ico"))

class KatiaWindow(pyglet.window.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)
        
        self.width = width
        self.height = height
        self.title = title

        self.set_icon(pyglet.image.load("data/icon/katia.ico"))
        self.set_minimum_size(400, 300)

        self.gui = glooey.Gui(self)

        self.logger = log.Log("Application", log.LogLevel.INFO, filepath="log.txt")

    def on_draw(self):
        self.clear()

    def open_file(self, file):
        try:
            with open(f"data/compendium/{file}.json") as f:
                return json.loads(f.read())
        except FileNotFoundError:
            self.logger.error(f"Could not find file '{file}.json' in 'data/compendium' folder. \nTry downloading one from GitHub or making your own. ")
            sys.exit(1)

    def get_gui(self):
        return self.gui
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def get_title(self):
        return self.title
