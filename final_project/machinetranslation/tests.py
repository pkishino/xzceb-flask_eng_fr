'''Translation service unittests'''
import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    '''Testing the E2F service'''
    def test1(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertEqual(english_to_french('NULL'),'NULL')
    def test2(self):
        self.assertNotEqual(english_to_french('Goodbye'),'Bonjour')
        self.assertNotEqual(english_to_french('NULL'),'')

class TestFrenchToEnglish(unittest.TestCase):
    '''Testing the F2E service'''
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(french_to_english('NULL'),'NULL')
    def test2(self):
        self.assertNotEqual(french_to_english('Au revoir'),'Hello')
        self.assertNotEqual(french_to_english('NULL'),'')

unittest.main()