import board


class Node:
    def __init__(self, board, goal_state):
        self.board = board
        self.goal_state = goal_state
        self.h = 0
        self.g = 0


    def calculate_h(self):
        for i in board.

    def get_f(self):
        return self.h+self.g