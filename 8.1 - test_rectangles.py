import pytest
from rectangles import Point, Rectangle


def test_rectangle_creation():
    r = Rectangle(0, 0, 10, 5)
    assert r.left == 0
    assert r.bottom == 0
    assert r.right == 10
    assert r.top == 5


def test_from_points():
    p1 = Point(1, 2)
    p2 = Point(5, 6)
    r = Rectangle.from_points((p1, p2))

    assert r.left == 1
    assert r.bottom == 2
    assert r.right == 5
    assert r.top == 6


def test_dimensions():
    r = Rectangle(0, 0, 4, 3)
    assert r.width == 4
    assert r.height == 3
    assert r.area == 12


def test_center():
    r = Rectangle(0, 0, 4, 4)
    assert r.center == Point(2, 2)


def test_corners():
    r = Rectangle(1, 2, 5, 6)

    assert r.topleft == Point(1, 6)
    assert r.topright == Point(5, 6)
    assert r.bottomleft == Point(1, 2)
    assert r.bottomright == Point(5, 2)


def test_move():
    r = Rectangle(0, 0, 2, 2)
    r.move(3, 4)

    assert r.left == 3
    assert r.bottom == 4
    assert r.right == 5
    assert r.top == 6


def test_equality():
    r1 = Rectangle(0, 0, 2, 2)
    r2 = Rectangle(0, 0, 2, 2)
    r3 = Rectangle(1, 1, 3, 3)

    assert r1 == r2
    assert r1 != r3

