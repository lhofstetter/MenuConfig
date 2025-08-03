class ConfigItem:
    def __init__(self, name: str, human_readable_name: str, description: str, suggestion: bool, warning: str = None, selected: bool = False, tristate: str = "n" , depends_on: list = [], is_dependency_of: list = [], selects: list = []):
        self.name = name
        self.human_readable_name = human_readable_name
        self.description = description
        self.suggestion = suggestion
        self.warning = warning
        self.depends_on = depends_on
        self.is_dependency_of = is_dependency_of
        self.selects = selects
        self.selected = selected
        self.tristate = tristate

    def select():
        self.selected = not self.selected

