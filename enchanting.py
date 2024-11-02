import dataclasses


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


@dataclasses.dataclass
class Spell:
    name: str
    attribute: str


null_spell = Spell(name='', attribute='')
