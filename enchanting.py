class Weapon:
    def __init__(self, name):
        self.name = name
        self.spell = null_spell

    @property
    def enchanted_name(self):
        return " ".join(filter(None, (self.spell.name, self.name)))

    def __str__(self):
        lines = [
            self.enchanted_name,
            "5 - 10 attack damage",
            "1.2 attack speed",
            self.spell.attribute
        ]
        return "\n".join(filter(None, lines))


class Spell:
    def __init__(self, name, attribute):
        self.name = name
        self.attribute = attribute


null_spell = Spell(name='', attribute='')
