def solution(filename) -> int:
    dirs = { "U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    points = [(0, 0)]

    b = 0 # interrial points

    with open(filename) as input:
        for line in input.readlines():
            dir, steps, color = line.strip().split()
            steps = int(steps)
            b += steps
            points.append((points[-1][0] + dirs[dir][0] * steps, points[-1][1] + dirs[dir][1] * steps))

    A = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))) // 2
    i = A - b // 2 + 1

    return i + b



if __name__ == '__main__':
    print(solution('2023/day-18/input.txt'))