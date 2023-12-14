def getLoad(grid) -> int:
    load = 0
    m, n = len(grid), len(grid[0])
    for row in range(m):
        for col in range(n):
            if grid[row][col] == 'O':
                load += (m - row)
    return load

def solution(filename) -> int:
    result = 0
    with open(filename) as input:
        grid = [list(line) for line in input.read().split("\n")]

    m, n = len(grid), len(grid[0])
    cycles = 15000
    seen = set()
    grids = []

    current = 0
    start = -1

    for cycle_num in range(cycles):

        t = tuple(tuple(row) for row in grid)
        if t in seen:
            start = grids.index(t)
            current = cycle_num
            print(f"Cycle #{current}, already have seen it at {start} cycle!")
            break
        else:
            seen.add(t)
            grids.append(t)

        # North
        for col in range(n):
            lastEmpty = 0
            for row in range(m):
                if grid[row][col] == 'O' and lastEmpty != row:
                    grid[lastEmpty][col] = 'O'
                    grid[row][col] = "."
                    lastEmpty += 1
                elif grid[row][col] in 'O#':
                    lastEmpty = row + 1

        # West
        for row in range(m):
            lastEmpty = 0
            for col in range(n):
                if grid[row][col] == 'O' and lastEmpty != col:
                    grid[row][lastEmpty] = 'O'
                    grid[row][col] = "."
                    lastEmpty += 1
                elif grid[row][col] in 'O#':
                    lastEmpty = col + 1

        # South
        for col in range(n):
            lastEmpty = m - 1
            for row in range(m - 1, -1, -1):
                if grid[row][col] == 'O' and lastEmpty != row:
                    grid[lastEmpty][col] = 'O'
                    grid[row][col] = "."
                    lastEmpty -= 1
                elif grid[row][col] in 'O#':
                    lastEmpty = row - 1

        # East
        for row in range(m):
            lastEmpty = n - 1
            for col in range(n - 1, -1, -1):
                if grid[row][col] == 'O' and lastEmpty != col:
                    grid[row][lastEmpty] = 'O'
                    grid[row][col] = "."
                    lastEmpty -= 1
                elif grid[row][col] in 'O#':
                    lastEmpty = col - 1
        

    idx = (1000000000 - start) % (current - start) + start
    result = getLoad(grids[idx])

    return result


if __name__ == '__main__':
    print(solution('2023/day-14/input.txt'))
