from collections import defaultdict
import re


def solution(filename: str) -> int:
    result = 0
    cards_counter = {}
    num_cards = 0
    pattern = re.compile("^Card \s+(\d+)")

    with open(filename) as input:
        for line in input:
            num_cards += 1
            card, numbers = line.strip().split(":")
            card_num = int(re.findall('[0-9]+', card)[0])

            wn, yn = numbers.split("|")
            wining_numbers = set(wn.strip().split(" "))
            your_numbers = set(yn.strip().split(" "))

            winners = your_numbers.intersection(wining_numbers)
            winners.discard("")
            print(card, "winners:", winners)
            if len(winners) > 0:
                result += 1 << (len(winners)-1)
                for i in range(len(winners)):
                    cards_counter[card_num + i + 1] = cards_counter.get(card_num + i + 1, 1) + cards_counter.get(card_num, 1)

    cards_total = 0
    
    for i in range(1, num_cards+1):
        cards_total += cards_counter.get(i, 1)
    
    return result, cards_total

if __name__ == '__main__':
    print(solution('2023/day-04/input.txt'))