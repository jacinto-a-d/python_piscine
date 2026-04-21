#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   creatures.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/21 15:28:32 by jabad-di            #+#    #+#            #
#   Updated: 2026/04/21 16:10:26 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex0.creature import Creature
from .capabilities import HealCapability, TransformCapability

class Sproutling(Creature, HealCapability):
    def __init__(self, name: str, creature_type: str) -> None:
        super().__init__(name, creature_type)

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"

    def attack(self) -> str:
        attack1: str = "Vine Whip"
        return f"{self.name} uses {attack1}"


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str, creature_type: str) -> None:
        super().__init__(name, creature_type)

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"

    def attack(self) -> str:
        attack1: str = "Petal Dance"
        return f"{self.name} uses {attack1}"


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, creature_type: str) -> None:
        super().__init__(name, creature_type)

    def heal(self) -> str:
        return f""

    def attack(self) -> str:
        pass


class Morphagon(Creature, TransformCapability):
    pass
