import os
import sys
import unittest
import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pytioanry.pytionary import Pytionary
from pytionary.util import make_connection

glossary = Pytionary()

class TestPytionary(unittest.TestCase):
    ''' test pytionary '''
    
    word = 'tuna'

    def test_make_connection(self):
        ''' test connection '''
        connection_1 = requests.get(f'http://www.thesaurus.com/browse/{self.word}')
        connection_2 = requests.get(f'http://www.dictionary.com/browse/{self.word}')
        self.assertEqual(connection_1.status_code, 200)
        self.assertEqual(connection_2.status_code, 200)

    def test_meanings(self):
        ''' test meaning '''
        self.assertIsInstance(glossary.meanings(self.word), list)

    def test_synonyms(self):
        ''' test synonyms '''
        self.assertIsInstance(glossary.synonyms(self.word), list)

    def test_antonyms(self):
        ''' test antonyms '''
        self.assertIsInstance(glossary.antonyms(self.word), list)    

if __name__ == '__main__':
    unittest.main()
    