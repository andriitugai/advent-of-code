def get_max_joltage_1(bank: str) -> int:
    m1, m2 = bank[0], bank[-1]
    for c in bank[1: -1]:
        if c > m1:
            m1 = c
            m2 = bank[-1]
        elif c > m2:
            m2 = c

    print(bank, m1+m2)
    return int(m1 + m2)

def get_max_joltage(bank: str) -> int:
    n = len(bank)
    stack = []
    for i in range(n):
        while len(stack) > 0 and stack[-1] < bank[i] and len(stack) + n - i > 12:
            stack.pop()
        stack.append(bank[i])

    while len(stack) > 12:
        stack.pop()

    return int("".join(stack))

def solution(filename: str) -> int:
    with open(filename) as input:
        result = 0
        for bank in input.readlines():
            result += get_max_joltage(bank.strip())

    return result


if __name__ == '__main__':
    print(solution('input.txt'))