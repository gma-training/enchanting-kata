import unittest

import enchanting


class WeaponTest(unittest.TestCase):
    def test_str_representing_weapon_includes_name_damage_and_speed(self):
        weapon = enchanting.Weapon("dagger")
        
        text = str(weapon)

        self.assertIn("dagger", text)
        self.assertIn("attack speed", text)
        self.assertIn("attack damage", text)

        self.assertEqual(len(text.split("\n")), 3)

    def test_weapon_description_includes_spell(self):
        weapon = enchanting.Weapon("dagger")

        weapon.spell = enchanting.Spell("Adjective", "+5 points")

        self.assertIn("Adjective dagger", str(weapon))


if __name__ == "__main__":
    unittest.main()
