from typing import List, Tuple, Set, Dict
from collections import defaultdict
from math import prod

def solve(filename: str) -> Dict[Tuple, int]:
    part_1, part_2 = 0, 0
    with open(filename) as input:
        points = [tuple(map(int, line.strip().split(','))) for line in input.readlines()]

    distances = {}
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x0, y0, z0 = points[i]
            x1, y1, z1 = points[j]
            distances[(i, j)] = (x0 - x1) ** 2 + (y0 - y1) ** 2 + (z0 - z1) ** 2

    limit = 10 if len(points) < 100 else 1000
    ds = sorted(distances.items(), key=lambda x: x[1])

    parents = {i : i for i in range(len(distances))}
    def find(x: int) -> int:
        nonlocal parents
        if x == parents[x]:
            return x
        parents[x] = find(parents[x])
        return parents[x]
    
    def union(x, y):
        parents[find(y)] = find(x)

    wires = 0

    # print(list(enumerate(ds))[:5])

    for i, ((x, y), d) in enumerate(ds):
        if i == limit:
            sizes = defaultdict(int)
            for x in range(len(points)):
                sizes[find(x)] += 1
            part_1 = prod(sorted(sizes.values(), reverse=True)[:3])

        rx = find(x)
        ry = find(y)
        if rx != ry:
            wires += 1
            union(x, y)
            if wires == len(points) - 1:
                part_2 = points[x][0] * points[y][0]

    return part_1, part_2


if __name__ == '__main__':
    filename = "input.txt"
    p1, p2 = solve(filename)

    print("Part 1:", p1)
    print("Part 2:", p2)
