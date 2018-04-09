#import time
#import ui2
#t0 = time.time()
answer = []
points = []

class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.toselect = []
        self.value = 0


def rownum(point, sudoku):
    row = set(sudoku[point.y * 9: (point.y + 1) * 9])
    row.remove(0)
    return row


def columnnum(point, sudoku):
    col = []
    for i in range(point.x, 81, 9):
        col.append(sudoku[i])
    column = set(col)
    column.remove(0)
    return column


def blocknum(point, sudoku):
    block_x = point.x // 3
    block_y = point.y // 3
    block = []
    start = block_y * 3 * 9 + block_x * 3
    for i in range(start, start + 3):
        block.append(sudoku[i])
    for i in range(start + 9, start + 3 + 9):
        block.append(sudoku[i])
    for i in range(start + 9 + 9, start + 3 + 9 + 9):
        block.append(sudoku[i])
    block = set(block)
    block.remove(0)
    return block


def pointsinfo(sudoku):
    points = []
    for i in range(81):
        if sudoku[i] == 0:
            p = point(i % 9, i // 9)
            for j in range(1, 10):
                if j not in rownum(p, sudoku) and j not in columnnum(p, sudoku) and j not in blocknum(p, sudoku):
                    p.toselect.append(j)
            points.append(p)
    return points


def trying(point, sudoku):
    for i in point.toselect:
        point.value = i
        if check(point, sudoku):
            sudoku[point.y * 9 + point.x] = point.value
            if len(points) <= 0:
               # t1 = time.time()
               # useTime = t1 - t0
               # printsudoku(sudoku)
                #print('b')
                global answer
                answer = sudoku
                printsudoku(answer)
                # with open('answer.txt', 'w+') as f:
                #     f.write(str(answer))
                #print('use Time: %f s' % (useTime))
                raise Exception
               # exit()
            p2 = points.pop()
            trying(p2, sudoku)
            sudoku[p2.y * 9 + p2.x] = 0
            sudoku[point.y * 9 + point.x] = 0
            p2.value = 0
            points.append(p2)
        else:
            pass


def check(p, sudoku):
    if p.value == 0:
        #print('no answer')
        return False
    if p.value not in rownum(p, sudoku) and p.value not in columnnum(p, sudoku) and p.value not in blocknum(p, sudoku):
        return True
    else:
        return False


def printsudoku(sudoku):
    for i in range(9):
        for j in range(9):
            print('%d ' % (sudoku[i * 9 + j]), end=' ')
        print('')


# '''
# if __name__ == '__main__':
#     ''
#     sudoku = [
#         8, 0, 0, 0, 0, 0, 0, 0, 0,
#         0, 0, 3, 6, 0, 0, 0, 0, 0,
#         0, 7, 0, 0, 9, 0, 2, 0, 0,
#         0, 5, 0, 0, 0, 7, 0, 0, 0,
#         0, 0, 0, 0, 4, 0, 7, 0, 0,
#         0, 0, 0, 1, 0, 5, 0, 3, 0,
#         0, 0, 1, 0, 0, 0, 0, 6, 8,
#         0, 0, 8, 5, 0, 0, 0, 1, 0,
#         0, 9, 0, 0, 0, 0, 4, 0, 0,
#     ]
#     ''
#     ui = ui2.MyUI()
#     ui.initUI()
#     sudoku = ui.data
#    # print(ui.data)
#     ui.root.mainloop()
#     #printsudoku(sudoku)
#     print('')
#     #points = pointsinfo(sudoku)
#     points = pointsinfo(ui.data)
#     point = points.pop()
#     try:
#         #trying(point, sudoku)
#         trying(point, ui.data)
#     except Exception:
#         #printsudoku(answer)
#         print(answer)
#     #printsudoku(sudoku)
#    # print(answer)
#     #ui.root.mainloop()
# '''


