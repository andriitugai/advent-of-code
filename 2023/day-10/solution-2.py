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
    maybe_s = {"|", "-", "F", "J", "L", "7"}

    while q:
        r, c = q.popleft()
        ch = grid[r][c]

        if r > 0 and ch in "S|JL" and grid[r - 1][c] in "|7F" and (r - 1, c) not in visited:
            visited.add((r - 1, c))
            q.append((r - 1, c))
            if ch == "S":
                maybe_s &= {"|", "J", "L"}

        if r < m - 1 and ch in "S|7F" and grid[r + 1][c] in "|JL" and (r + 1, c) not in visited:
            visited.add((r + 1, c))
            q.append((r + 1, c))
            if ch == "S":
                maybe_s &= {"|", "7", "F"}

        if c > 0 and ch in "S-J7" and grid[r][c - 1] in "-FL" and (r, c - 1) not in visited:
            visited.add((r, c - 1))
            q.append((r, c - 1))
            if ch == "S":
                maybe_s &= {"-", "J", "7"}

        if c < n - 1 and ch in "S-FL" and grid[r][c + 1] in "-J7" and (r, c + 1) not in visited:
            visited.add((r,c + 1))
            q.append((r, c + 1))
            if ch == "S":
                maybe_s &= {"-", "F", "L"}

    assert len(maybe_s) == 1
    (S,) = maybe_s
    print(S)

    grid = [row.replace("S", S) for row in grid]
    grid = ["".join(ch if (r, c) in visited else "." for c, ch in enumerate(row)) for r, row in enumerate(grid)]

    outside = set()
    for r, row in enumerate(grid):
        within = False
        # riding = False
        up = None
        for c, ch in enumerate(row):
            if ch == "|":
                assert up is None
                within = not within
            elif ch == "-":
                assert up is not None
            elif ch in "LF":
                assert up is None
                up = ch == "L"
            elif ch in "7J":
                assert up is not None
                if ch != ("J" if up else "7"):
                    within = not within
                up = None
            elif ch == ".":
                pass
            else:
                raise RuntimeError(f"unexpected error (horizontal): {ch}")

            if not within:
                outside.add((r, c))

    for r in range(m):
        for c in range(n):
            print("#" if (r, c) in outside else ".", end="")
        print("")

    return len(grid) * len(grid[0]) - len(outside | visited)


if __name__ == '__main__':
    print(solution('2023/day-10/input.txt'))
