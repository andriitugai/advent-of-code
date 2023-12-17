from collections import deque


class Beam:
    def __init__(self, start, dir) -> None:
        self.start = start
        self.dir = dir


def solution(filename: str) -> int:

    with open(filename) as input:
        grid = [list(line.strip()) for line in input.readlines()] 

    def getHearedCells(r0, c0, dr0, dc0):
        q = deque()

        q.append((r0, c0, dr0, dc0))
        visited = set()

        while q:
            r, c, dr, dc = q.popleft()

            r += dr
            c += dc

            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                continue

            ch = grid[r][c]
            
            if ch == "." or (ch == "-" and dc != 0) or (ch == "|" and dr != 0):
                if (r, c, dr, dc) not in visited:
                    visited.add((r, c, dr, dc))
                    q.append((r, c, dr, dc))
            elif ch == "/":
                dr, dc = -dc, -dr
                if (r, c, dr, dc) not in visited:
                    visited.add((r, c, dr, dc))
                    q.append((r, c, dr, dc))
            elif ch == "\\":
                dr, dc = dc, dr
                if (r, c, dr, dc) not in visited:
                    visited.add((r, c, dr, dc))
                    q.append((r, c, dr, dc))
            else:
                for dr, dc in [(1, 0), (-1, 0)] if ch == "|" else [(0, 1), (0, -1)]:
                    if (r, c, dr, dc) not in visited:
                        visited.add((r, c, dr, dc))
                        q.append((r, c, dr, dc))


        return len(set((r, c) for (r, c, _, _) in visited))
    
    maxHeated = 0
    for r0 in range(len(grid)):
        heated = getHearedCells(r0, -1, 0, 1)
        if heated > maxHeated:
            maxHeated = heated
        heated = getHearedCells(r0, len(grid[0]), 0, -1)
        if heated > maxHeated:
            maxHeated = heated

    for c0 in range(len(grid[0])):
        heated = getHearedCells(-1, c0, 1, 0)
        if heated > maxHeated:
            maxHeated = heated
        heated = getHearedCells(len(grid), c0, -1, 0)
        if heated > maxHeated:
            maxHeated = heated
    
    return maxHeated


if __name__ == '__main__':
    print(solution('2023/day-16/input.txt'))
