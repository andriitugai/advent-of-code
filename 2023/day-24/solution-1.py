testingAreaStart = tas = 200000000000000
testingAreaEnd = tae = 400000000000000

tas = 7
tae = 27

tas = 200000000000000
tae = 400000000000000

class HailStone:
    def __init__(self, x0, y0, z0, vx, vy, vz) -> None:
        
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.vx = vx
        self.vy = vy
        self.vz = vz

        self.a = vy
        self.b = -vx
        self.c = vy * x0 - vx * y0

    def __repr__(self) -> str:
        return f"HailStone a={self.a}, b={self.b}, c={self.c}"

def solution(filename) -> int:
    hails = []
    result = 0

    with open(filename) as input:
        for line in input:
            hails.append(HailStone(*map(int, line.replace("@", ",").split(","))))

    # for hs in hails:
    #     print(hs)

    # print(len(hails))    
    for i, hs1 in enumerate(hails):
        for hs2 in hails[:i]:
            a1, b1, c1 = hs1.a, hs1.b, hs1.c
            a2, b2, c2 = hs2.a, hs2.b, hs2.c

            if a1 * b2 == a2 * b1:
                continue

            x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
            y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)
            if tas <= x <= tae and tas <= y <= tae:
                if all((x - hs.x0) * hs.vx >= 0 and (y - hs.y0) * hs.vy >= 0 for hs in (hs1, hs2)):
                    result += 1

    return result
