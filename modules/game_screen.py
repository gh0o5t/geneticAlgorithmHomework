#!/usr/bin/env python3
import pygame

class GameScreen:
    def __init__(self):
        pygame.init()

    def setResolution(self, screenWidth=500, screenHeight=500):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

    def setBgColor(self, color=(0,0,0)):
        self.bgColor = color

    def fillScreen(self, color=(0,0,0)):
        self.screen.fill(color) 

    def setScreen(self):
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.fillScreen(self.bgColor)
