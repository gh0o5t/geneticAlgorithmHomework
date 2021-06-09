#!/usr/bin/env python3
from random import randint, choice, sample
from modules.game_object import Robot, GameObject
from modules.game_screen import GameScreen
import pygame


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

# Depricated
# def moveRobot(
        # robotObj: Robot,
        # gameScreen: GameScreen,
        # direction: int,
        # staticObj=None
    # ):

    # """
    # :description: Moves a robot object on the screen, and repairs static object
        # if necessary
    # :param robotObj: object to move
    # :type robotObj: Robot to move
    # :param gameScreen: Screen where the robot should be moved
    # :type gameScreen: GameScreen
    # :param direction: can be up, down, left, right
    # :param staticObj: optional, static object which shold be refreshed after screen mods
    # :type staticObj: if given it is GameObject, None otherwise

    # """

    # robotObj.move(gameScreen.screenWidth, 
                  # gameScreen.screenHeight,
                  # direction
    # )
    # gameScreen.fillScreen()
    # robotObj.drawObject(gameScreen.screen)
    # if staticObj:
        # staticObj.drawObject(gameScreen.screen)
    # pygame.time.delay(100)
    # pygame.display.flip()


# Depricated
# def pseudoRandomMove(
    # robotObj: Robot,
    # gameScreen: GameScreen,
    # staticObj=None,
    # maxStep = 50
# ):
    # """
    # :description: wrapper func which moves the robot with pseudo random steps, makes
        # the robot to go into a given direction until ... 
        # Other parameters are same as in moveRobot
    # :param maxStep: maximum step count
    # :type maxStep: int
    # """
    # mainDirection = randint(1, 4)
    # counter = 0
    # run = 1
    # while run:
        # for event in pygame.event.get():
            # if event.type == pygame.QUIT:
                # pygame.quit()
                # quit()
        # if counter > maxStep:
            # break
        # if counter % 3 == 0:
            # moveRobot(robotObj, gameScreen, mainDirection, staticObj)
        # else:
            # moveRobot(robotObj, gameScreen, randint(1, 4), staticObj)
        # counter += 1

def pseudoRandomMove(gameScreen: GameScreen, robots: list, dest: GameObject, mainDirection):
    """
    :description: Moves a list of robots randomly, to a main direction. It is the initialization
        of the first generation. List of robots is the population
    :param gameScreen: GameScreen object where the robots should be moved
    :type gameScreen: GameScreen
    :param robots: list of Robot objects
    :type robots: list
    :param dest: The destination object. It is necessary for reparing the dest object
    :type dest: GameObject

    """
    gameScreen.fillScreen()
    dest.drawObject(gameScreen.screen)
    for robot in robots:
        if len(robot.steps) == 0:
            robot.move(gameScreen.screenWidth, gameScreen.screenHeight, mainDirection)
        if len(robot.steps) > 0 and len(robot.steps) % 2 == 0:
            # mainDirection = robot.steps[0]['direction']
            robot.move(gameScreen.screenWidth, gameScreen.screenHeight, mainDirection)
        else:
            robot.move(gameScreen.screenWidth, gameScreen.screenHeight, randint(1,4))
        robot.drawObject(gameScreen.screen)

    pygame.display.flip()
    pygame.time.delay(100)
    

# Ez nem tereli oket semerre
# def pseudoRandomMove(gameScreen: GameScreen, robots: list, dest: GameObject):
    # """
    # :description: Moves a list of robots randomly, to a main direction. It is the initialization
        # of the first generation. List of robots is the population
    # :param gameScreen: GameScreen object where the robots should be moved
    # :type gameScreen: GameScreen
    # :param robots: list of Robot objects
    # :type robots: list
    # :param dest: The destination object. It is necessary for reparing the dest object

    # """
    # gameScreen.fillScreen()
    # dest.drawObject(gameScreen.screen)
    # for robot in robots:
        # robot.move(gameScreen.screenWidth, gameScreen.screenHeight, randint(1,4))
        # robot.drawObject(gameScreen.screen)

    # pygame.display.flip()
    # pygame.time.delay(100)

def crossover(population: list, gameScreen: GameScreen):

    """
    :description: produces the children for the next generation. The number of childen is equal
        to the number of parents
    :param population: a list of Robot objects
    :type population: list
    :param gameScreen: GameScreen object where the population moves, necessary to move the children
        to the right position and calculate the fitness
    :return children: a list of crossed robot objects
    :rtype: list
    """

    children = []

    for _ in range(len(population)):
        parents = sample(population, 2)
        robotA, robotB = parents[0], parents[1]
        # The chromosomeLength is same for A and B
        chromosomeLength = len(robotA.steps)
        counter = 0
        # These are the same values for robotA and robotB
        child = Robot(robotA.initialPosition, (robotA.width, robotA.height), robotA.velocity)
        for _ in range(chromosomeLength):
            child.steps.append(choice([robotA.steps[counter], robotB.steps[counter]]))
            counter += 1
        for step in child.steps:
            child.move(gameScreen.screenWidth, gameScreen.screenHeight, step, saveStep=False)
        children.append(child)
    return children



def mutatePopulation(population: list, gameScreen: GameScreen, mutatationFactor: int):

    """
    :description: mutates some of the bad fitness individuals. The fitness values of the robots must be
        calculated previously. This modifies the original population worst mutatationFactor amount of members.
    :param population: a list of Robot objects, this list of objects will me modified 
        with this function
    :type population: list
    :param gameScreen: GameScreen object where the population moves, necessary to move the gnomes
        to the right position and calculate the fitness
    :param mutatationFactor: number of indiviuals who will be mutatated
    :type mutatationFactor: int
    """

    population.sort(key=lambda x: x.fitness, reverse=True)
    c = 1
    # +1 is needed cuz without it it would mutate 
    #     mutationFactor - 1 amount of individuals
    while c != mutatationFactor + 1:
        gnome = population[-c]
        gnome.mutate()
        for step in gnome.steps:
            gnome.move(gameScreen.screenWidth, gameScreen.screenHeight, step, saveStep=False)
        c += 1

    
    
def checkQuitEvent():
    """
    :description: checks for quit event in pygame and quits if necessary
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
















