#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void
from convex import Polygon, Void, Segment, Point

f = Void()
try:
    while True:
        f = f.add(R2Point())
        print(f"S = {f.area()}, P = {f.perimeter()}", end=' ')
        if isinstance(f, Polygon):
            print(f'D = {f.diameter}\n')
        elif isinstance(f, Segment):
            print(f'D = {f.diameter()}\n')
        elif isinstance(f, Point):
            print(f'D = {0}\n')
        else:
            print('\n')
except (EOFError, KeyboardInterrupt):
    print("\nStop")
