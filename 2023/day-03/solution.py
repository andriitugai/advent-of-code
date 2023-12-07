from collections import namedtuple, defaultdict

Mark = namedtuple("Mark", "char row col")
deltas = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]


def isNotDigit(c: str) -> bool:
        return not ("0" <= c <= "9") and c != "."


def isDigit(c: str) -> bool:
    return "0" <= c <= "9"


def solution(filename: str) -> tuple:
    result = 0
    grid = []
    with open(filename) as input:
        for line in input:
            grid.append(line)

    m, n = len(grid), len(grid[0].strip())

    def checkNbr(r, c) -> set:
        ans = False
        marks = set()
        for dr, dc in deltas:
            if 0 <= r + dr < m and 0 <= c + dc < n:
                marked = isNotDigit(grid[r+dr][c+dc])
                if marked:
                    marks.add(Mark(grid[r+dr][c+dc], r+dr, c+dc))
                ans = ans or marked
        return marks
        
    marks_to_details = defaultdict(list)
    for row in range(m):
        numberNow = False
        curNumber = -1
        isTrueNumber = False
        number_marked_by = set()
        # print(f"Row #: {row} of lenght {len(grid[row])} *************************")
        for col in range(n):
            c = grid[row][col]
            if isDigit(c):
                marks = checkNbr(row, col)
                isTrueNumber = isTrueNumber or bool(marks)
                if numberNow:
                    curNumber = curNumber * 10 + int(c)
                else:
                    curNumber = int(c)
                    numberNow = True
                number_marked_by = number_marked_by.union(marks)
            else:
                if numberNow:
                    numberNow = False
                    # print(curNumber, isTrueNumber, "Marked by:", number_marked_by)
                    if isTrueNumber:
                        result += curNumber
                        for mark_on_detail in number_marked_by:
                            marks_to_details[mark_on_detail].append(curNumber)

                    isTrueNumber = False
                    number_marked_by = set()
            
        if numberNow:
            numberNow = False
            print(curNumber, isTrueNumber)
            if isTrueNumber:
                result += curNumber
                for mark_on_detail in number_marked_by:
                    marks_to_details[mark_on_detail].append(curNumber)

            isTrueNumber = False

    # print(marks_to_details)
    engine = 0
    for k, v in marks_to_details.items():
        if k.char == "*" and len(v) == 2:
            engine += v[0] * v[1]

    return result, engine

if __name__ == '__main__':
    print(solution('2023/day-03/input.txt'))
    
    