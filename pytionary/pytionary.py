import requests
from bs4 import BeautifulSoup
try:
    from .util import make_connection
except ImportError:
    from util import make_connection

class Pytionary:
    ''' pytionary main class'''
    #validate if its a single word
    @staticmethod
    def single_word_check(word):
        ''' raise exception if word length != 1 '''
        if len(word.split()) != 1:
            raise Exception("Must be a single word") 

    #get word pos 
    def pos(self, word):
        ''' get the pos of the word '''
        self.single_word_check(word)
        soup = make_connection('thesaurus', word)
        try:
            pos_word = soup.find('em', class_='css-siah4c e9i53te8').text   
        except:
            pos_word = ''
        return pos_word

    def meanings(self, word):
        ''' get the meaning of the word '''
        self.single_word_check(word)
        definitions = []
        soup = make_connection('dictionary', word)
        try:
            description_tags = soup.find_all('div', class_='e1q3nk1v3')
            #first clear the examples from definiton tag
            #Handle example not found error
            for desc in description_tags:
                try:
                    desc.find('span', class_='luna-example').clear()
                except:
                    continue
                finally:
                    definitions.append(desc.text)
        except:
            pass    
        return definitions

    def synonyms(self, word):
        ''' get synonyms '''
        self.single_word_check(word)
        synonyms_list = []
        soup = make_connection('thesaurus', word)
        try:
            synonym_tags = soup.find('ul', class_='css-1lc0dpe et6tpn80').find_all('li')
            for syn in synonym_tags:
                try:
                    synonyms_list.append(syn.span.a.text)
                except:
                    continue
        except:
            pass
        return synonyms_list

    def antonyms(self, word):
        ''' get antonyms '''
        self.single_word_check(word)
        antonyms_list = []
        soup = make_connection('thesaurus', word)
        try:
            antonym_tags = soup.find_all('ul', class_='css-1lc0dpe et6tpn80')[1]
            for ant in antonym_tags:
                try:    
                    antonyms_list.append(ant.span.a.text)
                except:
                    continue
        except:
            pass
        return antonyms_list
