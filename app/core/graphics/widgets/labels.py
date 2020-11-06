import glooey
import globalvars

class TitleLabel(glooey.Label):
    custom_font_name = globalvars.fonts["title"]
    custom_font_size = 24
    custom_color = globalvars.current_scheme["text_color"]
    custom_alignment = "center"

class TitleButtonLabel(glooey.Label):
    custom_font_name = globalvars.fonts["button"]
    custom_font_size = 24
    custom_color = globalvars.current_scheme["button_text_color"]
    custom_alignment = "center"
