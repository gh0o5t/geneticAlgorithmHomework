#!/usr/bin/env python3
import random
from utilities import GameScreen, Object, Robot
import pygame
import time

def createScreen():
    game = GameScreen()
    game.setResolution()
    game.setBgColor()
    game.setScreen()


def main():
    game = GameScreen()
    game.setResolution()
    game.setBgColor()
    game.setScreen()
    dest = Object((200,200), (20,20))
    dest.drawObject(game.screen)
    robot = Robot((300,300), (20,20), 10)
    robot.setColor((255,255,255))
    robot.drawObject(game.screen)
    run = True
    while run:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for step in range(5):
            robot.move(game.screenWidth, game.screenHeight, up=True)
            robot.drawObject(game.screen)
            time.sleep(1)
        pygame.display.update()

        

if __name__ == "__main__":
    main()
