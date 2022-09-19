import json
from pathlib import Path

import difflib
from difflib import get_close_matches

contents = Path('/Users/neshat/Downloads/dictionarydata.json').read_text()
print(type(contents))

words_dict = json.loads(contents)

print(type(words_dict))

def take_lookup():
    
    word = input('enter the word:')

    for w in words_dict:
        if word in words_dict:
            print(words_dict[word])
            break
            
        else:
            guess = get_close_matches(word , words_dict)
            word = input('which one did you mean? {}'.format(guess))
        
take_lookup()


#second project

import json
from pathlib import Path

import difflib
from difflib import get_close_matches

contents = Path('/Users/neshat/Downloads/dictionarydata.json').read_text()
print(type(contents))

words_dict = json.loads(contents)

print(type(words_dict))

def take_lookup():
    
    word = input('enter the word:')

    for w in words_dict:

        if word in words_dict:
            print(words_dict[word])
            break
            
        else:
            guess = get_close_matches(word , words_dict)
            if len(guess) < 1:
                print("I don't know either. ask google")
                break
            else:
                word = input('which one did you mean? {}'.format(guess))
        
take_lookup()

