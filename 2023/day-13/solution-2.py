def findMirror(grid: list) -> int:
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]
        
        if sum(sum(0 if a == b else 1 for a, b in zip(x, y)) for x, y in zip(above, below)) == 1:
            return r

    return 0


def solution(filename):
    total = 0

    with open(filename) as input:
        blocks = input.read().split("\n\n")

    for n, block in enumerate(blocks):
        grid = [[1 if c == '#' else 0 for c in row] for row in block.split("\n")]
        
        row = findMirror(grid)
        total += row * 100

        col = findMirror(list(zip(*grid)))
        total += col

    return total


if __name__ == '__main__':
    print(solution('2023/day-13/input.txt'))
