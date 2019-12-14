import cv2
import numpy as np
import queue
import logging
import copy
import pickle

from intcode import *

GAME_SIZE = 40
GAME_SHAPE = (GAME_SIZE, GAME_SIZE)
BLOCK_SIZE = 10
BLOCK_SHAPE = (BLOCK_SIZE, BLOCK_SIZE)

EMPTY = np.zeros(BLOCK_SHAPE, dtype=np.uint8)
WALL = np.ones(BLOCK_SHAPE, dtype=np.uint8) * 255
BLOCK = WALL.copy()
BLOCK[::2,::2] = 50
PADDLE = WALL.copy()
PADDLE[:BLOCK_SIZE//5,:] = 0
PADDLE[-BLOCK_SIZE//5:,:] = 0
BALL = WALL.copy()
BALL[np.sqrt(np.sum((np.indices(BLOCK_SHAPE) - BLOCK_SIZE / 2 -1) **2, axis=0)) > BLOCK_SIZE // 3] = 0

TILES = {
	0: EMPTY,
	1: WALL,
	2: BLOCK,
	3: PADDLE,
	4: BALL,
}

GAME = np.zeros((GAME_SIZE * BLOCK_SIZE, GAME_SIZE * BLOCK_SIZE), dtype=np.uint8)
GAME_LOGICAL = np.zeros(GAME_SHAPE, dtype=np.uint8)

def update_game(comp):
	while True:
		try:
			x, y, t = comp.get_output(), comp.get_output(), comp.get_output()

			if x == -1 and y == 0:
				print(f'\rScore: {t}', end='')
				continue

			GAME_LOGICAL[y,x] = t
			GAME[y*BLOCK_SIZE:y*BLOCK_SIZE+BLOCK_SIZE, x*BLOCK_SIZE:x*BLOCK_SIZE+BLOCK_SIZE] = TILES[t]
		
		except (OutputWait):
			break


if __name__ == '__main__':
	logging.basicConfig(level=logging.ERROR)
	game = [int(i) for i in open('input13.txt').read().split(',') if i.strip()]
	game[0] = 2
	comp = IntCodeComp(game)

	try:
		comp.process()
	except (InputWait):
		pass

	update_game(comp)

	x = np.max(np.any(GAME_LOGICAL != 0, axis=0) * np.indices((40,)))
	y = np.max(np.any(GAME_LOGICAL != 0, axis=1) * np.indices((40,)))
	GAME = GAME[:y*BLOCK_SIZE+BLOCK_SIZE,:x*BLOCK_SIZE+BLOCK_SIZE]
	GAME_LOGICAL = GAME_LOGICAL[:y,:x]

	states = []

	try:
		with open('game.pickle', 'rb') as g:
			state = pickle.load(g)
			comp = state[0]
			GAME = state[1]

	except Exception as e:
		print(e)

	while True:
		states.append((copy.deepcopy(comp), GAME.copy()))

		if len(states) > 30:
			states.pop(0)

		try:
			comp.process()
			break
		except (queue.Empty, InputWait):
			pass

		update_game(comp)

		cv2.imshow('', GAME)
		key = chr(cv2.waitKey(0))

		if key == 'a':
			comp.put_input(-1)

		elif key == 'd':
			comp.put_input(1)

		elif key == 'q':
			break

		elif key == 'o':
			c, g = states[0]
			comp = c
			GAME = g
			# try:
			# 	comp.put_input(0)
			# 	comp.process()
			# except:
			# 	pass
			# update_game(comp)
			# comp.put_input(0)
	
		else:
			comp.put_input(0)

	print()

	with open('game.pickle', 'wb') as g:
		pickle.dump(states[0], g)

	# dump the remaining output
	while True:
		print(comp.get_output())
	# print(np.sum(GAME_LOGICAL == 2))   # part 1


	# part 2
	# Score: 19210