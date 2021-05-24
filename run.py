#!/usr/bin/env python3
from modules.game_object import GameObject, Robot
from modules.game_screen import GameScreen
from modules.utilities import genRandomPosition, pseudoRandomMove, checkQuitEvent
import pygame

        
def main():
    # create game sceen
    game = GameScreen(1200,1200)

    # create destination object
    destSize = (30, 30)
    destRandPos = genRandomPosition(
        (game.screenWidth, game.screenHeight),
        destSize
    )
    dest = GameObject(destRandPos, destSize)
    dest.drawObject(game.screen)
    
    # Create robot object
    robotSize = (10, 10)
    robotVelocity = 20
    robotRandPos = genRandomPosition(
        (game.screenWidth, game.screenHeight),
        robotSize
    )

    generation = 0
    populationSize = 50
    population = [Robot(robotRandPos, robotSize, robotVelocity) for _ in range(populationSize)]

    # iCounter = 0
    # for robot in population: 
        # robot.setColor((255, 255, 255))
        # robot.drawObject(game.screen)
        # pseudoRandomMove(robot, game, dest)
        # iCounter += 1
        # pygame.time.delay(2000)


    # Azt kell megoldani, hogy egyszerre tudjam kirajzolni egy populacion belul hogy ki merre megy
    # EZ LESZ AZ, igy igazabol feleslegesen vannak a fuggvenyeim
    # for _ in range(100):
        # game.fillScreen()
        # dest.drawObject(game.screen)
        # for robot in population:
            # robot.move(game.screenWidth, game.screenHeight, randint(1,4))
            # robot.drawObject(game.screen)

        # pygame.display.flip()
        # pygame.time.delay(100)


    # Ez a fo mukodo verzio
    # while True:
        # checkQuitEvent()
    for _ in range(50):
        checkQuitEvent()
        pseudoRandomMove(game, population, dest)
    
    


    # # Running the game
    # run = 1

    # while run:
        # # pygame.time.delay(10)
        # # Check for quit event
        # for event in pygame.event.get():
            # if event.type == pygame.QUIT:
                # run = 0
        # moveRobot(game, randint(1,4), staticObj=dest, robotObjs=population)
        # # pseudoRandomMove(robot, game, dest) 
        # pygame.display.flip()

        
    # Temporary for addational info
    # print(robot.steps)

if __name__ == "__main__":
    main()
