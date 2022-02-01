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
        expected_result = "<Alignment.us: 1>"

        # Act
        actual_result = at1

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_Alignment_them(self):
        # Arrange
        at2 = Alignment.them
        expected_result = "<Alignment.them: 2>"

        # Act
        actual_result = at2

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_Alignment_chaotic(self):
        # Arrange
        at3 = Alignment.chaotic
        expected_result = '<Alignment.chaotic: 3>'

        # Act
        actual_result = at3

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
        #Arrange
        range = 1
        my_ship = Ship("my ship", 0, 0, 1, 20, range, 10)
        target_ship = Ship("target ship", 3, 4, 2, 20, 5, 10)
        expected_result = False

        #Act
        actual_result = my_ship._is_in_range(target_ship)

        #Assert
        self.assertEqual(expected_result, actual_result)

    def test_get_current_health(self):
        # Arrange
        max_health=20
        my_ship = Ship("my ship", 0, 0, 1, max_health, 100, 10)
        expected_result = 20

        # Act
        actual_result = my_ship.get_current_health()

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_attack_success(self, target):
        #Arrange
        range = 100
        my_ship = Ship("my ship", 0, 0, 1, 20, range, 10)
        target_ship = Ship("target ship", 3, 4, 2, 20, 5, 10)
        expected_target_current_health = 10

        #Act
        my_ship._attack(target_ship)
        actual_target_current_health = target_ship.get_current_health()

        #Assert
        self.assertEqual(expected_target_current_health, actual_target_current_health)

    def test_attack_success_KO(self, target):
        #Arrange
        my_ship = Ship("my ship", 0, 0, 1, 20, 100, 10)
        target_ship = Ship("target ship", 3, 4, 2, 20, 5, 10)
        target_ship._current_health = 5

        #Act
        my_ship._attack(target_ship)

        #Assert
        self.assertRaises(ValueError, "Target K.O.")

    def test_attack_fail(self, target):
        # Arrange
        range = 1
        my_ship = Ship("my ship", 0, 0, 1, 20, range, 10)
        target_ship = Ship("target ship", 3, 4, 2, 20, 5, 10)

        # Act
        my_ship._attack(target_ship)

        # Assert
        self.assertRaises(ValueError, "Ship out of range")

    def test_get_type(self):
        # Arrange
        my_ship = Ship("my ship", 0, 0, 1, 20, 100, 10)
        expected_result= "<class '__main__.Ship'>"

        # Act
        actual_result=my_ship.get_type()

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_get_x(self):
        # Arrange
        my_ship = Ship("my ship", 0, 0, 1, 20, 100, 10)
        expected_result = 0

        # Act
        actual_result=my_ship.get_x()

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_get_y(self):
        # Arrange
        my_ship = Ship("my ship", 0, 0, 1, 20, 100, 10)
        expected_result = 0

        # Act
        actual_result=my_ship.get_y()

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_get_alignment(self):
        # Arrange
        my_ship = Ship("my ship", 0, 0, 1, 20, 100, 10)
        expected_result = 1

        # Act
        actual_result=my_ship.get_alignment()

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_status(self):
        # Arrange
        my_ship = Ship("my ship", 0, 0, 1, 20, 100, 10)
        expected_result = "my ship\ntype:<class '__main__.Ship'>\nhealth:20\nlocation:(0,0)"

        # Act
        actual_result=my_ship.status()

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_move_in_x(self, move_in_x):
        # Arrange
        my_ship = Ship("my ship", 0, 0, 1, 20, 100, 10)
        move_in_x = 3
        expected_x_location = 3

        # Act
        actual_x_location=my_ship._move_in_x(move_in_x)

        # Assert
        self.assertEqual(expected_x_location, actual_x_location)

    def test_move_in_y(self, move_in_y):
        # Arrange
        my_ship = Ship("my ship", 0, 0, 1, 20, 100, 10)
        move_in_y = -3
        expected_y_location = -3

        # Act
        actual_y_location=my_ship._move_in_y(move_in_y)

        # Assert
        self.assertEqual(expected_y_location, actual_y_location)

    def test_move(self, move_in_x, move_in_y):
        # Arrange
        my_ship = Ship("my ship", 0, 0, 1, 20, 100, 10)
        my_ship._current_health=10
        move_in_x = 3
        move_in_y = -3
        expected_x_location = 3
        expected_y_location = -3
        expected_current_health = 11

        # Act
        my_ship._move(move_in_x, move_in_y)
        actual_x_location = my_ship.get_x()
        actual_y_location = my_ship.get_y()
        actual_current_health = my_ship.get_current_health()

        # Assert
        self.assertEqual(expected_x_location, actual_x_location)
        self.assertEqual(expected_y_location, actual_y_location)
        self.assertEqual(expected_current_health, actual_current_health)

    def test_change_alignment_us_to_them(self):
        # Arrange
        my_ship = Ship("my ship", 0, 0, 1, 20, 100, 10)
        expected_result = 1

        # Act
        my_ship._change_alignment()
        actual_result = my_ship.get_alignment()

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_change_alignment_them_to_us(self):
        # Arrange
        my_ship = Ship("my ship", 0, 0, 1, 20, 100, 10)
        expected_result = 1

        # Act
        my_ship._change_alignment()
        actual_result = my_ship.get_alignment()

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_assess_damage(self, amount):
        # Arrange
        my_ship = Ship("my ship", 0, 0, 1, 20, 100, 10)
        amount = 5
        expected_result = 15

        # Act
        my_ship._assess_damage(amount)
        actual_result = my_ship.get_current_health()

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_assess_damage_health_low(self, amount):
        # Arrange
        my_ship = Ship("my ship", 0, 0, 1, 20, 100, 10)
        my_ship._current_health = 3
        amount = 5
        expected_result = 0

        # Act
        my_ship._assess_damage(amount)
        actual_result = my_ship.get_current_health()

        # Assert
        self.assertEqual(expected_result, actual_result)

