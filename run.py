#!/usr/bin/env python3
from modules.game_object import GameObject, Robot
from modules.game_screen import GameScreen
from modules.utilities import pseudoRandomMove, checkQuitEvent 
from modules.utilities import crossover, mutatePopulation, selection
from random import randint
from config import screenWidth, screenHeight, robotSize, robotVelocity, destSize
from config import initialRobotPosition, destPosition
from config import populationSize, chromosomeLength
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

    print(dest.x, dest.y)

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




    # Ezzel nincsenek adott iranyba terelve
    # for _ in range(100):
        # checkQuitEvent()
        # pseudoRandomMove(game, population, dest)
 
    # Ez a fo mukodo verzio
    # Ezzel adott iranyba vannak terelve
    # 0. generation
    # mainDirection = randint(1,4)
    # for _ in range(chromosomeLength):
        # checkQuitEvent()
        # pseudoRandomMove(game, population, dest, mainDirection)

    # print("Fitness of parents")
    # for robot in population:
        # robot.calFitness(dest)
        # print(robot.x, robot.y, robot.fitness)

    # print(population[0].steps)
    # print(population[1].steps)
    # child = crossover(population[0], population[1])
    # print(child.steps)
    # print("Fitness of children")
    # children = crossover(population, game)
    # for child in children:
        # child.calFitness(dest)
        # print(child.x, child.y, child.fitness)
    
    # mergedPopulation = population + children
    # print(len(population), len(children), len(mergedPopulation))
    # mutatePopulation(mergedPopulation, game, round(populationSize * 0.1))

    # print("Fitness of merged population")
    # for robot in mergedPopulation:
        # robot.calFitness(dest)
    #     print(robot.x, robot.y, robot.fitness)

   
    c = 0
    while c != 15:
        # Delaying pygame between genration
        pygame.time.delay(10)

 
        # Reset screen for the current generation
        game.fillScreen()
        dest.drawObject(game.screen)
        pygame.display.flip()
        pygame.time.delay(300)

        if generation == 0:
            mainDirection = randint(1,4)
            for _ in range(chromosomeLength):
                checkQuitEvent()
                pseudoRandomMove(game, population, dest, mainDirection)
        else:
            for s in range(chromosomeLength):
                checkQuitEvent()
                game.fillScreen()
                dest.drawObject(game.screen)
                for robot in population:
                    robot.move(game.screenWidth, game.screenHeight, robot.steps[s], saveStep=False)
                    robot.drawObject(game.screen)
                pygame.display.flip()
                pygame.time.delay(10)

        # For Debugging
        with open("logs/debug1.log", 'a') as ouf:
            ouf.write("{}. generation before: X, Y, fitness, steps\n".format(generation))
            for robot in population:
                ouf.write("{}, {}, {}, {}\n".format(robot.x, robot.y, robot.fitness, robot.steps))

        # Crossover of population
        children = crossover(population, game)

        # Calculating fitness of current generation
        mergedPopulation = population + children
        [robot.calFitness(dest) for robot in mergedPopulation]

        # Mutatation of last 10% of the population.
        mutatePopulation(mergedPopulation, game, round(populationSize * 0.1))

        # Recalculating the fitness after mutation
        [robot.calFitness(dest) for robot in mergedPopulation]

        # Selection of population (sorts the population)
        selection(mergedPopulation)

        # Selecting the best fitness value member
        bestFitness = population[0].fitness

        # For Debugging
        with open("logs/debug1.log", 'a') as ouf:
            ouf.write("{}. generation afer: X, Y, fitness, steps\n".format(generation))
            for robot in population:
                ouf.write("{}, {}, {}, {}\n".format(robot.x, robot.y, robot.fitness, robot.steps))

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


        # Checking if we reached the destination
        # van valami baj a fitnessesl is mert siman atgazoltak a celponton :D
        # if bestFitness >= 0:
            # break
            
        c += 1

if __name__ == "__main__":
    main()
