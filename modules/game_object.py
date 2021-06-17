#!/usr/bin/env python3
import pygame
from modules.game_screen import GameScreen
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from config import initialRobotPosition, chromosomeLength, geneMutationFactor
from math import sqrt
from random import randint

class GameObject:

    """
    :description: object on the game screen
    """

    def __init__(self, position: tuple, dimension: tuple, color=(255, 0, 0)):
        self.x = position[0]
        self.y = position[1]
        self.width = dimension[0]
        self.height = dimension[1]
        self.color = color 
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def setColor(self, color: tuple):

        """
        :description: sets the color of GameObject
        :param color: rgb color 
        :type color: tuple
        """
         
        self.color = color

    def modifyPositon(self, newPosition):

        """
        :description: modifies the x and y values of a GameObject
        :param newPosition: new position of the GameObject
        :type newPosition: tuple
        """

        self.x = newPosition[0]
        self.y = newPosition[1]

    def drawObject(self, screen: GameScreen):
        # screen must be a a GameScreen screen attribute
        # pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        self.rect.x = self.x
        self.rect.y = self.y
        pygame.draw.rect(screen, self.color, self.rect)

class Robot(GameObject):

    """
    :description: In the genetic algorithm, it acts as an indiviual
    """

    def __init__(self, position: tuple, dimension: tuple, velocity: int, color=(255, 255, 255)):
        GameObject.__init__(self, position, dimension, color) 
        self.velocity = velocity
        # Works as a chromosome of the individual
        self.steps = []
        self.fitness = None
        self.mainDirection = 0

    def _saveStep(self, step: int):

        """
        :description: saves the steps into self.steps list
        :param step: the step which should be saved, it is a direction
        :type step: int
        """

        self.steps.append(step)


    def resetRobotPosition(self):

        """
        :description: resets the robot x and y coordinates. It should be used after
            calculating the fitness of the robot. It is necessary for having the same
            starting position for all the robots in all of the generations.
        """

        self.x = initialRobotPosition[0]
        self.y = initialRobotPosition[1]


    def move(self, wBorder: int, hBorder: int, direction: int, saveStep = True):

        """
        :description: Moves Robot object on the screen, calls self.saveStep if necessary.
        :param direction: 1: left, 2, right, 3: up, 4: down
        :type direction: int
        :param wBorder: width of screen where robot moves
        :type wBorder: int
        :param hBorder: height of screen where robot moves
        :type hBorder: int
        :param saveStep: if True saves the step of the robot to steps attribute, otherwise not.
            Basically if step list is emtpy it should be true, fale otherwise.
        :type saveStep: bool
        """

        # moving left
        if direction == 1 and self.x > 0:
            self.x -= self.velocity
            if self.x < 0:
                self.x = 0
        # moving right
        if direction == 2 and self.x < wBorder - self.width:
            self.x += self.velocity
            if self.x + self.width > wBorder:
                self.x = wBorder - self.width
        # moving up
        if direction == 3 and self.y > 0:
            self.y -= self.velocity
            if self.y < 0:
                self.y = 0
        # moving down
        if direction == 4 and self.y < hBorder - self.height:
            self.y += self.velocity
            if self.y + self.height > hBorder:
                self.y = hBorder - self.height

        # Saving the steps 
        if saveStep:
            self._saveStep(direction)

    def mutate(self, factor=geneMutationFactor):

        """
        :description: mutates the robot, randomly changes the genes. 
        :param factor: This percent of genes will be modified int the chromosome by mutation.
        :type factor: float
        """

        modifiedIndex = []
        for _ in range(int(chromosomeLength * factor)):
            index = randint(0, chromosomeLength -1 )
            while index in modifiedIndex:
                index = randint(0, chromosomeLength - 1)
            modifiedIndex.append(index)
            self.steps[index] = randint(1,4)
            
    def calFitness(self, dest: GameObject):

        """
        :description: calculates the fitness value of a robot
        :param dest: the destination which must be reached
        :type dest: GameObject 
        """

        self.fitness = - sqrt(pow((dest.y - self.y), 2) + pow((dest.x - self.x), 2))


