"""Word Finder: finds random words from a dictionary."""

"""
>>> wf = WordFinder("words.txt")
3 words read

>>> wf.random()
'cat'

>>> wf.random()
'cat'

>>> wf.random()
'porcupine'

>>> wf.random()
'dog'
"""
import random


class WordFinder:
    def __init__ (self,file):
        dictionary = open(file)

        self.words = self.word_List(dictionary)

        num_words = len(self.words)

        print(f"{num_words} words read")

    def word_List(self,dictionary):
        return [word.strip() for word in dictionary]

    def random(self):
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):


    def word_List(self,dictionary):
        return [word.strip() for word in dictionary if len(word.strip()) > 0 and not word.startswith("#")]  
   
