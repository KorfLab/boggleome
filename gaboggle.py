import argparse
import random
import unboggle

def fitness(d, b):
	words = list(unboggle.solve_board(b, d, arg.min))
	return len(words)

def mate(d, p1, p2, mut):
	size = len(p1['gen'])
	child = {'gen': unboggle.new_board(size), 'fit': None}
	
	# recombination
	for i in range(size):
		for j in range(size):
			if random.random() < 0.5:
				child['gen'][i][j] = p1['gen'][i][j]
			else:
				child['gen'][i][j] = p2['gen'][i][j]

	# mutation
	for i in range(size):
		for j in range(size):
			if random.random() < mut:
				child['gen'][i][j] = unboggle.random_letter()

	# finalization
	child['fit'] = fitness(d, child['gen'])
	
	return child

if __name__ == '__main__':
	
	parser = argparse.ArgumentParser(
		description='Boogle Board Breeder')
	parser.add_argument('dictionary', type=str, metavar='<file>',
		help='dictionary file')
	parser.add_argument('--min', required=False, type=int, default=3,
		metavar='<int>', help='minimum word length [%(default)i]')
	parser.add_argument('--size', required=False, type=int, default=4,
		metavar='<int>', help='board size [%(default)i]')
	parser.add_argument('--pop', required=False, type=int, default=100,
		metavar='<int>', help='population size [%(default)i]')
	parser.add_argument('--gen', required=False, type=int, default=100,
		metavar='<int>', help='generations [%(default)i]')
	parser.add_argument('--mut', required=False, type=float, default=0.1,
		metavar='<int>', help='mutation frequency [%(default).2f]')
	parser.add_argument('--seed', required=False, type=int,
		metavar='<int>', help='random seed')
	parser.add_argument('--verbose', action='store_true', help='show progress')
	parser.add_argument('--words', action='store_true', help='show all words')
	arg = parser.parse_args()
	
	# setup
	if arg.seed: random.seed(arg.seed)
	d = unboggle.read_into_tree(arg.dictionary)
	
	# create initial population
	pop = []
	for i in range(arg.pop):
		pop.append({'gen': unboggle.random_board(arg.size), 'fit': None})
	for ind in pop:
		ind['fit'] = fitness(d, ind['gen'])
	
	# evolve
	half = arg.pop // 2
	for g in range(arg.gen):
		pop = sorted(pop, key=lambda item: item['fit'], reverse=True)
		if arg.verbose:
			print(f'generation: {g}, maximum words: {pop[0]["fit"]}')
		for i in range(half, len(pop)):
			p1 = random.randint(0, half)
			p2 = random.randint(0, half)
			pop[i] = mate(d, pop[p1], pop[p2], arg.mut)
	
	# report best board
	pop = sorted(pop, key=lambda item: item['fit'], reverse=True)
	unboggle.show_board(pop[0]['gen'])
	print('words:', pop[0]['fit'])
	if arg.words:
		for word in unboggle.solve_board(pop[0]['gen'], d, arg.min):
			print(word)
	
