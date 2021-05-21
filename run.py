#!/usr/bin/env python3
import random
from modules.game_object import GameObject, Robot
from modules.game_screen import GameScreen
import pygame

def createScreen():
    """
    Creates a pygame screen

    :return game: GameScreen object
    :rtype: GameScreen

    """

    game = GameScreen()
    return game

def randomPosition(margin: tuple, objSize: tuple):
    """
    Creates random postion on the GameScreen

    :param margin: margin for random postion
    :type margin: tuple
    :param objSize: size of the object that should be placed
    :type objSize: tuple

    """

    pass 

def moveRobot(
        robotObj: Robot,
        gameScreen: GameScreen,
        direction: int,
        staticObj=None
    ):
    """
    :description: Moves a robot object on the screen, and repairs statit object
        if necessary
    :param robotObj: object to move
    :type robotObj: Robot
    :param gameScreen: Screen where the robot should be moved
    :type gameScreen: GameScreen
    :param direction: can be up, down, left, right
    :param staticObj: optional, static object which shold be refreshed after screen mods
    :type staticObj: if given it is GameObject, None otherwise

    """
    robotObj.move(gameScreen.screenWidth, 
                  gameScreen.screenHeight,
                  direction
    )
    gameScreen.fillScreen()
    robotObj.drawObject(gameScreen)
    if staticObj:
        staticObj.drawObject(gameScreen)
        pygame.time.delay(100)
    pygame.time.delay(100)
    pygame.display.flip()

# def main_test():
    # game = createScreen()
    # dest = GameObject((200,200), (20,20))
    # dest.drawObject(game.screen)
    # robot = Robot((300,300), (20,20), 20)
    # robot.setColor((255,255,255))
    # robot.drawObject(game.screen)
    # run = True
    # while run:
        # pygame.time.delay(10)
        # for event in pygame.event.get():
            # if event.type == pygame.QUIT:
                # run = False
        # robot.move(game.screenWidth, game.screenHeight, 2)
        # game.fillScreen()
        # robot.drawObject(game.screen)
        # dest.drawObject(game.screen)
        # pygame.time.delay(100)
        # pygame.display.flip()
        # # robot.move(game.screenWidth, game.screenHeight, up=True)
        # # game.fillScreen()
        # # robot.drawObject(game.screen)
        # # dest.drawObject(game.screen)
        # # pygame.time.delay(100)
        # pygame.display.flip()
    # print(robot.x, robot.y)
        
def main():
    # create game sceen
    game = createScreen()
    
    # create destination object
    dest = GameObject((200,200), (20,20))
    dest.drawObject(game.screen)
    
    # Create robot object
    robot = Robot((300,300), (20,20), 20)
    robot.setColor((255,255,255))
    robot.drawObject(game.screen)

    run = 1
    while run:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = 0
        
        moveRobot(robot, game.screen, 1, staticObj=dest)

if __name__ == "__main__":
    main()
