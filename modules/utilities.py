#!/usr/bin/env python3
import random
from modules.game_object import  Robot
from modules.game_screen import GameScreen
import pygame

def createScreen(size: tuple, ):
    """
    Creates a pygame screen
    :param size: size of screen
    :type scree: tuple
    :return game: GameScreen object
    :rtype: GameScreen

    """

    game = GameScreen()
    return game

def genRandomPosition(screenSize: tuple, objSize: tuple):
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
    xObjSize = objSize[0]
    yObjSize = objSize[1]

    randomPositionX = random.randint(0, xMargin)
    randomPositionY = random.randint(0, yMargin)

    if randomPositionX + xObjSize > xMargin:
        randomPositionX = xMargin - xObjSize
   
    if randomPositionY + yObjSize > yMargin:
        randomPositionY = yMargin - yObjSize
    
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
    pygame.display.flip()

