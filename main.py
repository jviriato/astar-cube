# /usr/bin/python3
#
#  @author: José Victor Viriato
#  como usar: python3 main.py [args]
#  na linha de comando.
#
#  python3 main.py -h para ajuda
#
#  ex de uso: python3 main.py -c 3 -p 50
#  para criar um cubo 3**3 com 50% dos pontos bloqueados
#
#  Argumentos omitidos serão aleatórios
#
# *****************************************

import random
import argparse
from cube import *
from point import *
from a_star import *


def pointIsDefined(x, y, z):
    return x is not None and y is not None and z is not None


def getSizeOfCube(numCube):
    if numCube is not None:
        return int(numCube)
    else:
        return random.randint(1, 10)


def getPercentOfBlockedPoints(pct):
    if pct is not None:
        return int(pct)
    else:
        return random.randint(0, 100)


def parseArgs(parser):
    parser.add_argument(
        '-x1', type=int, help="Point x of Init", required=False)
    parser.add_argument(
        '-y1', type=int, help="Point y of Init", required=False)
    parser.add_argument(
        '-z1', type=int, help="Point z of Init", required=False)
    parser.add_argument('-x2', type=int, help="Point x of End", required=False)
    parser.add_argument('-y2', type=int, help="Point y of End", required=False)
    parser.add_argument('-z2', type=int, help="Point z of End", required=False)
    parser.add_argument(
        '-c', type=int, help="c**3 = Quantity of Points in the Cube", required=False)
    parser.add_argument(
        '-p', type=int, help="Percentage of Blocked Points", required=False)
    return parser.parse_args()


def main():
    parser = argparse.ArgumentParser(
        description='Take two points in a Cube and find the path using A*.')
    args = parseArgs(parser)
    sizeOfCube = getSizeOfCube(args.c)
    percentOfBlockedPoints = getPercentOfBlockedPoints(args.p)

    if pointIsDefined(args.x1, args.y1, args.z1):
        p1 = Point(args.x1, args.y1, args.z1)
    else:
        p1 = Point(random.randint(0, sizeOfCube - 1), random.randint(
            0, sizeOfCube - 1), random.randint(0, sizeOfCube - 1))

    if pointIsDefined(args.x2, args.y2, args.z2):
        p2 = Point(args.x2, args.y2, args.z2)
    else:
        p2 = Point(random.randint(0, sizeOfCube - 1), random.randint(
            0, sizeOfCube - 1), random.randint(0, sizeOfCube - 1))

    cube = Cube(sizeOfCube, p1, p2, percentOfBlockedPoints)
    cube.pprintArray()
    astar = AStar(cube, cube.initPoint, cube.endPoint)


if __name__ == "__main__":
    main()
