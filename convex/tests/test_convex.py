from pytest import approx
from math import sqrt
from r2point import R2Point
from convex import Figure, Void, Point, Segment, Polygon


class TestVoid:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.f = Void()

    # Нульугольник является фигурой
    def test_figure(self):
        assert isinstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Void (нульугольник)
    def test_void(self):
        assert isinstance(self.f, Void)

    # Периметр нульугольника нулевой
    def test_perimeter(self):
        assert self.f.perimeter() == 0.0

    # Площадь нульугольника нулевая
    def test_аrea(self):
        assert self.f.area() == 0.0

    def test_diameter(self):
        assert self.f.diameter() == 0.0

    # При добавлении точки нульугольник превращается в одноугольник
    def test_add(self):
        assert isinstance(self.f.add(R2Point(0.0, 0.0)), Point)


class TestPoint:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.f = Point(R2Point(0.0, 0.0))

    # Одноугольник является фигурой
    def test_figure(self):
        assert isinstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Point (одноугольник)
    def test_point(self):
        assert isinstance(self.f, Point)

    # Периметр одноугольника нулевой
    def test_perimeter(self):
        assert self.f.perimeter() == 0.0

    # Площадь одноугольника нулевая
    def test_аrea(self):
        assert self.f.area() == 0.0

    def test_diameter(self):
        assert self.f.diameter() == 0.0

    # При добавлении точки одноугольник может не измениться
    def test_add1(self):
        assert self.f.add(R2Point(0.0, 0.0)) is self.f

    # При добавлении точки одноугольник может превратиться в двуугольник
    def test_add2(self):
        assert isinstance(self.f.add(R2Point(1.0, 0.0)), Segment)


class TestSegment:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.f = Segment(R2Point(0.0, 0.0), R2Point(1.0, 0.0))

    # Двуугольник является фигурой
    def test_figure(self):
        assert isinstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Segment (двуугольник)
    def test_segment(self):
        assert isinstance(self.f, Segment)

    # Периметр двуугольника равен удвоенной длине отрезка
    def test_perimeter(self):
        assert self.f.perimeter() == approx(2.0)

    # Площадь двуугольника нулевая
    def test_аrea(self):
        assert self.f.area() == 0.0

    def test_diameter(self):
        assert self.f.diameter() == approx(1.0)

    # При добавлении точки двуугольник может не измениться
    def test_add1(self):
        assert self.f.add(R2Point(0.5, 0.0)) is self.f

    # При добавлении точки двуугольник может превратиться в другой двуугольник
    def test_add2(self):
        assert isinstance(self.f.add(R2Point(2.0, 0.0)), Segment)

    # При добавлении точки двуугольник может превратиться в треугольник
    def test_add2(self):
        assert isinstance(self.f.add(R2Point(0.0, 1.0)), Polygon)


