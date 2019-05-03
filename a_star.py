


class AStar:
    def __init__(self, graph, initPoint, endPoint):
        self.graph     = graph
        self.initPoint = initPoint
        self.endPoint  = endPoint
        self.queue = []