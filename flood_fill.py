
import pprint
from random import choice, randint

from termcolor import colored


def generate_maze():
    walls = [1 for x in range(25)]
    space = [2 for y in range(55)]
    tiles = walls + space
    maze = [[1 if (i == 0 or j == 0 or i == 9 or j == 9) else choice(tiles) for i in range(10)] for j in range(10)]
    return maze


def print_maze(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            item = maze[i][j]

            if item == 1:
                out = colored(item, 'red')
            elif item == 2:
                out = colored(item, 'blue')
            elif item == 3:
                out = colored(item, 'yellow')
            else:
                out = colored(item, 'green')

            print(out, end=' ')
        print()


def flood_fill(maze):
    selected = -1
    while selected != 2:
        x = randint(0, len(maze) - 1)
        y = randint(0, len(maze[x]) - 1)

        selected = maze[x][y]

    rflood_fill(maze, x, y)
    maze[x][y] = 9  # mark start point


def rflood_fill(maze, x, y):
    tile = maze[x][y]
    if tile == 1:
        return
    if tile == 3:
        return
    maze[x][y] = 3

    rflood_fill(maze, x + 1, y)
    rflood_fill(maze, x - 1, y)
    rflood_fill(maze, x, y + 1)
    rflood_fill(maze, x, y - 1)


if __name__ == '__main__':
    maze = generate_maze()
    print("Before")
    print_maze(maze)

    print()
    print("After")
    flood_fill(maze)
    print_maze(maze)
