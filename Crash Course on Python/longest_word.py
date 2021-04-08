#! /usr/env/bin python3

def longer_word(word1, word2, word3):
    wordlist = [word1, word2, word3]
    sorted_wordlist = sorted(wordlist, key=len)
    longer_word = sorted_wordlist[-1]
    return 'Longest word in the given words is : {}'.format(longer_word)

print(longer_word('w13','w2','w333'))
print(longer_word("bed", "bath", "beyond"))
print(longer_word("laptop", "notebook", "desktop"))

example output:
===============
Scripts/test.py
Longest word in the given words is : w333
Longest word in the given words is : beyond
Longest word in the given words is : notebook
