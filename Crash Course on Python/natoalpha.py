# Here I practice using dictionary
# this function take a word input, and prints the nato alphabet words
# Used for loops, sys module/arguments , function, dictionary, if statements.


import sys

natoalpha = {"A" : "Alpha",
"B" : "Bravo",
"C" : "Charlie",
"D" : "Delta",
"E" : "Echo",
"F" : "Foxtrot",
"G" : "Golf",
"H" : "Hotel",
"I" : "India",
"J" : "Juliett",
"K" : "Kilo",
"L" : "Lima",
"M" : "Mike",
"N" : "November",
"O" : "Oscar",
"P" : "Papa",
"Q" : "Quebec",
"R" : "Romeo",
"S" : "Sierra",
"T" : "Tango",
"U" : "Uniform",
"V" : "Victor",
"W" : "Whiskey",
"X" : "X-ray",
"Y" : "Yankee",
"Z" : "Zulu"
             }


def nato(given_word):
    for letter in given_word:
        if letter.upper() in natoalpha:
            print("{} : {}".format(letter.upper(),natoalpha[letter.upper()]))
        else:
            print(letter.upper())
    sys.exit(0)

given_word = sys.argv[1]
nato(given_word)


'''
example outputs:
PS C:\Users\atmakl\PycharmProjects\Googlecourse\venv\Scripts> python .\Natoalpha.py Henry
H : Hotel
E : Echo
N : November
R : Romeo
Y : Yankee
PS C:\Users\atmakl\PycharmProjects\Googlecourse\venv\Scripts> python .\Natoalpha.py raju
R : Romeo
A : Alpha
J : Juliett
U : Uniform
PS C:\Users\atmakl\PycharmProjects\Googlecourse\venv\Scripts> python .\Natoalpha.py jade
J : Juliett
A : Alpha
D : Delta
E : Echo
PS C:\Users\atmakl\PycharmProjects\Googlecourse\venv\Scripts>
'''
