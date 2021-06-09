#!/usr/bin/env python3
from modules.game_object import GameObject, Robot
from modules.game_screen import GameScreen
from modules.utilities import genRandomPosition, pseudoRandomMove, checkQuitEvent, crossover, mutatePopulation
from modules.utilities import crossover, mutatePopulation
from random import randint
import pygame


# Maybe I should create functions for initialization of the environment

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
    
    # Create default robot object
    robotSize = (10, 10)
    robotVelocity = 10
    robotRandPos = genRandomPosition(
        (game.screenWidth, game.screenHeight),
        robotSize
    )

    # Setting up genetic algorithm specs
    generation = 0

    # Number of steps
    chromosomeLength = 30
   
    # Number of possible solutions/robots
    populationSize = 50

    # Initalizing first generation
    population = [Robot(robotRandPos, robotSize, robotVelocity) for _ in range(populationSize)]
    
    # Best fitness of any individual in the current generation
    bestFitness = None


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
    # Ezzel adott iranyba vannak terelve
    mainDirection = randint(1,4)
    for _ in range(chromosomeLength):
        checkQuitEvent()
        pseudoRandomMove(game, population, dest, mainDirection)

    print("Fitness of parents")
    for robot in population:
        robot.calFitness(dest)
        print(robot.x, robot.y, robot.fitness)

    # print(population[0].steps)
    # print(population[1].steps)
    # child = crossover(population[0], population[1])
    # print(child.steps)
    print("Fitness of children")
    children = crossover(population, game)
    for child in children:
        child.calFitness(dest)
        print(child.x, child.y, child.fitness)
    
    mergedPopulation = population + children
    print(len(population), len(children), len(mergedPopulation))
    mutatePopulation(mergedPopulation, game, round(populationSize * 0.1))

    print("Fitness of merged population")
    for robot in mergedPopulation:
        robot.calFitness(dest)
        print(robot.x, robot.y, robot.fitness)
    


   
    # Ezzel nincsenek adott iranyba terelve
    # for _ in range(100):
        # checkQuitEvent()
        # pseudoRandomMove(game, population, dest)
    


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
