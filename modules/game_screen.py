#!/usr/bin/env python3
import pygame

class GameScreen:
    def __init__(
            self,
            screenWidth = 500,
            screenHeight = 500,
            bgColor = (0,0,0),
        ):
        pygame.init()
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.bgColor = bgColor
        self.setScreen()

    # def setResolution(self, screenWidth: int, screenHeight: int):
        # self.screenWidth = screenWidth
        # self.screenHeight = screenHeight

    # def setBgColor(self, color: tuple):
        # self.bgColor = color

    def fillScreen(self, color=(0,0,0)):
        self.screen.fill(color) 

    def setScreen(self):
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.fillScreen(self.bgColor)
