#!/usr/bin/env python3
from modules.gen_random_position import genRandomPosition


# The propterties of game and game objects can be modified here
screenWidth = 600
screenHeight = 600
robotVelocity = 10
robotSize = (10, 10)
destSize = (30, 30)

# Number of individuals in the population or
#   number of possible solutions/robots
populationSize = 100

# The length of chromosome, it is the number of steps as well
#   which can be done by an individual
chromosomeLength = 500

# The initial position of the robot
initialRobotPosition = genRandomPosition((screenWidth, screenHeight), robotSize)

# The initial position of the destinaiton
destPosition = genRandomPosition((screenWidth, screenHeight), destSize)
