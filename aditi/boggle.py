import argparse
import string
import random

parser = argparse.ArgumentParser(description="Play Boggle")
parser.add_argument("--file", required=True, type=str, metavar='<path>')
parser.add_argument("--dim", required=False, type=int, default=3, metavar='<int>')
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
letters="a"*9 + "b"*2 + "c"*2 + "d"*4 + "e"*12 + "f"*2 + "g"*3 + "h"*2 + "i"*9 + "jk" + "l"*4 +"m"*2 + "n"*6 + "o"*8 + "p"*2 + "q" + "r"*6 + "s"*4 + "t"*6 + "u"*4 + "v"*2 +  "w"*2 + "x" + "y"*2 + "z"

board_letters=""
for i in range(len(board)):
    for j in range(len(board[i])):
        board[i][j]=random.choice(letters)
        board_letters+=board[i][j]

#get unique letters only
board_letters=''.join(set(board_letters))

#printer
def printer(m):
    for i in range(len(m)):
        print(m[i])



#for debugging
board_letters="abcde"
board=[["a", "a", "b"],
["c", "d", "e"],
["a", "b", "c"],
["a", "b", "c"]
]
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


results=[]

#finding the neighbors at position i, j
def scan(m, i, j):
    n_row=len(m)
    n_col=len(m[0])

    '''
    t=top cell (value to the Top of char)
    l=left
    r=right
    b=bottom

    d: for diagonal
    1-4: for cartesian grid coordinate
    ex: d1 is the upper right, d3 is lower left
    '''

    if i==0: #first row
        if j==0: #first col
            #top left corner
            #print("tl")
            r=m[i][j+1]
            b=m[i+1][j]
            d4=m[i+1][j+1]

            mylist=(
                    #["t",  t,  i-1, j],
                    #["l",  l,  i,   j-1],
                    ["r",  r,  i,   j+1],
                    ["b",  b,  i+1, j],
                    #["d1", d1, i-1, j+1],
                    #["d2", d2, i-1, j-1],
                    #["d3", d3, i+1, j-1],
                    ["d4", d4, i+1, j+1]                        
                    )
            return mylist

        elif j==(n_col-1):
            #top right corner
            #print("tr")
            l=m[i][j-1]
            b=m[i+1][j]
            d3=m[i+1][j-1]

            mylist=(
                    #["t",  t,  i-1, j],
                    ["l",  l,  i,   j-1],
                    #["r",  r,  i,   j+1],
                    ["b",  b,  i+1, j],
                    #["d1", d1, i-1, j+1],
                    #["d2", d2, i-1, j-1],
                    ["d3", d3, i+1, j-1]
                    #["d4", d4, i+1, j+1]                        
                    )
            return mylist

        else:
            #all other top row values
            #print("trow")
            l=m[i][j-1]
            r=m[i][j+1]
            b=m[i+1][j]
            d3=m[i+1][j-1]
            d4=m[i+1][j+1]

            mylist=(
                    #["t",  t,  i-1, j],
                    ["l",  l,  i,   j-1],
                    ["r",  r,  i,   j+1],
                    ["b",  b,  i+1, j],
                    #["d1", d1, i-1, j+1],
                    #["d2", d2, i-1, j-1],
                    ["d3", d3, i+1, j-1],
                    ["d4", d4, i+1, j+1]                        
                    )
            return mylist

    elif i==(n_row-1): #this is the last row of the matrix
        if j==(n_col-1): #this is the last col of the matrix
            #bottom right corner
            #print("br")
            t=m[i-1][j]
            l=m[i][j-1]
            d2=m[i-1][j-1]

            mylist=(
                    ["t",  t,  i-1, j],
                    ["l",  l,  i,   j-1],
                    #["r",  r,  i,   j+1],
                    #["b",  b,  i+1, j],
                    #["d1", d1, i-1, j+1],
                    ["d2", d2, i-1, j-1]
                    #["d3", d3, i+1, j-1],
                    #["d4", d4, i+1, j+1]                        
                    )
            return mylist

        elif j==0:
            #bottom left corner
            #print("bl")
            t=m[i-1][j]
            r=m[i][j+1]
            d1=m[i-1][j+1]

            mylist=(
                    ["t",  t,  i-1, j],
                    #["l",  l,  i,   j-1],
                    ["r",  r,  i,   j+1],
                    #["b",  b,  i+1, j],
                    ["d1", d1, i-1, j+1]
                    #["d2", d2, i-1, j-1],
                    #["d3", d3, i+1, j-1],
                    #["d4", d4, i+1, j+1]                        
                    )
            return mylist

        else:
            #all other bottom row values
            #print("brow")
            t=m[i-1][j]
            l=m[i][j-1]
            r=m[i][j+1]
            d1=m[i-1][j+1]
            d2=m[i-1][j-1]

            mylist=(
                    ["t",  t,  i-1, j],
                    ["l",  l,  i,   j-1],
                    ["r",  r,  i,   j+1],
                    #["b",  b,  i+1, j],
                    ["d1", d1, i-1, j+1],
                    ["d2", d2, i-1, j-1]
                    #["d3", d3, i+1, j-1],
                    #["d4", d4, i+1, j+1]                        
                    )
            return mylist

    else: #all middle rows
        if j==0:
            #first column values
            #print("col1")
            t=m[i-1][j] 
            r=m[i][j+1]
            d1=m[i-1][j+1]
            d4=m[i+1][j+1]
            b=m[i+1][j]

            mylist=(
                ["t",  t,  i-1, j],
                #["l",  l,  i,   j-1],
                ["r",  r,  i,   j+1],
                ["b",  b,  i+1, j],
                ["d1", d1, i-1, j+1],
                #["d2", d2, i-1, j-1],
                #["d3", d3, i+1, j-1],
                ["d4", d4, i+1, j+1]                        
                )
            return mylist

        elif j==(n_col-1):
            #last column values
            #print("lastcol")
            t=m[i-1][j] 
            l=m[i][j-1]
            d2=m[i-1][j-1]
            d3=m[i+1][j-1]
            b=m[i+1][j]

            mylist=(
                ["t",  t,  i-1, j],
                ["l",  l,  i,   j-1],
                #["r",  r,  i,   j+1],
                ["b",  b,  i+1, j],
                #["d1", d1, i-1, j+1],
                ["d2", d2, i-1, j-1],
                ["d3", d3, i+1, j-1]
                #["d4", d4, i+1, j+1]                        
                )
            return mylist

        else:
            #all middle values
            t=m[i-1][j] 
            l=m[i][j-1]
            r=m[i][j+1]
            b=m[i+1][j]
            d1=m[i-1][j+1]
            d2=m[i-1][j-1]
            d3=m[i+1][j-1]
            d4=m[i+1][j+1]
            

            mylist=(
                    ["t",  t,  i-1, j],
                    ["l",  l,  i,   j-1],
                    ["r",  r,  i,   j+1],
                    ["b",  b,  i+1, j],
                    ["d1", d1, i-1, j+1],
                    ["d2", d2, i-1, j-1],
                    ["d3", d3, i+1, j-1],
                    ["d4", d4, i+1, j+1]                        
                    )
            return mylist


