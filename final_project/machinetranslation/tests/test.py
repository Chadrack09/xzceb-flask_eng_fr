import unittest
from ../translator import english_to_french, french_to_english

class TestEnglishTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french(""),"Please enter a valid English word")
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertEqual(english_to_french("Goodbye"),"Au revoir")
        self.assertNotEqual(english_to_french("Goodbye"),"Bonjour")

class TestFrenchTranslator(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english(""),"Entrez un mot français valide")
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertEqual(french_to_english("Au revoir"),"Goodbye")
        self.assertNotEqual(french_to_english("Bonjour"),"Goodbye")

unittest.main()