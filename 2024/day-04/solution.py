from typing import List


word = 'XMAS'

def get_input(filename: str) -> List[List[str]]:
    with open(filename) as input:
        grid = [
            list(line.strip()) for line in input.readlines()
        ]
    return grid

def part_1(grid: List[List[str]]) -> int:
    result = 0
    dirs = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    m, n = len(grid), len(grid[0])

    for r in range(m):
        for c in range(n):
            if grid[r][c] == word[0]:
                for dx, dy in dirs:
                    x, y = c, r
                    idx = 1
                    while idx < len(word):
                        x += dx
                        y += dy
                        if 0 <= x < n and 0 <= y < m and grid[y][x] == word[idx]:
                            idx += 1
                            if idx == len(word):
                                result += 1
                        else:
                            break

    return result

def part_2(grid: List[List[str]]) -> int:
    result = 0
    m, n = len(grid), len(grid[0])

    for r in range(1, m - 1):
        for c in range(1, n - 1):
            if grid[r][c] == 'A' and \
                ((grid[r-1][c-1] == 'M' and grid[r+1][c+1] == 'S') or (grid[r-1][c-1] == 'S' and grid[r+1][c+1] == 'M')) and \
                ((grid[r+1][c-1] == 'M' and grid[r-1][c+1] == 'S') or (grid[r+1][c-1] == 'S' and grid[r-1][c+1] == 'M')):
                result += 1

    return result


if __name__ == '__main__':
    filename = "input.txt"
    grid = get_input(filename)

    print(part_1(grid))
    print(part_2(grid))
    