def match_finder(m, d, d_index, w_index, i, j, coords):
    while d_index<len(d):
        word=d[d_index] 
        # if len(coords)==0:
        #     coords.append([i, j]) 
        
        if word in results:
            d_index+=1 #we really don't need to query for this word again, let's move on
            coords=[] #wipe coordinates clean
            continue

        print(d_index, word, w_index)
        if w_index <len(word):
            next_let=word[w_index] 
                    
            neighbors=scan(m, i, j) 

            matches=0
            counter=0
            for option in neighbors:
                counter+=1
                #print(counter, option)
                
                if next_let==option[1]: #if a==a
                    if option[2:4] not in coords: #if a's coordinates have not already been used
                        coords.append(option[2:4]) #save the coordinates that we are using
                        matches+=1
                        w_index+=1 #goes up by 1 because you want to search for the next letter)
                        print("option", counter, "of", len(neighbors), "was good, recursing at", option[2:4], " new letter index is ", w_index)
                       


                        #need some way to remember to come back to this branch point!




                        match_finder(m, d,
                        d_index, #stays the same as before because you want to check the same word
                        w_index,
                        option[2],
                        option[3],
                        coords)
                   
                    else:
                        print("this path requires repeat coordinate, trying different option")
                        continue

            if matches==0: #if you went through all the immediate options and none of them worked
                #the whole word is useless, we can move on
                print(word, "was bad, tried", counter,"neighbors moving on")
                d_index+=1 #time for a new word
                coords=[] #reset all coordinates
                w_index=1
                
                continue
                # match_finder(m, d, 
                # d_index, #goes up by one cause now we do want a new word
                # 1, #w_index resets to i=1, making it the second letter
                # i, #stays the same because we still want to use the same starting letter, but different word in sorted dict
                # j,
                # coords)

        else:
            #now we found a word. horray! we need to reset everything and repeat
            print("found one, ending at", i, j, "word is", word)
            results.append(word)
            d_index+=1 #moves to next word in the dictionary
            coords=[]#reset all coordinates
           
            match_finder(m, d, 
            d_index, 
            1, #w_index resets to i=1, making it the second letter
            i, #stays the same because we still want to use the same starting letter, but different word in sorted dict
            j,#stays the same because we still want to use the same starting letter, but different word in sorted dict)
            coords)
        break



#finding the words
for row in range(len(board)):
    for col in range(len(board[row])):
        char=board[row][col]
        sorted=[x for x in mydict if x.startswith(char)] #subset the dictionary to contain words that start with the char letter
        used=[]
        print(char, ": ", sorted[0:3])

        match_finder(board, #m
        sorted[0:3], #d
        0, #d_index
        1, #w_index
        row, #i
        col, #j
        used) #coords

       
        
