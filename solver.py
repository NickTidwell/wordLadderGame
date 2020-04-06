import  csv
import random
import enchant
from _collections import  deque
viewedWord = dict()
d = enchant.Dict("en_US")

def printLadder(ladder):
    for i in range(0,len(ladder)-1):
        print(ladder[i], "-->", end='')
    print(ladder[-1])

def validWord(word):
    return d.check(word)

def swapChar(word, i , j):
    newWord = list(word)
    newWord[i] = chr(j)
    return ''.join(newWord)
def charOff(endWord, currentWord):
    charsOff = 0
    for i,let in enumerate(endWord):
        if(let != currentWord[i]):
            charsOff = charsOff + 1
    return charsOff

def generateOneOff(currentWord, maxOff,end):
    oneOff = set()
    for i,let in enumerate(currentWord):
        for j in range(97,123):
            newWord = swapChar(currentWord,i,j)
            currentCharOff = charOff(end, currentWord)
            if(currentCharOff < maxOff):
                maxOff = currentCharOff
            if(d.check(newWord) == True and viewedWord.get(newWord) == None) and currentCharOff <= maxOff and newWord != currentWord:
                oneOff.add(newWord)
    return oneOff

def reverseBFS(revTable,end):
    order = list()
    q = deque()
    q.append(end)
    currentWord = q.pop()
    while(revTable.get(currentWord) != None):
        order.append(currentWord)
        q.append(revTable[currentWord])
        currentWord = q.pop()
    order.append(currentWord)
    order = order[::-1]
    return order

def getWordPair():
    with open("sample_input.csv", "r+") as csvFile:
        data = list(csv.reader(csvFile))
        lines = len(data)
        wordPair = data[random.randrange(lines)]
        return wordPair

def getShortestSolution(begin, end):
    q = deque()
    q2 = deque()
    q.append(begin)
    maxOff = len(begin)
    table = dict()
    while(len(q) != 0):
        currentWord = q.pop()
        if(currentWord == end):
            break

        for genWord in generateOneOff(currentWord, maxOff,end):
            q2.append(genWord)
            table[genWord] = currentWord
        viewedWord[currentWord] = genWord

        if(len(q) == 0):
            q = q2
            q2 = deque()
            maxOff = maxOff -1
    solution = reverseBFS(table,end)
    return solution

