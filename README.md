Pytionary - A cool dictionary module for python to get meanings, pos, synonyms, antonyms of the given word. <br /> 
It uses requests and BeautifulSoup as dependencies.
<h3>Installation</h3>
The easiest way to install is through pip:

```
pip install pytionary
```

With Easy_Install
```
easy_install pytionary
```
<h3>Usage</h3>
It is very easy to get started with pytionary. You just create an instance of the Pytionary class.

```
from pytionary import Pytionary    #import module
gloss = Pytionary()    #create object
```

This will create an instance of the pytionary class. Now, you have access to its methods.<br /><br />
To get the meaning of the word:
```
print(gloss.meanings('tuna'))
```
This returns a list of the meanings. For example: 
```
['any of several large food and game fishes of the family Scombridae, inhabiting temperate and tropical seas.Compare albacore, bluefin tuna, yellowfin tuna.', 'any of various related fishes.', ' Also called tuna fish. the flesh of the tuna, used as food.', 'any of various prickly pears, especially either of two erect, treelike species, Opuntia tuna or O.
ficus-indica, of Mexico, bearing a sweet, edible fruit.', 'the fruit of these plants.', 'Also called: tunny any of various large marine spiny-finned fishes of the genus Thunnus, esp T. thynnus, chiefly of warm waters: family Scombridae .
They have a spindle-shaped body and widely forked tail, and are important food fishes', 'any of various similar and related fishes', 'any of various tropical American prickly pear cacti, esp Opuntia tuna, that are cultivated for their sweet edible fruits', 'the fruit of any of these cacti']
```

For pos (verb/adj/noun)
```
print(gloss.pos('tuna'))
```

For synonyms: 
```
print(gloss.synonyms('tuna'))
```

For antonyms:
```
print(gloss.antonyms('tuna'))
```

<h3>Full Example</h3>

```
from pytionary import Pytionary

word = 'tuna'

gloss = Pytionary() #Create object

print(gloss.pos(word))    #return pos(noun/verb/adj)
print(gloss.meanings(word))    #return meanings
print(gloss.synonyms(word))    #return synonyms
print(gloss.antonyms(word))    #return antonyms
```
