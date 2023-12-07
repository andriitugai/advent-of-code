
def solution(filename: str, load)-> tuple:
    result = 0
    total_power = 0
    with open(filename) as input:
        for line in input:
            game_num, game = line.strip().split(':')
            _, sid = game_num.split()
            id = int(sid)
            game_power = {'red': 0, 'green': 0, 'blue': 0}

            sets = game.split(";")
            isValid = True
            
            for s in sets:
                kube_info = s.split(",")
                
                for info in kube_info:
                    n, color = info.strip().split(" ")
                    num = int(n)

                    if num > game_power[color]:
                        game_power[color] = num

                    if load[color] < num:
                        isValid = False

            if isValid:
                result += id
            
            power = game_power['red'] * game_power['green'] * game_power['blue']
            total_power += power

    return result, total_power


if __name__ == '__main__':

    load = {'red': 12, 'green': 13, 'blue': 14}

    ans, power = solution('2023/day-02/input_1.txt', load)
    print(f"Answer is {ans}, total power is {power}")