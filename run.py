#!/usr/bin/env python3
from modules.game_object import GameObject, Robot
from modules.game_screen import GameScreen
from modules.utilities import genRandomPosition,  moveRobot 
import pygame


        
def main():
    # create game sceen
    game = GameScreen(1200,1200)

    
    # create destination object
    destSize = (20, 20)
    destRandPos = genRandomPosition(
        (game.screenWidth, game.screenHeight),
        destSize
    )
    dest = GameObject(destRandPos, destSize)
    dest.drawObject(game.screen)
    
    # Create robot object
    robotSize = (10, 10)
    robotRandPos = genRandomPosition(
        (game.screenWidth, game.screenHeight),
        robotSize
    )
    robot = Robot(robotRandPos, robotSize, 15)
    robot.setColor((255, 255, 255))
    robot.drawObject(game.screen)

    # Running the game
    run = 1
    while run:
        # pygame.time.delay(10)
        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = 0
        pygame.display.flip()
        moveRobot(robot,game, 1, dest)

        
    # Temporary for addational info
    print(robot.x, robot.y)
    # print(robot.steps)

if __name__ == "__main__":
    main()
