#!/bin/python
# -*- coding: utf-8 -*-

######################################################################
###                                                                ###
###  Description: Takes a message and brute forces its way         ###
###               through the ceasar cipher returning all          ###
###               values. Then will put it through                 ###
###               detectEnglish to thin possibile translations.    ###
######################################################################

__author__  = "Tyler Hall"
__copyright__ = "Copyright 2017"

###################
#     IMPORTS     #
###################
from detectEnglish import isEnglish
###################
# GLOBAL VARIABLE #
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
#     FUNCTIONS   #
###################

def hack(cipher):

    #Variables
    all_trans = []
    for key in range(26):

        translated = ''

        for char in cipher.lower():
            if char.isalpha():
                translated += key_int_let[ (key_let_int[char] - key) % 26]
            else:
                translated += char
        if isEnglish(translated, 60):
            all_trans.append(translated)

    return all_trans
###################
#       MAIN      #
###################
