#!/bin/python
# -*- coding: utf-8 -*-

#############################################################################
###                                                                       ###
###  Description: PlayFair Cipher Algorithm, takes a 25 character (5x5)   ###
###               key that is generated with a phrase. Then encrypts      ###
###               / decrypts the message using the rules and the key      ###
#############################################################################

__author__  = "Tyler Hall"
__copyright__ = "Copyright 2017"

###################
#     IMPORTS     #
###################

###################
#      GLOBAL     #
###################

ALPHABET = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
"""

Please note there is no J as it is translated as an I

"""

###################
#    FUNCTIONS    #
###################

# Method : Generates the table from the key phrase
# Param : key: string (phrase) used to create table
# Returns : Array table
def gen_key(key):
    # Variables
    x = 0
    y = 0
    cipher_table = {}

    # Use key
    for char in key.upper():
        if char == 'J':
            char = 'I'
        if char not in cipher_table.keys():
            cipher_table[char] = (x,y)
            if y == 4:
                y = 0
                x += 1
            else:
                y += 1

    #Fill in the rest of the table
    if x < 5:
        for char in ALPHABET:
            if char not in cipher_table.keys():
                cipher_table[char] = (x,y)
                if y == 4:
                    y = 0
                    x += 1
                else:
                    y += 1
                if x == 5:
                    break
    return cipher_table

# Method : Encryption Method
# Param : message: plaintext
#         dicKey: Key used to encrypt/decrypt the text
# Returns : returns cipherText
def encrypt(message, dictKey):
    cipherText = ''
    diagramList = breakMessage(message)
    print "diagramList : ", diagramList
    for coupling in diagramList:
        cipherText += encrypt_rules(coupling,dictKey)
    return cipherText

# Method : Decryption Method
# Param : cipherText: encrypted message
#         dicKey: Key used to encrypt/decrypt the text
# Returns : returns plain text
def decrypt(cipherText, dictKey):
    plainText = ''
    diagramList = breakMessage(cipherText)
    for coupling in diagramList:
        plainText += decrypt_rules(coupling,dictKey)
    return plainText

# Method : Breaks the plain text into diagrams (couples of two)
# Param : plainText: OG message
# Returns : returns sets of the grouped characters
def breakMessage(plainText):
    diagram = []
    plainText = ''.join(plainText.split())
    plainText = plainText.upper()

    for x in range(0,len(plainText),2):
        if (x+1) != len(plainText):
            if (plainText[x]!=plainText[x+1]):
                diagram.append(plainText[x]+plainText[x+1])
            else:
                diagram.append(plainText[x]+"X")
        else:
            diagram.append(plainText[x]+"X")
    return diagram

# Method : Rules for encrypting the coupling of the characters
# Param : coupling: Two characters that where put together
#         dicKey: Key used to encrypt/decrypt the text
# Returns : returns sets of the encrypted coupling
def encrypt_rules(coupling, dictKey):
    rowArray = []
    colArray = []
    row,col = -1, -1
    finalValue = ''
    for char in coupling:
        if char != 'J':
            row, col = dictKey[char]
            rowArray.append(row)
            colArray.append(col)
        else:
            char = 'I'
            row, col = dictKey[char]
            rowArray.append(row)
            colArray.append(col)

    if(rowArray[0] == rowArray[1]):
        for index in range(len(rowArray)):
            if (colArray[index]+1 <= 3):
                currentValue = (rowArray[index],colArray[index]+1)
            else:
                currentValue = (rowArray[index],0)
            for key, value in dictKey.items():
                if currentValue == value:
                    finalValue += key
        return finalValue
    elif(colArray[0] == colArray[1]):
        for index in range(len(rowArray)):
            if (rowArray[index]+1 <= 3):
                currentValue = (rowArray[index]+1,colArray[index])
            else:
                currentValue = (0,colArray[index])
            for key, value in dictKey.items():
                if currentValue == value:
                    finalValue += key
        return finalValue
    else:
        for index in range(len(rowArray)):
            if (index == 0):
                currentValue = (rowArray[index],colArray[1])
            else:
                currentValue = (rowArray[index],colArray[0])
            for key, value in dictKey.items():
                if currentValue == value:
                    finalValue += key
        return finalValue

# Method : Rules for decrypting the coupling of the characters
# Param : coupling: Two characters that where put together
#         dicKey: Key used to encrypt/decrypt the text
# Returns : returns sets of the decrypted coupling
def decrypt_rules(coupling, dictKey):
    rowArray = []
    colArray = []
    row,col = -1, -1
    finalValue = ''
    for char in coupling:
        row, col = dictKey[char]
        rowArray.append(row)
        colArray.append(col)

    if(rowArray[0] == rowArray[1]):
        for index in range(len(rowArray)):
            if (colArray[index]-1 >= 0):
                currentValue = (rowArray[index],colArray[index]-1)
            else:
                currentValue = (rowArray[index],3)
            for key, value in dictKey.items():
                if currentValue == value:
                    finalValue += key
        return finalValue
    elif(colArray[0] == colArray[1]):
        for index in range(len(rowArray)):
            if (rowArray[index]-1 >= 0):
                currentValue = (rowArray[index]-1,colArray[index])
            else:
                currentValue = (3,colArray[index])
            for key, value in dictKey.items():
                if currentValue == value:
                    finalValue += key
        return finalValue
    else:
        for index in range(len(rowArray)):
            if (index == 0):
                currentValue = (rowArray[index],colArray[1])
            else:
                currentValue = (rowArray[index],colArray[0])
            for key, value in dictKey.items():
                if currentValue == value:
                    finalValue += key
        return finalValue
