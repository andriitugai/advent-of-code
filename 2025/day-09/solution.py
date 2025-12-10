from typing import List, Tuple
from functools import cache

tiles = []
segments = []

def get_input(filename: str):
    global tiles, segments
    with open(filename) as input:
        tiles = [list(map(int, line.strip().split(','))) for line in input.readlines()]

    segments = [(*tiles[-1], *tiles[0])]
    for i, tile in enumerate(tiles[1:]):
        segments.append((tiles[i][0], tiles[i][1], *tile))


def get_area(p1: Tuple[int], p2: Tuple[int]) -> int:
    x1, y1 = p1
    x2, y2 = p2
    if x2 > x1: x1, x2 = x2, x1
    if y2 > y1: y1, y2 = y2, y1
    return (x1 - x2 + 1) * (y1 - y2 + 1)


@cache
def inside_poly(x: int, y: int) -> bool:
    inside = False
    for (x1, y1), (x2, y2) in zip(tiles, tiles[1:] + tiles[:1]):
        if (x == x1 == x2 and min(y1, y2) <= y <= max(y1, y2) or
            y == y1 == y2 and min(x1, x2) <= x <= max(x1, x2)):
            return True
        if ((y1 > y) != (y2 > y)) and (x < (x2 - x1)* (y - y1) / (y2 - y1) + x1):
            inside = not inside

    return inside

def edge_intersects_rectangle(x1, y1, x2, y2, rx1, ry1, rx2, ry2):
    if y1 == y2:
        if ry1 < y1 < ry2:
            if max(x1, x2) > rx1 and min(x1, x2) < rx2:
                return True
        else:
            if rx1 < x1 < rx2:
                if max(y1, y2) > ry1 and min(y1, y2) < ry2:
                    return True
    return False


def rectangle_valid(x1, y1, x2, y2):
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])

    for x, y in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
        if not inside_poly(x, y):
            return False
        
    for (ex1, ey1), (ex2, ey2) in zip(tiles, tiles[1:] + tiles[:1]):    
        if edge_intersects_rectangle(ex1, ey1, ex2, ey2, x1, y1, x2, y2):
            return False
    
    return True


def part_1() -> int:  
    global tiles 
    maxArea = 0
    for i in range(len(tiles)):
        for j in range(i+1, len(tiles)):
            area = get_area(tiles[j], tiles[i])
            if area > maxArea:
                maxArea = area
    return maxArea


def part_2() -> int:  
    global tiles 
    maxArea = 0
    for i in range(len(tiles)):
        for j in range(i+1, len(tiles)):
            area = get_area(tiles[j], tiles[i])
            if area > maxArea and rectangle_valid(tiles[j][0], tiles[j][1], tiles[i][0], tiles[i][1]):
                maxArea = area
    return maxArea



if __name__ == '__main__':
    filename = "input.txt"
    get_input(filename)

    print(part_1())
    print(part_2())