'''

@author: Rob Herley

'''
import itertools
from collections import OrderedDict

letterScore = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
               'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
               'x': 24, 'y': 25, 'z': 26}

def answer(names):
    names = sorted(names, reverse = True)
    nameScore = sortList(scoreList(names))
    return nameList(nameScore)

def nameScore(name):
    sum = 0
    for letter in name:
        sum += letterScore[letter]
    return sum

def scoreList(namelist):
    newList = []
    for name in namelist:
        newList += [[name, nameScore(name)]]
    return newList

def sortList(namescorelist):
    return sorted(namescorelist, key = lambda name: name[1], reverse = True)

def nameList(sortedlist):
    newlist = []
    for item in sortedlist:
        newlist += [item[0]]
    return newlist
