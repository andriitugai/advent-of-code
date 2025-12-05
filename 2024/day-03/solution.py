import re
from typing import List, Tuple

def get_input(filename: str) -> str:
    with open(filename) as input:
        lines = input.readlines()

    # print(len(lines))
    return lines


def get_muls_result_1(line: str) -> int:
    result = 0
    pattern = r"mul\(\d+\,\d+\)"
    muls = re.findall(pattern, line)
    for mul in muls:
        a, b = list(map(int, mul[4:-1].split(',')))
        result += a * b
    return result

def get_muls_result_2(line: str, isdo: bool) -> Tuple[int, bool]:
    result = 0
    pattern = r"mul\(\d+\,\d+\)|do\(\)|don\'t\(\)"
    muls = re.findall(pattern, line)
    # print(muls)
    for mul in muls:
        if mul == 'do()':
            isdo = True
        elif mul == "don't()":
            isdo = False
        else:
            if isdo:
                a, b = list(map(int, mul[4:-1].split(',')))
                result += a * b
    return result, isdo


def part_1(instructions: List[str]) -> int:
    result = 0
    for instr in instructions:
        result += get_muls_result_1(instr)

    return result


def part_2(instructions: List[str]) -> int:
    result = 0
    isdo = True
    for instr in instructions: 
        inc, isdo = get_muls_result_2(instr, isdo)
        result += inc

    return result


if __name__ == '__main__':
    instructions = get_input("input.txt")
    print(part_1(instructions))
    print(part_2(instructions))