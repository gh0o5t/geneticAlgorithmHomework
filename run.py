#!/usr/bin/env python3
import random
from modules.game_object import GameObject, Robot
from modules.game_screen import GameScreen
import pygame

def createScreen():
    game = GameScreen()
    game.setResolution()
    game.setBgColor()
    game.setScreen()
    return game

def randomPosition(margin):
    pass 


def main_test():
    game = createScreen()
    dest = GameObject((200,200), (20,20))
    dest.drawObject(game.screen)
    robot = Robot((300,300), (20,20), 20)
    robot.setColor((255,255,255))
    robot.drawObject(game.screen)
    run = True
    while run:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        robot.move(game.screenWidth, game.screenHeight, right=True)
        game.fillScreen()
        robot.drawObject(game.screen)
        dest.drawObject(game.screen)
        pygame.time.delay(100)
        pygame.display.flip()
        # robot.move(game.screenWidth, game.screenHeight, up=True)
        # game.fillScreen()
        # robot.drawObject(game.screen)
        # dest.drawObject(game.screen)
        # pygame.time.delay(100)
        pygame.display.flip()
    print(robot.x, robot.y)
        
def main():
    # create game sceen
    game = createScreen()
    
    # create destination object
    dest = GameObject 
    
    # create initial population
    pass

if __name__ == "__main__":
    main_test()
