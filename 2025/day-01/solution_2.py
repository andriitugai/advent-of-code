def part_2(filename: str):
    position = 50
    result = 0
    with open(filename) as input:
        for line in input.readlines():
            dir = 1
            if line[0] == 'L':
                dir = -1
            dist = int(line.strip()[1:])
            new_position = position + dir * dist
            if new_position == 0 or (new_position < 0 and position > 0) or (new_position > 0 and position < 0):
                result += 1
            # result += dist // 100

            while new_position <= -100:
                new_position += 100
                result += 1
            while new_position >= 100:
                new_position -= 100
                result += 1

            

            new_position %= 100
            position = new_position

    return result

if __name__ == '__main__':
    print(part_2('input.txt'))