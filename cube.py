# /usr/bin/python3
import math
import pprint
import random
from point import *


class Cube:
    def __init__(self, cubeSize, initPoint, endPoint, percentOfBlockedPoints, blockedValues=[]):
        """ Função construtora de um Cubo.

        Arguments:
            cubeSize {int}    -- Número de pontos em uma face.
            initPoint {Point} -- Ponto de início.
            endPoint {Point}  -- Ponto final.
            percentOfBlockedPoints {int} -- Porcentagem de pontos bloqueados.

        Keyword Arguments:
            blockedValues {list} -- Lista de elementos bloqueados. 
            Se deixar em branco, é gerado aleatoriamente. (default: {[]})
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
        """ Método que cria obstáculos no cubo baseado em uma porcentagem 
        fornecida na criação do cubo
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

    def pprintArray(self):
        """ Printa a array de maneira bonita
        """
        pprint.pprint(self.array)

    def getInformations(self):
        """ Retorna as principais informações do cubo

        Returns:
            [string] -- [String contendo tamanho, porcentagem,
                        pts de inicio e fim]
        """
        return ("size: {}, blocked: {}%, init: {}, end: {}"
                .format(self.cubeSize, self.percentOfBlockedPoints,
                        self.initPoint, self.endPoint))

    def getBlockedValues(self):
        """ Retorna uma array com as coordenadas de valores bloqueados. 
        Útil para realizar a mesma busca diversas vezes

        Returns:
            [list] -- [Array com valores bloqueados]
        """
        return self.blockedValues

    def getNeighbors(self, point):
        """ Pega os vizinhos de cada ponto
        
        Arguments:
            point {[Ponto]}
        
        Returns:
            [Array[Point]] -- [Array com os vizinhos validos deste ponto]
        """
        neighbors = []
        neighbors.append(Point(point.getX() + 1, point.getY(),
                               point.getZ(), parent=point, endPoint=self.endPoint))
        neighbors.append(Point(point.getX(), point.getY() + 1,
                               point.getZ(), parent=point, endPoint=self.endPoint))
        neighbors.append(Point(point.getX(), point.getY(
        ), point.getZ() + 1, parent=point, endPoint=self.endPoint))
        neighbors.append(Point(point.getX() - 1, point.getY(),
                               point.getZ(), parent=point, endPoint=self.endPoint))
        neighbors.append(Point(point.getX(), point.getY() - 1,
                               point.getZ(), parent=point, endPoint=self.endPoint))
        neighbors.append(Point(point.getX(), point.getY(
        ), point.getZ() - 1, parent=point, endPoint=self.endPoint))

        return list(filter(self.neighborIsValid, neighbors))

    def getLowestFValue(self, array):
        """ Pegar o menor valor de F.
        
        Arguments:
            array {[Ponto]} -- [array de pontos]
        
        Returns:
            [Ponto] -- [Ponto com menor F]
        """
        if len(array) > 0:
            lowest = array[0]
            for point in array:
                if point.calculateF() < lowest.calculateF():
                    lowest = point
            return lowest

    def neighborIsValid(self, point):
        """ Determina se os vizinhos do Ponto são válidos
        
        Arguments:
            point {[Point]} -- [Ponto]
        
        Returns:
            [bool] -- [Se é valido]
        """
        return ((point.getX() < self.cubeSize and point.getY() < self.cubeSize and
                 point.getZ() < self.cubeSize and point.getX() >= 0 and
                 point.getY() >= 0 and point.getZ() >= 0) and self.array[point.getX()][point.getY()][point.getZ()].isBlocked == False)
