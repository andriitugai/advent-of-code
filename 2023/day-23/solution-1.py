
dirs = {
    '^': [(-1, 0)],
    'v': [(1, 0)],
    '>': [(0, 1)],
    '<': [(0, -1)],
    '.': [(-1, 0), (1, 0), (0, -1), (0, 1)]
}

def solution(filename) -> int:
    with open(filename) as input:
        grid = [list(line.strip()) for line in input.readlines()]

    m, n = len(grid), len(grid[0])
    start = (0, grid[0].index('.'))
    dest = (m-1, grid[-1].index('.'))

    print(start, dest)
    points = [start, dest]

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == '#':
                continue
            neighbors = 0
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != '#':
                    neighbors += 1
            if neighbors > 2:
                points.append((r, c))

    graph = {pt: {} for pt in points}

    for sr, sc in points:
        stack =  [(0, sr, sc)]
        visited = {(sr, sc)}

        while stack:
            numSteps, r, c = stack.pop()

            if numSteps != 0 and (r, c) in points:
                graph[(sr, sc)][(r, c)] = numSteps
                continue

            for dr, dc in dirs[grid[r][c]]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != '#' and (nr, nc) not in visited:
                    stack.append((numSteps + 1, nr, nc))
                    visited.add((nr, nc))

    seen = set()
    def dfs(pt):
        if pt == dest:
            return 0
        
        maxPath = -float('inf')

        seen.add(pt)
        for nx in graph[pt]:
            maxPath = max(maxPath, dfs(nx) + graph[pt][nx])
        seen.remove(pt)

        return maxPath

    return dfs(start)


if __name__ == '__main__':
    print(solution('2023/day-23/input.txt')) 