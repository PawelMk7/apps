"""
Pmk
English Interactive Dictionary
"""

import os
import json
import difflib

os.getcwd()
os.chdir(r'D:\Github_Projects\10 Apps/'.replace(os.sep , os.altsep))
data = json.load(open('data.json'))

def keydefinition(key):
    if key.lower() in data.keys():
        return data[key]
    elif difflib.get_close_matches(key.lower(), data.keys(), cutoff=0.8) != []:
        similar = difflib.get_close_matches(key.lower(), data.keys(), cutoff=0.8)[0].capitalize()
        comfirmation = input(f"This dictionary doesn't contain word '{key}'. Did you mean '{similar}'? Please write Y if yes, or N if no.\n[Y]/[N]: ")
        if comfirmation == 'Y':
            return data[similar.lower()]
        elif comfirmation == 'N':
            return 'Thank you for using my dictionary.'
        else:
            return 'Your entrance was not recognized as Y or N.'
    else:
        return 'This dictionary does not contain such word or similar to it.'

key = input('Enter a word you would like to translate: ')


if isinstance(keydefinition(key), list):
    print(key.capitalize() + ':')
    for i in keydefinition(key):
        print('\n' + i)
else:
    print(keydefinition(key))




