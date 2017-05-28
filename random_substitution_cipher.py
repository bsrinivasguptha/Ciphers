#!/bin/python
# -*- coding: utf-8 -*-

######################################################################
###                                                                ###
###  Description: Functions for encrypting and decrypting using    ###
###               the random substitution cipher method. The       ###
###               encryption method writes to a txt file that      ###
###               formats encryption string:key. This file can     ###
###               then be read by the decrypt_by_file function.    ###
###                                                                ###
######################################################################

__author__  = "Tyler Hall"
__copyright__ = "Copyright 2017"

###################
#     IMPORTS     #
###################
import random
import os
import copy

###################
# GLOBAL VARIABLE #
###################
alphabet = 'abcdefghijklmnopqrstuvwxyz'

key_dic = {'a' : '0',
                'b' : '1',
                'c' : '2',
                'd' : '3',
                'e' : '4',
                'f' : '5',
                'g' : '6',
                'h' : '7',
                'i' : '8',
                'j' : '9',
                'k' : '10',
                'l' : '11',
                'm' : '12',
                'n' : '13',
                'o' : '14',
                'p' : '15',
                'q' : '16',
                'r' : '17',
                's' : '18',
                't' : '19',
                'u' : '20',
                'v' : '21',
                'w' : '22',
                'x' : '23',
                'y' : '24',
                'z' : '25'
                }
### TO BE USED LATER ###
freq_letter = {'e' : 12.702,
                't' : 9.056,
                'a' : 8.167,
                'o' : 7.507,
                'i' : 6.966,
                'n' : 6.749,
                's' : 6.327,
                'h' : 6.094,
                'r' : 5.987,
                'd' : 4.253,
                'l' : 4.025,
                'c' : 2.782,
                'u' : 2.758,
                'm' : 2.406,
                'w' : 2.360,
                'f' : 2.228,
                'g' : 2.015,
                'y' : 1.974,
                'p' : 1.929,
                'b' : 1.492,
                'v' : 0.978,
                'k' : 0.772,
                'j' : 0.153,
                'x' : 0.150,
                'q' : 0.095,
                'z' : 0.074
                }

###################
#     FUNCTIONS   #
###################
# Method: Writes the encrypted string and the key to a file
# Param: string : encrypted string,
#        key : encrypting key,
#        filepath (optional) : path to where text will be saved
# Returns: Nothing
def write_to_file(string, key, filepath = './substitution_ciphers.txt'):
    # Either Creates file, Writes to an emtpy file, or Appends to a file
    if os.path.isfile(filepath):
        target = open(filepath, 'a')
        if os.stat('./substitution_ciphers.txt').st_size != 0:
            target.write('\n')
    else:
        target = open(filepath, 'w')
    target.truncate()
    target.write(string + ":" + key)
    target.close()

# Method: Takes the raw string and creates an encrypted string as well as writes to a file
# Param: raw : Plain text
#        key : encrypting key
# Returns: Encrypted String
def encrypt(raw, key):
    #Variables
    local_dic = copy.deepcopy(key_dic)
    encrypt_string = ''

    # Populate key_dic with key values
    if(len(key) == 26):
        for dic_key, dic_value in local_dic.items():
                local_dic[dic_key] = key[int(dic_value)]

    # Creates the encrypted string
    for raw_char in raw:
        if raw_char.isalpha():
            encrypt_string += local_dic[raw_char.lower()]
        else:
            encrypt_string += raw_char


    # Calls method to write encrypted string with the key in format:
    # encrypt_string:key
    write_to_file(encrypt_string, key)

    # Returns the encrypted string
    return encrypt_string

# Method: Takes a file and decrypts the entire file with the encrypted string:key format
# Param: filename : the path to the file with the encrypted string
# Returns: Array of decrypted Messages
def decrypt_by_file(filepath):
    # Variables
    my_messages = []

    # Opens File that has encrypted string
    with open(filepath) as f:
        for line in f:
            line_stripped = line.rstrip()
            encrypted, key = line_stripped.split(':')
            my_messages.append(decrypt(encrypted, key))

# Method: Takes the encrypted string and the key to return the decrypted string
# Param: encrypted : the encrypted string
#        key : encrypting key
# Returns: Decrypted String
def decrypt(encrypted, key):
    # Variables
    local_dic = copy.deepcopy(key_dic)
    decrypt_string = ''

    # Populates the key_dic with key values
    if(len(key) == 26):
        for dic_key, dic_value in local_dic.items():
            local_dic[dic_key] = key[int(dic_value)]

    # Creates the decrypted string
    for encrypt_char in encrypted:
        if encrypt_char.isalpha():
            for dic_key, dic_value in local_dic.items():
                if dic_value == encrypt_char:
                    decrypt_string += dic_key
                    break
        else:
            decrypt_string += encrypt_char

    # Returns the decrypted string
    return decrypt_string

# Method: Returns a random order alphabet key
# Param: NONE
# Returns: Key String
def gen_key():
    alpha = list(alphabet)
    random.shuffle(alpha)
    return ''.join(alpha)

###################
#       MAIN      #
###################
