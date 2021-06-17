#!/usr/bin/env python3
from random import randint
from modules.game_object import GameObject
from modules.game_screen import GameScreen
import pygame


def pseudoRandomMove(gameScreen: GameScreen, robots: list, dest: GameObject):

    """
    :description: Moves a list of robots randomly, to a main direction. It is the initialization
        of the first generation.
    :param gameScreen: GameScreen object where the robots should be moved
    :type gameScreen: GameScreen
    :param robots: list of Robot objects
    :type robots: list
    :param dest: The destination object. It is necessary for reparing the dest object on the game screen
    :type dest: GameObject
    """

    gameScreen.fillScreen()
    dest.drawObject(gameScreen.screen)
    for robot in robots:
        if len(robot.steps) % 2 == 0:
            robot.move(gameScreen.screenWidth, gameScreen.screenHeight, robot.mainDirection)
        else:
            robot.move(gameScreen.screenWidth, gameScreen.screenHeight, randint(1,4))
        robot.drawObject(gameScreen.screen)

    pygame.display.flip()
    pygame.time.delay(10)


def checkQuitEvent():

    """
    :description: checks for quit event in pygame and quits if necessary
    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()




