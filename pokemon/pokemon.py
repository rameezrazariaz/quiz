class Pokemon:
    def __init__(self, name, level, typ, max_health, current_health, knocked_out):
        self.name = name
        self.level = level
        self.type = typ
        self.max_health = max_health
        self.current_health = current_health
        self.knocked_out = knocked_out

    def lose_health(self, damage):
        health_lost = damage
        self.current_health -= health_lost
        if self.current_health <= 0:
            self.is_knocked_out()
        else:
            print(
                "{} has lost {} health. It now has {} health left.".format(self.name, health_lost, self.current_health))

    def gain_health(self):
        health_gained = 30
        self.current_health += health_gained
        print("{} has gained {} health. It now has {} health".format(self.name, health_gained, self.current_health))

    def is_knocked_out(self):
        if self.current_health <= 0:
            print("{} has been knocked out.".format(self.name))

    def attack(self, other_pokemon):
        damage = 0
        if self.type == "Fire":
            if other_pokemon.type == "Grass":
                damage *= 2
            elif other_pokemon.type == "Water":
                damage /= 2
        elif self.type == "Grass":
            if other_pokemon.type == "Fire":
                damage /= 2
            elif other_pokemon.type == "Water":
                damage *= 2
        elif self.type == "Water":
            if other_pokemon.type == "Fire":
                damage *= 2
            elif other_pokemon.type == "Grass":
                damage /= 2

        other_pokemon.lose_health(damage)

class Trainer:
    def __init__(self, name, pokemons, potions, current_pokemon):
        self.name = name
        self.pokemons = pokemons
        self.potions = potions
        self.current_pokemon = current_pokemon
