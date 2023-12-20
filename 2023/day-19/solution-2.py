
def solution(filename) -> int:


    def apply_flow(flow, property, value) -> str:
        nonlocal flows
        for rule in flows[flow]:
            if ":" not in rule:
                return rule

            if property == rule[0]:
                comp = rule[1]
                val, dest = rule[2:].split(":")
                v = int(val)
                if comp == "<" and value < v or comp == ">" and value > v:
                    return dest
                
        return flows[flow][-1]


    with open(filename) as input:
        wflows, _ = input.read().split("\n\n")

    flows = dict()
    for wflow in wflows.split("\n"):
        name, wrules = wflow[:-1].split("{")
        rules = wrules.split(",")

        flows[name] = ([], rules.pop())
        for rule in rules:
            comparison, dest = rule.split(":")
            prop = comparison[0]
            cmp = comparison[1]
            value = int(comparison[2:])
            flows[name][0].append((prop, cmp, value, dest))

    def count(ranges, name = "in"):
        if name == "R":
            return 0
        if name == "A":
            product = 1
            for lo, hi in ranges.values():
                product *= hi - lo + 1
            return product
        
        rules, fallback = flows[name]

        total = 0

        for key, cmp, n, target in rules:
            lo, hi = ranges[key]
            if cmp == "<":
                T = (lo, n - 1)
                F = (n, hi)
            else:
                T = (n + 1, hi)
                F = (lo, n)
            if T[0] <= T[1]:
                copy = dict(ranges)
                copy[key] = T
                total += count(copy, target)
            if F[0] <= F[1]:
                ranges = dict(ranges)
                ranges[key] = F
            else:
                break
        else:
            total += count(ranges, fallback)
                
        return total    

    
    return count({prop: (1, 4000) for prop in "xmas"})



if __name__ == '__main__':
    print(solution('2023/day-19/input.txt'))