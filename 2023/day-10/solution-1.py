from collections import deque


def solution(filename):
    grid = []
    with open(filename) as input:
        for line in input.readlines():
            grid.append(line.strip())

    m, n = len(grid), len(grid[0])
    # Search the starting point:
    r0, c0 = -1, -1
    for row in range(m):
        for col in range(n):
            if grid[row][col] == "S":
                r0 = row
                c0 = col
                break
        else:
            continue
        break

    q = deque([(r0, c0)])
    
    visited = set()
    visited.add((r0, c0))
    steps = 0

    while q:
        # for _ in range(len(q)):
        r, c = q.popleft()
        ch = grid[r][c]

        if r > 0 and ch in "S|JL" and grid[r - 1][c] in "|7F" and (r - 1, c) not in visited:
            visited.add((r - 1, c))
            q.append((r - 1, c))

        if r < m - 1 and ch in "S|7F" and grid[r + 1][c] in "|JL" and (r + 1, c) not in visited:
            visited.add((r + 1, c))
            q.append((r + 1, c))

        if c > 0 and ch in "S-J7" and grid[r][c - 1] in "-FL" and (r, c - 1) not in visited:
            visited.add((r, c - 1))
            q.append((r, c - 1))

        if c < n - 1 and ch in "S-FL" and grid[r][c + 1] in "-J7" and (r, c + 1) not in visited:
            visited.add((r,c + 1))
            q.append((r, c + 1))
            
        steps += 1

    return len(visited) // 2


if __name__ == '__main__':
    print(solution('2023/day-10/input.txt'))
