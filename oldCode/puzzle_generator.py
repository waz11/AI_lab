import itertools
import random


def find_empty(puzzle):
    size = len(puzzle)
    for r in range(size):
        for c in range(size):
            if puzzle[r][c] == 0:
                return (r,c)

def get_moves(puzzle):
    r,c = find_empty(puzzle)
    size = len(puzzle)
    direcs = [(r, c - 1),
     (r, c + 1),
     (r - 1, c),
     (r + 1, c)]
    moves = []
    for d in direcs:
        i=d[0]
        j=d[1]
        if(i>=0 and i<size and j>=0 and j<size):
            moves.append(d)
    return moves

def swap(puzzle, empty, other):
    r1 = empty[0]
    c1 = empty[1]
    r2 = other[0]
    c2 = other[1]
    tmp = puzzle[r1][c1]
    puzzle[r1][c1] = puzzle[r2][c2]
    puzzle[r2][c2] = tmp

def shuffle(puzzle):
    r, c = find_empty(puzzle)
    for _ in range(1000):
        moves = get_moves(puzzle)
        move = random.choice(moves)
        swap(puzzle, (r, c), move)
        r,c = move[0], move[1]
    print(puzzle)

def main():
    puzzle = [[1,2,3],[4,5,6],[7,8,0]]
    shuffle(puzzle)


if __name__ == '__main__':
    main()