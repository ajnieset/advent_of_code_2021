from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Point:
    x: int
    y: int

    def __init__(self, coordinates: Tuple[str]) -> None:
        self.x = int(coordinates[0])
        self.y = int(coordinates[1])

@dataclass
class Line:
    start: Point
    end: Point

    def __init__(self, segment: Tuple[Point]) -> None:
        self.start = segment[0]
        self.end = segment[1]


def format_data(vents: List[str]) -> List[Line]:
    vents = map(lambda x: Line(tuple(map(lambda y: Point(tuple(y.split(','))), tuple(x.rstrip().split(' -> '))))), vents)
    return list(vents)

def main():
    with open("input.csv") as inputs:
        vents = list(inputs)
    vents = format_data(vents)

if __name__ == "__main__":
    main()