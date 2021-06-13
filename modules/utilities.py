#!/usr/bin/env python3
from random import randint, choice, sample
from modules.game_object import Robot, GameObject
from modules.game_screen import GameScreen
from config import robotSize, robotVelocity, chromosomeLength, initialRobotPosition
import pygame

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
    pygame.time.delay(10)
    

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
        # Selecting parents randomly
        parents = sample(population, 2)
        robotA, robotB = parents[0], parents[1]
        counter = 0
        # Init child
        child = Robot(initialRobotPosition, robotSize, robotVelocity)
        # Randomly choosing the chromosome of a parent
        for _ in range(chromosomeLength):
            child.steps.append(choice([robotA.steps[counter], robotB.steps[counter]]))
            counter += 1
        # Moving the child to receive the last position for calculating fitness
        for step in child.steps:
            child.move(gameScreen.screenWidth, gameScreen.screenHeight, step, saveStep=False)
        children.append(child)
    return children



def mutatePopulation(mergedPopulation: list, gameScreen: GameScreen, mutatationFactor: int):

    """
    :description: mutates some of the bad fitness individuals. The fitness values of the robots must be
        calculated previously. This modifies the original population worst mutatationFactor amount of members.
        This function also sorts the population based on fitness value.
    :param population: a list of Robot objects, this list of objects will me modified 
        with this function
    :type population: list
    :param gameScreen: GameScreen object where the population moves, necessary to move the gnomes
        to the right position and calculate the fitness
    :param mutatationFactor: number of indiviuals who will be mutatated
    :type mutatationFactor: int
    """

    mergedPopulation.sort(key=lambda x: x.fitness, reverse=True)
    c = 1
    # +1 is needed cuz without it it would mutate 
    #     mutationFactor - 1 amount of individuals
    while c != mutatationFactor + 1:
        gnome = mergedPopulation[-c]
        gnome.mutate()
        for step in gnome.steps:
            gnome.move(gameScreen.screenWidth, gameScreen.screenHeight, step, saveStep=False)
        c += 1

def selection(mergedPopulation: list):

    """
    :description: select best individuals from the population. Size of
        the population will remain the same over the generations. This function should be
        called on a merged (children and parents) and a mutated population.
        Cuz the len of population must be same over the genrations it will remove the worse half
        of the merged population. This function also sort the population based on fitness before
        deletion.
        This fuction modifies the original population. 
    :param mergedPopulation: the merged population which must go through selection
        list of robot objects (children, parents, gnomes)
    :type mergedPopulation: list
    """

    mergedPopulation.sort(key=lambda x: x.fitness, reverse=True)
    n = int(-len(mergedPopulation)/2) 
    del mergedPopulation[n:]

    
    
def checkQuitEvent():
    """
    :description: checks for quit event in pygame and quits if necessary
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()




