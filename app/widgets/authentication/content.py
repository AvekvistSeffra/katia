import glooey
from core.graphics.widgets.buttons import TitleButton
from core.graphics.widgets.labels import TitleLabel
import globalvars

class AuthenticationContent(glooey.VBox):
    globalvars.current_scheme["background_color"]
    
    def __init__(self):
        super().__init__()

        self.add(TitleLabel("IP Address"))
        self.add(TitleLabel("Port"))
        self.add(TitleLabel("Username"))
        self.add(TitleLabel("Password"))

        button = TitleButton("Log in")
        button.push_handlers(on_click=lambda w: print(f"{w} clicked!"))
        self.add(button)
