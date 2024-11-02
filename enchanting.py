import dataclasses


class Weapon:
    def __init__(self, name):
        self.name = name
        self.spell_prefix = None
        self.spell_attribute = None

    def enchant(self, spell):
        self.spell_prefix = spell.name
        self.spell_attribute = spell.attribute

    @property
    def prefixed_name(self):
        if self.spell_prefix is None:
            return self.name
        return self.spell_prefix + " " + self.name

    def show(self):
        lines = [
            self.prefixed_name,
            "5 - 10 attack damage",
            "1.2 attack speed",
            self.spell_attribute
        ]
        return "\n".join(filter(None, lines))


@dataclasses.dataclass
class Spell:
    name: str
    attribute: str
