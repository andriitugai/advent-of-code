import functools
from collections import defaultdict

strength = {
        '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, 
        '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13
    }

def getType(hand: str) -> int:
    h = defaultdict(int)
    for c in hand :
        h[c] += 1
    v = sorted(h.values(), reverse=True)
    if v[0] == 1:
        return 1        # High card
    elif v[0] == 2:
        if v[1] == 2:
            return 3    # Two pair
        return 2        # One pair
    elif v[0] == 3:
        if v[1] == 2:
            return 5    # Full House
        return 4        # Three of a kind
    elif v[0] == 4:
        return 6        # Four of a kind
    return 7            # Five of a kind


def compare(cards1: str, cards2: str) -> int:
    hand1, hand2 = cards1[0], cards2[0]
    t1, t2 = getType(hand1), getType(hand2)
    if t1 < t2 :
        return -1
    elif t1 > t2:
        return 1
    else:
        for i in range(5):
            if strength[hand1[i]] != strength[hand2[i]]:
                return -1 if strength[hand1[i]] < strength[hand2[i]] else 1
    return 0



def solution(filename: str) -> int:
    hands = []
    with open(filename) as input:
        for line in input.readlines():
            hand, bid = line.split()
            hands.append((hand, int(bid)))

    result = 0
    for i, hand in enumerate(sorted(hands, key=functools.cmp_to_key(compare)), start=1):
        _, bid = hand
        result += bid * i

    return result


if __name__ == '__main__':
    print(solution('2023/day-07/input.txt'))