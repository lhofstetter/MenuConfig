import sys,os

sys.path.append(os.path.join(os.getcwd(), "src"))

from textual.widgets import Label
from textual.widget import Widget

from DataStructures import ConfigItem

class VConfigItem(Widget):
    def __init__(self, config_item: ConfigItem, item_id: str) -> None:
        self.config_item = config_item
        self.item_id = item_id
        super().__init__()

    def compose(self):
        yield Label(self.config_item.name, id=self.item_id)

class ConfigList(Widget):
    def __init__(self, config_items: list[ConfigItem]):
        if len(config_items) == 0:
            raise Exception("You cannot have a ConfigList with no ConfigItems!")

        self.config_items = config_items
        super().__init__()

    def compose(self):
        for item in self.config_items:
            yield VConfigItem(item, "#" + item.name)


