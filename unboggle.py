import argparse
import random

alph = 'aaaabcddeeeeeefghhhiiiijkllmnnnooopqrrrsssttttuvwxyz'

def read_into_tree(file):
	head = {}
	with open(file) as fp:
		for word in fp.readlines():
			word = word.lower()
			word = word.rstrip()
			d = head
			for i, let in enumerate(word):
				if let not in d: d[let] = {}
				if i == len(word) -1: d[let]['*'] = True # * means end of word
				d = d[let]
	return head

def word_in_dictionary(d, w):
	head = d
	for c in w:
		if c in head: head = head[c]
		else: return False
	if '*' in head: return True
	else:           return False

def word_extends(d, w):
	head = d
	for c in w:
		if c in head: head = head[c]
		else: return False
	if len(head) == 1 and '*' in head: return False
	return True

def new_board(s):
	board = []
	for i in range(s):
		row = ['.'] * s
		board.append(row)
	return board

def copy_board(b):
	new = new_board(len(b))
	for i in range(len(b)):
		for j in range(len(b)):
			new[i][j] = b[i][j]
	return new

def random_letter():
	return random.choice(alph)

def random_board(s):
	
	board = new_board(s)
	for i in range(s):
		for j in range(s):
			board[i][j] = random_letter()
	return board

def show_board(b):
	h = '-' * (len(b) + 2)
	print(h)
	for i in range(len(b)):
		print('|', end='')
		for j in range(len(b)):
			print(b[i][j], end='')
		print('|')
	print(h)

def solve_board(b, d, m):
	size = len(b)
	words = []
	for i in range(size):
		for j in range(size):
			path = new_board(size)
			path[i][j] = 1
			chain = b[i][j]
			if word_in_dictionary(d, chain):
				words.append(chain)
			find_words(b, d, i, j, path, chain, words)

	unique = {}
	for word in words:
		if len(word) < m: continue
		unique[word] = True
	for word in sorted(unique): yield word

def find_words(b, d, x0, y0, path, chain, words):
	size = len(b)
	move = ((0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1))
	for dx, dy in move:
		x = x0 + dx
		y = y0 + dy
		if x < 0 or x == size: continue
		if y < 0 or y == size: continue
		if path[x][y] != '.':  continue
		chain += b[x][y]
		if word_in_dictionary(d, chain):
			words.append(chain)
		if word_extends(d, chain):
			path2 = copy_board(path)
			find_words(b, d, x, y, path2, chain, words)

if __name__ == '__main__':
	
	parser = argparse.ArgumentParser(
		description='Demo Boogle Solver')
	parser.add_argument('dictionary', type=str, metavar='<file>',
		help='dictionary file')
	parser.add_argument('--min', required=False, type=int, default=3,
		metavar='<int>', help='minimum word length [%(default)i]')
	parser.add_argument('--size', required=False, type=int, default=4,
		metavar='<int>', help='board size [%(default)i]')
	parser.add_argument('--seed', required=False, type=int,
		metavar='<int>', help='random seed')
	arg = parser.parse_args()
	
	if arg.seed: random.seed(arg.seed)
	
	d = read_into_tree(arg.dictionary)
	
	for i in range(100):
		b = random_board(arg.size)
		show_board(b)
		for word in solve_board(b, d, arg.min):
			print(word)
		
