#/usr/bin/python3
import math
import pprint
import random
from point import *


class Cube:
    def __init__(self, cubeSize, initPoint, endPoint, percentOfBlockedPoints):
        self.cubeSize  = cubeSize
        self.initPoint = initPoint
        self.endPoint  = endPoint
        self.percentOfBlockedPoints = percentOfBlockedPoints
        self.array = [[[Point(k,j,i) for k in range(cubeSize)] for j in range(cubeSize)] for i in range(cubeSize)]
        self.array[self.initPoint.x][self.initPoint.y][self.initPoint.z] = self.initPoint
        self.array[self.endPoint.x][self.endPoint.y][self.endPoint.z] = self.endPoint
        

    def createObstacles(self):
        numOfBlockedPoints = ((self.cubeSize**3) * self.percentOfBlockedPoints) / 100
        blocked_values = []
        while len(blocked_values) < numOfBlockedPoints:
            x = random.randint(0, self.cubeSize - 1)
            y = random.randint(0, self.cubeSize - 1)
            z = random.randint(0, self.cubeSize - 1)
            if (x,y,z) not in blocked_values:
                blocked_values.append((x,y,z))
                self.array[x][y][z].isBlocked = True

    def printCube(self):
        for i in range(self.cubeSize):
            for j in range(self.cubeSize):
                for k in range(self.cubeSize):
                    print(self.array[i][j][k])

    def pprint_array(self):
        pprint.pprint(self.array)

    # def __str__(self):
    #     return pprint.pprint(self.array)

    # def __repr__(self):
    #     return pprint.pprint(self.array)
