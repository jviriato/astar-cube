# /usr/bin/python3

from cube import *
from point import *
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Take two points in a Cube and find the path using A*.')
    parser.add_argument('-x1', help="Point x of Init", required=False)
    parser.add_argument('-y1', help="Point y of Init", required=False)
    parser.add_argument('-z1', help="Point z of Init", required=False)
    parser.add_argument('-x2', help="Point x of End", required=False)
    parser.add_argument('-y2', help="Point y of End", required=False)
    parser.add_argument('-z2', help="Point z of End", required=False)
    parser.add_argument(
        '-c', help="c**3 = Quantity of Points in the Cube", required=False)
    parser.parse_args()
    c = Cube(3, Point(0, 0, 0, isInit=True), Point(0, 0, 2, isEnd=True), 5)
    c.createObstacles()
    c.pprint_array()
    # c.printCube()


if __name__ == "__main__":
    main()
