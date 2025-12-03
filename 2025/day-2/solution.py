def is_valid_1(id: str) -> bool:
    n = len(id)
    if n % 2:
        return True
    
    p1, p2 = 0, n // 2
    while p2 < n:
        if id[p1] != id[p2]:
            return True
        p1 += 1
        p2 += 1

    return False


def is_valid(id: str) -> bool:
    n = len(id)
    for size in range(1, n // 2 + 1):
        if n % size == 0:
            if len(set(id[i:i + size] for i in range(0, n, size))) == 1:
                return False
    return True


def part_1(filename: str):
    result = 0
    with open(filename) as input:
        for rng in input.readline().split(','):
            left, right = map(int, rng.split('-'))
            for id_ in range(left, right+1):
                if not is_valid(str(id_)):
                    result += id_

    return result


if __name__ == '__main__':
    print(part_1('input.txt'))