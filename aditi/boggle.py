import argparse
import string
import random

parser = argparse.ArgumentParser(description="Play Boggle")
parser.add_argument("--file", required=True, type=str, metavar='<path>')
parser.add_argument("--dim", required=False, type=int, default=4, metavar='<int>')
parser.add_argument("--size", required=False, type=int, default=3, metavar='<int>')

arg=parser.parse_args()

#making the board
dim=arg.dim
size=arg.size
board=[]
for i in range(dim):
    temp=[None]*dim
    board.append(temp)

#fill the board (equal probability of each letter, NOT USED )
'''
for i in range(len(board)):
    for j in range(len(board[i])):
        board[i][j]=random.choice(string.ascii_lowercase)
'''

#fill the board (scrabble frequencies)
letters="a"*9 + "b"*2 + "c"*2 + "d"*4 + "e"*12 + "f"*2 + "g"*3 + "h"*2 + "i"*9 + "jk" + "l"*4 +"m"*2 + "n"*6 + "o"*8 + "p"*2 + "q" + "r"*6 + "s"*4 + "t"*6 + "u"*4 + "v"*2 +  "w"*2 + "x" +   "y"*2 + "z"

board_letters=""
for i in range(len(board)):
    for j in range(len(board[i])):
        board[i][j]=random.choice(letters)
        board_letters+=board[i][j]

board_letters=''.join(set(board_letters))

#printer
def printer(m):
    for i in range(len(m)):
        print(m[i])


printer(board)



#shrinking the dictionary
mydict=[]

fp = open(arg.file)

for word in fp.readlines(): #for word in set of word
    word = word.rstrip() 		#format the word so it is readable
    if len(word) < size:
        continue #takes you back to 'if word is right size'
    else: #meaning word is a valid size
        mydict.append(word) #add the word to my list
        for char in word: 
            if char not in board_letters: #if there is any letter in the word not in board letters
                mydict.pop() #remove the word cause it wasn't valid
                break #break out of this, want to reset COMPLETELY, move onto next word
               
fp.close()

#finding the words
for row in range(len(board)):
    for col in range(len(board[row])):
        char=board[row][col]
        sorted = [x for x in mydict if x.startswith(char)] #subset the dictionary to contain words that start with the char letter

'''pseudocode
        for word in sorted:
            for char in word
                if char is present adjacent to the current coordinates (this one can be in a function)
                    return the coordinates of where the char is
                then change the coordinates to that location
                repeat check if next char is present adjacent to the current coordinates
                if we reach the last letter of word, add word to 'results'
'''

       
        
