from typing import List

def get_input(filename: str) -> List[List[int]]:
    with open(filename) as input:
        grid = [
            [1 if cell == '@' else 0 for cell in line.strip()]
            for line in input.readlines()
        ]
    return grid

def remove_possible(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    def get_num_adjacents(row: int, col: int) -> int:
        adj = 0
        for r in [row - 1, row, row + 1]:
            for c in [col - 1, col, col + 1]:
                if r >= 0 and c >= 0 and r < m and c < n and (r, c) != (row, col):
                    adj += grid[r][c]
        return adj
    
    removed = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1 and get_num_adjacents(r, c) < 4:
                removed += 1
                grid[r][c] = 0

    return removed


def part_2(grid: List[List[int]]) -> int:
    total = 0
    while True:
        removed = remove_possible(grid)
        if removed == 0:
            break
        total += removed
    return total


def part_1(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    def get_num_adjacents(row: int, col: int) -> int:
        adj = 0
        for r in [row - 1, row, row + 1]:
            for c in [col - 1, col, col + 1]:
                if r >= 0 and c >= 0 and r < m and c < n and (r, c) != (row, col):
                    adj += grid[r][c]
        return adj
        
    return sum(1 if grid[r][c] and get_num_adjacents(r, c) < 4 else 0 for r in range(m) for c in range(n))


if __name__ == '__main__':
    grid = get_input('input.txt')

    print(part_1(grid))
    print(part_2(grid))