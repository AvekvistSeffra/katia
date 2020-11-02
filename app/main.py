import pyglet
import glooey

window = pyglet.window.Window(640, 480, "Katia", resizable=True)
window.set_icon(pyglet.image.load("images/katia_icon.jpg"))
window.set_minimum_size(400, 300)

gui = glooey.Gui(window)

class WesnothLabel(glooey.Label):
    custom_font_name = "Lato Regular"
    custom_font_size = 10
    custom_color = "#b9ad86"
    custom_alignment = "center"

label = WesnothLabel("Hello, world!")

button = glooey.Button("Click here!")
button.push_handlers(on_click = lambda w: print(f"{w} clicked!"))

vbox = glooey.VBox()
vbox.add(WesnothLabel("Hello, world!"))
vbox.add(button)

hbox = glooey.HBox()
hbox.add(vbox)
hbox.add(WesnothLabel("Baibai!"))

gui.add(hbox)

@window.event
def on_resize(width, height):
    pass

pyglet.app.run()
