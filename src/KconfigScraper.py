import sys,os

def main():
    if not os.path.exists("linux"):
        raise Exception("No linux repository found! Please clone the linux repo in the src directory and try again.")
    
    source_config = os.path.join(os.getcwd(), "linux/Kconfig")
    main_menu_title = ""
    top_level_menus = []
    
    with open(source_config, "r") as f:
        while (line := f.readline()) != "":
            if "mainmenu" in line:
                main_menu_title = line.replace("mainmenu ", "")
            elif "source" in line and "debug" not in line and "freezer" not in line and "binfmt" not in line and "scripts" not in line:
                source_file_path = line.split("\"")[1] # retrieves the path to the Kconfig file from within the parenthesis
                top_level_menus.append(source_file_path)
    for menu in top_level_menus:
        with open(os.path.join(os.getcwd(), "linux", menu)) as f:
            print(f.read())



if __name__ == "__main__":
    main()
