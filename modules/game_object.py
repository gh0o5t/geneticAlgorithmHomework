#!/usr/bin/env python3
import pygame
import random
from modules.game_screen import GameScreen

class GameObject:
    def __init__(self, position: tuple, dimension: tuple):
        self.x = position[0]
        self.y = position[1]
        self.width = dimension[0]
        self.height = dimension[1]
        self.color = (255, 0, 0)

    def setColor(self, color: tuple):
        self.color = color

    def drawObject(self, screen: GameScreen):
        # screen must be a a GameScreen screen attribute
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

class Robot(GameObject):
    def __init__(self, position: tuple, dimension: tuple, velocity: int):
        GameObject.__init__(self, position, dimension)
        self.velocity = velocity
        self.steps = []

    def saveStep(self, step: int):

        """
        :description: saves the step and and the position into self.steps list of dicts
        :param step: the step which shold be saved, it is a direction
        :type step: int
        """

        self.steps.append(
            {
                'direction': step,
                'position': (self.x, self.y)
            }
        )

    def move(self, wBorder: int, hBorder: int, direction: int):

        """
        :description: Moes Robot object on the screen
        :param direction: 1: left, 2, right, 3: up, 4: down
        :type direction: int
        """

        # moving left
        if direction == 1 and self.x > 0:
            self.x -= self.velocity
        # moving right
        if direction == 2 and self.x < wBorder - self.width:
            self.x += self.velocity
        # moving up
        if direction == 3 and self.y > 0:
            self.y -= self.velocity
        # moving down
        if direction == 4 and self.y < hBorder - self.height:
            self.y += self.velocity

        # Saving the steps 
        self.saveStep(direction)

    def randomMove(self):
        pass
