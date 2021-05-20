import numpy as np
import random

from connect4 import ConnectFourEnv
from Agents import RandomAgent

class test_environment():
    def __init__(self, agent, env):
        self.env = env
        self.agent = agent

    def test_find_avail_row(self, action):
        col = self.env._game_board[:, action]

        print('available row before taking actions in columns 1 to 4:',  self.env.find_avail_row(col))
        for i in range(4):
            self.env.step(i, 2)

        print('available row after taking the actions:', self.env.find_avail_row(col))

    def test_rest(self):
        for i in range(3):
            action = self.agent.take_action()
            token = random.randint(1,2)
            self.env.step(action, token)
        print("board before reset:")
        print(self.env.display_board())
        self.env.reset()
        print("board after reset:")
        print(self.env.display_board())

    def test_winning_positions(self, token):
       # test the vertical win
       self.env.step(1, token)
       self.env.step(1, token)
       self.env.step(1, token)
       _,_,d,_ = self.env.step(1, token)
       print('Done:',d)
       print('vertical win')
       print(self.env.display_board())

       self.env.reset()
       # test the horizontal win
       self.env.step(1, token)
       self.env.step(1, token)
       self.env.step(1, token)
       _,_,d,_ = self.env.step(1, token)
       print('Done:',d)
       print('horizontal win')
       print(self.env.display_board())

       self.env.reset()
       # test the diagonal (left to right) win
       self.env.step(1, token)
       self.env.step(2, token)
       self.env.step(3, token)
       self.env.step(3, token)
       self.env.step(4, token)
       _,_,d,_ = self.env.step(4, token)
       print('Done:',d)
       print('diagonal (Left to Right) win')
       print(self.env.display_board())


       # test the diagonal (right to left) win
       self.env.step(6, token)
       self.env.step(5, token)
       self.env.step(4, token)
       self.env.step(4, token)
       self.env.step(3, token)
       _,_,d,_ = self.env.step(3, token)
       print('Done:', d)
       print('diagonal (Right to Left) win')
       print(self.env.display_board())

    def test_step(self):
        self.env.reset()
        for i in range(5):
            action = self.agent.take_action()
            token = random.randint(1,2)
            print('board after taking action {} by player {}:' .format(action, token))
            _,_,done,_ = self.env.step(action, token)
            print(self.env.display_board())

            if done:
                break

    def test_visualize_board(self):
        self.env.visualize_board()
        print('figure of the board is saved!')

if __name__ == "__main__":
    env = ConnectFourEnv()
    agent = RandomAgent(env)
    tse = test_environment(agent, env)
    print( '\n #### Test winning_position() ####\n')
    tse.test_winning_positions(token=1)

    print( '\n #### Test step() ####\n')
    tse.test_step()

    print( '\n #### Test find_avail_row() ####\n')
    tse.test_find_avail_row(action=3)

    print( '\n #### Test reset() ####\n')
    tse.test_rest()

    print( '\n #### Test visualize_board() ####\n')
    tse.test_visualize_board()