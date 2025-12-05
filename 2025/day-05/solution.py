from typing import Tuple, List

def get_input(filename: str) -> Tuple[List[List[int]], List[int]]:
    intervals = []
    ids = []

    with open(filename) as input:
        while True:
            line = input.readline().strip()
            if line == "":
                break

            intervals.append(list(map(int, line.split('-'))))

        ids = sorted(list(map(int, input.readlines())))

    intervals.sort(key=lambda x: x[0])

    # Get intervals united
    intervals_united = []
    s0, e0 = intervals[0]
    for s1, e1 in intervals[1:]:
        if s1 >= s0 and s1 <= e0 and e1 > e0:
            e0 = e1
        elif s1 > e0:
            intervals_united.append([s0, e0])
            s0, e0 = s1, e1
    intervals_united.append([s0, e0])

    return intervals_united, ids

def part_1(intervals, ids: List[int]) -> int:
    result = 0
    pi, ni = 0, len(intervals)
    s, e = intervals[pi]
    max_fresh = intervals[-1][1]
    for id in ids:
        if id > max_fresh:
            break
        for s, e in intervals:
            if s <= id <= e:
                result += 1
                break
            if id > e:
                continue

    return result

def part_2(intervals) -> int:
    result = 0
    for s, e in intervals:
        result += (e - s + 1)
    return result

if __name__ == '__main__':
    intervals, ids = get_input('input.txt')
    # print(ids)
    # print(intervals)

    print(part_1(intervals, ids))
    print(part_2(intervals))
