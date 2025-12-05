from typing import Tuple, List
from collections import Counter

def get_input(filename: str) -> Tuple[List[int], List[int]]:
    list_1, list_2 = [], []
    with open(filename) as input:
        for line in input.readlines():
            a1, a2 = list(map(int, line.strip().split('   ')))
            list_1.append(a1)
            list_2.append(a2)

    return sorted(list_1), sorted(list_2)

def part_1(l1: List[int], l2: List[int]) -> int:
    result = 0
    for i in range(len(l1)):
        a, b = l1[i], l2[i]
        if a < b: 
            a, b = b, a

        result += a - b

    return result
    
def part_2(l1: List[int], l2: List[int]) -> int:
    c2 = Counter(l2)
    result = 0
    for num in l1:
        result += num * c2[num]

    return result


if __name__ == '__main__':
    l1, l2 = get_input("input.txt")
    print(part_1(l1, l2))
    print(part_2(l1, l2))
