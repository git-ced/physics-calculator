import math


def square(s):
    return s * s


def rectangle(l, w):
    return l * w


def circle(r):
    return math.pi * r * r


def triangle(b, h):
    return b * h * 0.5


def parallelogram(b, h):
    return b * h


def sphere(r):
    return circle(r) * 4


def cube(s):
    return square(s) * 6


def cylinder(r, h):
    return (2 * math.pi * r * h) + (circle(r) * 2)
