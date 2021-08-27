boggleome
=========

An advanced algorithmic challenge.

## Boggle ##

Boggle is a word game where you connect letters to create words. Whoever finds 
the most unique words in the time limit wins.

1. The board is 4x4 in size
2. Letters must be adjacent to each other
3. You cannot reuse the same position twice
4. The word must be at least 3 letters long and in the dictionary

## Setup ##

1. You need a dictionary (e.g. https://github.com/dolph/dictionary)
2. You need to decide on board size (4x4 by default, but what not 5x5?)
3. You need to decide on minimum word length (3 by default, but maybe more?)

## Challenge 1: Solving Boggle ##

Making a boggle solver is a little complicated because you have to try many 
paths on the board and keep checking them against a dictionary. You can do it 
in your mind easily enough, but writing the algorithm takes a little work.

## Challenge 2: Solving Maximum Words ##

Find the Boggle board with the most words. That is, what combination of 4x4 
letters (or whatever) has the most words embedded in it?
