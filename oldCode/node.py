from board import Board

def build_goal_state(size=9):
    l = []
    for i in range(1, size):
        l.append(i)
    l.append(0)
    return Board(l)

class Node:
    def __init__(self, board, g = 0):
        self.board = board
        self.goal_state: Board = build_goal_state(len(board))
        self.h = self.calc_h()
        self.g = g
        self.f = self.h + self.g


    def calc_h(self):
        board = []
        res=0
        for r in range(self.board.rows):
            for c in range(self.board.cols):
                curr = self.board.board[r][c]
                if curr>0 and curr != self.goal_state.board[r][c]:
                    res+=1
        return res

    def __str__(self):
        print(self.board)
        return ''

    def get_neighbors(self):
        row, col = self.board.empty_idx[0], self.board.empty_idx[1]
        neighbors = []
        for op in [[0,1],[1,0],[-1,0],[0,-1]]:
            i=op[0]
            j=op[1]
            if (self.board.is_valid(row + i, col + j)):
                neighbor_board = self.board.__copy__()
                neighbor_board.swap(row+i,col+j)
                neighbor = Node(neighbor_board, self.g+1)
                neighbor.board.empty_idx = [row+i,col+j]
                neighbors.append(neighbor)
        return neighbors

    def __eq__(self, other):
        return other.board == self.board



def main():
    board = Board([3, 4, 0, 6, 1, 8, 2, 5, 7])
    node = Node(board)

    print(node.g)

if __name__ == '__main__':
    main()