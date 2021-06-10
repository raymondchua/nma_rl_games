import numpy as np
from connect4 import ConnectFourEnv as board

def encode_board(board):
    board_state = board.current_board
    encoded = np.zeros([6,7,3]).astype(int)
    for row in range(6):
        for col in range(7):
            if board_state[row,col] != " ":
                encoded[row, col, board_state[row,col]] = 1
    if board.player == 1:
        encoded[:,:,2] = 1 # player to move
    return encoded

def decode_board(encoded):
    decoded = np.zeros([6,7]).astype(str)
    decoded[decoded == "0.0"] = " "

    for row in range(6):
        for col in range(7):
            for k in range(1,2):
                if encoded[row, col, k] == 1:
                    decoded[row, col] = k
    cboard = board()
    cboard.current_board = decoded
    cboard.player = encoded[0,0,2]
    return cboard