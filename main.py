from board import Board


def main():
    initial_state = Board([1,2,3,8,0,4,7,6,5])
    goal_state = Board([2,8,1,0,4,3,7,6,5])
    print(initial_state)
    print(goal_state)



if __name__ == '__main__':
    main()