#!/usr/bin/env python3
from modules.gen_random_position import genRandomPosition


# The propterties of game and game objects can be modified here
screenWidth = 1900
screenHeight = 1600
robotVelocity = 10
robotSize = (10, 10)
destSize = (30, 30)

# Number of individuals in the population or
#   number of possible solutions/robots
populationSize = 100

# The length of chromosome, it is the number of steps as well
#   which can be done by an individual
chromosomeLength = 200

# Maximum number of generations
# This is for terminating the program in case of unsolvable problem
maxGeneration = 100

# The initial position of the robot
# initialRobotPosition = genRandomPosition((screenWidth, screenHeight), robotSize)
initialRobotPosition = (450, 600)

# The initial position of the destinaiton
# destPosition = genRandomPosition((screenWidth, screenHeight), destSize)
destPosition = (1700, 0)
