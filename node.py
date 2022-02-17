from board import Board


class Node:
    def __init__(self, board, goal_state, g = 0):
        self.board = board
        self.goal_state = goal_state
        self.h = self.calc_h()
        self.g = g


    def calc_h(self):
        board = []
        res=0
        for r in range(self.board.rows):
            for c in range(self.board.cols):
                curr = self.board.board[r][c]
                if curr>0 and curr != self.goal_state.board[r][c]:
                    res+=1
        return res

    def f(self):
        return self.h+self.g

    def __str__(self):
        print(self.board)
        return ''

    def get_neighbors(self):




def main():
    initial_state = Board([1,2,3,8,0,4,7,6,5])
    goal_state = Board([2,8,1,0,4,3,7,6,5])
    print(initial_state)

    n = Node(initial_state, goal_state)
    print(n.f())


if __name__ == '__main__':
    main()