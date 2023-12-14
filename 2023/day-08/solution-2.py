from math import gcd

def solution(filename) -> int:
    desertMap = {}
    
    with open(filename) as input:
        path, *lines = input.read().split('\n')
        # print(path)

        for i, line in enumerate(lines[1:]):            
            vertex, nbrs = line.split(" = ")
            dir = [nbrs[1:4], nbrs[6:9]]

            desertMap[vertex] = dir

    curr = []
    for v in desertMap.keys():
        if v[-1] == 'A':
            curr.append(v)

    print(curr)
    idx = 0
    steps = 0
    
    dir = {
        'L': 0, 'R': 1
    }
    nums = []
    while True:
        new = []
        for v in curr:
            dest = desertMap[v][dir[path[idx]]]
            if dest[-1] != 'Z':
                new.append(dest)
            else:
                print(steps+1)
                nums.append(steps+1)
                

        idx += 1
        if idx == len(path):
            idx = 0

        steps += 1

        # check
        done = True
        for v in new:
            if v[-1] != 'Z':
                done = False
        if done:
            break
        curr = new
        # print(new, steps, "Num of Z: ", c, "**************" if c > 0 else "")

    lcm = nums.pop()
    for num in nums:
        lcm = lcm * num // gcd(lcm, num)

    return lcm


if __name__ == '__main__':
    print(solution('2023/day-08/input.txt'))