def part_1(filename: str):
    position = 50
    result = 0
    with open(filename) as input:
        for line in input.readlines():
            dir = 1
            if line[0] == 'L':
                dir = -1
            dist = int(line.strip()[1:])
            position += dir * dist
            position %= 100
            if position == 0:
                result += 1

    return result

if __name__ == '__main__':
    print(part_1('input.txt'))