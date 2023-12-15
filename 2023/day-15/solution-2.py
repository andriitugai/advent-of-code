def getHash(s: str) -> int:
    hash = 0
    for c in s:
        hash = (hash + ord(c)) * 17 % 256
    return hash


def solution(filename) -> int:
    boxes = [[] for _ in range(256)]
    focal_lengths = {}

    with open(filename) as input:
        words = input.read().split(",")


    for word in words:
        if "-" in word:
            label = word[:-1]
            index = getHash(label)
            if label in boxes[index]:
                boxes[index].remove(label)
        else:
            label, length = word.split("=")
            length = int(length)
            
            index = getHash(label)
            if label not in boxes[index]:
                boxes[index].append(label)
                
            focal_lengths[label] = length

    result = 0

    for box_number, box in enumerate(boxes, 1):
        for lens_slot, label in enumerate(box, 1):
            result += box_number * lens_slot * focal_lengths[label]

    return result


if __name__ == '__main__':
    print(solution('2023/day-15/input.txt'))
