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
        if (self._alignment != target._alignment) or self._alignment == Alignment.chaotic:
            if self._is_in_range:
                target._current_health -= self._attack_power
            else:
                raise ValueError("Ship out of range")

    def _is_in_range(self, target):
        dist = sqrt((self._x_location - target._x_location) ^ 2 + (self._y_location - target._y_location) ^ 2)
        if dist > range:
            return False
        else:
            return True

    def get_type(self):
        return type(self)

    def get_x(self):
        return self._x_location

    def get_y(self):
        return self._y_location

    def get_alignment(self):
        return self._alignment

    def status(self):
        return "{}\n type:{}\n health:{}\n location:({},{})".format(self.name, \
        type(self),self._current_health, self._x_location, self._y_location)
        if self.get_type == "Battleship":
            return "torpedoes: " + self.get_torpedoes

    def _move(self):
        move_in_x = 1
        move_in_y = 1
        self._move_in_x
        self._move_in_y
        if self._current_health < self._max_health:
            self._current_health += 1

    def _move_in_x(self, move_in_x):
        self._x_location += move_in_x

    def _move_in_y(self, move_in_y):
        self._y_location += move_in_y

    def _change_alignment(self):
        if self._alignment == Alignment.us:
            self._alignment = Alignment.them
        elif self._alignment == Alignment.them:
            self._alignment = Alignment.us

    def _assess_damage(self, amount):
        self._current_health -= amount
        if self._current_health < 0:
            self._current_health = 0

get_torpedoes