import sympy


def solution(filename) -> int:
    with open(filename) as input:
        hailstones = [tuple(map(int, line.replace("@", ",").split(","))) for line in input]

    xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

    equations = []

    for i, (sx, sy, sz, vx, vy, vz) in enumerate(hailstones):
        equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
        equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))
        if i < 2:
            continue
        answers = [soln for soln in sympy.solve(equations) if all(x % 1 == 0 for x in soln.values())]
        if len(answers) == 1:
            break
        
    answer = answers[0]

    return answer[xr] + answer[yr] + answer[zr]


if __name__ == '__main__':
    print(solution('2023/day-24/input.txt')) 