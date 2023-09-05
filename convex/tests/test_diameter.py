from pytest import approx
from math import sqrt
from r2point import R2Point
from convex import Figure, Void, Point, Segment, Polygon

class TestPoint:
    def setup_method(self):
        self.f = Point(R2Point(0.0, 0.0))

    def test_diameter(self):
        assert self.f.diameter() == 0.0

class TestSegment:
    def setup_method(self):
        self.f = Segment(R2Point(0.0, 0.0), R2Point(1.0, 0.0))

    def test_diameter(self):
        assert self.f.diameter() == approx(1.0)

class TestPolygon:
    def test_diameter10(self):
        self.t = Polygon(R2Point(-17.0, 95.0), R2Point(21.0, 37.0),
                         R2Point(14.0, -56.0))
        self.t.add(R2Point(63.0, -78.0))
        self.t.add(R2Point(38.0, -52.0))
        self.t.add(R2Point(26.0, -27.0))
        self.t.add(R2Point(-8.0, -36.0))
        self.t.add(R2Point(-41.0, 25.0))
        self.t.add(R2Point(65.0, -62.0))
        self.t.add(R2Point(82.0, 14.0))
        self.t.add(R2Point(43.0, -61.0))
        self.t.add(R2Point(-48.0, -40.0))
        self.t.add(R2Point(-7.0, -63.0))
        self.t.add(R2Point(2.0, 85.0))
        self.t.add(R2Point(83.0, -1.0))
        assert self.t.diameter() == approx(sqrt(36329))

    def test_diameter7(self):
        self.t = Polygon(R2Point(9.0, 3.0), R2Point(-14.0, 12.0),
                         R2Point(-8.0, -11.0))
        self.t.add(R2Point(0.0, 6.0))
        self.t.add(R2Point(3.0, 14.0))
        self.t.add(R2Point(8.0, 10.0))
        self.t.add(R2Point(0.0, 9.0))
        self.t.add(R2Point(-9.0, -9.0))
        self.t.add(R2Point(8.0, 14.0))
        self.t.add(R2Point(-8.0, 10.0))
        self.t.add(R2Point(6.0, -5.0))
        assert self.t.diameter() == sqrt(881)