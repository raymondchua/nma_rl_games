
import random

class RandomAgent(object):
    def __init__(self, board):
        self.board = board

    def take_action(self):
        col = random.choice(range(1,self.board._num_cols))
        return col
