class Weapon:
    def __init__(self, name):
        self.name = name
        self.attribute = None

    def enchant(self, prefix, attribute):
        self.name = prefix + " " + self.name
        self.attribute = attribute

    def show(self):
        lines = [
            self.name,
            "5 - 10 attack damage",
            "1.2 attack speed",
            self.attribute
        ]
        return "\n".join(l for l in lines if l is not None)
