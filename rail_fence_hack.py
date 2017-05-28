#!/bin/python
# -*- coding: utf-8 -*-

#############################################################################
###                                                                       ###
###  Description:  Functions for encrypting and decrypting a message      ###
###                using the zigzag method. Which produces an array       ###
###                that if written out properly will look as though       ###
###                the word was written in a zigzag format                ###
###                                                                       ###
#############################################################################

__author__  = "Tyler Hall"
__copyright__ = "Copyright 2017"

###################
#     IMPORTS     #
###################

from rail_fence_cipher import decrypt
from detectEnglish import isEnglish

###################
#      GLOBAL     #
###################

###################
#    FUNCTIONS    #
###################

def zigzag_cracker(message):
    all_trans = []
    translated = ''
    for size in range(2, len(message)-1, 1):
        translated = decrypt(message, size)

        if isEnglish(translated, 80):
            all_trans.append(translated)
    return all_trans
