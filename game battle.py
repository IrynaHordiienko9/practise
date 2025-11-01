class Warrior:
    def __init__(self, health: int = 50, attack=5):
        self.health = health
        self.attack = attack

    @property
    def is_alive(self):
        return self.health > 0

    def receive_damage(self, damage: int) -> None:
        self.health -= damage


class Knight(Warrior):
    def __init__(self, health=50, attack=7):
        super().__init__(health, attack)


class Defender(Warrior):
    def __init__(self, health=60, attack=3, defense=2) -> None:
        super().__init__(health, attack)
        self.defense = defense

    def receive_damage(self, damage: int) -> None:
        damage_fact = damage - self.defense
        if damage_fact > 0:
            self.health -= damage_fact


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit_type, count):
        for _ in range(count):
            self.units.append(unit_type())


class Battle:
    def fight(self, army1: Army, army2: Army) -> bool:
        while army1.units and army2.units:
            unit1 = army1.units[0]
            unit2 = army2.units[0]
            res: bool = fight(unit1, unit2)
            if res:
                army2.units.pop(0)
            else:
                army1.units.pop(0)
        return len(army1.units) > 0


def fight(w1: Warrior, w2: Warrior) -> bool:
    while w1.is_alive and w2.is_alive:
        w2.receive_damage(w1.attack)
        if w2.is_alive:
            w1.receive_damage(w2.attack)
    return w1.is_alive


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")