class TestBattleship(TestCase):

    def test_battleship_get_torpedoes(self):
        return self._torpedoes
        # Arrange
        torpedoes = 3
        my_battleship = Battleship("my battleship", 0, 0, 1, 100, 10, 10, torpedoes)
        expected_result = 3

        # Act
        actual_result = my_ship.get_torpedoes()

        # Assert
        self.assertEqual(expected_result, actual_result)


    def test_battleship_move(self):
        # Arrange
        my_battleship = Battleship("my battleship", 0, 0, 1, 100, 10, 10, 3)
        expected_x_result = -1
        expected_y_result = -1

        # Act
        my_battleship._move()
        actual_x_result = my_battleship.get_x()
        actual_y_result = my_battleship.get_y()

        # Assert
        self.assertEqual(expected_x_result, actual_x_result)
        self.assertEqual(expected_y_result, actual_y_result)

    def test_battleship_attack(self, target):
        # Arrange
        torpedoes = 3
        my_battleship = Battleship("my battleship", 0, 0, 1, 100, 10, 10, torpedoes)
        target_ship = Ship("target ship", 3, 4, 2, 30, 5, 10)
        expected_torpedoes_result = 2
        expected_target_health = 10

        # Act
        my_battleship._attack(target_ship)
        actual_torpedoes_result = my_battleship.get_torpedoes()
        actual_target_health = target_ship.get_current_health()

        # Assert
        self.assertEqual(actual_torpedoes_result, expected_torpedoes_result)
        self.assertEqual(actual_target_health, expected_target_health)

    def test_battleship_status(self):
        super()._status
        print("torpedoes:" + str(self.get_torpedoes()))
        # Arrange
        my_battleship = Battleship("my battleship", 0, 0, 1, 100, 10, 10, 3)
        expected_result = "my battleship\ntype:<class '__main__.Battleship'>\nhealth:100\nlocation:(0,0)\ntorpdedoes: 3"

        # Act
        actual_result=my_battleship._status()

        # Assert
        self.assertEqual(expected_result, actual_result)

class TestCruiser(TestCase):

    def test_cruiser_move(self):
        # Arrange
        my_cruiser = Cruiser("my cruiser", 0, 0, 1, 50, 50, 5)
        expected_x_result = 1
        expected_y_result = 2

        # Act
        my_cruiser._move()
        actual_x_result = my_cruiser.get_x()
        actual_y_result = my_cruiser.get_y()

        # Assert
        self.assertEqual(expected_x_result, actual_x_result)
        self.assertEqual(expected_y_result, actual_y_result)


class TestCorvette(TestCase):
    def test_corvette_move(self):
        # Arrange
        my_corvette = Corvette("my corvette", 0, 0, 2, 20, 25)
        expected_x_result = 5
        expected_y_result = 5

        # Act
        my_corvette._move()
        actual_x_result = my_corvette.get_x()
        actual_y_result = my_corvette.get_y()

        # Assert
        self.assertEqual(expected_x_result, actual_x_result)
        self.assertEqual(expected_y_result, actual_y_result)

    def test_corvette_attack(self, target):
        # Arrange
        my_corvette = Corvette("my corvette", 0, 0, 2, 20, 25)
        target_ship = Ship("target ship", 3, 4, 1, 30, 5, 10)
        expected_result = 1

        # Act
        my_corvette._attack(target_ship)
        actual_result = target_ship.get_alignment()

        # Assert
        self.assertEqual(expected_result, actual_result)

class TestRepair(TestCase):
    def test_repair_attack(self, target):
        if self._alignment == target._alignment:
            target._current_health = target._max_health
        # Arrange
        my_repair = Repair("my repair", 0, 0, 1, 20, 25,5)
        target_ship = Ship("target ship", 3, 4, 1, 30, 5, 10)
        target_ship._current_health = 20
        expected_result = 30

        # Act
        my_repair._attack(target_ship)
        actual_result = target_ship.get_current_health()

        # Assert
        self.assertEqual(expected_result, actual_result)