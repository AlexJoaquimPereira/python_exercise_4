#Day 40 - Exercise 4
#Coding and decoding a string
# if strlen() <= 3
#     Simply reverse the string
# else
#     Remove and append the first character to the end 
#     And then add a string of 3 random characters at both ends

import random
import string

#Reverses the string
def reverse (str1):
    return str1[::-1]

#Removes and appends the first character, then adds the random strings
def tripleEncrypt(str1):
    str1 = str1[1:] + str1[0] #Removes and appends

    #Following two steps generate lists of three random characters using 'random', then converts to string using '.join'
    tempstr1 = ''.join(random.choices(string.ascii_lowercase, k = 3)) 
    tempstr2 = ''.join(random.choices(string.ascii_lowercase, k = 3))
    str1 = tempstr1 + str1 + tempstr2
    return str1

#Undoes the work done by tripleEncrypt()
def tripleDecrypt(str1):
    str1 = str1[2:len(str1)-3:1] #slices the string to remove the random characters
    str1 = str1[len(str1)-1] + str1[1:len(str1)-1] #removes and appends the last character of the string to the first, returning a list
    str1 = ''.join(str1)
    return str1

def Coding():
    str1 = input("Enter the text to encrypt\n")
    str2 = ''
    for word in str1.split(): #str.split() iterates the string in words with reference to whitespaces
        if (len(word) <= 3):
            word = reverse(word)
        else:
            word = tripleEncrypt(word)
        str2 = str2 + word + ' '
    print("Your encrypted text is:", str2)
    pass

def Decoding():
    str1 = input("Enter the test to decrypt\n")
    str2 = ''
    for word in str1.split():
        if (len(word) <= 3):
            word = reverse(word)
        else:
            word = tripleDecrypt(word)
        str2 = str2 + word + ' '
    print("Your decrypted text is:", str2)
    pass

print(''' 
What would you like to do?
1. Coding
2. Decoding
''')

a = int(input())

match a:
    case 1:
        Coding()
    case 2:
        Decoding()
    case _:
        print("Invalid input")