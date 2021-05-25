#!/usr/bin/env python3
import pygame
from modules.game_screen import GameScreen
from math import sqrt

class GameObject:
    def __init__(self, position: tuple, dimension: tuple, color=(255, 0, 0)):
        self.x = position[0]
        self.y = position[1]
        self.width = dimension[0]
        self.height = dimension[1]
        self.color = color 

    def setColor(self, color: tuple):
        self.color = color

    def drawObject(self, screen: GameScreen):
        # screen must be a a GameScreen screen attribute
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

class Robot(GameObject):

    """
    :description: In the genetic algorithm, it acts as an indiviual
    """

    def __init__(self, position: tuple, dimension: tuple, velocity: int, color=(255, 255, 255)):
        GameObject.__init__(self, position, dimension, color) 
        self.velocity = velocity
        # Works as a chromosome of the individual
        self.steps = []
        self.fitness = 0

    def _saveStep(self, step: int):

        """
        :description: saves the steps into self.steps list
        :param step: the step which should be saved, it is a direction
        :type step: int
        """

        self.steps.append(step)

    def move(self, wBorder: int, hBorder: int, direction: int):

        """
        :description: Moes Robot object on the screen
        :param direction: 1: left, 2, right, 3: up, 4: down
        :type direction: int
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
        self._saveStep(direction)


    def mutate(self):

        pass

    def calFitness(self, dest: GameObject):

        """
        :description: calculates the fitness value of a Robot/Individual
        :param dest: the destination of which must be reached
        :type dest: GameObject 

        """
        
        self.fitness = - sqrt(pow((dest.y - self.y), 2) + pow((dest.x - self.x), 2))
