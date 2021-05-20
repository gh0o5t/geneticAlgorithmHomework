#!/usr/bin/env python3
import pygame

class GameScreen:
    def __init__(self):
        pygame.init()

    def setResolution(self, screenWidth=500, screenHeight=500):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

    def setBgColor(self, rgb=(0,0,0)):
        self.bgColor = rgb

    def setScreen(self):
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.screen.fill(self.bgColor)

        

class Object:
    def __init__(self, position, dimension):
        self.x = position[0]
        self.y = position[1]
        self.width = dimension[0]
        self.height = dimension[1]
        self.color = (255, 0, 0)

    def setColor(self, color):
        self.color = color

    def drawObject(self, screen):
        # screen must be a a GameScreen screen attribute
        pygame.draw.rect(screen, self.color , (self.x, self.y, self.width, self.height))

class Robot(Object):
    def __init__(self, position, dimension, velocity):
        Object.__init__(self, position, dimension)
        self.velocity = velocity

    def move(self, wBorder, hBorder, up=False, down=False, left=False, right=False):
        # moving left
        if left and self.x > 0:
            self.x -= self.velocity
        # moving right
        if right and self.x < wBorder - self.width:
            self.x += self.velocity
        # moving up
        if up and self.y > 0:
            self.y -= self.velocity
        # moving down
        if down and self.y < hBorder - self.height:
            self.y += self.velocity
        



