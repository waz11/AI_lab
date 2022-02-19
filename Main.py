import time
from Search.Algorithms.Astar import Astar
from Search.Algorithms.DFID import DFID
from Search.Algorithms.IDA import IDA
from Puzzle.PuzzleGenerator import PuzzleGenerator
from Experiments.ResultFile import ResultFile


def main():
    file = ResultFile()
    generator = PuzzleGenerator()
    for i in range(1):
        # initial_state = generator.generate()
        # initial_state = [[8, 2, 3], [1, 0, 5],[ 4, 6, 7]]
        initial_state = [[1,2,3], [0,5,6], [4,7,8]]

        # A* Algorithm:
        start = time.time()
        num_of_nodes1, path_length1 = Astar(initial_state).search()
        end = time.time()
        f_time1 = end - start
        print(num_of_nodes1, path_length1, f_time1)

        # IDA* Algorithm:
        start = time.time()
        num_of_nodes2, path_length2 = IDA(initial_state).search()
        end = time.time()
        f_time2 = end - start
        print(num_of_nodes2, path_length2, f_time2)

        # DFID Algorithm:
        start = time.time()
        num_of_nodes2, path_length2 = DFID(initial_state).search()
        end = time.time()
        f_time2 = end - start
        print(num_of_nodes2, path_length2, f_time2)


        file.add_result(initial_state,f_time1,num_of_nodes1,path_length1, f_time2,num_of_nodes2,path_length2)


if __name__ == '__main__':
    main()