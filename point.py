# /usr/bin/python3

import pprint
import math


class Point:

    def __init__(self, x, y, z,
                 parent=None,
                 isBlocked=False, isInit=False,
                 isEnd=False, endPoint=None):
        """Função construtora de um ponto no cubo.

        Arguments:
            x {[int]} -- [coordenada x do ponto]
            z {[int]} -- [coordenada y do ponto]
            y {[int]} -- [coordenada z do ponto]

        Keyword Arguments:
            parent    {Point} -- [Guarda a posição do ponto pai]          (default: {None})
            endPoint  {Point} -- [Guarda a posição do ponto final]        (default: {None})
            isBlocked {bool}  -- [Verificar se ponto está bloqueado]      (default: {False})
            isInit    {bool}  -- [Verificar se ponto é o ponto inicial]   (default: {False})
            isEnd     {bool}  -- [Verificar se ponto é o ponto final]     (default: {False})

        """
        self.x = x
        self.y = y
        self.z = z
        self.isEnd = isEnd
        self.isInit = isInit
        self.isBlocked = isBlocked
        if (parent is not None):
            self.parent = parent
            self.g = calcHeuristicDistanceFromEnd(endPoint)
            self.h = calcDistanceBetweenInit(parent)
            self.f = calculateF()
        else:
            self.parent = None
            self.g = 0
            self.h = 0
            self.f = 0

    def distanceBetweenThisPointAndAnother(self, point):
        """Calcula a distância entre esse ponto e outro

        Arguments:
            point {[Point]} -- [Outro ponto]

        Returns:
            [float] -- [Distância calculada entre esse ponto e outro]
        """
        return math.sqrt(
            ((point.x - self.x) ** 2) +
            ((point.y - self.y) ** 2) +
            ((point.z - self.z) ** 2))

    def setBlocked(self):
        self.isBlocked = True
    
    def setInit(self):
        self.isInit = True
    
    def setEnd(self):
        self.isEnd = True

    def isBlocked(self):
        return self.IsBlocked
    
    def isInit(self):
        return self.isInit
    
    def isEnd(self):
        return self.isEnd

    def calcHeuristicDistanceFromEnd(self, point):
        """Calcula a distância heurística do ponto
        
        Arguments:
            point {[Point]} -- [Ponto Final]
        
        Returns:
            [float] -- [Distância entre dois pontos]
        """
        return distanceBetweenThisPointAndAnother(self, point)

    def calcDistanceBetweenInit(self, point):
        """Calcula a distância do ponto até o ponto inicial
        
        Arguments:
            point {[Point]} -- [Ponto inicial]
        
        Returns:
            [int] -- [Distância entre dois pontos]
        """
        return 1 + point.g

    def calculateF(self):
        return self.g + self.h

    def __str__(self):
        if(self.isBlocked):
            return "({0}, {1}, {2}, B)".format(self.x, self.y, self.z)
        if(self.isInit):
            return "({0}, {1}, {2}, I)".format(self.x, self.y, self.z)
        if(self.isEnd):
            return "({0}, {1}, {2}, E)".format(self.x, self.y, self.z)

        return "({0}, {1}, {2}, {3}, _)".format(self.x, self.y, self.z, self.isBlocked)

    def __repr__(self):
        if(self.isBlocked):
            return "({0}, {1}, {2}, B)".format(self.x, self.y, self.z)
        if(self.isInit):
            return "({0}, {1}, {2}, I)".format(self.x, self.y, self.z)
        if(self.isEnd):
            return "({0}, {1}, {2}, E)".format(self.x, self.y, self.z)

        return "({0}, {1}, {2}, _)".format(self.x, self.y, self.z)

    def __eq__(self, value):
        return (self.x == value.x and
                self.y == value.y and
                self.z == value.z)
