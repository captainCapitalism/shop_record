class MenuPosition:
    def __init__(self, string):
        self.everything = string.split(';')
        try:
            self.name = self.everything[0].strip()
            self.def_price = float(self.everything[1].strip())
            self.pot_price = float(self.everything[2].strip())
            self.gaiwan_price = float(self.everything[3].strip())
            self.bulk_price = float(self.everything[4].strip())
            self.package_price = float(self.everything[5].strip())
            self.code = self.everything[6].strip()
        except ValueError:
            print("Value in " + self.name + " is not number or missing")


def find_menu_position(string, menu):
    names = [o.name for o in menu]
    print(names)
    return menu[names.index(string)]


def create_menu():
    filename = "values/MenuPositions.txt"
    file = open(filename, 'r')
    split_file = file.read().split('\n')
    menu_positions = []

    for line in split_file:
        if line != '':
            menu_positions.append(MenuPosition(line))
    file.close()
    menu_positions.__delitem__(0)

    return menu_positions
