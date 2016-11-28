from collections import OrderedDict

def score(word):
    out = 0
    for letter in word:
        if letter in "eaionrtlsu": out += 1
        if letter in "dg":         out += 2
        if letter in "bcmp":       out += 3
        if letter in "fhvwy":      out += 4
        if letter == "k":          out += 5
        if letter in "jx":         out += 8
        if letter in "qz":         out += 10
    return out

def is_possible(letters, word):
    for letter in word:
        if letters.count(letter) < word.count(letter):
            return False
    return True

n = int(input())
dictionary = OrderedDict()
for i in range(n):
    w = input()
    dictionary[w] = score(w)


max_val = 0
letters = input()
for word in dictionary:
    if is_possible(letters, word):
        if dictionary[word] > max_val:
            max_val = dictionary[word]
            max_word = word
            
print(max_word)
