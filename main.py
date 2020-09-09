import random
from langton_ant import LangtonsAnt


if __name__ == "__main__":
    grid = [
        [random.choice([True, False]), random.choice([True, False])] for _ in range(3)
    ]

    print("This is Langston's Ant game, please input ant's position next")
    ant_x = input("Enter ant position x: ")
    ant_y = input("Enter ant position y: ")

    la_app = LangtonsAnt(initial_state=grid, start_position=[int(ant_x), int(ant_y)])

    is_grid_correct = la_app.validate()
    if not is_grid_correct:
        print("Grid is not correct")
        exit(1)

    is_ant_position_corrent = la_app.validate_move()
    if not is_ant_position_corrent:
        print("Ant position is not correct")
        exit(1)

    print("Use: \nn for next move \ns to print the state \nq for quit")

    while True:
        command = input("--> ")
        if command == "n":
            result = la_app.next()
            if not result:
                print("Error in the last move")
                break

        elif command == "s":
            print(la_app.state)

        elif command == "q":
            break
