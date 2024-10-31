import unittest

import enchanting


class EnchantingTest(unittest.TestCase):
    def test_show_weapon_includes_name_damage_and_speed(self):
        weapon = enchanting.Weapon("dagger")
        
        text = weapon.show()

        self.assertIn("dagger", text)
        self.assertIn("attack speed", text)
        self.assertIn("attack damage", text)

        self.assertEqual(len(text.split("\n")), 3)

    def test_weapon_has_enchantment(self):
        weapon = enchanting.Weapon("dagger")
        weapon.enchant("Spell", "+5 points")

        text = weapon.show()

        self.assertIn("Spell dagger", text)

if __name__ == "__main__":
    unittest.main()
