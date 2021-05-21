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

def genRandomPosition(screenSize: tuple, objSize: int):
    """
    Creates random postion on the GameScreen

    :param screenSize: size of screen 
    :type screenSize: tuple
    :param objSize: size of the object that should be placed
    :type objSize: int
    :return randomPosition: random x and y coordinates
    :rtype: tuple

    """

    xMargin = screenSize[0]
    yMargin = screenSize[1]

    randomPositionX = random.randint(0, xMargin)
    randomPositionY = random.randint(0, yMargin)

    if randomPositionX + objSize > xMargin:
        randomPositionX = xMargin - objSize
   
    if randomPositionY + objSize > yMargin:
        randomPositionY = yMargin - objSize
    
    randomPosition = (randomPositionX, randomPositionY)

    return randomPosition

def moveRobot(
        robotObj: Robot,
        gameScreen: GameScreen,
        direction: int,
        staticObj=None
    ):
    """
    :description: Moves a robot object on the screen, and repairs static object
        if necessary
    :param robotObj: object to move
    :type robotObj: Robot to move
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
    robotObj.drawObject(gameScreen.screen)
    if staticObj:
        staticObj.drawObject(gameScreen.screen)
        pygame.time.delay(100)
    pygame.time.delay(100)
    pygame.display.flip()

        
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

    # Running the game
    run = 1
    while run:
        pygame.time.delay(10)
        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = 0
        pygame.display.flip()
        

    # Temporary for addational info
    print(robot.x, robot.y)

if __name__ == "__main__":
    main()
