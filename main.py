import solver as solver

wordPair = solver.getWordPair()
begin = wordPair[0].strip()
end = wordPair[1].strip()

print("Welcome to the Doublet Game!")
print("Today's word pair is: {begin} -> {end}".format( begin =begin, end =end))
print("Please enter word chain (not including the start and end words.")
print("Enter 'q' when you're done.")

currentWord = input()
wordLength = len(begin)
wordLadder = [begin]
while(currentWord != 'q'):
    wordLadder.append(currentWord)
    currentWord = input()
wordLadder.append(end)

prevWord = begin
valid = True
for word in wordLadder:
    if not solver.validWord(word):
        print("'{currentWord}' is not a word in the dictionary. You Lose!".format(currentWord=currentWord))
        valid = False
        break
    charsOff = solver.charOff(prevWord,word)
    if(charsOff > 1):
        print("You have violated the one letter change constraint. You Lose!")
        valid = False
        break
    if(len(word) != wordLength):
        print("Word must be of length {wordLength}. You Lose".format(wordLength=wordLength))
        valid = False
        break
    prevWord = word

if(valid):
    print("Valid Solution")
    shortestLadder = solver.getShortestSolution(begin,end)
    if(len(wordLadder) > len(shortestLadder)):
        print("Not the shortest solution")
        solver.printLadder(shortestLadder)
    else:
        print("This is the shortest solution, You win!")