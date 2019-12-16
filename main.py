import functions as fn
import pygame 
from pygame.locals import *
import sys

# game made by bruteforce and in a hurry
# sorry for quality of this code 

def main():
    pygame.init()
    
    x_board, y_board = fn.chooseSizeOfBoard()
    print('x: ' + str(x_board) + ' y: ' + str(y_board))
    board = fn.Board(x_board, y_board)
    player = fn.Player(board)
    moveCounter = 0
    
    screen_size = (fn.measures['width'], fn.measures['height'])
    screen = pygame.display.set_mode(screen_size)

    running = True
    while running:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                print("Game over")
                print("Your score: " + str(player.score))
                print("Numer of moves: " + str(moveCounter))
                running = False
                
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    print("Game over")
                    print("Your score: " + str(player.score))
                    print("Numer of moves: " + str(moveCounter))
                    running = False
                elif event.key == K_LEFT:
                    player.move("L")
                elif event.key == K_RIGHT:
                    player.move("R")
                elif event.key == K_UP:
                    player.move("U")
                elif event.key == K_DOWN:
                    player.move("D")

                moveCounter += 1
                board.addTile()
                board.updatePic()
        
        board.draw(screen)
        if not board.ifWin():
            print("Game over")
            print("Your score: " + str(player.score))
            print("Numer of moves: " + str(moveCounter))
            running = False
        pygame.display.flip()
            
    

if __name__ == '__main__':
    main()
    pygame.quit()