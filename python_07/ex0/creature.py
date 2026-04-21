#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   creature.py                                          :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/20 22:03:20 by dipekko             #+#    #+#            #
#   Updated: 2026/04/21 13:21:31 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, creature_type: str) -> None:
        self.name: str = name
        self.creature_type: str = creature_type

    def describe(self) -> str:
        return f"{self.name} is a {self.creature_type} type Creature"

    @abstractmethod
    def attack(self) -> str:
        pass


class Flameling(Creature):
    def attack(self) -> str:
        attack_1: str = "Ember"
        return f"{self.name} uses {attack_1}!"


class Pyrodon(Creature):
    def attack(self) -> str:
        attack_1: str = "Flamethrower"
        return f"{self.name} uses {attack_1}!"


class Aquabub(Creature):
    def attack(self) -> str:
        attack_1: str = "Water Gun"
        return f"{self.name} uses {attack_1}!"


class Torragon(Creature):
    def attack(self) -> str:
        attack_1: str = "Hydro Pump"
        return f"{self.name} uses {attack_1}!"


class CreatureFactory(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling("Flameling", "Fire")

    def create_evolved(self) -> Creature:
        return Pyrodon("Pyrodon", "Fire/Flying")


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub("Aquabub", "Water")

    def create_evolved(self) -> Creature:
        return Torragon("Torragon", "Water")
