import csv

CANT_VISIT = -2
DIDNT_VISIT = -1
with open('maze.txt') as MAZE_file:
    maze = []
    for line in MAZE_file:
        line = line[:-1]
        lineArr = []
        for data in line:
            if data == " ":
                val = DIDNT_VISIT
            else:
                val = CANT_VISIT
            lineArr.append(val)
        maze.append(lineArr)

M = len(maze[0])
N = len(maze)
to_reach = (M - 1, N - 1)

print(to_reach)
maze[0][0] = 0
to_visit = [(0, 0)]


def append(x, y, c):
    maze[y][x] = c
    print(x,y)
    to_visit.append((x, y))


def print_maze():
    for line in maze:
        for x in line:
            if x==DIDNT_VISIT:
                val=" "
            elif x==CANT_VISIT:
                val="*"
            else:
                val="o"
            print(val, end='')
        print()

while True:
    p = to_visit.pop(0)
    if p[0] == to_reach[0] and p[1] == to_reach[1]:
        break
    current_value = maze[p[1]][p[0]]
    if p[0] + 1 < M and maze[p[1]][p[0] + 1] == DIDNT_VISIT:
        append(p[0] + 1, p[1], current_value + 1)
    if p[0] - 1 >= 0 and maze[p[1]][p[0] - 1] == DIDNT_VISIT:
        append(p[0] - 1, p[1], current_value + 1)
    if p[1] + 1 < N and maze[p[1] + 1][p[0]] == DIDNT_VISIT:
        append(p[0], p[1] + 1, current_value + 1)
    if p[1] - 1 >= 0 and maze[p[1] - 1][p[0]] == DIDNT_VISIT:
        append(p[0], p[1] - 1, current_value + 1)

print_maze()