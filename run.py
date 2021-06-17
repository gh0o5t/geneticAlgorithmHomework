#!/usr/bin/env python3
from modules.game_object import GameObject, Robot
from modules.game_screen import GameScreen
from modules.utilities import pseudoRandomMove, checkQuitEvent
from modules.ga_utilities import crossover, mutation
from random import randint
from config import screenWidth, screenHeight, robotSize, robotVelocity, destSize
from config import initialRobotPosition, destPosition
from config import populationSize, chromosomeLength, maxGeneration 
from config import populationMutationFactor
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

    # Initalizing 0. generation
    population = [Robot(initialRobotPosition, robotSize, robotVelocity) for _ in range(populationSize)]

    # Initalizing main direction of robots
    # Only the first generation has the main direction set
    for robot in population:
        robot.mainDirection = randint(1,4)

    # Randomly moving first generation
    for _ in range(chromosomeLength):
        checkQuitEvent()
        pseudoRandomMove(game, population, dest)

    # Calculating the fitness of 0. generation
    [robot.calFitness(dest) for robot in population]

    c = 0
    while c != maxGeneration:
        # Delaying pygame between generations
        pygame.time.delay(10)

        # Reset screen for the current generation
        game.fillScreen()
        dest.drawObject(game.screen)
        pygame.display.flip()
        pygame.time.delay(300)

        # Crossover of population
        children = crossover(population, game)

        # Calculating the fitness of children
        [robot.calFitness(dest) for robot in children]

        # Mutation of newly created individuals
        mutation(children, game, populationMutationFactor)
        
        # Recalculating fitness of new generation with gnomes
        [robot.calFitness(dest) for robot in children]

        # New generation
        population = children

        # Increasing generation number of population
        generation += 1
        print("Current generation: {}".format(generation))
        
        # Print best fitness of population
        fitnessValues = set()
        [fitnessValues.add(robot.fitness) for robot in population]
        print("Best fitness: {}".format(max(fitnessValues)))

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
                    return [max(fitnessValues), generation]

        c += 1

if __name__ == "__main__":
    results = main()
    # Write best fintess and generation number to log 
    with open("genetic.log", "a") as logfile:
        logfile.write("Best fitness: {}, Generations: {}\n".format(results[0], results[1]))
