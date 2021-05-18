#!/usr/bin/env python3


import numpy as np
import random

from connect4 import ConnectFourEnv
from Agents import RandomAgent

def seed(seed):
    random.seed(seed)
    np.random.seed(seed)


def main():
	seed(1234)
	turn = random.randint(0, 1) # to choose between players
	WIN = False

	env = ConnectFourEnv()
	agent = RandomAgent(env)
	env.reset()

	print(env.display_board())

	temp_board = np.zeros((6,7))
	temp_board[0,5] = piece1
	temp_board[1,5] = piece2
	temp_board[2,5] = piece1


	env.load_game_board(temp_board)

	print(env.display_board())
	while not WIN:
		if turn == 0:
			action = agent.take_action()
			next_state, reward, done, _  = env.step(action, piece1)
			turn += 1
			turn = turn % 2
			if done:
				print("Player 1 wins!!!")
				WIN=True
				break
		else:
			action = agent.take_action()
			next_state, reward, done, _  = env.step(action, piece2)
			turn += 1
			turn = turn % 2
			if done:
				print("Player 2 wins!!!")
				WIN=True
				break

	print(env.display_board())

if __name__ == "__main__":
	# initialize players
	piece1 = 1
	piece2 = 2

	player1 = 0
	player2 = 1

	main()