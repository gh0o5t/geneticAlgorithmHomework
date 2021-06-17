#!/usr/bin/env python3
from config import robotSize, robotVelocity, chromosomeLength, initialRobotPosition, populationSize
from modules.game_screen import GameScreen
from modules.game_object import Robot
from random import  choice, sample

def parentSelection(population: list):
    """
    :description: selection for parents
    :param population: the population of Robot objects
    :type population: list 
    :returns: _
    :rtype: list
    """
    concurrentParents = sample(population, 6)
    concurrentParents.sort(key=lambda x: x.fitness, reverse=True)
    return concurrentParents[0]


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
        robotA, robotB = parentSelection(population), parentSelection(population)
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

def mutation(population: list, gameScreen: GameScreen, mutatationFactor: float): 

    """
    :description: mutates some of the individuals.
        The fitness values of the robots must be calculated previously.
        This function modifies mutationFactor percent of the original population
        This function also sorts the population based on fitness value.
    :param population: a list of Robot objects, this list of objects will me modified 
        with this function
    :type population: list
    :param gameScreen: GameScreen object where the population moves, necessary to move the gnomes
        to the right position and calculate the fitness
    :param mutatationFactor: percentage of individuals who will be mutated
    :type mutatationFactor: float
    """

    mutated = set()
    for _ in range(int(populationSize * mutatationFactor)):
        gnome = choice(population)
        # Prevent double mutation on one indiviual
        while gnome in mutated:
            gnome = choice(population)
        gnome.mutate()
        gnome.resetRobotPosition()
        for step in gnome.steps:
            # Moving the gnome to last position to calculate fitness
            gnome.move(gameScreen.screenWidth, gameScreen.screenHeight, step, saveStep=False)

