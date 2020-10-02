import abc
import os

# Abstract class.
class TriangleStrategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    # Identify the type of triangle based on each of its sides.
    def get_triangle_type(self):
        pass

# Strategy based when each of its sides are the same.
class EquilateralStrategy(TriangleStrategy):
    def get_triangle_type(self):
        return 'Equilátero'
# Strategy based when there are two sides that are the same.
class IsoscelesStrategy(TriangleStrategy):
    def get_triangle_type(self):
        return 'Isóceles'
# Strategy based when all of its sides are different.
class ScaleneStrategy(TriangleStrategy):
    def get_triangle_type(self):
        return 'Escaleno'
# Strategy based when the sum of its two sides are not greather than the third side.
class NoTriangleStrategy(TriangleStrategy):
    def get_triangle_type(self):
        return 'No triángulo'

# Context.
class TriangleContext(object):
    def __init__(self, sides: str, strategy: TriangleStrategy = None):
        self._sides = [int(side) for side in sides.split(' ')]
        self._first_side = self._sides[0]
        self._second_side = self._sides[1]
        self._third_side = self._sides[2]
        self._strategy = strategy

    def get_triangle_type_context(self):
        # Strategy based when the sum of its two sides are not greather than the third side.
        if (self._first_side + self._second_side <= self._third_side) or (self._first_side + self._third_side <= self._second_side) or (self._second_side + self._third_side <= self._first_side): 
            return NoTriangleStrategy().get_triangle_type()
        # Strategy based when each of its sides are the same.
        if self._first_side == self._second_side == self._third_side:
            return EquilateralStrategy().get_triangle_type()
        # Strategy based when there are two sides that are the same.
        if self._first_side == self._second_side or self._second_side == self._third_side or self._third_side == self._first_side:
            return IsoscelesStrategy().get_triangle_type()
        # Strategy based when all of its sides are different.
        if self._first_side != self._second_side and self._first_side != self._third_side and self._second_side != self._third_side:
            return ScaleneStrategy().get_triangle_type()

# Reads each line of the file.
def tri_from_file(file_path):
    file = open(file_path, "r")
    line = file.readlines()[0]
    file.close()
    return TriangleContext(line).get_triangle_type_context()