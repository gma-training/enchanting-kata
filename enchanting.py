class Weapon:
    def __init__(self, name):
        self.name = name

    def show(self):
        return f"""{self.name}
5 - 10 attack damage
1.2 attack speed
"""
