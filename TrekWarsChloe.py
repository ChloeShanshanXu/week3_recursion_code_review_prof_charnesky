from enum import Enum

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