from math import sqrt


class Board:

    def __init__(self, values):
        self.rows = self.cols = int(sqrt(len(values)))
        self.empty_idx = ()
        self.board = self.__build__(values)


    def __build__(self, values):
        board = []
        i = 0
        for r in range(self.rows):
            board.append([])
            for c in range(self.cols):
                board[r].append(values[i])
                if values[i] == 0: self.empty_idx = (r, c)
                i += 1
        return board

    def __str__(self):
        for r in range(self.rows):
            print(self.board[r])
        return ''



def main():
    b = Board([1, 2, 3, 4, 5, 6, 7, 8, 0])
    print(b)
    print(b.empty_idx)


if __name__ == '__main__':
    main()