
def solution(filename) -> int:
    desertMap = {}
    
    with open(filename) as input:
        path, *lines = input.read().split('\n')
        print(path)

        for i, line in enumerate(lines[1:]):            
            vertex, nbrs = line.split(" = ")
            dir = [nbrs[1:4], nbrs[6:9]]

            desertMap[vertex] = dir

    curr = "AAA"
    dir = {
        'L': 0, 'R': 1
    }
    idx = 0
    steps = 0
    while curr != "ZZZ":
        curr = desertMap[curr][dir[path[idx]]]
        # if path[idx] == 'L':
        #     curr = desertMap[curr][0]
        # else:
        #     curr = desertMap[curr][1]
        idx += 1
        if idx == len(path):
            idx = 0

        steps += 1

    return steps


if __name__ == '__main__':
    print(solution('2023/day-08/input.txt'))