class TestPolygon:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.f = Polygon(
            R2Point(
                0.0, 0.0), R2Point(
                1.0, 0.0), R2Point(
                0.0, 1.0))

    # Многоугольник является фигурой
    def test_figure(self):
        assert isinstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Polygon (многоугольник)
    def test_polygon(self):
        assert isinstance(self.f, Polygon)

    # Изменение количества вершин многоугольника
    #   изначально их три
    def test_vertexes1(self):
        assert self.f.points.size() == 3
    #   добавление точки внутрь многоугольника не меняет их количества

    def test_vertexes2(self):
        assert self.f.add(R2Point(0.1, 0.1)).points.size() == 3
    #   добавление другой точки может изменить их количество

    def test_vertexes3(self):
        assert self.f.add(R2Point(1.0, 1.0)).points.size() == 4
    #   изменения выпуклой оболочки могут и уменьшать их количество

    def test_vertexes4(self):
        assert self.f.add(
            R2Point(
                0.4,
                1.0)).add(
            R2Point(
                1.0,
                0.4)).add(
                    R2Point(
                        0.8,
                        0.9)).add(
                            R2Point(
                                0.9,
                                0.8)).points.size() == 7
        assert self.f.add(R2Point(2.0, 2.0)).points.size() == 4

    # Изменение периметра многоугольника
    #   изначально он равен сумме длин сторон
    def test_perimeter1(self):
        assert self.f.perimeter() == approx(2.0 + sqrt(2.0))
    #   добавление точки может его изменить

    def test_perimeter2(self):
        assert self.f.add(R2Point(1.0, 1.0)).perimeter() == approx(4.0)

    # Изменение площади многоугольника
    #   изначально она равна (неориентированной) площади треугольника
    def test_аrea1(self):
        assert self.f.area() == approx(0.5)
    #   добавление точки может увеличить площадь

    def test_area2(self):
        assert self.f.add(R2Point(1.0, 1.0)).area() == approx(1.0)

    def test_diameter1(self):
        assert self.f.diameter() == approx(sqrt(2))

    def test_diameter2(self):
        assert self.f.add(R2Point(3.0, 4.0)).diameter() == approx(5.0)

    def test_diameter3(self):
        assert self.f.add(R2Point(0.0, -1.0)).add(R2Point(-4.0, 12.0)).add(
            R2Point(0.0, 0.0)).diameter() == sqrt(185)

    def test_diameter4(self):
        assert self.f.add(R2Point(5.0, 2.0)).add(R2Point(0.0, 5.0)).add(
            R2Point(-2.0, -1.0)).diameter() == sqrt(58)

    def test_diameter5(self):
        self.t = Polygon(R2Point(52.0, 23.0), R2Point(65.0, 45.0),
                         R2Point(98.0, 22.0))
        self.t.add(R2Point(33.0, 50.0))
        self.t.add(R2Point(76.0, 58.0))
        self.t.add(R2Point(52.0, 48.0))
        self.t.add(R2Point(59.0, 40.0))
        self.t.add(R2Point(37.0, 97.0))
        self.t.add(R2Point(52.0, 31.0))
        self.t.add(R2Point(58.0, 77.0))
        self.t.add(R2Point(49.0, 48.0))
        self.t.add(R2Point(52.0, 68.0))
        self.t.add(R2Point(19.0, 33.0))
        self.t.add(R2Point(17.0, 28.0))
        self.t.add(R2Point(12.0, 29.0))
        assert self.t.diameter() == sqrt(9346)

    def test_diameter6(self):
        self.t = Polygon(R2Point(-4.0, 1.0), R2Point(-7.0, -10.0),
                         R2Point(-7.0, -10.0))
        self.t.add(R2Point(-5.0, 1.0))
        self.t.add(R2Point(-5.0, 4.0))
        self.t.add(R2Point(-4.0, -10.0))
        self.t.add(R2Point(0.0, 9.0))
        self.t.add(R2Point(-1.0, -10.0))
        self.t.add(R2Point(2.0, -7.0))
        self.t.add(R2Point(-3.0, -4.0))
        self.t.add(R2Point(5.0, 5.0))
        self.t.add(R2Point(1.0, 1.0))
        self.t.add(R2Point(-1.0, -5.0))
        self.t.add(R2Point(4.0, 9.0))
        self.t.add(R2Point(-8.0, 1.0))
        assert self.t.diameter() == sqrt(482)

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

    def test_diameter8(self):
        self.t = Polygon(R2Point(-74.0, -31.0), R2Point(16.0, -40.0),
                         R2Point(80.0, 76.0))
        self.t.add(R2Point(79.0, 40.0))
        self.t.add(R2Point(48.0, 52.0))
        self.t.add(R2Point(39.0, -40.0))
        self.t.add(R2Point(22.0, 64.0))
        self.t.add(R2Point(31.0, 16.0))
        self.t.add(R2Point(-83.0, -76.0))
        self.t.add(R2Point(26.0, 84.0))
        assert self.t.diameter() == sqrt(49673)

    def test_diameter9(self):
        self.t = Polygon(R2Point(-8.0, 21.0), R2Point(27.0, 7.0),
                         R2Point(-49.0, -72.0))
        self.t.add(R2Point(-64.0, -53.0))
        self.t.add(R2Point(75.0, -11.0))
        self.t.add(R2Point(90.0, -4.0))
        self.t.add(R2Point(52.0, -43.0))
        self.t.add(R2Point(95.0, 3.0))
        self.t.add(R2Point(-55.0, -55.0))
        self.t.add(R2Point(13.0, -70.0))
        assert self.t.diameter() == sqrt(28417)

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
