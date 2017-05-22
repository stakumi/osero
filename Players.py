import random

class HumanPlayer:

    def __init__(self,s):
        self._stone = s

    def input_stone(self,board):
        while(True):
            if self._stone == True:
                print("[O player input]>",end="")
            else:
                print("[X player input]>",end="")
            try:
                x,y = [int(i) for i in input().split()] 
                break;
            except:
                print("---Syntax Error!---")
        return x,y

class RandomPlayer:

    def __init__(self,s):
        self._stone = s

    def input_stone(self, board):
        x=random.randint(0,8)
        y=random.randint(0,8)
        return x,y
