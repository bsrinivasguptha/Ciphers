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

###################
#      GLOBAL     #
###################

###################
#    FUNCTIONS    #
###################

# Method: takes a message and produces a zigzag array
# Param: text: message string
#        key: The number of rows that the cipher will
#             produce for the zigzag
# Returns: returns an array of the zigzag text
def fence(text, key):
    #Variables
    fence = [[None] * len(text) for n in range(key)]
    rails = range(key - 1) + range(key - 1, 0, -1)

    for n, x in enumerate(text):
        fence[rails[n % len(rails)]][n] = x

    if 0: # debug
        for rail in fence:
            print ''.join('.' if c is None else str(c) for c in rail)

    return [c for rail in fence for c in rail if c is not None]

# Method: takes a message and uses function fence
#         to produce the ciphered string
# Param: raw: plain text
#        key: The number of rows that the cipher will
#             produce for the zigzag
# Returns: the complete ciphered text
def encrypt(raw, key):
    return ''.join(fence(raw, key))

# Method: takes a ciphered message and uses function fence
#         to produce the plain text
# Param: decrypt: cipher text
#        key: The number of rows that was used in the
#             original cipher
# Returns: the original plain text
def decrypt(message, key):
    rng = range(len(message))
    pos = fence(rng, key)
    return ''.join(message[pos.index(key)] for key in rng)

###################
#       MAIN      #
###################
