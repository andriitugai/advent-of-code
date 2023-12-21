from collections import deque


class Module:
    def __init__(self, name, type, outputs) -> None:
        self.name = name
        self.type = type
        self.outputs = outputs

        if type == "%":
            self.memory = "off"
        else:
            self.memory = {}

    def __repr__(self) -> str:
        return f"{self.name} (type={self.type}): {','.join(self.outputs)} "


def solution(filename: str) -> int:
    modules = {}
    broadcast_targets = []

    with open(filename) as input:
        for line in input.readlines():
            left, right = line.strip().split(" -> ")
            outputs = right.split(", ")
            if left == "broadcaster":
                broadcast_targets = outputs
            else:
                type = left[0]
                name = left[1:]
                modules[name] = Module(name, type, outputs)

    for name, module in modules.items():
        for output in module.outputs:
            if output in modules and modules[output].type == "&":
                modules[output].memory[name] = "lo"

    low = high = 0
    for _ in range(1000):
        low += 1
        q = deque([("broadcaster", x, "lo") for x in broadcast_targets])
    
        while q:
            origin, target, pulse = q.popleft()

            if pulse == "lo":
                low += 1
            else:
                high += 1
            
            if target not in modules:
                continue
            
            module = modules[target]
            
            if module.type == "%":
                if pulse == "lo":
                    module.memory = "on" if module.memory == "off" else "off"
                    outgoing = "hi" if module.memory == "on" else "lo"
                    for x in module.outputs:
                        q.append((module.name, x, outgoing))
            else:
                module.memory[origin] = pulse
                outgoing = "lo" if all(x == "hi" for x in module.memory.values()) else "hi"
                for x in module.outputs:
                    q.append((module.name, x, outgoing))

    return low * high


if __name__ == '__main__':
    print(solution('2023/day-20/input.txt'))