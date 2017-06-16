#!/usr/bin/python

# Boggle solver
# Eric Jones
# First argument is the word list file
# Second argument is the minimum word length
# Subsequent arguments should be comma separated rows
# Example:
# boggle.py dictionary.txt 4 f,i,r,s,t s,e,c,o,n t,h,i,r,d f,o,u,r,t f,i,f,t,h


import sys
import re
with open(sys.argv[1]) as dictionaryfile:
	dictionary = set(word.strip().lower() for word in dictionaryfile)

board=[]
minlength=int(sys.argv[2])
for row in sys.argv[3:]:
	board.append(row.split(','))
print board



scores=[
0, #1
0, #2
1, #3
1, #4
2, #5
3, #6
5, #7
11 #8
]
pathlist=[]
wordlist=set()

def getword(array):
	word = ''
	for character in array:
		word += board[character[0]][character[1]]
	return word

def scoreword(word):
	length = min(len(word),8)
	return scores[length-1]

def buildlist(array, dictionary):
	word = getword(array)
	r = re.compile('^'+word+'.*')
	matchingwords = filter(r.match, dictionary)
	if len(matchingwords) !=0:
		if len(array) >= minlength:
			if word in matchingwords:
				wordlist.add(word)
		if len(matchingwords) > 1:
			x0=array[len(array)-1][0]
			y0=array[len(array)-1][1]
			for x in range(max(x0-1,0),min(x0+1,len(board)-1)+1):
				for y in range(max(y0-1,0),min(y0+1,len(board[x])-1)+1):
					if [x,y] not in array:
						buildlist(array + [[x,y]], matchingwords)

for x in range(len(board)):
	for y in range(len(board[x])):
		buildlist([[x,y]], dictionary)
score=0
for word in wordlist:
	wordscore=scoreword(word)
	score+=wordscore
	print word, wordscore
print 'Found '+str(len(wordlist))+' words'
print 'Score: '+str(score)+' points'