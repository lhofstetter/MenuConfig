from textual.app import App
from textual.widgets import Header, Footer

import sys, os
sys.path.append(os.path.join(os.getcwd(), "src/CustomWidgets"))

from Menu import ConfigList, VConfigItem

class MainApp(App):
    item_1 = VConfigItem()
    item_2 = VConfigItem()

    def compose(self):
        yield Header()
        yield ConfigList(["item 1", "item 2"])
        yield Footer()
        
    def on_mount(self):
        self.title = "menuconfig"
    pass

if __name__ == "__main__":
    app = MainApp()
    app.run()
