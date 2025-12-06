import re
from typing import List
from functools import reduce


def get_input(filename: str) -> List[List]:
    ops = []
    with open(filename) as input:
        lines = [line.strip() for line in input.readlines()]
        pat_num = r"\d+"
        pat_ops = r"\*|\+"

        for line in lines[:-1]:
            ops.append(list(map(int, re.findall(pat_num, line))))

        ops.append(re.findall(pat_ops, lines[-1]))

    # Transpose matrix
    home_tasks = [list(task) for task in list(zip(*ops))]
    return home_tasks

def get_input_2(filename: str) -> List[List]:
    with open(filename) as input:
        lines = [line.replace('\n', '') for line in input.readlines()]

    ops = list(line for line in zip(*lines))
    home_tasks = []
    for op in ops:
        home_tasks.append(["".join(list(op[:-1])).strip(), op[-1]])

    return home_tasks


def part_1(home_tasks: List[List]) -> int:
    # print(home_tasks)
    result = 0
    for task in home_tasks:
        func = lambda x, y: x + y
        if task[-1] == '*':
            func = lambda x, y: x * y

        result += reduce(func, task[:-1])

    return result

def part_2(home_tasks: List[List]) -> int:
    home_tasks.append(['', ''])
    result = 0
    func = lambda x, y: x + y
    curr_ops = []

    for task in home_tasks:
        if task[0].strip() == '' and curr_ops:
            result += reduce(func, curr_ops)
            curr_ops = []
            continue

        if task[1] == '+':
            func = lambda x, y: x + y
        elif task[1] == '*':
            func = lambda x, y: x * y

        curr_ops.append(int(task[0]))

    return result
    

if __name__ == '__main__':
    filename = "input.txt"

    ops = get_input(filename)
    print(part_1(ops))
    
    ops = get_input_2(filename)
    print(part_2(ops))