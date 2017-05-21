


def right_check(board, x, y, stone):
    enemy = not(stone)
    if x<=5 and board[y][x+1] == enemy:
        for k in range(x+2,8):
            if board[y][k] == stone:
                return True
            elif board[y][k] == None:
                break
            return False

def left_check(board, x, y, stone):
    enemy = not(stone)
    if x>=2 and board[y][x-1] == enemy:
        for k in range(x-2,-1,-1):
            if board[y][k] == stone:
                return True
            elif board[y][k] == None:
                break
            return False

def up_check(board, x, y, stone):
    enemy = not(stone)
    if y>=2 and board[y-1][x] == enemy:
        for k in range(y-2,-1,-1):
            if board[k][x] == stone:
                return True
            elif board[k][x] == None:
                break
            return False

def down_check(board, x, y, stone):
    enemy = not(stone)
    if y<=5 and board[y+1][x] == enemy:
        for k in range(y+2,8):
            if board[k][x] == stone:
                return True
            elif board[k][x] == None:
                break
            return False

def right_up_check(board, x, y, stone):
    enemy = not(stone)
    if x<=5 and y>=2 and board[y-1][x+1] == enemy:
        k=2
        while x+k<8 and y-k>=0:
            if board[y-k][x+k] == stone:
                return True
            elif board[y-k][x+k] == None:
                break
            k+=1
    return False

def right_down_check(board, x, y, stone):
    enemy = not(stone)
    if x<=5 and y<=5 and board[y+1][x+1] == enemy:
        k=2
        while x+k<8 and y+k<8:
            if board[y+k][x+k] == stone:
                return True
            elif board[y+k][x+k] == None:
                break
            k+=1
    return False

def left_up_check(board, x, y, stone):
    enemy = not(stone)
    if x>=2 and y>=2 and board[y-1][x-1] == enemy:
        k=2
        while x+k>=0 and y-k>=0:
            if board[y-k][x-k] == stone:
                return True
            elif board[y-k][x-k] == None:
                break
            k+=1
    return False

def left_down_check(board, x, y, stone):
    enemy = not(stone)
    if x>=2 and y<=5 and board[y+1][x-1] == enemy:
        k=2
        while x+k>=0 and y-k<8:
            if board[y+k][x-k] == stone:
                return True
            elif board[y+k][x-k] == None:
                break
            k+=1
    return False

    
