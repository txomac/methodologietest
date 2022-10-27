import unittest
import main
from datetime import *


class TestMain(unittest.TestCase):
    def test_heure_morning(self):
        now = datetime.now().replace(hour=8)
        self.assertEqual(main.heureActuelle(now), "Bonjour")

    def test_heure_evening(self):
        now = datetime.now().replace(hour=18)
        self.assertEqual(main.heureActuelle(now), "Bonsoir")

    def test_heure_noon(self):
        now = datetime.now().replace(hour=13)
        self.assertEqual(main.heureActuelle(now), "Bon appétit")

    def test_heure_night(self):
        now = datetime.now().replace(hour=21)
        self.assertEqual(main.heureActuelle(now), "Bonne nuit")

    def test_palindrome_false(self):
        mot = "toto"
        self.assertEqual(main.miroir(mot), False)


    def test_palindrome_true(self):
        mot = "totot"
        self.assertEqual(main.miroir(mot), True)


if __name__ == '__main__':
    unittest.main()
