from unittest import TestCase

class Test(TestCase):

    def test_alignment(self):
        self.fail()

# test_ship(self):
        self.fail()

    def test_is_in_range_true(self, target):
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



# test_battleship(self):
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


# test_cruiser(self):

    def test_cruiser_move(self):
        move_in_x = 1
        move_in_y = 2
        super()._move(move_in_x, move_in_y)

# test_corvette(self):
    def test_corvette_move(self):
        move_in_x = 5
        move_in_y = 5
        super()._move(move_in_x, move_in_y)

    def test_corvette_attack(self, target):
        if self._alignment != target._alignment:
            target._alignment = self._alignment

# test_repair(self):
    def test_repair_attack(self, target):
        if self._alignment == target._alignment:
            target._current_health = target._max_health
