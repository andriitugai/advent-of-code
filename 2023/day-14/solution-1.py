def solution(filename) -> int:
    result = 0
    with open(filename) as input:
        grid = [list(line) for line in input.read().split("\n")]

    m, n = len(grid), len(grid[0])

    for col in range(n):
        lastEmpty = 0
        for row in range(m):
            if grid[row][col] == 'O' and lastEmpty != row:
                grid[lastEmpty][col] = 'O'
                grid[row][col] = "."
                result += (n - lastEmpty)
                lastEmpty += 1
            elif grid[row][col] == 'O':
                lastEmpty = row + 1
                result += (n - row)
            elif grid[row][col] == '#':
                lastEmpty = row + 1

    return result


if __name__ == '__main__':
    print(solution('2023/day-14/input_.txt'))
