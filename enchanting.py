import dataclasses


class Weapon:
    def __init__(self, name):
        self.name = name
        self.spell = None

    @property
    def prefixed_name(self):
        if self.spell is None:
            return self.name
        return self.spell.name + " " + self.name

    def show(self):
        lines = [
            self.prefixed_name,
            "5 - 10 attack damage",
            "1.2 attack speed",
            self.spell.attribute if self.spell else None
        ]
        return "\n".join(filter(None, lines))


@dataclasses.dataclass
class Spell:
    name: str
    attribute: str
