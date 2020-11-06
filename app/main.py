import pyglet
import core.graphics.window as window

if __name__ == "__main__":
    aw = window.AuthenticationWindow()
    pyglet.app.run()
    wh = window.KatiaWindow(640, 480, "Katia")
    pyglet.app.run()
