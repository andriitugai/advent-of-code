from typing import List, Tuple, Set
from functools import cache

def get_input(filename: str) -> (Tuple[int, List[Set[int]]]):
    global grid
    with open(filename) as input:
        start_line = input.readline()
        start = start_line.index('S')

        for line in input.readlines():
            grid.append(set(i for i, c in enumerate(line) if c == '^'))

    # print(f'S={start}')
    # for r in grid:
    #     print(r)

    return start

def part_1(start: int) -> int:
    result = 0
    prev = set([start])
    for row in grid:
        curr = set()
        for beam in prev:
            if beam in row:
                curr.add(beam - 1)
                curr.add(beam + 1)
                result += 1
            else:
                curr.add(beam)

        prev = curr
    return result

@cache
def part_2(start: int, row = 0) -> int:
    if row >= len(grid):
        return 1
    
    if start not in grid[row]:
        return part_2(start, row + 1)
    else:
        return part_2(start + 1, row + 1) + part_2(start - 1, row + 1)
    

grid = []
if __name__ == '__main__':
    filename = "input.txt"
    start = get_input(filename)
    print(part_1(start))
    print(part_2(start))