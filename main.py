#!/usr/bin/env python3


import numpy as np
import random

from connect4 import ConnectFourEnv


def seed(seed):
    random.seed(seed)
    np.random.seed(seed)


def main():
	seed(1234)
	env = ConnectFourEnv()
	
	env.reset()

	print(env.display_board())

	temp_board = np.zeros((6,7))
	temp_board[0,5] = 1
	temp_board[1,5] = 1
	temp_board[2,5] = 1



	env.load_game_board(temp_board)

	print(env.display_board())

	next_state, reward, done, _  = env.step(5,2)

	print(reward)
	print(env.display_board())




if __name__ == "__main__":
	main()