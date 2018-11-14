class Trash:
    def __init__(self):
        """
        This class is to serialize Japanese trash.
        name = trash name
        category = what kind of trash...ex flammables, non-flammables etc...
        method = sentence that explain how to throw a way the trash 
        """
        self.name = ""
        self.category = ""
        self.description = ""

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_category(self):
        return self.category

    def set_category(self, category):
        self.category = category

    def get_method(self):
        return self.description

    def set_method(self, description):
        self.description = description

    def generate_new_trash(self, name,category, description):
        return Trash(name, category, description)


