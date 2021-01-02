grid = [[0, 4, 5, 9, 0, 0, 3, 0, 0],
        [8, 0, 3, 0, 4, 6, 0, 0, 5],
        [0, 1, 0, 0, 5, 2, 0, 7, 0],
        [7, 6, 0, 8, 0, 0, 0, 0, 9],
        [4, 0, 0, 0, 0, 0, 0, 0, 7],
        [5, 0, 0, 0, 0, 1, 0, 3, 2],
        [0, 2, 0, 6, 1, 0, 0, 9, 0],
        [1, 0, 0, 2, 9, 0, 8, 0, 3],
        [0, 0, 4, 0, 0, 8, 2, 5, 0]]


def print_grid():
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")


def possible(y, x, n):
    global grid
    for i in range(0, 9):
        if grid[y][i] == n:
            return False
    for i in range(0, 9):
        if grid[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print_grid()
    input("More?")


print("Solved: ")
solve()
