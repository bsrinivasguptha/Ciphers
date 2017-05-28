#!/bin/python
# -*- coding: utf-8 -*-

#############################################################################
###                                                                       ###
###  Description: Uses a .txt file that has a plethora of                 ###
###               english dictionary words contained within               ###
###               to tell if the message is actually english              ###
###               or still cipher text.                                   ###
###                                                                       ###
###    Code Provided by:                                                  ###
### https://github.com/asweigart/codebreaker/blob/master/detectEnglish.py ###
#############################################################################

__author__  = "Tyler Hall"
__copyright__ = "Copyright 2017"

###################
#     IMPORTS     #
###################

###################
#      GLOBAL     #
###################

LOWERLETTERS = 'abcdefghijklmnopqrstuvwxyz'
LETTERS_AND_SPACE = LOWERLETTERS.upper() + LOWERLETTERS + ' \t\n'

def load_dictionary():
    dictionaryFile = open('./dictionary.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords

ENGLISH_WORDS = load_dictionary()

###################
#    FUNCTIONS    #
###################

# Method: Takes a message and checks to see the total number of english words found
# Param: message : string to be tested
# Returns: Float number of total amount of english words
def get_english_count(message):
    message = message.lower()
    message = rm_non_alpha(message)
    possible_words = message.split()

    if possible_words == []:
        return 0.0

    matches = 0
    for word in possible_words:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possible_words)

# Method: Takes a message and removes all symbols
# Param: message : string to be removed of symbols
# Returns: List of only Letters
def rm_non_alpha(message):
    only_letters = []
    for symbol in message:
            if symbol in LETTERS_AND_SPACE:
                only_letters.append(symbol)
    return ''.join(only_letters)

# Method: Takes a file and decrypts the entire file with the encrypted string:key format
# Param: message : the path to the file with the encrypted string
#        wordPercentage (default: 20%) : words that exist in the dictionary file
#        letterPercentage (default: 85%) : characters in the message must be letters / spaces
# Returns: Boolean of True or False
def isEnglish(message, wordPercentage=20, letterPercentage=85):
    wordsMatch = get_english_count(message) * 100 >= wordPercentage
    numLetters = len(rm_non_alpha(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch
