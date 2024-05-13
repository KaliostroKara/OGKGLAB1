import math
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Node:
    def __init__(self, point):
        self.point = point
        self.topLeft = None
        self.topRight = None
        self.bottomLeft = None
        self.bottomRight = None

class Quadtree:
    def __init__(self):
        self.root = None

    def insert(self, point):
        self.root = self._insert_node(self.root, point)

    def _insert_node(self, node, point):
        if node is None:
            return Node(point)
        elif point.x < node.point.x:
            if point.y < node.point.y:
                node.bottomLeft = self._insert_node(node.bottomLeft, point)
            else:
                node.topLeft = self._insert_node(node.topLeft, point)
        else:
            if point.y < node.point.y:
                node.bottomRight = self._insert_node(node.bottomRight, point)
            else:
                node.topRight = self._insert_node(node.topRight, point)
        return node

    def collect_all_points(self):
        result = []
        self._collect_all_points(self.root, result)
        return result

    def _collect_all_points(self, node, result):
        if node is None:
            return
        result.append(node.point)
        self._collect_all_points(node.topLeft, result)
        self._collect_all_points(node.topRight, result)
        self._collect_all_points(node.bottomLeft, result)
        self._collect_all_points(node.bottomRight, result)

    def is_point_inside_circle(self, point, center, radius):
        return math.sqrt((point.x - center.x) ** 2 + (point.y - center.y) ** 2) <= radius

def main():
    radius = float(input("Enter the radius of the circle: "))
    num_points = int(input("Enter the number of points: "))
    center_x, center_y = map(float, input("Enter the coordinates of the center of the circle (x, y): ").split())

    rng = random.Random()
    quadtree = Quadtree()
    for _ in range(num_points):
        x = rng.uniform(-10.0, 10.0)
        y = rng.uniform(-10.0, 10.0)
        quadtree.insert(Point(x, y))

    all_points = quadtree.collect_all_points()

    for point in all_points:
        if quadtree.is_point_inside_circle(point, Point(center_x, center_y), radius):
            print(f"Point ({point.x}, {point.y}) inside")
        else:
            print(f"Point ({point.x}, {point.y}) outside")

if __name__ == "__main__":
    main()
