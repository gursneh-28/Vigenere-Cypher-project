import string

def textstrip(filename):
    '''This takes the file and converts it to a string with all the spaces and other
    special characters removed. What remains is only the lower case letters,
    retain only the lowercase letters!
    '''

def letter_distribution(s):
    '''Consider the string s which comprises of only lowercase letters. Count
    the number of occurrences of each letter and return a dictionary'''

def substitution_encrypt(s,d):
    '''encrypt the contents of s by using the dictionary d which comprises of
    the substitutions for the 26 letters. Return the resulting string'''

def substitution_decrypt(s,d):
    '''decrypt the contents of s by using the dictionary d which comprises of
    the substitutions for the 26 letters. Return the resulting string'''

def cryptanalyse_substitution(s):
    '''Given that the string s is given to us and it is known that it was
    encrypted using some substitution cipher, predict the d'''

def vigenere_encrypt(s,password):
    '''Encrypt the string s based on the password the vigenere cipher way and
    return the resulting string'''

def vigenere_decrypt(s,password):
    '''Decrypt the string s based on the password the vigenere cipher way and
    return the resulting string'''

def rotate_compare(s,r):
    '''This rotates the string s by r places and compares s(0) with s(r) and
    returns the proportion of collisions'''

def cryptanalyse_vigenere_afterlength(s,k):
    '''Given the string s which is known to be vigenere encrypted with a
    password of length k, find out what is the password'''

def cryptanalyse_vigenere_findlength(s):
    '''Given just the string s, find out the length of the password using which
    some text has resulted in the string s. We just need to return the number
    k'''

def cryptanalyse_vigenere(s):
    '''Given the string s cryptanalyse vigenere, output the password as well as
    the plaintext'''


