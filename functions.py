import pygame
from pygame.locals import *
import random

measures = {
    # HD resolution
    'width': 1000,
    'height': 720,
    }
class Tile():
    def __init__(self, value=0, x=None, y=None):
        self.value = value
        # coordinates on the board
        self.x = x # range: (0,3) in 3x3 case
        self.y = y # range: (0,3) in 3x3 case
        self.picture = None
        self.loadPicture()
      
    def loadPicture(self):
        if self.value == 0:
            self.picture = pygame.image.load("images/0.png") 
        elif self.value == 2:
            self.picture = pygame.image.load("images/2.png") 
        elif self.value == 4:
            self.picture = pygame.image.load("images/4.png") 
        elif self.value == 8:
            self.picture = pygame.image.load("images/8.png") 
        elif self.value == 16:
            self.picture = pygame.image.load("images/16.png") 
        elif self.value == 32:
            self.picture = pygame.image.load("images/32.png") 
        elif self.value == 64:
            self.picture = pygame.image.load("images/64.png") 
        elif self.value == 128:
            self.picture = pygame.image.load("images/128.png") 
        elif self.value == 256:
            self.picture = pygame.image.load("images/256.png") 
        elif self.value == 512:
            self.picture = pygame.image.load("images/512.png") 
        elif self.value == 1024:
            self.picture = pygame.image.load("images/1024.png") 
        elif self.value == 2048:
            self.picture = pygame.image.load("images/2048.png") 


class Board():
    def __init__(self, w=None, h=None):
        self.w = w
        self.h = h
        self.board = [[Tile(0, x, y) for y in range(h)] for x in range(w)]
        self.addTile()
               
    def countFree(self):
        counter = 0
        for x in range(self.w):
            for y in range(self.h):
                if self.board[x][y].value == 0:
                   counter += 1
        return counter
    
    def updatePic(self):
        [[self.board[x][y].loadPicture() for y in range(self.h)] for x in range(self.w)]
        
    def draw(self, screen):
        sizeOfTile = 127 + 1 
        xShift = measures['width']/2 - (self.w/2) * sizeOfTile
        yShift = measures['height']/2 - (self.h/2) * sizeOfTile
        [[screen.blit(self.board[x][y].picture, (xShift + self.board[x][y].x * (sizeOfTile), yShift + self.board[x][y].y * (sizeOfTile))) for y in range(self.h)] for x in range(self.w)]
    
    def neighbor(self):
        for x in range(self.w - 1):
            for y in range(self.h - 1):
                if self.board[x][y].value == self.board[x][y + 1].value:
                    return True
                if self.board[x][y].value == self.board[x + 1][y].value:
                    return True
        return False

    def ifWin(self):
        if self.countFree() and self.neighbor():
            return True
        else:
            return False
   
    def addTile(self):
        if self.countFree():
            while True:
                x = random.randint(0, self.w - 1)
                y = random.randint(0, self.h - 1)
                if self.board[x][y].value == 0:
                   p = random.randint(0, 100) 
                   if p < 91: # 90% chance for 2
                       self.board[x][y] = Tile(2, x, y)
                       break
                   else: # 10% chance for 4
                       self.board[x][y] = Tile(4, x, y)
                       break
        
class Player():
    def __init__(self, board):
        self.board = board
        self.score = 0
        
    def move(self, direction):
        self.moveBoard(direction)
        self.merge(direction)
        self.moveBoard(direction)
        self.board.updatePic()
    
    def merge(self, direction):
        if direction == "L":
            for x in range(self.board.w - 1):
                for y in range(self.board.h):
                    if self.board.board[x][y].value == self.board.board[x + 1][y].value:
                        self.board.board[x][y].value *= 2
                        self.board.board[x + 1][y] = Tile(0, x + 1, y)
                        self.score += self.board.board[x][y].value
        elif direction == "R":
            for x in range(self.board.w - 1, 0, -1):
                for y in range(self.board.h):
                    if self.board.board[x][y].value == self.board.board[x - 1][y].value:
                        self.board.board[x][y].value *= 2
                        self.board.board[x - 1][y] = Tile(0, x - 1, y)
                        self.score += self.board.board[x][y].value
        elif direction == "U":
            for x in range(self.board.w):
                for y in range(self.board.h - 1):
                    if self.board.board[x][y].value == self.board.board[x][y + 1].value:
                        self.board.board[x][y].value *= 2
                        self.board.board[x][y + 1] = Tile(0, x, y + 1)
                        self.score += self.board.board[x][y].value
        elif direction == "D":
            for x in range(self.board.w):
                    for y in range(self.board.h - 1, 0, -1):
                        if self.board.board[x][y].value == self.board.board[x][y - 1].value:
                            self.board.board[x][y].value *= 2
                            self.board.board[x][y - 1] = Tile(0, x, y - 1)    
                            self.score += self.board.board[x][y].value
    
    def moveBoard(self, direction):
        for _ in range(max(self.board.w, self.board.h)):
            if direction == "L":
                for x in range(self.board.w - 1):
                    for y in range(self.board.h):
                        if self.board.board[x][y].value == 0 and self.board.board[x + 1][y].value != 0:
                            self.board.board[x][y], self.board.board[x + 1][y] = Tile(self.board.board[x + 1][y].value, x, y), Tile(0, x + 1, y)
            elif direction == "R":
                for x in range(self.board.w - 1, 0, -1):
                    for y in range(self.board.h):
                        if self.board.board[x][y].value == 0 and self.board.board[x - 1][y].value != 0:
                            self.board.board[x][y], self.board.board[x - 1][y] = Tile(self.board.board[x - 1][y].value, x, y), Tile(0, x - 1, y)
            elif direction == "U":
                for x in range(self.board.w):
                    for y in range(self.board.h - 1):
                        if self.board.board[x][y].value == 0 and self.board.board[x][y + 1].value != 0:
                            self.board.board[x][y], self.board.board[x][y + 1] = Tile(self.board.board[x][y + 1].value, x, y), Tile(0, x, y + 1)
            elif direction == "D":
                for x in range(self.board.w):
                    for y in range(self.board.h - 1, 0, -1):
                        if self.board.board[x][y].value == 0 and self.board.board[x][y - 1].value != 0:
                            self.board.board[x][y], self.board.board[x][y - 1] = Tile(self.board.board[x][y - 1].value, x, y), Tile(0, x, y - 1)
                            
def chooseSizeOfBoard():
    x = y = 0
    while (int(x) <= 1 or int(y) <= 1):
        print("\nSet size of board")
        print("Width and height has to be greater than 1")
        print("(press enter for default 4x4)")
        x = input("Width: ")
        if x == '': # if Enter, set default size: 4x4
            x = y = 4
            break
        y = input("Height: ")

    return int(x), int(y)
