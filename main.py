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

	print('done')





if __name__ == "__main__":
	main()