import sys  # !/usr/bin/python


# Head ends here

def dist(x1, y1, board):            #to find the coordinates of the nearest dirty cell using Manhattan Distance
    dis = sys.maxsize
    rr,rc=0,0
    for i in range(5):
        for j in range(5):
            temp = (abs(x1 - i) +
                    abs(y1 - j))
            if board[i][j] == 'd' and temp < dis:
                dis = temp
                rr = i
                rc = j
    return rr, rc


def next_move(posr, posc, board):
    move = ""
    r, c = dist(posr, posc, board)
    if c < posc:
        print("LEFT")
    elif c > posc:
        print("RIGHT")
    elif r < posr:
        print("UP")
    elif r > posr:
        print("DOWN")
    elif posr == r and posc == c:
        print("CLEAN")


# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)