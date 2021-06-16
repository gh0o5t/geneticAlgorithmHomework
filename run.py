#!/usr/bin/env python3
from modules.game_object import GameObject, Robot
from modules.game_screen import GameScreen
from modules.utilities import pseudoRandomMove, checkQuitEvent
from modules.ga_utilities import crossover, mutatePopulation, selection
from random import randint
from config import screenWidth, screenHeight, robotSize, robotVelocity, destSize
from config import initialRobotPosition, destPosition
from config import populationSize, chromosomeLength, maxGeneration
import pygame



def initGame():
    """
    :description: initalizes the necessary game objects
    :returns _: a the game and destination object
    :rtype: tuple 
    """
    game = GameScreen(screenWidth, screenHeight)
    dest = GameObject(destPosition, destSize)
    dest.drawObject(game.screen)

    return {'game': game, 'dest': dest}



def main():
    initializedGame = initGame()

    game = initializedGame['game']
    dest = initializedGame['dest']

    # Initalizing generation number
    generation = 0

    # Initalizing first generation
    population = [Robot(initialRobotPosition, robotSize, robotVelocity) for _ in range(populationSize)]

    # Best fitness of any individual in the current generation
    bestFitness = None

    # Initalizing main direction of robots
    # Only the first generation has the main direction set
    for robot in population:
        robot.mainDirection = randint(1,4)

        # Randomly moving first generation
    for _ in range(chromosomeLength):
        checkQuitEvent()
        pseudoRandomMove(game, population, dest)

    c = 0
    while c != maxGeneration:
        # Delaying pygame between genration
        pygame.time.delay(10)

        # Reset screen for the current generation
        game.fillScreen()
        dest.drawObject(game.screen)
        pygame.display.flip()
        pygame.time.delay(300)

        # Crossover of population
        children = crossover(population, game)

        # Calculating fitness of children and parents of current generation
        mergedPopulation = population + children
        [robot.calFitness(dest) for robot in mergedPopulation]

        # Mutatation of last 10% of the population.
        mutatePopulation(mergedPopulation, game, round(populationSize * 0.1))

        # Recalculating the fitness after mutation
        [robot.calFitness(dest) for robot in mergedPopulation]

        # Selection of population (sorts the population)
        selection(mergedPopulation)

        # Removing unused objects, creating new population
        del children
        del population
        population = mergedPopulation
        del mergedPopulation


        # Increasing generation number of population and individuals
        generation += 1
        for robot in population:
            robot.generation += 1
        print("Current generation: {}".format(generation))
        print("Best fitness: {}".format(population[0].fitness))

        # Reseting starting position to draw out population
        [robot.resetRobotPosition() for robot in population]

        # Drawing population
        for s in range(chromosomeLength):
            checkQuitEvent()
            game.fillScreen()
            dest.drawObject(game.screen)
            for robot in population:
                robot.move(game.screenWidth, game.screenHeight, robot.steps[s], saveStep=False)
                robot.drawObject(game.screen)
            pygame.display.flip()
            pygame.time.delay(10)

            # Checking if any of the individuals reached the destination
            for robot in population:
                if robot.rect.colliderect(dest.rect):
                    return 0

        c += 1

if __name__ == "__main__":
    main()
