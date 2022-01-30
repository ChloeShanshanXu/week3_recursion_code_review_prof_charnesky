from enum import Enum
#code reference from: https://docs.python.org/3.11/howto/enum.html
class Alignment(Enum):
    us = 1
    them = 2
    chaotic = 3

class Ship:

    def __init__(self, name, x, y, alignment,max_health, range, attack_power):
        self._name = name
        self._x_location = x
        self._y_location = y
        self._alignment = alignment
        self._max_health = max_health
        self._range = range
        self._attack_power = attack_power
        self._current_health = self._max_health

    def _attack(self, target):
        if target _is_in_range:
            target._current_health -= self._attack_power
        else:
            raise ValueError("Ship out of range")

    def _is_in_range:
        dist = sqrt((self._x_location - target._x_location) ^ 2 + (self._y_location - target._y_location) ^ 2)
        if dist > range:
            return False
        else:
            return True