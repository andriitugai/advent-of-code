import math


def solution(filename: str) -> int:
    with open(filename) as input:
        times = list(map(int, input.readline().split(":")[1].split()))
        distances = list(map(int, input.readline().split(":")[1].split()))

        print(times)
        print(distances)
        solutions = []

        result = 1
        for t, d in zip(times, distances):
            s1 = (t - math.sqrt(t * t - 4 * d)) / 2
            if s1 == round(s1, 0):
                s1 = int(s1) + 1
            else:
                s1 = math.ceil(s1)

            s2 = (t + math.sqrt(t * t - 4 * d)) / 2
            if s2 == round(s2, 0):
                s2 = int(s2) - 1
            else:
                s2 = math.floor(s2)

            print(s1, s2, s2 - s1 + 1)
            result *= (s2 - s1 + 1)

        return result


if __name__ == '__main__':
    print(solution('2023/day-06/input.txt'))