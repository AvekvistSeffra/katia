import glooey
from core.graphics.widgets.labels import TitleButtonLabel
import globalvars

class TitleButton(glooey.Button):
    custom_font_name = globalvars.fonts["title"]
    custom_font_size = 24
    custom_alignment = "center"
    Foreground = TitleButtonLabel
