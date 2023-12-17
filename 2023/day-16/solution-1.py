from collections import deque


class Beam:
    def __init__(self, start, dir) -> None:
        self.start = start
        self.dir = dir


def solution(filename: str) -> int:

    with open(filename) as input:
        grid = [list(line.strip()) for line in input.readlines()] 

    q = deque()
    q.append((0, -1, 0, 1))
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



if __name__ == '__main__':
    print(solution('2023/day-16/input.txt'))
