import copy

TEST1 = """
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""

class Combat:
	def __init__(self, decktext):
		decks = decktext.split('\n\n')
		self.decks = {}
		for deck in decks:
			name, cardtext = deck.split(':')
			cards = list(map(int, filter(None, cardtext.split('\n'))))
			self.decks[name.strip()] = cards

		self.players = list(self.decks.keys())
		print(self.decks)

		self.winner = None

	def play(self):
		while all((any(d) for d in self.decks.values())):
			cards = [self.decks[player].pop(0) for player in self.players]
			index = cards.index(max(cards))
			roundwinner = self.players[index]
			self.decks[roundwinner].extend(sorted(cards, reverse=True))
			# print(self.decks)

		return roundwinner

	def play_recursive(self):
		# rounds = [d for d in self.decks.values()]

		def play_round(decks, sub=0):
			rounds = {}
			# print(sub, decks)
			while all((any(d) for d in decks.values())):
				# rounddecks = copy.deepcopy(list(decks.values()))
				rounddecks = ''.join(map(str, decks['Player 1'])) + '|' + ''.join(map(str, decks['Player 2']))
				if rounddecks in rounds:
					# print(rounddecks)
					# raise Exception()
					return 'Player 1'

				rounds[rounddecks] = None

				card1 = decks['Player 1'].pop(0)
				card2 = decks['Player 2'].pop(0)

				size1 = len(decks['Player 1'])
				size2 = len(decks['Player 2'])
				if size1 >= card1 and size2 >= card2:
					# recurse
					newdecks = copy.deepcopy(decks)
					newdecks['Player 1'] = newdecks['Player 1'][:card1]
					newdecks['Player 2'] = newdecks['Player 2'][:card2]
					winner = play_round(copy.deepcopy(newdecks), sub=sub+1)
				else:
					winner = 'Player 1' if card1 > card2 else 'Player 2'

				if winner == 'Player 1':
					wincards = [card1,card2]
				else:
					wincards = [card2,card1]
				decks[winner].extend(wincards)

				# print(sub, decks)

			return winner

		decks = copy.deepcopy(self.decks)
		# try:
		winner = play_round(decks)
		# except:
		# 	winner = 'Player 1'
		cards = decks[winner]
		return sum((card * (len(cards) - i) for i, card in enumerate(cards)))

	def score(self, player):
		cards = self.decks[player]
		return sum((card * (len(cards) - i) for i, card in enumerate(cards)))


TEST2  = """
Player 1:
43
19

Player 2:
2
29
14
"""

if __name__ == '__main__':
	INPUT = open('input22.txt').read()
	# INPUT = TEST1
	# INPUT = TEST2
	g = Combat(INPUT)
	winner = g.play()
	print('Part 1:', g.score(winner))

	g = Combat(INPUT)
	print('Part 2:', g.play_recursive())
	# not 8271