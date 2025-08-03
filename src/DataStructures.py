import time

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

class ConfigMenuNode:
    """
    Implements a node class for a linked list-esque data structure that tracks sub-menus and config items at each level of the tree. 
    
    ...

    Attributes
    ----------
    title : str
        title/name of the menu that this node represents
    data : list
        list of ConfigItems' and ConfigMenuNodes' which represent the items listed under this menu
    previous_node : ConfigMenuNode
        previous ConfigMenuNode, which represents the "parent" menu that this node comes from
    last_updated : int
        timestamp (in seconds) of the last time this node's data attribute was updated

    Methods
    -------
    status(info_level=0):
        Prints out information about the current status of the node, the amount of which depends on the information level passed in as a parameter.
    """

    def __init__(self, title: str, previous_node = None):
        """
        Initializes a new ConfigMenuNode with a menu title, the previous node in the "list" (if applicable) and an empty list which will store newly discovered ConfigItems' and ConfigMenuNodes'.
        
        Parameters
        ----------
            title : str
                title of the config menu
            previous_node : ConfigMenuNode
                Previous node in the "list", representing the parent menu that this menu was listed under.
        """
        self.title = title
        self.data = []
        self.previous_node = previous_node
        self.last_updated = time.time()

    def status(self, info_level=0):
        """
        status(info_level=0)

        Prints the current status of the node, with more detailed information appearing with higher values for the log_level.

            Parameters:
                info_level (int): a positive integer corresponding to the level of information the user would like to receive. The levels and their corresponding meanings are:
                    0: the title of the node
                    1: length of the node's data attribute (provides a measure of how many nodes and ConfigItems are currently stored under this node)
                    2: individual amounts of ConfigMenuNodes and ConfigItems present in this node's data attribute
                    4: how long it's been since this particular node was updated
                
                NOTE: Any info level above 4 or below 0 is meaningless and will simply output the level of information associated with the closest valid level to the passed value.
                Additionally, please note that the info levels are inclusive, e.g a log level of 1 will output both the title of the node AND the length of the node's data attribute.
        """
        if info_level < 0:
            info_level = 0
        print("------------------------------ NODE INFO ------------------------------")
        if info_level >= 0:
            print(f"TITLE: {self.title}")

        if info_level >= 1:
            print(f"NUMBER OF NODES + CONFIG ITEMS = {len(self.data)}")

        if info_level >= 2:
            number_of_nodes = 0
            number_of_config_items = 0

            for item in self.data:
                if isinstance(item, ConfigItem):
                    number_of_config_items += 1
                else:
                    number_of_nodes += 1

            print(f"NUMBER OF NODES: {number_of_nodes}\nCONFIG ITEMS: {number_of_config_items}")

        if info_level >= 3:
            print(f"TIME SINCE LAST UPDATE: {time.time() - self.last_updated}")

        
            
