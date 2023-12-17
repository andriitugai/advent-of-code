from heapq import heappop, heappush

def solution(filename) -> int:

    with open(filename) as input:
        grid = [list(map(int, list(line.strip()))) for line in input.readlines()]

    m, n = len(grid), len(grid[0])

    heap = [(0, 0, 0, 0, 0, 0)]
    visited = set()

    while heap:
        heatLoss, r, c, dr, dc, numSteps = heappop(heap)
        if r == m - 1 and c == n - 1 and numSteps >= 4:
            return heatLoss

        if r < 0 or r >= m or c < 0 or c >= n:
            continue

        if (r, c, dr, dc, numSteps) in visited:
            continue
        visited.add((r, c, dr, dc, numSteps))

        if numSteps < 10 and (dr, dc) != (0, 0):
            r1, c1 = r + dr, c + dc
            if 0 <= r1 < m and 0 <= c1 < n: 
                heappush(heap, (heatLoss + grid[r1][c1], r1, c1, dr, dc, numSteps + 1))

        if numSteps >= 4 or (dr, dc) == (0, 0):
            for dr1, dc1 in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (dr1, dc1) != (dr, dc) and (dr1, dc1) != (-dr, -dc):
                    r1, c1 = r + dr1, c + dc1
                    if 0 <= r1 < m and 0 <= c1 < n: 
                        heappush(heap, (heatLoss + grid[r1][c1], r1, c1, dr1, dc1, 1))

    return 0


if __name__ == '__main__':
    print(solution('2023/day-17/input.txt'))