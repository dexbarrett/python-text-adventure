class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0

    def status_text(self):
        if self.is_alive():
            return self.alive_text

        return self.dead_text



class GiantSpider(Enemy):
    def __init__(self):
        self.name = "Giant Spider"

        self.hp = 10

        self.damage = 2

        self.alive_text = "A giant spider jumps down from " \
            "its web in front of you!"

        self.dead_text = "The corpse of a dead spider " \
            "rots on the ground."

class Ogre(Enemy):
    def __init__(self):
        self.name = "Ogre"
        self.hp = 30
        self.damage = 10

        self.alive_text = "An ogre is blocking your path!"

        self.dead_text = "A dead ogre reminds you of your triumph."


class BatColony(Enemy):
    def __init__(self):
        self.name = "Colony of Bats"
        self.hp = 100
        self.damage = 4

        self.alive_text = "You hear a squeaking noise growing louder" \
            "...suddenly you are lost in s swarm of bats!"

        self.dead_text = "Dozens of dead bats are scattered on the ground."


class RockMonster(Enemy):
    def __init__(self):
        self.name = "Rock Monster"
        self.hp = 80
        self.damage = 15

        self.alive_text = "You've disturbed a rock monster " \
            "from his slumber!"

        self.dead_text = "Defeated, the monster has reverted " \
            "into an ordinary rock."
