#!/bin/python
# -*- coding: utf-8 -*-

######################################################################
###                                                                ###
###  Description: Takes raw string and shifts the characters       ###
###               to produce the cipher text.                      ###
###                                                                ###
###                                                                ###
######################################################################

__author__  = "Tyler Hall"
__copyright__ = "Copyright 2017"

###################
#     IMPORTS     #
###################

###################
#      GLOBAL     #
###################

key_int_let = { 0 : 'a',
                1 : 'b',
                2 : 'c',
                3 : 'd',
                4 : 'e',
                5 : 'f',
                6 : 'g',
                7 : 'h',
                8 : 'i',
                9 : 'j',
                10 : 'k',
                11 : 'l',
                12 : 'm',
                13 : 'n',
                14 : 'o',
                15 : 'p',
                16 : 'q',
                17 : 'r',
                18 : 's',
                19 : 't',
                20 : 'u',
                21 : 'v',
                22 : 'w',
                23 : 'x',
                24 : 'y',
                25 : 'z'
                }

key_let_int = { 'a' : 0,
                'b' : 1,
                'c' : 2,
                'd' : 3,
                'e' : 4,
                'f' : 5,
                'g' : 6,
                'h' : 7,
                'i' : 8,
                'j' : 9,
                'k' : 10,
                'l' : 11,
                'm' : 12,
                'n' : 13,
                'o' : 14,
                'p' : 15,
                'q' : 16,
                'r' : 17,
                's' : 18,
                't' : 19,
                'u' : 20,
                'v' : 21,
                'w' : 22,
                'x' : 23,
                'y' : 24,
                'z' : 25
                }

###################
#    FUNCTIONS    #
###################

# Desc : Takes a string and shifts the letters
# Param : raw : plain text
#         key : int from 1 to 25 that the plain text will be shifted by
#Returns : String
def encrypt(raw, key):
    #Variables
    encrypt_string = ''

    #Goes through each character in raw string to produce ciphertext
    for char in raw.lower():
        if char.isalpha():
            encrypt_string += key_int_let[ (key_let_int[char] + key) % 26]
        else:
            encrypt_string += char

    return encrypt_string

# Desc : Takes a cipher text and shifts the letters back to original
# Param : encrypted : cipher text
#         key : int from 1 to 25 that was used by the encrypted string
#Returns : String
def decrypt(encrypted, key):
    #Variables
    decrypt_string = ''

    # Goes through ciphertext to produce original plaintext
    for char in encrypted.lower():
        if char.isalpha():
            decrypt_string += key_int_let[ (key_let_int[char] - key) % 26]
        else:
            decrypt_string += char
            
    return decrypt_string

###################
#       MAIN      #
###################
