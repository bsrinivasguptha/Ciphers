#!/bin/python
# -*- coding: utf-8 -*-

######################################################################
###                                                                ###
###  Description: Uses the RSA encryption method to encrypt        ###
###               and decrypt data.                                ###
###                                                                ###
######################################################################

__author__  = "Tyler Hall"
__copyright__ = "Copyright 2017"

###################
#     IMPORTS     #
###################

import random
import rabinMiller

###################
#      GLOBAL     #
###################

###################
#    FUNCTIONS    #
###################

# Desc : Greatest Common Denominator
# Param : a : number
#         b : number
#Returns : Greatest Common Denominator
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

# Desc : Finds and returns two 2048 bit prime numbers
# Param : NONE
#Returns : p , q (Two prime 2048 bit numbers)
def twoPrimes():
    p = rabinMiller.generateLargePrime()
    q = rabinMiller.generateLargePrime()
    return p, q

# Desc : Finds the value for d that fits in the equation e*d = 1 mod phi
# Param : e : e value
#         phi : phi value
#Returns : the d value
def inverse(e,phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2- temp1* x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi

# Desc : produces the Public and Private key pairs
# Param : p : 2048 bit prime number
#         q : 2048 bit prime number
#Returns : (e,n),(d,n) returns the Public Key and the Private Key (e,n),(d,n)
def keyPair(p,q):
    # Variables
    e,phi,d = 0, 0, 0

    #n
    n = p * q
    #phi
    phi = (p-1)*(q-1)
    #e
    e = random.randint(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randint(1, phi)
        g = gcd(e, phi)
    #d
    d = inverse(e, phi)

    return ((e,n), (d,n))

# Desc : Encrypts the plain Text with the public key
# Param : plainText : Message you would like to encrypt
#         pubKey : Public Key
#Returns : the Cipher Text
def encrypt(plainText, pubKey):
    # Variables
    position = len(plainText) - 1
    cipherText = 0
    e, n = pubKey

    for i in range(len(plainText)):
        asciiChar = ord(plainText[i])
        asciiChar = asciiChar * pow(256, position)
        position -= 1
        cipherText += asciiChar

    cipherText = pow(cipherText, e, n)
    return cipherText

# Desc : Takes the cipher Text and decrypts using the Private Key
# Param : cipher: Encrypted message
#         privKey: Private Key
#Returns : returns the plain text message
def decrypt(cipher, privKey):
    #Variables
    charList = {}
    position = 0
    loop = 0
    plainText,decrypted = '', ''
    d, n = privKey

    cipherText= pow(cipher,d,n)

    decrypted = int(cipherText)
    while  decrypted > 0:
        asciiChar = decrypted % 256
        if asciiChar == 0:
            asciiChar = decrypted
            while asciiChar > 256:
                asciiChar = asciiChar / 256
                loop += 1
            charList[loop] = chr(asciiChar)
            decrypted -= asciiChar * pow(256, loop)
            loop = 0
        else:
            charList[position] = chr(asciiChar)
            decrypted -= asciiChar * pow(256, position)
            position += 1

    for index, value in sorted(charList.items(), reverse=True):
        plainText += charList[index]

    return plainText

###################
#     EX MAIN     #
###################
#Uncomment to see the example of code use
"""
#produce two primes
p, q = twoPrimes()
#get the keys
pubKey, privKey = keyPair(p,q)
#encrypt the plaintext
encrypted = encrypt('TEST message FOR testing PURPOSES', pubKey)
print encrypted
#decrypt the cipher text
decrypted = decrypt(encrypted, privKey)
print decrypted
"""
