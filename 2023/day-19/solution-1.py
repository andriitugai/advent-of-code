
def solution(filename) -> int:


    def apply_flow(flow, part) -> str:
        nonlocal flows
        for rule in flows[flow]:
            if ":" not in rule:
                return rule
            prop = rule[0]
            comp = rule[1]
            val, dest = rule[2:].split(":")
            value = int(val)
            if comp == "<" and part[prop] < value or comp == ">" and part[prop] > value:
                return dest


    with open(filename) as input:
        wflows, details = input.read().split("\n\n")

    flows = dict()
    for wflow in wflows.split("\n"):
        name, wrules = wflow[:-1].split("{")
        flows[name] = wrules.split(",")
        
    # for item in flows.items():
    #     print(item)

    parts = []
    for detail in details.split("\n"):
        part = dict()
        for d in detail[1:-1].split(","):
            property, val = d.split("=")
            part[property] = int(val)
        # print(part)
        parts.append(part)

    accepted = []
    rejected = []

    for part in parts:
        flow = "in"
        while flow not in "AR":
            flow = apply_flow(flow, part)

        if flow == "A":
            accepted.append(part)
        else:
            rejected.append(part)

    result = 0
    for part in accepted:
        for _, val in part.items():
            result += val

    return result



if __name__ == '__main__':
    print(solution('2023/day-19/input.txt'))