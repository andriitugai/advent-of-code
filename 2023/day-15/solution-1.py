def getHash(s: str) -> int:
    hash = 0
    for c in s:
        hash = (hash + ord(c)) * 17 % 256
    return hash


def solution(filename) -> int:
    with open(filename) as input:
        words = input.read().split(",")

    return sum(map(getHash, words))


if __name__ == '__main__':
    print(solution('2023/day-15/input.txt'))
