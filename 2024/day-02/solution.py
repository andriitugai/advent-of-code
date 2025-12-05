from typing import List


def get_input(filename: str) -> List[List[int]]:
    result = []
    with open(filename) as input:
        for line in input.readlines():
            result.append(list(map(int, line.strip().split(" "))))
    return result

def part_1(reports: List[List[int]]) -> int:
    result = 0
    for report in reports:
        if is_safe(report):
            result += 1

    return result

def is_safe(report: List[int]) -> bool:
    dir = 1
    prev = report[0]
    if report[1] < prev:
        dir = -1

    for level in report[1:]:
        diff = dir * (level - prev)
        if diff < 1 or diff > 3:
            return False
        prev = level
        
    return True

def part_2(reports: List[List[int]]) -> int:
    result = 0
    for report in reports:
        if is_safe(report):
            result += 1
        else:
            for iex in range(len(report)):
                if is_safe(report[:iex] + report[iex+1:]):
                    result += 1
                    break

    return result


if __name__ == '__main__':
    reports = get_input("input.txt")
    print(part_1(reports))
    print(part_2(reports))