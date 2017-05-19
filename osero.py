class OseroBoard:

    def __init__(self):
        self._board = [[None for i in range(0,8)] for j in range(0,8)]
        self._board[3][3] = True
        self._board[3][4] = False
        self._board[4][3] = False
        self._board[4][4] = True
        self._turn = False
        self._count = 0
        self._winner = None

    def print_board(self):
        print("  0 1 2 3 4 5 6 7")
        for x in range(0,8):
            print(x,end="")
            for y in range(0,8):
                print(self.xy_to_stone(x,y),end="")
            print("")

    def xy_to_stone(self,x,y):
        if self._board[x][y] == False:
            return(" X")
        elif self._board[x][y] == True:
            return(" O")
        else:
            return(" -")

    def next_turn(self):
        self._turn = not(self._turn)
        self._count += 1
            
    def put_stone(self,stone):
        if self._turn :
            print("[O player input]>",end="")
        else:
            print("[X player input]>",end="")
        y,x = [int(i) for i in input().split()]
        self._board[x][y] = stone
        self.print_board()

    def play(self):
        while self._winner is None:
            self.put_stone(self._turn)
            self.next_turn()


if __name__ == "__main__":
    b = OseroBoard()
    b.print_board()
    b.play()