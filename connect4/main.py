#!/usr/bin/env python3


import numpy as np
import random

from connect4 import ConnectFourEnv
from connect4.Agents import RandomAgent
#from connect4_MCTS import run_MCTS
#from connect4_net import ConnectNet
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--iteration", type=int, default=0, help="Current iteration number to resume from")
parser.add_argument("--total_iterations", type=int, default=1000, help="Total number of iterations to run")
parser.add_argument("--MCTS_num_processes", type=int, default=5, help="Number of processes to run MCTS self-plays")
parser.add_argument("--num_games_per_MCTS_process", type=int, default=120, help="Number of games to simulate per MCTS self-play process")
parser.add_argument("--temperature_MCTS", type=float, default=1.1, help="Temperature for first 10 moves of each MCTS self-play")
parser.add_argument("--num_evaluator_games", type=int, default=100, help="No of games to play to evaluate neural nets")
parser.add_argument("--neural_net_name", type=str, default="cc4_current_net_", help="Name of neural net")
parser.add_argument("--batch_size", type=int, default=32, help="Training batch size")
parser.add_argument("--num_epochs", type=int, default=300, help="No of epochs")
parser.add_argument("--lr", type=float, default=0.001, help="learning rate")
parser.add_argument("--gradient_acc_steps", type=int, default=1, help="Number of steps of gradient accumulation")
parser.add_argument("--max_norm", type=float, default=1.0, help="Clipped gradient norm")
args = parser.parse_args()

def seed(seed):
    random.seed(seed)
    np.random.seed(seed)

def initialize_players():
	token1 = 1
	token2 = 2
	player1 = 0
	player2 = 1
	return token1, token2, player1, player2

def main():
	seed(1234)
	turn = random.randint(0, 1) # to choose between players
	WIN = False
	steps = 0
	movements = [] # to store player 1 and 2 actions for a round of game
	piece1, piece2, player1, player2 = initialize_players()

	env = ConnectFourEnv()
	agent = RandomAgent(env)
	env.reset()

	print(env.display_board())

	temp_board = np.zeros((6,7))
	temp_board[0,5] = piece1
	temp_board[1,5] = piece2
	temp_board[2,5] = piece1


	env.load_game_board(temp_board)

	curr_iteration = 0
	total_iterations = 100
	print(env.display_board())
	#for i in range(curr_iteration, total_iterations):
	#	run_MCTS(args, start_idx=0, iteration=i)


	while not WIN:
		steps+=1
		if turn == 0:
			action = agent.take_action()
			next_state, reward, done, _  = env.step(action, piece1)
			movements.append(action)
			turn += 1
			turn = turn % 2
			if done:
				print("Player 1 wins!!!")
				WIN=True
				break
		else:
			action = agent.take_action()
			next_state, reward, done, _  = env.step(action, piece2)
			movements.append(action)
			turn += 1
			turn = turn % 2
			if done:
				print("Player 2 wins!!!")
				WIN=True
				break
	env.visualize_board()
	print(env.display_board())
	print(movements)
	print(steps)

if __name__ == "__main__":
	main()