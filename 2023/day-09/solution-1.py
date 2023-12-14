
def predict(hist: list) -> int:
    pred = [hist]
    n = len(pred[0])

    while True:
        row = [0] * n
        for i in range(n-len(pred)):
            row[i] = pred[-1][i+1] - pred[-1][i]
        print(row)
        if any(row):
            pred.append(row)
        else:
            break

    c = n - len(pred)
    r = len(pred) - 1
    val = pred[r][c]
    while c < n-1 and r >= 0 :
        val += pred[r-1][c+1] 
        r -= 1
        c += 1

    return val


def solution(filename) -> int:
    result = 0
    with open(filename) as input:
        for line in input.readlines():
            history = list(map(int, line.split()))
            result += predict(history)
    return result


if __name__ == '__main__':
    print(solution('2023/day-09/input.txt'))
    # predict([10, 13, 16, 21, 30, 45])