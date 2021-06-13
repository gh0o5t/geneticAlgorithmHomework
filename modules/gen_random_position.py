#!/usr/bin/env python3
from random import randint

# Help function to randomly initalize game object postions
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

    randomPositionX = randint(0, xMargin)
    randomPositionY = randint(0, yMargin)

    if randomPositionX + xObjSize > xMargin:
        randomPositionX = xMargin - xObjSize
   
    if randomPositionY + yObjSize > yMargin:
        randomPositionY = yMargin - yObjSize
    
    randomPosition = (randomPositionX, randomPositionY)

    return randomPosition

