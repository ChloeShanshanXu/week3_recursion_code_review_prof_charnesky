from unittest import TestCase
from TrekWarsChloe import Alignment
from TrekWarsChloe import Ship
from TrekWarsChloe import Battleship
from TrekWarsChloe import Cruiser
from TrekWarsChloe import Corvette
from TrekWarsChloe import Repair

class TestAlignment(TestCase):

    def test_Alignment_us(self):
        # Arrange
        at1 = Alignment.us
        expected_result = 1

        # Act
        actual_result = at1

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_Alignment_them(self):
        # Arrange
        at2 = Alignment.them
        expected_result = 2

        # Act
        actual_result = at2

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_Alignment_chaotic(self):
        # Arrange
        at3 = Alighment.chaotic
        expected_result = 3

        # Act
        actual_result = Alignment.us

        # Assert
        self.assertEqual(expected_result, actual_result)

class TestShip(TestCase):

    def test_is_in_range_true(self, target):
        #Arrange
        range = 100
        my_ship = Ship("my ship", 0, 0, 1, 20, range, 10)
        target_ship = Ship("target ship", 3, 4, 2, 20, 5, 10)
        expected_result = True

        #Act
        actual_result = my_ship._is_in_range(target_ship)

        #Assert
        self.assertEqual(expected_result, actual_result)

    def test_is_in_range_false(self, target):
        dist = sqrt((self._x_location - target._x_location) ^ 2 + (self._y_location - target._y_location) ^ 2)
        if dist > range:
            return False
        else:
            return True

    def test_attack_success(self, target):
        if (self._alignment != target._alignment) or self._alignment == Alignment.chaotic:
            if self._is_in_range:
                target._current_health -= self._attack_power
                if target._current_health < 0:
                    target._current_health = 0
                    print ("Target K.O.")
    def test_attack_success_KO(self, target):
    def test_attack_fail(self, target):
                raise ValueError("Ship out of range")

    def test_get_type(self):
        return type(self)

    def test_get_x(self):
        return self._x_location

    def test_get_y(self):
        return self._y_location

    def test_get_alignment(self):
        return self._alignment

    def test_status(self):
        return "{}\n type:{}\n health:{}\n location:({},{})".format(self.name, \
        type(self),self._current_health, self._x_location, self._y_location)

    def test_move_in_x(self, move_in_x):
        self._x_location += move_in_x

    def test_move_in_y(self, move_in_y):
        self._y_location += move_in_y

    def test_move(self, move_in_x=1, move_in_y=1):
        self._move_in_x
        self._move_in_y
        if self._current_health < self._max_health:
            self._current_health += 1

    def test_change_alignment_us_to_them(self):
    def test_change_alignment_them_to_us(self):
        if self._alignment == Alignment.us:
            self._alignment = Alignment.them
        elif self._alignment == Alignment.them:
            self._alignment = Alignment.us

    def test_assess_damage(self, amount):
        self._current_health -= amount
        if self._current_health < 0:
            self._current_health = 0

    def test_assess_damage_health_low(self, amount):

class TestBattleship(TestCase):
    def test_battleship_get_torpedoes(self):
        return self._torpedoes


    def test_battleship_move(self):
        move_in_x = -1
        move_in_y = -1
        super()._move(move_in_x, move_in_y)


    def test_battleship_attack(self, target):
        if self._torpedoes > 0:
            target._current_health -= 10
            self._torpedoes -= 1
        super()._attack()


    def test_battleship_status(self):
        super()._status
        print("torpedoes:" + str(self.get_torpedoes()))


class TestCruiser(TestCase):

    def test_cruiser_move(self):
        move_in_x = 1
        move_in_y = 2
        super()._move(move_in_x, move_in_y)

class TestCorvette(TestCase):
    def test_corvette_move(self):
        move_in_x = 5
        move_in_y = 5
        super()._move(move_in_x, move_in_y)

    def test_corvette_attack(self, target):
        if self._alignment != target._alignment:
            target._alignment = self._alignment

class TestRepair(TestCase):
    def test_repair_attack(self, target):
        if self._alignment == target._alignment:
            target._current_health = target._max_health
