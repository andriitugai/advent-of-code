from collections import deque


def solution(filename) -> int:

    with open(filename) as input:
        grid = [list(line.strip()) for line in input.readlines()]

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "S":
                cell = row, col
                print(f"Start = {cell}")
                break

    q = deque()
    q.append(cell)
    nSteps = 0
    stepLimit = 64
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    while len(q) > 0:
        gardens = len(q)
        visited = set()
        for _ in range(gardens):
            cr, cc = q.popleft()
            for dr, dc in dirs:
                row, col = cr + dr, cc + dc
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and (row, col) not in visited and grid[row][col] != "#":
                    q.append((row, col))
                    visited.add((row, col))
        nSteps += 1
        print(f"Step #{nSteps:2}: {len(q)} gardens are reached")
        if nSteps == stepLimit:
            return len(q)

    return 0



if __name__ == '__main__':
    print(solution('2023/day-21/input.txt'))