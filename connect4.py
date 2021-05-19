#!/usr/bin/env python3

import numpy as np

from enum import IntEnum

import matplotlib.pyplot as plt
from matplotlib.table import Table
import pandas as pd
from IPython.display import Image


class ConnectFourEnv(object):

	'''
	Connect 4 is a 6 (rows) x 7 (cols) two player game. 
	Possible states: 
		0 - empty
		1 - red token
		2 - yellow token

	Possible actions (discrete):
		0 - column 1 (from left)
		1 - column 2 
		2 - column 3
		3 - column 4 
		4 - column 5 
		5 - column 6 
		6 - column 7 

	'''

	# Enumeration of possible actions
	class Actions(IntEnum):
		# choose which column to drop the token
		col0 = 0
		col1 = 1
		col2 = 2
		col3 = 3
		col4 = 4
		col5 = 5
		col6 = 6

	def __init__(self, num_rows=6, num_cols=7):
		self._num_rows = num_rows
		self._num_cols = num_cols
		self._game_board = np.zeros((self._num_rows,self._num_cols))
		self._max_steps = self._num_rows * self._num_cols

		self._step_count = 0 

		# Action enumeration for this environment
		self._actions = self.Actions

	def find_avail_row(self, col):
		for i in range(self._num_rows):
			if col[i] == 0:
				return i

	def reset(self):
		self._step_count = 0 
		self._game_board = np.zeros((self._num_rows,self._num_cols))
		return self._game_board

	def display_board(self):
		return np.flip(self._game_board, 0)

	def winning_positions(self, token):
		#check for winning horizontal tokens
		for r in range(self._num_rows):
			for c in range(self._num_cols-3):
				if self._game_board[r,c] == token and self._game_board[r,c+1] == token and self._game_board[r,c+2] == token and self._game_board[r, c+3] == token:
					return True

		#check for winning vertical tokens
		for r in range(self._num_rows-3):
			for c in range(self._num_cols):
				if self._game_board[r,c] == token and self._game_board[r+1,c] == token and self._game_board[r+2,c] == token and self._game_board[r+3, c] == token:
					return True

		#check for diagonal with positive gradient (ie. /)
		for r in range(3,self._num_rows):
			for c in range(self._num_cols-3):
				if self._game_board[r,c] == token and self._game_board[r-1, c+1] == token and self._game_board[r-2, c+2] == token and self._game_board[r-3, c+3] == token:
					return True

		#check for diagonal with negative gradient (ie. \)
		for r in range(self._num_rows-3):
			for c in range(self._num_cols-3):
				if self._game_board[r,c] == token and self._game_board[r+1, c+1] == token and self._game_board[r+2, c+2] == token and self._game_board[r+3, c+3] == token:
					return True

		return False

	def load_game_board(self, board):
		self._game_board = board

	def check_valid_action(self, action):
		assert action >= 0 and action < self._num_cols,'invalid action!'


	def step(self, action, token):
		reward = 0
		done = False
		self._step_count += 1

		self.check_valid_action(action)

		#get corresponding col
		col = self._game_board[:, action] 


		#check for next available row 
		row = self.find_avail_row(col)
		print(row, action)
		self._game_board[row, action] = token

		# game ends when all spaces are filled
		if self._step_count == self._max_steps:
			done = True

		#check for winning positions
		if self.winning_positions(token):
			reward = 1
			done = True

		return self._game_board, reward, done, {}


	def visualize_board(self, fmt='{:d}', bkg_colors=['yellow', 'pink']):
		data = pd.DataFrame(self.display_board())
		fig, ax = plt.subplots(figsize=[7,7])
		ax.set_axis_off()
		tb = Table(ax, bbox=[0,0,1,1])
		nrows, ncols = data.shape
		width, height = 1.0 / ncols, 1.0 / nrows

		for (i,j), val in np.ndenumerate(data):
			idx = [j % 2, (j + 1) % 2][i % 2]
			color = bkg_colors[idx]
			tb.add_cell(i, j, width, height, text=fmt.format(int(val)),
					loc='center', facecolor=color)

		tb.set_fontsize(24)
		ax.add_table(tb)
		fig.savefig('connect4_final_state.png')

		return fig
