def findMirror(nums: list) -> int:
    n = len(nums)
    mirr = 0
    
    for i in range(1, n):
        left = nums[:i][::-1]
        right = nums[i:]

        left = left[:len(right)]
        right = right[:len(left)]

        if left == right:
            mirr = i
            break
        
    return mirr


def solution(filename):
    total = 0

    with open(filename) as input:
        blocks = input.read().split("\n\n")

    for n, block in enumerate(blocks):
        print(n)
        grid = [[1 if c == '#' else 0 for c in row] for row in block.split("\n")]
        
        rows = []
        for r in range(len(grid)):
            num = 0
            for c in range(len(grid[0])):
                num = num * 2 + grid[r][c]
            rows.append(num)

        # print(rows)
        # print("Mirror at:", findMirror(rows))
        total += 100 * findMirror(rows)

        cols = []
        for c in range(len(grid[0])):
            num = 0
            for r in range(len(grid)):
                num = num * 2 + grid[r][c]
            cols.append(num)
        
        # print("Mirror at:", findMirror(cols))
        total += findMirror(cols)

    return total


if __name__ == '__main__':
    print(solution('2023/day-13/input.txt'))
