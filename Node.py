import collections
import copy


def calc_h(board):
    res = 0
    goal_state = [[1,2,3],[4,5,6],[7,8,0]]
    size = len(board)
    for r in range(size):
        for c in range(size):
            curr = board[r][c]
            if curr > 0 and curr != goal_state[r][c]:
                res += 1
    return res


def find_empty(board):
    size = len(board)
    for r in range(size):
        for c in range(size):
            if board[r][c]==0:
                return (r, c)

def swap(new_board,r1, c1,r2, c2):
    tmp = new_board[r1][c1]
    new_board[r1][c1] = new_board[r2][c2]
    new_board[r2][c2] = tmp

class Node:
    def __init__(self,board,g=0):
        self.board = board
        self.id = hash(str(board))
        self.g = g
        self.h = calc_h(board)
        self.f = self.g+self.h
        self.r0, self.c0 = find_empty(board)
        self.size = len(board)

    def __str__(self):
        a = ''
        for r in range(self.size):
            for c in range(self.size):
                val= self.board[r][c]
                a+=str(val)+' '
            a+='\n'
        return a

    def swap(self, r,c):
        tmp = self.board[self.r0][self.c0]
        self.board[self.r0][self.c0] = self.board[r][c]
        self.board[r][c] = tmp

    def is_valid(self,row,col):
        size = len(self.board)
        return 0<=row<size and 0<=col<size

    def get_neighbors(self):
        row, col = self.r0, self.c0
        neighbors = []
        dir = [[0,1],[1,0],[-1,0],[0,-1]]
        for op in dir:
            new_row, new_col = self.r0+op[0], self.c0+op[1]
            if (self.is_valid(new_row, new_col)):
                new_board = copy.deepcopy(self.board)
                swap(new_board,row, col,new_row, new_col)

                neighbor = Node(new_board, self.g+1)
                neighbor.r0, neighbor.c0 = new_row, new_col
                neighbors.append(neighbor)
        return neighbors

    def __eq__(self, other):
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] != other.board[r][c]:
                    return False
        return True

    def __gt__(self, other):
        if self.f == other.f:
            return self.h > other.h
        return self.f>other.f

    def __lt__(self, other):
        return not self.__gt__(other)


if __name__ == '__main__':
    # b = Node([[3, 4, 0],[ 6, 1, 8], [2, 5, 7]])
    # print(hash(str(b.board)))
    n1 = Node([[1, 2, 3], [4, 5, 6], [7, 8,0]])

    open_queue = collections.deque([])


