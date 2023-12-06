def part_1(filename: str) -> int:
    nums = { "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", 
            "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    result = 0
    with open(filename) as input:
        for line in input:
            left_number, right_number = -1, -1
            digit = -1
            for i in range(len(line)):
                if '0' <= line[i] <= '9':
                    digit = int(line[i])
                else:
                    for k, v in nums.items():
                        if line[i:].startswith(k):
                            digit = int(v)

                if left_number == -1:
                    left_number = digit
                right_number = digit

            result += left_number * 10 + right_number
    return result
    

if __name__ == '__main__':
    result = part_1("2023/day-01/part-1/input_1.txt")
    print(result)