#!/usr/bin/env python3
from modules.gen_random_position import genRandomPosition


# The propterties of game and game objects can be modified here
screenWidth = 1680
screenHeight = 1050
robotVelocity = 10
robotSize = (10, 10)
destSize = (30, 30)

# Number of individuals in the population or
# number of possible solutions/robots
populationSize = 100

# The length of chromosome, it is the number of steps as well
# which can be done by an individual
chromosomeLength = 300

# Maximum number of generations
# This is for terminating the program in case of unsolvable problem
maxGeneration = 100

# The mutation factor of population
populationMutationFactor = 0.05

# Mutation factor of genes
geneMutationFactor = 0.5


# The initial position of the robot

# Comment out this line if random position is needed
# initialRobotPosition = genRandomPosition((screenWidth, screenHeight), robotSize)

initialRobotPosition = (0, 1040)


# The initial position of the destinaiton

# Comment out this line if random position is needed
# destPosition = genRandomPosition((screenWidth, screenHeight), destSize)

destPosition = (1650, 0)
