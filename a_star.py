

from point import Point
from cube import Cube


class AStar:
    def __init__(self, graph, initPoint, endPoint):
        """ Construtor da função A*
        
        Arguments:
            graph {[Cube]} -- [Um cubo]
            initPoint {[Point]} -- [Ponto inicial]
            endPoint {[Point]} -- [Ponto final]
        """
        self.graph = graph
        self.initPoint = initPoint
        self.endPoint = endPoint
        self.openedPoints = []
        self.closedPoints = []

    def search(self):
        """ Aplica a busca do A*
        
        Raises:
            ValueError: [Caso não tenha solução, causa uma exceção]
        
        Returns:
            [array] -- [O caminho percorrido até chegar no ponto final]
        """
        self.openedPoints.append(self.initPoint)
        while len(self.openedPoints) > 0:
            current = min(self.openedPoints, key=lambda o: o.g + o.h)
            print(current)

            self.openedPoints.remove(current)
            self.closedPoints.append(current)
            
            if current == self.endPoint:
                print(current.g)
                path = []
                while current.parent:
                    path.append(current)
                    current = current.parent
                path.append(current)
                return path[::-1]

            children = self.graph.getNeighbors(current)
            for child in children:
                if child in self.closedPoints:
                    continue

                if child in self.openedPoints:
                    continue
                
                else:
                    child.g = current.g + 1
                    child.h = child.calcHeuristicDistanceFromEnd(self.endPoint)
                    child.parent = current
                    self.openedPoints.append(child)
        raise ValueError('No Path Found')