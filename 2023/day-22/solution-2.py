from collections import deque

def overlaps(a, b) -> bool:
    return max(a[0], b[0]) <= min(a[3], b[3]) and max(a[1], b[1]) <= min(a[4], b[4])


def solution(filename) -> int:

    with open(filename) as input:
        bricks = [list(map(int, line.strip().replace("~", ",").split(","))) for line in input.readlines()]
        bricks.sort(key=lambda b: b[2])

    for i, brick in enumerate(bricks):
        max_z = 1
        for check in bricks[:i]:
            if overlaps(brick, check):
                max_z = max(max_z, check[5] + 1)
        brick[5] -= brick[2] - max_z
        brick[2] = max_z

    bricks.sort(key=lambda b: b[2])

    k_supports_v = {i: set() for i in range(len(bricks))}
    v_supports_k = {i: set() for i in range(len(bricks))}

    for j, upper in enumerate(bricks):
        for i, lower in enumerate(bricks[:j]):
            if overlaps(lower, upper) and upper[2] == lower[5] + 1:
                k_supports_v[i].add(j)
                v_supports_k[j].add(i)

    total = 0

    for i in range(len(bricks)):
        q = deque(j for j in k_supports_v[i] if len(v_supports_k[j]) == 1)
        falling = set(q)
        falling.add(i)
        
        while q:
            j = q.popleft()
            for k in k_supports_v[j] - falling:
                if v_supports_k[k] <= falling:
                    q.append(k)
                    falling.add(k)
        
        total += len(falling) - 1

    return total







if __name__ == '__main__':
    print(solution('2023/day-22/input.txt')) 