# /usr/bin/python3
import math
import pprint
import random
from point import *


class Cube:
    def __init__(self, cubeSize, initPoint, endPoint, percentOfBlockedPoints, blockedValues=[]):
        """Cria um Cubo.

        Arguments:
            cubeSize {[int]}    -- [Número de pontos em uma face.]
            initPoint {[Point]} -- [Ponto de início.]
            endPoint {[Point]}  -- [Ponto final.]
            percentOfBlockedPoints {[Int]} -- [Porcentagem de pontos bloqueados.]

        Keyword Arguments:
            blockedValues {list} -- [Lista de elementos bloqueados. Se deixar em branco,
                                                é gerado aleatoriamente.] (default: {[]})
        """

        self.cubeSize = cubeSize
        self.initPoint = initPoint
        self.initPoint.setInit()
        self.endPoint = endPoint
        self.endPoint.setEnd()
        self.percentOfBlockedPoints = percentOfBlockedPoints
        self.array = [[[Point(k, j, i) for k in range(cubeSize)]
                       for j in range(cubeSize)] for i in range(cubeSize)]
        self.array[self.initPoint.x][self.initPoint.y][self.initPoint.z] = self.initPoint
        self.array[self.endPoint.x][self.endPoint.y][self.endPoint.z] = self.endPoint
        self.blockedValues = blockedValues
        self.createObstacles()

    def createObstacles(self):
        """ Método que cria obstáculos no cubo baseado em uma porcentagem fornecida na criação do cubo
        """
        InitAndEnd = 2
        numOfBlockedPoints = ((((self.cubeSize**3) - InitAndEnd) *
                               self.percentOfBlockedPoints) / 100)
        self.blockedValues = []
        self.blockedValues.append(
            (self.initPoint.x, self.initPoint.y, self.initPoint.z))
        self.blockedValues.append(
            (self.endPoint.x, self.endPoint.y, self.endPoint.z))
        while len(self.blockedValues) < numOfBlockedPoints + InitAndEnd:
            x = random.randint(0, self.cubeSize - 1)
            y = random.randint(0, self.cubeSize - 1)
            z = random.randint(0, self.cubeSize - 1)
            if (x, y, z) not in self.blockedValues:
                self.blockedValues.append((x, y, z))
                self.array[x][y][z].isBlocked = True

    def printCube(self):
        for i in range(self.cubeSize):
            for j in range(self.cubeSize):
                for k in range(self.cubeSize):
                    print(self.array[i][j][k])

    def pprintArray(self):
        pprint.pprint(self.array)

    def getInformations(self):
        return ("size: {}, blocked: {}%, init: {}, end: {}"
                .format(self.cubeSize, self.percentOfBlockedPoints,
                        self.initPoint, self.endPoint))

    def getBlockedValues(self):
        return self.blockedValues
